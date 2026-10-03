# Unreal Engine support implementation plan

Date: 2026-09-27. Status: U1–U4 complete; Unreal library support delivered. Target pilot not run.

**Goal:** Deliver importable Unreal rules that guide engine-specific engineering,
editor operations and sufficient verification in new and existing projects.
**Architecture:** One short profile entry routes to six conditional sections.
Common policy keeps scope, evidence and workflow ownership; narrow entry/passport
clarifications accommodate engine-managed construction and gameplay structure.
**Artifacts:** English Markdown rules/templates, schema-1 TOML catalog metadata,
Russian README. No runtime code, engine plugin or new skill.
**Spec:** [Approved Unreal support specification](../specs/2026-09-27-unreal-engine-support.md).
Executors read the spec and this plan; requirements remain in the spec, progress here.
**Evidence:** [Dated research](../research/2026-09-27-unreal-engine-engineering-and-mcp.md).
Reuse its relevant findings and sources; resolve consequential gaps only.

## Global Constraints

- The user confirmed the specification and this plan on 2026-09-27, including
  inline execution with review after each stage. U1–U3 were accepted and U4 authorized
  by the latest instruction to proceed. Project integration is a separate task.
- Workspace/instruction root and execution checkout:
  `/home/vitalii/Documents/Local_Project/AgentsFramework`. This file is the canonical
  execution record; the linked spec owns requirements. No task-store relocation.
- Recommended execution after approval: inline with `superpowers:executing-plans`,
  one logical stage and a user checkpoint. Reuse later explicit authorization for
  multiple stages. No delegation or model configuration is needed for this task.
- Apply [Superpowers adaptations](../../standards/superpowers.md), including the
  existing work-mode and proportionate verification rules. No stock mandatory
  commits, worktrees, TDD campaign, extra reviewer or repeated final run.
- Preserve original contents/absence before each stage's first writes, including
  pre-existing user changes. Retain the baseline through scoped review and handoff.
- Reference baseline: researched UE 5.8 guidance, not a universal compatibility
  claim. Actual engine, host, target and provider capabilities govern use.
- Profile: `unreal-engine`; source `standards/unreal-engine.md`; dependency `core`;
  `technologies = ["unreal-engine"]`; descriptor hints `**/*.uproject`, `**/*.uplugin`.
  Retain `schema_version = 1` and existing profile IDs.
- Exactly six detail resources are specified below. Bundle availability is not
  mandatory reading. Research is optional background outside profile resources.
- First release includes no new skill. Mandatory MCP workflow must be portable;
  installed skills are optional, with actual capabilities verified when needed.
- Do not install an engine/client, launch MCP, alter personal settings/plugin caches,
  import into a target or run external models. A target pilot is separate work.
- General C++, UEFN/Verse, detailed specialist subsystems and the deferred project
  integration mechanism remain outside this implementation.

## File ownership and stage order

| Stage | Create | Modify |
| --- | --- | --- |
| U1: C++, gameplay and evidence | `standards/unreal-engine/cpp-lifetime.md`, `standards/unreal-engine/gameplay-blueprints.md`, `standards/unreal-engine/verification.md` | This plan's stage result |
| U2: Build, runtime and editor | `standards/unreal-engine/build-assets.md`, `standards/unreal-engine/runtime-performance.md`, `standards/unreal-engine/mcp-editor.md` | U1 files only for concrete cross-section findings; this plan |
| U3: Profile and shared integration | `standards/unreal-engine.md` | `standards/catalog.toml`, `standards/catalog.md`, `standards/core.md`, `templates/AGENTS.root.md`, `templates/AGENTS.project.md`, `templates/policy-entry.md`, `templates/project-architecture.md`, `MIGRATION.md`, `ARCHITECTURE.md`, this plan |
| U4: Acceptance and handoff | None | `README.md`, this plan, `docs/plans/2026-09-27-project-rule-integration.md`; prior stage files only to fix findings |

U1/U2 produce complete, reviewable reference sections before registration. Do not
activate profile/entry routes or link to missing future files. U3 connects the
completed resources as one coherent profile. Use direct relevant source citations
in rules; mandatory references must remain reachable in the selected bundle.
Do not require copied research or an absolute personal skill path.

## Review focus and ownership

| Material failure | Owner and evidence |
| --- | --- |
| Generic DI advice overrides engine creation, or guard simplification removes a real lifetime check | U1 walkthrough A5–A6; U3 reconciles common entry wording |
| Blueprint-only/source-only work loads every profile or forces MCP setup | U3 task routing walkthrough A1–A4; U4 checks complete routes |
| Asset edits lose unsaved/intervening user changes, or an uncertain mutation is duplicated | U2 A8/A10–A11 walkthrough with disk versus editor state and timeout outcomes |
| A native-provider recipe or local skill workaround becomes a cross-version requirement | U2 A12 and U3 version/passport checks; no runtime claim from documentation |
| A successful build is overclaimed, or final reporting triggers unnecessary reruns | U1 A13/A15; U4 reuses valid evidence and reports actual acceptance limits |

## U1: C++, gameplay and evidence rules

**Consumes:** UE3–UE4, Blueprint boundary portions of UE5, UE9; existing core and
verification policy, researched engine contracts.
**Produces:** Three complete sections defining language/lifetime, gameplay owners
and Unreal verification choices; no new active profile yet.

- [x] Capture the three files' prior absence or existing content and the plan baseline.
- [x] Write `cpp-lifetime.md`: language/naming and reflection constraints, strings,
  engine creation versus ordinary RAII, GC reference chains, weak/soft/strong/raw
  pointer uses, lifecycle hooks, and assertion/guard semantics. Preserve necessary
  invalidation checks without making all pointer access defensive by default.
- [x] Write `gameplay-blueprints.md`: Actor/Component/Controller/state/Subsystem
  ownership, worlds and players, native/Blueprint boundaries, reflected interfaces,
  lifecycle composition and conditional events/timers/Tick. Preserve appropriate
  data-only models and avoid compulsory DI containers or backend layers.
- [x] Write `verification.md`: map changed contracts to compilation, asset/Blueprint,
  focused test, PIE, package and performance evidence; preserve required gates,
  distinguish in-memory/persisted state and reuse results for unchanged inputs.
  Keep general test/review rules with their existing owner.
- [x] Walk through A5–A7 and A13/A15. Explicitly distinguish a synchronous invariant
  from an invalidatable deferred reference, and required execution from a disabled
  shipping assertion. Check these sections' links and scoped diff; no engine build
  or new permanent tests. Record the result here and apply the user checkpoint.

## U2: Build, runtime and editor operations

**Consumes:** U1 ownership/evidence contracts, UE5–UE8 and the relevant research.
**Produces:** The remaining three sections, including a standalone MCP procedure
that works without any external skill.

- [x] Preserve the stage baseline for new files and any U1 corrections.
- [x] Write `build-assets.md`: UBT/UHT target/configuration/platform, public/private
  dependencies, editor/runtime separation, IWYU/generated files, Live Coding versus
  normal build/restart, binary assets, redirects, loading/retention and cook scope.
  Preserve source-control and unsaved-work contracts; no routine cache deletion.
- [x] Write `runtime-performance.md` with separately selectable sections for
  concurrency/lifetime, network authority/ownership and measured performance.
  Keep GAS/Lyra conditional and avoid speculative multiplayer or optimization.
- [x] Write `mcp-editor.md`: context selection, bounded discovery, exact identifiers,
  recoverable prior state including dirty assets, serial native calls, one shared
  editor mutation owner, completion/error interpretation, timeout inspection,
  scoped save and partial recovery. Distinguish pending completion from a retry.
- [x] Include version/provider-aware local setup boundaries and optional installed
  skill use; no forced global configuration, unconditional session restart or copied
  workstation workaround. Define when a missing operation warrants custom-tool
  evaluation, without implementing a plugin or requiring a new skill.
- [x] Walk through A8–A12 and A14 using concrete read/write/timeout/restart cases.
  Check that disk backups do not stand in for dirty editor state, package and object
  identifiers are not conflated, and pinning does not promise thread safety.
  Check affected links/diff and record outcomes without a live editor pilot.

## U3: Register the profile and reconcile shared guidance

**Consumes:** All six completed resources, UE1–UE2/UE10 and U1's architecture rules.
**Produces:** A reachable portable profile with actual task routes and compatible
entry/passport guidance; no dependency on a personal skill installation.

- [x] Capture the baseline of each modified path and the new entry's prior absence.
- [x] Create `standards/unreal-engine.md` with version/evidence boundaries, task
  routes to the six resources and explicit Blueprint-only/source-only behavior.
  Link only existing resources; select subsections within runtime guidance.
- [x] Register the exact UE2 profile values and six resources in `catalog.toml`;
  use applicable design/implementation/test/review/setup activities and a `when`
  condition based on actual Unreal context. Do not make it globally required or
  add Python as an unconditional dependency. Add Unreal reading examples to
  `catalog.md`, preserving availability-versus-reading semantics.
- [x] Reconcile the construction and DIP passages in `core.md`, compressed wording
  in `AGENTS.root.md`, and relevant project/policy entry routes. Engine-managed
  composition must not imply custom DI constructors or backend layer scaffolding.
  Preserve business invariants, typing rules for other stacks and mode/evidence rules.
- [x] Adapt `project-architecture.md` to allow gameplay/editor entry points and
  flows. Add a conditional compact Unreal context section with version/build,
  target/module/asset/lifetime/required-check ownership and relevant MCP facts.
  Retain intended-versus-observed evidence; omit irrelevant backend fields at adoption.
- [x] In `MIGRATION.md`, qualify architecture/DI inventory for Unreal and add the
  relevant conditional-read check. In `ARCHITECTURE.md`, reconcile profile/skill
  ownership and engine-managed composition where affected. Keep import-skill
  implementation, model selection and task-store behavior with existing owners.
- [x] Parse the catalog with Python `tomllib`; require schema 1, unique IDs,
  retained existing profile identities, valid dependencies and all seven Unreal
  files present. Check affected Markdown and fenced passport TOML, including
  template links from their intended adopted location.
- [x] Walk through A1–A5 and A12 with a Blueprint project, an older source-only
  project, a generic C++ file, Python editor scripting and an independently opened
  target. Verify no full-bundle reading or mandatory external skill. Review the
  scoped integration diff, record the result and apply the checkpoint.

## U4: Library acceptance and documentation

**Consumes:** U1–U3 artifacts/evidence and all approved acceptance scenarios.
**Produces:** Documented library readiness and a precise dependency handoff to
project integration, without an implicit target pilot or import.

- [x] Preserve the baseline and add the Unreal profile to README navigation and
  scope descriptions: conditional sections, documented version baseline, optional
  MCP/skills and verification limits. Keep user-facing prose Russian.
- [x] Map A1–A15 to the completed rule sections and prior checks. Resolve concrete
  gaps; reuse valid walkthrough and format results. Check newly changed routes or
  formats rather than rerunning unchanged evidence as a final ceremony.
- [x] Inspect the scoped cumulative diff against stage baselines, including new
  files and pre-existing edits. Confirm no active links to missing resources,
  personal paths in delivered rules, accidental catalog expansion or conflicting
  common policy. Correct in-scope defects and recheck only affected contracts.
- [x] Record changed paths, requirements/scenarios met, commands/inspections and
  results, relevant artifact state and limitations in this plan. Library checks
  do not establish native discovery, actual model behavior, engine builds or MCP
  runtime compatibility.
- [x] Update the dependency state in the project-rule integration plan with the
  actual support result. Its implementation remains deferred until the user
  authorizes resumption; no import skill or adoption record is created here.

## Verification execution notes

Use existing tools and temporary scripts where useful. `python3 -c 'import tomllib;
from pathlib import Path; tomllib.loads(Path("standards/catalog.toml").read_text());
print("catalog syntax: PASS")'` checks syntax only; U3 also owns catalog identity,
dependency/resource and routing checks. Plain Markdown links can be resolved with
`pathlib`; respect the declared installed locations of template links.

Walkthroughs check instruction decisions and contradictory routes, not engine
execution. Preserve concise outcomes under each stage result here; temporary
logs/diffs are supporting evidence, not another canonical task ledger. No new
renderer, validator dependency, test runner or fixed review count is required.

## Current handoff

- Approved: support specification and implementation plan, including one profile,
  six resources and no new mandatory skill; inline execution with stage checkpoints.
- U1–U3 are accepted; U4 is complete. Library acceptance covers UE1–UE10 and
  A1–A15; the next separate task is project integration on resumption. U1 evidence remains in
  `/tmp/af-unreal-u1-9d_wkik2/`; U2 baseline is `/tmp/af-unreal-u2-93f25new/`.
  U3 baseline is `/tmp/af-unreal-u3-rc3dmm36/`;
  U4 baseline is `/tmp/af-unreal-u4-3i_m7xx9/`.
- Historical planning baseline: `/tmp/af-unreal-plan-llcditi0/`. That preparation
  created the plan, recorded specification approval and updated the dependency link;
  implementation and its evidence are recorded in U1–U4 below.

## U1 result and verification

Created `standards/unreal-engine/cpp-lifetime.md` (101 lines),
`standards/unreal-engine/gameplay-blueprints.md` (77 lines) and
`standards/unreal-engine/verification.md` (87 lines). Updated only this plan for
authorization/progress. The new sections have no active catalog or entry route yet.

Scoped Python `pathlib`/Markdown checks passed: 12 local links and fragments,
balanced fences, no placeholder markers or personal paths in delivered sections.
The sections cite 20 distinct official source URLs. Existing research was reused;
targeted official documentation confirmed Blueprint interface dispatch and Actor
teardown details. This was not a new general research sweep or an external link
availability audit.

| Scenario | Instruction walkthrough result |
| --- | --- |
| A5 | UObject/default-subobject construction and Actor spawning are distinct; hooks follow dependency availability. Gameplay composition permits engine-managed dependencies without custom DI constructors. Common entry reconciliation remains U3. |
| A6 | The synchronous invariant avoids duplicate guards; a deferred weak reference is resolved after possible invalidation. Required side effects cannot depend on shipping-disabled `check`; `verify`/`ensure` do not replace reachable-failure handling. |
| A7 | A Blueprint-only interface implementation uses reflected support checks where needed and generated `Execute_` dispatch. Direct `_Implementation` and a native interface cast cannot substitute for Blueprint-aware dispatch. |
| A13 | A local change selects relevant evidence and required gates. Reporting, a new agent or an unrelated restart does not mandate another full build/cook/test cycle. |
| A15 | Library artifact checks, editor state and runtime evidence are distinguished; no editor, build or package success is inferred from this stage. |

Scoped review of the three new documents and the plan change found no unresolved
U1 defect. Baseline, diff and check output: `/tmp/af-unreal-u1-9d_wkik2/`.
No engine execution, permanent tests, catalog edits, native setup, Git writes or
delegation occurred. The completion note changes only progress/evidence text;
  the checked rule files and existing link targets remain unchanged.

## U2 result and verification

Created `standards/unreal-engine/build-assets.md` (92 lines),
`standards/unreal-engine/runtime-performance.md` (74 lines) and
`standards/unreal-engine/mcp-editor.md` (110 lines). Updated this plan's progress;
U1 sections did not require corrections. Profile registration remains U3.

Scoped Python Markdown checks passed: 12 local links and fragments, balanced
fences, no placeholder markers or personal paths in the new rules. They cite 20
distinct official source URLs. Reused research and U1 evidence; a targeted read of
the official MCP page confirmed serial calls, local/no-auth behavior, configuration
generation differences and tool-refresh/restart constraints. No general source
re-audit or live provider check was needed.

| Scenario | Instruction walkthrough result |
| --- | --- |
| A8 | Asset moves preserve references and dirty state; asset and Core Redirects have separate owners. Fixup scope includes affected referencing packages, without automatic project-wide resaves or checkout/check-in. |
| A9 | Runtime/editor dependencies and public/private headers determine the build boundary. Body-only patching is not evidence for changed reflection/layout, a cold start or target packaging. |
| A10 | Context identifies the intended project/editor/world. Native reads and writes are serial; a shared editor has one mutation owner. Discovery is limited to needed tools and identifiers. |
| A11 | Pending completion is observed rather than resubmitted. Unknown spawn/import outcomes are inspected before retry; unresolved outcomes stop dependent writes. Dirty/intervening user work survives scoped saving or recovery, and reload invalidates affected handles. |
| A12 | Native commands are provider-specific; external skill recipes and restart assumptions are conditional. Existing client settings are preserved instead of deleted to bypass configuration-generation refusal. |
| A14 | Concurrency, networking and performance have separate headings and triggers. Thread lifetime does not imply state safety; authority and performance claims require their relevant evidence. Profile-level conditional routing is completed in U3. |

Scoped review found no unresolved U2 defect. Baseline, diff and check output:
`/tmp/af-unreal-u2-93f25new/`. The checks establish instruction/artifact consistency,
not an engine build, live MCP session or runtime compatibility. No permanent tests,
native setup, Git writes or delegation occurred. This result note changes only
progress/evidence text; existing rule-file and link-check evidence remains valid.
Next checkpoint: user review of U2, then U3 on instruction to continue.

## U3 result and verification

Created `standards/unreal-engine.md` and registered its six resources. Modified
`standards/catalog.toml`, `standards/catalog.md`, `standards/core.md`, the root,
project and policy entry templates, `templates/project-architecture.md`,
`MIGRATION.md`, `ARCHITECTURE.md` and this plan. U1/U2 sections remain unchanged.

Python `tomllib`/`pathlib` checks passed: catalog schema 1, 20 unique profiles,
all 19 previous profile definitions and shared metadata unchanged, valid acyclic
dependencies, 147 existing catalog paths, one fenced passport TOML block and 76
local links/fragments. Entry-template paths were resolved from their documented
adopted root. All seven Unreal files and their direct local references fit the
selected Unreal/shared bundle; Python is not an unconditional dependency. Hashes
confirmed all six prior detail sections unchanged.

| Scenario | Integration walkthrough result |
| --- | --- |
| A1 | Declared Blueprint-only Unreal work reaches the profile and relevant gameplay/assets/verification routes, without compulsory C++ details, Python or MCP installation. |
| A2 | An older source-only project retains its actual engine version; consequential APIs are checked by capability. Editing source needs no provider connection, while unavailable dependent checks remain explicit. |
| A3 | Root/policy/project entries require a reachable selected local profile; independently opened projects do not depend on parent discovery or personal skills. Profile resources fit the selected bundle without mandatory research. |
| A4 | Only Unreal descriptor hints are registered; generic C++/headers do not establish context. Python editor scripting explicitly selects relevant Python guidance without unused backend components. |
| A5 | Core construction/DIP, compressed entries and passport flows now agree with engine-managed lifetime/composition. Existing invariants, other-stack typing and evidence/work-mode policy remain intact. |
| A12 | Profile selection establishes neither an installed provider nor a skill. Native UE 5.8 is a documented reference, with installed-version/provider decisions kept conditional. |

Scoped integration review found no unresolved U3 defect. Role templates were
searched only for conflicting DI/constructor/layer mandates; none were found and
no role/configuration changes were needed. Baseline, diff and check output:
`/tmp/af-unreal-u3-rc3dmm36/`. Checks establish static catalog/route consistency,
not actual client loading or editor runtime behavior. No engine/client setup,
target adoption, permanent tests, Git writes or delegation occurred.

The completion note updates only progress/evidence text; checked rules, catalog
and link targets are unchanged. Next: user review of U3, then U4 documentation and
library acceptance on instruction to continue. Project integration stays deferred.

User clarification within U3: Unreal differs materially from the existing language
and application-framework profiles. The profile entry, catalog semantics and
architecture now state its engine/editor integration model explicitly: lifecycle,
reflection/serialization, binary assets, World/PIE state and cooking. Shared
principles apply through these contracts; backend/frontend patterns and check
routines are not automatic defaults. This clarifies the approved design without
adding a profile/schema, changing permissions or starting U4. Original U3 baselines
remain valid; the clarification adds no links or executable metadata.


## U4 acceptance record

Scope: `README.md`, this canonical plan and
`docs/plans/2026-09-27-project-rule-integration.md`. Baseline and scoped diff:
`/tmp/af-unreal-u4-3i_m7xx9/`. README documents the engine/editor model,
conditional reading, UE 5.8 research reference, optional MCP/skills and runtime
limits. The integration plan records the completed prerequisite while leaving
its implementation tasks deferred.

### Requirements and acceptance evidence

These are static instruction walkthroughs. U1–U3 outcomes above remain the
acceptance evidence; final reporting does not require rerunning their checks.

| Requirements | Delivered owners and stages |
| --- | --- |
| UE1–UE2 | Profile context/version and catalog/task routing, U3 |
| UE3 | C++ contracts, construction and lifetime, U1 |
| UE4 | Gameplay ownership and engine composition; common core/entry/passport reconciliation, U1/U3 |
| UE5 | Blueprint contracts, modules, serialized assets and target builds, U1/U2 |
| UE6 | Conditional concurrency, networking and performance sections, U2/U3 |
| UE7–UE8 | Portable MCP discovery, mutation, recovery and optional skill boundaries, U2/U3 |
| UE9 | Shared verification owner and Unreal change/evidence matrix, U1 |
| UE10 | Importable catalog/resources, local routes, documentation and accurate handoff, U3/U4 |

| Scenario | Rule owner | Accepted evidence and outcome |
| --- | --- | --- |
| A1 | Profile and catalog | U3: Blueprint-only context selects relevant rules without C++, Python or MCP setup. |
| A2 | Profile and Unreal verification | U3: source-only work preserves actual version and reports missing editor evidence. |
| A3 | Profile, catalog and entry templates | U3: all seven Unreal files fit the selected bundle; independent local routes need no personal skill path or recursive reading. |
| A4 | Catalog and profile routes | U3: generic C++ does not imply Unreal; editor Python selects only applicable Python guidance. |
| A5 | C++ lifetime, gameplay and common templates | U1/U3: engine creation and explicit ownership work without mandatory custom DI/factory layers. |
| A6 | C++ lifetime | U1: reuse synchronous invariants, revalidate invalidatable deferred references and preserve required shipping side effects. |
| A7 | Gameplay/Blueprint contracts | U1: interface dispatch preserves Blueprint implementations and affected derived behavior. |
| A8 | Build/assets | U2: serialized references and affected packages govern renames/moves; no unrequested bulk resave. |
| A9 | Build/assets and verification | U2: runtime/editor dependencies, reload boundary and actual target govern build/restart evidence. |
| A10 | MCP/editor | U2: native calls are serial, discovery is scoped and the intended editor/world has one mutation owner. |
| A11 | MCP/editor | U2: inspect a timeout before retry, reacquire invalidated handles and preserve dirty/intervening user state. |
| A12 | MCP/editor and profile | U2/U3: actual provider capabilities govern; installed skill commands are optional, version-specific guidance. |
| A13 | Unreal/shared verification | U1: run affected checks and mandatory gates; reuse valid evidence without automatic full cycles. |
| A14 | Runtime/performance and profile anchors | U2/U3: load only relevant runtime sections and establish applicable thread/authority/measurement contracts. |
| A15 | Verification, profile and README | U1/U3 plus U4 documentation: static acceptance does not establish native loading, engine builds or MCP execution. |

### Changed-path inventory

Implementation U1–U4 covers 19 distinct paths: seven new rule files and twelve
modified library/documentation files. Research and the approved specification
precede this implementation scope.

New: `standards/unreal-engine.md` and six files in `standards/unreal-engine/`:
`cpp-lifetime.md`, `gameplay-blueprints.md`, `verification.md`, `build-assets.md`,
`runtime-performance.md`, `mcp-editor.md`.

Modified: `standards/catalog.toml`, `standards/catalog.md`, `standards/core.md`,
`templates/AGENTS.root.md`, `templates/AGENTS.project.md`, `templates/policy-entry.md`,
`templates/project-architecture.md`, `MIGRATION.md`, `ARCHITECTURE.md`, `README.md`,
this plan and `docs/plans/2026-09-27-project-rule-integration.md`.

No target configuration, installed skill, engine plugin or import mechanism was
created. Native instruction discovery, actual agent behavior, builds, gameplay,
asset operations and MCP runtime remain unobserved. A target pilot is separate.


### Verification result

PASS: `python3 /tmp/af-unreal-u4-3i_m7xx9/check.py` checked 52 local links/fragments
and Markdown fences in the three U4 documents. It matched 16 delivered artifacts
against the saved U1–U3 reviewed diffs, established the 19-path cumulative scope
(seven new files, twelve modified), and confirmed the deferred integration skill
and adoption-record template remain absent. Baselines and `checks.json` preserve
these results; `changes.diff` records U4 changes.

Scoped content review found no unresolved issue in README, the acceptance mapping
or the dependency handoff. U1/U2 rule/source checks and U3 catalog/template/bundle
checks remain valid: the final artifact comparison found no unreviewed rule or
metadata changes. This reuses prior evidence for links, personal-path portability,
profile identities and common-policy reconciliation rather than repeating them.
No engine build, editor/MCP call, target import or additional test suite was run.
The final status/checklist/evidence text introduces no new links or formats;
only the saved diff was refreshed after recording completion.
