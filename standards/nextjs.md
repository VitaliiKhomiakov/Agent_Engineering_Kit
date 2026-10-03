# Next.js / React

Apply React guidance to React work, including projects without Next.js, together
with the [common standard](core.md). TypeScript must follow the mandatory
[strict typing profile](typescript.md), including props, hooks, API contracts,
tests and Server Actions. The combined catalog ID remains `nextjs`.

Read only sections relevant to the task; stop once its applicable rules are known.
Examples and research are optional; do not load all links recursively. Installed
resources are available references, not additional automatic reading routes.

## Essential React rules

Keep rendering pure, follow Hook call rules and give state one clear owner.
Use events for user commands and Effects for external synchronization with cleanup.
Preserve accessible interaction and explicit pending/error outcomes. Client checks
cannot enforce server authorization or state-dependent business invariants.

Record React, React DOM, TypeScript and renderer/build versions; the actual host,
SSR/hydration use and selected form, state, query, styling and lint tools. React
19.3 research does not authorize upgrades or make its APIs available in React 18.

## Read by task

| Task touches | Read |
| --- | --- |
| Component/hook boundaries, props, module ownership or dependency construction | [Components and boundaries](react/components-boundaries.md) |
| State shape/ownership, keys, reset, reducers, context or external stores | [State and identity](react/state-identity.md) |
| Effects, subscriptions, reads, races, cancellation or loading boundaries | [Effects and integrations](react/effects-integrations.md) |
| Forms, commands, validation, mutation outcomes or accessible feedback | [Forms and contracts](react/forms-contracts.md) |
| Tests, render/build checks, performance, security, SSR or version migration | [Verification and compatibility](react/verification-compatibility.md) |

## Next.js only: versions and task routes

Apply this block only when Next.js is used. Record its version, App/Pages Router,
server runtime/deployment adapter, cache model and build tool. Do not upgrade or
apply App Router/Cache Components settings to a different installed model.

Keep server-only dependencies behind enforced boundaries and client data minimal.
Each public server entry validates input and operation authority. A layout or Proxy
check is not operation authorization. Cache freshness must follow the chosen API's
actual semantics; framework caching is not a business transaction.

| Next.js task touches | Read |
| --- | --- |
| Routes/layouts/parameters, navigation, API shape or feature ownership | [Routing and composition](nextjs/routing-composition.md); [feature structure](nextjs-feature-structure.md) only for structure decisions |
| Server/Client imports, RSC props, sessions, Actions or trust boundaries | [Server/Client security](nextjs/server-client-security.md) |
| Server reads, persistence, caches, mutations or revalidation | [Data, cache and mutations](nextjs/data-cache-mutations.md) |
| Streaming, errors, metadata/assets, host lifecycle or deployment | [Rendering and runtime](nextjs/rendering-runtime.md) |
| Build/tests, generated types, performance or version migration | [Verification and migration](nextjs/verification-migration.md) |

A small UI change does not require revisiting application organization. React task
routes above remain applicable; Next.js sections do not redefine their shared rules.

## Basis

[React research](../docs/research/2026-09-21-react-engineering-practices.md) and
[Next.js research](../docs/research/2026-09-21-nextjs-engineering-practices.md) record
primary evidence, alternatives and version limits checked on 2026-09-21. The
[practice plan](../docs/plans/2026-09-21-engineering-practices.md) records verification.
