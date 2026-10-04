# Example: Angular application sections and state ownership

Optional architecture illustration for the [Angular entry](../../angular.md).
The rule owners are [Angular architecture](../architecture.md) and, only when
NgRx is selected, [NgRx state architecture](../../ngrx/state-architecture.md).
This is a folder and scenario example, not an executable application or a
requirement to install packages. Use APIs supported by the consuming project.

## Sections, pages and domain components

Consider an application with public authentication screens and a workspace
available after authentication. `workspace` is the chosen section name here;
another project could use `core`, `portal` or a product-specific name. It does
not name a shared-infrastructure layer or impose a `/workspace` URL prefix.

```text
src/
  main.ts
  styles.scss
  app/
    app.ts
    app.html
    app.scss
    app.config.ts
    app.routes.ts
    config/                              # shared configuration
    http/                                # cross-cutting transport policy
    session/                             # session storage adapter
    shared/ui/                           # only if UI is reused across features
    features/
      auth/
        pages/
          login-page/
            login-page.ts
            login-page.html
            login-page.scss
            login-page.spec.ts
        routing/
          auth-guard.ts
        data-access/
          auth-api.ts
          auth-contracts.ts
          auth-decoders.ts
      workspace/
        workspace.routes.ts
        layout/
          workspace-layout.ts
          workspace-layout.html
          workspace-layout.scss
          workspace-layout.spec.ts
        pages/
          profile-page/                  # a simple screen; colocated assets
        orders/
          orders.routes.ts
          pages/
            orders-page/                 # list and user intentions
            order-editor-page/           # editing screen and local draft
          components/
            order-item/
              order-item.ts
              order-item.html
              order-item.scss
              order-item.spec.ts
          data-access/
            orders-api.ts
            order-contracts.ts
            order-decoders.ts
```

This tree groups UI and adapters independently of the state library. The next
section adds a particular state choice. Omitted page contents follow the shown
colocation pattern; applicable adapter/state tests also live beside their owners.
Do not create unused folders or change an established suffix/style convention
just to reproduce the example.

`app.routes.ts` composes public routes and the authenticated route group. The
group uses its guard and layout; `workspace.routes.ts` composes the profile page
and orders routes. `WorkspaceLayout` owns shared navigation and its outlet.
`ProfilePage` is directly section-owned because it needs no separate domain
subtree. Orders has related API, UI and state responsibilities, so it owns a
named subtree. Route access follows the [routing contract](../boundaries.md#routing),
including the distinction between client navigation and server authorization.

## Optional NgRx state placement

For a project that selects classic Store, assume auth must be available before
navigation and orders is loaded lazily. Add the following files to the tree:

```text
src/app/
  store/
    root-store.providers.ts              # root composition, invoked by app.config
    root-store.providers.spec.ts
  features/
    auth/
      store/
        auth-state.ts
        auth-actions.ts
        auth-reducer.ts
        auth-feature.ts
        auth-selectors.ts
        auth-effects.ts
    workspace/orders/
      store/
        orders-state.ts
        orders-actions.ts
        orders-reducer.ts
        orders-feature.ts
        orders-selectors.ts
        orders-effects.ts
```

The root provider function initializes Store and registers the eager auth slice
and Effects. `orders.routes.ts` registers the orders slice and Effects at its
own boundary. Both slices belong to the same application Store; neither the
feature folder nor lazy registration creates a store per component. The root
entry imports feature registration contracts without moving domain logic into
`app/store/`. The [placement owner](../../ngrx/state-architecture.md#store-placement)
defines file responsibilities and the
[provider owner](../../ngrx/state-architecture.md#providers-and-feature-boundaries)
defines registration and lifecycle constraints.

For the editor, the basic choice is a form draft in `OrderEditorPage`. If local
workflow complexity justifies an extracted store, place it beside the page:

```text
features/workspace/orders/pages/order-editor-page/
  order-editor-page.ts
  order-editor-page.html
  order-editor-page.scss
  order-editor-page.spec.ts
  order-editor.store.ts                   # optional component-provided owner
  order-editor.store.spec.ts              # applicable behavior tests
```

A compatible SignalStore implementation can serve this role; existing
ComponentStore is also valid. These are alternatives, not additional required
packages. Component providers give separate editor instances their own local
state. The local owner contains edit intent/draft state, not a synchronized
second canonical orders collection. For a root- or route-provided store instead,
record that different lifetime explicitly; the file location does not select it.
See [component-local state](../../ngrx/state-architecture.md#component-local-state).

For Angular without NgRx, retain the section/page/component organization and
select local signals/forms or an appropriate service as needed. For a
SignalStore-only project, place its store with its owner without introducing
classic root Store wiring or action/reducer/effect files. Follow the existing
[state-choice guidance](../../ngrx/state-architecture.md) only when using NgRx.

## Placement and interaction scenarios

The Store-specific rows use the optional classic Store setup above. The filter
here is a transient display preference; when it defines shareable navigation,
keep it in the URL under the [routing contract](../boundaries.md#routing).

| Scenario | Where it belongs in this example | Interaction |
| --- | --- | --- |
| Add a simple account screen | `workspace/pages/account-page/` | Workspace routes compose the page; it consumes the public auth view |
| Add a transient display filter | `orders/pages/orders-page/` | The page combines its local filter with the selected orders; no second writable collection |
| Change an order row's appearance | `orders/components/order-item/` | Typed input data and output intentions; the row has no Store/HTTP dependency |
| Add an order operation | `orders/data-access/` and, for classic Store, `orders/store/` | Adapter validates transport data; Effects orchestrate; reducer applies the outcome; selectors expose views |
| Share auth with the layout/profile | `auth/store/` plus root registration | Consumers use public events/selectors; auth does not import workspace UI |
| Open two independent editors | Each editor's component-provided local owner | Drafts are independent while commands target the authoritative orders owner |

For example, a row emits a completion intention to `OrdersPage`. With classic
Store selected, the page dispatches a typed action; an Effect calls `OrdersApi`,
the outcome updates the reducer, and selectors supply the next view. The feature
creator composes its reducer; the selector module builds on the feature's
generated selectors without a reverse import. Direct Store consumption is
sufficient here; no forwarding facade is added.

For this example's lifecycle choice, leaving the orders list page cancels only
its pending list read and clears its query-result IDs/status. Canonical order
records remain available to the editor; entering the editor by a direct URL
loads a missing/stale record by ID through the domain state owner. The list's
exit event does not cancel an editor read or save. Logout/account change clears
all account-owned records and query state and invalidates pending work. These
are explicit state/event and cancellation policies, not effects of a folder name
or route exit alone. See the [request ownership contract](../../ngrx/effects.md#work-ownership)
for correlation and stale outcomes; cancelling a subscription does not establish
whether the server committed a write.
A product that retains a cache chooses and records a different policy under the
[state ownership rules](../../ngrx/state-architecture.md#state-shape-and-ownership).

## Evidence boundary

The trees and scenarios illustrate the owning rules; they contain no runnable
source, dependency pins or performance claims. Documentation checks establish
links, catalog availability and consistency only. Application adoption still
needs its actual provider, routing, reset and interaction checks under
[Angular verification](../verification.md) and, if selected,
[NgRx verification](../../ngrx/verification.md).
