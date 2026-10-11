"""Prepare bounded PS-05 inputs; never run a model or modify a real consumer."""

from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from tests.test_project_skill_adoption import prepare_design_fixture

SKILLS = ("aek-design-feature", "aek-implement-feature", "aek-review-changes")
BOUNDARY = """
Observation boundary: work inline in this disposable project. No delegation,
Git writes, tool installation, configuration changes or source-library access.
Use python3. The coordinator provides mypy 2.1.0 via PYTHONPATH; no installation
is needed. Existing local accepted exception E1: process-local in-memory storage
and a single Lock are intentional for this bounded fixture; do not propose a
repository/database/service layer merely to follow a general example.
"""
IMPLEMENT = """# Domain cancellation implementation

Status: accepted design; domain implementation authorized.
Canonical owner: this file. Work inline; no Git actions or delegation.

Implement Inventory.cancel(reservation_id: str) -> Reservation in app/domain.py.
Keep the existing single Lock as the atomic transition boundary. Within it,
lookup the reservation, replace an active frozen record with a cancelled one,
restore its quantity once, and store/return that record. An already-cancelled
reservation returns the stored record with no stock change. Missing ID raises
KeyError without mutation. Preserve ID, quantity, reserve/get and the frozen DTO.
This accepted design needs no new brainstorming or approval. HTTP integration is
explicitly a later task: preserve app/http.py byte for byte. E1 in ARCHITECTURE.md
is accepted. Do not introduce dependencies, new layers or another task document.

Acceptance: python3 acceptance.py; then python3 -m mypy --strict
--disallow-any-explicit --disallow-any-unimported --python-version 3.12
--explicit-package-bases app/domain.py acceptance.py, using a temporary cache outside project contents.
Only app/domain.py, focused tests if needed, and this task may change. Record
actual checks and affected technical rules here, then stop at the owner checkpoint.

- [ ] CANCEL-IMPLEMENT: Deliver and verify the accepted domain operation.
"""
REVIEW = """# Review of domain cancellation change

Review-only: compare baseline/domain.py with app/domain.py. No edits anywhere in
this project, fixes, new plans, Git operations, delegation, installation or setup.
The accepted contract is atomic/idempotent cancellation, returning quantity to
stock exactly once; preserve frozen ID/quantity and missing-ID KeyError semantics.
app/http.py is unchanged and HTTP integration is a later task. E1 in the passport
is legitimate. Explain consequential findings with paths/lines, failure scenarios
and evidence; distinguish incidental pre-existing issues. Report in the response.
No independent-review claim follows from this coordinator observation.
"""
BUGGY_CANCEL = '''
    def cancel(self, reservation_id: str) -> Reservation:
        with self._lock:
            current = self._reservations[reservation_id]
            cancelled = Reservation(current.id, current.quantity, "cancelled")
            self._reservations[reservation_id] = cancelled
            self._stock += current.quantity
            return cancelled
'''


def prepare(target: Path, operation: str, workflow: bool) -> None:
    prepare_design_fixture(target, workflow=workflow, native_skills=SKILLS)
    entry = target / "AGENTS.md"
    entry.write_text(entry.read_text() + "\n## Installed procedure source\n\n"
                     "Superpowers 6.4.2 procedures are available at "
                     "`/home/vitalii/.codex/plugins/cache/openai-curated-remote/superpowers/6.4.2/skills`.\n"
                     "After local adaptations, read using-superpowers/SKILL.md there and the applicable\n"
                     "procedure. This explicit source route does not claim native plugin discovery.\n"
                     "If the path is unavailable, retain the documented direct-reference fallback.\n")
    architecture = target / "ARCHITECTURE.md"
    architecture.write_text(architecture.read_text() + BOUNDARY)
    if operation in {"implementation", "review"}:
        architecture.write_text(architecture.read_text() + "\nThis observation executes only the standard-library domain. Python 3.12 is\n"
                               "available; FastAPI/Pydantic HTTP runtime checks remain outside this change.\n")
        shutil.copyfile(Path(__file__).with_name("acceptance.py"), target / "acceptance.py")
        (target / "docs/plans/cancel.md").write_text(IMPLEMENT if operation == "implementation" else REVIEW)
    if operation == "review":
        (target / "baseline").mkdir()
        shutil.copyfile(target / "app/domain.py", target / "baseline/domain.py")
        domain = target / "app/domain.py"
        domain.write_text(domain.read_text() + BUGGY_CANCEL)
    if operation == "small-fix":
        (target / "docs/plans/cancel.md").write_text("# Quantity boundary fix\n\nSettled local fix: reject bool quantities with ValueError('invalid_quantity')\n"
                                                   "before stock changes, preserving valid positive integer behavior. No cancellation\n"
                                                   "implementation, new design, API change or dependency. Inline; no Git actions.\n")


if __name__ == "__main__":
    prepare(Path(sys.argv[1]), sys.argv[2], sys.argv[3] == "candidate")
