# Agent-behavior pilot development and execution plan

> Use Superpowers with [local adaptations](../../standards/superpowers.md).
> Follow `executing-plans` inline when this work is selected. Selecting a plan
> does not authorize live runs, target changes, delegation or automatic progression.

**Goal:** Find a concrete improvement opportunity in ordinary AEK use, or retain
the current configuration with explicit evidence limits.
**Spec:** [Agent-behavior pilot](../specs/2026-10-07-agent-behavior-pilot.md).
**Architecture:** Existing client and task workflow, a compact observation
record, and an optional controlled comparison of one instruction change.
**Stack:** Source documentation and Python 3.11+ standard-library artifact tooling;
the isolated Docker fixture uses Python 3.12, FastAPI, Pydantic v2, Uvicorn,
pytest, HTTPX2 and mypy. Docker Compose runs the application and all its checks.
The library itself acquires no runtime dependencies.
**Status:** Stage A completed on 2026-10-11 as one transparent, unblinded
observation in the existing session; awaiting owner review. Stage S remains
complete. Independent fresh-session observation and controlled comparison remain
unexecuted. The observation service is stopped.

## Global Constraints

- Preserve the rules-library scope; no new AEK runtime, CLI, MCP server, SDK or mandatory evaluation dependency.
- Use one selected target, client and bounded task; reuse the owner's recorded sandbox grant, without inferring permission for other projects or additional external model batches.
- Preserve binding user requirements, project gates, permissions, local exceptions and unrelated changes in every condition.
- Use observable artifacts and client evidence; unknown loading, model identity, reasoning effort or token use must remain unknown.
- Keep decisions and progress in one canonical pilot task; retain private transcripts and code outside public source-library evidence.
- Default to inline execution and existing role choices; do not configure or activate delegation for the evaluation itself.
- Run the sandbox application, tests and analyzers in Docker containers; host tooling may prepare files and operate Docker, but is not an application runtime fallback.

## Ownership, authorization and prerequisites

- Source instruction root and current source checkout:
  `/home/vitalii/Documents/Local_Projects/Agent_Engineering_Kit`.
- This file owns workstream-stage decisions and source-support progress. After
  selection, the existing canonical target task owns detailed application/run
  progress and private evidence; reference it without copying its checklist here.
- The [roadmap](2026-10-07-development-roadmap.md) owns portfolio prioritization
  and the current documentation stage, not this future execution checklist.
- On 2026-10-08 the owner supplied
  `/home/vitalii/Documents/Local_Projects/AEK_TEST` for technology setup and tests,
  allowing either scheduling or execution. The documentation continuation took
  the scheduling option; the owner then explicitly instructed execution. Stage S
  reuses that authorization for reversible local
  fixture setup and functional tests; no repeat task-permission question is needed.
- The supplied root is outside the current tool's writable roots. Actual writes
  and restricted dependency downloads require the tool's applicable escalation;
  this is an execution permission boundary, not missing user task authorization.
- The sandbox and cancellation scenario are selected. Record the actual client,
  observed model/effort and evidence access before stage A; additional paid runs,
  a candidate treatment and any comparison envelope remain unselected.
- Future execution remains in the selected current checkout by default. Optional
  disposable trial copies and any external calls need their actual task scope.
  No staging, commits, branches, worktrees, pushes or public deployment are implied.
- Capture fresh scoped originals/prior absence before any future source or target
  write. The documentation-stage baseline does not cover later application work.
- Reuse existing client/model/effort choices. Their observed evidence, including
  unknown values, belongs in the selected pilot record; no setup skill is forced.

**Current item:** None active. LAB-01 through LAB-04 and PIL-01 through PIL-03
are complete for the recorded unblinded mode; stage A is awaiting owner review.
**Next checkpoint:** Owner review of the completed observation and the skill-library
assessment. Formal stage C disposition may reuse this evidence. No candidate
instruction treatment, comparison batch or new skill implementation is selected.

## Review focus

- A quick result can be incomplete: acceptance and preservation precede efficiency.
- Shared global context, cache, model drift or dirty input can invalidate attribution.
- Instrumentation can change behavior: prefer existing events and ordinary prompts.
- Missing telemetry must remain unknown; avoid double-counting cached tokens.
- Failed/aborted runs and negative findings must remain visible.

## Stage S — Final preparation: provision AEK_TEST

**Purpose:** Produce one checked starting application and adopted instruction
bundle before observing an agent task. This is the final step of preparation,
not a step after stage C's conclusions.
**Files:** Under the supplied sandbox root only: `README.md`, `seed/` application
and instruction files listed in the spec, and setup evidence in
`evidence/setup/`. Create `runs/observation-01/project/` from the verified seed
after preparation; its detailed application task is owned locally when started.
**Consumes:** The spec's selected sandbox contract, recorded user grant, current
source contents and applicable Python/FastAPI/Pydantic rules.
**Produces:** A reproducible fixture, a clean initial observation copy and an
honest handoff separating setup checks from unexecuted agent observation.

- [x] **LAB-01:** Recheck sandbox contents, ancestor instructions and interpreter;
  preserve any newly present contents before writing. Record scoped absence or
  originals and actual source identity including relevant uncommitted contents.
  Resolve compatible exact dependencies against official release contracts in
  Docker; prepare a fully pinned `requirements.lock` and base image digest.
  Record container Python/platform, Engine/Compose and installed versions.
- [x] **LAB-02:** Implement the spec's starting reservation API, focused domain
  and HTTP tests, strict typing configuration, Dockerfile, Compose configuration,
  context exclusions and container reproduction README.
  Keep cancellation absent from the seed. Check invariants including failed-request
  preservation, competing reservations and independent app state. Review the
  actual files and run the scoped application checks below.
- [x] **LAB-03:** Adopt required assets plus `python`, `fastapi`, `pydantic` and `docker`
  through MIGRATION's inventory/profile/prepare-and-apply procedure. Adapt target
  AGENTS/PLANS routes and accepted contents; validate the contained bundle using
  the source checker. Do not export source-maintenance AGENTS or activate unrelated
  profiles/native settings. The source plan remains the workstream owner.
- [x] **LAB-04:** Preserve the checked seed with a content manifest excluding
  volatile environments/caches. Create the observation copy and build its image
  from the same lock/base; run its baseline checks to verify reproduction.
  Start the API through Compose, check real HTTP behavior and clean shutdown.
  Record setup commands/results and unresolved client evidence in `evidence/setup/`.
  Hand off the cancellation request for a fresh session; no comparison or benefit
  result is inferred from preparation. Leave runtime pilot items unchecked.

From the seed root, after its container files exist:

```sh
docker compose -p aek-seed config --quiet
docker compose -p aek-seed build
docker compose -p aek-seed run --rm --no-deps api python -m pip check
docker compose -p aek-seed run --rm --no-deps api python -m pytest -q
docker compose -p aek-seed run --rm --no-deps api python -m mypy --strict app tests
docker compose -p aek-seed up -d --wait --wait-timeout 60
```

Expected: compatible installed dependencies, all starting-contract tests pass,
and no typing errors. Verify health and a business request through the listener,
then stop this owned Compose project and inspect its exit evidence. Build the
observation copy under project name `aek-observation-01` and run its baseline
checks; preserve unrelated Docker projects, images and volumes.
The setup record retains commands, versions and actual results, not predictions.

From the source root, after adoption, use the existing CLI contract:

```sh
python3 tools/check_instruction_artifacts.py --root /home/vitalii/Documents/Local_Projects/AEK_TEST/seed --bundle-dir .agents-framework --profile python --profile fastapi --profile pydantic --profile docker
```

Expected: exit 0 with no artifact diagnostics for the selected profile closure,
root Markdown entries and adoption record. Explicit file arguments replace this
body selection; do not accidentally narrow it to entries alone. Inspect adapted
entries and local instructions as well; the checker does not establish native
client discovery.
Verify that project copies retain relative routes and baseline content identities.
No runtime test of an unchanged source-library technology fixture is required.

**Exit:** PIL-AC11, PIL-AC12 and PIL-AC14 hold, with PIL-AC15's limits recorded.
Missing tool permissions or package access blocks only dependent provisioning;
keep partial state and resume without destructive cleanup. If a directory that
was empty now contains user work, inspect and preserve it rather than resetting it.
Do not add a database or a second stack to work around an unrelated environmental
obstacle. Docker is mandatory under the owner's execution clarification.

## Stage A — One selected task, with observation

**Purpose:** Obtain useful evidence before changing any instruction.
**Files:** No source-library implementation file is required. Read relevant target
entries, adopted identity, task and local commands. Write only the already-selected
canonical target task/report and application files authorized by that task.
**Consumes:** The spec's inputs, selected permissions and current configuration.
**Produces:** One observation record under the spec's minimal evidence report and
one of its explicit outcomes; a sanitized reference may be retained here.

- [x] **PIL-01:** Select the target/client and useful bounded task; establish its
  acceptance, starting-state representation, canonical record and permitted actions.
  For the chosen sandbox, reuse `runs/observation-01/project/` and the cancellation
  contract after stage S; do not repeat stack selection. Record known/unknown
  native model and tool evidence. Independent observation requires a fresh session
  without completed solutions or prior transcripts; the 2026-10-11 run instead
  uses the explicitly recorded transparent unblinded mode below.
- [x] **PIL-02:** Execute that ordinary authorized task to its normal checkpoint.
  Preserve baseline contents and collect already-available artifacts/events.
  Do not add a separate narrated rule inventory to the evaluated task prompt.
- [x] **PIL-03:** Review acceptance and preservation, then classify material
  repeated work or instruction omissions using actual evidence. Record whether
  any candidate improvement question exists and whether evidence can support it.

**Checks:** The selected task's required checks and scoped diff/preservation
review. Reuse valid results. Inspect observations against PIL-AC01, PIL-AC04,
PIL-AC07, PIL-AC08, PIL-AC10, PIL-AC13 and PIL-AC15. The sandbox task needs its
domain/HTTP acceptance and scoped typing checks; the AEK source library needs
no application build. Independently inspect stock after repeated/concurrent
cancellation; passing tests written by the evaluated agent alone are insufficient.

**Exit:** An evidence-backed observation, including an honest inconclusive result.
If no material issue is identified, recommend retaining the configuration and
stop. Do not enter stage B merely because it exists in this plan.

## Stage B — One controlled comparison, only if justified

**Entry gate:** Stage A yields an actionable question; the owner selects one
candidate and the additional execution envelope. A client with insufficient
isolation/evidence can leave the result inconclusive without additional setup.
**Files:** Candidate instruction files and isolated task inputs in the selected
trial locations; the canonical pilot record. Do not change accepted source or
target instructions as a side effect of preparing a treatment.
**Consumes:** Stage A's hypothesis and current accepted baseline.
**Produces:** A predeclared comparison contract and identified run records.

- [ ] **PIL-04:** Name the single treatment and verify its exact diff, task input,
  independent acceptance oracle, client/model/effort, tool set and initial files.
  Record intended order/repetitions and the authorized resource boundary before runs.
- [ ] **PIL-05:** Prepare approved independent sessions and starting states.
  Account for local/untracked inputs, global instructions and environment/cache
  differences. Keep golden solutions and other runs' outputs outside agent access.
- [ ] **PIL-06:** Run only the selected paired experiment; retain all terminal
  outcomes, evidence and interruptions. Do not change the treatment midway or
  repeat until a desired result appears. Stop at the authorized boundary.

**Checks:** Verify the starting-state equality excluding the declared treatment;
inspect each final diff and independently assess the same acceptance criteria.
Cover PIL-AC02, PIL-AC03, PIL-AC05, PIL-AC06 and PIL-AC08. A changed environment
invalidates affected attribution, not necessarily the underlying task's own result.

**Exit:** Comparable evidence or a precisely stated comparison limitation. One
pair is diagnostic; repeated pairs remain a small personal sample. No required
minimum run count overrides the user's execution envelope.

## Stage C — Decision and scoped follow-up

**Files:** Existing canonical pilot record; this plan only for stage outcome and
approved sanitized evidence references. A resulting code/rule repair has its own
existing task owner or separately approved implementation scope.
**Consumes:** Observation or comparison evidence, including failed runs.
**Produces:** Retain, propose correction, investigate adoption, inconclusive or stop.

- [ ] **PIL-07:** Compare quality and preservation first. Report per-run results,
  material behavior evidence, available efficiency measures and confounders.
  Reject unsupported savings claims and distinguish user wait from known execution
  time when the evidence allows it.
- [ ] **PIL-08:** Present the smallest supported next action for owner review.
  If no benefit is demonstrated, close the experiment without adding a feature.
  A useful correction is a proposal; implementation/rollout needs its selected scope.

**Checks:** Cover all applicable acceptance IDs, particularly PIL-AC03, PIL-AC04,
PIL-AC06 and PIL-AC09. Confirm unknown values were not converted to zero and native
token categories were not double-counted. Reviewer judgment must cite evidence,
not an agent's unsupported self-report or private reasoning.

**Exit:** Reviewed recommendation, with unresolved evidence limits preserved.

## Stage D — Optional reusable procedure after repeated utility

**Entry gate:** Actual use demonstrates recurring value in retaining the protocol;
ordinary MIGRATION guidance is insufficient for convenient repeatability. Otherwise
mark this stage deferred with a reason, not completed implementation.
**Files:** Create `docs/maintenance/agent-behavior-pilot.md`; modify only the
relevant pilot route in `MIGRATION.md` and, if needed for discovery, the status/pilot
section of `README.md`. No catalog, checker, skill or policy-setting change.
**Consumes:** Reviewed useful observation/report practice and the existing owners.
**Produces:** One conditional operational procedure; the report outline stays in it.

- [ ] **PIL-09:** Promote the concise procedure and report outline from the tested
  practice. Link existing policy owners and omit private examples. Do not turn
  pilot instructions into always-loaded requirements or compulsory extra checks.
- [ ] **PIL-10:** Validate affected documents, report ownership and the conditional
  route; document runtime evidence separately from source artifact validity.

Run from the source root after those files exist:

```sh
python3 tools/check_instruction_artifacts.py MIGRATION.md README.md docs/maintenance/agent-behavior-pilot.md
git diff --check
```

Expected: exit 0 and no artifact diagnostics; inspect newly created files separately.
Omit unchanged README from the scoped command if it was not edited. No new unit
test suite is needed for this documentation promotion. If an executable helper
becomes necessary, stop to define that distinct change and its behavior checks.

## Acceptance coverage and stopping

| Spec criteria | Owning stage |
| --- | --- |
| PIL-AC01 | A, C |
| PIL-AC02, PIL-AC05 | B |
| PIL-AC03 | B, C |
| PIL-AC04, PIL-AC10 | A, C |
| PIL-AC06 | B, C |
| PIL-AC07, PIL-AC08 | A, B |
| PIL-AC09 | C, D |
| PIL-AC11, PIL-AC12, PIL-AC14 | S |
| PIL-AC13 | A, B when the sandbox task is compared |
| PIL-AC15 | S, A, B, C |

Stage boundaries follow the default human checkpoint. No automatic transition to
another project, client, tool or paid batch follows a completed observation.
For a resumed pilot reconcile the canonical record and relevant actual state;
reuse valid evidence instead of rerunning the complete experiment by default.
Additional automation, publication and rollout remain outside this plan.

## Execution evidence

### Stage S started — 2026-10-08

The owner instructed execution after the evidence-status clarification. Work
proceeds inline without Git writes. Source-plan/roadmap originals, source status,
HEAD and the empty target inventory are preserved under
`/tmp/aek-pilot-execution-84oy8_j4`. No ancestor AGENTS.md was found on the
target path. Prepare and test in that temporary directory before publishing
the fixture to the supplied sandbox through the required filesystem permission.
Runtime evidence will name the actual installed package versions and checks.

**Execution clarification:** The owner required all project execution in Docker.
The initial temporary host-venv preparation is superseded. An eight-case domain
red run failed on deliberate stubs; after domain implementation, eight domain
checks passed before the host HTTP run stalled and was interrupted (exit 130).
That incomplete host run is not acceptance evidence. Continue application and
analyzer verification only in containers. Pre-clarification document copies are
under `/tmp/aek-pilot-execution-84oy8_j4/before-docker`.

**LAB-01 evidence:** Docker CLI/Engine 29.8.2, Compose 5.6.0; Linux amd64 base
`python:3.12-slim@sha256:05cda9777409a9c3ffddd94a4c476b79f0769a0b4857f0c7ed9226b6800b0d6f`.
The prepared image installed the exact lock (FastAPI 0.138.0, Pydantic 2.13.4,
Starlette 1.7.0, HTTPX2 2.13.1, Uvicorn 0.49.0, pytest 9.0.2, mypy 1.19.1).
Container `pip check` reported no broken requirements. HTTPX2 is selected from
the installed Starlette contract, not by changing historical source examples.
The seed HTTP red run in Docker had 25 expected failures against the route-less
factory; implementation and final container acceptance follow that evidence.

**LAB-02 evidence:** The implemented seed passed 33 domain/HTTP tests in Docker.
mypy initially identified four generated Pydantic-constructor Any diagnostics;
the existing `standards/pydantic/verification.md` owner prescribed the missing
plugin and strict constructor settings. After applying them, container mypy
reported no issues in five source files. No diagnostic suppression was added.
Container pip check is clean; runtime Python is 3.12.15 and UID is 10001.
The prepared bundle checker passed 57 artifacts. Files and preserved setup results
remain under the execution baseline until the target copy and its checks succeed.

### Stage S completed — 2026-10-08

The fixture was published to `/home/vitalii/Documents/Local_Projects/AEK_TEST`
after rechecking the empty-directory baseline. `seed/` retains the initial API;
`runs/observation-01/project/` is the independently built observation copy.
Both contain project-specific instructions and the selected contained bundle.
Source maintenance AGENTS was not exported and no native roles were activated.

**Durable evidence:** Sandbox `evidence/setup/report.md` summarizes the scope;
`checks.json` preserves 19 target commands with timestamps, stdout/stderr and
exit codes, all zero. `preparation-checks.json` records container Python 3.12.15,
runtime UID 10001 and all 26 package versions. `seed-manifest.json` identifies
68 starting files and matches the observation copy. `adoption-manifest.json`
and `accepted-instructions/` preserve identities/bytes of 55 imported files;
the adoption record is retained separately. No host virtual environment was
copied into the sandbox.

| Evidence | Result and scope |
| --- | --- |
| Seed and observation artifact checks | Each checked 57 artifacts, zero errors, with the four selected profiles |
| Observation dependency check | No broken requirements |
| Observation tests | 33 domain/HTTP cases passed in Docker, warnings as errors |
| Observation static analysis | Strict mypy passed for all five app/test source files with Pydantic plugin |
| Real server behavior | Uvicorn served health, strict input rejection, reservation create/read, 409 conflict and 404 missing item; stock preserved on rejected writes |
| Shutdown | Seed container exited 0, no OOM; application shutdown completed in logs |
| Reproduction | Observation image built from copied inputs; its starting files match the seed |
| Running handoff | `aek-observation-01-api-1` healthy, bound to `127.0.0.1:18080`, initial stock 10; seed container stopped |

PIL-AC11, PIL-AC12 and PIL-AC14 are satisfied within this setup scope. PIL-AC15's
evidence limits are preserved. PIL-AC13 remains untested: cancellation is deliberately
absent. The saved model-selection outcome is unresolved, not an invented deferral;
ordinary inline work used the current session, and no model/effort assignment or
native discovery result is claimed.

The sandbox root README contains Docker commands. A normal cancellation request
is prepared at `evidence/observation-01/request.txt` for the next fresh session.
Do not include operator reports or previous solutions as its task context. The
source plan owns stages; the new application task will own detailed progress.
This completes the selected preparation stage under the default human checkpoint.
Stages A-C and optional feature packaging remain unexecuted, not implicitly complete.

### Owner-requested pause — 2026-10-08

The owner requested safe shutdown and a detailed continuation prompt. The owned
observation service was stopped using its exact Compose project/file; Docker
inspection confirms `Running=false`, `ExitCode=0`, `OOMKilled=false`, and no
runtime error. It finished at `2026-10-07T23:26:26.914575954Z`
(2026-10-08, Europe/Belgrade). A scoped Docker listing found no running `aek-`
containers. The earlier running handoff above remains historical setup evidence.

Application files, the checked seed, observation copy, images and existing evidence
were preserved. In-memory application state is intentionally reset on startup;
there is no database or volume migration to resume. No agent task was started and
all PIL items remain unchecked. No Git staging, commit, branch or worktree was made.

Durable shutdown evidence is in sandbox `evidence/setup/pause-2026-10-08.json`;
`RESUME.md` describes restart commands, the next scope and evidence boundaries.
Pre-pause copies of the affected handoff documents are retained in sandbox
`evidence/setup/before-pause-2026-10-08/` as well as the temporary execution baseline.
Do not rebuild the seed or repeat stack research merely because a new session
begins. Reconcile any intervening edits before resuming. Use the prepared ordinary
request in a fresh observation session, without feeding operator reports into the
evaluated task. Broader feature development and controlled comparison remain gated.

### Prior planning-stage preflight

Read-only preflight on 2026-10-08 found the supplied sandbox empty and Python
3.12.3 available; inspected application dependencies were absent from that
interpreter. No files were provisioned and no application checks or fresh-session
pilot were run. This does not complete LAB-01's remaining setup requirements.
Document preparation is tracked in the roadmap. Future outcomes name the actual
evidence/state they cover; a deferred stage is not completed implementation.


### Unblinded observation started — 2026-10-11

The owner requested inspection, execution and recorded observations for AEK_TEST.
The existing session executes the prepared cancellation task inline with no
workers. This is the specification's permitted transparent unblinded observation,
not the fresh-session variant described in PIL-01. The fresh-session prerequisite
is superseded for this run only; a future independent experiment remains separate.
Preparation reports and source policies have already entered the context, and
this conversation also researches skill design. Therefore task-level cost, native
instruction discovery and AEK's causal benefit cannot be isolated.

The host identifies the assistant as Codex; native client version, runtime model
identifier, reasoning effort and token/billing telemetry are unavailable. No model
selection file exists in the target. No configuration or model change is made.
Both seed and observation copies match all 68 hashes in the setup manifest, with
no extra files. Both owned containers were stopped at entry. Scoped source
originals and the application baseline are preserved under
`/tmp/aek-observation-20261011-69j77q1q`; durable target baseline and run evidence
use `AEK_TEST/evidence/observation-01/run-2026-10-11/`. That report owns detailed
run evidence, while this plan remains the pilot progress owner.

Implementation design: expand the frozen reservation status to active/cancelled;
perform lookup, first cancellation and stock restoration under the existing lock;
return the stored cancelled snapshot on retries. The HTTP route translates the
existing not-found exception and preserves the explicit response shape. Five
focused tests cover stock restoration, immutable snapshots, concurrent calls,
HTTP projection and missing IDs. A separate live probe will verify public state
without importing application internals. Dependencies and adopted rules stay fixed.

The first Docker inspection failed because the sandbox could not access
`docker.sock`; the escalated read succeeded. This is an environment permission
event, not an application failure. Target writes similarly require filesystem
escalation. Red tests are now installed after baseline preservation; implementation
and acceptance remain pending.


### Stage A completed in unblinded mode — 2026-10-11

**Retained outcome: successful completion of one pilot task.** This section is
the self-contained result retained in AEK. Understanding it does not require the
disposable test workspace. Historical setup paths elsewhere in this plan describe
the original run location; they are not dependencies of this outcome record.

**Fixture and task:** A small Python/FastAPI HTTP service kept item stock and
reservations in memory, with an existing lock protecting state changes. Creating
a reservation consumed stock. The task added `POST /reservations/{id}/cancel`:
an active reservation becomes cancelled and restores its quantity exactly once;
repeated or concurrent cancellation returns the same cancelled representation
with HTTP 200. Reservation ID, item ID and quantity remain unchanged. Lookup
reflects cancellation. An unknown ID returns HTTP 404 with
`{"detail":"reservation_not_found"}` and leaves state unchanged. Existing
behavior, dependencies, container configuration and adopted instructions were
to remain intact. Application execution and checks ran in Docker.

**Execution and evidence scope:** The coordinator implemented the change in the
existing session with AEK references and Superpowers procedures already in
context. This was one transparent, unblinded observation, not an independent
fresh-session or controlled comparison. Six fixture files changed: domain and
API modules, their two test modules, README and architecture documentation. The
original run captured 11 Docker command records, before/after manifests and an
application diff. Raw logs and fixture copies were stored in the disposable
workspace; this retained summary does not archive those artifacts or promise
their availability after workspace deletion.

Five new tests first failed for the missing cancellation method/route and error
body. After one implementation, all 38 fixture tests passed in Docker and strict
mypy reported no issues in five source files. The selected target bundle check
passed 57 artifacts. The real Uvicorn probe issued twelve concurrent cancellations,
verified one stock restoration, then reserved seven units and verified an old
cancellation replay left stock at three. Missing-ID 404, preservation, lookup and
OpenAPI checks passed. The coordinator inspected the actual six-file project diff,
including the complete locked state transition and unchanged existing callers;
there is no unresolved material finding. No independent reviewer ran.

The seed retains all 68 original hashes. Adopted instructions, dependency/container
inputs and model setup were not edited. Observed container versions were Python
3.12.15, FastAPI 0.138.0, Pydantic 2.13.4, Starlette 1.7.0, HTTPX2 2.13.1,
Uvicorn 0.49.0, pytest 9.0.2 and mypy 1.19.1; the process ran as UID 10001.
Main shutdown exited 0 without OOM and
logs confirm application shutdown completed. A health-probe exit 137 overlapped
shutdown, leaving a final unhealthy health record; this is retained separately
from the successful live checks and main-process result.

**Interpretation:** The task met its contract using existing AEK references and
Superpowers procedures; no observed material instruction defect justified a new
language/coding/review skill. Repeated broad documentation reads produced truncated
output, suggesting narrower reads as a working improvement. The active target
PLANS.md retains a pre-existing template-installation note, an incidental editorial
finding left unchanged during observation. Neither fact establishes a new tool need.

PIL-AC01, PIL-AC04, PIL-AC07, PIL-AC08, PIL-AC10, PIL-AC13 and PIL-AC15 are covered
within the unblinded observation limits. Token/model/discovery values remain unknown;
no causal benefit, savings or cross-stack claim is made. Recommend retaining current
instructions. Stage B remains unselected; stage C's formal owner disposition and
stage D's conditional reusable packaging are not marked complete by this report.
The source feasibility note contains the dated vendor research and skill allocation
recommendation. No new skill, policy, catalog entry or runtime service was created.


**Documentation verification for the 2026-10-11 handoff:** The scoped source
artifact command checked the pilot plan, roadmap and feasibility note: three
artifacts, zero errors. A target-root invocation with the existing nested bundle
and explicit README, RESUME and observation report checked three artifacts with
zero errors. The earlier target-project invocation checked 57 artifacts. Git
whitespace checks passed, including separate no-index checks for 15 changed/new
file pairs against scoped originals or absence. Actual application/source diffs
were reviewed; final seed and application manifests each match their expected
68-file state. No unchanged application tests were rerun for report-only edits.
