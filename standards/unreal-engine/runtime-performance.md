# Unreal concurrency, networking and performance

Read only the section whose contract changes. These concerns do not require each
other; a local gameplay edit does not automatically add multiplayer or profiling.
Use the actual project's engine, target and [verification policy](verification.md).

## Concurrency and lifetime

- Give background work an owner, immutable snapshot or synchronized data contract,
  completion context and cancellation policy. Use existing engine scheduling where
  suitable; a new thread/pool is not required for every asynchronous operation.
- Express prerequisites instead of blocking workers unnecessarily. Never wait on
  the game thread for work that needs that same thread to complete.
- Return to the required thread for world/editor mutations. Verify the API's thread
  contract; an async wrapper does not make arbitrary engine access thread safe.
- At completion, establish that the intended owner/world/request is still relevant
  before applying results. Handle destruction, cancellation or a superseded request
  when reachable. Do not repeat checks for an unchanged state without a reason.

Basis: [Tasks System](https://dev.epicgames.com/documentation/unreal-engine/tasks-systems-in-unreal-engine).

Retaining or pinning a UObject protects allocation lifetime, not arbitrary shared
state or gameplay validity. Thread-safe reference counting protects the count,
not the object. Follow [reference ownership](cpp-lifetime.md#references-and-ownership)
and the accessed API's contract; do not capture a raw `this` into deferred work
without a lifetime guarantee.
[Object pointers](https://dev.epicgames.com/documentation/unreal-engine/object-pointers-in-unreal-engine).

## Networking and authority

Apply when networking is affected or multiplayer is an established requirement:

- Identify server authority, ownership and intended recipients before choosing
  replication or an RPC. Local control and server authority are different facts.
- Keep authoritative state transitions and validation on the server. Validate
  reachable client requests against current rules; do not trust a local UI check
  as authorization or reproduce identical validation at every unchanged layer.
- Use replicated state for a state contract and RPCs for appropriate calls/events.
  Consider late joining or reconnection when the affected behavior depends on them;
  receiving a one-time event does not establish persistent state for later clients.
- Select RPC reliability deliberately. Unbounded reliable calls driven by Tick or
  rapid input can congest queues; do not label every message reliable by default.
- Verify the relevant authority/client/ownership scenario. Standalone success alone
  does not prove a changed multiplayer contract; avoid a full network matrix for
  an unrelated local edit.

Basis: [Networking overview](https://dev.epicgames.com/documentation/unreal-engine/networking-overview-for-unreal-engine).
Settle intended multiplayer constraints early; do not add speculative networking
to a task whose required scope is single-player.

## Performance and conditional systems

- Start with the actual frame, memory, latency or loading budget and a representative
  workload/target. Capture the bottleneck before changing architecture.
- Use comparable build/configuration, scene/workload and capture conditions when
  evaluating a change. Distinguish game, render and GPU costs rather than treating
  every low frame rate as a C++ problem. Account for profiling overhead.
- Prefer bounded numeric captures (for example Insights or an existing project
  metric export) for timing/resource claims. Screenshots answer visual questions;
  they are not a substitute for reliable performance measurements.
- Scope optimization to measured cost. No blanket ban on Tick, casts, allocations
  or Blueprints, and no automatic pooling, threading or native rewrite.

Basis: [Performance profiling](https://dev.epicgames.com/documentation/unreal-engine/introduction-to-performance-profiling-and-configuration-in-unreal-engine),
[bounded trace capture](https://dev.epicgames.com/documentation/unreal-engine/trace-quick-start-guide-in-unreal-engine).

Consult GAS/Lyra when current requirements need their ability, effect, attribute
or modular gameplay mechanisms. They demonstrate particular solutions, not a
mandatory architecture for a small interaction. Preserve grant/removal and state
lifetime ownership when those systems are used.
[Lyra](https://dev.epicgames.com/documentation/unreal-engine/lyra-sample-game-in-unreal-engine),
[abilities](https://dev.epicgames.com/documentation/unreal-engine/abilities-in-lyra-in-unreal-engine).
For rendering, animation, Niagara, Mass or other specialist work, read the relevant
versioned subsystem contract rather than extrapolating this general section.
