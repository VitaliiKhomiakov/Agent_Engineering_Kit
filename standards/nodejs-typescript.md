# Node.js / JavaScript / TypeScript

Apply this entry with the [common rules](core.md). Read only sections relevant to
the task; stop once its applicable rules are known. Examples and research are
optional, not an instruction to load all links recursively.

Shared JavaScript rules apply across hosts. Server responsibilities apply to
server code. NestJS also requires its [framework profile](nestjs.md). For a
Next.js UI, use the [Next.js profile](nextjs.md); apply server-side Node.js rules
as the task requires. The [strict typing profile](typescript.md) is mandatory
for TypeScript.

## Versions and modules

- Establish the JavaScript engine/host and supported targets, including browsers
  where relevant. Language syntax, host APIs and module resolution differ.
- Establish the Node.js, package manager, and TypeScript versions; the ESM/CommonJS
  mode; and how the project runs and builds. Reconcile `package.json`, the lockfile,
  build configuration, and CI. Do not migrate JavaScript to TypeScript or CommonJS
  to ESM as part of an ordinary fix.

The Node.js/TypeScript inventory above applies where those tools are present;
a browser-only script does not require installing them. Group modules by cohesive
responsibility and expose the smallest useful contract. Give mutable state and
required asynchronous effects explicit owners; validate data before accepting it.

## Read by task

| Task touches | Read |
| --- | --- |
| Modules/imports, file moves, construction, dependencies, classes or callbacks | [Modules and structure](javascript/modules-structure.md) |
| JSDoc/data contracts, coercion, null/presence, JSON, mutation or domain invariants | [Values and state](javascript/values-state.md) |
| Promises, ordering, cancellation, resources, stale results or external effects | [Async operations and effects](javascript/async-effects.md) |
| Tests, static checking, host compatibility, security, performance or upgrades | [Verification and compatibility](javascript/verification-compatibility.md) |

For code that actually runs in Node.js, also select from this table. A browser
bundle or `package.json` alone does not make Node server guidance applicable.

| Node.js task touches | Read |
| --- | --- |
| Startup/configuration, package loading, dependency assembly or direct TS execution | [Runtime and composition](nodejs/runtime-composition.md) |
| Streams, files, CPU work, workers, event callbacks or bounded concurrency | [I/O and concurrency](nodejs/io-concurrency.md) |
| HTTP servers/clients, body limits, deadlines, persistence or external effects | [HTTP and integrations](nodejs/http-integrations.md) |
| Signals, shutdown, resource cleanup, diagnostics, security checks or runtime upgrades | [Lifecycle and verification](nodejs/lifecycle-verification.md) |

## Typed boundaries

- In TypeScript, use concrete commands, DTOs, and results. Validate external
  `unknown` values before converting them to an owned type; `as` does not validate data.
- In JavaScript, preserve the same explicit contracts through the accepted runtime
  schema mechanism and JSDoc where needed. Do not install a new validator without a need.
- An input DTO may be a typed object with a schema and need not always be a class
  instance. Classes are mandatory only where the selected mechanism requires them,
  such as a particular Nest ValidationPipe configuration.
- Do not add `any`. Do not substitute unnamed payloads or `Record<string, unknown>`
  for a known contract. Genuine maps and typed arrays are acceptable.
- An ORM model or database document does not automatically become an input DTO or
  API response. Centralize domain-object creation and client configuration.

## Server execution and responsibility

Keep handlers thin, dependencies explicit and effects bounded and observed.
Assembly owns resource lifetimes; shutdown must account for application work as
well as sockets. The detailed obligations are in the applicable Node sections.

## Verification

When changing exports or paths, verify the actual run and build mechanism, not
only editor type resolution. Use the existing runner and targeted checks for the
changed operation or adapter. Do not create a separate test for every one-line
function or a new E2E suite for a local change.

## Basis

- [JavaScript research](../docs/research/2026-09-21-javascript-engineering-practices.md)
  records primary evidence checked on 2026-09-21, alternatives and version limits;
  the [practice plan](../docs/plans/2026-09-21-engineering-practices.md) records checks.
- [Node.js research](../docs/research/2026-09-21-nodejs-engineering-practices.md)
  records runtime evidence checked on 2026-09-21 and the examples' version limits.
- [TypeScript: Type Assertions](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-assertions)
  explains that type assertions provide no runtime validation.
- [Node.js: Don't Block the Event Loop](https://nodejs.org/en/learn/asynchronous-work/dont-block-the-event-loop)
  explains the constraints on synchronous work in handlers.

Module grouping and numeric thresholds are our project standard. Detailed
TypeScript rules belong to its profile; React and Next.js guidance belongs to the
[UI entry](nextjs.md), with Next.js sections conditional on that framework.
