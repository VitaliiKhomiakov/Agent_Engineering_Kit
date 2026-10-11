# Project design skill validation — 2026-10-11

This records the first slice of the [canonical plan](../plans/2026-10-11-project-skills-reorganization.md).
PS-02 now has passing static checks, observed Codex discovery, a completed explicit
design trial and a completed unrelated-task counterexample. An implicit trial
observed skill selection and produced a design but timed out during verification.
The resumed observation below closes the first slice's behavioral gate; initial
failures retain their original limits. No previous pilot result is reused as proof.

## Inputs and scope

Source HEAD before changes: `a725cf28cb4e399e64c13dc421e63ea7cc4ae580`.
The stage snapshot is `/tmp/aek-project-skills-ps02-5uvsmse8/baseline.json` with
exact originals and prior-absence entries; this record retains the useful results
independently of that temporary directory. Only the optional design entry was
implemented. No consumer installation, plugin update, model reassignment, Git
mutation or delegation was performed.

| Checked input | SHA-256 |
| --- | --- |
| `standards/project-skills.md` | `afcb2859d8f669cc350f7228efcbf84fa859ce9be4dd17c738ac94b850fbdbae` |
| `templates/skills/aek-design-feature/SKILL.md` | `44d7ab1bd85aef5b357e6c85d15efff0c860f3fdb850a45b7b5d22154c3c4c85` |
| `tests/test_project_skill_adoption.py` | `59724b4f1c7075564b3e3d348b21f1ac84a251e761cb8d39a6248ecbbf34a74a` |

Native contract source reviewed on this date: OpenAI's
[Build skills](https://learn.chatgpt.com/docs/build-skills), covering repository
`.agents/skills`, required name/description and implicit skill selection. Vendor
documentation does not establish the behavior of this particular skill.
Installed client: `codex-cli 0.162.1`; installed Superpowers: `6.4.2`.
The saved model/effort (`gpt-6-astra`, `high`) was reused without overrides.
This is CLI evidence only, not desktop, Claude Code or Cursor verification.

## Reproducible target and acceptance

[The fixed fixture helper](../../tests/test_project_skill_adoption.py) selects the
actual `fastapi` and optionally `project-workflows` closures. It adapts the real
policy entry and planning template, copies the selected resources, and installs
the design skill in `.agents/skills/aek-design-feature/SKILL.md`. It explicitly
classifies omitted optional references and rejects other missing references.
This test helper is not a production adoption implementation or metadata fixture.

[Fixture architecture](../../tests/fixtures/project-skills/ARCHITECTURE.md),
[canonical task](../../tests/fixtures/project-skills/docs/plans/cancel.md),
[domain](../../tests/fixtures/project-skills/app/domain.py) and
[HTTP boundary](../../tests/fixtures/project-skills/app/http.py) are static design
inputs. They declare Python 3.12/FastAPI 0.138.0/Pydantic v2, an in-memory
reservation store and one lock. No application runtime dependencies were installed
and no runtime correctness is claimed for these inputs.

From the source root, prepare each observation in a new empty temporary directory:

```sh
python3 - /tmp/aek-design-observation <<'PY'
from pathlib import Path
import sys
sys.path.insert(0, 'tests')
from test_project_skill_adoption import prepare_design_fixture
prepare_design_fixture(Path(sys.argv[1]))
PY
python3 tools/check_instruction_artifacts.py --root /tmp/aek-design-observation --bundle-dir .agents-framework --profile fastapi --profile project-workflows
python3 tools/check_instruction_artifacts.py --root /tmp/aek-design-observation --bundle-dir .agents-framework --profile fastapi --profile project-workflows .agents/skills/aek-design-feature/SKILL.md
```

Use `workflow=False` for the no-skill control and omit its workflow checker
selection. Each observation must begin from a separately prepared directory.
Contained layout is the full fixture; flat/custom regression cases only establish
rebasing of the installed native link, not complete adoption of those layouts.

Design prompt, unchanged between control and implicit case:

> Complete CANCEL-DESIGN in docs/plans/cancel.md using the applicable project instructions. This authorizes the design document only, not application implementation. Keep the existing task as the only design/progress record. Do not delegate, install tools or change configuration. Report the actual rules used and the work completed.

For the explicit case replace the opening with `Use $aek-design-feature to
complete CANCEL-DESIGN`. For the unrelated case request correction of `servce`
to `service` in README.md only, preserving every other file and forbidding
delegation, installations and configuration changes.

Successful design must identify the real domain/HTTP owners, design an atomic and
idempotent cancellation returning stock once, preserve immutable fields and
existing contracts, map actual selected rules to decisions, and keep proposed
checks distinct from execution. Only the existing task may change. The unrelated
case must change only the typo without loading the design procedure. Record actual
skill reads and output; discovery or self-report alone does not satisfy these gates.

## Observed native boundary — initial attempt

Prepared directories contained 53 files for control and 56 each for implicit,
explicit and unrelated cases. A bubblewrap mount namespace exposed the selected
fixture at `/tmp/aek-observation`, made the host read-only, masked the AEK checkout
and other `/tmp` contents, and gave Codex a private writable runtime. Existing
configuration/authentication were reused privately; package/plugin/skill/rule
directories remained read-only. Temporary private runtime copies were removed
after observations. Credentials and full user configuration are not evidence artifacts.

Using this source-hidden fixture, the installed client's `app-server` protocol
accepted `initialize`, `initialized`, then `skills/list` with
`{"cwds":["/tmp/aek-observation"],"forceReload":true}`. Its returned matching entry:

```json
{"name":"aek-design-feature","path":"/tmp/aek-observation/.agents/skills/aek-design-feature/SKILL.md","scope":"repo","enabled":true,"pluginId":null}
```

No protocol error was returned. This establishes native discovery of the adapted
file without the source checkout, not successful task-time reference reading.

The bounded control used `codex exec --ephemeral --skip-git-repo-check --sandbox
workspace-write --json -C /tmp/aek-observation -`, with the prompt on stdin and a
180-second process limit. The first attempt could not reach workspace routing;
an approved network-capable retry reached the model. Shell operations then failed
with `Failed to create unified exec process: Permission denied (os error 13)`.
The model's alternative file-read tool required approval unavailable under the
nested CLI's policy. It reported CANCEL-DESIGN incomplete; no task or source file
changed. A completed CLI turn (exit 0) is therefore **not** a successful design.

The underlying exec denial was not resolved or attributed to a specific mount or
sandbox defect. Do not weaken permissions to turn this into a passing result.
Implicit, explicit and unrelated behavioral runs were not started after the common
workspace-tool failure. All four fixture manifests remained unchanged. Retry those
dependent observations only in a client environment with working authorized file
access; retain source unavailability and the same task constraints.

## Executed deterministic checks

| Check | Result and limit |
| --- | --- |
| Default source artifact checker | 208 artifacts; zero errors |
| `test_instruction_artifacts.py` | 40 tests passed |
| `test_profile_selection.py` | 33 tests passed, including workflow omission and six retained stack combinations |
| `test_project_skill_adoption.py` | 5 tests passed: real source/installed paths, unadapted link, missing guide, broken route, flat/custom native rebasing |
| Skill-creator `quick_validate.py templates/skills/aek-design-feature` | `Skill is valid!`; metadata validation only |
| mypy 2.1.0 strict analyzer | No issues in the checker and three test modules (4 files) |

Before adding the profile, the two new selection tests failed on unknown
`project-workflows` as expected. The final passing tests cover the implemented
closure. Commands are maintained in [verification](../maintenance/verification.md#artifact-checker).
Host Python was 3.12.3; missing host pip/venv support prevented a local analyzer
environment. The analyzer ran instead in the already available `python:3.12-slim`
image with the repository mounted read-only, a read-only root and disposable
`/tmp`. It installed mypy 2.1.0 only in `/tmp/check-tools`, then ran the documented
strict command with `PYTHONPATH=/tmp/check-tools` and cache under `/tmp`.
An initial non-executable tmpfs prevented loading mypy's extension; the corrected
temporary analyzer mount enabled execution and passed. No host packages changed.

At the initial handoff these checks established the static V02/V03 slice and part
of V07; PS-02 and its behavioral criteria remained open. No adoption benefit or
successful source-independent design was claimed from those checks alone.

## Resumed observation — 2026-10-11

The owner requested continuation after the initial handoff. Originals of this
record, the inventory and canonical plan were preserved under
`/tmp/aek-ps02-resume-196yejjc/originals/`; the initial operational input hashes
above still match. Earlier failed observations remain historical results.

Model-free diagnosis reproduced two independent harness problems. With the host
root bound read-only, nested `codex sandbox /bin/echo` failed to create its UID
mapping through `/proc`. Providing a private proc mount fixed that probe.
The native app-server `command/exec` still failed; a file/process syscall trace
identified `EACCES` opening `/dev/null` and `/dev/urandom`. Providing a private
device mount fixed that failure. The corrected bubblewrap prefix is
`bwrap --ro-bind / / --proc /proc --dev /dev`, followed by the existing private
runtime binding, read-only package/plugin/skill/rule bindings, masked source and
temporary paths, and selected fixture binding. Neither native sandbox nor
approval checks were disabled. User files were not made writable.

The local app-server probe then executed Bash in `/tmp/aek-observation`, confirmed
the source README was absent at its ordinary path and read the fixture README,
returning exit code 0 and empty stderr. It used the installed protocol's
`command/exec` with `workspaceWrite`, the fixture writable root, network disabled
and a 10-second timeout; no model call was needed for diagnosis. An outer
sandbox blocked diagnostic tracing/network-namespace operations, so the approved
diagnostic calls ran outside that outer sandbox while retaining this isolation.

Fresh cases reused the recorded fixture inputs, saved model/effort and original
prompts. The implicit case read the native `SKILL.md`, local project-skill guide,
core/planning/verification and Python/Pydantic/FastAPI topics. It produced a design
in `docs/plans/cancel.md`, then reached the 180-second limit during document
verification (harness exit 124, no completed turn). Its output is partial evidence
of implicit selection and technical routing, not a completed native trial.
The retained design SHA-256 is
`e42858e284299fcc187d83f54f79c4488c695cd9b2bbe5f6c9712a409f406c9c`.
Coordinator inspection found the domain/HTTP owners, atomic state replacement,
idempotency, preserved contracts and proposed concurrency checks. A separate
scoped artifact check of this produced task passed: one artifact, zero errors.
The model encountered a missing `python` executable and was retrying with
`python3`; this is not a source-code failure or executed application-test evidence.

The unrelated case completed normally (exit 0 and `turn.completed`). The recorded
commands did not read the design skill or its guide. It read general
Superpowers/verification guidance, changed only README.md, and verified the edit.
Coordinator comparison against all 56 original file hashes confirmed exactly
`servce` → `service`, no other content changes and no added/deleted project files.
This is one observed non-trigger, not a statistical reliability claim.

The explicit case uses a fresh fixture and the recorded `$aek-design-feature`
prompt with a 600-second bound, allowing document verification to finish. It does
not resume or overwrite the interrupted case. No model/effort override, prompt
relaxation, source access, implementation or dependency installation was added.

### Completed explicit result and acceptance

The explicit case finished with exit 0 and `turn.completed`. Commands read the
installed native skill and adopted guide, project sources, selected technical
topics and applicable Superpowers procedures through local adaptations. It kept
one design process and edited only `docs/plans/cancel.md`. The final task reports
design complete, awaiting user review, with implementation still unauthorized.
Its SHA-256 is
`66a27a6ad596c37ecb9e806f025c096c5e0af0dd6d5be86baffcf92ba8e1e829`.

| Acceptance boundary | Observed output and verification |
| --- | --- |
| Actual project owners | `Inventory.cancel(self, reservation_id: str) -> Reservation` in `app/domain.py`; synchronous thin POST handler in `app/http.py`; transport continues to depend on domain |
| State and lifetime | Lookup, cancelled-state check, immutable replacement and stock update in one existing lock; no nested call to lock-taking `get`; guarantee scoped to one process/inventory lifetime |
| Public compatibility | Original ID/quantity, cancelled state and HTTP 200 on first/repeated/concurrent calls; unknown opaque string maps to the existing 404 detail; subsequent GET reflects the replacement |
| Rules affect decisions | Python ownership/typing informs frozen snapshots and lock scope; Pydantic public-output rules inform reuse of the three-field record; FastAPI rules inform the synchronous thin handler and narrow error translation |
| Alternatives and checks | Rejects HTTP-owned transition, deletion, per-reservation locking and new storage/DTO layers; proposes stock-conservation, duplicate/concurrent calls, snapshot, missing-ID and actual HTTP/schema checks |
| Evidence boundary | Runtime tests and strict application analysis explicitly unexecuted; observed checks cover document links/anchors, structure, whitespace and unchanged application hashes |
| Scope and source independence | All 56 fixture hashes compared: only the canonical task changed; no new/deleted project files. Source checkout remained masked, and recorded commands used local adopted rules without accessing its path |

The native turn's inline `python3` check returned exit 0: 23 local links/anchors,
whitespace, task structure and both application hashes passed. Coordinator review
inspected the actual final design against the original requirements and source;
the library checker also passed the produced task (one artifact, zero errors).
These document checks do not certify a future cancellation implementation.

The combined evidence satisfies PS-02's bounded selected-client design and
unrelated-task observation alongside static V02/V03/V07 slice coverage. The
implicit trial's unfinished verification is still recorded as unfinished; it is
not counted as a second successful design. This is not the PS-05 matched
comparison, a controlled Superpowers-present/absent experiment, or support evidence
for other clients. No cost improvement or general trigger reliability is inferred.
The no-skill control was not rerun after harness repair because comparative benefit
is outside this slice's acceptance. The unchanged source/profile/adoption tests
and strict analyzer results above remain valid and were not rerun for prose updates.

After the observations, private runtime/authentication copies and diagnostic
traces were removed. The three changed source progress/evidence documents passed
their scoped artifact check with zero errors; whitespace and baseline review
passed without changes outside the stage's preserved scope. No user configuration,
plugin content, application source or Git state was modified by this resumption.

## Stage 3 source-contract validation — 2026-10-11

PS-03 adds implementation/review templates and expands the shared guide, entry
routes and optional profile. Its pre-edit contents are retained under
`/tmp/aek-ps03-qq8upp1_/originals/`, with 274 original identities and new-path
absence records in `baseline.json`. The PS-02 behavior observations above remain
evidence for their earlier input hashes; they do not validate the changed guide
or this three-entry arrangement. No new model/client trial ran in PS-03.

| Checked input | SHA-256 |
| --- | --- |
| `standards/project-skills.md` | `3d8aae1649c829bc1cf92fa10723fc9300fd0dbeb746e763fbb8b4cbb71a1f36` |
| `standards/superpowers.md` | `914705f0bd47d0b5b1fdf08c0dd8fbea6fa03cbef85dd65cc0532d48e040f22e` |
| `templates/skills/aek-implement-feature/SKILL.md` | `baaeaf1fe4b04dce113ad746d3bd21bb82ffcd4f79053cf1668c7519142136aa` |
| `templates/skills/aek-review-changes/SKILL.md` | `553c583fff0dbc5f820de0ad044fd83f6558b1f3953795f766ad7b170ce69d60` |
| `tests/test_project_skill_adoption.py` | `367787e24e60033b5da0da0cc9b5f7b375299eed46da715fc5d5b029ab78a489` |

The [updated ownership map](2026-10-11-project-skills-reorganization.md#stage-3-ownership-and-overlap-disposition--2026-10-11)
records distinct entry value, the omitted conceptual delivery-phase skill and
overlaps with installed Superpowers 6.4.2. Review covered design approval, canonical
artifacts, progression/Git, testing cadence, review independence, findings/fixes,
delegation/models, language, evidence reuse and missing-plugin fallback. Existing
technical topics keep their owners. The new composition section does not require
the optional profile or call back into its skills.

Executed commands are the source checker, the three documented unittest suites,
skill-creator `quick_validate.py` on each new skill directory, and the documented
strict mypy command over the checker and all three test modules. Results:

| Check | Result |
| --- | --- |
| Full source artifacts | 210 checked; zero errors |
| Artifact/profile/adoption regression suites | 40 / 33 / 7 tests passed; 80 total |
| New skill metadata | Both returned `Skill is valid!` |
| mypy 2.1.0 | No issues in four source files; disposable read-only-source container as documented for PS-02 |
| Catalog comparison to stage baseline | Schema/IDs preserved; 36 profiles and seven required profiles; all profile records except `project-workflows` unchanged |

The extended closure assertions cover all three task resources without adding
technologies. Two new adoption tests check actual native paths for all three
entries and review-only native selection while the other templates stay inactive
in the bundle. The helper remains a fixed empty-root test fixture, not a production
installer. Its cohesive template-copy/adaptation scope was reviewed; the new
parameter selects native entries without adding update/recovery behavior.
Flat/custom native-path tests still cover design only; broader adoption is PS-04.

Coordinator review inspected the actual scoped diff, including both new templates
and changed untracked originals. No material source-contract finding remains.
This is V01 mapping, V02 regression and V08 source review for PS-03. Independent
review was not selected for this additive instruction/template stage; no claim of
independent review or observed implementation/review behavior is made. AC03/AC05
behavioral gates remain pending PS-05, and native mappings for other clients remain
unverified. No consumer code, native configuration, plugin or model setting changed.

## Stage 4 portability and recovery validation — 2026-10-11

The [adoption record](2026-10-11-project-skills-adoption.md) contains the inputs,
reproduction procedure, scenario decisions and evidence limits. The preserved
pre-edit baseline covers 276 files under `/tmp/aek-ps04-9gp8aros`; this addendum
does not revise PS-02 or PS-03 observations to imply testing of newer contents.

| Checked input | SHA-256 |
| --- | --- |
| `MIGRATION.md` | `22c794a9b4a9393b905afce4ea4fd354fc8e87cc52c9238f0535f9129d19c384` |
| `templates/framework/adoption-record.md` | `c86438ab6bc239e4e443ccba805720fababcd1f3639f89aae5d26f2428cb7921` |
| `templates/skills/aek-integrate-project/SKILL.md` | `a24e07c660098180bbd569614a12eeb58f5aaf1198a1a65615408d1d1358b266` |
| `tests/test_project_skill_adoption.py` | `c080607a662210dfdee12cc1645259589bbb57383039b16f460e204dd3e027ac` |
| `tests/test_project_skill_portability.py` | `2797698cbcbe97b1d070db74c20e380cbb637f1ead20ea9e6fd3d13ca9cb3148` |

| Executed check | Result |
| --- | --- |
| Full source artifact checker | 210 artifacts; zero errors |
| Artifact/profile/adoption/portability unittest suites | 40 / 33 / 7 / 4 passed; 84 total |
| Portability matrix within the four new tests | All 15 layout/profile combinations passed, including each of the three native skills |
| Integration skill metadata validator | `Skill is valid!` |
| Strict mypy 2.1.0, documented flags | No issues in five source files; disposable container, source mounted read-only |
| Instruction-led walkthrough | 13 recorded outcomes; real diff3 for independent/conflicting B/C/N changes; accepted snapshots and hashes cross-checked |

The first matrix run exposed nine subcases with unclassified conditional routes;
the reviewed explicit list fixed their preparation without relaxing required-route
checks. The first walkthrough draft exposed an accepted-metadata mistake; the
corrected run hashes adapted snapshots. Final evidence separates synthetic N's
identity from the source manifest and points records to the matching final results.
Original drafts remain retained. The strict analyzer was repeated because its
prior terminal result was unavailable; its successful output is retained in
`/tmp/aek-ps04-9gp8aros/mypy-final.log`. No host packages were installed.

Conflict, missing-base, deletion and collision cases deliberately withhold dependent
writes. Partial recovery deliberately preserves later edits, including the record,
and does not advance accepted state. These are expected procedure outcomes, not
completed consumer imports or evidence of autonomous compliance. The unchanged
three task-skill templates and guide have no new native behavior evidence here.
V02–V06, AC04 and the recovery portion of AC08 are covered at PS-04's specified
file/procedure scope; PS-05 remains the current-arrangement behavioral gate.

## Stage 5 observed behavior and client support — 2026-10-11

The [current behavior record](2026-10-11-project-skills-behavior.md) preserves
self-contained fixture inputs, exact prompts, source/result identities, native
commands, isolation, actual outcomes, token telemetry and limitations. Ten completed
Codex CLI 0.162.1 observations use the saved gpt-6-astra/high configuration: matched
design, implementation, review and small-fix conditions, an unrelated edit, and
explicit review without Superpowers. Every completed trial met its bounded outcome.

Both domain implementations passed three unchanged acceptance tests and strict
mypy 2.1.0; both small fixes passed three focused regression tests and strict
analysis. The review seed was detected, the legitimate exception preserved, and
review-only files unchanged. Both generated designs passed scoped artifact checks.
All three AEK entries were natively discovered and implicitly read; current explicit
review also worked. No real consumer, source rule, plugin or saved setting changed.

The initial private runtime did not natively discover Superpowers. Its completed
control and interrupted candidate remain recorded separately; corrected fresh pairs
share an explicit route to installed 6.4.2 procedures. Automatic plugin activation
is not claimed. The original analyzer command needed namespace-package resolution;
both implementation runs independently passed with `--explicit-package-bases`.
The durable fixture command now includes it without rewriting those initial results.

No consistent cost/quality improvement was established: telemetry varies by task,
outputs can be verbose and this is one unblinded run per condition. Native behavior
claims are bounded to the observed Codex surface; Claude/Cursor retain only their
recorded static/reference limits. PS-05 and PS-06 are satisfied at this scope;
whole-system reconciliation and final acceptance remain PS-07/PS-08. Earlier
84-test/210-artifact PS-04 results remain valid for their unchanged operational
inputs and were not rerun solely because this evidence stage ended.

## Stage 6 integrated source acceptance — 2026-10-11

The [final integrated review](2026-10-11-project-skills-reorganization.md#final-integrated-review-and-acceptance--2026-10-11)
reconciles every original owner/profile with current source and observed native
copies, records finding dispositions, maps AC01–AC08 and retains adoption/rollback
routes. Review was coordinator-only. Current README/architecture/maintenance
statements now point to the completed behavioral observations and their limits;
no normative skill, technology contract, fixture behavior or native setting changed.

Executed checks: all 36 profile closures resolve; 180 of 182 original standards
Markdown files and all 35 original profile records remain byte-identical; modified
shared-route headings survive; three observed native skills and guide match current
adaptation. The checker passed 210 source artifacts and 13 task/evidence/fixture
documents. Strict mypy 2.1.0 passed the documented six-module source command.
Earlier 84 regression tests, 15 portability combinations, 13 instruction-led
adoption outcomes and ten completed native observations remain valid at their
recorded scopes. No repeat model calls, unchanged-stack builds or broad test rerun
were selected solely for final handoff.

AC01–AC08 are satisfied for the stated bounded source package. The support record
still excludes automatic Superpowers discovery in the private CLI runtime,
other-client task activation, statistical quality/cost gains and real consumer
rollout. This is not a claim of universal agent adherence or independent review.
