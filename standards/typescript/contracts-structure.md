# TypeScript contracts and structure

Read when changing contract ownership, exported APIs, modules, construction or
dependency boundaries. The [entry](../typescript.md) owns the mandatory named
interface, strictness and public-signature policy; [common rules](../core.md) own
cohesion and architectural responsibility. TypeScript adds static contracts to
JavaScript; it does not require a new class or directory hierarchy.

## Put contracts with their consumers and owners

Use a named `interface` for public object and dependency contracts. The interface
describes the capability a consumer needs, not every method of a concrete SDK or
service. Keep transport, persistence and generated-client types behind adapters
unless the architecture explicitly owns that dependency. Pure contracts should
not import a framework module merely to access an unrelated type.

Use `type` for unions, tuples, mapped/conditional types and schema-derived types.
An inferred schema output should remain linked to its schema; do not hand-copy
the fields into another interface. A named interface is our consistency policy,
not a claim that object type aliases are invalid TypeScript. Local inferred
objects need no declaration merely to give each expression a name.

Define public parameter/result types at stable boundaries, including async
results. Let precise inference handle ordinary locals. Co-locate a contract with
its operation or domain owner; do not create a global `interfaces.ts` or one
file/interface for every private class. Split independently changing adapters
and responsibilities even when their filenames share a suffix.

Structural compatibility does not establish semantic identity, origin, validity
or exact field equality. Two equally shaped IDs can be swapped; extra properties
can survive assignment through a variable. Choose distinct named fields and an
explicit public projection first. Branded/opaque types are optional when mixing
same-shaped values causes a real defect; they need a controlled construction
boundary and do not validate a string or survive JSON as a runtime guarantee.

## Construction and actual runtime values

A DTO can be a plain object; a stateful model may use a class with guarded intent
methods. Choose a factory for an actual creation policy, resource protocol or
implementation selection. A constructor wrapper for every object adds no
guarantee. Prefer injected functions or a small interface to a speculative
Strategy/Repository hierarchy; a function can satisfy an actual dependency need.

Interfaces and type aliases are erased. They cannot be constructed, used with
`instanceof` or serve as runtime injection tokens. A framework requiring a class,
symbol/token, schema or decorator metadata needs that actual mechanism at its
boundary. Do not replace such a class with an interface because type checking
still succeeds; verify the framework's runtime lookup and validation path.
Do not add classes where the selected framework mechanism does not require them.

Use `satisfies` for authored literals/configuration when checking a target shape
while retaining useful inference. It is a compile-time check, not a parser or a
cast to a verified domain state. `as const` narrows authored literals and adds
readonly typing; it does not freeze arbitrary objects or prove external data.
Use an annotation when intentional widening is the contract; avoid elaborate
type expressions that merely reproduce a straightforward explicit interface.

## Type imports and module boundaries

Use `import type`/`export type` for pure type dependencies when supported by the
project toolchain. Keep a value import when its runtime identity or side effect
is required. Type-only syntax does not repair an inappropriate architectural
dependency, and a barrel can still expose private layers or create value cycles.

Match module format/resolution to the actual host and bundler. Package exports,
file extensions, path aliases, generated declarations and runtime imports are
different contracts. A `.d.ts` file can describe an API that does not actually
exist. After moving a file or changing an export, verify affected consumers and
the [actual toolchain](toolchain-verification.md), including framework registration
when present. Do not make incidental ESM or package-layout migrations.

## Basis

[Structural compatibility](https://www.typescriptlang.org/docs/handbook/type-compatibility.html),
[type-only modules](https://www.typescriptlang.org/docs/handbook/modules/reference.html),
[satisfies](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-9.html)
and [classes](https://www.typescriptlang.org/docs/handbook/2/classes.html) explain
language mechanisms. Contract placement and the interface/type preference are
project policy. See the [research](../../docs/research/2026-09-21-typescript-engineering-practices.md)
for conditions, simpler alternatives and version limits.
