# React

Apply to React work with [JavaScript](javascript.md) and the [common rules](core.md).
Select the mandatory [TypeScript profile](typescript.md) when TypeScript is used,
including props, hooks, API contracts and tests. Select [Next.js](nextjs-framework.md)
only where that framework is used, and [Node.js](nodejs.md) for actual Node host work.
Read only relevant sections; examples and research are optional, not a recursive
reading queue. An example's TypeScript syntax does not require converting a
JavaScript project or selecting unused technology guidance.

## Essential React rules

Keep rendering pure, follow Hook call rules and give state one clear owner.
Use events for user commands and Effects for external synchronization with cleanup.
Preserve accessible interaction and explicit pending/error outcomes. Client checks
cannot enforce server authorization or state-dependent business invariants.

Record React, React DOM, renderer/build and, when used, TypeScript versions; the actual host,
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

## Basis

[React research](../docs/research/2026-09-21-react-engineering-practices.md) records
primary evidence, alternatives and version limits checked on 2026-09-21. The
[practice plan](../docs/plans/2026-09-21-engineering-practices.md) records verification.
