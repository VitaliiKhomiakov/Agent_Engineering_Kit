# Unreal C++: contracts, construction and lifetime

Read the relevant section for Unreal C++, reflection, object ownership or guards.
Use the project's actual engine/toolchain; the reference basis is UE 5.8, not a
requirement to upgrade. Shared [core](../core.md) and [verification](../verification.md)
apply; engine-managed composition follows [gameplay ownership](gameplay-blueprints.md#ownership-and-composition).

## Language and reflected contracts

- Follow compatible project conventions and Unreal type prefixes (`U`, `A`, `F`,
  `I`, `E`, `T`) and `b` Boolean naming in new engine-facing code. Preserve existing
  public/serialized names unless migration is part of the task.
- Use the selected engine's supported C++ standard. The researched baseline uses
  C++20; do not introduce newer features without target-toolchain support. Prefer
  explicit types, with Epic's limited `auto` exceptions for lambdas, verbose
  iterators and types that cannot reasonably be spelled out.
- Use UE containers/strings at engine contracts; standard atomics and type traits
  can be appropriate. Keep third-party conversions at their interop boundary;
  neither blanket `std::` prohibition nor wholesale STL replacement is a rule.
- Keep project-owned copyright notices. Epic's source-header policy does not
  make Epic the owner of user code.

Basis: [Epic coding standard](https://dev.epicgames.com/documentation/unreal-engine/epic-cplusplus-coding-standard-for-unreal-engine).

Choose `FName` for identifiers/comparisons, `FString` for string manipulation and
`FText` for localizable display text. Preserve identifier case requirements and
localization intent across conversions; these types are not interchangeable.
[String handling](https://dev.epicgames.com/documentation/unreal-engine/string-handling-in-unreal-engine).

Expose `UCLASS`, `USTRUCT`, `UPROPERTY` and `UFUNCTION` only for a required engine
contract. Preserve the generated-header layout and supported reflected signatures;
edit declarations, not UHT output. Reflection/serialization support does not imply
that every type or field automatically replicates or is visible to Blueprints.
[UHT](https://dev.epicgames.com/documentation/unreal-engine/unreal-header-tool-for-unreal-engine).
Inspect module/target settings before depending on exceptions or RTTI. Use reflected
type mechanisms where appropriate; do not change global flags or disable diagnostics
to accommodate an unrelated C++ recipe.
[Module properties](https://dev.epicgames.com/documentation/unreal-engine/module-properties-in-unreal-engine).

## Construction and lifecycle

- Use `NewObject` for appropriate runtime UObjects and `CreateDefaultSubobject`
  for constructor default subobjects. Do not allocate/delete UObjects with ordinary
  `new`/`delete` or give them custom constructor injection incompatible with engine
  creation. Ordinary C++ helpers and resources can use ordinary construction/RAII.
- Constructors establish defaults and default subobjects, including class default
  objects. Do not assume a playable world, local player or live subsystem there.
  Select later initialization by the dependency's actual availability.

Basis: [Objects](https://dev.epicgames.com/documentation/unreal-engine/objects-in-unreal-engine),
[ordinary smart pointers](https://dev.epicgames.com/documentation/unreal-engine/smart-pointers-in-unreal-engine).

- Spawn Actors through the appropriate world spawning API; complete deferred
  spawning when used. Respect load, duplication and spawn paths rather than
  assuming every instance follows a single creation path.
- Choose construction, registration/component initialization, `BeginPlay` and
  teardown hooks for their real responsibilities. Preserve required `Super` calls
  and ordering; do not put all setup in `BeginPlay` by convention.
- End gameplay participation, owned subscriptions and timers at the relevant
  boundary. `EndPlay` also covers PIE end, travel and streaming, so cleanup solely
  in a destructor or an explicit-destruction handler can be too late or incomplete.
  Memory existence is not proof of active gameplay participation; streaming can
  end and later restore participation without allocating a fresh object.

Basis: [Actor lifecycle](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-actor-lifecycle).

## References and ownership

| Need | Reference choice and constraint |
| --- | --- |
| Persistent reflected UObject reference | `UPROPERTY` with `TObjectPtr<T>`; the containing reference chain must remain reachable to GC |
| Non-owning cache or deferred target | `TWeakObjectPtr<T>`; resolve and check at use after possible invalidation |
| Asset path for loading on demand | `TSoftObjectPtr<T>` / appropriate soft class reference; a path alone neither loads nor retains an asset |
| Short-lived parameter/local | Raw pointer when lifetime and access are established |
| Deliberate retention from a non-UObject owner | `TStrongObjectPtr<T>` where needed; consider retention cost and cycles |

A bare `TObjectPtr` is not automatically a GC-tracked root. Ordinary shared/unique
pointers cannot own UObjects. Soft references need an explicit loading and retention
strategy. Keeping an object allocated or pinning a weak reference does not establish
thread safety or current gameplay validity. Reuse an established lifetime contract;
do not mechanically replace every raw pointer.
[Object pointers](https://dev.epicgames.com/documentation/unreal-engine/object-pointers-in-unreal-engine).

## Guards and diagnostics

Apply [simple control flow](../core.md#simple-control-flow): each safeguard needs
a current contract or reachable failure. Within an unchanged synchronous contract,
avoid stacking null checks, `IsValid`, `check` and `ensure` for the same fact.
After a callback, load, world transition or destruction opportunity, resolve the
reference and relevant state again. A non-null address alone may be insufficient.

- `check` expresses an invariant; it is normally disabled in shipping. Never put
  an operation required for correct execution only inside its expression.
- `verify` evaluates its expression even when its diagnostic behavior is disabled;
  it is not shipping error handling. Expected failure still needs appropriate handling.
- `ensure` is a nonfatal diagnostic, not recovery. Continue only when the following
  path is valid; do not return an invented success or silently replace invalid state.

Use diagnostics at the owning boundary, not on every layer or Tick. Select checks
for the changed behavior under [Unreal verification](verification.md).
[Assertion behavior](https://dev.epicgames.com/documentation/unreal-engine/asserts-in-unreal-engine).
