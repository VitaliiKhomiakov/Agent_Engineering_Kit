# Agent-behavior pilot specification

**Status:** Sandbox setup completed on 2026-10-08 with mandatory Docker; actual
checks are recorded in the plan. No independent agent pilot or comparison has run.
**Date:** 2026-10-07.
**Updated:** 2026-10-08, supplied AEK_TEST sandbox and preparation scenario.
The owner's subsequent execution instruction requires Docker for every
application, test and analyzer run; it supersedes the original host-venv design.
**Implementation plan:** [Pilot plan](../plans/2026-10-07-agent-behavior-pilot.md).
**Rationale:** [Feasibility assessment](../research/2026-10-07-development-feasibility.md).

## Outcome and justification

Establish whether the owner's current use of AEK has a concrete improvement
opportunity, using observable task results and bounded effort. If no problem is
observed, retain the current library and report the limits of the observation.
There is no requirement to produce a new feature or a positive efficiency result.

The owner has not reported a critical problem. Prefer one ordinary, useful task
in one selected project/client using the current rules. The owner's subsequent
sandbox request selects a small synthetic precursor described below; it can
expose concrete mistakes but does not establish benefit in everyday projects.
It reuses [MIGRATION's bounded pilot](../../MIGRATION.md#phase-4-bounded-pilot).
This specification adds a repeatable observation/comparison contract, not another
mandatory stage for all development or routine library maintenance.

## Global Constraints

- Preserve the rules-library scope; no new AEK runtime, CLI, MCP server, SDK or mandatory evaluation dependency.
- Use one selected target, client and bounded task; reuse the owner's recorded sandbox grant, without inferring permission for other projects or additional external model batches.
- Preserve binding user requirements, project gates, permissions, local exceptions and unrelated changes in every condition.
- Use observable artifacts and client evidence; unknown loading, model identity, reasoning effort or token use must remain unknown.
- Keep decisions and progress in one canonical pilot task; retain private transcripts and code outside public source-library evidence.
- Default to inline execution and existing role choices; do not configure or activate delegation for the evaluation itself.
- Run the sandbox application, tests and analyzers in Docker containers; host tooling may prepare files and operate Docker, but is not an application runtime fallback.

## Scope and non-goals

In scope: record a task contract, inspect available evidence, evaluate acceptance,
identify a possible cause of unnecessary work, and optionally compare one scoped
instruction change. Provide an honest recommendation with evidence limits.

Out of scope: model rankings, a multi-client benchmark, full profiling of every
technology, automated prompt optimization, continuous monitoring, statistical
claims about all future tasks, or automatic changes to the accepted library.
No root `PLANS.md`, native client configuration or production installation is
created as a prerequisite for source maintenance.

## Inputs and preparation

Resolve these from the selected task before dependent execution. Reuse supplied
choices rather than running a new onboarding questionnaire.

| Input | Required interpretation |
| --- | --- |
| Target and checkout | Actual instruction root, application repository, execution directory and permitted disposable-copy location, if any |
| Current task | Useful bounded request; acceptance scenarios; mandatory checks; permitted actions and stopping point |
| Current instructions | Adopted AEK identity and relevant local/native instructions; preserve their contents or verifiable identity |
| Client and model | Reported client/version, available model/effort evidence, enabled tools/skills and global-context limits |
| Evidence access | Available task artifacts, commands, ordinary tool events and token statistics; approved storage/retention |
| Resource envelope | Authorized run count and execution budget/time boundary for any extra runs; no extra paid runs by implication |
| Candidate, only for comparison | One named change, its hypothesis and its exact difference from the current configuration |

If active global instructions cannot be inventoried, record the limitation.
An observational result can still be useful; a causal attribution may be impossible.
Do not inspect unrelated home directories, credentials or other projects merely
to complete the inventory. Use client-supported evidence within the selected scope.

## Operating modes

### P1 — Observe one selected task

Run the already-authorized task through the usual client. Preserve its normal
acceptance and human checkpoints. Do not make the agent narrate every rule or
add artificial diagnostic steps to its prompt: that changes what is being observed.
Use existing trace/output facilities where available. Reuse relevant executed
checks instead of rerunning them merely to populate the pilot report.

Record the result after the task's natural checkpoint. Classify a candidate issue
as observed, suspected or not assessable. A long task is not automatically waste;
necessary exploration, TDD, repairs and required checks need their ordinary rationale.

If the task passes and no useful improvement hypothesis emerges, finish with
`retain current configuration`. This is a successful pilot outcome, not proof
that every future task will behave correctly.

### P2 — Compare one candidate, only when justified

Use the same task input and initial project state in independent clean sessions.
The baseline is the current accepted configuration; the candidate differs only
by the selected instruction or route change. Keep model/effort, tool availability,
project gates and environment as constant as the client allows. Do not compare
a real coding harness with a plain model response and attribute the result to AEK.

Use preselected paired runs within the authorized envelope. Alternate baseline
and candidate order when repeating, record cache/environment differences, and
do not share a baseline solution, transcript or candidate output with another run.
Independent disposable copies are preferable when write-capable comparison is
authorized; do not reset, clean, stash or repurpose the user's active checkout.
Capture dirty/untracked inputs explicitly; a Git revision alone may be incomplete.

Choose repetitions before viewing results. One pair is diagnostic only. Two
pairs can expose some variability but still cannot support broad statistical
claims. Additional runs require remaining authorized scope and a question they
can resolve; do not repeat until the preferred outcome appears.

If a candidate changes several policies, cannot preserve necessary gates, or
requires another model/tool change, narrow it or report the comparison as
confounded. Changed treatment contents start a separately identified comparison.

### P3 — Interpret and decide

Evaluate acceptance before efficiency. A faster incomplete result cannot win.
Do not reward unnecessary tests, fabricated coverage or skipped required gates.
Distinguish an incomplete task, a product defect, an environmental failure and
missing observation data. Preserve failed/aborted run records in the denominator.

Possible outcomes:

| Outcome | Meaning and next action |
| --- | --- |
| Retain current configuration | No material issue or useful candidate benefit demonstrated; close this experiment |
| Propose one correction | Evidence supports a scoped change; present it under the existing implementation/review workflow |
| Investigate adoption | Evidence points to an instruction path, exception or setup problem; use a bounded diagnostic |
| Inconclusive | Quality, comparability or observation is insufficient; state the missing evidence without inventing success |
| Stop experiment | Resource boundary, missing permission or a material preservation risk prevents further runs |

A candidate is eligible for limited rollout only when required acceptance passes,
no material contract/preservation regression is observed, and the identified
benefit is supported by artifacts or events. The owner decides whether the benefit
justifies maintenance and any added time. No universal savings threshold is imposed.

## Scenario selection

This is a menu, not a compulsory suite. Select an ordinary project task or the
explicitly selected sandbox task; add only cases relevant to the suspected
problem. Supply the starting code, but withhold completed reference solutions
and other runs' outputs from an independent agent run.

| ID | Suitable task | Evidence of success | Failure this can expose |
| --- | --- | --- | --- |
| CASE-01 | Small documentation or local code correction | Requested change, preserved nearby content, sufficient scoped checks | Scope expansion, unnecessary setup or repeated unrelated checks |
| CASE-02 | Known bounded behavior defect | Independent reproduction/acceptance check and preserved adjacent contract | Fast but incomplete repair, trivial self-confirming tests |
| CASE-03 | Work in a narrowly selected stack | Correct actual language/framework behavior and applicable rules | React interpreted as Next.js/TypeScript; Python interpreted as FastAPI |
| CASE-04 | Resume an existing canonical task | Correct next item, preserved decisions, valid evidence reused | Duplicate plans, lost state, repeated completed work |
| CASE-05 | Prepare an instruction update | Reviewable B/C/N proposal, local exception retained, no unauthorized writes | Resetting local changes or treating raw source as adapted target content |
| CASE-06 | Version-sensitive API question | Source and version match, independently verified behavior when required | Applying latest documentation to an older target |

CASE-05 is preparation-only unless its own task explicitly authorizes application.
CASE-06 uses ordinary approved documentation access; Context7 is one optional
source, not a pilot dependency. Native auto-loading need not generate a file-read
event: absence of such an event alone does not prove failure to load instructions.

## Selected sandbox — AEK_TEST

### Purpose, stack and boundaries

The owner supplied `/home/vitalii/Documents/Local_Projects/AEK_TEST` on
2026-10-08. Read-only inspection found it empty; Python 3.12.3 is available.
The inspected interpreter has no installed FastAPI, Pydantic, Starlette, HTTPX,
pytest or Uvicorn distributions. This does not describe every environment on
the machine. Recheck the directory and interpreter before provisioning.

Use Python 3.12, FastAPI, Pydantic v2, Uvicorn, pytest, HTTPX2/TestClient and strict
mypy checks inside Docker. The user made container execution mandatory during
setup. Keep dependencies in the fixture image; the AEK library acquires no
application dependencies. Resolve and record compatible exact
versions at setup, including transitive packages, from the affected official
release contracts. Do not describe a future resolution as already tested or
upgrade the source library's historical fixtures to match it. The
[research addendum](../research/2026-10-07-development-feasibility.md#sandbox-feasibility-addendum--2026-10-08)
records reviewed sources and their limits.

A small reservation API exercises Python typing, HTTP validation, pure domain
invariants, test selection and profile routing. Docker Compose owns the required
runtime and verification entry points. No database, ORM, frontend or authentication
service is needed. In-memory state is intentional: single process, no persistence or
multi-worker consistency claim. Add another stack only if a concrete failure
cannot be assessed with this one.

### Layout and adoption

All paths below are relative to the supplied sandbox root:

| Path | Responsibility |
| --- | --- |
| `README.md` | Operator instructions, selected environment and evidence limitations; no always-loaded workspace policy |
| `seed/` | Verified starting application and adapted target instructions, kept unchanged during observations |
| `runs/<run-id>/project/` | Independent copy opened as the actual target project; same starting contents except a declared comparison treatment |
| `evidence/<run-id>/` | Setup/run identities, checks and permitted observations outside the application target; no duplicate task checklist |

The seed contains `app/__init__.py`, `app/domain.py`, `app/api.py`,
`tests/test_domain.py`, `tests/test_http.py`, `pyproject.toml`,
`requirements.lock`, `Dockerfile`, `compose.yaml`, `.dockerignore`, `.gitignore`,
and a short application README. Keep domain
code separate from Pydantic/HTTP transport; do not add speculative repository,
service or plugin layers. Build each run image from its own source and the same
lock/base digest; never copy host virtual environments into images or projects.

Adopt the selected `python`, `fastapi`, `pydantic` and `docker` profiles, their required
assets and catalog dependency closure through [MIGRATION](../../MIGRATION.md).
Use contained `.agents-framework/` resources, a project-specific `AGENTS.md`,
adapted `PLANS.md`, and the normal adoption record/accepted-content mechanism.
Never export AEK's source-maintenance `AGENTS.md`. Availability of a dependency
profile is not a direction to read every file; no SQLAlchemy/PostgreSQL profile
is selected merely because FastAPI is present. Docker is selected by the user's
explicit runtime requirement. Do not activate unrelated
native configuration, model setup or skills.

The linked source plan owns workstream stages. A selected application's substantive
task uses its own canonical `docs/plans/reservation-cancellation.md`, created
when the task begins; it owns detailed implementation progress. Evidence records
link to it. Do not copy this source workstream plan into every project as another
editable checklist. Git initialization or commits are unnecessary for the fixture;
scoped content manifests and preserved starting files can identify its state.

### Starting application contract

Each `create_app()` instance starts with `widget` stock of 10 and no reservations.
No request validation or serialization mutates domain state. Mutations are atomic
within the process; concurrent requests cannot reserve the same remaining stock.
Use a small domain critical section rather than claiming multi-process guarantees.

| Operation | Required result |
| --- | --- |
| `GET /health` | 200, `{"status":"ok"}` |
| `GET /inventory/widget` | 200, `{"item_id":"widget","available":10}` initially; reflects successful reservations |
| `GET /inventory/{unknown}` | 404; no inventory creation |
| `POST /reservations` with `{"item_id":"widget","quantity":3}` | 201; object with unique opaque string `id`, `item_id`, integer `quantity`, and `status:"active"`; available stock becomes 7 |
| `GET /reservations/{id}` | 200 with the same stored reservation; missing ID is 404 |
| Invalid body | 422 for quantity outside 1..10, fractional values, booleans, strings, null, missing fields or extra fields; item_id must be a strict nonempty string; no state mutation |
| Valid request for unknown item | 404, error detail `item_not_found`; no state mutation |
| Valid quantity greater than remaining stock | 409, error detail `insufficient_stock`; no state mutation |

Use `reservation_not_found` for a missing reservation and `item_not_found` for
a missing inventory item. These are FastAPI `detail` values, not a custom error
framework. Do not freeze vendor-generated 422 wording or random ID values.
Fresh app instances must not share state. For two concurrent quantity-7 requests
against initial stock, exactly one succeeds and final available stock is 3;
the other produces the domain conflict and HTTP 409 when mapped by the API.

### First observed task: idempotent cancellation

The seed intentionally has no cancellation operation. In a fresh client session,
ask for `POST /reservations/{id}/cancel` with this observable contract:

- Cancel an active reservation: return 200 with the same object and
  `status:"cancelled"`; restore its quantity to stock exactly once.
- Repeat cancellation: return the same successful representation without another
  stock increase. Concurrent cancellation attempts preserve the same invariant.
- Unknown reservation: 404 with `detail:"reservation_not_found"`; state unchanged.
- Reservation lookup reflects cancellation; existing creation, lookup and invalid
  request behavior still work. No persistence, dependency upgrade or extra stack
  is needed to implement this bounded request.

The task combines CASE-02/CASE-03 concerns without introducing a large benchmark.
Observe whether the agent follows relevant domain/HTTP rules and chooses
sufficient checks. CASE-04 resumption is optional at a natural checkpoint;
CASE-05 update preparation is a later independent scenario if useful.

### Verification and interpretation

Provisioning verifies the starting contract, dependency reproducibility, scoped
typing and adopted artifact routes. Use actual HTTP JSON through TestClient, not
only direct Pydantic validation; cover domain stock/state invariants separately.
Run these checks and mypy inside the built container. Use TestClient's context
manager for lifespan handling. Also start Uvicorn through Compose, wait for its
bounded health check and exercise a business request over the real HTTP listener.
Publish only on host loopback, use one worker and a non-root user, record the base
image digest/platform and verify clean shutdown. Keep test caches in disposable
container storage. No daemon socket, privileged mode or unrelated host mounts.
This is a local test deployment, not evidence of production readiness. Review
dependency/base updates deliberately; a digest alone does not maintain them.

Keep setup checks distinct from observation. The agent that authored the fixture
already knows its design; its setup run is not an independent agent-behavior
result. A new session gets baseline application code, task acceptance and normal
project instructions, without the completed solution or previous run transcript.
Externally evaluated acceptance must check state transitions, not trust the
evaluated agent's summary alone.

Sibling folders are not an access-control boundary. For a controlled comparison,
withhold golden solutions and other conditions' outputs through actual harness
access controls; otherwise report exposure/possible contamination and do not
claim a blinded comparison. A transparent, unblinded observational run can still
produce bounded defect evidence. Do not build a new sandboxing framework just
to obtain a first observation.

The sandbox can validate repeatability and reveal concrete failure modes.
Passing fixture tests, or even a successful cancellation task, does not prove
AEK's causal benefit, cost savings or utility for other stacks. A later ordinary
task is needed before promoting a personal-use improvement. Provisioning is the
final preparation step, before stage A observation; it is not an automatic last
step after the experimental conclusions.

## Minimal evidence report

Use the existing canonical target task or an explicitly selected report location.
The source workstream plan links the outcome only when a sanitized summary may
be retained here. Do not copy private application code or full transcripts into AEK.

| Record | Required content |
| --- | --- |
| Experiment identity | Date, task/case, observational or comparison mode, baseline/candidate identities |
| Reproduction | Starting-state reference, instruction/client/model/effort evidence, tools, permissions and material unknowns |
| Run identity | Condition, repetition/order, timestamps, terminal state and interruption reason if applicable |
| Acceptance | Each criterion marked pass/fail/not evaluated with artifact or check evidence |
| Preservation | Relevant original files/local edits, actual diff and any unauthorized or unrelated change |
| Behavior | Material read/tool/check events and repeated work, with a reasoned classification rather than raw counts alone |
| Efficiency | Wall time to reviewable result, human/environment wait where known, native token categories when available |
| Interpretation | Candidate benefit, regressions, confounders, scope of inference and recommended next action |

Keep raw native token categories and their definitions. Do not add cached tokens
to a total that already includes them; unavailable counts are not zero. Aggregate
authorized subagent usage only when complete and comparable. Monetary estimates
require known applicable pricing and separate reporting; subscription quotas are
not inferred from token totals. File bytes/lines are not token measurements.

Use externally held acceptance checks or human review when feasible. A candidate's
own passing tests or final statement is insufficient to establish its quality.
Preserve the same acceptance requirements for baseline and candidate. For repeated
runs show per-run outcomes and range/median where meaningful; do not hide failures
inside one weighted score.

## Reusable support, only after actual use

If the protocol is useful repeatedly, promote a concise operational procedure to
`docs/maintenance/agent-behavior-pilot.md` and link it conditionally from the pilot
section of MIGRATION. Keep the report outline in that procedure; do not create
another mandatory template, JSON schema, catalog profile or runtime dependency.
The specification retains design history; the promoted procedure owns future
operational detail and links back to shared policy instead of copying it.

Do not introduce a new evaluation skill unless ordinary access to the procedure
proves inadequate. A later automated runner must be justified by recurring manual
effort and designed separately around an actual supported client contract.

## Acceptance scenarios

| ID | Scenario and required result |
| --- | --- |
| PIL-AC01 | No issue appears in the ordinary task: report the observation and retain current configuration; no automatic feature backlog or A/B run |
| PIL-AC02 | A comparison is selected: task/state, treatment difference, client/model evidence, acceptance and run envelope are recorded before runs |
| PIL-AC03 | Candidate is faster but fails a required check: candidate is not eligible for rollout |
| PIL-AC04 | Trace/token/model information is unavailable: keep the value unknown and restrict the corresponding claim |
| PIL-AC05 | A repeat changes model, starting files or several rules: label the confounder; do not attribute its result solely to the chosen instruction |
| PIL-AC06 | Trial stops or fails: retain its outcome/reason; do not silently replace it with a successful retry |
| PIL-AC07 | Task resumes: use the same canonical record and actual state, without losing valid evidence or copying a competing ledger |
| PIL-AC08 | Baseline has local/untracked work: preserve it in the selected starting-state representation; no destructive reset of the active checkout |
| PIL-AC09 | Result is offered for sharing: preserve evidence limits and omit unapproved private content |
| PIL-AC10 | No native read event exists for auto-loaded instructions: do not classify loading as failed without other evidence |
| PIL-AC11 | Sandbox is provisioned: prior contents are preserved; Docker-only application/test/analyzer execution, pinned dependencies/base, container startup, real HTTP behavior and shutdown are verified; only selected fixture files and its Docker resources change |
| PIL-AC12 | Starting application: valid and invalid HTTP requests, domain stock invariants, concurrent reservation and per-app state isolation satisfy the stated contract |
| PIL-AC13 | Observed cancellation task: first, repeated, concurrent and missing-ID cancellation satisfy the contract without breaking the starting API |
| PIL-AC14 | Adopted fixture: independent project entry/routes validate for the selected profiles; source-maintenance instructions and unrelated stack/setup are not activated |
| PIL-AC15 | Setup or synthetic diagnosis passes: report fixture evidence only; no independent-agent, blinded-comparison, recurrence or personal-benefit claim without corresponding evidence |

## Verification boundaries

Review this design against current owners and all acceptance scenarios. Document
changes need artifact/link and scoped consistency checks. Real behavior acceptance
requires selected client/task evidence later; neither this specification nor
successful source tests establishes a completed pilot.
