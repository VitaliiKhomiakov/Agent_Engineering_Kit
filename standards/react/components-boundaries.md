# React components and dependency boundaries

Read for component decomposition, Hook extraction, props or module ownership.
The [entry](../react.md) owns selection; [core](../core.md) owns shared architecture.

## Cohesive owners

- A feature represents a user action: place an order, change an address, or add a
  document to favorites. A button, modal, or individual input does not become a
  feature merely because it has a click handler.
- Small private UI components and their props may share a file. An independent
  component, complex hook, API adapter, and input schema have different
  responsibilities and move apart as they grow or become reusable.
- When a component grows beyond `size.react_component_review_lines`, resolved
  through [policy configuration](../policy-configuration.md), reconsider whether it mixes UI,
  requests, state, and transformations. This is a signal in our standard, not a
  React rule. The common size limits still apply. Moving the entire component into
  a large hook is not successful decomposition.

Prefer function components for new UI and composition through props/children for
real variation. Preserve working classes during unrelated edits; error boundaries
may use a class or the project's supported boundary component. Do not invent a
base component, generic Hook engine or frontend Repository for a single call.

Colocate a capability's UI, state and API adapter where their ownership is clear.
A framework-neutral TypeScript example is `features/reserve/{ReservationForm.tsx, contract.ts,
reservation-api.ts}`; these are possible owners, not required folders. Route-local
UI can stay local. Framework route conventions apply only to the chosen framework.
In Next.js, the existing [feature structure](../nextjs-feature-structure.md) owns
import directions. React itself mandates no FSD layers or route directory.

## Props, Hooks and assembly

When using [TypeScript](../typescript.md), use named interfaces for public
props/dependencies and express real variants with unions rather than unrelated
Boolean flags. JavaScript uses explicit contracts under its shared language rules. Prefer a
small explicit callback such as `reserve(command)` to passing an entire SDK/client
through the tree. Do not duplicate transport models just to cross a component.

A pure calculation belongs in an ordinary function. A custom Hook encapsulates
React state/synchronization for a cohesive capability; calling it twice creates
two state owners, not a shared store. Avoid lifecycle-shaped wrappers that obscure
reactive inputs or make the dependency linter ineffective. Context supplies an
explicit tree-scoped dependency when distant consumers need it; it is not an
application-wide DI container requirement. A prop is simpler for nearby consumers.
Construct long-lived integrations in the actual composition owner, not on every render.

Rendering and state updaters/reducers must be repeatable without external writes.
Treat props/state as immutable snapshots; local mutation of a newly created object
is fine. Start purchases, logging side effects and subscriptions outside rendering.
React can restart or discard render work. Call Hooks at the top level of components
or custom Hooks, before early returns. React 19's `use` has documented conditional
call exceptions; it still belongs in React rendering and cannot be caught in a
`try/catch`. Do not generalize that exception to `useState` or `useEffect`.

## Basis

[Thinking in React](https://react.dev/learn/thinking-in-react),
[purity](https://react.dev/reference/rules/components-and-hooks-must-be-pure),
[Hook rules](https://react.dev/reference/rules/rules-of-hooks),
[custom Hooks](https://react.dev/learn/reusing-logic-with-custom-hooks) and
[`use`](https://react.dev/reference/react/use) describe React behavior. Capability
ownership, named contracts and avoiding speculative layers are project policy.
