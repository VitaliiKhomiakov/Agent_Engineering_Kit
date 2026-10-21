# Godot input, UI and performance

Read only sections affected by the task. Use the project's actual 2D/3D, renderer,
viewport and platform context from the [Godot entry](../godot.md).

## Input and UI

Use InputMap actions for player intent. Decide which actions belong to GUI and
gameplay; unhandled input processing can let GUI consume an event first. Polling
input still needs relevant game/pause/focus gating. Verify that UI interaction does
not trigger an unintended gameplay action. See
[input propagation](https://docs.godotengine.org/en/4.7/tutorials/inputs/inputevent.html).

Use Control/Container layout and shared themes where they own the UI responsibility.
Do not repeatedly overwrite positions controlled by a Container. Check affected
resize/aspect ratios, focus/navigation and supported input modes. Localization,
fonts and expanded text need checks when those features/locales are supported or
changed; do not add an internationalization framework to a local UI edit. Sources:
[containers](https://docs.godotengine.org/en/4.7/tutorials/ui/gui_containers.html),
[internationalization](https://docs.godotengine.org/en/4.7/tutorials/i18n/internationalizing_games.html).

## Renderer and visual evidence

Select renderer and quality assumptions from actual device/platform needs.
Forward+, Mobile and Compatibility have different capabilities and costs; a 2D or
3D label alone does not determine the selection. Preserve a compatible existing
choice unless a change is in scope. Verify affected materials, shaders, lighting,
animation and UI on the chosen renderer/target. Consult
[renderer differences](https://docs.godotengine.org/en/4.7/tutorials/rendering/renderers.html).

Appearance requires an actual rendered observation of the relevant scene/state.
Headless parsing, a scene-tree dump or a textual description is not visual evidence.
Use existing reproducible interactions/screenshots when suitable; do not invent
a full visual regression system for every local edit. Report unavailable target
evidence through [verification](verification.md).

## Performance

When performance is the reason for a change, measure the relevant bottleneck before
introducing pooling, caches, native code, ECS or threads. CPU/GPU time, memory,
loading and frame-time stability are different outcomes. Use representative scenes
and the target hardware/renderer where the claim depends on them. Establish the
comparison's workload and conditions in the existing evidence note, not a second
performance ledger.

A native-library integration for required functionality follows
[GDExtension guidance](interop.md#gdextension) without needing a pre-existing
performance bottleneck. Its compatibility, loading and behavior checks still
apply; a separate claim of improved performance requires measurement.

Reduce allocations or scene-tree churn in a demonstrated hot path; do not demand
speculative optimization or benchmarks for every script. Check that an optimization
preserves the behavior and lifetimes it changes. Follow
[Godot's measurement guidance](https://docs.godotengine.org/en/4.7/tutorials/performance/general_optimization.html)
and [concurrency contracts](lifecycle-runtime.md#processing-and-concurrency) when
introducing worker jobs. A faster editor session or MCP response is not evidence
that the exported game's frame time improved.
