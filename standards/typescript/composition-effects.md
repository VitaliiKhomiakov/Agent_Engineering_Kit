# TypeScript composition and effect contracts

Read when changing generics, unions, callback signatures, promises or integration
interfaces. Apply the [entry](../typescript.md); [validation/state](validation-state.md)
owns the unknown-to-owned-data boundary. The [typed-operation example](examples/typed-operation.md)
shows a generic result tied to an executed decoder, without assertions or a DSL.

## Preserve a real relationship

Use a generic when input/dependency types determine the result or another input.
A decoder `Decoder<T>` can establish T from unknown data; a bare `read<T>()` that
casts arbitrary data to the caller's desired T cannot. Prefer inference where it
preserves that relationship. A concrete signature or a union is simpler when
there is no meaningful type variation; do not add unused type parameters.

Constrain only the capability the operation actually needs. Use `keyof` and
indexed access when key selection really determines the value type. Mapped or
conditional types can preserve a genuine transformation; they should not become
a type-level interpreter hiding ordinary business rules. Name complex reusable
types, inspect their errors and measure checker cost if the affected build is slow.

Choose an overload only when call forms have different relationships that a
simple union parameter cannot express clearly. The implementation must honor
every advertised form; overload declarations and assertions do not execute
validation. Do not expand a single optional argument into an overload family.

## Outcomes, states and errors

Use named object interfaces for union variants and a `type` alias for their union.
A discriminant makes the valid data for each state visible. Handle all relevant
variants; a `never` exhaustiveness check makes an added variant a compiler-visible
change at consumers. A default success/fallback can conceal a newly unhandled case.
Untrusted wire values still need validation before entering that closed union.

Use a result union for meaningful expected outcomes callers must distinguish;
use the project's exception contract for failures that propagate. Do not catch
every exception and relabel defects as an ordinary refusal. Preserve useful cause
and context at a boundary, narrow caught `unknown`, and expose deliberate public
errors. TypeScript has no checked-exception list on `Promise<T>`.

Option/Result composition is optional when it simplifies repeated failure-aware
operations and the project already benefits from that model. A discriminated
union, guard and normal control flow often suffice. Do not add a functional
library or a monadic class hierarchy to rename a few branches. Runtime effects
and failure ordering remain part of the contract regardless of the wrapper type.

## Dependency callbacks and variance

A replacement must accept the consumer's promised inputs and preserve its outcomes.
For a callback capability, a function-valued property such as `parse: (input:
unknown) => T` is checked under `strictFunctionTypes`. Method-syntax parameters have
compatibility exceptions; a compiling assignment is not a universal substitutability
proof. Keep callback contracts honest, especially when a handler accepts only one
member of a wider union. Do not weaken a parameter with `any` or a double assertion.

Retain the receiver if a concrete method needs `this`; interface conformance does
not bind it automatically. Inject a small object or callback at the actual assembly
boundary. A typed fake must satisfy the required behavior as well as the shape;
casting an empty object to a service makes the test less informative.

## Types do not own effects

Declare `Promise<Result>` where the public operation is async. Its type does not
ensure it is awaited, cancellable, transactional, timed out or durable. Return or
await required work and give detached effects a real lifecycle owner. A callback
typed to return `void` can hide a returned promise; verify whether the invoker
awaits it and use an async callback contract when required.

Use the host's actual signal/cleanup mechanisms; a signal parameter alone does
not implement cancellation. Model completion and expected failure without claiming
that a branded transaction handle, readonly object or promise prevents external
interleavings. A timeout can leave a write's commit status unknown. Persisted
constraints, atomic operations, idempotency and durable handoff belong to the
actual adapter/use case. Do not add a generic repository for every entity solely
to obtain a type parameter.

The [JavaScript entry](../javascript.md) owns shared language/effect policy;
TypeScript contracts describe operations without extending their runtime guarantees.
For a host/framework change, read its relevant profile and verify its actual API.

## Basis

[Generics](https://www.typescriptlang.org/docs/handbook/2/generics.html),
[function design](https://www.typescriptlang.org/docs/handbook/2/functions.html),
[discriminated unions and never](https://www.typescriptlang.org/docs/handbook/2/narrowing.html),
[strict function parameters](https://www.typescriptlang.org/tsconfig/strictFunctionTypes.html)
and [promise linting](https://typescript-eslint.io/rules/no-floating-promises/)
explain mechanisms/limits. Pattern selection and effect ownership are project
policy, not guarantees added by a generic signature.
