# Unreal Engine engineering and editor workflow

Apply to a declared or evidenced Unreal project/plugin and the current task.
`.uproject`/`.uplugin` files are useful hints; a generic C++, header or Python file
does not establish Unreal context. Use with the relevant [core rules](core.md).

Unreal is an engine/editor environment. Its integration model includes
engine-owned lifecycles and worlds, reflection/serialization, binary assets,
unsaved editor state and target cooking. A change can cross source, content and
live editor state; select rules and evidence for those actual boundaries.
Apply shared engineering principles through this model. Existing backend/frontend
profile layouts, DTO/service patterns and build/test routines are not transferable
defaults merely because part of the project is written in C++ or Python.

## Context and essential rules

- Reuse the project's engine version/build identity, installed/source build, host
  and target platforms, project/plugin type, module owners, required plugins and
  existing checks. Distinguish intended choices in a new project from observed
  capabilities in an existing one. Resolve only facts needed for the current task.
- Respect engine-managed construction, object lifetime and gameplay ownership.
  Actors and Components need not mirror backend layers or custom DI constructors.
  Preserve invariants and explicit dependency ownership using engine-compatible
  composition; plain algorithms and configuration need no speculative abstraction.
- Choose C++ and Blueprints by the feature's contract and iteration needs. Retain
  useful existing boundaries; profile before a performance-driven rewrite.
- Preserve source and unsaved editor changes. Binary assets, loaded objects and
  packages on disk have different mutation/recovery contracts.
- Select sufficient evidence with [Unreal verification](unreal-engine/verification.md).
  Default to a bounded block of related edits followed by one verification cycle,
  not a build, PIE run or screenshot after every tool call. Observe operation
  errors immediately; check earlier when dependent work needs the result.
  Required gates remain binding; repeat checks only for an identified invalidation,
  unreliable result or concrete unanswered risk.

## Read for the task

Read only the relevant rows/sections; stop when applicable rules are known.
All resources declared for `unreal-engine` in [the catalog](catalog.toml) form
the portable bundle; their availability does not require preloading them.

| Task condition | Read |
| --- | --- |
| Unreal C++, reflection, constructors, lifetime, references or guards | [C++ and lifetime](unreal-engine/cpp-lifetime.md) |
| Gameplay owner, component/subsystem, Blueprint/native boundary or interface | [Gameplay and Blueprints](unreal-engine/gameplay-blueprints.md) |
| Module/build/reload, assets/references, migration, cook or package | [Build and assets](unreal-engine/build-assets.md) |
| Editor-provider setup, discovery, mutation, recovery or missing tool | [MCP/editor workflow](unreal-engine/mcp-editor.md) |
| Choosing skills for Unreal, Blender asset work or MCP extension | [Optional skills](unreal-engine/skills.md) |
| Select checks, review evidence or report results | [Verification](unreal-engine/verification.md) |
| Async work, thread access or deferred completion | [Concurrency](unreal-engine/runtime-performance.md#concurrency-and-lifetime) |
| Established multiplayer requirement or affected network contract | [Networking](unreal-engine/runtime-performance.md#networking-and-authority) |
| Performance question or a relevant specialist system | [Performance](unreal-engine/runtime-performance.md#performance-and-conditional-systems) |

A Blueprint-only asset task need not read C++ lifetime rules. A source-only change
does not require MCP setup; report dependent editor checks that remain unavailable.
An engine installation or a new skill is not a prerequisite for editing instructions.
Select Python guidance only for actual Python scripting; that choice does not select
FastAPI or other backend components. Optional installed skills assist execution;
the mandatory editor procedure remains in the portable MCP rule section.

## Version and evidence boundary

The research baseline is Epic's UE 5.8 documentation, checked **2026-09-27**.
Native `ModelContextProtocol` is the documented experimental provider; this does
not prove it is installed in the target. Match consequential APIs, build/reload
behavior and tool schemas to the actual engine/provider. Preserve compatible
existing versions; do not require an upgrade or repeat a general source search
before every task. Older releases and other providers need affected capability
checks, not assumed native compatibility.

This profile supplies instructions, not a provider, detector or verified editor
session. UEFN/Verse, generic non-Unreal C++ and detailed specialist subsystems need
their own applicable guidance. Actual project/client discovery and runtime results
must be established in the target; static library acceptance is a separate claim.
Optional evidence in the framework source:
`docs/research/2026-09-27-unreal-engine-engineering-and-mcp.md`.
