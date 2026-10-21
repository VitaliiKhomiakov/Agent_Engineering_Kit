# Godot engineering practices and MCP research

Date: **2026-10-22**. Research performed on 2026-10-21–22.
Purpose: support the proposed [Godot profile specification](../specs/2026-10-22-godot-support.md)
and its [implementation plan](../plans/2026-10-22-godot-support.md).
This is dated evidence and recommendation rationale, not an active instruction profile.

## Scope and evidence limits

The user selected GDScript as the primary language, with conditional C# and
GDExtension sections. Both 2D and 3D projects are covered; no particular game,
renderer, platform, client, commercial product or downstream installation was selected.

The official archive listed **4.7.2 stable**, released 2026-08-18, and **4.8 beta1**,
released 2026-10-15. Use versioned **4.7** documentation as this research baseline.
That is a reference contract, not authorization to upgrade an existing project or
a claim that every Godot 4.x release supports every described API. [Official archive](https://godotengine.org/download/archive/).

Evidence consists of official documentation, original authors' explanations,
maintainer documentation/release records and explicitly identified issue reports.
Search results and comparison directories were discovery aids, not evidence of a
provider's reliability. No MCP provider, engine, formatter or test runner was
installed or executed. `godot`, `godot4`, `gdformat`, `gdlint` and `dotnet` were not
on this session's PATH. This does not establish their absence elsewhere on the machine.
Provider descriptions below are documentation review, not a source-code security
audit, performance benchmark, compatibility certification or observed client session.

## Official Godot sources

All links below were read during this research. IDs let the specification trace
its proposed requirements without repeating a bibliography in every section.

| ID | Primary source | Relevant contract |
| --- | --- | --- |
| O01 | [Release archive](https://godotengine.org/download/archive/) | Stable versus prerelease baseline |
| O02 | [Scene organization, 4.7](https://docs.godotengine.org/en/4.7/tutorials/best_practices/scene_organization.html) | Scene independence and explicit provision of external dependencies |
| O03 | [Project organization, 4.7](https://docs.godotengine.org/en/4.7/tutorials/best_practices/project_organization.html) | Related assets near scenes, filename conventions, `.gdignore` semantics |
| O04 | [Autoloads versus regular nodes, 4.7](https://docs.godotengine.org/en/4.7/tutorials/best_practices/autoloads_versus_regular_nodes.html) | Costs of global state; legitimate cross-scene lifetime |
| O05 | [Alternatives to nodes, 4.7](https://docs.godotengine.org/en/4.7/tutorials/best_practices/node_alternatives.html) | `Object`, `RefCounted`, `Resource` and node responsibilities |
| O06 | [Resources, 4.7](https://docs.godotengine.org/en/4.7/tutorials/scripting/resources.html) | Shared resources, loading and scene instantiation |
| O07 | [Resource API, 4.7](https://docs.godotengine.org/en/4.7/classes/class_resource.html) | Scene-local resources, duplication and custom change notifications |
| O08 | [Node API, 4.7](https://docs.godotengine.org/en/4.7/classes/class_node.html) | Tree lifecycle, freeing, serialization ownership and scene-unique names |
| O09 | [GDScript style, 4.7](https://docs.godotengine.org/en/4.7/tutorials/scripting/gdscript/gdscript_styleguide.html) | Language conventions, tabs and logical spacing; guide allows contextual judgment |
| O10 | [Static typing, 4.7](https://docs.godotengine.org/en/4.7/tutorials/scripting/gdscript/static_typing.html) | Gradual typing, inference and remaining dynamic boundaries |
| O11 | [Warning system, 4.7](https://docs.godotengine.org/en/4.7/tutorials/scripting/gdscript/warning_system.html) | Project warning configuration and local suppressions |
| O12 | [Idle and physics processing, 4.7](https://docs.godotengine.org/en/4.7/tutorials/scripting/idle_and_physics_processing.html) | Frame-driven versus fixed-step callbacks |
| O13 | [Input events, 4.7](https://docs.godotengine.org/en/4.7/tutorials/inputs/inputevent.html) | Input actions and GUI/event propagation |
| O14 | [Thread-safe APIs, 4.7](https://docs.godotengine.org/en/4.7/tutorials/performance/thread_safe_apis.html) | Active scene-tree restrictions and shared-resource hazards |
| O15 | [General optimization, 4.7](https://docs.godotengine.org/en/4.7/tutorials/performance/general_optimization.html) | Measurement, bottlenecks and target-device evidence |
| O16 | [Import process, 4.7](https://docs.godotengine.org/en/4.7/tutorials/assets_pipeline/import_process.html) | Source assets, generated imports and resource loading in exports |
| O17 | [Version control, 4.7](https://docs.godotengine.org/en/4.7/tutorials/best_practices/version_control_systems.html) | Generated caches, export metadata, line endings and optional LFS |
| O18 | [UID changes for 4.4](https://godotengine.org/article/uid-changes-coming-to-godot-4-4/) and [ResourceUID, 4.7](https://docs.godotengine.org/en/4.7/classes/class_resourceuid.html) | Historical introduction of sidecars; current resource identity contract |
| O19 | [3D formats, 4.7](https://docs.godotengine.org/en/4.7/tutorials/assets_pipeline/importing_3d_scenes/available_formats.html) | glTF recommendation and Blender dependency for direct `.blend` import |
| O20 | [Editor scripts, 4.7](https://docs.godotengine.org/en/4.7/tutorials/plugins/running_code_in_the_editor.html) | `@tool` executes in the editor; mutations need deliberate handling |
| O21 | [Command line, 4.7](https://docs.godotengine.org/en/4.7/tutorials/editor/command_line_tutorial.html) | Import, script parsing, running and export have different scopes |
| O22 | [Exporting, 4.7](https://docs.godotengine.org/en/4.7/tutorials/export/exporting_projects.html) | Templates, presets and platform requirements |
| O23 | [Renderers, 4.7](https://docs.godotengine.org/en/4.7/tutorials/rendering/renderers.html) | Forward+, Mobile and Compatibility tradeoffs |
| O24 | [Containers, 4.7](https://docs.godotengine.org/en/4.7/tutorials/ui/gui_containers.html) | Container-owned child layout |
| O25 | [Internationalization, 4.7](https://docs.godotengine.org/en/4.7/tutorials/i18n/internationalizing_games.html) | Translation, locale and resource adaptation |
| O26 | [Saving games, 4.7](https://docs.godotengine.org/en/4.7/tutorials/io/saving_games.html) and [FileAccess](https://docs.godotengine.org/en/4.7/classes/class_fileaccess.html) | Persistence APIs, I/O errors and unsafe object deserialization |
| O27 | [High-level multiplayer, 4.7](https://docs.godotengine.org/en/4.7/tutorials/networking/high_level_multiplayer.html) | Authority, RPC and platform-dependent transport |
| O28 | [C# basics, 4.7](https://docs.godotengine.org/en/4.7/tutorials/scripting/c_sharp/c_sharp_basics.html) | .NET editor/SDK and export restrictions |
| O29 | [C# signals, 4.7](https://docs.godotengine.org/en/4.7/tutorials/scripting/c_sharp/c_sharp_signals.html) | Generated events, rebuilding and disconnection exceptions |
| O30 | [godot-cpp, 4.7](https://docs.godotengine.org/en/4.7/tutorials/scripting/cpp/about_godot_cpp.html) and [extension descriptor](https://docs.godotengine.org/en/4.7/engine_details/engine_api/gdextension/gdextension_file.html) | Native bindings, compatibility and platform libraries |
| O31 | [CharacterBody2D, 4.7](https://docs.godotengine.org/en/4.7/classes/class_characterbody2d.html) | Velocity/movement contract; avoid applying `delta` twice |
| O32 | [Scripting languages, 4.7](https://docs.godotengine.org/en/4.7/getting_started/step_by_step/scripting_languages.html) | Language integration choices; GDScript is not Python |

## Community practices and their adaptation

| Original source | Useful practice | Boundary for AEK |
| --- | --- | --- |
| C01: [GDQuest: design patterns](https://www.gdquest.com/library/design_patterns_intro/), updated 2026-04-04, Godot 4.x | Use engine facilities and choose abstractions for actual problems | Adopt the rationale. Do not wait for file growth before separating responsibilities already known to be independent; do not turn state counts into thresholds for mandatory state classes. |
| C02: [GDQuest: signals](https://www.gdquest.com/tutorial/godot/best-practices/signals/), 2021 | Avoid hard-to-trace signal forwarding; make communication understandable | Architectural advice only. Older `yield`/connection syntax and machine-specific timings are not a Godot 4.7 API or performance baseline. |
| C03: [GDQuest: event bus](https://www.gdquest.com/tutorial/godot/design-patterns/event-bus-singleton/), 2021 | A global event channel can simplify genuinely distant communication | Conditional alternative after simpler ownership/direct connections; no universal bus, hidden command dispatch or global state mandate. |
| C04: [KidsCanCode: node communication](https://kidscancode.org/godot_recipes/4.x/basics/node_communication/index.html), Godot 4 recipes | Avoid fragile traversal outside a scene; parents coordinate children | Directional guidance is a heuristic, not a ban on injected references. Godot's `Node.owner` is serialization metadata, not a general dependency-injection container or business owner. |

These sources reinforce engine-compatible composition. Their examples do not
authorize copying whole architectures or assets. AEK's stronger typing,
responsibility placement and scoped acceptance rules remain explicit local choices.

## Development tools and recommended selection

| Tool | Recommendation | Evidence and practical limit |
| --- | --- | --- |
| Godot editor, debugger, remote scene tree, profiler and CLI | Baseline; use the project's pinned engine | O08, O15, O21. These expose engine behavior; parsing/import alone does not validate gameplay, visuals or an exported target. |
| [Godot Tools for VS Code](https://github.com/godotengine/godot-vscode-plugin/blob/master/README.md) | Recommended when VS Code is the selected editor | Maintained under `godotengine`; GDScript LSP/debugger and headless LSP are documented. C# uses its own debugger/toolchain. No editor migration is required. |
| [gdtoolkit](https://github.com/Scony/godot-gdscript-toolkit/blob/master/README.md?plain=1): `gdformat`, `gdlint` | Optional mechanical-format/lint baseline, after a compatibility trial | [Release page](https://github.com/Scony/godot-gdscript-toolkit/releases) showed 4.5.0 while development `setup.py` showed 4.5.1. Pin an actual published package; do not infer Godot 4.7 grammar coverage from its name. Its parser is independent of the engine. |
| [GUT](https://github.com/bitwes/Gut) | First candidate for a new GDScript-only project that needs a runner | Maintainer matrix maps [9.7.1](https://github.com/bitwes/Gut/releases/tag/v9.7.1) to Godot 4.7.x, 9.6.1 to 4.6.x and 9.5.0 to 4.5.x. Keep a working existing runner. |
| [GdUnit4](https://github.com/godot-gdunit-labs/gdUnit4) | Alternative for scene-oriented testing or an established mixed-language workflow | [6.2.2 release](https://github.com/godot-gdunit-labs/gdUnit4/releases) was observed; development documentation also describes 7.0.0. Its listed 6.2.x matrix includes 4.7/4.7.1 but does not explicitly list 4.7.2: exact-pair validation remains necessary. |
| [GdUnit4Net](https://github.com/godot-gdunit-labs/gdUnit4Net) | Conditional C# testing option; separate compatibility decision | Its API, adapter, analyzers, SDK and Godot versions form a matrix. The observed 4.7.2 row references an RC/development API. Do not present that row as a tested stable combination. Ordinary .NET unit tests suit engine-independent C# logic. |
| Git, optional Godot Git plugin and selected Git LFS patterns | Reuse the project's VCS workflow | O17. LFS is useful for appropriate large binaries, not a reason to put every text scene/resource under LFS or rewrite Git history. |
| Blender and glTF tooling | Conditional 3D authoring pipeline | O19. Prefer portable exported assets when that avoids requiring Blender in CI; direct `.blend` import is valid with an explicitly provisioned pipeline. |

Do not install both GUT and GdUnit4 to cover the same behavior, adopt a provider's
private test API merely because MCP exposes it, or require Python/Node development
profiles just because a tool is implemented in that language. Tool selection must
identify a concrete gap, exact version/platform, configuration owner, useful check,
known limitations and removal/update path. Shared check/adoption ownership stays
in AEK's [verification](../../standards/verification.md) and
[migration procedure](../../MIGRATION.md#prepare-and-apply).

The GUT preference is a recommendation inferred from the user's primary language
and the explicit compatibility matrix for the researched engine baseline. It is not
a performance ranking or a reason to replace an established GdUnit4 workflow.

## MCP candidates

Godot MCP implementations exist. Every candidate below is third-party. No
first-party Godot MCP recommendation was established by the reviewed official
engine/editor material. An Asset Store listing or the word "Native" in a product
name does not establish first-party ownership. The engine's LSP/DAP are separate
protocols and are not themselves MCP servers.

### Primary candidate: Godot AI

[hi-godot/godot-ai v4.3.0](https://github.com/hi-godot/godot-ai/releases/tag/v4.3.0)
was released on 2026-10-03, commit
`b82b5c519b1b17228f70d8effce1626f391bd1dd`. Its
[pinned README](https://github.com/hi-godot/godot-ai/blob/v4.3.0/README.md)
documents Godot 4.7+, an editor add-on and a Python/uv server; MIT licensing;
authenticated local bridges; and a stdio attach command. It also documents
telemetry and opt-out, global client-configuration defaults and configuration
changes across scopes. Installation must preserve local configuration and explicitly
choose the intended scope. The default AEK proposal is local/project scope and
telemetry disabled, when the provider supports that arrangement.

The [pinned tool contract](https://github.com/hi-godot/godot-ai/blob/v4.3.0/docs/TOOLS.md)
distinguishes editor state, sessions, script diagnostics, game liveness and log
buffers. C# writes are explicitly not compiler checks. Running can autosave;
disk operations can return partial outcomes, so batch/undo wording is not proof
of crash-safe rollback. Screenshots may use optional vision routing: assess that
separately before transmitting project images elsewhere.

**Recommendation:** first pilot candidate for substantial live-editor work on
Godot 4.7, because it documents the required authoring and feedback boundaries.
This is a comparative recommendation for evaluation, not a blanket reliability
endorsement or a mandatory AEK dependency. Validate the selected release/client
with the specification's small provider acceptance exercise before relying on it.

### Alternatives and reasons not to standardize them globally

| Provider | Documented shape | Recommendation and unresolved evidence |
| --- | --- | --- |
| [Coding-Solo/godot-mcp](https://github.com/Coding-Solo/godot-mcp) | MIT; Node/npm server; launches engine processes, retrieves output and performs selected scene/resource operations | Candidate for narrow CLI/process workflows or an existing working integration. Do not infer live unsaved-scene or playtest control from launch support. [Issue 142](https://github.com/Coding-Solo/godot-mcp/issues/142) reports process cleanup/timeouts for package 0.1.1; [issue 102](https://github.com/Coding-Solo/godot-mcp/issues/102) reports UID resave false success. These are reports, not locally reproduced defects; check the selected revision and affected paths before a new adoption. |
| [zeegzoog/godot-mcp](https://github.com/zeegzoog/godot-mcp), formerly `zigenzoog` | MIT; Rust binary plus editor bridge, documented token/loopback protection, undo and headless fallback | Secondary experimental candidate when a native server is valuable. [Release page](https://github.com/zeegzoog/godot-mcp/releases) showed v0.4.0 (2026-10-16); branch documentation already describes newer version-specific packaging. Use a released pair's actual contract, not development-branch instructions. Not the default until the exact release's recovery and platform behavior are exercised. |
| [ee0pdt/Godot-MCP](https://github.com/ee0pdt/Godot-MCP) | MIT; Godot add-on plus Node server; scene, script, node and editor commands | Existing-installation/reference option. Reviewed documentation gives less precise current-version, authentication and recovery guarantees; this is an evidence gap, not proof those mechanisms are absent. No first-choice recommendation for a new 4.7 adoption on this evidence. |
| [GDAI MCP](https://gdaimcp.com/) | Commercial editor add-on; vendor advertises Godot 4.2+, scene/script operations, screenshots and input simulation | Consider when the vendor's workflow/support is specifically valuable. Recheck license, price, target compatibility and data handling before procurement. Marketing demonstrations were not executed; no purchase or default paid dependency is proposed. |

The shortlist is intentionally bounded; it is not a ranking of every fork.
Prefer the existing proven provider when it meets the actual need. For source
editing and deterministic CI, direct files plus the engine CLI may require no MCP.
Use one selected provider for a mutation scope; simultaneous providers/editor/file
writers need explicit coordination rather than assumed transactional behavior.

## Consequential disagreements and evidence gaps

- **Typing:** Godot permits gradual typing. The proposal chooses typed application
  contracts as AEK policy, with explicit dynamic boundaries; it does not mislabel
  that choice as a language requirement.
- **Composition:** tutorials sometimes encourage later extraction or categorical
  signal direction. AEK identifies existing independent responsibilities before
  writing, while allowing cohesive scripts and explicit dependencies.
- **Spacing:** official GDScript guidance already separates logical sections.
  A formatter cannot establish whether the sections themselves are appropriate;
  reuse AEK's existing readability acceptance mechanism with a GDScript owner.
- **Version evidence:** release pages, development README files and package registries
  can disagree. Observed versions here are dated, not an instruction to install
  `latest`. A supported-looking range still needs a relevant target smoke check.
- **Automation:** according to the [MCP tools specification](https://modelcontextprotocol.io/specification/2025-11-25/server/tools),
  tools expose schemas and results; error handling and tool annotations must not be
  mistaken for an application-level acceptance guarantee. Capability discovery,
  saved-state checks and project evidence remain necessary.
- **Missing runtime evidence:** this planning stage does not prove engine commands,
  add-on export exclusion, MCP authentication/undo, test-runner failure exits or
  native client loading in a consuming project. The plan distinguishes these
  optional target trials from source-library artifact checks.

## Research outcome

Propose one optional `godot` profile with a short task router and separately owned
engineering topics. Use built-in engine tooling first, an existing test runner
where present, GUT as the initial GDScript runner candidate, and Godot AI as the
first live-editor MCP pilot candidate under its documented constraints. Keep
tool versions and comparisons in dated research; put durable selection and
verification rules in the future profile. Implementation and target installation
remain outside this research/planning stage.
