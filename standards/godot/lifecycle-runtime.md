# Godot lifecycle and runtime state

Read the sections relevant to changed runtime behavior. Choose structural owners
through [architecture](architecture.md); select evidence through [verification](verification.md).

## Lifetimes and state

Distinguish the responsibility owner, tree parent controlling node lifetime and
serialization ownership described in [assets](assets-export.md#scenes-and-resource-identity).
Initialize dependencies when they are available: entering the tree and becoming
ready are different events, and child readiness precedes parent readiness. Do not
assume a child's `_ready()` can use values supplied later by its parent's `_ready()`.
Repeated activation/reparenting does not imply that `_ready()` runs on every entry.

Free objects through their actual ownership contract. `queue_free()` is deferred;
a reference can remain after its native object is freed. Signal connections,
timers, awaited work and delayed callbacks need a lifetime policy when either end
can disappear or a scene can be replaced. Freeing a connection's target object drops
that connection, but lambdas are not tied to the object that created them
([Object](https://docs.godotengine.org/en/4.7/classes/class_object.html)); C#
exceptions are in [interop](interop.md#c). Bound arguments and `await` on a
long-lived or never-emitting signal also need that policy. Cancel obsolete work, reject stale results
or check validity at that boundary. Do not add blanket validity checks that conceal
a broken ownership invariant. See the [Node contract](https://docs.godotengine.org/en/4.7/classes/class_node.html).

Resources loaded or instantiated through scenes may be shared. Keep shared
configuration immutable by convention; actor health, inventory and similar
per-instance state need the appropriate separate state owner. If a mutable resource
is intentional, verify whether it is shared, duplicated or scene-local, including
nested resources. From 4.5, `duplicate(true)` copies only internal subresources; use
`duplicate_deep()` with an explicit mode when external subresources must also be
copied, and check code migrated from 4.4
([4.5 upgrade notes](https://docs.godotengine.org/en/4.7/tutorials/migrating/upgrading_to_godot_4.5.html)).
Do not mechanically deep-copy all resources or assume changing
a scene-local flag retroactively isolates existing instances. Emit change
notifications when custom observable resource state requires them. See
[resources](https://docs.godotengine.org/en/4.7/tutorials/scripting/resources.html) and
[Resource API](https://docs.godotengine.org/en/4.7/classes/class_resource.html).

## Processing and concurrency

Use frame processing for frame-driven work and fixed-step processing for physics
simulation. Keep authoritative simulation and visual interpolation distinct. Respect
the units/integration behavior of the actual movement API: for example,
`CharacterBody2D.move_and_slide()` uses velocity and handles its time step; do not
multiply that velocity by `delta` again. Check changed pause/input/timer behavior
and use deferred collision/tree changes when the applicable callback contract
requires them. Sources: [processing](https://docs.godotengine.org/en/4.7/tutorials/scripting/idle_and_physics_processing.html),
[CharacterBody2D](https://docs.godotengine.org/en/4.7/classes/class_characterbody2d.html).

Awaiting a signal does not make code run on a worker thread or make scene access
thread-safe. Introduce threads for a concrete need, after considering the affected
[performance](ui-performance.md#performance) evidence. Respect the versioned
[thread-safe API contract](https://docs.godotengine.org/en/4.7/tutorials/performance/thread_safe_apis.html):
active scene-tree mutation belongs on the supported thread; workers should process
suitable isolated data and hand results back through a supported mechanism.
Explicitly handle shared resources, result ownership, cancellation and shutdown.
A deferred call alone does not prove the referenced scene/consumer is still valid.

## Persistence

Use a writable location such as `user://` for runtime saves, not an assumed writable
`res://`. Choose a format for the contract; a tutorial's JSON example does not make
JSON mandatory or supply schema validation. Configuration and game-state formats
can have different requirements.

Validate loaded fields before they affect ordinary typed state. Handle missing,
malformed, unsupported and failed I/O outcomes. When compatibility/durability matters,
define a data version, supported migration path and interrupted-write strategy;
these are application responsibilities. Do not enable object deserialization for
untrusted input. Local policy: do not `load()` or `ResourceLoader`-load `.tres`/`.res`
or scene files from player-modifiable or downloaded locations. Resource files "store
the path of the script they use"
([resources](https://docs.godotengine.org/en/4.7/tutorials/scripting/resources.html)),
so loading one also loads that script; code running on load is discussed in engine
proposals [#4925](https://github.com/godotengine/godot-proposals/issues/4925) and
[#10968](https://github.com/godotengine/godot-proposals/issues/10968), not in the
manual. Use a data-only format validated at the boundary and treat ConfigFile values
as untrusted input. See [saving games](https://docs.godotengine.org/en/4.7/tutorials/io/saving_games.html)
and [FileAccess](https://docs.godotengine.org/en/4.7/classes/class_fileaccess.html).
Resource imports/export inclusion have a different owner: [assets and export](assets-export.md).

## Networking, when present

Read this section for an established networking requirement or changed network
contract. Define authoritative state, validate sender/authority and input at RPC
boundaries, and handle relevant disconnect/reconnect and ordering behavior. Select
transport/platform checks for the actual target; do not infer multiplayer correctness
from a local run or MCP input automation. Use the versioned
[multiplayer contract](https://docs.godotengine.org/en/4.7/tutorials/networking/high_level_multiplayer.html).
An ordinary offline feature does not require networking setup or a network audit.
