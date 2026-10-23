"""Exercise offline saved-selection agreement through disposable native files."""

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


REPOSITORY = Path(__file__).resolve().parents[1]
CHECKER = REPOSITORY / "tools/check_model_routing.py"
ROUTING = '''schema_version = 2
status = "configured"
scope = "workspace"
client = "codex"
max_subagents = 2
[orchestration]
mode = "delegated"
allowed_edges = ["orchestrator->implementer", "orchestrator->reviewer"]
[roles.orchestrator]
enabled = true
model = "main-model"
reasoning_effort = "high"
[roles.implementer]
enabled = true
model = "worker-model"
reasoning_effort = "medium"
[roles.reviewer]
enabled = true
model = "review-model"
reasoning_effort = "high"
'''
CONFIG = '''model = "main-model"
model_reasoning_effort = "high"
unrelated_setting = "preserve"
[agents]
enabled = true
max_concurrent_threads_per_session = 2
default_subagent_model = "worker-model"
default_subagent_reasoning_effort = "medium"
'''


class ModelRoutingChecks(unittest.TestCase):
    def setUp(self) -> None:
        directory = tempfile.TemporaryDirectory(prefix="aek-routing-test-")
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        self.write(".agents-framework/model-routing.toml", ROUTING)
        self.write(".codex/config.toml", CONFIG)
        self.role("implementer", "worker-model", "medium")
        self.role("reviewer", "review-model", "high")

    def write(self, name: str, text: str) -> None:
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def role(self, name: str, model: str, effort: str) -> None:
        self.write(f".codex/agents/af-{name}.toml", f'name = "af-{name}"\n'
                   f'description = "Bounded role"\nmodel = "{model}"\n'
                   f'model_reasoning_effort = "{effort}"\n'
                   'developer_instructions = "Follow supplied task scope."\n')

    def run_checker(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run([sys.executable, "-B", str(CHECKER), "--root", str(self.root), *args],
                              text=True, capture_output=True, check=False, timeout=15)

    def failure(self, fragment: str, *args: str) -> None:
        result = self.run_checker(*args)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn(fragment, result.stdout + result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_agreement_is_read_only_and_not_runtime_proof(self) -> None:
        before = {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        result = self.run_checker("--default-role", "implementer")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("runtime", result.stdout)
        self.assertEqual(before, {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()})

    def test_main_pair_and_ceiling_must_match(self) -> None:
        for old, new, fragment in [('"main-model"', '"wrong"', "model"),
                                   ('max_concurrent_threads_per_session = 2',
                                    'max_concurrent_threads_per_session = 3', "ceiling"),
                                   ('enabled = true', 'enabled = false', "agents.enabled")]:
            with self.subTest(fragment=fragment):
                self.write(".codex/config.toml", CONFIG.replace(old, new))
                self.failure(fragment)

    def test_role_override_and_missing_role_fail(self) -> None:
        self.role("implementer", "wrong", "medium")
        self.failure("af-implementer")
        (self.root / ".codex/agents/af-implementer.toml").unlink()
        self.failure("af-implementer")

    def test_required_native_metadata_is_validated(self) -> None:
        self.write(".codex/agents/af-reviewer.toml", 'name = "af-reviewer"\n')
        self.failure("description")

    def test_worker_defaults_need_explicit_mapping(self) -> None:
        self.write(".codex/config.toml", CONFIG.replace('"worker-model"', '"other-default"'))
        result = self.run_checker()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("defaults not compared", result.stdout)
        self.failure("default_subagent_model", "--default-role", "implementer")
        self.failure("enabled specialist", "--default-role", "absent")

    def test_graph_errors_fail(self) -> None:
        valid = '["orchestrator->implementer", "orchestrator->reviewer"]'
        cases = [('[' + '"orchestrator->implementer", ' * 2 + '"orchestrator->reviewer"]', "duplicate"),
                 ('["orchestrator->absent"]', "enabled"),
                 ('["implementer->implementer"]', "self"),
                 ('["orchestrator->implementer", "implementer->orchestrator"]', "cycle"),
                 ('["implementer->reviewer"]', "unreachable"),
                 ('["orchestrator ->reviewer"]', "edge")]
        for edges, fragment in cases:
            with self.subTest(edges=edges):
                self.write(".agents-framework/model-routing.toml", ROUTING.replace(valid, edges))
                self.failure(fragment)

    def test_valid_nested_graph_checks_agreement_without_claiming_enforcement(self) -> None:
        self.write(".agents-framework/model-routing.toml", ROUTING.replace(
            '"orchestrator->reviewer"', '"implementer->reviewer"'))
        result = self.run_checker()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("not verified", result.stdout)

    def test_orphan_role_has_no_implicit_edge(self) -> None:
        self.write(".agents-framework/model-routing.toml", ROUTING.replace(', "orchestrator->reviewer"', ''))
        result = self.run_checker()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_native_integer_and_boolean_types_are_not_coerced(self) -> None:
        for old, new, fragment in [('max_concurrent_threads_per_session = 2',
                                    'max_concurrent_threads_per_session = true', "native ceiling"),
                                   ('enabled = true', 'enabled = 1', "agents.enabled")]:
            with self.subTest(new=new):
                self.write(".codex/config.toml", CONFIG.replace(old, new))
                self.failure(fragment)

    def test_disabled_role_must_not_remain_discoverable(self) -> None:
        disabled = ROUTING.replace(', "orchestrator->reviewer"', '').replace(
            '[roles.reviewer]\nenabled = true', '[roles.reviewer]\nenabled = false')
        self.write(".agents-framework/model-routing.toml", disabled)
        self.failure("disabled")
        (self.root / ".codex/agents/af-reviewer.toml").unlink()
        result = self.run_checker()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_duplicate_name_in_other_file_is_reported(self) -> None:
        self.write(".codex/agents/duplicate.toml", (self.root / ".codex/agents/af-reviewer.toml").read_text())
        self.failure("duplicate")

    def test_unrelated_custom_role_is_preserved(self) -> None:
        self.write(".codex/agents/custom.toml", 'name = "custom"\ndescription = "Local role"\n'
                   'developer_instructions = "Use local policy."\n')
        self.assertEqual(self.run_checker().returncode, 0)

    def test_single_agent_ignores_inactive_positive_native_defaults(self) -> None:
        single = ROUTING.split("[roles.implementer]")[0].replace('max_subagents = 2', 'max_subagents = 0').replace(
            'mode = "delegated"', 'mode = "single-agent"').replace(
            '["orchestrator->implementer", "orchestrator->reviewer"]', '[]')
        self.write(".agents-framework/model-routing.toml", single)
        self.write(".codex/config.toml", CONFIG.replace('enabled = true', 'enabled = false'))
        # Unrecorded custom definitions are outside ownership, inactive by mode.
        self.assertEqual(self.run_checker().returncode, 0)
        self.write(".codex/config.toml", CONFIG)
        self.failure("agents.enabled")

    def test_unconfigured_legacy_and_other_clients_are_inconclusive(self) -> None:
        for old, new in [('status = "configured"', 'status = "unconfigured"'),
                         ('schema_version = 2', 'schema_version = 1'),
                         ('schema_version = 2', 'schema_version = 999'),
                         ('client = "codex"', 'client = "cursor"')]:
            with self.subTest(new=new):
                self.write(".agents-framework/model-routing.toml", ROUTING.replace(old, new))
                result = self.run_checker()
                self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
                self.assertIn("not evaluated", result.stdout + result.stderr)

    def test_mode_and_coordinator_invariants(self) -> None:
        for old, new, fragment in [
                ('max_subagents = 2', 'max_subagents = 0', "positive ceiling"),
                ('mode = "delegated"', 'mode = "single-agent"', "single-agent mode requires"),
                ('mode = "delegated"', 'mode = "unknown"', "orchestration.mode"),
                ('[roles.orchestrator]\nenabled = true', '[roles.orchestrator]\nenabled = false',
                 "roles.orchestrator: must be enabled"),
                ('reasoning_effort = "high"', 'reasoning_effort = ""', "roles.orchestrator.reasoning_effort")]:
            with self.subTest(new=new):
                # Only the first occurrence: the orchestrator's effort, not the reviewer's.
                self.write(".agents-framework/model-routing.toml", ROUTING.replace(old, new, 1))
                self.failure(fragment)

    def test_malformed_types_and_incomplete_config_fail_cleanly(self) -> None:
        for old, new, fragment in [('max_subagents = 2', 'max_subagents = true', "max_subagents"),
                                   ('enabled = true', 'enabled = "true"', "roles.orchestrator.enabled"),
                                   ('schema_version = 2', 'schema_version = "2"', "schema_version"),
                                   ('model = "main-model"', 'model = ""', "roles.orchestrator.model"),
                                   ('[orchestration]', '[wrong]', "orchestration: expected a table")]:
            with self.subTest(new=new):
                self.write(".agents-framework/model-routing.toml", ROUTING.replace(old, new))
                self.failure(fragment)

    def test_missing_record_and_native_ceiling_are_not_evaluated(self) -> None:
        cases = [(".agents-framework/model-routing.toml", None, "model-routing.toml is missing"),
                 (".codex/config.toml", CONFIG.replace("max_concurrent_threads_per_session = 2\n", ""),
                  "native ceiling agreement not evaluated")]
        for name, replacement, fragment in cases:
            with self.subTest(name=name):
                self.setUp()
                if replacement is None:
                    (self.root / name).unlink()
                else:
                    self.write(name, replacement)
                result = self.run_checker()
                self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
                self.assertIn(fragment, result.stdout)
                self.assertNotIn("Traceback", result.stderr)

    def test_absent_native_ceiling_does_not_mask_definite_conflicts(self) -> None:
        self.write(".codex/config.toml", CONFIG.replace("max_concurrent_threads_per_session = 2\n", ""))
        self.role("implementer", "wrong", "medium")
        self.failure("af-implementer")
        self.role("implementer", "worker-model", "medium")
        self.failure("enabled specialist", "--default-role", "absent")
        result = self.run_checker()
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        self.assertIn("native ceiling agreement not evaluated", result.stdout)

    def test_shipped_templates_agree_once_selected(self) -> None:
        # Copies only; the source template stays unconfigured and inactive.
        routing = (REPOSITORY / "templates/framework/model-routing.toml").read_text(encoding="utf-8")
        self.assertIn('status = "unconfigured"', routing)
        for name in (".codex/agents/af-implementer.toml", ".codex/agents/af-reviewer.toml"):
            (self.root / name).unlink()
        self.write(".agents-framework/model-routing.toml",
                   routing.replace('status = "unconfigured"', 'status = "configured"'))
        for name in ("config.toml", "agents/af-implementer.toml"):
            self.write(f".codex/{name}", (REPOSITORY / "templates/codex" / name).read_text(encoding="utf-8"))
        for args in ((), ("--default-role", "implementer")):
            with self.subTest(args=args):
                result = self.run_checker(*args)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_missing_and_malformed_files_fail_cleanly(self) -> None:
        self.write(".codex/config.toml", '[broken')
        self.failure("config.toml")
        (self.root / ".codex/config.toml").unlink()
        self.failure("config.toml")

    def test_bundle_or_native_symlink_escape_fails(self) -> None:
        with tempfile.TemporaryDirectory(prefix="aek-routing-outside-") as directory:
            outside = Path(directory) / "config.toml"
            outside.write_text(CONFIG)
            native = self.root / ".codex/config.toml"
            native.unlink()
            native.symlink_to(outside)
            self.failure("outside root")

    def test_routing_symlink_escape_fails(self) -> None:
        with tempfile.TemporaryDirectory(prefix="aek-routing-outside-") as directory:
            outside = Path(directory) / "routing.toml"
            outside.write_text(ROUTING)
            routing = self.root / ".agents-framework/model-routing.toml"
            routing.unlink()
            routing.symlink_to(outside)
            self.failure("outside root")


if __name__ == "__main__":
    unittest.main()
