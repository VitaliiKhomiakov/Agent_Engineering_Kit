# Unreal Engine engineering and MCP: evidence and proposed support

Researched **2026-09-27** at the user's request, using Superpowers brainstorming.
This is research and a support proposal, not an activated technology profile or
evidence of an Unreal Editor pilot. Unreal support precedes the deferred
[project integration specification](../specs/2026-09-27-project-rule-integration.md)
and [integration plan](../plans/2026-09-27-project-rule-integration.md).

The subsequent [Unreal support specification](../specs/2026-09-27-unreal-engine-support.md)
turns the recommendations below into a proposed delivery contract. Its first
release keeps mandatory MCP guidance in portable rules and treats installed
skills as optional; the alternatives below remain research context.

## Intent, evidence and version boundary

AgentsFramework must guide AI work in new and existing Unreal projects: use engine
idioms, operate editor tools correctly, load relevant rules on demand, and select
sufficient verification without speculative guards, excessive tests or repeated
checks. Support must remain importable instructions rather than an Unreal plugin,
installer, application or mandatory automation service.

The reference baseline is Epic's current **UE 5.8 documentation**. Epic announced
5.8 with experimental integrated MCP. This establishes a documented baseline, not
the engine version of a future target project or compatibility with every 5.x
release. [Release announcement](https://www.unrealengine.com/news/unreal-engine-5-8-is-now-available).

Sources below are Epic documentation and API references. Search results for UE4,
old tutorials and community claims were not treated as current compatibility
evidence. A current page can still contain historical examples or omit supported
types; confirm consequential APIs against the selected engine's headers, build
rules and actual tool schemas. No engine upgrade is proposed.

**Evidence** paragraphs describe documented behavior. **Proposal** paragraphs and
tables are framework design recommendations inferred from that evidence and the
user's requirements; they are not additional Epic mandates. No installed engine,
target project, live MCP session, compiler or packaged game was exercised.

At adoption, obtain relevant facts from the project before asking the user:
engine version/build identity, installed versus source build, host and target
platforms, project/plugin type, Blueprint/C++ usage, required plugins, multiplayer
requirements, source-control policy and existing checks. Resolve missing facts
only when the task depends on them. UEFN/Verse needs separate support.

## 1. Unreal C++ is a distinct integration model

### Language and public APIs

**Evidence:** Epic's current standard uses C++20, engine naming prefixes and
explicit types with limited `auto` exceptions. It recommends Unreal containers
and strings at UE interfaces, while accepting selected standard facilities such
as atomics and type traits. Consequently, a blanket ban on `std::` is inaccurate.
Epic's copyright-header requirement concerns Epic-distributed source, not a
license to add Epic ownership notices to user code.
[Coding standard](https://dev.epicgames.com/documentation/unreal-engine/epic-cplusplus-coding-standard-for-unreal-engine).

**Proposal:** preserve the target's supported toolchain and compatible conventions;
use Unreal naming and reflected API conventions for new engine-facing code.
Do not impose generic C++23/26 recipes or reformat unrelated legacy files. Keep
third-party interop conversions at a meaningful boundary.

**Evidence:** Unreal distinguishes identifiers (`FName`), mutable strings
(`FString`) and localizable display text (`FText`). Conversions can lose information
or localization semantics. [String handling](https://dev.epicgames.com/documentation/unreal-engine/string-handling-in-unreal-engine).

**Proposal:** choose by semantic use, not a universal string alias. A display label
and a persisted identifier need not share a type or validation rule.

**Evidence:** module rules expose `bEnableExceptions`, `bUseRTTI`, `CppStandard`
and public/private dependencies. These are build decisions, not independent
choices for each source file. Public dependencies support public headers; private
dependencies support implementation. [Module properties](https://dev.epicgames.com/documentation/unreal-engine/module-properties-in-unreal-engine).

**Proposal:** inspect actual flags before relying on exceptions or RTTI; use the
engine's reflected type mechanisms where applicable. Do not globally enable flags,
disable warnings or add circular dependencies to make an example compile.

### Reflection, creation and lifetime

**Evidence:** UHT processes reflected declarations before C++ compilation.
Reflection is a constrained API surface, not arbitrary C++ with decorative macros.
[Unreal Header Tool](https://dev.epicgames.com/documentation/unreal-engine/unreal-header-tool-for-unreal-engine).
Engine-managed UObjects use `NewObject` and constructor default subobjects use
`CreateDefaultSubobject`; ordinary `new`/`delete` is unsuitable for their lifetime.
Constructors must not assume a running gameplay world.
[Objects](https://dev.epicgames.com/documentation/unreal-engine/objects-in-unreal-engine).

**Proposal:** expose only fields/functions that require engine integration; keep
generated files generated. Preserve header ordering and macro conventions required
by the actual UHT version. Avoid adding reflection to every helper or requiring a
custom factory around every engine creation call.

**Evidence:** Actors have separate load, duplication and spawn paths. Use actor
spawning for Actors; initialization and teardown have lifecycle hooks, including
`BeginPlay` and `EndPlay`. Ending PIE, level transitions and streaming can end play
without the same path as an explicit gameplay destruction request.
[Actor lifecycle](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-actor-lifecycle).

**Proposal:** choose the hook according to when dependencies exist; retain required
`Super` calls. Release subscriptions, timers and gameplay participation at the
appropriate lifecycle boundary. Do not defer all cleanup to C++ destruction, or
place every initialization step in `BeginPlay` irrespective of component needs.

### Ownership and pointers

**Evidence:** for a reflected, reachable owner, `UPROPERTY` plus `TObjectPtr<T>`
provides a tracked UObject reference. A bare `TObjectPtr` is not sufficient by
itself. Use weak references for non-owning caches, soft references for assets
loaded on demand, and short-lived raw pointers when the lifetime is established.
`TStrongObjectPtr` supports keeping UObjects alive from non-UObject owners, with
cost and cycle implications. Soft references do not load or retain objects merely
because a path exists. Pinning protects lifetime; it does not establish arbitrary
thread safety. [Object pointers](https://dev.epicgames.com/documentation/unreal-engine/object-pointers-in-unreal-engine).

**Evidence:** `TUniquePtr`, `TSharedPtr` and `TSharedRef` belong to ordinary C++
ownership and cannot manage UObjects. [Smart pointer library](https://dev.epicgames.com/documentation/unreal-engine/smart-pointers-in-unreal-engine).

**Proposal:** use RAII for ordinary resources and the engine's GC/lifecycle rules
for UObjects. Before adding or removing a validity guard, identify who owns the
reference and whether destruction, unloading or deferred execution can intervene.
Do not replace every raw pointer or wrap every access in repeated null checks.

## 2. Architecture and Blueprint boundaries

**Evidence:** UE supplies Actor/Component, Pawn/Character, Controller, GameMode,
GameState, PlayerState and GameInstance roles. Their purposes and lifetimes differ.
[Gameplay framework](https://dev.epicgames.com/documentation/unreal-engine/gameplay-framework-in-unreal-engine).
Subsystems provide engine-managed extension points with lifecycle hooks.
[Subsystems](https://dev.epicgames.com/documentation/unreal-engine/programming-subsystems-in-unreal-engine).
The API additionally documents `UWorldSubsystem`; the overview's short list is not
exhaustive. [World subsystem](https://dev.epicgames.com/documentation/unreal-engine/API/Runtime/Engine/UWorldSubsystem).

**Proposal:** select the owner by world/player/session lifetime and responsibility.
Prefer components for reusable actor behavior and an appropriate subsystem for
shared services. Do not introduce a global manager for every feature. Account for
multiple PIE worlds and world replacement; avoid retaining a world-owned object
in a longer-lived service without a deliberate reference policy.

**Evidence:** Epic recommends a task-dependent C++/Blueprint mix, often native
systems with Blueprint customization. Native execution can help computational
hotspots, but a conversion should follow profiling. Blueprint Header View produces
declarations, not an automatic translation of function implementations.
[Blueprint versus C++](https://dev.epicgames.com/documentation/unreal-engine/coding-in-unreal-engine-blueprint-vs-cplusplus).
Event-driven Blueprint behavior is a useful default; functions and macros have
different execution and reuse properties.
[Blueprint practices](https://dev.epicgames.com/documentation/unreal-engine/blueprint-best-practices-in-unreal-engine).

**Proposal:** keep designer-facing configuration and appropriate behavior in
Blueprints. Prefer native code for engine access, reusable systems or measured
hot paths. Neither “everything in C++” nor “everything in Blueprint” is a framework
rule. Keep graphs understandable; do not recreate engine facilities in a large
custom graph. Choose events/timers instead of polling when they express the real
behavior; Tick remains valid for work that genuinely needs frame updates.

**Evidence:** reflected interfaces have a `UINTERFACE` declaration and an `I` type;
Blueprint implementations require appropriate exposure and dispatch semantics.
[Interfaces](https://dev.epicgames.com/documentation/unreal-engine/interfaces-in-unreal-engine).

**Proposal:** distinguish ordinary C++ interfaces from reflected contracts; preserve
Blueprint overrides when calling them. Add an interface for actual variation or
decoupling, not automatically for every UObject or component.

### Reconcile the existing core before activating the profile

The current [core](../../standards/core.md) is qualified by task and stack, but its
DI language and the compressed [entry template](../../templates/AGENTS.root.md)
can be interpreted too broadly. The following clarifications belong in the
eventual support change, with narrow references from common rules:

| Existing principle | Unreal interpretation to specify |
| --- | --- |
| Explicit dependencies and DI | Respect engine-managed construction; use appropriate initialization, components, subsystem access or references with explicit lifetime. Do not inject custom constructors into engine-created types. |
| Thin boundaries and domain rules | Preserve gameplay invariants in their actual owner; Actors and Components are not automatically HTTP-controller equivalents. Pure algorithms may remain ordinary C++. |
| Factories and meaningful abstractions | Engine creation APIs are legitimate construction boundaries; no mandatory wrapper, service/repository layer or DI container. |
| Simple data versus rich models | Reflected structs, Data Assets and configuration may remain data; state transitions still enforce gameplay rules. |
| Reuse validation | An unchanged synchronous invariant can be reused; a later callback, load or world transition may require a new lifetime/state check. |
| Size and cohesion | Review handwritten responsibilities; do not split generated code or mechanically map source-line limits onto Blueprint node counts. |

These are proposed clarifications, not permission to discard core invariants,
required checks or existing project contracts.

## 3. Build, assets and migration

**Evidence:** UE modules have their own dependency/build model, separate from
C++20 language modules. Modules can separate runtime and editor functionality.
[Modules](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-modules).
IWYU makes dependencies explicit; its enforcement defaults differ between engine
and game code. [IWYU](https://dev.epicgames.com/documentation/unreal-engine/include-what-you-use-iwyu-for-unreal-engine-programming).

**Proposal:** use UBT/UHT and the selected target/configuration/platform. Keep
editor dependencies out of runtime modules. Add public dependencies only when the
public contract needs them, and prefer direct includes to accidental transitive
ones. Avoid building the entire engine, clearing caches or deleting Intermediate
as routine verification; diagnose the actual build failure first.

**Evidence:** Live Coding patches running binaries and supports object reinstancing;
cached pointers can need invalidation or rebinding. Disabling reinstancing changes
which edits are safe. [Live Coding](https://dev.epicgames.com/documentation/unreal-engine/using-live-coding-to-recompile-unreal-engine-applications-at-runtime).

**Proposal:** record the actual host/version capability. Function-body iteration
and reflected/layout/module changes require different judgment. Choose a normal
build/restart when the changed contract requires it; preserve unsaved work before
restart. A patched editor is not evidence for a cold launch or target package.

**Evidence:** `.uasset` and `.umap` are binary assets; ordinary text merging is not
appropriate. [Asset source control](https://dev.epicgames.com/documentation/unreal-engine/using-perforce-as-source-control-for-unreal-engine).
Asset moves can leave redirectors; fixup may resave referencing packages.
[Asset redirectors](https://dev.epicgames.com/documentation/unreal-engine/asset-redirectors-in-unreal-engine).
Reflected symbol renames can require Core Redirects to retain serialized references.
[Core Redirects](https://dev.epicgames.com/documentation/unreal-engine/core-redirects-in-unreal-engine).

**Proposal:** perform asset edits through supported editor APIs/tools, preserving
dirty state and ownership. Do not text-patch binary assets or silently copy generic
Git merge tactics. Plan affected references before a move/rename. A scoped rename
does not authorize project-wide resaves, automatic checkout/check-in, or removal
of old redirects whose compatibility role is still required.

**Evidence:** Asset Manager distinguishes primary and secondary assets and provides
loading, audit and chunking controls. [Asset management](https://dev.epicgames.com/documentation/unreal-engine/asset-management-in-unreal-engine).
Build, cook, stage, package, deploy and run are distinct operations; UAT can
orchestrate them. [Build operations](https://dev.epicgames.com/documentation/unreal-engine/build-operations-cooking-packaging-deploying-and-running-projects-in-unreal-engine).

**Proposal:** loading and cook inclusion must match the actual reference strategy.
An asset visible in the editor is not automatically verified in the target build.
Use Asset Manager or async loading where the current content contract warrants
them; avoid making every reference soft or every small project a chunking system.

## 4. Concurrency, networking and performance

**Evidence:** UE Tasks supports dependencies and asynchronous work with engine
scheduling. [Tasks System](https://dev.epicgames.com/documentation/unreal-engine/tasks-systems-in-unreal-engine).

**Proposal:** background work should have a defined data owner, completion context
and cancellation/lifetime policy. Return to the required thread for editor/world
mutation. Thread-safe reference counting does not make referenced state thread
safe. Avoid blocking the game thread on work that needs that thread to complete;
do not move arbitrary UObject access into a worker just because an async API exists.

**Evidence:** UE networking distinguishes authority, ownership and network modes;
overusing reliable RPCs can overflow queues. [Networking](https://dev.epicgames.com/documentation/unreal-engine/networking-overview-for-unreal-engine).

**Proposal:** load networking rules for a networking task or an established
multiplayer requirement. Keep authoritative gameplay checks server-side; select
RPC/property replication deliberately and consider late joining and ownership.
Do not add multiplayer to a single-player task speculatively. When multiplayer is
intended, settle that constraint early instead of assuming it can be added cheaply.

**Evidence:** Insights and related profiling tools expose CPU, GPU, memory and
network costs. Profiling itself has overhead.
[Performance profiling](https://dev.epicgames.com/documentation/unreal-engine/introduction-to-performance-profiling-and-configuration-in-unreal-engine).
Trace channels and bookmarks can constrain a capture to the question being asked.
[Trace quick start](https://dev.epicgames.com/documentation/unreal-engine/trace-quick-start-guide-in-unreal-engine).

**Proposal:** identify the bottleneck and representative target conditions before
pooling objects, adding threads, removing casts or converting Blueprints. Use
numeric captures for performance claims and visual evidence for visual behavior.
Avoid universal bans on Tick, casts, Blueprint or allocations; scope optimizations
to measured cost and the task's performance budget.

**Evidence:** Lyra is a modular learning sample with multiplayer and a customized
GAS architecture. [Lyra](https://dev.epicgames.com/documentation/unreal-engine/lyra-sample-game-in-unreal-engine).
Its ability system demonstrates attributes, abilities, effects and explicit
grant/removal ownership. [Abilities in Lyra](https://dev.epicgames.com/documentation/unreal-engine/abilities-in-lyra-in-unreal-engine).

**Proposal:** use Lyra/GAS as conditional references for matching requirements;
do not import their entire architecture into a small interaction feature. Rendering,
Niagara, animation, Mass, World Partition and platform-specific optimization need
task-specific follow-up; this research does not claim detailed coverage of them.

## 5. MCP: documented baseline and proposed operating contract

**Evidence:** UE 5.8's experimental `ModelContextProtocol` plugin serves local
HTTP at `127.0.0.1:8000/mcp` by default, without authentication. Tool calls run
serially on the game thread; clients must not overlap them. Tool-search mode
provides `list_toolsets`, `describe_toolset`, then `call_tool`. Toolsets can be
enabled individually. Client configuration generation needs care with existing
files. The server also has runtime modules; editor-only operation is a policy
choice, not a universal plugin limitation. Python and C++ toolsets are supported;
new C++ `UFUNCTION` tools require an editor restart, while existing body changes
can use Live Coding. Epic references a `create-toolset` skill in its `unreal-mcp`
Claude Code plugin. [Unreal MCP](https://dev.epicgames.com/documentation/unreal-engine/unreal-mcp-in-unreal-editor).

**Evidence:** ToolsetRegistry exposes structured descriptors, registration and
asynchronous result types. Discover the tool's real completion contract instead
of assuming a transport reply means the operation has finished.
[ToolsetRegistry API](https://dev.epicgames.com/documentation/unreal-engine/API/Plugins/ToolsetRegistry).
Python editor scripting is a supported content-automation surface with
project-specific plugin setup. It must not be assumed to provide packaged gameplay
scripting. [Editor Python](https://dev.epicgames.com/documentation/unreal-engine/scripting-the-unreal-editor-using-python).

**Proposed framework workflow:**

1. **Identify context:** selected project and engine, provider/version, endpoint,
   editor instance, relevant world/map and PIE state. Reuse this context until it
   changes. Existing work should not trigger another editor instance automatically.
2. **Discover narrowly:** load only the needed schema, request selected properties
   or assets, and use returned identifiers. Distinguish filesystem, package, object
   and class paths according to the actual tool. Do not preload the entire registry.
3. **Establish the change boundary:** record affected assets and prior dirty state;
   preserve the stage baseline. Existing task authorization covers ordinary scoped
   edits. A batch operation must have a known selection and consequence.
4. **Execute and observe:** use supported tools and the provider's concurrency
   contract. Interpret structured errors and completion state. Following a timeout
   with an uncertain mutation, inspect its effect before retrying to avoid duplicates.
5. **Persist deliberately:** save the affected work and report remaining unsaved
   state. Do not save all packages or use undo as a guarantee that every operation,
   external effect or file write can be reversed. Preserve intervening user edits.
6. **Verify the intended result:** inspect the changed state and use the selected
   behavioral check. Stop when sufficient; another screenshot or full scene scan
   requires a concrete unanswered question.

**Proposed setup scope:** use a local editor connection by default, preserve other
client configuration, and enable only capabilities needed for the task. Connection
setup, installation and project editing are distinct operations with their own
scope. Runtime exposure, remote access and external providers require a separate
design. MCP absence must not block an ordinary source-only C++ change; report the
editor checks that remain unavailable.

### Existing skills and provider alternatives

The locally available `unreal-engine-mcp` skill was read, not executed or modified.
It contains useful operational observations, but its Linux launch environment,
client-registration command, mandatory-session-restart assertion, tool parameter
workarounds and camera behavior are not universal verified contracts. Its recipes
must be checked against the actual client and schemas before use. In particular,
do not inherit `-NoSourceControl` or environment changes as project defaults.

| Candidate | Proposed use | Boundary |
| --- | --- | --- |
| Existing `unreal-engine-mcp` | Reuse compatible local execution knowledge through the framework's rules | Client/tool-specific details need validation; no plugin-cache patching or unconditional copying |
| Epic `create-toolset` | Evaluate when a real missing editor operation needs a custom tool | Mentioned in official docs; package contents and cross-client availability were not inspected here |
| Framework `af-unreal-editor-task` | Optional thin skill for contextual discovery, scoped editor mutation and evidence | Add only if it provides a useful trigger/handoff beyond the selected native skill; reference standards instead of duplicating them |
| Framework custom-toolset skill | Defer unless an actual tool-authoring workflow is needed | A new skill is not necessary for merely using existing tools |
| Third-party Unreal MCP | Conditional adapter for a selected existing provider or older engine | Do not reuse native tool names, transport, concurrency or compatibility claims without examining that provider |

**Recommendation:** begin with the native documented provider and a provider-aware
MCP rule section. Preserve source-only workflows and older-project compatibility
through capability checks. Do not require a new plugin or multiple competing
skills simply to declare Unreal support.

## 6. Guards, tests and sufficient verification

**Evidence:** `check` is normally absent from shipping execution; its expression
must not contain required side effects. `verify` still evaluates its expression
when diagnostics are disabled. `ensure` reports a nonfatal diagnostic and does
not supply recovery by itself. [Assertions](https://dev.epicgames.com/documentation/unreal-engine/asserts-in-unreal-engine).

**Proposal:** retain an invariant assertion where appropriate, ordinary handling
for reachable failure, and a lifetime check after a boundary that can invalidate
the object. Avoid `IsValid`/null/assert/ensure chains for the same unchanged fact.
Do not silence a defect with a default value or add logging on every Tick. External
data and network input still need the checks their actual contracts require.

**Evidence:** Automation Framework covers engine-dependent tests; Low-Level Tests
offers module-oriented tests using Catch2. Neither requires testing every accessor.
[Automation Framework](https://dev.epicgames.com/documentation/unreal-engine/automation-test-framework-in-unreal-engine),
[Low-Level Tests](https://dev.epicgames.com/documentation/unreal-engine/lowlevel-tests-in-unreal-engine?lang=en-US).
Data Validation supports selected assets and dependencies; the commandlet's default
validator coverage does not automatically include every Blueprint/Python validator.
[Data Validation](https://dev.epicgames.com/documentation/unreal-engine/data-validation-in-unreal-engine).

The following **proposed defaults** specialize shared
[verification policy](../../standards/verification.md); project gates remain binding.
Rows select evidence by changed contract rather than mandate a sequence of checks.

| Change | Smallest useful evidence | Widen when |
| --- | --- | --- |
| Framework instructions | Changed links, catalog/format, concrete instruction scenarios | An executable example or routing contract changed |
| Ordinary C++ algorithm | Applicable compile and focused existing test or meaningful regression | Engine integration or target behavior also changed |
| Reflected C++ or module boundary | Relevant UHT/UBT target and dependent asset/Blueprint compatibility | Layout/loading/restart or packaged runtime boundary is affected |
| Blueprint graph | Compile affected Blueprint; relevant behavior in PIE or existing functional test | Callers, inherited behavior or asset loading also changed |
| Asset settings or references | Inspect affected assets; applicable scoped validation | Cook inclusion, rename dependencies or target behavior is affected |
| Multiplayer behavior | Relevant authority/client/ownership scenario | Reconnect, late join or network conditions are part of the change |
| Cook/package configuration | Applicable target cook/package and required launch check | More supported targets are materially affected or required by CI |
| Performance fix | Comparable bounded capture of the affected scenario | The bottleneck moves or acceptance covers additional workloads |

Do not add a new runner or permanent test harness for a reversible documentation
change. Preserve existing regression coverage and required CI. Do not duplicate
the same contract in unit, editor, functional and screenshot tests without a
distinct failure mode. A successful compile, tool reply or screenshot does not
prove all gameplay, serialization and deployment behavior.

**Evidence reuse:** retain the checked source/asset state, target, environment and
result in the existing task record. Re-run only when relevant inputs changed,
evidence is unreliable, a concrete failure remains or a required gate demands it.
An editor restart can invalidate object handles and session state without
invalidating an unchanged source check. A final report does not require repeating
builds, full scans or screenshots. Polling an unfinished operation is distinct
from starting it again; observe completion with bounded waits.

## 7. Proposed framework shape and subsequent stages

The preferred shape is a short `standards/unreal-engine.md` entry and conditional
detail files, following existing profile conventions. Proposed paths below do not
exist yet and are not active reading routes.

| Proposed resource | Load when |
| --- | --- |
| `standards/unreal-engine.md` | An Unreal project/task is explicitly selected or evidenced |
| `unreal-engine/cpp-lifetime.md` | C++, reflection, ownership or lifecycle changes |
| `unreal-engine/gameplay-blueprints.md` | Gameplay ownership, Blueprint/native boundaries or interfaces |
| `unreal-engine/build-assets.md` | Modules, compilation, assets, redirects, cook or packaging |
| `unreal-engine/mcp-editor.md` | Editor operations, connection setup or MCP tool authoring |
| `unreal-engine/verification.md` | Selecting UE-specific checks or reporting their evidence |
| `unreal-engine/runtime-performance.md` | Concurrency, replication or performance work; only relevant sections |

Do not load C++ details for a simple asset task or MCP setup for a source-only edit.
Research remains optional background, outside the normal instruction bundle.
Use one new Unreal profile with core as its common dependency; select Python only
for actual Python scripting. A standalone generic C++ profile can be separate work.
File globs alone cannot prove all stack relationships or inspect binary assets;
explicit project technology and task selection remain valid routes.

Suggested next implementation stages, subject to a reviewed support specification:

1. **Contract and routing:** settle version/capability boundaries, profile resources
   and narrow core/entry clarifications. Check representative new/existing and
   source-only/Blueprint/MCP tasks without activating unrelated profiles.
2. **Engineering content:** add C++ lifetime, gameplay, modules/assets and conditional
   runtime guidance. Use concise examples only for real ambiguities; preserve
   proportional guards, tests and evidence reuse.
3. **MCP and optional skill:** define the provider-aware workflow and integration
   with existing skills. Author a thin skill only if its distinct purpose is agreed.
4. **Library acceptance:** check catalog/resources/links and instruction scenarios;
   document actual support and limitations. A separately scoped target pilot may
   then validate real discovery, editor operations and selected behavior.

Before implementation, settle whether the first deliverable includes a new editor
skill or references the available skill, and whether any specific older engine or
third-party provider needs verified support. Exact project and platform choices
are prerequisites for a pilot, not for saving this research.

Acceptance scenarios for the support specification should include: Blueprint-only
asset edit without C++/MCP setup; engine-owned object construction without a DI
wrapper; necessary validity checks after deferred work; shipping assertion
semantics; source-only work without MCP; serial native editor calls; unknown
mutation outcome before retry; dirty user assets preserved; reflected rename
compatibility; focused verification with evidence reuse; and optional networking
remaining unloaded in unrelated work.

The deferred project-rule integration remains a later task. Its completion cannot
be inferred from this research or from adding the Unreal profile. This research
does not promise measured AI reliability, runtime compatibility, installed skills
or verified target builds.
