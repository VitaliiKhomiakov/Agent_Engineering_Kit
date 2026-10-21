# Godot engineering and editor workflow

Apply to a declared or evidenced Godot project and the current task, with the
relevant [core rules](core.md). `project.godot` establishes useful project context;
`.tscn`, `.tres`, `.gd` and `.gdextension` files are supporting hints. Generic C#
or C++ files alone do not select this profile. GDScript is the primary language
here; C# and GDExtension guidance applies only where used.

Godot has engine-managed scenes, object lifetimes, shared resources, imported
assets and live editor state. Apply common responsibility and verification rules
through those contracts, without requiring backend layers or custom DI frameworks.
The profile covers common 2D and 3D work; a genre, renderer, multiplayer system or
MCP provider is not implied by selecting it.

## Context for the task

Reuse the project's actual engine version/build and standard or .NET edition,
project root, languages, target platforms, renderer and existing check commands.
Consult relevant ownership, asset/export and optional tool facts in the project
architecture record. Distinguish observed capabilities from intended choices;
resolve only missing facts needed for this task, without repeating setup.

Identify whether the change affects source, serialized scenes/resources, imported
data, editor execution, runtime behavior, visual output or a target export. Select
the relevant rows below and sufficient evidence, preserving existing user work.

## Read for the task

All resources declared for `godot` in [the catalog](catalog.toml) belong to the
portable bundle. Availability does not require preloading every topic.

| Task condition | Read |
| --- | --- |
| New/changed responsibility, scene boundary, dependency, signal or autoload | [Architecture and composition](godot/architecture.md) |
| GDScript implementation or readability review | [GDScript contracts and style](godot/gdscript.md) |
| Initialization, freeing, shared state, callbacks or deferred completion | [Lifetimes and state](godot/lifecycle-runtime.md#lifetimes-and-state) |
| Processing, physics or concurrent jobs | [Processing and concurrency](godot/lifecycle-runtime.md#processing-and-concurrency) |
| Save/load behavior or an established multiplayer requirement | [Persistence](godot/lifecycle-runtime.md#persistence) or [networking](godot/lifecycle-runtime.md#networking-when-present) |
| Scene serialization, UID, imported assets, VCS or export | [Assets and export](godot/assets-export.md) |
| Input, UI layout, renderer or a performance question | Relevant [UI/performance sections](godot/ui-performance.md) |
| C# or GDExtension | Relevant [interop section](godot/interop.md); no unused language setup |
| Tool selection, editor/MCP discovery, mutation or recovery | [Tooling and MCP](godot/tooling-mcp.md) |
| Selecting checks, reviewing evidence or reporting completion | [Verification](godot/verification.md) |

A source-only task does not require MCP. GDScript is not Python; an add-on/server's
implementation language does not select a Python/Node application profile. Missing
engine/editor access limits dependent checks, not ordinary instruction editing.

## Version and evidence boundary

The reference contract is Godot **4.7**, researched **2026-10-22** using versioned
[official documentation](https://docs.godotengine.org/en/4.7/) and the
[release archive](https://godotengine.org/download/archive/). Preserve the project's
supported version; the baseline neither requires upgrading nor certifies every
Godot 4.x release. Match consequential APIs, syntax, export targets and tool pairs
to the actual project. Godot 3 migration requires separate version-specific work.

This profile supplies instructions, not an installed engine/provider or a verified
game session. Source artifact checks and downstream engine/client results are
different evidence. Optional source research and tool comparisons are recorded in
`docs/research/2026-10-22-godot-engineering-and-mcp.md`; ordinary tasks need not load it.
