"""Exercise the checker CLI against disposable instruction bundles."""

from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


CHECKER = Path(__file__).resolve().parents[1] / "tools/check_instruction_artifacts.py"
CATALOG = '''schema_version = 1
assets = ["standards/catalog.toml"]
templates = {entry = "templates/policy-entry.md"}

[[profiles]]
id = "core"
source = "standards/core.md"
required = true

[[profiles]]
id = "python"
source = "standards/python.md"
resources = ["standards/details.md"]
dependencies = ["core"]

[[profiles]]
id = "optional"
source = "standards/optional.md"
'''

# Independent fixture values, not a source of operational policy defaults.
POLICY = '''schema_version = 1
[verification]
timing = "phase_end"
diagnostic_reset_after_stalled_attempts = 2
[review]
independent = "risk_based"
[size]
function_review_lines = 50
class_review_lines = 400
file_review_lines = 500
growth_review_from_lines = 600
documented_review_above_lines = 700
react_component_review_lines = 250
[instructions]
root_guideline_lines = [40, 70]
local_guideline_lines = [10, 25]
'''


class ArtifactChecks(unittest.TestCase):
    def setUp(self) -> None:
        directory = tempfile.TemporaryDirectory(prefix="aek-check-test-")
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        self.write("standards/catalog.toml", CATALOG)
        self.write("standards/core.md", "# Core\n\n## Rules\n")
        self.write("standards/python.md", "# Python\n[Details](details.md#details)\n")
        self.write("standards/details.md", "# Details\n")
        self.write("standards/optional.md", "# Optional\n")
        self.write("templates/policy-entry.md", "[Rules](standards/core.md#rules)\n")

    def write(self, name: str, text: str) -> None:
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def run_checker(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, "-B", str(CHECKER), "--root", str(self.root), *args],
            text=True, capture_output=True, check=False, timeout=15,
        )

    def assert_failure(self, result: subprocess.CompletedProcess[str], text: str) -> None:
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn(text, result.stdout + result.stderr)

    def test_valid_source_resolves_installed_template_base(self) -> None:
        self.write("docs/old.md", "[Historical missing](absent.md)\n")
        result = self.run_checker()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_missing_catalog_resource_fails_even_with_explicit_paths(self) -> None:
        (self.root / "standards/details.md").unlink()
        result = self.run_checker("standards/core.md")
        self.assert_failure(result, "missing resource")
        self.assertRegex(result.stdout + result.stderr, r"standards/catalog.toml:\d+:")

    def test_bad_fragment_reports_link_location(self) -> None:
        self.write("standards/python.md", "# Python\n[Wrong](core.md#absent)\n")
        result = self.run_checker()
        self.assert_failure(result, "missing fragment")
        self.assertIn("standards/python.md:2:", result.stdout + result.stderr)

    def test_duplicate_ids_fail(self) -> None:
        self.write("standards/catalog.toml", CATALOG.replace('id = "optional"', 'id = "core"'))
        self.assert_failure(self.run_checker(), "duplicate profile")

    def test_dependency_cycle_fails(self) -> None:
        self.write("standards/catalog.toml", CATALOG.replace(
            "required = true", 'required = true\ndependencies = ["python"]',
        ))
        self.assert_failure(self.run_checker(), "dependency cycle")

    def test_unknown_dependency_fails(self) -> None:
        self.write("standards/catalog.toml", CATALOG.replace(
            'dependencies = ["core"]', 'dependencies = ["unknown"]',
        ))
        self.assert_failure(self.run_checker(), "unknown dependency")

    def test_selected_bundle_omits_unselected_files_and_source_history(self) -> None:
        (self.root / "standards/optional.md").unlink()
        (self.root / "templates/policy-entry.md").unlink()
        self.write("standards/python.md", "# Python\nSource research: docs/research/old.md (not bundled).\n")
        result = self.run_checker("--profile", "python", "--profile", "core")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_selected_bundle_still_rejects_dangling_history_link(self) -> None:
        self.write("standards/python.md", "[Research](../docs/research/old.md)\n")
        self.assert_failure(self.run_checker("--profile", "python"), "missing link target")

    def test_selected_bundle_checks_adapted_root_entry(self) -> None:
        self.write("AGENTS.md", "[Route](standards/missing.md)\n")
        self.assert_failure(self.run_checker("--profile", "python"), "missing link target")

    def test_required_profile_and_transitive_resource_are_not_optional(self) -> None:
        for missing in ("standards/core.md", "standards/details.md"):
            with self.subTest(missing=missing):
                path = self.root / missing
                content = path.read_text(encoding="utf-8")
                path.unlink()
                self.assert_failure(self.run_checker("--profile", "python"), "missing resource")
                self.write(missing, content)

    def test_unknown_selected_profile_fails(self) -> None:
        self.assert_failure(self.run_checker("--profile", "typo"), "unknown profile")

    def test_explicit_history_path_is_checked_but_scoped_prose_is_not_expanded(self) -> None:
        self.write("docs/old.md", "[Missing](absent.md)\n")
        self.write("README.md", "[Also missing](absent.md)\n")
        result = self.run_checker("standards/core.md")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assert_failure(self.run_checker("docs/old.md"), "missing link target")

    def test_code_samples_do_not_create_links_or_heading_anchors(self) -> None:
        self.write("standards/details.md", "# Details\n````md\n```\n# Fake\n[x](missing.md)\n````\n`[x](missing.md)`\n")
        result = self.run_checker()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.write("standards/python.md", "[Fake](details.md#fake)\n")
        self.assert_failure(self.run_checker(), "missing fragment")

    def test_unclosed_fence_fails_at_its_opening_line(self) -> None:
        self.write("standards/details.md", "# Details\n~~~~python\n~~~\n")
        result = self.run_checker()
        self.assert_failure(result, "unclosed fence")
        self.assertIn("standards/details.md:2:", result.stdout + result.stderr)

    def test_wrapped_link_labels_resolve_and_keep_start_line(self) -> None:
        self.write("standards/details.md", "# Details\n[Core\nrules](core.md#rules)\n")
        result = self.run_checker()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.write("standards/details.md", "# Details\n[Core\nrules](core.md#missing)\n")
        result = self.run_checker()
        self.assert_failure(result, "missing fragment")
        self.assertIn("standards/details.md:2:", result.stdout + result.stderr)

    def test_duplicate_heading_and_explicit_anchor_resolution(self) -> None:
        self.write("standards/details.md", '# Details\n## A `code` value!\n## A `code` value!\n<a id="legacy"></a>\n')
        self.write("standards/python.md", "[Second](details.md#a-code-value-1) [Alias](details.md#legacy)\n")
        result = self.run_checker()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_ambiguous_reference_links_are_reported(self) -> None:
        self.write("standards/details.md", "[See][reference]\n\n[reference]: core.md\n")
        self.assert_failure(self.run_checker(), "unsupported")

    def test_custom_anchors_do_not_change_heading_numbering(self) -> None:
        self.write("standards/details.md", '<a name="heading"></a>\n# Heading\n# Heading\n')
        self.write("standards/python.md", "[Absent](details.md#heading-2)\n")
        self.assert_failure(self.run_checker(), "missing fragment")

    def test_repository_absolute_links_resolve_from_root(self) -> None:
        self.write("standards/details.md", "# Details\n[Rules](/standards/core.md#rules)\n")
        result = self.run_checker()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_invalid_toml_and_catalog_field_types_fail_without_traceback(self) -> None:
        for document in ('schema_version = [', CATALOG.replace('required = true', 'required = "yes"')):
            with self.subTest(document=document):
                self.write("standards/catalog.toml", document)
                result = self.run_checker()
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertNotIn("Traceback", result.stderr)

    def test_path_escape_is_not_followed(self) -> None:
        self.write("standards/details.md", "[Outside](../../outside.md)\n")
        self.assert_failure(self.run_checker(), "outside root")

    def test_missing_explicit_file_fails(self) -> None:
        self.assert_failure(self.run_checker("missing.md"), "missing input")

    def nested_bundle(self) -> None:
        for name in ("standards", "templates"):
            shutil.copytree(self.root / name, self.root / ".agents-framework" / name)
        # Root-installed templates are adapted separately even while inactive.
        self.write(".agents-framework/templates/policy-entry.md", "[Rules](../standards/core.md#rules)\n")
        self.write("AGENTS.md", "[Rules](.agents-framework/standards/core.md#rules)\n")
        self.write(".agents-framework/adoption.md", "[Rules](standards/core.md#rules)\n")

    def run_nested(self, *args: str) -> subprocess.CompletedProcess[str]:
        return self.run_checker("--bundle-dir", ".agents-framework", "--profile", "python", *args)

    def test_nested_selection_uses_its_catalog_and_dependency_closure(self) -> None:
        self.nested_bundle()
        (self.root / ".agents-framework/standards/optional.md").unlink()
        self.write("standards/catalog.toml", "invalid flat catalog")
        result = self.run_nested()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assert_failure(self.run_checker("--profile", "python"), "invalid catalog")
        for name in ("core.md", "details.md"):
            with self.subTest(name=name):
                path = self.root / ".agents-framework/standards" / name
                content = path.read_text(encoding="utf-8")
                path.unlink()
                self.assert_failure(self.run_nested(), "missing resource")
                path.write_text(content, encoding="utf-8")

    def test_nested_links_use_document_and_project_bases(self) -> None:
        self.nested_bundle()
        self.write(".agents-framework/standards/details.md", "# Details\n[Root](/AGENTS.md)\n")
        self.assertEqual(self.run_nested().returncode, 0)
        self.write(".agents-framework/standards/python.md", "[Bad](core.md#absent)\n")
        result = self.run_nested()
        self.assert_failure(result, "missing fragment")
        self.assertIn(".agents-framework/standards/python.md:1:", result.stdout)

    def test_nested_transitive_optional_dependency_cannot_use_flat_resource(self) -> None:
        self.nested_bundle()
        self.write(".agents-framework/standards/catalog.toml", CATALOG.replace(
            'dependencies = ["core"]', 'dependencies = ["optional"]',
        ).replace('id = "optional"', 'id = "optional"\ndependencies = ["core"]'))
        result = self.run_nested()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        (self.root / ".agents-framework/standards/optional.md").unlink()
        self.assert_failure(self.run_nested(), "missing resource: standards/optional.md")

    def test_nested_root_and_adoption_bodies_are_scanned_unless_scoped(self) -> None:
        self.nested_bundle()
        for name in ("AGENTS.md", ".agents-framework/adoption.md"):
            with self.subTest(name=name):
                original = (self.root / name).read_text(encoding="utf-8")
                self.write(name, "[Missing](missing.md)\n")
                self.assert_failure(self.run_nested(), "missing link target")
                result = self.run_nested(".agents-framework/standards/core.md")
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assert_failure(self.run_nested(name), "missing link target")
                self.write(name, original)

    def test_nested_scoped_paths_keep_catalog_checks(self) -> None:
        self.nested_bundle()
        (self.root / ".agents-framework/standards/details.md").unlink()
        self.assert_failure(self.run_nested("AGENTS.md"), "missing resource")
        self.assert_failure(self.run_nested("standards/missing.md"), "missing input")

    def test_bundle_option_requires_profiles_and_contained_directory(self) -> None:
        self.nested_bundle()
        for args in (("--bundle-dir", ".agents-framework"),
                     ("--bundle-dir", "missing", "--profile", "python"),
                     ("--bundle-dir", "standards/core.md", "--profile", "python"),
                     ("--bundle-dir", "../outside", "--profile", "python"),
                     ("--bundle-dir", str(self.root), "--profile", "python")):
            with self.subTest(args=args):
                result = self.run_checker(*args)
                self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
                self.assertIn("bundle", result.stderr)
                self.assertNotIn("Traceback", result.stderr)
        result = self.run_checker("--bundle-dir", ".")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_catalog_cannot_escape_bundle_even_into_project(self) -> None:
        self.nested_bundle()
        self.write("local.md", "# Local\n")
        for resource in ("../local.md", str(self.root / "local.md")):
            with self.subTest(resource=resource):
                self.write(".agents-framework/standards/catalog.toml", CATALOG.replace(
                    '"standards/details.md"', f'"{resource}"',
                ))
                self.assert_failure(self.run_nested(), "bundle")

    def test_symlinks_cannot_escape_bundle_or_project(self) -> None:
        self.nested_bundle()
        with tempfile.TemporaryDirectory(prefix="aek-check-outside-") as directory:
            outside = Path(directory)
            (outside / "file.md").write_text("# Outside\n", encoding="utf-8")
            (self.root / "outside-bundle").symlink_to(outside, target_is_directory=True)
            result = self.run_checker("--bundle-dir", "outside-bundle", "--profile", "python")
            self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
            self.write("AGENTS.md", "[Outside](escape.md)\n")
            (self.root / "escape.md").symlink_to(outside / "file.md")
            self.assert_failure(self.run_nested(), "outside root")
        resource = self.root / ".agents-framework/standards/details.md"
        resource.unlink()
        resource.symlink_to(self.root / "standards/details.md")
        self.assert_failure(self.run_nested(), "outside bundle")
        catalog = self.root / ".agents-framework/standards/catalog.toml"
        catalog.unlink()
        catalog.symlink_to(self.root / "standards/catalog.toml")
        self.assert_failure(self.run_nested(), "outside bundle")

    def test_source_mapping_is_limited_to_declared_templates_and_source_mode(self) -> None:
        for name in ("policy-entry.md", "AGENTS.root.md", "PLANS.md"):
            self.write(f"templates/{name}", "[Rules](.agents-framework/standards/core.md#rules)\n")
        result = self.run_checker()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.write("templates/other.md", "[Rules](.agents-framework/standards/core.md)\n")
        self.assert_failure(self.run_checker(), "missing link target")
        (self.root / "templates/other.md").unlink()
        self.write("AGENTS.md", "[Rules](.agents-framework/standards/core.md)\n")
        self.assert_failure(self.run_checker(), "missing link target")
        (self.root / "AGENTS.md").unlink()
        self.assert_failure(self.run_checker("--profile", "python"), "missing link target")
        self.nested_bundle()
        self.write(".agents-framework/templates/policy-entry.md", "[Rules](.agents-framework/standards/core.md)\n")
        self.assert_failure(self.run_nested(), "missing link target")

    def test_source_mapping_still_checks_missing_resources_and_fragments(self) -> None:
        self.write("templates/PLANS.md", "[Bad](.agents-framework/standards/core.md#absent)\n")
        self.assert_failure(self.run_checker(), "missing fragment")
        self.write("templates/PLANS.md", "[Bad](.agents-framework/standards/absent.md)\n")
        self.assert_failure(self.run_checker(), "missing link target")

    def test_symlink_loops_report_errors_without_traceback(self) -> None:
        self.nested_bundle()
        loop = self.root / "loop"
        loop.symlink_to(loop)
        resource = self.root / ".agents-framework/standards/details.md"
        resource.unlink()
        resource.symlink_to(resource)
        self.write("AGENTS.md", "[Loop](loop/file.md)\n")
        for args, status in ((["--bundle-dir", "loop", "--profile", "python"], 2),
                             (["--bundle-dir", ".agents-framework", "--profile", "python"], 1),
                             (["AGENTS.md"], 1)):
            with self.subTest(args=args):
                result = self.run_checker(*args)
                self.assertEqual(result.returncode, status, result.stdout + result.stderr)
                self.assertNotIn("Traceback", result.stderr)

    def policy_bundle(self, directory: str) -> str:
        if directory == ".agents-framework" and not (self.root / directory / "standards").exists():
            self.nested_bundle()
        prefix = "" if directory == "." else directory + "/"
        self.write(prefix + "standards/catalog.toml", CATALOG.replace(
            'assets = ["standards/catalog.toml"]',
            'assets = ["standards/catalog.toml", "standards/policy-defaults.toml", "standards/policy-configuration.md"]',
        ))
        self.write(prefix + "standards/policy-defaults.toml", POLICY)
        self.write(prefix + "standards/policy-configuration.md", "# Policy configuration\n")
        self.write(prefix + "templates/policy-entry.md", "[Rules](../standards/core.md#rules)\n")
        return prefix

    def run_policy(self, directory: str, *paths: str) -> subprocess.CompletedProcess[str]:
        return self.run_checker("--bundle-dir", directory, "--profile", "python", *paths)

    def test_policy_defaults_and_sparse_overrides_in_both_layouts(self) -> None:
        for directory in (".", ".agents-framework"):
            with self.subTest(directory=directory):
                self.policy_bundle(directory)
                override = self.root / ".agents-framework/policy.toml"
                override.unlink(missing_ok=True)
                for text in (None, 'schema_version = 1\n',
                             'schema_version = 1\n[verification]\ntiming = "task_end"\n[review]\nindependent = "on_request"\n',
                             'schema_version = 1\n[size]\ngrowth_review_from_lines = 700\n'):
                    if text is not None:
                        self.write(".agents-framework/policy.toml", text)
                    result = self.run_policy(directory)
                    self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                # Explicit source-mode paths still run policy validation.
                if directory == ".":
                    result = self.run_checker("standards/core.md")
                    self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_policy_invalid_override_reports_field_even_with_scoped_markdown(self) -> None:
        cases = (
            ('schema_version = 2', 'schema_version'),
            ('schema_version = true', 'schema_version'),
            ('[review]\nindependent = "risk_based"', 'schema_version'),
            ('schema_version = 1\nmax_tests = 1', 'max_tests'),
            ('schema_version = 1\n[unknown]\nvalue = 1', 'unknown'),
            ('schema_version = 1\n[verification]\nmax_fix_rounds = 1', 'verification.max_fix_rounds'),
            ('schema_version = 1\n[verification]\ntiming = "per_file"', 'verification.timing'),
            ('schema_version = 1\n[review]\nindependent = "always"', 'review.independent'),
            ('schema_version = 1\n[size]\nfile_review_lines = 0', 'size.file_review_lines'),
            ('schema_version = 1\n[size]\nclass_review_lines = -1', 'size.class_review_lines'),
            ('schema_version = 1\n[size]\nfunction_review_lines = true', 'size.function_review_lines'),
            ('schema_version = 1\n[size]\nreact_component_review_lines = 250.0', 'size.react_component_review_lines'),
            ('schema_version = 1\n[verification]\ndiagnostic_reset_after_stalled_attempts = false', 'verification.diagnostic_reset_after_stalled_attempts'),
            ('schema_version = 1\nsize = 1', 'size'),
            ('schema_version = 1\n[instructions]\nroot_guideline_lines = [70, 40]', 'instructions.root_guideline_lines'),
            ('schema_version = 1\n[instructions]\nroot_guideline_lines = [40, 40]', 'instructions.root_guideline_lines'),
            ('schema_version = 1\n[instructions]\nlocal_guideline_lines = [10]', 'instructions.local_guideline_lines'),
            ('schema_version = 1\n[instructions]\nlocal_guideline_lines = [0, 25]', 'instructions.local_guideline_lines'),
            ('schema_version = 1\n[instructions]\nlocal_guideline_lines = [true, 25]', 'instructions.local_guideline_lines'),
        )
        for directory in (".", ".agents-framework"):
            prefix = self.policy_bundle(directory)
            for content, field in cases:
                with self.subTest(directory=directory, field=field, content=content):
                    self.write(".agents-framework/policy.toml", content + "\n")
                    result = self.run_policy(directory, prefix + "standards/core.md")
                    self.assert_failure(result, field)
                    self.assertIn(".agents-framework/policy.toml:", result.stdout)
                    self.assertNotIn("Traceback", result.stderr)
                    self.assertEqual((self.root / ".agents-framework/policy.toml").read_text(), content + "\n")

    def test_policy_merged_growth_constraints_use_inherited_values(self) -> None:
        for directory in (".", ".agents-framework"):
            self.policy_bundle(directory)
            for field, value in (("growth_review_from_lines", 701), ("documented_review_above_lines", 599)):
                with self.subTest(directory=directory, field=field):
                    self.write(".agents-framework/policy.toml", f'schema_version = 1\n[size]\n{field} = {value}\n')
                    self.assert_failure(self.run_policy(directory), "size.growth_review_from_lines")
            self.write(".agents-framework/policy.toml", 'schema_version = 1\n[size]\ngrowth_review_from_lines = 800\ndocumented_review_above_lines = 900\n')
            result = self.run_policy(directory)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_policy_defaults_must_be_complete_and_valid_before_override(self) -> None:
        prefix = self.policy_bundle(".")
        self.write(".agents-framework/policy.toml", 'schema_version = 1\n[size]\ngrowth_review_from_lines = 500\n')
        for content, field in (
            (POLICY.replace('function_review_lines = 50\n', ''), 'size.function_review_lines'),
            (POLICY.replace('schema_version = 1', 'schema_version = 2'), 'schema_version'),
            (POLICY.replace('growth_review_from_lines = 600', 'growth_review_from_lines = 800'), 'size.growth_review_from_lines'),
            (POLICY.replace('independent = "risk_based"', 'independent = false'), 'review.independent'),
            (POLICY + '\nextra = 1\n', 'instructions.extra'),
        ):
            with self.subTest(field=field):
                self.write(prefix + "standards/policy-defaults.toml", content)
                result = self.run_checker("standards/core.md")
                self.assert_failure(result, field)
                self.assertIn("standards/policy-defaults.toml:", result.stdout)

    def test_policy_legacy_absence_and_partial_setup(self) -> None:
        for directory in (".", ".agents-framework"):
            if directory == ".agents-framework":
                self.nested_bundle()
            prefix = "" if directory == "." else directory + "/"
            self.write(prefix + "templates/policy-entry.md", "[Rules](../standards/core.md#rules)\n")
            override = self.root / ".agents-framework/policy.toml"
            override.unlink(missing_ok=True)
            result = self.run_policy(directory)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.write(".agents-framework/policy.toml", 'schema_version = 1\n')
            self.assert_failure(self.run_policy(directory), "partial policy setup")
            self.policy_bundle(directory)
            (self.root / (prefix + "standards/policy-configuration.md")).unlink()
            self.assert_failure(self.run_policy(directory, prefix + "standards/core.md"), "partial policy setup")
            # Restore a genuinely legacy source for the following layout fixture.
            for name in ("policy-defaults.toml", "policy-configuration.md"):
                (self.root / (prefix + "standards/" + name)).unlink(missing_ok=True)
            self.write(prefix + "standards/catalog.toml", CATALOG)

    def test_policy_override_is_project_relative_for_custom_bundle(self) -> None:
        self.policy_bundle(".agents-framework")
        (self.root / ".agents-framework").rename(self.root / "custom-bundle")
        self.write(".agents-framework/policy.toml", 'schema_version = 1\n[size]\nfile_review_lines = false\n')
        self.write("custom-bundle/policy.toml", 'schema_version = 1\n')
        result = self.run_policy("custom-bundle", "custom-bundle/standards/core.md")
        self.assert_failure(result, "size.file_review_lines")
        self.assertIn(".agents-framework/policy.toml:", result.stdout)

    def test_policy_malformed_toml_and_symlink_escape_fail(self) -> None:
        self.policy_bundle(".agents-framework")
        self.write(".agents-framework/policy.toml", 'schema_version = [\n')
        self.assert_failure(self.run_policy(".agents-framework"), "invalid policy")
        override = self.root / ".agents-framework/policy.toml"
        override.unlink()
        with tempfile.TemporaryDirectory(prefix="aek-policy-outside-") as directory:
            outside = Path(directory) / "policy.toml"
            outside.write_text('schema_version = 1\n', encoding="utf-8")
            override.symlink_to(outside)
            self.assert_failure(self.run_policy(".agents-framework"), "outside root")
        override.unlink()
        defaults = self.root / ".agents-framework/standards/policy-defaults.toml"
        self.write("local-policy.toml", POLICY)
        defaults.unlink()
        defaults.symlink_to(self.root / "local-policy.toml")
        self.assert_failure(self.run_policy(".agents-framework"), "outside bundle")


if __name__ == "__main__":
    unittest.main()
