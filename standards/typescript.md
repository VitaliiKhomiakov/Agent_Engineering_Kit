# TypeScript: strict types and interfaces

Apply this common TypeScript profile with the [common rules](core.md), regardless
of runtime. The [JavaScript entry](nodejs-typescript.md) owns shared language
and effect rules; apply its Node.js sections only when code runs in that host.
NestJS, Next.js and [Angular](angular.md) add their own relevant requirements
only when the respective framework is used. Angular selects [NgRx](ngrx.md)
only when an NgRx package is used or explicitly chosen.
Read only sections relevant to the task; stop once its applicable rules are known.
Examples and research are optional, not an instruction to load all links recursively.

## Mandatory rules

- Use strict type checking. The target configuration is `strict: true`; do not
  weaken it to make a build pass. The project pins the TypeScript version.
- Do not add explicit or implicit `any`, including `any[]`, `Promise<any>`, and
  `Record<string, any>`. This also applies to tests, mocks, and fixtures.
- Describe public object and dependency contracts with named `interface`
  declarations. Use `type` for unions, tuples, mapped or conditional types, and
  types derived from schemas. Do not duplicate a schema with an interface that
  repeats the same fields.
- Explicitly type the inputs and result of public functions and methods, including
  `Promise<Result>`. Local values may use precise type inference.
- A dependency interface describes the operations its consumer needs. Do not
  create an interface for every private class or collect all application contracts
  in one `interfaces.ts`. Place a contract with its architectural owner.
- Type props, events, hook results, DTOs, errors, and collections. A generic must
  preserve the relationship between input and result rather than conceal it.

## Read by task

| Task touches | Read |
| --- | --- |
| Interfaces/type ownership, modules, construction, dependencies or public APIs | [Contracts and structure](typescript/contracts-structure.md) |
| Unknown input, schemas/narrowing, presence/null, readonly state or invariants | [Validation and state](typescript/validation-state.md) |
| Generics, unions/exhaustiveness, callbacks, promises or typed integration contracts | [Composition and effects](typescript/composition-effects.md) |
| Compiler/lint checks, emit/resolution, framework generation, upgrades or performance | [Toolchain and verification](typescript/toolchain-verification.md) |

## External data

At a boundary, an unknown value has the `unknown` type and goes through the
accepted runtime validation or demonstrable type narrowing. Use a concrete
contract after the boundary. Do not make `unknown` a universal business-layer type.

`as`, a double assertion such as `as unknown as T`, a non-null assertion, and
disabled diagnostics do not replace data validation. An assertion is acceptable
only for an established invariant the analyzer cannot express; do not use it to
hide a type mismatch.

Third-party library types may contain `any`; do not rewrite vendor code. Confine
the dynamic boundary to an adapter, validate the value, and return a typed result.
Do not propagate a library's `any` into authored public contracts.

## Enforceability

`strict` does not ban explicit `any` or all vendor leaks. Use the project type-check
command and its required config/framework generation; enforce `no-explicit-any`
and unsafe-operation rules when the corresponding lint tooling is configured.
The [toolchain section](typescript/toolchain-verification.md#enforceability)
owns the full checks and legacy-migration obligations. Do not weaken checks, add
suppressions or migrate unrelated legacy code to make a local change pass.

Type checking does not execute validation, freeze state, authorize an operation,
cancel work or provide a transaction. Verify actual runtime behavior and module
loading at the changed boundary. Keep the supported compiler/toolchain pinned.

## Basis

- [TypeScript research](../docs/research/2026-09-21-typescript-engineering-practices.md)
  records primary evidence checked on 2026-09-21, policy choices and version limits;
  the [practice plan](../docs/plans/2026-09-21-engineering-practices.md) records checks.
- [TypeScript: strict](https://www.typescriptlang.org/tsconfig/strict.html) describes
  the compiler option group.
- [typescript-eslint: no-explicit-any](https://typescript-eslint.io/rules/no-explicit-any/)
  explains the separate ban on explicit `any` and the safer `unknown` type.

These restrictions are mandatory as a user standard; they are not a claim that
the language technically prohibits dynamic types.
