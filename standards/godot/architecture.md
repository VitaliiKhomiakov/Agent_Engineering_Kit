# Godot responsibilities and composition

Read for scene/component design, new responsibility placement or changed dependencies.
Use the actual context from the [Godot entry](../godot.md).

## Choose owners before writing

Apply [responsibility placement](../core.md#responsibility-placement-before-implementation)
before implementation. Inspect existing state, collaborators, callers and reasons
to change; reuse an appropriate owner. Separate already independent duties now,
without waiting for file size or repetition. Keep cohesive helpers with their owner.

For example, adding save serialization to a pause menu introduces a responsibility
independent of button presentation. Place serialization with the save-state owner;
the menu initiates the action and presents its result. Conversely, computing a
movement direction and applying its speed can remain together in the movement
owner. Neither case requires one node/class/file per small operation.

Prefer feature-local scenes, scripts and specific assets. Promote shared components
when they have an actual shared responsibility, not just a similar filename. A
separate script organizes code; a folder or `class_name` is not an access-control
boundary. Introduce a reusable scene, add-on or native boundary for a concrete
dependency, lifetime, distribution or reuse need. Do not manufacture public APIs
or backend service/repository layers merely to split files.

This adapts Godot's [scene organization](https://docs.godotengine.org/en/4.7/tutorials/best_practices/scene_organization.html)
and [project organization](https://docs.godotengine.org/en/4.7/tutorials/best_practices/project_organization.html)
to AEK's responsibility-first policy; directory layout alone does not establish cohesion.

## Choose engine representations

| Representation | Appropriate responsibility |
| --- | --- |
| Node / scene | Tree participation, engine callbacks and composed runtime/editor behavior |
| Resource | Serializable, editor-friendly data/configuration with an explicit sharing policy |
| RefCounted | Logic or data that needs reference-counted lifetime without scene-tree services |
| Plain values | Small calculations and state needing no object identity or lifecycle |

Do not add a node solely to look up another node. Choose direct `Object` ownership
only with a deliberate release contract. Engine alternatives are described in
[node alternatives](https://docs.godotengine.org/en/4.7/tutorials/best_practices/node_alternatives.html).
Mutable resource sharing belongs to [runtime state](lifecycle-runtime.md#lifetimes-and-state);
persisted scene ownership belongs to [serialization](assets-export.md#scenes-and-resource-identity).
Do not confuse either with the engineering responsibility owner.

## Dependencies and communication

Give reusable scenes understandable inputs and outputs. Their composing parent or
context supplies external collaborators. Avoid brittle traversal outside the scene
such as chains of `../`, hidden global lookups or dependence on a particular sibling
layout. Use exported/assigned typed references, an explicit `setup(...)` method or
signal connections. Supply each dependency before the callback or operation that
uses it. If a dynamically instantiated scene needs it in `_enter_tree()` or
`_ready()`, assign it after `instantiate()` and before adding the instance to the
active tree. Pre-tree setup must not rely on `@onready` fields. If setup needs ready
nodes, defer the dependent behavior until setup completes; follow
[readiness](lifecycle-runtime.md#lifetimes-and-state).

For scripts instantiated by `PackedScene.instantiate()` or recreated by
`Node.duplicate()`, `_init(...)` must be callable without arguments. The same applies
to custom resources that need to support `duplicate()`. These engine creation paths
do not supply constructor arguments; see
[Object._init](https://docs.godotengine.org/en/4.7/classes/class_object.html#class-object-private-method-init)
and [Resource.duplicate](https://docs.godotengine.org/en/4.7/classes/class_resource.html#class-resource-method-duplicate).
Required constructor arguments remain valid for objects created directly with
`new(...)` when all their actual creation paths supply them.

Use direct calls for commands to a known collaborator and signals for meaningful
events. Directional advice such as calling children and signaling parents is a
heuristic, not a ban on injected references or a reason for forwarding the same
signal through many intermediaries. Keep the producer, consumer and state owner
traceable. Scene-unique names are scoped to their scene ownership; they do not
provide global dependency resolution.

Use autoloads for a real application-wide or cross-scene lifetime. Do not turn
every manager into a singleton or use an event bus to conceal all dependencies.
An event bus can be appropriate for genuinely distant communication when simpler
composition is inadequate; document that consequential choice in the existing
design note, without an extra ceremony. See
[autoloads versus ordinary nodes](https://docs.godotengine.org/en/4.7/tutorials/best_practices/autoloads_versus_regular_nodes.html).

State machines and other patterns address actual transitions or variation. Do not
require a class per state, a global bus, pooling or ECS merely because a tutorial
uses them. Performance-driven changes follow [measurement](ui-performance.md#performance).
Apply these decisions to the changed responsibility; unrelated legacy layout is
not an invitation to reorganize the project.
