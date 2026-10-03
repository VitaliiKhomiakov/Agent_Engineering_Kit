# Unreal gameplay ownership and Blueprints

Read for gameplay structure, engine-managed composition, Blueprint/C++ boundaries
or interfaces. Apply the project's selected engine and gameplay requirements;
use [C++ lifetime](cpp-lifetime.md) only when that concern is affected.

## Ownership and composition

Choose the existing owner by responsibility, lifetime and required engine behavior:

| Responsibility | Candidate owner |
| --- | --- |
| World object and reusable attached behavior | Actor and appropriate Components |
| Possessable entity and its control | Pawn/Character and Controller |
| Game rules and shared game/player state | GameMode, GameState and PlayerState according to their network/lifetime contracts |
| State spanning world changes within a game instance | GameInstance or suitable GameInstance subsystem |
| Shared service scoped to engine, editor, world or local player | Subsystem with the matching supported lifetime |

These are roles to select, not a required class list. Distinguish ownership from
access: retaining a world-owned object in a longer-lived owner requires deliberate
lifetime management. Resolve the intended world/player; a global reference must
not silently select another PIE instance. Do not move all state into GameInstance.
[Gameplay framework](https://dev.epicgames.com/documentation/unreal-engine/gameplay-framework-in-unreal-engine),
[Subsystems](https://dev.epicgames.com/documentation/unreal-engine/programming-subsystems-in-unreal-engine),
[World subsystem API](https://dev.epicgames.com/documentation/unreal-engine/API/Runtime/Engine/UWorldSubsystem).

Apply the [core design principles](../core.md#practical-solid-dry-kiss-and-yagni)
through engine-compatible composition. Components, suitable subsystem access,
configured references and lifecycle initialization can express dependencies;
engine-created types do not require custom DI constructors or a DI container.
Keep responsibility and lifetime explicit. Add factories or interfaces only for
actual creation rules, variation or a meaningful boundary.

An Actor or Component can own gameplay rules; it is not automatically equivalent
to an HTTP controller. Enforce invariants where state changes, with ordinary C++
helpers for pure algorithms when useful. Reflected structs, Data Assets and
configuration may remain data. Do not create backend-style layers or pass-through
adapters solely to mirror a generic architecture diagram.

## Native and Blueprint boundaries

- Select the mix from the current feature: C++ suits reusable systems, lower-level
  engine access and measured computational hotspots; Blueprint suits appropriate
  designer behavior, composition and iteration. Keep useful existing boundaries.
- Expose the narrow native API and configuration that designers need. Preserve
  editable defaults, subclass behavior and serialized references during changes.
  A declaration generated from a Blueprint is not a complete behavior translation.
- Profile a real performance problem before converting a Blueprint to C++. Neither
  language is mandatory for every feature, and conversion is not a routine cleanup.

Basis: [Blueprint versus C++](https://dev.epicgames.com/documentation/unreal-engine/coding-in-unreal-engine-blueprint-vs-cplusplus).

Keep graphs cohesive with meaningful functions and local state. Choose macros
only where their expansion/latent behavior fits. Use events, delegates or timers
when work is driven by a change or interval; retain Tick when frame updates are
actually required. Avoid polling for an existing event or duplicating subscriptions
across repeated initialization. Blueprint node counts are not source-line limits.
[Blueprint practices](https://dev.epicgames.com/documentation/unreal-engine/blueprint-best-practices-in-unreal-engine).

## Interfaces and dispatch

Use an ordinary C++ interface for an ordinary native contract. Use `UINTERFACE`
and the corresponding `I` interface when reflection/Blueprint participation is
required, with suitable event/exposure specifiers.

For Blueprint-capable interface events, call the generated static `Execute_`
wrapper on the implementing UObject. Calling `_Implementation` directly bypasses
Blueprint overrides; `Cast<I...>` cannot establish support for an implementation
added only in Blueprint. At a boundary where support is unknown, establish object
validity and interface support using reflected checks before dispatch. Do not
repeat those checks where the same unchanged contract already guarantees them.
[Unreal interfaces](https://dev.epicgames.com/documentation/unreal-engine/interfaces-in-unreal-engine).

Choose evidence for the affected caller and native/Blueprint implementation under
[Unreal verification](verification.md). Compile relevant derived Blueprints when
their exposed contract changes; use a behavioral scenario when dispatch or gameplay
changes. Do not rewrite or test unrelated graphs to complete a local change.
