# Unreal Engine support

Date: 2026-09-27. Status: approved by the user; implementation pending.

The user authorized this specification after the
[Unreal engineering and MCP research](../research/2026-09-27-unreal-engine-engineering-and-mcp.md).
It defines the next technology addition to Agent_Engineering_Kit. The
[project-rule integration plan](../plans/2026-09-27-project-rule-integration.md)
remains deferred until that addition is implemented and checked.
This document owns the support requirements. The
[implementation plan](../plans/2026-09-27-unreal-engine-support.md)
owns stages, authorization, progress and execution evidence.

## Outcome and scope

An AI working in a new or existing Unreal project can select applicable rules,
use Unreal-specific C++ and Blueprint conventions, operate an available editor
provider within the task scope, and gather sufficient evidence without unnecessary
guards, tests or repeated checks. The imported rules work without access to the
framework author's personal skills or engine installation.

The deliverable is one technology profile, conditional reference sections,
catalog/entry/passport integration and concise documentation. It remains a
rules-only library: no engine plugin, application, installer, automated detector,
background process, project conversion or mandatory test infrastructure.

Target adoption, engine/client installation, personal configuration, Git actions
and a live editor pilot are separate scopes. This specification does not activate
rules or authorize those operations. UEFN/Verse and a standalone general C++ profile
are outside this addition. Detailed rendering, animation, Niagara, Mass and other
specialist subsystems remain task-specific follow-up work.

## Design decisions

| Choice | Decision and reason |
| --- | --- |
| Profile boundary | One `unreal-engine` profile covering Unreal C++, Blueprints and editor work; tasks select the needed sections. |
| Detail placement | Short profile entry plus six cohesive sections. Research is background, not mandatory context. |
| Version scope | Documented UE 5.8 reference baseline; actual project version and capabilities determine applicable instructions. No blanket 5.x or future-version compatibility claim. |
| MCP provider | Native `ModelContextProtocol` is the documented initial provider. Other providers require their own verified contract before use. |
| Skills | First release includes no new skill. All required workflow resides in portable rules; compatible existing skills are optional execution aids. |
| Shared rules | Narrow Unreal clarifications in core/entry/passport; common scope, evidence and work-mode rules retain their owners. |
| Verification | Library acceptance uses artifact checks and concrete instruction scenarios. Runtime confidence requires a separately scoped project pilot. |

A single large prompt would increase routine context and obscure task boundaries.
A required external skill would make imported rules depend on a personal setup.
The selected design keeps behavior complete in the library; a future thin skill
can add a useful trigger without becoming another policy owner.

## Requirements

### UE1. Version and project context

The profile must distinguish documented guidance from observed target capability.
Reuse the researched source baseline; consult version-matched documentation or
actual headers/schemas for consequential differences, not as a mandatory web
search before every task.

Record relevant facts in the existing project passport: engine version/build
identity and source, installed/source build, host and target platforms, project
or plugin type, Blueprint/C++ use, module ownership, required plugins, multiplayer
requirements and existing checks. For editor work, additionally resolve provider,
editor instance, endpoint and world/PIE context. Load only the relevant facts;
ordinary code editing does not require a complete environment questionnaire.

For a new project, distinguish intended choices from observations. For an existing
project, preserve compatible contracts and versions; do not force an engine
upgrade or generic legacy rewrite. An older engine or different provider requires
checking the affected capability, not assuming native MCP availability. Missing
editor access limits dependent verification and does not prevent source-only work.

### UE2. Portable catalog and conditional reading

Add profile ID `unreal-engine`, source `standards/unreal-engine.md`, dependency
`core`, with explicit task applicability and the six resources below. Retain
catalog schema 1 and existing IDs. Use `technologies = ["unreal-engine"]` and
Unreal descriptor hints (`**/*.uproject`, `**/*.uplugin`); generic `.cpp`, `.h` or
Python files alone must not select Unreal.

| Resource under `standards/` | Read for |
| --- | --- |
| `unreal-engine.md` | Profile selection and the current task route |
| `unreal-engine/cpp-lifetime.md` | Reflected C++, construction, ownership, lifetime, assertions and language conventions |
| `unreal-engine/gameplay-blueprints.md` | Gameplay owners, components/subsystems, Blueprint/native boundaries and interfaces |
| `unreal-engine/build-assets.md` | Modules, build/reload decisions, assets, redirects, cook and packaging |
| `unreal-engine/mcp-editor.md` | Editor-provider setup, discovery, mutation, persistence or custom-tool evaluation |
| `unreal-engine/verification.md` | Selecting Unreal checks and interpreting their results |
| `unreal-engine/runtime-performance.md` | Affected concurrency, networking or performance sections only |

Catalog resources describe bundle availability, not a reading queue. Adopted
entries must route declared or evidenced Unreal work to the profile; file globs
are hints, not an implemented detector. A Blueprint-only task need not load C++
details, and a source-only task need not load MCP instructions. Select the existing
Python rules only for actual Python work, with no implied FastAPI or other backend.

Use relocatable paths and explicit selection for independently opened projects.
Keep research outside profile resources. Stop reading once applicable rules and
contracts are known; no full-profile, full-project or tool-registry preload.

### UE3. Unreal C++ and ownership

Specify engine naming, supported language/build settings, reflected declarations
and generated-code boundaries. Choose Unreal versus standard-library facilities
by engine contracts and interoperability; avoid a blanket `std::` ban. Distinguish
`FName`, `FString` and `FText`. Do not copy Epic copyright notices into user-owned
code or enable RTTI/exceptions globally merely to satisfy a generic example.

Distinguish engine-managed UObject creation, Actor spawning and ordinary C++
resource ownership. Cover constructor/default-object constraints, default
subobjects, lifecycle hooks and required parent behavior. Select initialization
and cleanup by dependency/lifetime, including component registration and world
transitions; do not force every operation into constructors or `BeginPlay`.

Explain tracked `UPROPERTY`/`TObjectPtr` references, weak caches, soft assets,
ordinary short-lived raw pointers and deliberate strong references outside
UObject owners. Retention must be valid through the owning reference chain;
pointer syntax alone is not a guarantee. RAII remains useful for ordinary resources;
ordinary shared/unique pointer ownership must not manage UObjects.

Guard guidance must identify the invariant or reachable failure. Reuse an unchanged
validated fact, while retaining necessary checks after deferred execution,
destruction, unloading or another invalidating boundary. Explain shipping behavior
of `check`, `verify` and `ensure`; required side effects cannot depend on a disabled
assertion. Do not hide invalid state with a successful-looking fallback.

### UE4. Gameplay structure and reconciliation with core

Select Actors, Components, Controllers, gameplay state owners and Subsystems by
responsibility and lifetime. Account for multiple worlds, local players and
session transitions. State and dependency ownership must remain explicit without
requiring a DI container, custom constructor injection or a factory for each
engine-created object.

Adapt the common DI/entry wording so Unreal objects are not automatically mapped
to HTTP controllers or backend service layers. Engine lifecycle and composition
are legitimate mechanisms. Pure algorithms can remain ordinary C++; reflected
structs, configuration and Data Assets may remain data. Preserve domain/gameplay
invariants and task-specific dependency boundaries.

Explain reflected versus ordinary interfaces and Blueprint-aware dispatch. Prefer
the simplest existing owner; add abstractions for concrete contracts or variation.
Source-size guidance applies to handwritten code; do not invent Blueprint node
quotas or split generated files to satisfy it.

### UE5. Blueprints, assets and build contracts

Choose C++/Blueprint boundaries by iteration, designer needs, engine access and
measured cost. Keep appropriate designer configuration and behavior in Blueprints;
do not mandate a whole-project translation. Prefer events/timers when they express
the behavior, retaining Tick when frame updates are required.

Use UBT/UHT with the actual target/configuration/platform. Distinguish public/private
module dependencies and editor/runtime boundaries. Respect IWYU and generated
artifacts without changing build flags or clearing caches as a routine check.
Select Live Coding, normal build and restart by affected contracts and actual
host/version capability; preserve dirty work before restart.

Treat `.uasset`/`.umap` as binary editor-owned artifacts. Use supported editing
tools; preserve asset dependencies and applicable source-control contracts.
Asset redirects and reflected Core Redirects have distinct migration roles.
Renames must account for serialized references; scoped changes do not authorize
bulk resaves, unrelated checkout/check-in or removal of compatibility redirects.

Make hard/soft references, load completion, retention and cook inclusion deliberate.
Asset Manager and chunking are conditional tools, not required architecture.
Distinguish build, cook, package and launch evidence; editor visibility alone does
not establish target-build availability.

### UE6. Conditional runtime guidance

For asynchronous work, identify data ownership, thread affinity, completion and
cancellation/lifetime. Lifetime pinning or thread-safe reference counting does not
make arbitrary object access thread safe. Avoid blocking work that depends on the
blocked game thread; mutate editor/world state on its required execution context.

Load networking guidance for an affected networking contract or established
multiplayer requirement. Preserve authority, ownership and server validation;
choose replication and RPC reliability for the actual state/event. Test relevant
client/server behavior, including late join only when it is affected or required.

Performance work needs representative conditions and a measured bottleneck.
Prefer bounded numeric captures for performance claims; screenshots serve visual
questions. Do not impose general bans on casts, Tick, allocations or Blueprint.
GAS/Lyra are conditional references, not default architecture for every feature.

### UE7. MCP context, mutations and recovery

The mandatory procedure must be usable directly from the rule file:

1. Identify the selected project, provider/version, editor instance and relevant
   world/PIE state. Reuse established context until an event invalidates it.
2. Discover only needed toolsets/schemas and resolve actual identifiers. Distinguish
   package, object, class and filesystem paths by the tool's contract.
3. Establish affected objects/packages and baseline, including dirty user work.
   A disk copy does not preserve unsaved editor changes; obtain a supported
   recoverable state or resolve that limitation before dependent mutations.
4. Execute within task authorization. Native MCP calls must not overlap; a shared
   editor has one mutation owner even if source-only tasks are delegated elsewhere.
   Do not parallelize calls merely because a general tool workflow permits it.
5. Interpret errors and actual completion. If a mutation times out with an unknown
   outcome, inspect its effect before retrying. Polling completion does not mean
   starting the operation again. Reacquire invalid handles after reload/restart.
6. Save deliberately within the affected scope and verify the intended result.
   Preserve intervening user changes. Report partial and unsaved state; do not
   claim that undo guarantees reversal of file writes or external effects.

Native setup guidance must reflect experimental status and documented local
connection behavior. Local editor use is the default policy; runtime hosting is
not claimed to be technically impossible. Preserve other client settings and
required project plugins. Scope installation, restarts and new connections to the
task; a tool-editing request is not permission to rewrite personal configuration.

Other providers require verified identity, capabilities and execution contracts.
Do not apply native tool names or transport assumptions to them. Avoid broad
schema/property dumps, blind UI automation and mandatory repeated screenshots.

### UE8. Skills and tool extension boundary

All essential instructions must be available in the selected bundle. Refer to a
compatible installed `unreal-engine-mcp` skill conditionally, applying the framework's
work mode and evidence policy. Do not copy its installation-specific paths,
environment changes, source-control flags or camera/schema workarounds as defaults.
Do not claim that every client requires a session restart to discover tools.

When an actual operation is missing, first inspect existing tools and supported
editor APIs. A custom tool must solve a present repeated/complex operation and
have a bounded input, output and mutation/completion contract. Python versus C++
depends on exposed APIs and requirements; use the selected engine's authoring
documentation. Documentation of a vendor skill does not prove its local presence.

A new framework skill, provider implementation or plugin remains a separate
scoped addition. No automatic installation, cache patching or external-model call
is required by this profile.

### UE9. Proportionate tests and evidence reuse

The Unreal verification section specializes shared
[verification policy](../../standards/verification.md), retaining its authority:

- Select evidence for the changed contract: relevant compilation, affected
  Blueprint/asset validation, focused existing/regression test, PIE/functional
  scenario, or target cook/package/run where needed. These are alternatives or
  complementary checks for distinct risks, not a universal checklist.
- Preserve mandatory project gates. Add tests for meaningful uncovered behavior;
  do not test trivial accessors, engine internals or the same contract at several
  levels without a distinct failure mode. Do not introduce a runner for a docs edit.
- Distinguish source/asset state, in-memory editor state and persisted state.
  A successful build or MCP response does not prove gameplay or packaging behavior.
- Reuse evidence for unchanged relevant inputs. Before repeating a build, test,
  search, scene inspection or screenshot, name the changed input, unreliable result,
  unresolved failure or required fresh gate. Reporting and context handoff alone
  are not invalidation events.
- After a fix or restart, rerun affected checks and retain unrelated evidence.
  No final full suite, rebuild or extra reviewer is mandatory merely because a
  stage is ending. Report unavailable checks without inventing success.

### UE10. Library integration and acceptance boundary

The implementation must reconcile `standards/core.md`, catalog metadata and guide,
root/project/policy entry templates, and the project architecture passport where
their current wording or routes affect Unreal. Keep common rules concise and link
to the profile. Passport fields and flow examples must accept gameplay/editor
projects without forcing backend layers or irrelevant ORM/HTTP fields.

README must identify the supported instruction scope and conditional MCP/skill
behavior. Reconcile architecture or migration descriptions only where this profile
changes their stated contract; do not implement the deferred import mechanism.
An import must preserve reachable resources and project exceptions under existing
migration policy, without requiring personal absolute paths.

Check affected formats, catalog uniqueness/dependencies/resource existence and
relative links. Review the changed instructions against the scenarios below.
Use disposable checks when helpful; no permanent engine test project is required
for library acceptance. Record runtime verification separately if later authorized.

## Acceptance scenarios

| ID | Scenario and required result | Requirements |
| --- | --- | --- |
| A1 | A new Blueprint-only project selects Unreal and relevant gameplay/assets rules without mandatory C++, Python or MCP setup. | UE1–UE2, UE5 |
| A2 | An existing source-only project with no MCP proceeds with relevant source work and reports unavailable editor evidence. Its version is preserved. | UE1–UE3, UE9 |
| A3 | An independently opened imported project can reach all required rules without the author's personal skill paths; catalog dependencies do not trigger full reading. | UE2, UE8, UE10 |
| A4 | A generic C++ file outside an Unreal context does not select the profile. Python editor scripting selects only relevant Python guidance. | UE2 |
| A5 | Engine-created objects use appropriate creation/lifecycle and explicit owners without compulsory custom DI constructors or factory wrappers. | UE3–UE4 |
| A6 | A synchronous validated invariant avoids duplicate guards; an invalidatable deferred reference retains a necessary check. Required side effects survive shipping assertion settings. | UE3, UE9 |
| A7 | A Blueprint/native interface change preserves Blueprint implementations and relevant derived behavior without converting the whole feature. | UE4–UE5 |
| A8 | A reflected rename or asset move accounts for serialized references and affected packages without unrequested bulk resaves. | UE5 |
| A9 | A runtime-module change avoids accidental editor dependencies; build/restart and target checks reflect the actual changed contract. | UE1, UE5, UE9 |
| A10 | Native MCP calls are serialized, bound to the intended editor/world and restricted to necessary discovery. Shared-editor mutation has one owner. | UE7 |
| A11 | A timed-out mutation is inspected before retry; a restart invalidates relevant handles; dirty and intervening user changes survive scoped work. | UE7, UE9 |
| A12 | An installed skill's incompatible command/workaround is not treated as authority; absent or different provider capabilities are reported accurately. | UE1, UE7–UE8 |
| A13 | A small local fix reuses valid evidence and runs affected checks plus required gates, without automatic full build/cook/test/visual cycles. | UE9 |
| A14 | Unrelated work does not load networking/GAS/performance procedures. A relevant runtime task establishes thread/authority/performance evidence. | UE6 |
| A15 | Library checks can pass without an editor pilot; reporting explicitly distinguishes documented guidance, static acceptance and observed runtime capability. | UE1, UE9–UE10 |

## Handoff

The user approved this written specification on 2026-09-27. The implementation
plan is prepared under Superpowers writing-plans with the framework's
[workflow adaptations](../../standards/superpowers.md). It owns the next review
checkpoint and coherent profile/content stages; active routes must not point to
missing resources. Specification approval does not claim implementation completion.

Specification preparation changes only this document and its research/integration
navigation. No profile, native skill or target project has been modified. The
pre-stage baseline is `/tmp/af-unreal-spec-nv9008b2/`; scoped checks and the diff
are retained there for the handoff. Engine execution is not needed to review
this design, and the existing research is reused without a new source sweep.
