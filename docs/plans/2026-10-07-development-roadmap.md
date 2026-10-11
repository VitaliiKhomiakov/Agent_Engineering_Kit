# Evidence-led development: feasibility, specifications and roadmap

**Date:** 2026-10-07.
**Status:** The 2026-10-11 unblinded AEK_TEST observation and skill-library
assessment are complete for owner review. The pilot plan owns execution evidence.
Independent fresh-session observation and controlled comparison have not run.
Feature proposals remain conditional; the observation container is stopped.

**User outcome:** Improve the owner's everyday use of Agent_Engineering_Kit,
while retaining a path to reuse by other developers. Establish usefulness and
duplication risk before investing in new capabilities.

**Authorization:** The initial request authorized feasibility research,
specifications and plans. On 2026-10-08 the owner supplied
`/home/vitalii/Documents/Local_Projects/AEK_TEST` and authorized selecting and
setting up a technology combination for tests, either scheduled in the scenario
or performed as a final step. The documentation continuation took the scheduling
option; the owner subsequently instructed execution and required Docker. Stage S
prepares the fixture before agent observation. This is not approval to build the proposed AEK features or
launch an unspecified paid evaluation batch.

## Canonical ownership and baseline

- Instruction root and source execution checkout:
  `/home/vitalii/Documents/Local_Projects/Agent_Engineering_Kit`.
- Canonical owner of this research/design task and portfolio decisions: this file.
  Future workstream plans own their own execution items; do not mirror them here.
- Baseline: clean checkout at `a725cf28cb4e399e64c13dc421e63ea7cc4ae580`.
  All six documents in this task were absent before writing. The path inventory
  and initial state are recorded at
  `/tmp/aek-development-design-737re1wa/baseline.json`; retain through review.
- Work inline in this checkout. No staging, commits, branches, worktrees,
  delegation or installed-plugin changes are selected. Reversible setup and
  functional testing in the supplied sandbox are authorized but scheduled later.
- Planning follows [the repository planning policy](../../templates/PLANS.md),
  [delivery](../../standards/delivery-workflow.md), and
  [Superpowers adaptations](../../standards/superpowers.md).
- No model-routing setup is needed for this inline documentation task.
- Sandbox root: `/home/vitalii/Documents/Local_Projects/AEK_TEST`; inspected empty
  on 2026-10-08. Selected fixture: Python 3.12, FastAPI and Pydantic v2, with a
  reservation API. Pilot client/version, observed model/effort, any candidate
  treatment and additional-run budget remain execution inputs.
- Before this addendum, exact copies of the six untracked documents and a state
  manifest were saved at `/tmp/aek-sandbox-design-9d3jntkp`. This supplements,
  rather than replaces, the initial absence baseline.

## Documentation stage

- [x] **DEV-01:** Assess current coverage, external evidence, useful additions,
  cheaper alternatives and conditions for rejecting each proposal.
- [x] **DEV-02:** Specify a bounded agent-behavior pilot and a conditional
  read-only adoption diagnostic without introducing a new runtime.
- [x] **DEV-03:** Write resumable workstream plans with exact affected areas,
  acceptance scenarios, dependency gates and sufficient checks.
- [x] **DEV-04:** Review the complete document set, validate links/format and
  consistency, and record the review handoff and evidence limits.
- [x] **DEV-05:** Define the supplied sandbox, useful minimum stack, application
  contract, observation task and optional diagnostic reuse; update both workstreams.
- [x] **DEV-06:** Validate the updated documents and actual scoped diff; record
  the distinction between scheduled provisioning and executed runtime evidence.

**Current item:** None; DEV-01 through DEV-06 are complete for documentation.
**Next checkpoint:** Review the completed unblinded stage A observation and the
2026-10-11 skill-library assessment. The pilot plan owns LAB/PIL execution markers.

## Document map

The research note owns evidence and feasibility judgments. Each specification
owns one workstream's behavior and acceptance criteria; its plan owns execution
progress. This roadmap owns prioritization and conditions for opening new work.

| Artifact | Responsibility |
| --- | --- |
| [Feasibility assessment](../research/2026-10-07-development-feasibility.md) | Current capability, primary-source evidence, alternatives, cost/duplication risks and investment gates |
| [Pilot specification](../specs/2026-10-07-agent-behavior-pilot.md) | Observation/comparison modes, concrete sandbox contract, evidence limits and fifteen acceptance scenarios |
| [Pilot plan](2026-10-07-agent-behavior-pilot.md) | Stage S for sandbox preparation, stages A-C for observation/optional comparison/decision, and optional stage D for reusable documentation |
| [Diagnostics specification](../specs/2026-10-07-adoption-diagnostics.md) | Read-only inputs, scope, findings/evidence model, legacy/exception behavior and twelve acceptance scenarios |
| [Diagnostics plan](2026-10-07-adoption-diagnostics.md) | Manual diagnosis, conditional reusable procedure and separately conditional `aek-doctor` wrapper |

**User clarification:** No critically important issue has been noticed; no deep
effectiveness analysis has yet been performed. Prefer observation during ordinary
work. New features remain conditional on evidence, not presumed necessary.

## Portfolio decision and sequence

The recommended next step is the selected small sandbox, then one observed task;
an ordinary project task remains necessary to assess daily usefulness. No
production feature is established as necessary by this assessment. Both workstream
plans have target-specific inputs and explicit stage gates; later feature stages
are not a commitment or permission to execute.

| Direction | Decision now | Why | Evidence required to reopen |
| --- | --- | --- | --- |
| AEK_TEST fixture | Stage S complete; Docker fixture checked | Owner supplied a disposable target and requires container execution | Fresh-session observation remains next; fixture success is not proof of personal benefit |
| Ordinary-task pilot | Validate daily usefulness | Complements the synthetic fixture with useful work and existing procedures | Select a real target/task and observable acceptance |
| Controlled A/B comparison | Conditional after observation | Costs extra runs; useful only for one concrete hypothesis | An observed issue, one candidate change and a permitted run envelope |
| Manual adoption diagnosis | Conditional on a question | Existing owners/checker can resolve many problems without a new feature | A setup uncertainty, relevant pilot finding or explicit recurring check need |
| Reusable procedure / `aek-doctor` | Conditional; no implementation now | Potential convenience, but also discovery/maintenance overhead | Useful manual result and recurring reuse; wrapper only if direct procedure access is insufficient |
| Semantic update summary | Small extension of existing integration if needed | B/C/N comparison and provenance already exist | A real update whose consequences are hard to review |
| `aek-context` | Deferred | Conditional task routes already solve the intended selection problem in design | Repeated observed routing failure that a simpler entry correction does not solve |
| Custom MCP/vector retrieval | Not scheduled | Adds runtime, transport, indexing and provenance work | Demonstrated retrieval bottleneck and a measured benefit over local lookup/existing tools |
| Background freshness service | Deferred | Dated evidence and version-triggered review already exist | Repeated version-related failures with a cheaper maintenance alternative ruled out |
| Public distribution | Later optional work | Personal use has priority | A useful repeatable workflow and a selected sharing/support scope |

Sequence: provision and check the sandbox as the final preparation stage, observe
one fresh-session task, then decide whether to retain the configuration,
diagnose adoption, or compare one proposed correction. Review the outcome before
promoting any change. Diagnosis can run independently when a concrete question
already exists; it does not require paying for a benchmark first. In the pilot
plan, stage A may go directly to C; B is optional. Reusable source documentation
and skill packaging follow evidence rather than precede it.

There is no calendar schedule or numeric ROI estimate: actual run effort, client
observability and recurrence are not known. Relative effort and rejection
conditions are recorded in the research note. Do not create implementation
commitments for the deferred ideas merely to fill a roadmap.

## Design boundaries and alternatives

1. Preserve the accepted rules-library scope; do not reopen the retired
   application/CLI backlog.
2. Prefer a bounded pilot and reuse of existing procedures before creating
   more instructions, skills, metadata or services.
3. Do not infer agent behavior from file validity, tool availability, a saved
   model assignment or the agent's unsupported claim that it read a rule.
4. A feature may be declined after investigation. That is a valid planning
   result, not a reason to build a substitute feature automatically.

The research compares keeping the library unchanged, evidence-first incremental
improvement, and building a tool platform. Recommend the second as a method of
investigation, with the first as an acceptable outcome. The platform option is
unjustified for the currently reported need.

No active policy, catalog ID/schema, technology version, template or executable
tool changes in this documentation stage. These documents are conditional research
and task artifacts, not new catalog resources or always-loaded instructions.
Future source-owned optional procedures have exact paths in their workstream plans;
links to nonexistent future files are not installed now.

## Success and stop conditions

For this documentation task: the feasibility assessment challenges the original
ideas; both specifications distinguish existing mechanisms from additions; plans
map requirements to logical stages, sufficient checks and explicit gates; all
new references and document state are consistent.

For future development: useful evidence or an explicit no-change conclusion is
a valid outcome. Stop a dependent investigation if evidence/permissions are
missing or its selected resource boundary is reached. Preserve incomplete results
honestly. No shortened check list may override a required task gate.

Review can change or reject either proposed feature workstream. The separate
sandbox grant does not approve those features. Existing
accepted historical stages remain closed; this proposal does not recast their
evidence as a pilot of the current instructions.

## Initial documentation verification — before the sandbox addendum

The six new documents are the complete changed scope; no existing tracked source
file, active policy, template or executable tool was modified. Source review
checked duplication, authority, permission boundaries, conditional progression,
requirement-to-stage coverage and current/future completion markers.

Executed document validation:

```sh
python3 tools/check_instruction_artifacts.py docs/research/2026-10-07-development-feasibility.md docs/plans/2026-10-07-development-roadmap.md docs/specs/2026-10-07-agent-behavior-pilot.md docs/plans/2026-10-07-agent-behavior-pilot.md docs/specs/2026-10-07-adoption-diagnostics.md docs/plans/2026-10-07-adoption-diagnostics.md
git diff --check
```

The explicit artifact run reported `Checked 6 artifacts; 0 error(s).`; the Git
whitespace check emitted no diagnostics. New files were inspected separately,
including `git diff --no-index --check` against `/dev/null`. A temporary review
helper initially misclassified the normal no-index difference exit code 1 as a
failure. Clean/whitespace-error control files established the distinction; no
document defect was indicated by that helper result.

Scoped consistency checks compare the verbatim Global Constraints in each
specification/plan pair, unique acceptance/task IDs, complete acceptance coverage,
absence of unresolved placeholders and unchecked future execution items. No
independent agent review, application test, live evaluation, Context7 tool query
or native setup was performed. Third-party capabilities remain source-reviewed;
personal benefit remains unmeasured.

That result covers the initial document contents, not the subsequent sandbox
addendum. Its six new files remained untracked when the addendum began.

## Sandbox addendum verification and handoff — 2026-10-08

The six existing task documents were updated; no tracked source policy, catalog,
tool, template or executable example changed. Their actual diffs were reviewed
against `/tmp/aek-sandbox-design-9d3jntkp`, preserving the earlier evidence above.
The same explicit six-document artifact command reported
`Checked 6 artifacts; 0 error(s).` after the sandbox edits. `git diff --check`
was clean; separate no-index checks against both the saved originals and
`/dev/null` covered all six untracked files without whitespace diagnostics.

Scoped consistency checks passed: paired Global Constraints match; all 15 pilot
and 12 diagnostic acceptance IDs have stage coverage; task IDs are unique; all
14 pilot/preparation and nine diagnostic runtime items remain unchecked; no
unresolved placeholders were found. Source status contains only these six
untracked documents. The supplied sandbox was rechecked and remains empty.
Review also corrected the planned checker invocation to preserve full selected-
profile body coverage instead of narrowing it to explicit entry files alone.

Provisioning, application tests and fresh-session observation have not run.
The exact sandbox contract belongs to the pilot specification and the executable
sequence to its plan. Next scheduled work is LAB-01 through LAB-04 under stage S,
followed by a separately recorded agent observation; the existing sandbox grant
is retained. No new diagnostic/context/MCP feature is justified by this document
check or by the mere availability of a test directory.

## Evidence status clarification — 2026-10-08

**Recorded conclusion:** The specifications and plans passed the scoped document
checks. A successful live AEK pilot has not been demonstrated.

Completed DEV items describe documentation work only. Reinspection confirmed
that `AEK_TEST` remains empty, and the pilot plan records no provisioning,
application tests or observed agent task. These results do not establish AEK's
general effectiveness or improved task quality/time/cost.

To record a successful bounded pilot, first complete the selected preparation
and observed task, then assess its acceptance and preservation using actual run
evidence. State the tested stack, task, client and remaining limitations; even
that result would not establish effectiveness for all projects.

This clarification preserves prior evidence and execution markers. Its pre-edit
roadmap copy is retained at
`/tmp/aek-evidence-status-s5kxipgx/2026-10-07-development-roadmap.md`.

## Execution and Docker clarification — 2026-10-08

The owner instructed execution, then clarified that the project must always run
in a container. Docker is now a selected profile and runtime constraint; the
earlier host-venv proposal is superseded. Current execution evidence and blockers
belong to the pilot plan's stage S; earlier statements that no work had run retain
their historical scope. No application/agent result is inferred from document
validation or from container configuration alone.

Stage S subsequently completed: the container fixture passed 33 tests, strict
typing, dependency checks, 57-artifact checks for each project copy, real HTTP
checks, clean shutdown and reproduction. At that handoff the observation API was
running on `127.0.0.1:18080`. The pilot plan owns detailed evidence and remaining PIL items;
sandbox `evidence/setup/report.md` distinguishes these executed checks from the
unexecuted fresh-session task. No feature-investment gate is satisfied merely
by the fixture's success.

## Owner-requested pause — 2026-10-08

The observation container subsequently stopped cleanly (exit 0, no OOM) for the
owner's overnight pause. No `aek-` containers were running at the shutdown check.
Files, images and existing evidence were preserved; no Git writes were performed.
The sandbox `RESUME.md` and `evidence/setup/pause-2026-10-08.json` record the
operator handoff and observed shutdown state. The pilot plan remains the execution
owner: LAB-01 through LAB-04 are complete, PIL-01 is next after continuation.
No independent pilot, controlled comparison or proposed feature implementation
was performed during shutdown.


## Observation and skill assessment handoff — 2026-10-11

The owner requested execution and recorded observations on a disposable reservation
API fixture, plus research
on skills for architecture, coding, review, languages and technologies. One prepared
cancellation task completed in the current session under the pilot specification's
unblinded mode. The self-contained [retained pilot outcome](2026-10-07-agent-behavior-pilot.md#stage-a-completed-in-unblinded-mode--2026-10-11)
records the task, versions, results and limits inside AEK without depending on the
disposable workspace. All 38 tests,
strict types and a real HTTP concurrency/stock probe passed; the seed and adopted
instructions remain unchanged, and the service is stopped. Independent-session
behavior, native discovery, token savings and causal AEK benefit remain unmeasured.

**Current decision: create no new skills in this stage.** Retain current rules,
the three existing inactive AEK skill templates and applicable Superpowers
procedures. The existing feasibility note's dated addendum maps vendor guidance to
AEK and defines when a specialized skill earns its place. No blanket language-by-phase
skill library or new diagnostic/context service is justified by this run. Proposed
specialized workflow examples remain illustrative, not approved files or a backlog.
The preceding portfolio table records the earlier proposal; this handoff advances
only the executed unblinded observation and research, not the deferred feature gates.

## Consumer-project skill planning — 2026-10-11

After clarifying that the skills are to be installed in consuming projects, the
owner requested a specification and staged plan for selective reorganization,
instruction reachability, adoption correctness, Superpowers compatibility and
final conflict/duplication review. The new [canonical plan](2026-10-11-project-skills-reorganization.md)
owns that work and links its specification. This advances the earlier no-new-skills
observation-stage decision to a proposed design; implementation and native rollout
have not been authorized or executed by this documentation request. Earlier pilot
evidence and deferred diagnostic/context-service proposals remain unchanged.
