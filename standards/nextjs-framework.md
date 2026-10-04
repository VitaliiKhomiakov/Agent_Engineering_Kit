# Next.js

Apply only where Next.js is used, with [React](react.md) and its shared language
rules. Select [TypeScript](typescript.md) when authored code uses it, including
Server Actions and tests. Select [Node.js](nodejs.md) for work on Node runtime,
tooling or APIs; check the actual Node, Edge, static-export or adapter contract.
A deployment target does not remove the project's build/toolchain requirements.
Read only task-relevant sections; examples and research are optional. Selecting
this profile does not require reading every topic or enabling a framework feature.

## Versions and runtime boundaries

Apply this block only when Next.js is used. Record its version, App/Pages Router,
server runtime/deployment adapter, cache model and build tool. Do not upgrade or
apply App Router/Cache Components settings to a different installed model.

Keep server-only dependencies behind enforced boundaries and client data minimal.
Each public server entry validates input and operation authority. A layout or Proxy
check is not operation authorization. Cache freshness must follow the chosen API's
actual semantics; framework caching is not a business transaction.

## Read by task

| Task touches | Read |
| --- | --- |
| Routes/layouts/parameters, navigation, API shape or feature ownership | [Routing and composition](nextjs/routing-composition.md); [feature structure](nextjs-feature-structure.md) only for structure decisions |
| Server/Client imports, RSC props, sessions, Actions or trust boundaries | [Server/Client security](nextjs/server-client-security.md) |
| Server reads, persistence, caches, mutations or revalidation | [Data, cache and mutations](nextjs/data-cache-mutations.md) |
| Streaming, errors, metadata/assets, host lifecycle or deployment | [Rendering and runtime](nextjs/rendering-runtime.md) |
| Build/tests, generated types, performance or version migration | [Verification and migration](nextjs/verification-migration.md) |

A small UI change does not require revisiting application organization. React's
task routes remain applicable; Next.js sections do not redefine their shared rules.
Example TypeScript filenames do not require converting a JavaScript project.

## Basis

[Next.js research](../docs/research/2026-09-21-nextjs-engineering-practices.md) records
primary evidence, alternatives and version limits checked on 2026-09-21. The
[practice plan](../docs/plans/2026-09-21-engineering-practices.md) records verification.
