# Godot profile research and implementation plan

Date: **2026-10-22**.
Status: **Source implementation complete, including final-review corrections;
commit and push authorized**.
Current authorized scope: **commit the reviewed Godot changes and push the current
`main` branch to `origin`**. Target installation remains outside this task.

## Goal, design and context

Add coherent optional Godot guidance to AEK, with primary GDScript, conditional
C#/GDExtension, common 2D/3D engineering practices, proportionate verification and
an evidence-based optional MCP selection. Stage 1 produced the researched proposal;
Stage 2 implements the instruction library, not an installed Godot environment.

Canonical design: [Godot support specification](../specs/2026-10-22-godot-support.md).
Sources and dated tool qualification: [research](../research/2026-10-22-godot-engineering-and-mcp.md).
The specification owns design requirements; this file owns progress and execution.
Research records vendor evidence without becoming an active target instruction.

The source is a Markdown/TOML instruction library with a Python standard-library
artifact checker and tests. Godot is a reference technology, not this repository's
runtime. Use [library architecture](../../ARCHITECTURE.md),
[catalog contract](../../standards/catalog.md), [migration](../../MIGRATION.md),
[verification](../../standards/verification.md) and
[local Superpowers adaptations](../../standards/superpowers.md).

## Execution context and baseline

| Field | Recorded value |
| --- | --- |
| Instruction/workspace root | `/home/vitalii/Documents/Local_Projects/Agent_Engineering_Kit` |
| Project/repository execution checkout | Same current checkout; branch `main`; no worktree |
| Canonical artifact store | This checkout's `docs/plans/`, `docs/specs/`, `docs/research/` |
| Canonical progress owner | Coordinator, this file; no parallel editable checklist |
| Pre-edit HEAD | `f9d18ffb699d2aa9c4a5e6c2e1d38367998e8dcf` |
| Pre-edit worktree | Clean; all three task documents absent |
| Local baseline capture | `/tmp/aek-godot-planning-20261022-k2_p7pzg/baseline.json` |
| Execution mode | Inline, one coherent planning stage followed by user review |
| Git authorization for this task | No staging, commit, branch, worktree, push or release requested |
| Model/delegation reference | [Model configuration](../../standards/model-configuration.md); no delegation selected |
| Available local runtime evidence | `godot`, `godot4`, `gdformat`, `gdlint`, `dotnet` absent from the session PATH; no installation or runtime trial |

The previous task's commit/push permission is not a Git action request for this new
proposal. On resumption, compare current state with this baseline, preserve new user
edits and capture a new implementation-stage baseline before changing active policy.
Do not reconstruct historical evidence as if it tested newly implemented content.

## Global constraints

- Write repository artifacts in English; communicate with the user in Russian.
- GDScript is primary; C# and GDExtension apply only when selected by the project/task.
- Godot 4.7 is the researched documentation baseline. Preserve actual project
  versions, platforms and renderer; no implicit upgrade or all-4.x certification.
- One optional `godot` profile depends on `core`. Topics have single rule owners;
  availability does not force all topics to be read. Tool implementation languages
  do not introduce application-stack dependencies.
- Reuse shared responsibility placement, readability acceptance, evidence reuse,
  orchestration and adoption policy. No extra agents or whitespace review rounds.
- Preserve user edits, scene/resource identities and local adaptation boundaries.
  No repository-wide formatting, mass scene resave or forced architecture template.
- Keep tool versions/comparisons in dated research. Do not install providers, edit
  global client configuration, enable telemetry or modify third-party caches.
- Separate documentation/source review, manual scenario reasoning, artifact tests
  and actual engine/provider trials. Do not describe one as proof of another.

## Stage 1: research and reviewable proposal

- [x] **GDT-1 — Inspect source ownership and gather primary evidence.**
  Read the applicable repository/Superpowers/planning policies and engine-profile
  routes. Research official versioned Godot contracts, original community practices
  and maintainer MCP/tool documentation. Record dated versions, evidence limits,
  disagreements and conditional recommendations in the research document.
  Acceptance: concrete source owners identified; GDScript/C#/GDExtension scope
  resolved; recommendations distinguish built-in tools, optional runners and MCP.
- [x] **GDT-2 — Specify the correction, plan delivery and validate the proposal.**
  Complete the linked specification and this plan, including single-owner topics,
  relevant integration routes, manual scenarios and future checks. Review consistency
  with existing policy, check all three documents and inspect new-file whitespace.
  Acceptance: artifact checks pass, review findings resolved, scope remains the three
  documents, and evidence/limits are recorded below. **Completed; review checkpoint.**

Stage 1 changes only:

- `docs/research/2026-10-22-godot-engineering-and-mcp.md` — dated sources and recommendations.
- `docs/specs/2026-10-22-godot-support.md` — proposed practices, ownership and acceptance.
- `docs/plans/2026-10-22-godot-support.md` — execution context, tasks and evidence.

Planning-stage checks:

```sh
python3 -B tools/check_instruction_artifacts.py docs/research/2026-10-22-godot-engineering-and-mcp.md docs/specs/2026-10-22-godot-support.md docs/plans/2026-10-22-godot-support.md
git diff --check
git status --short
```

Additionally inspect the three untracked files for trailing whitespace and their
complete contents; `git diff --check` alone does not cover them. No source checker
regression suite or Godot build is justified merely by planning-document additions.
External source evidence is the dated research; the artifact checker does not fetch
external links or verify their claims.

## Stage 2: implement the profile after review

**Completed, including the two final-review corrections; authorized for Git delivery.**
GDT-3 through GDT-5 form one coherent source-library
implementation stage. Internal task completion is not a separate approval or
automatic extra test/review checkpoint. Apply any user changes to the design before
starting; do not interpret unchecked tasks as authorization.

- [x] **GDT-3 — Author the engine entry and canonical topics.**
  Entry and eight canonical topics authored; acceptance validation follows in GDT-5.
  Dependencies: reviewed specification and reconciled current baseline.
  Create `standards/godot.md` and exactly the eight topic owners listed in the
  [ownership table](../specs/2026-10-22-godot-support.md#authority-routing-and-ownership).
  The entry routes by task and records the actual supported context; it contains
  neither all topic rules nor an installation tutorial.

  Implement architecture, GDScript, lifecycle/runtime, assets/export, UI/performance,
  interop, tooling/MCP and verification requirements from the specification. Keep
  the Godot-specific semantics with their owner: resource sharing in runtime;
  serialization/UIDs in assets; GDScript grouping in GDScript; provider operation
  and recovery in tooling; evidence selection in verification. Cross-link instead
  of copying. Use official versioned links in the deliverable; avoid requiring the
  dated research file inside every adopted bundle.

  Include small GDScript grouping and responsibility-placement examples only where
  they resolve ambiguity. Prefer minimal illustrative snippets over a sample game.
  If introducing executable fixtures or asserting snippet execution, perform the
  applicable documented checks with the selected engine and record the result;
  otherwise label examples/command shapes accurately and retain the evidence limit.
  No engine installation follows automatically from documentation authoring.

  Acceptance: all owner topics exist, the short router covers relevant triggers,
  GDScript and optional language boundaries are clear, and no copied generic policy
  or unconditional tool mandate was introduced.

- [x] **GDT-4 — Connect catalog, target routes and migration.**
  Catalog/entry integration and closure/adoption checks passed; evidence below.
  Dependency: complete profile resources from GDT-3.
  Make the following narrowly scoped changes; retain existing schemas and mechanics.

  | Existing path | Intended change |
  | --- | --- |
  | `standards/catalog.toml` | Register `godot`, its `core` dependency and complete resource inventory |
  | `standards/catalog.md` | Explain independent Godot selection and conditional resources where selection guidance needs it |
  | `templates/policy-entry.md` | Short conditional route to the Godot entry |
  | `templates/AGENTS.root.md` | Reachable applicable-profile route for Godot projects |
  | `templates/AGENTS.project.md` | Reachable Godot profile from independently opened project scope; reuse generic routing when sufficient |
  | `templates/project-architecture.md` | Conditional actual engine/edition, platforms/renderer, ownership, assets, checks and optional tool context |
  | `MIGRATION.md` | Godot selection and version-sensitive adaptation; reuse B/C/N updates and configuration-preservation rules |
  | `README.md` | Add Godot to available technology navigation after the profile exists |
  | `ARCHITECTURE.md` | Only a small inventory/example adjustment if needed for an accurate source-library description |
  | `tests/test_profile_selection.py` | Add the Godot topic inventory and meaningful closure/isolation/composition assertions |

  Test that `godot` includes its complete resources, excludes unrelated engine/web/
  Python/Node stacks, composes with `project-workflows`, and can be explicitly selected
  alongside `unreal-engine` without either engine implicitly selecting the other.
  Extend existing control assertions rather than testing incidental prose wording.

  Inspect shared bodies `templates/agents/implementer.md` and `reviewer.md` and native
  adapters under `templates/codex/agents/`, `templates/claude/agents/` and
  `templates/cursor/agents/`. Their existing shared-body/profile routes should suffice;
  change them only if a concrete unreachable route is demonstrated. Do not duplicate
  Godot rules or change model settings merely to add a profile.

  Acceptance: source inventory and conditional routes agree; profiles remain
  independent; both new adoption and updates deliver the authoritative instructions
  while preserving target-owned customization. Generic checker code needs no change
  unless an actual unsupported artifact contract is discovered.

- [x] **GDT-5 — Validate implemented policy and adoption boundaries.**
  Reopened and completed after the final review: corrected ambiguous constructor
  guidance and the overbroad measurement prerequisite for native integrations.
  Updated both owners and the specification; checked artifacts and focused scenarios.
  Earlier route/adoption regression evidence remains valid for unchanged mechanisms.
  Dependencies: GDT-3 and GDT-4 complete.
  Run the relevant source artifact and profile-selection checks. Use the existing
  native-role checks for affected route evidence; extend portability/adoption fixtures
  only where the changed integration contract needs a new regression case.

  Prepare a temporary selected Godot bundle using the existing migration approach.
  Check nested/default layout and an independently opened project route; include the
  actual installed entries explicitly where the checker would not discover them.
  If existing fixture coverage already proves a layout's unchanged rebase mechanism,
  reuse it and check the new Godot route rather than recreating every client matrix.
  Omit optional history safely and run the checker with `--profile godot` and the
  actual bundle directory. This is a candidate fixture, not a user's installation.

  Exercise an update candidate with a locally customized entry/check choice: compare
  B/C/N, preserve local content and retain a single canonical style owner. Assess
  conflicts/new acceptance criteria explicitly. This manual exercise is not an
  automated migration test unless implemented as an actual executable fixture.

  Apply S01–S16 to the implemented text and record any changed outcome. Inspect for
  ambiguous obligations: shared versus per-instance resources; domain ownership
  versus `Node.owner`; script organization versus package boundaries; conditional
  MCP versus mandatory setup; parse versus build/runtime/visual evidence; reference
  version versus forced upgrade. Review the actual scoped diff and preserve unrelated
  rules. Follow existing risk-based review policy; no second reviewer solely for style.

  Acceptance: applicable checks and the accountable review pass, integration evidence
  covers the new routes, unresolved limits are explicit, and the stage is presented
  for user review without unauthorized Git actions or target setup.

Expected Stage 2 command selection, **not executed in Stage 1**:

```sh
python3 -B tools/check_instruction_artifacts.py
python3 -B -m unittest discover -s tests -p 'test_profile_selection.py'
python3 -B -m unittest discover -s tests -p 'test_agent_templates.py'
git diff --check
```

The no-path artifact check covers source catalog/standards/templates/root documents;
explicitly check any newly changed historical docs. Run
`test_project_skill_portability.py` or `test_project_skill_adoption.py` when their
route/candidate logic is changed or used for new relevant coverage. Run
`test_instruction_artifacts.py` if checker behavior is actually changed. Do not
broaden to every application example merely because a new profile is available.

## Conditional later activity: target/provider trial

- [ ] **GDT-6 — Qualify a selected target toolchain/provider, only if requested.**
  **Optional and not selected; not a prerequisite for source-profile completion.**
  Choose the actual project, engine/platform, client and concrete missing capability.
  Recheck dated provider/tool contracts, then prepare a reviewable configuration and
  dependency change under the existing adoption process. Preserve existing runner,
  plug-ins and local client settings; select configuration scope deliberately.

  For MCP, follow the specification's
  [bounded provider exercise](../specs/2026-10-22-godot-support.md#small-provider-acceptance-exercise).
  Record actual tested release pairs, capability limits and removal/recovery steps.
  For a formatter/runner, verify current syntax, relevant configuration, test
  discovery and failure exits before making a check mandatory. For C#/GDExtension,
  qualify the actual additional toolchain only if that language is present.

  Acceptance: only selected capabilities have observed supporting evidence and a
  working direct-tool fallback where appropriate. Retain "not tested" for the rest.
  No Godot/MCP installation or purchase is performed by this planning task.

## Requirement traceability

| Design concern | Implementation/validation items |
| --- | --- |
| Responsibility-first composition and semantic readability | GDT-3; GDT-5, S02–S04 and S15 |
| Runtime lifetime, sharing and UI contracts | GDT-3; GDT-5, S05 and S08–S09 |
| Serialization, UID preservation and export | GDT-3; GDT-5, S06–S07 and S12 |
| Conditional languages and accurate check claims | GDT-3; GDT-5, S10–S13 |
| Optional tools, MCP recovery and source authority | GDT-3; GDT-5, S01 and S14; optional GDT-6 |
| Profile/native routes and customization-preserving updates | GDT-4; GDT-5, S16 |

## Evidence and handoff

GDT-1 and GDT-2 are complete. On 2026-10-22:

- The explicit three-document artifact check returned `Checked 3 artifacts; 0 error(s).`
  It checked local links/anchors, supported format and the unchanged source catalog;
  it did not validate external web content or agent behavior.
- `git diff --check` exited 0. A separate Python inspection of all three new UTF-8
  documents found no trailing whitespace, CR endings or missing final newline.
- Worktree inspection matched exactly the three new task documents; tracked files
  and HEAD remained at the captured baseline.
- One inline accountable review covered the full proposal, source ownership,
  conditional routes, responsibility/readability policy, tool-evidence limits and
  scope. Wording was clarified to avoid interpreting semantic grouping as mechanical
  insertion and to keep provider recommendations explicitly third-party/conditional.
  No unresolved policy conflict was identified in this scoped review.
- S01–S16 were assessed manually against the proposed rules. These are documented
  design judgments, not automated regression tests or an independent agent review.
  No Godot build, import, runner, MCP session or target installation was executed.

Current checkpoint: user review of the three documents. Proposed next stage:
GDT-3 through GDT-5 after the implementation request and any design corrections.
GDT-6 remains optional and unselected. There are no unresolved blockers to the
planning deliverable; runtime/provider compatibility remains explicitly untested.

### Stage 2 execution record

The user's subsequent implementation request authorizes GDT-3 through GDT-5 in
the current checkout. The Stage 1 checkpoint above is historical. Before edits,
HEAD was unchanged and the only existing changes were the three Stage 1 documents.
The scoped baseline, including their actual contents and new-profile path absence,
is `/tmp/aek-godot-implementation-20261022-ur4unr9y/baseline.json`, with file copies
beside it. The research and specification remain unchanged as design/evidence inputs.

Execute inline through `executing-plans` with AEK's local adaptations: one canonical
plan, current checkout, phase-end checks and accountable scoped review. No new
worktree, helper ledger, Git action, tool installation or automatic extra review
cycle is selected. The profile resource set feeds the catalog/entry routes; those
routes feed closure and adoption checks. No conflicting interface was found in
this pre-implementation assessment.

GDT-3 produced the short entry and eight topic owners. GDT-4 added conditional
catalog/entry/passport/migration routes, technology navigation, closure/isolation
cases and Godot coverage in existing portability fixtures. The fixture adapter now
classifies the Godot entry as an optional route when the profile is not selected;
required Godot resources still fail if missing from a selected bundle.
Shared/native role bodies already explicitly load applicable profiles and the
shared readability policy, so no duplicated role policy or model edits were needed.
GDT-5 validated the complete stage. GDScript excerpts are illustrative and were
checked against the official 4.7 style/ProgressBar contracts; no engine execution
is claimed.

### Stage 2 validation and review

Executed on 2026-10-22 against the implemented profile and integration changes:

| Check | Result and covered scope |
| --- | --- |
| `python3 -B tools/check_instruction_artifacts.py` | 231 source artifacts, 0 errors; catalog, resources, local links/anchors and supported document formats |
| `python3 -B -m unittest discover -s tests -p 'test_profile_selection.py'` | 35 tests passed; includes complete Godot resources, no unrelated dependencies and explicit profile composition |
| `python3 -B -m unittest discover -s tests -p 'test_project_skill_portability.py'` | 4 tests passed, including Godot subcases in nested, flat and custom bundle layouts with independent child roots and preserved local files |
| `python3 -B -m unittest discover -s tests -p 'test_project_skill_adoption.py'` | 7 tests passed; omitted conditional Godot route is adapted without dropping mandatory selected resources |
| `python3 -B -m unittest discover -s tests -p 'test_agent_templates.py'` | 6 tests passed; shared role-body routes for Codex, Claude and Cursor remain valid |
| `git diff --check` plus separate new-file inspection | Passed; inspected UTF-8/LF, final newlines and trailing whitespace, including untracked profile files |
| Baseline comparison | Exactly 22 implementation-stage paths changed; research/specification bytes and HEAD preserved; no unrelated paths changed |

Total: **52 regression tests passed**. These are instruction artifact/route tests,
not model behavior evaluations or native-client execution. No checker behavior,
shared role policy, model configuration or unrelated technology rule was changed.

A separate **manual B/C/N update exercise with assertions** used the captured old
policy-entry template for B, a locally extended C with an existing test command,
and the new adapted Godot entry for N. Reconciled that independent local section
explicitly and checked the resulting temporary selected bundle: **53 artifacts,
0 errors**. Existing task, policy override, client configuration and local check
were preserved. No Python/Unreal profile or optional research archive was introduced.
The fixture is retained at
`/tmp/aek-godot-implementation-20261022-ur4unr9y/update-assessment/`, including
`B.md`, `C.md`, `N.md` and `check.log`. This is not a general merge implementation,
automated migration regression test or downstream installation.

One inline accountable review covered the tracked diff and all nine new profile
documents, authority/routing, scoped acceptance and tool/version limits. No
unresolved in-scope conflict was identified. Detailed GDScript spacing/examples
have one active owner; verification and role routes reuse shared acceptance policy.
Risk-based review did not select an additional reviewer for this instruction-only
change with existing adoption/checking mechanisms. Native client loading and
engine/provider behavior remain untested; passing template tests does not prove them.

### Implemented scenario assessment

S01–S16 were assessed manually against the actual source owners below. This is
semantic instruction review, not an automated regression or independent agent test.

| Case | Implemented owner and assessment |
| --- | --- |
| S01 | [Entry](../../standards/godot.md): source work proceeds without MCP or unused language setup. |
| S02 | [Architecture](../../standards/godot/architecture.md#choose-owners-before-writing): cohesive movement steps stay together; no size-based extraction finding. |
| S03 | Same owner: menu presentation and save serialization get their existing independent owners immediately. |
| S04 | [GDScript grouping](../../standards/godot/gdscript.md#semantic-grouping-inside-functions): compact distinct phases require a finding; grouped phases and the contiguous operation/guard are accepted; cohesive configuration remains together. |
| S05 | [Runtime state](../../standards/godot/lifecycle-runtime.md#lifetimes-and-state): shared configuration cannot accidentally own actor-specific mutable health. |
| S06 | [Serialization](../../standards/godot/assets-export.md#scenes-and-resource-identity): a node meant to persist needs serialization ownership and save/reopen evidence; current editor visibility is insufficient. |
| S07 | Serialization and [reuse](../../standards/godot/verification.md#reuse-and-reporting): preserve moved UID identity, check affected references and retain only still-applicable evidence. |
| S08 | Runtime state: delayed completion after scene replacement needs a defined lifetime/result policy and affected transition evidence. |
| S09 | [Input](../../standards/godot/ui-performance.md#input-and-ui): unintended gameplay activation from a UI click violates the input contract. |
| S10 | [C#](../../standards/godot/interop.md#c): empty/unchecked script diagnostics cannot replace a compiler result. |
| S11 | [GDExtension](../../standards/godot/interop.md#gdextension): build success does not establish engine/API/target loading compatibility. |
| S12 | [Export](../../standards/godot/assets-export.md#export-and-editor-execution): missing exported assets need inclusion/loading correction and the affected target check. |
| S13 | [Test tooling](../../standards/godot/tooling-mcp.md#formatting-and-tests): no intended discovered tests means no claimed behavior coverage. |
| S14 | [MCP operations](../../standards/godot/tooling-mcp.md#editor-and-mcp-operations): inspect and reconcile partial mutations before retry. |
| S15 | Verification reuse: an earlier clean review does not prove a newly adopted requirement; assess the missing scope explicitly. |
| S16 | [Migration](../../MIGRATION.md#repeat-and-update) plus the update exercise: preserve local entries/checks and avoid a second runner or unrelated stack. |

The GDScript examples and engine CLI shapes were not parsed/run locally:
`godot`, `godot4`, `gdformat`, `gdlint` and `dotnet` remain absent from the session
PATH. No tools, add-ons or native roles were installed. This does not block source
instruction acceptance, but leaves the optional GDT-6 target qualification unselected.

Handoff: GDT-3, GDT-4 and GDT-5 are complete. The implementation is ready for user
review; no commits, pushes or releases were made. New adoptions select `godot`;
existing integrations use the documented customization-preserving update procedure.

### Final-review corrections

On 2026-10-22 the user requested an additional final review and then authorized
fixing its two findings. The Stage 2 review result above is historical, not evidence
that these newly identified ambiguities were absent. GDT-5 was reopened for this
bounded correction and is now complete; GDT-3/GDT-4 and optional, unselected GDT-6
retain their scope.

The current contents of the two policy owners, specification and this plan were
captured before edits at
`/tmp/aek-godot-review-fixes-20261022-g7mbxqrh/baseline.json`, with scoped copies
beside it. The baseline also records HEAD and hashes of the existing changed files
to distinguish this correction from earlier work.

The [architecture owner](../../standards/godot/architecture.md#dependencies-and-communication)
now distinguishes explicit setup, engine-created/duplicated objects and direct
construction, including dependency timing. Checked the linked Godot 4.7 creation
contracts, [Node readiness](https://docs.godotengine.org/en/4.7/classes/class_node.html#class-node-private-method-ready)
and [GDScript initialization order](https://docs.godotengine.org/en/4.7/tutorials/scripting/gdscript/gdscript_basics.html#initialization-order).
The [performance owner](../../standards/godot/ui-performance.md#performance) limits
the measurement prerequisite to performance-driven changes and retains the existing
interop checks for functional native integrations. The specification is aligned;
dated research and earlier validation records remain intact.

Executed checks for this correction:

- `python3 -B tools/check_instruction_artifacts.py standards/godot/architecture.md standards/godot/ui-performance.md docs/specs/2026-10-22-godot-support.md docs/plans/2026-10-22-godot-support.md`
  returned **4 artifacts, 0 errors**; source catalog and affected local links/format.
- `git diff --check` passed. Separate inspection covered UTF-8/LF, final newlines
  and trailing whitespace in all four untracked files.
- Scoped baseline comparison found exactly those four changed paths; HEAD and all
  other pre-existing changes were preserved.

Focused **manual instruction assessment**, not automated or in-engine tests:

| Scenario | Assessment under the corrected policy |
| --- | --- |
| Scene creation or node duplication with required `_init` parameters | Finding required: the engine path needs a no-argument call. Defaulted parameters remain possible. |
| Custom resource with required `_init` parameters that must support `duplicate()` | Finding required for its duplication contract; assigning data later does not repair failed construction. |
| Directly created object supplied with constructor arguments on every actual creation path | Accepted; no blanket constructor ban or mandatory setup method. |
| Dynamically instantiated scene receives a dependency before tree entry; setup needing ready nodes occurs later | Accepted if callbacks use the dependency only after supply and dependent behavior waits for setup. Pre-tree use of `@onready` fields requires a finding. |
| Native library supplies required functionality without a speed claim | No missing-benchmark finding; interop compatibility, loading and behavior evidence remain required. |
| Native conversion is proposed to improve performance, or a separate speed claim is made | Measurement remains required; functional integration alone cannot support a speed claim. |

Both findings are resolved in this scoped assessment; no additional policy conflict
was identified in the changed rules and their existing lifecycle/interop consumers.
Earlier catalog, native-role and adoption test results remain applicable to unchanged
routes/mechanisms and were not rerun. They do not prove semantic compliance with the
clarified rules. No engine/client trial, additional reviewer, installation or Git
action was performed. GDT-5 is complete; this correction is ready for user review.

### Authorized Git delivery

After the correction handoff, the user explicitly requested committing and pushing
the work. This supersedes the earlier no-Git scope for this delivery only. Include
the 24 reviewed Godot profile, integration, test and task-document paths in one
commit on the current `main`, then push to `origin/main` without force. Preserve
the earlier evidence limits; no target installation is selected.

The pre-delivery plan and scoped file hashes are captured at
`/tmp/aek-godot-git-delivery-20261022-7_s45ebd/`. Reuse applicable implementation and
correction evidence, check this updated report, and verify the staged scope and
remote state. Report the resulting commit and push outcome in the session handoff.
