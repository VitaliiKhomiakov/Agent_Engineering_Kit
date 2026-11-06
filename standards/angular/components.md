# Angular component contracts

Use the [Angular entry](../angular.md) for the installed version and composition
contract. This topic owns component APIs, queries and projection;
[reactivity](reactivity.md) owns state and subscription choices, and
[form boundaries](boundaries.md#forms-and-component-contracts) own form semantics.

## Inputs and outputs

Inputs carry data; outputs describe intent for the receiving owner to handle.
Use typed `input`/`output` APIs in new compatible code; preserve supported
decorator APIs when changing existing components. Declare a meaningful default,
an explicit absent state, or a required input according to the caller contract.
A required input enforces binding presence, not the business validity of its
value; do not read it before Angular supplies it. Validate external data at its
existing boundary rather than trust the generic type or duplicate validation in
every presentation component.

Keep state ownership explicit. Use `model` for an intentional two-way control
contract, not to expose a store's mutation API. Do not mutate a parent's object or
maintain a synchronized writable copy of an input. Choose output names/payloads
that identify the requested operation; bind them at the responsible consumer.
Component outputs are not bubbling DOM events. Avoid aliases that obscure the
contract or collide with native element events; expose composed behavior through
the [directive API](directives.md#composition-and-public-api) deliberately.

## Child queries

Use `viewChild`/`viewChildren` for the component's own view and
`contentChild`/`contentChildren` for consumer-provided content. Query by the
intended directive/component token or template reference; a string query locator
is not a CSS selector. Queries do not traverse another component's template.

A single optional query can be `undefined` before availability or when an `@if`
branch is absent. Handle that state and reread the signal when using the child;
do not cache an initial DOM reference across removal/recreation. A required query
is appropriate only when the component/consumer contract guarantees a match;
reading it without a result throws. It does not make a conditional child present
or permit an early constructor read. Use the relevant render lifecycle for DOM
work, as described in [directives](directives.md#lifetime-and-browser-effects).

Plural queries yield collections. Check the selected API's descendant scope:
in Angular 20, `contentChild` searches descendants by default while
`contentChildren` searches direct children by default. Set scope deliberately
where nesting is part of the public contract. Supported decorator queries remain
valid; a local change does not require migrating all queries to signals.

## Projection and creation ownership

Treat projected content as a consumer-owned view. The receiving component defines
slots and consumes their contract; it does not gain ownership of the consumer's
state or reach through nested components to manipulate their implementation.

`ng-content` is a compile-time projection placeholder. Do not conditionally place
it inside `@if`/`@for`/`@switch` to achieve lazy creation: projected nodes are still
created even if their slot is hidden. Let the consumer conditionally create its
content, or use an explicit template-fragment contract when the receiver must
control instantiation. Decide what an absent optional slot displays and whether
unmatched content has a default slot. Static slot selection and runtime query
results serve different purposes; hiding a slot does not remove its content query.

## Host semantics and accessibility

Use native controls when their semantics fit the interaction. Keep accessible
names, disabled behavior, keyboard operation and state attributes coherent with
the actual control, including when it is projected. An ARIA attribute alone does
not implement the control's interaction. Do not introduce a second focusable host
around an already focusable native control without a specific interaction need.

Choose one owner for host properties, classes, attributes and event handling.
Prefer Angular host/template bindings for declarative behavior. Resolve collisions
between consumer bindings, the component and composed directives explicitly;
do not depend on an accidental override to establish roles, IDs or tab order.

For conditional UI, specify where focus goes after opening, closing or removing
the focused child. When an update creates the focus target, wait for that render
and handle absence; preserve unaffected keyboard behavior. Apply existing
[form feedback](boundaries.md#forms-and-component-contracts) and
[style acceptance](verification.md#scss-and-style-acceptance) only when affected.
Use [verification](verification.md#choose-evidence-by-the-changed-contract) for
behavioral checks; no particular widget library or accessibility threshold is
introduced here.

Optional example: [conditional view, projected action and focus](examples/component-contracts.md).
The [dated evidence](../../docs/research/2026-11-06-angular-component-contracts.md)
separates versioned source review from executed checks.

Basis: Angular 20 [input](https://v20.angular.dev/api/core/input),
[output](https://v20.angular.dev/api/core/output),
[queries](https://v20.angular.dev/guide/components/queries),
[projection](https://v20.angular.dev/guide/components/content-projection),
[host elements](https://v20.angular.dev/guide/components/host-elements) and
[accessibility](https://v20.angular.dev/best-practices/a11y).
