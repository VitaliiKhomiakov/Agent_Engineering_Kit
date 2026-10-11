# Project task-skill adoption observations — 2026-10-11

PS-04 of the [canonical plan](../plans/2026-10-11-project-skills-reorganization.md)
checks portable instruction artifacts and the decisions in the actual
[adoption procedure](../../MIGRATION.md). This is a disposable fixture exercise,
not a consumer rollout, production installer or native-client behavior trial.
No application dependencies, Git repository or client configuration were installed
on the user's machine. Native-looking files below exist only in temporary projects.

## Inputs and boundaries

The pre-edit stage baseline is `/tmp/aek-ps04-9gp8aros/baseline.json`, with exact
originals in `originals/`. It includes 276 original file identities and absence
records for new paths. Relevant source changes are the native-skill mapping in
the adoption-record template, the integration skill's selected-skill route and
MIGRATION's scope/ownership reminders. Catalog IDs, native task-skill templates,
technology rules, saved user choices and earlier behavior evidence are unchanged.

The durable inputs and deterministic assertions are in
[test_project_skill_portability.py](../../tests/test_project_skill_portability.py).
Its `portable_candidate` renders real catalog-selected resources and actual entry,
planning, bridge, role and skill templates into a byte mapping in memory. It does
not read a target, infer ownership, merge files or perform an update. Its explicit
fixture writer is not an adoption interface. The shared link adapter rejects
unclassified missing references; it does not hide every absent resource.

The local sentinels in `LOCAL_FILES` preserve an architecture/passport, exception
E1 and local gate, a canonical task at `.work/items/feature.md`, native model/effort
values with a comment, and a root-relative policy override. The local gate is a
future application requirement, not a command claimed to have run during import.
The existing-initial-import walkthrough additionally preserves the original root
entry's local gate in the adapted entry. Snapshots and comparison operands live
outside the target's instruction/skill discovery paths.

## Portable layouts and representative selections

The automated matrix covers all 15 combinations:

| Bundle placement | Selected application profiles, each with project-workflows |
| --- | --- |
| `.agents-framework` | FastAPI; React + TypeScript; Angular; Angular + NgRx; Go |
| `.` (retained flat) | Same five selections |
| `rules/aek` (custom) | Same five selections |

Each target is an independently addressable child directory. The checker runs
with an explicit target root from outside that child, first on the selected bundle
and then on all three native skills plus the native role syntax fixture. Resolved
guide paths must remain inside the child. Source MIGRATION and a new `docs/plans`
store are absent; the existing task location remains. No application build is
needed for these instruction-only inputs.

Additional explicit checks cover the `@AGENTS.md` import, planning-policy
code-span paths and TOML developer-instruction routes, since Markdown checks
alone do not cover those syntaxes. TOML model/effort values are preserved. Native
skill prose retains its clearly labelled contained-layout example; the actual
Markdown guide reference uses the selected layout. Metadata such as
`.agents-framework/policy.toml` intentionally remains instruction-root-relative.
Inactive example templates are not counted as extra native installations.
These fixture paths do not establish Claude/Codex role activation or enforcement.

The first expanded matrix correctly rejected unclassified optional Node.js,
Next.js and NgRx references (nine failing subcases). Source review confirmed the
host/framework conditions. The test helper now receives an explicit reviewed
allowlist for these optional links, preserving their surrounding conditions as
labelled source references. Required local links still fail when missing. No
technology was added simply to make an unrelated optional link resolve.

## Reproduce preparation and layout checks

From the source root:

```sh
python3 -m unittest discover -s tests -p test_project_skill_portability.py
```

For an inspectable contained FastAPI fixture, choose a new temporary directory:

```sh
aek_fixture_dir=$(mktemp -d /tmp/aek-adoption-XXXXXX)
python3 - "$aek_fixture_dir" <<'PY'
from pathlib import Path
import shutil
import sys
from tests.test_project_skill_portability import LOCAL_FILES, portable_candidate, snapshot, write_fixture
work = Path(sys.argv[1])
target = work / 'project'
write_fixture(target, {name: text.encode() for name, text in LOCAL_FILES.items()})
before = snapshot(target)
candidate = portable_candidate(('fastapi',), '.agents-framework')
assert snapshot(target) == before
shutil.copytree(target, work / 'recovery-before')
write_fixture(target, candidate)  # Explicit fixture application, not an installer.
PY
python3 tools/check_instruction_artifacts.py --root "$aek_fixture_dir/project" --bundle-dir .agents-framework --profile fastapi --profile project-workflows
python3 tools/check_instruction_artifacts.py --root "$aek_fixture_dir/project" --bundle-dir .agents-framework --profile fastapi --profile project-workflows .agents/skills/aek-design-feature/SKILL.md .agents/skills/aek-implement-feature/SKILL.md .agents/skills/aek-review-changes/SKILL.md .codex/agents/af-reviewer.toml
```

The unittest matrix also verifies that preparing for a nonexistent target creates
no target path, and that repeat preparation is byte-identical without refreshing
target file/directory mtimes. This is not evidence that an autonomous updater
will make the same no-op decision.

## Instruction-led update and recovery walkthrough

The coordinator walked through MIGRATION's prepare/apply, ownership, B/C/N and
recovery sections against actual temporary files. Recorded choices determined
which writes occurred; there is no new automatic conflict resolver. Raw operation
files remain at `/tmp/aek-ps04-9gp8aros/cases-reviewed` and `recovery-reviewed`
through review. The table and fixture recipe retain the inputs/results if those
temporary directories are later removed.

New/existing imports used the same real-template candidate, then a populated
adoption record with identity/agreement, managed paths, native mapping and accepted
exception sections from the record template. The record distinguishes source
identity, adapted accepted hashes, retrievable snapshots and unobserved client use;
it does not hash itself. Local model selection was checked/reused from the fixture's
existing native config, without rewriting it or implying activation.

Update cases use `.agents/skills/aek-review-changes/SKILL.md`. Construct accepted
**B** from its adapted bytes plus this fixture-only trailer:

```text

## Fixture update input

Transport note: accepted.

Project note: accepted.
```

**N** replaces `Transport note: accepted.` with `Transport note: upstream revision.`
**C** for independent/local-only edits replaces `Project note: accepted.` with
`Project note: local contract retained.` For overlap, C instead replaces the same
transport line with `Transport note: local decision.` These are synthetic text
revisions for reconciliation, not new production policy or skill behavior.

Compare actual operands with `diff3 -m C B N`, keeping its output outside the
target. Exit 0 means no textual conflict, not semantic approval; exit 1 exposes
the seeded conflict. Recheck the destination against prepared C before applying.

| Scenario | Action and observed result |
| --- | --- |
| New rule import | Prepared without target changes, preserved originals outside discovery, applied the selected closure and three native entries; bundle/native checks passed and local files/mtimes survived |
| Existing initial import | Reconciled the existing root gate into the adapted entry; local exception, task, model comment/values and policy override survived; record and installed references passed |
| Unchanged repeat | Compared the complete candidate with managed bytes and selected no writes; target manifest plus every file/directory mtime stayed identical, including the record |
| Clean update, C = B | Rechecked C, preserved the operation original, wrote N, checked affected files, then recorded a separate accepted-update snapshot; old B remained retrievable |
| Local-only change, N = B | Kept C and its mtimes; neither reset local content nor silently advanced the accepted base |
| C = N | No content rewrite; provenance reconciliation remains a separate decision, so this is not reported as a fully unchanged import merely from one matching file |
| Independent B/C/N edits | Real diff3 returned 0 with both revisions; coordinator accepted this fixture's noncompeting notes, rechecked C, applied and checked the result, then advanced accepted references separately |
| Overlapping B/C/N edits | Real diff3 returned 1 and conflict markers; exposed the decision and withheld the dependent target write; C and mtimes stayed unchanged |
| Missing accepted contents | Removed the accepted skill snapshot while retaining its recorded B hash; both C/N differed from that hash. No three-way merge or replacement was claimed or performed |
| Intentionally removed managed file | Retained the missing native file; recorded that explicit selection/restore reconciliation is required. The old verified record was not treated as proof of current completeness |
| Unowned same-name skill | Prepared against a local `aek-review-changes` definition with no ownership record; preserved it unchanged and withheld replacement rather than acquiring ownership by name |
| Edit after preview | Changed the destination from prepared B to C before application; the mismatch prevented replacement |
| Interrupted write and later user edits | Compared current bytes with operation-written bytes path by path; restored one unchanged operation-written skill, removed one unchanged operation-created file, retained later edits to another skill, another created file and the record; reported partial recovery, without advancing the accepted base |

The recovery case uses the implementation skill as the safely restorable file.
Its written result is the original adapted content plus `Operation revision.`.
The review skill receives N and then `Later user edit.`. Two newly created notes
initially contain `Operation-created note.`; one is later replaced with
`Later user content.` and must survive. The record receives `Later user record edit.`
and must also survive. Preserve original contents/absence and the written byte
mapping outside discovery before performing these explicit operations. The final
fixture still has exactly three active `*/SKILL.md` definitions; no backup becomes
discoverable. Remaining planned writes were not attempted after interruption.

Expected conflicts and partial recovery are successful observations of a safe
stopping decision, not successful completed imports. No action in those dummy
cases requires an owner decision in the real source repository.

During review, the first walkthrough draft incorrectly used candidate hashes
for accepted metadata, losing an existing entry's retained local addition. The
reviewed run instead hashes the actual adapted accepted snapshots and seeds the
recorded B before updates. Snapshot/hash consistency was then checked explicitly;
the corrected cases were rerun. This illustrates why passing link checks alone
does not validate ownership or accepted-content metadata.

The final run also records the synthetic N hash separately from the unchanged
source manifest and uses the matching operation-evidence path. Accepted content
hashes still refer to actual adapted snapshots, including a combined local edit.
Disposable final outputs are `/tmp/aek-ps04-9gp8aros/walkthrough-results-final.json`,
`cases-final/` and `recovery-final/`; the preceding drafts remain preserved. The
coordinator's concrete script is `walkthrough-final.py` in that same directory.
These paths aid the current review; the durable reproduction inputs and procedure
are recorded above. The [validation addendum](2026-10-11-project-skills-validation.md#stage-4-portability-and-recovery-validation--2026-10-11)
records the source identities and executed regression/analyzer checks.

## Evidence limits

Automated assertions establish closure, paths, retained contents and mtimes for
these fixed inputs. The separate walkthrough records the coordinator's actual
decisions under the instruction-led procedure; it does not prove an autonomous
agent will make them. It uses actual files and diff3, not a simulated model.
The update operands are deliberately small text changes, not a universal semantic
merge claim. Snapshot paths are disposable test evidence, not durable bases for a
real future consumer update. Native trigger/adherence testing remains PS-05.
