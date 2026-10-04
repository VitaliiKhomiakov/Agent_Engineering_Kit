# JavaScript values, contracts and state

Read when changing external data, JSDoc, coercion, JSON, object ownership or
business invariants. Apply the [entry's typed-boundary obligations](../javascript.md#typed-boundaries).
The [input/state example](examples/input-state.md) is optional.

## From external representation to an owned contract

Give stable commands, results and data objects meaningful names. Use the project's
accepted runtime schemas and JSDoc `@typedef`, `@param` and `@returns` where they
clarify a boundary. Infer obvious locals; do not annotate every expression or
adopt a validator/checker just to spell a small literal. A known DTO remains a
known contract in JavaScript; an unrestricted dictionary does not express it.

Treat untrusted parsed values as `unknown` while checking them. A JSDoc assertion,
an editor suggestion, `JSON.parse()` success or a class-shaped object does not
validate a contract. Check the boundary's actual representation, allowed fields,
presence, types and relevant limits, then return an explicit owned projection.
Keep transport parsing separate from the domain's current-state decision.

For a small JSON-text contract, explicit checks can be clearer than a new schema
dependency. For established or large schemas, reuse the accepted validator and
its declared output type. Do not duplicate a schema in handwritten checks that
can drift. Distinguish parsing JSON text from accepting arbitrary live objects:
the latter can contain getters, proxies and inherited properties.

Make coercion a contract decision. Prefer `===` for ordinary comparisons; it
does not convert a numeric string to a number. Object equality is identity unless
the domain defines a value comparison. `Object.is` and collection key comparison
have different `NaN`/signed-zero semantics; choose them only where that matters.

Do not use truthiness to distinguish missing data from valid `0`, `false` or `''`.
Use own-property checks when omission differs from a present field; choose
`undefined`, `null` and defaults deliberately. `??` defaults only for nullish
values; it does not validate the result or establish property presence.

Validate numeric type, finiteness, range and, for bounded integral quantities,
`Number.isSafeInteger`. Implicit `Number()`/`parseInt()` conversions can accept
representations the contract rejects. Precision lost during parsing cannot be
recovered by a later type annotation. Use an explicit representation for exact
large IDs, money or decimal quantities; do not silently change an API to BigInt.
String length counts UTF-16 code units; bytes and user-perceived characters need
their own limits when required by the transport or product.

## State and behavioral invariants

Use `const` for bindings that do not change. It does not make the referenced object
immutable. Destructuring, object/array spread and `Object.assign` do not detach
nested mutable values. `Object.freeze` is shallow; a frozen container is not a
general guarantee that everything reachable through it cannot change.

Define who can mutate shared state and for how long. Keep invariant-bearing state
behind intent operations and validate a transition before mutation. Private class
fields or a closure can help; neither replaces persistence concurrency control.
Return a deliberate result/snapshot instead of exposing an internal mutable array
or object. Copy only the part whose independent ownership is required; blanket
deep cloning on every call can be expensive and lose semantics.

Simple transport data usually needs no rich class. Stateful business behavior may
justify one; a DTO's shape/range validation does not prove an operation is permitted
against current capacity, authorization or persisted state. Keep those decisions
with their owner. Do not add getters/setters that let callers bypass invariants,
or place an entire use case and its external effects inside a data object.

Use arrays for sequences and `Map`/`Set` when their key or membership semantics fit.
Use an object with named fields for a known result. For genuinely dynamic keys,
consider `Map` or a null-prototype dictionary; explicitly control keys and ownership
when crossing back to ordinary objects. Never merge arbitrary input into a domain
object, configuration or prototype-bearing target as a substitute for validation.

## Serialization and errors

Define the serialized contract separately from its in-memory representation.
JSON omits object properties holding `undefined`, changes non-finite numbers to
`null`, cannot directly encode BigInt, and does not preserve class behavior. A JSON
round trip is not a general clone. `structuredClone`, where the host supports it,
handles supported data graphs, but does not reproduce arbitrary functions,
prototype contracts or private class state. Reconstruct owned behavior explicitly.

Use actionable error types or a named result variant according to the established
API. Do not invent an error class per function. Preserve a useful `cause` when
adding context; normalize unknown thrown values at an appropriate boundary. Map
expected refusals separately from defects, and expose a deliberate public error
projection instead of raw payloads, secrets or stack traces. See [async ownership](async-effects.md)
when failures interact with unfinished work.

## Basis

[Equality](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Equality_comparisons_and_sameness),
[safe integers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/isSafeInteger),
[freeze](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze),
[JSON serialization](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify),
[structured clone](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm)
and [JSDoc support](https://www.typescriptlang.org/docs/handbook/jsdoc-supported-types.html)
establish tool/language limits; named contracts and ownership are project policy.
