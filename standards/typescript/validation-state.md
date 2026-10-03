# TypeScript validation and state

Read when changing runtime schemas, narrowing, null/presence, readonly types or
business invariants. Apply the [entry's external-data policy](../typescript.md#external-data).
The [validated-command example](examples/validated-command.md) distinguishes a
parsed command from an allowed transition against current state.

## Establish the boundary before relying on types

Capture external data as `unknown`, including a vendor result typed as `any`.
Execute the accepted schema validator or real narrowing, then return a concrete
contract from the adapter. Avoid general `unknown` payloads deeper in business
code. A `Promise<T>` annotation or generic JSON/fetch helper cannot manufacture T
from external data; tie the result to an executed decoder when T varies.

Check the actual representation: object/null/array distinctions, own fields,
types, range and relevant formats. A `number` includes invalid business quantities
and non-finite values. Define the unknown-field policy: reject unsupported input,
or deliberately accept extensions and project only owned fields. TypeScript's
excess-property check on a fresh literal is not a runtime exact-object validator.
Do not spread a raw payload into an ORM entity, configuration or public response.

Keep one owner for each schema. If a validator transforms input, distinguish its
accepted input from the parsed output type and asynchronous validation behavior.
Derive the output type using the installed library's supported mechanism. Do not
declare an interface that merely repeats its fields or claim a schema runs because
it appears in a type annotation/decorator. Small explicit guards can be sufficient
for an isolated simple boundary without adding another validator dependency.

Prefer control-flow narrowing with real checks. A user-defined `value is T` or
`asserts value is T` function is a contract the compiler trusts; an incorrect
implementation can admit invalid values. Test the meaningful rejected case when
such a guard protects a boundary. Prefer a parser returning a fresh validated
value when normalization/field selection is required. `instanceof` only applies
to actual runtime constructors and does not reconstruct JSON into a class.

## Absence, nullability and indexed access

Specify whether a field may be missing, explicitly undefined, null or empty.
Do not use truthiness when zero/false/empty string are valid. An optional property
and a required property whose value includes undefined express different shapes.
`exactOptionalPropertyTypes` distinguishes absent from explicit undefined on writes;
reads can still be undefined. It is additional to `strict`, not an automatic
consequence of enabling it. Check the project's effective configuration.

`noUncheckedIndexedAccess` adds possible absence to unchecked indexed reads. It
does not validate a collection or make a broad string-key dictionary complete.
Use a named contract for known fields, an appropriate map for dynamic keys, and
handle absence rather than appending `!`. Adopt these extra flags for new/changed
boundaries where useful; broad legacy enablement is a separately scoped migration.

Use a discriminated union when valid states have different required data. Several
optional fields and Boolean flags can permit combinations the operation never
supports. Avoid replacing a simple nullable result with a general state machine
unless the caller has meaningful additional states to distinguish.

## Static readonly and runtime ownership

`readonly`, `Readonly<T>`, readonly arrays and `as const` constrain access through
that static view. They do not create a runtime freeze, deep immutability or an
exclusive owner. Mutable aliases and nested objects can still change. Accept
readonly inputs when mutation is unnecessary; return a deliberate projection or
snapshot when the caller must not hold an internal mutable reference.

Protect stateful invariants through intent operations before mutation, regardless
of which entry point calls them. Private class fields or closures may own state;
TypeScript's `private` is a compile-time restriction, unlike JavaScript `#` fields.
Use the runtime mechanism the privacy contract requires. A numeric annotation or
readonly command does not prove a transition is allowed, authorized or current.

Narrowing is not a lock or a durable validation certificate. Another owner can
change referenced state while an operation awaits work. Capture what the operation
owns, revalidate/version-check live state where required and use actual database
constraints/transactions for persistence. No type assertion replaces concurrency
control. Serialization needs an explicit wire contract; readonly and branded types
do not restore themselves when data is read back.

## Basis

[Narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html),
[object/readonly semantics](https://www.typescriptlang.org/docs/handbook/2/objects.html),
[exact optional properties](https://www.typescriptlang.org/tsconfig/exactOptionalPropertyTypes.html),
[indexed access](https://www.typescriptlang.org/tsconfig/noUncheckedIndexedAccess.html)
and [class privacy](https://www.typescriptlang.org/docs/handbook/2/classes.html)
describe static guarantees and limits. Domain/ownership obligations remain project
policy; TypeScript is not a runtime validation or persistence system.
