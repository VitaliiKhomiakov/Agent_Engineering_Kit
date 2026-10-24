"""Fixed instruction-only adoption scenarios, not an installer or client eval."""

import hashlib
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import tomllib
import unittest

from tests.test_project_skill_adoption import ROOT, adapt_document
from tools.check_instruction_artifacts import Checker


SKILLS = ("aek-design-feature", "aek-review-changes")
ROLE_FILES = ("af-architect.toml", "af-implementer.toml", "af-reviewer.toml")
TASK = ".work/items/feature.md"
# Reviewed conditional host/framework links; never treat every missing route as optional.
OPTIONAL_STACK_ROUTES = frozenset({
    "standards/nodejs.md", "standards/nextjs-framework.md", "standards/nextjs-feature-structure.md",
    "standards/nextjs/verification-migration.md", "standards/angular.md", "standards/react.md",
    "standards/ngrx.md", "standards/ngrx/state-architecture.md", "standards/ngrx/entity-router.md",
    "standards/ngrx/effects.md", "standards/ngrx/verification.md",
})
LOCAL_FILES = {
    "ARCHITECTURE.md": "# Fixture passport\n\nInstruction-only project; no runtime claim.\n"
    "Canonical task: `.work/items/feature.md`. Local gate: `fixture-local-gate`.\n",
    "LOCAL_RULES.md": "# Local contracts\n\nPreserve the existing task store.\n"
    "Accepted exception E1: retain the fixture's existing compatibility interface.\n"
    "Future implementation requires `fixture-local-gate`; importing instructions does not run it.\n",
    TASK: "# Existing canonical task\n\n- [ ] LOCAL-1: Preserve the existing task and exception E1.\n",
    ".codex/config.toml": '# Existing fixture choice; preserve comment and values.\n'
    'model = "gpt-6-astra"\nmodel_reasoning_effort = "high"\n',
    ".agents-framework/policy.toml": 'schema_version = 1\n[review]\nindependent = "on_request"\n',
}


def snapshot(root: Path) -> dict[str, tuple[str, int]]:
    """Include directory mtimes so prepare/no-op cannot create hidden paths."""
    if not root.exists():
        return {}
    return {p.relative_to(root).as_posix(): (
        hashlib.sha256(p.read_bytes()).hexdigest() if p.is_file() else "directory",
        p.stat().st_mtime_ns,
    ) for p in (root, *sorted(root.rglob("*")))}


def write_fixture(root: Path, files: dict[str, bytes]) -> None:
    """Write an explicitly constructed test fixture, never infer ownership/actions."""
    for relative, contents in files.items():
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(contents)


def portable_candidate(profiles: tuple[str, ...], bundle_dir: str, *,
                       client: str = "codex",
                       roles: tuple[str, ...] = ("architect", "implementer", "reviewer"),
                       pairs: dict[str, tuple[str, str]] | None = None) -> dict[str, bytes]:
    """Render known fixture inputs in memory; no target reads/writes or merge logic."""
    target = Path("/tmp/aek-virtual-target")
    bundle = target / bundle_dir
    prefix = "" if bundle_dir == "." else bundle_dir + "/"
    checker = Checker(ROOT)
    selection = checker.catalog_selection((*profiles, "project-workflows"))
    if checker.diagnostics:
        raise ValueError(str(checker.diagnostics))
    selected = set(selection.bundle_files)
    source_references = frozenset(path.relative_to(ROOT).as_posix() for path in selection.source_files)
    optional_references = source_references | OPTIONAL_STACK_ROUTES
    native_skills = SKILLS if client == "codex" else ()
    result: dict[str, bytes] = {}
    for source in sorted(selected):
        relative = source.relative_to(ROOT).as_posix()
        destination = bundle / relative
        result[prefix + relative] = (
            adapt_document(source, destination, bundle, selected,
                           source.read_text(encoding="utf-8"), optional_references).encode()
            if source.suffix in {".md", ".mdc"} else source.read_bytes())

    for template, filename, heading in (("policy-entry.md", "AGENTS.md", "Reasoning and communication language"),
                                         ("PLANS.md", "PLANS.md", "Language")):
        source = ROOT / "templates" / template
        text = "# Fixture instructions\n\n## " + heading + source.read_text().split("## " + heading, 1)[1]
        text = text.replace("$projects", f"Instruction root: this project. Passport: `ARCHITECTURE.md`.\n"
                            f"Canonical task: `{TASK}`. Preserve [local contracts](LOCAL_RULES.md).")
        # LOCAL_RULES is a fixture-local route, not a source-template reference.
        text = text.replace("[local contracts](LOCAL_RULES.md)", "`LOCAL_RULES.md`")
        text = text.replace("<actual installed task skill paths>", ", ".join(
            f".agents/skills/{name}/SKILL.md" for name in native_skills) or
            "none; use the adopted local project-skill contract")
        text = text.replace("<actual installed or accessible source skill path>",
                            "separately identified source; integration is not installed here")
        text = text.replace("Remove this optional route when that profile is omitted; direct rules remain usable.\n", "")
        text = adapt_document(source, target / filename, bundle, selected, text, optional_references)
        text = text.replace("$routes", "\n".join(
            f"- [{name}]({prefix}standards/{name}.md)" for name in profiles))
        # Only bundle-owned literal prefixes change; metadata paths stay root-relative.
        for directory in ("standards", "templates"):
            text = text.replace(f".agents-framework/{directory}/", f"{prefix}{directory}/")
        result[filename] = text.encode()

    for name in native_skills:
        source = ROOT / "templates/skills" / name / "SKILL.md"
        destination = target / ".agents/skills" / name / "SKILL.md"
        result[destination.relative_to(target).as_posix()] = adapt_document(
            source, destination, bundle, selected, source.read_text(), optional_references).encode()
    # Separate syntax fixtures: reference resolution only, not client activation.
    if client == "claude":
        result["CLAUDE.md"] = (ROOT / "templates/claude/policy-bridge.md").read_bytes()
    for role in roles:
        suffix = "toml" if client == "codex" else "md"
        filename = f"af-{role}.{suffix}"
        text = (ROOT / f"templates/{client}/agents" / filename).read_text().replace(
            ".agents-framework/templates/", prefix + "templates/")
        # Fixed fixture assignments, not discovery, schema validation or an installer.
        if pairs is not None:
            model, effort = pairs[role]
            if client == "codex":
                text = re.sub(r'^model = .*$', f'model = "{model}"', text, flags=re.MULTILINE)
                text = re.sub(r'^model_reasoning_effort = .*$',
                              f'model_reasoning_effort = "{effort}"', text, flags=re.MULTILINE)
            elif client == "claude":
                text = re.sub(r'^model: .*$', f'model: {model}', text, flags=re.MULTILINE)
                text = re.sub(r'^effort: .*$', f'effort: {effort}', text, flags=re.MULTILINE)
            else:
                text = re.sub(r'^model: .*$', f'model: {model}[effort={effort}]', text, flags=re.MULTILINE)
        result[f".{client}/agents/{filename}"] = text.encode()
    return result


class ProjectSkillPortabilityChecks(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory(prefix="aek-portability-")
        self.addCleanup(temporary.cleanup)
        self.workspace = Path(temporary.name)
        self.root = self.workspace / "independently-opened-child"

    def check_bundle(self, profiles: tuple[str, ...], layout: str) -> None:
        args = [sys.executable, "-B", str(ROOT / "tools/check_instruction_artifacts.py"),
                "--root", str(self.root), "--bundle-dir", layout]
        for profile in (*profiles, "project-workflows"):
            args.extend(("--profile", profile))
        native = [f".agents/skills/{name}/SKILL.md" for name in SKILLS]
        for paths in ([], [*native, *(f".codex/agents/{name}" for name in ROLE_FILES)]):
            result = subprocess.run([*args, *paths], cwd=self.workspace, capture_output=True,
                                    text=True, timeout=20, check=False)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_layouts_stacks_and_independent_child_routes(self) -> None:
        cases = (("fastapi",), ("react", "typescript"), ("angular",), ("angular", "ngrx"),
                 ("go",), ("godot",))
        for layout in (".agents-framework", ".", "rules/aek"):
            for profiles in cases:
                with self.subTest(layout=layout, profiles=profiles), tempfile.TemporaryDirectory(
                        dir=self.workspace, prefix="case-") as directory:
                    self.root = Path(directory) / "child"
                    local = {name: text.encode() for name, text in LOCAL_FILES.items()}
                    write_fixture(self.root, local)
                    before = snapshot(self.root)
                    candidate = portable_candidate(profiles, layout)
                    self.assertEqual(snapshot(self.root), before)
                    self.assertTrue(set(local).isdisjoint(candidate))
                    write_fixture(self.root, candidate)
                    self.check_bundle(profiles, layout)
                    for name in local:
                        self.assertEqual(snapshot(self.root)[name], before[name])
                    for name in SKILLS:
                        native = self.root / ".agents/skills" / name / "SKILL.md"
                        guide = re.search(r"\[project-skill contract\]\(([^)]+)\)", native.read_text())
                        assert guide is not None
                        resolved = (native.parent / guide[1]).resolve()
                        self.assertTrue(resolved.is_relative_to(self.root.resolve()))
                        self.assertEqual(resolved, (self.root / layout / "standards/project-skills.md").resolve())
                    self.assertFalse((self.root / "MIGRATION.md").exists())
                    self.assertFalse((self.root / "docs/plans").exists())
                    self.assertFalse((self.root / layout / "standards/nextjs-framework.md").exists())

    def test_non_markdown_routes_and_native_literals(self) -> None:
        for layout in (".agents-framework", ".", "rules/aek"):
            with self.subTest(layout=layout):
                candidate = portable_candidate(("fastapi",), layout)
                claude = portable_candidate(("fastapi",), layout, client="claude")
                for line in claude["CLAUDE.md"].decode().splitlines():
                    if line.startswith("@"):
                        self.assertIn(line[1:], claude)
                plans = candidate["PLANS.md"].decode()
                routes = re.findall(r"`([^`]+/standards/[^`]+\.md|standards/[^`]+\.md)`", plans)
                self.assertGreaterEqual(len(routes), 6)
                for route in routes:
                    self.assertIn(route, candidate)
                for filename in ROLE_FILES:
                    role = tomllib.loads(candidate[f".codex/agents/{filename}"].decode())
                    original = tomllib.loads((ROOT / "templates/codex/agents" / filename).read_text())
                    for key in original.keys() - {"developer_instructions"}:
                        self.assertEqual(role[key], original[key], (filename, key))
                    role_routes = re.findall(r"[\w./-]*templates/agents/[\w/-]+\.md", str(role["developer_instructions"]))
                    self.assertTrue(role_routes, filename)
                    for route in role_routes:
                        self.assertIn(route, candidate, filename)
                entry = candidate["AGENTS.md"].decode()
                self.assertNotIn("<actual", entry)
                self.assertNotIn("$routes", entry)
                self.assertIn(TASK, entry)

    def test_prepare_does_not_create_a_missing_target(self) -> None:
        before = snapshot(self.workspace)
        portable_candidate(("fastapi",), ".agents-framework")
        self.assertFalse(self.root.exists())
        self.assertEqual(snapshot(self.workspace), before)

    def test_candidate_repeat_is_identical_without_target_rewrites(self) -> None:
        candidate = portable_candidate(("fastapi",), ".agents-framework")
        write_fixture(self.root, candidate)
        before = snapshot(self.root)
        repeated = portable_candidate(("fastapi",), ".agents-framework")
        self.assertEqual(candidate, repeated)
        self.assertEqual(snapshot(self.root), before)


if __name__ == "__main__":
    unittest.main()
