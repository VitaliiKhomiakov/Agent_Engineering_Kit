# Responsibility placement before implementation

## Outcome and authorized scope

Make responsibility discovery and placement explicit before implementation across
AEK profiles. Use existing suitable owners from the first change, without waiting
for file growth, and distinguish file organization from stronger dependency,
access or lifecycle boundaries. The user's 2026-10-21 request approves this
direction and asks for its implementation using Superpowers.

**Status:** Follow-up correction stage complete (RFI-5 through RFI-7); awaiting user review.
The original stage and follow-up planning evidence remain recorded below.
**Original-stage design:** The common policy owns the rule; ordinary implementation and existing
review route to it. Reconcile growth-dependent wording in Go, React and NestJS.
That stage combined design, plan and evidence under `templates/PLANS.md`.
The later planning request has a dedicated
[follow-up specification](../specs/2026-10-21-responsibility-boundary-clarification.md)
and uses this same document as its sole progress owner.
**Execution:** Inline, current checkout, no new agents or review rounds. No Git
writes, toolchain changes, runtime refactoring or downstream application edits.

Instruction root and execution checkout:
`/home/vitalii/Documents/Local_Projects/Agent_Engineering_Kit`.
Canonical task and progress owner: this document, maintained by the coordinator.
No source model-routing setup is needed. The pre-stage HEAD is
`f8b43b83bc2ae6f7a0fddeef86337f70daa668d8`, but HEAD does not capture existing edits.
The actual baseline, including the previous Go-readability correction and its
untracked plan, is saved at
`/tmp/aek-responsibility-first-20261021-qckx6l0v/baseline.json`, with exact originals
and `preexisting.diff` beside it. Preserve that work and its dated evidence.

## Constraints and decisions

- One canonical owner in `standards/core.md`; roles and profiles route to it.
- Identify responsibilities present in the affected scenario, not speculative
  future capabilities. Reuse suitable existing owners and settled decisions.
- Organize independent responsibilities from the outset; retain cohesive private
  helpers and related declarations. No one-function/type-per-file rule.
- Use the language/framework's actual import, visibility and lifecycle contracts.
  A separate file is not universally equivalent to a dependency/access boundary.
  Do not mandate a package, exported API, shared library or folder scaffold.
- Size thresholds remain additional review signals. Keep local legacy fixes scoped;
  neither discovering debt nor this rule authorizes a repository-wide restructuring.
- Incorporate checks into existing review and evidence. No separate responsibility
  ledger, compulsory architect, per-component report or automatic guarantee of adherence.

## Progress

- [x] RFI-1: Confirm current owners/routes, relevant profile wording and boundary contracts.
- [x] RFI-2: Add the common rule and connect implementation/review; align affected profiles.
- [x] RFI-3: Assess representative cases, run artifact/adoption checks, inspect the
  stage delta and preserve prior changes, then present the result for review.
- [x] RFI-4: Specify the two review corrections and prepare/check the follow-up plan.
- [x] RFI-5: Clarify the core extraction criterion without weakening responsibility placement.
- [x] RFI-6: Align Unreal module creation with the concrete boundary requirement.
- [x] RFI-7: Assess BC-1 through BC-8, run affected artifact checks, review the scoped
  correction and preserve prior changes, then return the stage for user review.

Current item: None active. RFI-5 through RFI-7 are complete; stop for user review.
RFI-1 through RFI-3 retain their original completed-stage evidence. The later review
exposed two remaining wording ambiguities, now addressed by the follow-up correction.

## Findings and file ownership

This section records the original investigation. The later review findings and
their correction scope are recorded in the follow-up below.

Core already defines SRP, reuse and decomposition below function-size thresholds.
Architect/design instructions already inspect owners; ordinary implementation
does not explicitly require the placement decision before writing. Go and React
wording can defer separation until growth; NestJS similarly frames service
decomposition around growth. The missing condition is early placement of already
independent responsibilities, not a new size threshold.

| Path to change | Responsibility |
| --- | --- |
| `standards/core.md` | Canonical rule, ordinary implementation route and relationship to size/extraction |
| `standards/verification.md` | Preparation route and a check within the existing accountable review |
| `templates/agents/implementer.md` | Explicit pre-write route, retaining the prior readability correction |
| `templates/agents/reviewer.md` | Scoped placement-review route, retaining the prior readability correction |
| `standards/go/architecture.md` | Early file grouping and separate package/access decision |
| `standards/react/components-boundaries.md` | Independent owners from the outset, with cohesive local components/helpers retained |
| `standards/nestjs/modules-providers.md` | Responsibility-led service organization without a growth prerequisite |
| This document | Design, progress, scenario assessment and dated evidence |

Python, JavaScript/TypeScript, PHP, Angular and Unreal already describe ownership
and suitable local boundaries. NgRx's store-placement rules already separate used
responsibilities; its advice for a growing store does not require delaying those
boundaries. Their profiles inherit core, so duplicating the new policy in each
would create overlapping owners. Existing root entries, architect/task skills and
native adapters already route to core/verification/shared bodies. Catalog resources
and IDs need no changes; no new operational file is introduced.

## Primary-source boundary check — 2026-10-21

- [Go module layout](https://go.dev/doc/modules/layout) permits multiple files
  within one package and distinguishes separately imported packages. Earlier
  responsibility placement is AEK policy, not a new Go syntax requirement.
- [Thinking in React](https://react.dev/learn/thinking-in-react) begins with
  component decomposition and retains judgment about smaller subcomponents.
  AEK's placement convention does not require extracting every UI fragment.
- [Nest modules](https://docs.nestjs.com/modules) describes cohesive feature
  modules and provider visibility through imports/exports. A separate source file
  does not itself introduce a Nest DI boundary.

These are source-reviewed boundary concepts, not executed compatibility tests.
Existing Go target/toolchain constraints, React 18/19 compatibility conditions and
Nest older-version conditions remain unchanged. No version-sensitive API, native
configuration syntax, dependency, executable example or supported-version floor changes.

## Verification and acceptance

Use `python3 -B tools/check_instruction_artifacts.py` for the source and an explicit
invocation for this plan. Run the existing `tests.test_agent_templates` and
`tests.test_project_skill_portability` suites: their inputs include changed common
policies/bodies and representative Go, React, Python and Angular bundles. Review
the remaining NestJS route in the source catalog and affected local links. These
fixtures check structure/routes and preserved local sentinels, not model behavior.
No new implementation-shaped tests or application builds are needed for prose changes.

Compare changes to the saved stage baseline, including dirty shared files; inspect
the new plan separately and run `git diff --check`. Check unchanged previous-task
paths byte-for-byte and inspect only the added stage delta in shared paths.

## Manual scenario assessment — 2026-10-21

The following is coordinator assessment against the revised
[placement rule](../../standards/core.md#responsibility-placement-before-implementation)
and scoped [review requirement](../../standards/verification.md#review-boundaries).
It is not an automated regression test or an independent model evaluation.

| Scenario | Required decision and review outcome |
| --- | --- |
| A new small Go file combines a transport handler and an independent SQL adapter, each with different contracts/dependencies; separation was deferred because the file is short | Finding required: already independent responsibilities need suitable owners and separate cohesive files under the Go profile. No size or reuse threshold permits the deferral. Reuse an existing adapter if one is suitable. |
| A React component retains a private render helper, its props and a small related calculation with no independent contract/state/dependency ownership | No finding merely for sharing a file. These serve a cohesive owner; extracting them solely to increase file count adds indirection. An independent API adapter would require its own placement even while short. |
| A Go package uses `handler.go` and `storage.go` for separate responsibilities with the same intended package boundary | No finding merely because there is no new package. Files organize code; another package needs a distinct dependency/access reason. Moving methods alone would not resolve an overly broad type. |
| An adapter needs dependency isolation from a business capability, or Nest consumers need an explicitly exported provider capability | Establish the necessary package/module boundary and permitted dependencies/exports. A file move alone is insufficient if the required boundary remains absent. Check actual contracts, not directory count. |
| A Python or JavaScript adapter moves to another source file | Apply that profile's module/import/visibility rules and adjust affected consumers. Do not assume Go's same-package file semantics or require an additional package/folder layer. Report a broken affected contract, not the absence of a Go-shaped layout. |
| A local error-handling fix touches a cohesive operation inside a pre-existing oversized legacy service | Keep the fix and review bounded. Record visible unrelated decomposition debt once; do not require a whole-service rewrite. A new independent responsibility introduced by this task must still receive suitable placement. |
| A valid accepted design already maps the unchanged responsibilities to suitable owners | Reuse the decision and evidence after checking applicability to the current scope/rule. No repeated design round or per-function report. A historical clean result that did not assess the clarified criterion does not supply missing coverage. |

The distinctions follow actual responsibility, cohesion, dependency/access/lifecycle
contracts and scope. No verdict depends on a fixed line count or a file per function.

## Results and delivery — 2026-10-21

These results apply to the original RFI-1 through RFI-3 state. They do not establish
that the subsequent review findings have been fixed or validate future wording.

| Check | Result and limits |
| --- | --- |
| `python3 -B tools/check_instruction_artifacts.py` | 222 artifacts; 0 errors. Catalog resources and supported local links/anchors pass. |
| `python3 -B tools/check_instruction_artifacts.py docs/plans/2026-10-21-responsibility-first-implementation.md` | 1 artifact; 0 errors. Historical plans remain outside the default scan. |
| `python3 -B -m unittest -q tests.test_agent_templates tests.test_project_skill_portability` | 10 tests passed. Existing fixtures cover shared bodies, three native clients, contained/flat/custom layouts and representative profiles; no live native client or model behavior was exercised. |
| `git diff --check` and separate new-plan inspection | No whitespace errors. New/untracked plan inspected separately; no application code changed. |
| Baseline comparison | Six earlier-task paths, including the Go plan, remain byte-identical. In the three shared paths, all baseline lines are retained and this stage only adds placement routes/checks. No changed paths outside the recorded stage and prior work. |
| Coordinator source review | One detailed placement owner in core; ordinary implementation, shared roles and verification route to it. Go/React/Nest wording is consistent with it; size signals, legacy scope and the earlier readability acceptance rule remain intact. Seven scenarios assessed above. |

The native Codex, Claude and Cursor adapters already direct each role to its shared
body using the instruction root. Those bodies now route to the placement owner.
Root entry templates route ordinary work through core and before-edit verification.
This verifies instruction routes in source and fixture bundles, not actual loading
or compliance in a running client. No new agent or independent review was required
by the bounded policy edit and existing risk-based review policy.

New imports receive the common rule through the required core/verification profiles,
the already catalogued Go/React/Nest resources and shared role bodies. No catalog,
native configuration or root-template rewrite is necessary. Existing targets use the normal reviewed
[update procedure](../../MIGRATION.md#repeat-and-update), comparing accepted, current
and new adapted content and preserving local customizations. Source changes do not
automatically update existing targets. Reconcile the changed common files and selected
profile resources; update shared bodies without overwriting locally adapted native
role definitions. Recheck affected routes and assess previous acceptance evidence
against the clarified rule rather than treating an old clean review as coverage.

Artifact checks enforce supported structure, resource and route constraints;
fixture tests check specific prepared-file properties. Identifying independent
responsibilities, choosing boundaries and applying them during implementation/review
still require agent judgment. These instruction changes do not guarantee future
compliance. No installed plugin cache, downstream project, dependency, executable
example, branch, commit or release was changed.

## Review follow-up — 2026-10-21

The requested subsequent review found two ambiguities: core's extraction trigger
could require a helper for any meaningful step; Unreal's module trigger could
justify a module solely by a meaningful responsibility. These qualify the earlier
consistency conclusion; retain the earlier executed checks with their original
scope. The user then requested a specification and plan, not implementation in
this turn. See the [design and BC acceptance cases](../specs/2026-10-21-responsibility-boundary-clarification.md).

### Scope, baseline and execution

The instruction root, execution checkout and coordinator ownership remain as
recorded above. The planning-stage snapshot is
`/tmp/aek-boundary-clarification-plan-20261021-gid_e39f/baseline.json`; exact originals
and the pre-existing diff are beside it. It records all existing local changes,
the untracked canonical plan, source owners and the new specification's absence.
Only the specification and this plan may change during RFI-4.

For RFI-5 through RFI-7, use inline execution in the current checkout if the user
continues with this stage. Use Superpowers `executing-plans` through the local
adaptations; no delegation or source model-routing setup is needed. Capture a new
pre-implementation baseline including intervening edits; do not reuse HEAD or the
planning snapshot as proof that the working state is unchanged.

Carry forward all existing constraints: preserve the Go correction, user edits,
historical evidence and version conditions; retain one owner per rule; no new
review cycle, threshold, tooling dependency, Git write, plugin-cache change or
downstream refactor. Only the two operational owners and this task's evidence are
planned for the correction. The specification is design input, not an adopted rule.

### Planned steps and acceptance

| Item | Work and dependency | Completion criterion |
| --- | --- | --- |
| RFI-4 | Save the requested specification, retain this canonical plan, inspect the diff and check both documents | Spec and plan cover both findings, BC-1 through BC-8 and verification; only these documents changed. Present them for review without starting implementation. |
| RFI-5 | After the user's continuation, capture the current baseline and revise only the extraction bullet in `standards/core.md#small-methods-and-functions` according to the specification | Nameable purpose/independent inputs alone are insufficient; genuine single-use extraction and required separation remain. Preserve the size-threshold assessment, adjacent contract/reuse rules and existing anchors. |
| RFI-6 | Use the settled core meaning from RFI-5; revise the runtime/editor/module-choice bullet in `standards/unreal-engine/build-assets.md#modules-and-build-inputs` and link the existing placement owner | The module needs a concrete boundary reason; cohesive files remain available. Runtime/editor isolation, public/private dependencies and acyclic imports remain intact. |
| RFI-7 | After both edits, assess BC-1 through BC-8 against final text and inspect affected core/Go/Unreal/verification/role interactions; run the commands below | Both findings resolved; scenario reasons and actual command results recorded here, prior work preserved and no new contradiction or duplicated rule introduced. Stop for user review. |

Checks are batched at RFI-7 for this one coherent prose-correction stage. No new unit
tests or engine/application builds are justified. Existing native-route fixtures
remain reusable while their routes, configuration and resources are unchanged;
revisit only a changed input if implementation unexpectedly alters that scope.

```sh
python3 -B tools/check_instruction_artifacts.py
python3 -B tools/check_instruction_artifacts.py docs/specs/2026-10-21-responsibility-boundary-clarification.md docs/plans/2026-10-21-responsibility-first-implementation.md
git diff --check
```

Expect exit 0 and no artifact errors. Also inspect new/untracked documents and the
stage-only delta against its recorded baseline. Check that the Unreal profile
still includes its build-assets owner and required core resource; no catalog or
native-adapter changes are planned. Apply the existing update procedure to future
adoptions, preserving customizations rather than copying source files over them.

Record BC judgments as manual policy assessment, not an automated regression test
or independent model evaluation. Do not reuse an old clean review as evidence for
the newly clarified criterion; retain unrelated valid results. A formatter or
artifact checker cannot decide whether an extraction/module is necessary.

### Planning-stage evidence

RFI-4 completed on 2026-10-21:

- The explicit two-document artifact command above passed: 2 artifacts, 0 errors,
  exit 0. `git diff --check` passed; both untracked documents were also inspected
  for whitespace/newline errors separately.
- Baseline comparison confirmed 14 protected prior-work/reference paths remain
  byte-identical. Prior findings/results in this plan remain intact, with later
  qualifications appended. No operational standard or native instruction changed.
- Spec/plan self-review covered both findings, owner/route consistency, preservation
  constraints and the BC cases. RFI-5 owns the extraction decision, RFI-6 owns the
  Unreal decision and RFI-7 validates their interaction and all eight cases.
- The official source assessment is recorded in the specification. No model or
  Unreal runtime evaluation was performed; no implementation test is claimed.

The operational corrections and BC scenario execution remain planned, not completed.
Earlier source/adoption test results remain historical evidence for their recorded
states, not results of this follow-up. Present these documents and stop at this
planning checkpoint.

### Correction-stage execution — 2026-10-21

The user subsequently requested execution with Superpowers, authorizing RFI-5
through RFI-7 in the current checkout. The fresh pre-implementation baseline is
`/tmp/aek-boundary-clarification-20261021-r_le1ky8/baseline.json`, with exact originals
and the pre-existing diff beside it. It covers 16 paths, including all local edits
and untracked task artifacts; the three planned paths are the core owner, Unreal
build-assets owner and this plan. Preserve the specification and all other prior work.

The specification's two corrections compose through the existing responsibility
placement section. No interface, route or version conflict prevents execution.
Use the planned single inline stage and batched RFI-7 checks; the earlier planning
checkpoint and its evidence are historical, not current blocking instructions.

RFI-5 implemented the specified extraction condition in core. A nameable step or
separate inputs alone no longer mandates a helper; real reuse, obscuring detail
and independent responsibilities still justify extraction. The size assessment,
adjacent contract/reuse rules and anchors remain. Stage acceptance awaits RFI-7.

RFI-6 replaced the Unreal module trigger with concrete dependency/public-exposure,
module loading/lifecycle or target/platform inclusion needs, routing to core.
Cohesive files remain available where those boundaries stay shared. Runtime/editor
separation, public/private dependency declarations and the cycle prohibition remain.

### Correction-stage manual assessment

The coordinator assessed BC-1 through BC-8 against the implemented text on
2026-10-21. This is manual policy assessment, not an automated regression test,
independent reviewer/model evaluation or application/engine execution.

| Case | Result against the final rule |
| --- | --- |
| BC-1 | Satisfied. Nameable creation/configuration/registration/result steps do not by themselves trigger extraction under core. The grouped router remains valid; its compact variant still has the three missing separators under the unchanged Go style owner. |
| BC-2 | Satisfied. Obscuring detail/complexity is an independent extraction reason; actual reuse and size-threshold crossing are not prerequisites. The adjacent cohesion rule still prevents a helper that only adds indirection. |
| BC-3 | Satisfied. Core explicitly retains separation of independent responsibilities below the size threshold and routes placement to the actual owner. A short mixed handler/storage implementation cannot use the nameable-step exception to evade that boundary. |
| BC-4 | Satisfied. The reuse trigger requires absence of a suitable existing owner, and the existing adjacent rule requires reusing an appropriate implementation. A parallel helper is not justified by naming alone. |
| BC-5 | Satisfied. Unreal now states that responsibility alone is insufficient for a new module and permits cohesive files when the relevant boundaries remain shared. Organization alone no longer supplies the stronger-boundary justification. |
| BC-6 | Satisfied. The runtime/editor separation and prohibition on editor-only runtime dependencies remain intact. Reuse of a suitable editor owner follows core; a file move cannot satisfy a missing module boundary. |
| BC-7 | Satisfied. The listed concrete boundary reasons are alternatives, not cumulative requirements. The shared placement owner requires reuse of a suitable boundary before introducing another one; module loading/lifecycle does not mean each Actor's lifetime. |
| BC-8 | Satisfied. The unchanged task-scope and evidence-reuse owners retain bounded legacy work and require matching code, context and criterion. This stage freshly assesses the changed criteria and preserves earlier unrelated evidence without claiming it tested the correction. |

The stage-only source diff changes exactly the two specified bullets and adds
their routes to the existing placement section. The surrounding size, cohesion,
typed-contract, Go spacing, review and evidence-reuse rules remain consistent.
No detailed policy was copied into another role/profile. Source catalog inspection
confirmed that core is required and Unreal still includes its build-assets owner;
shared roles and the Unreal entry retain their routes to these policies.

### Correction-stage verification and handoff

Executed on 2026-10-21 against the two final operational changes:

| Check | Result |
| --- | --- |
| `python3 -B tools/check_instruction_artifacts.py` | Exit 0; 222 artifacts, 0 errors. Supported source syntax, catalog resources and links/anchors pass. |
| Explicit artifact command for the specification and this plan | Exit 0; 2 artifacts, 0 errors. |
| `git diff --check` and separate untracked-document inspection | Exit 0; no whitespace/newline errors. |
| Stage-baseline comparison | 13 other prior-work paths, including the specification and Go correction, remain byte-identical. Earlier findings and planning/original-stage evidence in this plan remain verbatim. No unrelated paths changed. |

The full stage delta is saved beside the implementation baseline as `stage.diff`.
Only `standards/core.md`, `standards/unreal-engine/build-assets.md` and this plan
changed in this stage. Existing anchors and role/catalog routes remain intact;
new integrations receive the two owners through their existing resources. Existing
targets retain the previously documented B/C/N update and customization boundaries.

Both review findings are resolved in their source owners. The scoped coordinator
review found no remaining conflict between extraction, responsibility placement,
Go grouping, Unreal module criteria and existing acceptance/evidence rules.
The eight manual assessments above supply the new semantic evidence; unchanged
native-route evidence remains applicable to those routes, not a new native-client
run or proof of instruction following. No new tests, runtime builds or agents were
needed for this bounded prose correction. Artifact success does not establish
semantic compliance by future agents.

No further stage, downstream update or Git action is started. The remaining
checkpoint is the user's review of this completed correction.
