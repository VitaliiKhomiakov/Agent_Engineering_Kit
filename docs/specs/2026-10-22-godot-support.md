# Godot engineering profile specification

Date: **2026-10-22**. Status: **proposed; awaiting user review**.
2026-10-23 status note: implemented in the source library by commit `8173afb`
per the [canonical plan](../plans/2026-10-22-godot-support.md); the original
proposal text below is retained unchanged, and paths it shows as future now exist.
Evidence: [dated research and primary sources](../research/2026-10-22-godot-engineering-and-mcp.md).
Execution and progress: [canonical plan](../plans/2026-10-22-godot-support.md).

This document specifies a future AEK profile. It does not activate target-project
instructions, install tools or claim that the proposed engine checks were executed.
Source IDs below refer to the research bibliography. Requirements are proposed AEK
engineering choices unless explicitly described as an engine/tool contract.

## Outcome and decisions

Provide an optional Godot profile that helps agents place responsibilities before
implementation, use engine facilities correctly, preserve scene/resource identity
and present evidence appropriate to changed behavior. The profile must reach
adopted projects through AEK's existing catalog, entry and role routes.

The user selected **GDScript as primary**, with **C# and GDExtension conditional**.
Cover common 2D and 3D development; do not assume a genre, networking, a renderer,
mobile/web distribution, an IDE or an MCP client. Godot 4.7 documentation and the
observed 4.7.2 stable release are the reference baseline (O01). Older Godot 4.x
projects retain their actual supported versions and require relevant API/tool
compatibility assessment. Godot 3 migration and blanket support for every 4.x
release are outside scope. A newer release never authorizes an engine upgrade.

Choose one engine profile with small task-selected topics. A single long document
would force unrelated editor, native and runtime details into ordinary script work.
Separate language/tool profiles would add selection machinery before independent
cross-engine requirements exist. The proposed arrangement matches AEK's current
[library architecture](../../ARCHITECTURE.md) and [catalog contract](../../standards/catalog.md).

Do not add game code, a mandatory game template, a source-library Godot dependency,
an installation script, a provider-specific native agent or a new review cycle.

## Authority, routing and ownership

The existing [core policy](../../standards/core.md),
[verification policy](../../standards/verification.md),
[orchestration](../../standards/orchestration.md) and
[migration procedure](../../MIGRATION.md) retain their authority. Godot topics apply
those policies to engine contracts; they do not redefine permissions, stage
progression, evidence reuse, model selection or independent-review requirements.

Proposed source paths are shown as code because they do not exist yet.

| Future owner | Responsibility and reading trigger |
| --- | --- |
| `standards/godot.md` | Short entry: applicability, actual engine/version/platform context and task-to-topic routes |
| `standards/godot/architecture.md` | Responsibility placement; scene/node/resource boundaries; dependencies, signals and autoloads |
| `standards/godot/gdscript.md` | GDScript typing, naming, layout, warnings and the single detailed GDScript readability rule |
| `standards/godot/lifecycle-runtime.md` | Tree/object lifetimes, callbacks, asynchronous work, physics, persistence and conditional networking |
| `standards/godot/assets-export.md` | Scene/resource serialization, UIDs, imports, source assets, VCS and export boundaries |
| `standards/godot/ui-performance.md` | Input, Control layout, target rendering and measured performance; read relevant sections only |
| `standards/godot/interop.md` | Conditional C# and GDExtension contracts, toolchains, lifetimes and target limitations |
| `standards/godot/tooling-mcp.md` | Optional tool selection, editor/MCP capability checks, mutation and recovery procedure |
| `standards/godot/verification.md` | Engine-specific check selection and evidence scope; route to shared acceptance policy |

Add catalog profile `godot`, depending on `core`, with the entry and these eight
topics as resources. Availability is not a recursive reading queue. Use an explicit
Godot declaration or established project evidence such as `project.godot` to select
the profile; scene/script/extension files can corroborate the selection. A generic
`.cs` or `.cpp` file alone does not establish a Godot project. This is adoption
guidance, not a requirement to invent a new automatic detection system.

Entry templates route conditionally to `standards/godot.md`. Shared implementer
and reviewer bodies already require applicable profiles and readability acceptance;
native adapters must continue loading those bodies. Add no copied Godot checklist
to each adapter. Research and plans remain optional historical artifacts outside
the bundle closure. Vendor comparisons and changing release numbers stay in dated
research; adopted policy links directly to relevant official contracts.

## Project context before implementation

Record or reuse the actual engine minor/patch, standard or .NET edition, project
root, selected languages, target platforms and renderer. Add only relevant details:
autoloads and ownership, asset pipeline, extension ABI/architectures, test runner,
export presets and enabled editor/MCP add-ons. Reuse the project architecture record
instead of producing a second setup questionnaire for every edit.

Read current scripts/scenes/resources and identify the affected responsibility and
existing owner before writing. Inspect local unsaved editor state when the task
touches the same files. Establish whether the change affects source only, imported
resources, editor execution, runtime behavior, visual output or exported builds;
that distinction selects evidence and prevents irrelevant tool setup.

## Engineering practices

### Responsibility placement and engine composition

Apply [responsibility placement before implementation](../../standards/core.md#responsibility-placement-before-implementation)
from the first change. For example, save serialization and menu presentation are
already distinct responsibilities even in a small feature. Place them with their
appropriate owners immediately. A cohesive movement script may retain closely
related calculations; do not invent a helper node or class for every few lines.

Colocate a feature's scenes, scripts and specific resources where that makes
ownership clear. Shared assets/components need actual shared use or responsibility.
A separate script improves organization; a folder or `class_name` is not an access
control boundary. Introduce a reusable scene, add-on or native boundary only for
an actual dependency, lifecycle, distribution or reuse requirement. Do not impose
backend service/repository/DTO layers on engine-managed entities (O02–O05).

Choose the representation deliberately: nodes participate in engine/tree behavior;
resources represent editor-friendly serializable data; `RefCounted` suits logic
that does not need tree services. Avoid a node merely to obtain access to another
node. Keep configuration and per-instance mutable state separate when their sharing
requirements differ (O05–O07).

Scenes should have understandable external contracts. A composing parent/context
provides required collaborators. Prefer explicit references and meaningful signals
to fragile traversal outside a scene or lookups hidden inside every child.
Clarified after the 2026-10-22 final review: dependency setup must respect engine
creation and callback order, with the detailed contract in the
[architecture owner](../../standards/godot/architecture.md#dependencies-and-communication).
Distinguish explicit setup from required `_init` arguments on engine-created or
duplicated objects; do not ban required constructors for directly created objects.
Signals express events; direct calls suit known commands. The community direction heuristic
is useful, but does not prohibit injected references or justify chains of signal
forwarding. Scene-unique names are scoped, not globally resolvable dependency names
(O02, O08, C02, C04).

Use autoloads for a real application-wide lifetime or cross-scene responsibility,
not as a default service locator. State machines, event buses, pooling and ECS are
conditional tools for actual problems; their mere availability is not a reason
to introduce them. Keep a global event channel narrow enough that producers,
consumers and state owners remain traceable (O04, C01, C03).

### GDScript contracts and readability

Adopt the versioned official GDScript guide as the mechanical baseline: tabs,
UTF-8/LF, conventional snake_case functions/variables and file paths, PascalCase
types/nodes and uppercase constants. Preserve declared project conventions where
adoption deliberately adapts the baseline. The future GDScript topic owns the
selected layout details and examples; entry/verification files link to it (O03, O09).

AEK should require useful types at application boundaries: function parameters and
returns, exported/configuration properties, signals and collections whose element
types are known. Use clear local inference; avoid inference that accidentally
turns a known contract into `Variant`. Dynamic data remains valid at a genuine
boundary, followed by validation/narrowing before ordinary typed code. Use syntax
supported by the project's engine version. This is AEK's stronger convention,
not a claim that optional typing is forbidden by GDScript (O10).

Inspect engine warnings for changed code and resolve relevant issues. Configure
warnings according to project compatibility; do not switch every warning to fatal
or suppress a category repository-wide merely to clear one change. A necessary
local suppression identifies the concrete false positive or intentional boundary
(O11). Do not treat GDScript as Python for formatting, imports or dependency policy.

Separate meaningful phases within a function with blank lines, while retaining
cohesive statements together. An operation and its immediate result/error guard
normally form one group. A small, cohesive calculation needs no manufactured split.
A multi-step function that creates, configures, registers and returns an object
should make those phases visible. Do not require a blank line before every
`if`/return, after every brace/statement, a fixed group length or extraction/comments
merely to create space. This becomes the single authoritative GDScript rule,
supported by small language-native examples, not a duplicate of Go's document.

Apply shared [readability acceptance](../../standards/verification.md#readability-acceptance)
to final changed code after formatting. Formatter/linter success is mechanical
evidence; it does not prove semantic groups or responsibility placement are correct.
Keep the existing compact scope/outcome record rather than adding per-function forms.

### Lifetimes, runtime state and persistence

Account for engine lifecycle order: entry and readiness are different events, and
child readiness precedes its parent's readiness. Initialize dependencies at the
point they are available; do not assume a parent `_ready()` already supplied them.
Handle repeated activation/reparenting according to actual callback contracts, not
the assumption that `_ready()` is rerun on every re-entry (O08).

Distinguish the gameplay responsibility owner, the tree parent controlling lifetime
and `Node.owner` controlling scene serialization. `queue_free()` is deferred; stale
references can outlive an object. Signal connections, timers, awaited operations
and callbacks need an explicit lifetime policy when their producer/consumer can
disappear or the scene can change. Validate a reference or cancel obsolete work at
that boundary; do not wrap every access in defensive checks that hide bad ownership.

`Resource` instances can be shared through loading and scene instantiation. Treat
shared configuration as immutable by convention; place actor health, inventory or
other per-instance state in the correct state owner. When mutation of a resource
is intentional, choose and verify the relevant duplication/scene-local mechanism,
including nested sharing. Do not mechanically deep-copy everything. Emit required
change notifications for custom observable resource state (O06–O07).

Use frame processing for frame-driven work and fixed-step processing for physics
simulation. Respect the units and integration behavior of each motion API; in
particular, do not multiply a velocity by `delta` when an API already applies it.
Do not mix visual interpolation with authoritative simulation accidentally (O12,
O31). Pause behavior, input processing and collision-affecting deferred changes
must be checked where the change depends on them.

Awaiting an event does not make scene operations thread-safe. Keep active scene-tree
mutation on the appropriate thread; worker jobs operate on suitable isolated data
and hand results back through a supported mechanism. Plan shutdown/cancellation
and shared-resource synchronization when actual concurrent work is introduced.
Threading requires a concrete need, not a general responsiveness slogan (O14).

For persistence, use an appropriate writable location such as `user://`, validate
loaded fields and handle missing, malformed and failed I/O outcomes. Specify a data
version/migration and interrupted-write strategy when saved-state compatibility or
durability requires them. These are AEK design requirements, not guarantees supplied
by a tutorial's JSON example. Choose a format for the data; never enable object
deserialization for untrusted input merely for convenience (O26).

Networking guidance is conditional on a networking task: define authority, validate
sender/input at RPC boundaries and test actual transport/platform constraints.
Local play or an MCP-driven session does not prove multiplayer behavior (O27).

### Assets, serialized scenes and export

Preserve source assets, authored text scenes/resources, applicable import settings
and UID sidecars. Keep generated `.godot/` caches out of source control under the
version-appropriate VCS policy. Move existing identities with their assets/scripts;
do not regenerate UIDs or mass-resave unrelated scenes to simplify one edit (O16–O18).

Prefer the editor or a proven structured operation when it preserves serialization
correctly. Bounded text edits are valid when the format/IDs are understood and the
result is loaded/checked. Avoid arbitrary reordering, large float churn or replacing
user-authored scene data with a generated reconstruction. For editor-created nodes,
set serialization ownership when they must persist in the packed scene; saving
and reopening must retain them. Runtime-only children do not all need an owner.

Keep imported model/animation source and intentional scene/resource overrides
distinct. glTF is a suitable interchange default; direct `.blend` import is a valid
choice when the matching Blender dependency is deliberately available, including
in CI. Do not edit a generated import as the durable source of a change (O19).

Use resource-loading APIs for imported engine resources. Raw filesystem reads that
happen to work in an editor checkout need export-aware treatment. Check dynamic
resource inclusion, case-sensitive paths, presets, templates and actual target
requirements. Keep credentials/signing material out of committed configuration;
do not apply old export-preset ignore rules indiscriminately to newer Godot versions
(O16–O17, O22). Optional LFS adoption preserves existing history and text diffs.

Editor tools and MCP add-ons must not accidentally become runtime dependencies or
ship privileged development behavior. Verify the chosen export inclusion/exclusion
mechanism; a directory named `addons` or an `@tool` annotation is not proof of
exclusion. `@tool` and editor plug-ins may execute while loading/importing a project;
treat that execution and its mutations as part of the task's actual tool surface
(O20). Editor undo does not automatically cover external disk operations.

### Input, UI, rendering and performance

Use InputMap actions for player intent. Decide which inputs belong to GUI versus
gameplay; unhandled-event processing can let GUI consume an event first. Polling
input still needs appropriate game/pause/focus gating. Test that clicking a UI
control does not also fire a gameplay action when that is the intended contract
(O13).

Use Control/Container layout and shared themes for UI where appropriate. Do not
continuously overwrite positions owned by a Container. Check the affected resize,
aspect ratio, focus/navigation and input modes; localization/font/text expansion
checks apply when those features or supported locales are involved (O24–O25).

Select renderer and quality assumptions from actual target requirements. Forward+,
Mobile and Compatibility have different capabilities and device costs; neither
all 2D projects nor all 3D projects imply one universal setting. Verify affected
materials, lighting, shaders and UI on the selected renderer/target (O23).

For performance-driven changes, measure the relevant bottleneck before pooling,
caching, native conversion or threading: CPU, GPU, memory, load time and frame-time
stability are different outcomes. Use representative scenes and target hardware.
Avoid allocation or scene-tree churn in a demonstrated hot path, but do not demand
speculative micro-optimization or a synthetic benchmark for every ordinary script
(O15). Clarified after the 2026-10-22 final review: integrating a native library for
required functionality does not need a performance bottleneck; compatibility,
loading and behavior checks still apply. The [performance owner](../../standards/godot/ui-performance.md#performance)
defines the measurement condition, including separate performance claims.

### Conditional C# and GDExtension

For C#, establish the .NET editor, project target framework/SDK and engine-compatible
packages before applying build guidance. Keep C# naming and .NET conventions rather
than imposing GDScript naming. Separate engine-independent logic from tree-bound
behavior when those are existing independent responsibilities; this does not require
a second assembly for every class. Manage native Godot object lifetime separately
from managed garbage collection. Signal subscriptions, especially capturing lambdas
and custom signal cases, need their documented disconnect/lifetime treatment (O28–O29).

Build changed C# and observe the relevant engine behavior; a text write or empty
GDScript diagnostic result is not C# compilation. Under the reviewed 4.7 contract,
Godot 4 C# web export is unavailable and Android/iOS support is experimental. Recheck
the actual project's version/platform before promising delivery. Do not select
GDScript instead of the user's language silently to bypass a target constraint.

Use GDExtension for an actual native integration or measured performance need.
Pin the target engine API, bindings, compiler/platform/architecture, build mode and
precision. Build matching libraries and validate extension loading on the target;
compilation alone is insufficient. Keep `.gdextension` descriptors, exported
libraries and compatibility bounds consistent. Compatibility is directional and
version-dependent, not a universal ABI promise for all Godot 4.x. Native code must
still follow engine object/thread/lifetime contracts (O30).

Do not make Unreal, a generic C++ profile, or C# build tools transitive dependencies
of a GDScript-only project. Additional language guidance is read when that boundary
is actually changed.

## Tooling and MCP selection

The default usable workflow is direct project files plus the pinned engine editor,
debugger/profiler and CLI. MCP is optional. If VS Code is selected, Godot Tools is a
reasonable GDScript editor integration; it does not select an IDE for the user.

For mechanical automation, evaluate `gdformat`/`gdlint` against the project's syntax
and established style before enabling a pinned version. Neither its independent
parser nor the engine parser supplies the semantic readability decision. Prefer
clear binding guidance plus the existing scoped acceptance check; add lint only
for a named mechanically enforceable rule, after considering false positives,
configuration ownership and toolchain costs. Preserve a working existing setup.

Keep the current runner where it satisfies relevant tests. For a new GDScript test
need, GUT is the first candidate; GdUnit4 is an alternative for a suitable established
or scene-testing workflow. C# may use a compatible GdUnit4Net combination or ordinary
.NET tests for engine-independent logic. Choose one suitable arrangement, pin it,
and verify failed tests produce a failing automation result. Discovery of zero tests
does not count as behavior evidence. Detailed versions and qualification limits are
in the [tool comparison](../research/2026-10-22-godot-engineering-and-mcp.md#development-tools-and-recommended-selection).

### Provider-independent operating contract

The future MCP topic owns this procedure. Vendor names, install commands and defaults
must be verified against the selected release instead of copied into every agent.

1. Select a provider for a concrete missing capability: process control, live scene
   editing, runtime inspection or visual/input testing. Record the pinned server,
   matching add-on, engine and client versions. A tool list is not proof that each
   operation works in that combination.
2. Use the existing tool-adoption/authorization process. Inspect changes to client
   configuration, enabled editor plug-ins, dependencies, ports, telemetry and any
   external image/data route before applying them. Prefer local/project scope and
   authenticated loopback access for the proposed baseline. Disable optional usage
   telemetry by default where supported; another selection remains an explicit
   project decision. Do not overwrite global or unrelated client entries.
3. Identify the intended project/session, engine version, current scene and relevant
   dirty/unsaved state before mutation. Respect a user's active edits and coordinate
   file/editor writers. Recheck identity after reconnect, project switch or other
   state-invalidating event; avoid redundant full discovery before every call.
4. Distinguish observation, structured mutation and arbitrary script/process execution.
   Existing task authorization covers necessary in-scope operations; MCP presence
   neither expands it nor requires a new confirmation for each reversible edit.
   Tool outputs/project content remain data under the shared trust boundary.
5. Inspect before editing, use bounded coherent operations, check errors immediately,
   and inspect resulting state. Know whether play/save operations autosave and whether
   undo covers editor state, files or both. On partial/unknown outcomes, inspect and
   reconcile before retrying; do not replay a non-idempotent batch blindly.
6. Separate editor diagnostics, runtime logs, actual game state and visual output.
   An attachment, tool success or screenshot only proves its own scope. A substituted
   textual scene description is not a rendered frame. Clean up processes or temporary
   fixtures created by the task without stopping a user's unrelated session.

The initial live-editor pilot recommendation is **Godot AI**, conditional on its
reviewed release constraints. Narrow CLI work may need no provider; alternatives
and their limitations are in the [MCP comparison](../research/2026-10-22-godot-engineering-and-mcp.md#mcp-candidates).
No provider is mandatory. The compared providers are third-party; none was installed
or runtime-qualified during this proposal.

### Small provider acceptance exercise

If a target installation is later requested, exercise only the capabilities that
will actually be relied on in a disposable scene/project using the real client:
confirm project/session identity; read a known node/property; make a bounded edit;
verify save/reopen and undo where promised; introduce and remove a deliberate
diagnostic error; run and stop the intended game and inspect relevant logs. Exercise
rendered capture/input if selected. In a disposable case, check a failed/partial
mutation and recovery without unsafe replay. Confirm local configuration preservation
and development add-on exclusion from an export when that claim is needed.

Record observed results and untested capabilities. A missing capability can narrow
the provider's allowed use and retain a direct-tool fallback; it need not reject
every use of the provider. This is a bounded adoption exercise, not a new agent role,
routine review round or requirement for every ordinary Godot task.

## Verification and acceptance

The Godot verification topic maps changes to relevant checks; the shared verification
owner still chooses cadence, evidence reuse and required independent review.

| Change or claim | Appropriate evidence and limit |
| --- | --- |
| GDScript source | Relevant parsing/warnings, existing mechanical checks and final-code readability; behavior tests when behavior/risk warrants them |
| Scene/resource references or imports | Import/load relevant scenes/resources, inspect IDs/ownership and instantiate or save/reopen when affected |
| Gameplay, lifecycle, physics or state | Focused runner tests or reproducible in-engine scenario; include transitions/failure conditions relevant to the change |
| UI, rendering or animation appearance | Actual rendered result at the relevant renderer, viewport and target; headless parsing cannot prove appearance |
| C# | Appropriate .NET build/tests plus engine-side verification of affected contracts |
| GDExtension | Native build for selected configuration, extension load and relevant runtime/export check |
| Export/import pipeline or target distribution | Actual selected preset/templates and target smoke check; editor success is not export success |
| MCP operation | Actual resulting project/editor/runtime state; tool return alone is not application acceptance |

Illustrative command shapes from O21, **not executed here**:

```sh
godot --version
godot --headless --path /absolute/project --import
godot --headless --path /absolute/project --script res://scripts/example.gd --check-only
godot --headless --path /absolute/project --scene res://scenes/example.tscn --quit-after 30
```

Use the actual binary name and supported options from its help. Import executes
editor/import work and is not read-only. The script check parses the supplied
script; it is not an all-project build or behavioral test. `--quit-after` counts
iterations, not seconds, and a short run does not establish gameplay correctness.
Use bounded timeouts where appropriate and inspect diagnostics as well as exit
status. Export commands additionally need the actual preset, templates and output
location. Do not invent a universal test-runner CLI without selecting its version.

Implementers apply the relevant topic while writing, inspect final changed code and
affected scene/resource contracts, fix in-scope defects and distinguish tool output
from readability/behavior evidence. Reviewers, when required by existing policy,
apply the binding adopted requirements, identify concrete violations and avoid
inventing preferences. Coordinators verify coverage and unresolved findings before
acceptance. A compact scope/outcome entry can cover related functions; no duplicate
checklist or second whitespace reviewer is needed.

Reuse evidence for unchanged/moved code only while code, context, tools and applicable
criteria remain covered. A clarified newly adopted requirement requires assessing
whether earlier evidence addressed it. Historical clean acceptance is not proof of
an unexamined scene lifetime or style rule. Avoid repository-wide refactoring or
formatting to satisfy a local task.

## Integration and existing-project updates

For new adoption, select `godot` through the catalog, include its closure, and adapt
entry routes and architecture context through the existing migration process.
GDScript does not select Python; a Node/Python-based MCP server does not select an
application stack. C# and native details remain conditional topic sections.

For existing projects, use the accepted adapted baseline **B**, current local state
**C** and new adapted candidate **N** from [repeat integration](../../MIGRATION.md).
Add the selected profile and update relevant routes while preserving local architecture,
style decisions, checks and client configuration. Surface conflicting mandatory
rules for resolution; do not copy source templates over customized `AGENTS.md` or
replace local instructions wholesale. Profile adoption is not tool installation,
an engine upgrade or permission to normalize every existing script.

Check that root/project entries reach the profile, native definitions load shared
roles and selected bundles have no dangling references to omitted optional resources.
Do not add this research/specification/plan to every consuming project's reading path.

## Documented scenario assessment

These are **manual design assessments of the proposed policy**, not automated
regression tests, runtime observations or an independent agent evaluation.

| ID | Scenario | Required decision under the proposal |
| --- | --- | --- |
| S01 | A GDScript-only feature needs a source edit; no MCP is installed | Proceed with suitable direct/engine tools; no MCP, Node, Python or .NET setup is required by profile selection. |
| S02 | A short movement calculation has one state owner and cohesive operations | No extraction or spacing finding solely because it has several lines; evaluate actual cohesion. |
| S03 | A small menu script is about to gain independent save serialization | Identify and place the serialization responsibility separately now; file size does not defer that boundary. |
| S04 | A multi-phase function has no visible phase separation; a guarded operation is otherwise tightly related | A grouping finding is required for the distinct phases; keep the operation and its immediate guard together. A correctly grouped version needs no finding. |
| S05 | Two actors mutate health on one shared configuration resource | Require correction of instance-state ownership/sharing; a clean parse cannot justify the cross-instance mutation. |
| S06 | An editor operation adds a visible node that disappears after saving/reopening | Require a serialization/ownership correction and persistence check; tool success or visibility alone is insufficient. |
| S07 | A reviewed script is moved with its UID, behavior unchanged | Preserve identity; reuse applicable behavioral/readability evidence, but check affected paths/references. Reassess if a newly adopted rule was never covered. |
| S08 | An awaited operation can finish after its consumer scene is replaced | Require a defined cancellation/validity/result-delivery policy and relevant transition evidence; no blanket null-check mandate elsewhere. |
| S09 | A UI click also triggers an unintended gameplay action | Require input propagation/state handling correction and a relevant UI/gameplay scenario. |
| S10 | C# was edited through MCP; its diagnostics report nothing | Require actual C# build evidence; unavailable/unchecked diagnostics cannot be called a successful compiler check. |
| S11 | A native library builds but uses an unverified engine API/target combination | Do not accept extension compatibility until relevant loading/ABI/target evidence exists. |
| S12 | An imported asset loads in the editor but is absent in the export | Require resource inclusion/loading correction and the affected export check; editor evidence covers a different scope. |
| S13 | The test command exits successfully but discovered no intended tests | Do not claim behavior coverage; verify discovery and the runner's failure-exit behavior when establishing automation. |
| S14 | An MCP batch reports partial disk edits and offers retry | Inspect current state and reconcile first; blindly replaying mutations is not an acceptable recovery mechanism. |
| S15 | A prior clean review predates adoption of the clarified readability requirement | Assess coverage explicitly; obtain the missing scoped evidence rather than treating historical acceptance as proof. |
| S16 | A target has custom agent instructions and a working test runner | Preserve/adapt them through B/C/N integration; no wholesale overwrite, second runner or unrelated stack dependency. |

## Completion criteria and limits

The eventual implementation is ready for review when the profile and conditional
routes exist, catalog closure is tested, relevant links/anchors pass, source/adopted
ownership is consistent, and the scenarios above have been assessed against the
actual implemented text. Changes must preserve existing shared policy and optional
profile boundaries. Source artifact checks are distinct from target runtime trials.

Automation can check catalog availability, links, selected syntax/build results,
test outcomes and observable tool operations. Meaningful grouping, responsibility
placement, suitable abstractions and adequate evidence coverage still require agent
judgment. Clear instructions and acceptance evidence improve accountability; they
do not guarantee future model compliance or certify an untested MCP installation.
