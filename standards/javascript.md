# JavaScript

Apply across JavaScript hosts with the [common rules](core.md). Select
[Node.js](nodejs.md) only for work in that host, and the mandatory
[TypeScript profile](typescript.md) when authored code uses TypeScript.
Framework profiles apply only where used. Read task-relevant sections; examples
and research are optional, not a recursive reading queue.

## Versions and modules

- Establish the JavaScript engine/host and supported targets, including browsers
  where relevant. Language syntax, host APIs and module resolution differ.
- Check the actual package/build tools and module mode where present. Do not
  migrate JavaScript to TypeScript or CommonJS to ESM as part of an ordinary fix.

Group modules by cohesive responsibility and expose the smallest useful contract.
Give mutable state and required asynchronous effects explicit owners; validate
data before accepting it. A browser-only script does not require installing Node.

## Read by task

| Task touches | Read |
| --- | --- |
| Modules/imports, file moves, construction, dependencies, classes or callbacks | [Modules and structure](javascript/modules-structure.md) |
| JSDoc/data contracts, coercion, null/presence, JSON, mutation or domain invariants | [Values and state](javascript/values-state.md) |
| Promises, ordering, cancellation, resources, stale results or external effects | [Async operations and effects](javascript/async-effects.md) |
| Tests, static checking, host compatibility, security, performance or upgrades | [Verification and compatibility](javascript/verification-compatibility.md) |

## Typed boundaries

- Preserve explicit commands, DTOs and results through the accepted runtime
  schema mechanism and JSDoc where needed. Do not install a new validator without a need.
- An input DTO may be an object with a schema and need not always be a class
  instance. Classes are mandatory only where the selected mechanism requires them,
  such as a particular Nest ValidationPipe configuration.
- Use named contracts for known payloads; do not replace known fields with an
  unrestricted dictionary. Genuine maps and typed arrays are acceptable.
- An ORM model or database document does not automatically become an input DTO or
  API response. Centralize domain-object creation and client configuration.

For TypeScript, its [strict typing](typescript.md#mandatory-rules) and
[external-data policy](typescript.md#external-data) own named interfaces, the
ban on `any`, validation of `unknown` and the limits of type assertions.
[Values and state](javascript/values-state.md) owns shared runtime validation.

## Verification

When changing exports or paths, verify the actual run and build mechanism, not
only editor type resolution. Use the existing runner and targeted checks for the
changed operation or adapter. Do not create a separate test for every one-line
function or a new E2E suite for a local change.

## Basis

[JavaScript research](../docs/research/2026-09-21-javascript-engineering-practices.md)
records primary evidence checked on 2026-09-21, alternatives and version limits.
The [practice plan](../docs/plans/2026-09-21-engineering-practices.md) records checks.
Module grouping and numeric thresholds are local policy. Framework-specific
[React](react.md) and [Next.js](nextjs-framework.md) profiles apply only where used.
