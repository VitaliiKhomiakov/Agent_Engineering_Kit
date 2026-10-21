"""Real-template task-skill fixtures; not a consumer installer or model eval."""

import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from urllib.parse import urlsplit

from tools.check_instruction_artifacts import Checker, ROOT_LINK_TEMPLATES, markdown


ROOT = Path(__file__).resolve().parents[1]
SKILL = "templates/skills/aek-design-feature/SKILL.md"
NATIVE = ".agents/skills/aek-design-feature/SKILL.md"
# These references are conditional on technologies/profile omitted by this fixture.
OMITTED = {"standards/react/components-boundaries.md", "standards/unreal-engine.md", "standards/godot.md",
           "standards/project-skills.md"}


def adapt_document(source: Path, destination: Path, bundle: Path,
                   selected: set[Path], text: str,
                   optional_references: frozenset[str] = frozenset()) -> str:
    """Adapt only supported links, rejecting any unclassified missing reference."""
    result = text
    virtual = source.relative_to(ROOT).as_posix() in ROOT_LINK_TEMPLATES
    for link in markdown(source, text).links:
        url = urlsplit(link.target)
        if url.scheme or url.netloc or not url.path:
            continue
        target = ((ROOT / url.path.removeprefix(".agents-framework/")) if virtual
                  else source.parent / url.path).resolve()
        relative = target.relative_to(ROOT).as_posix()
        if target not in selected:
            if (not relative.startswith(("docs/research/", "docs/plans/"))
                    and relative not in OMITTED and relative not in optional_references):
                raise ValueError(f"Unclassified missing reference: {relative}")
            pattern = r"\[([^]]+)\]\(" + re.escape(link.target) + r"\)"
            result = re.sub(pattern, lambda match: match[1] + " (optional source reference: `"
                            + relative + "`; source identity in adoption record)", result)
        else:
            installed = bundle / relative
            route = Path(os.path.relpath(installed, destination.parent)).as_posix()
            if url.fragment:
                route += "#" + url.fragment
            result = result.replace("](" + link.target + ")", "](" + route + ")")
    return result


def prepare_design_fixture(target: Path, *, workflow: bool = True,
                           bundle_dir: str = ".agents-framework",
                           native_skills: tuple[str, ...] = ("aek-design-feature",)) -> None:
    """Prepare this fixed FastAPI instruction fixture in a caller-owned empty root."""
    if target.exists() and any(target.iterdir()):
        raise ValueError("Fixture target must be empty")
    bundle = target / bundle_dir
    bundle.mkdir(parents=True, exist_ok=True)
    checker = Checker(ROOT)
    profiles = ("fastapi", "project-workflows") if workflow else ("fastapi",)
    selected = checker.catalog_files(profiles)
    if checker.diagnostics:
        raise ValueError(str(checker.diagnostics))
    for source in sorted(selected):
        destination = bundle / source.relative_to(ROOT)
        destination.parent.mkdir(parents=True, exist_ok=True)
        if source.suffix in {".md", ".mdc"}:
            destination.write_text(adapt_document(source, destination, bundle, selected,
                                                 source.read_text(encoding="utf-8")), encoding="utf-8")
        else:
            shutil.copyfile(source, destination)
    entry_source = ROOT / "templates/policy-entry.md"
    entry = "# Fixture instructions\n\n## Reasoning and communication language" + entry_source.read_text(
        encoding="utf-8").split("## Reasoning and communication language", 1)[1]
    entry = entry.replace("$projects", "Project: this independently opened reservation-service fixture.\n"
                          "Architecture: `ARCHITECTURE.md`. Canonical task: `docs/plans/cancel.md`.")
    routes = "\n".join(f"- [{name}]({bundle_dir}/standards/{name}.md)"
                       for name in ("python", "pydantic", "fastapi"))
    # Insert final-location routes after source-template link adaptation.
    entry = entry.replace("<actual installed or accessible source skill path>",
                          "a separately identified source; integration is not installed here")
    entry = entry.replace("<actual installed task skill paths>", ", ".join(
        f".agents/skills/{name}/SKILL.md" for name in native_skills))
    entry = entry.replace("Remove this optional route when that profile is omitted; direct rules remain usable.\n", "")
    if not workflow:
        entry = re.sub(r"If `project-workflows` is explicitly selected,.*?\n\n", "", entry, flags=re.DOTALL)
    entry = adapt_document(entry_source, target / "AGENTS.md", bundle, selected, entry)
    (target / "AGENTS.md").write_text(entry.replace("$routes", routes), encoding="utf-8")
    plans_source = ROOT / "templates/PLANS.md"
    plans = "# Planning rules\n\n## Language" + plans_source.read_text(
        encoding="utf-8").split("## Language", 1)[1]
    (target / "PLANS.md").write_text(adapt_document(
        plans_source, target / "PLANS.md", bundle, selected, plans), encoding="utf-8")
    for source in sorted((ROOT / "tests/fixtures/project-skills").rglob("*")):
        if source.is_file():
            destination = target / source.relative_to(ROOT / "tests/fixtures/project-skills")
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, destination)
    if workflow:
        for name in native_skills:
            source = ROOT / "templates/skills" / name / "SKILL.md"
            destination = target / ".agents/skills" / name / "SKILL.md"
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(adapt_document(source, destination, bundle, selected,
                                                 source.read_text(encoding="utf-8")), encoding="utf-8")


class ProjectSkillAdoptionChecks(unittest.TestCase):
    def setUp(self) -> None:
        directory = tempfile.TemporaryDirectory(prefix="aek-skill-test-")
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name) / "independent-child"
        prepare_design_fixture(self.root)

    def check(self, *paths: str, bundle_dir: str = ".agents-framework") -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, "-B", str(ROOT / "tools/check_instruction_artifacts.py"),
             "--root", str(self.root), "--bundle-dir", bundle_dir,
             "--profile", "project-workflows", "--profile", "fastapi", *paths],
            cwd=self.root.parent, text=True, capture_output=True, check=False, timeout=15,
        )

    def test_actual_templates_resolve_in_bundle_and_native_locations(self) -> None:
        for paths in ((), (NATIVE,)):
            result = self.check(*paths)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertFalse((self.root / "MIGRATION.md").exists())
        self.assertFalse((self.root / ".agents-framework/standards/react.md").exists())
        self.assertFalse((self.root / ".agents-framework/standards/nextjs-framework.md").exists())

    def test_unadapted_native_link_fails_despite_valid_inactive_template(self) -> None:
        shutil.copyfile(ROOT / SKILL, self.root / NATIVE)
        self.assertEqual(self.check().returncode, 0)
        result = self.check(NATIVE)
        self.assertEqual(result.returncode, 1)
        self.assertIn("missing link target", result.stdout)

    def test_missing_required_guide_fails_even_for_native_only_scan(self) -> None:
        (self.root / ".agents-framework/standards/project-skills.md").unlink()
        result = self.check(NATIVE)
        self.assertEqual(result.returncode, 1)
        self.assertIn("missing resource: standards/project-skills.md", result.stdout)

    def test_broken_required_skill_reference_is_reported_at_native_path(self) -> None:
        path = self.root / NATIVE
        path.write_text(path.read_text(encoding="utf-8").replace(
            "../../../.agents-framework/standards/project-skills.md)",
            "../../../.agents-framework/standards/missing-guide.md)"), encoding="utf-8")
        result = self.check(NATIVE)
        self.assertEqual(result.returncode, 1)
        self.assertIn(NATIVE, result.stdout)
        self.assertIn("missing-guide.md", result.stdout)

    def test_native_reference_uses_actual_flat_or_custom_bundle(self) -> None:
        for layout in (".", "rules/aek"):
            with self.subTest(layout=layout):
                shutil.rmtree(self.root)
                prepare_design_fixture(self.root, bundle_dir=layout)
                result = self.check(NATIVE, bundle_dir=layout)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_all_task_entries_resolve_from_their_actual_native_paths(self) -> None:
        names = ("aek-design-feature", "aek-review-changes")
        shutil.rmtree(self.root)
        prepare_design_fixture(self.root, native_skills=names)
        paths = tuple(f".agents/skills/{name}/SKILL.md" for name in names)
        for selection in ((), paths):
            result = self.check(*selection)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        entry = (self.root / "AGENTS.md").read_text(encoding="utf-8")
        for path in paths:
            self.assertIn(path, entry)
        self.assertFalse((self.root / ".agents-framework/templates/skills/aek-implement-feature").exists())
        self.assertFalse((self.root / ".agents/skills/aek-implement-feature").exists())
        self.assertNotIn("aek-implement-feature", entry)

    def test_native_review_selection_does_not_install_other_bundle_skills(self) -> None:
        shutil.rmtree(self.root)
        prepare_design_fixture(self.root, native_skills=("aek-review-changes",))
        native = ".agents/skills/aek-review-changes/SKILL.md"
        result = self.check(native)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        entry = (self.root / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn(native, entry)
        name = "aek-design-feature"
        self.assertFalse((self.root / ".agents/skills" / name).exists())
        self.assertNotIn(f".agents/skills/{name}/SKILL.md", entry)
        self.assertTrue((self.root / ".agents-framework/templates/skills" / name / "SKILL.md").is_file())


if __name__ == "__main__":
    unittest.main()
