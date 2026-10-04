# Angular architecture and composition

Use the [Angular entry](../angular.md). Structure follows cohesive product
capabilities; source folders do not determine service lifetime.

## Feature ownership

For new application structure, group code by application section under
`features/`. A section owns its route group, optional layout and simple pages.
When a domain needs related pages, UI, state and adapters, keep them together in
a named subfolder of its section. A simple screen does not need a domain wrapper.

Recommended shape, with optional folders shown only to explain their roles:

```text
src/app/
  app.ts                         # root outlet host
  app.config.ts                  # application provider composition
  app.routes.ts                  # top-level routes and access policy
  config/                        # shared configuration, when needed
  http/                          # shared transport policy, when needed
  session/                       # session storage adapter, when needed
  store/root-store.providers.ts   # only when classic NgRx Store is selected
  shared/ui/                     # genuinely cross-feature presentation
  features/
    auth/
      pages/login-page/          # component, template, styles, tests
      routing/                   # guards, when needed
      data-access/               # auth API and boundary contracts
      store/                     # only when a store is selected
    <authenticated-section>/     # project-chosen name
      <section>.routes.ts
      layout/                    # navigation and nested outlet
      pages/profile-page/        # simple section-owned screen
      orders/                    # cohesive nested domain
        orders.routes.ts
        pages/orders-page/
        components/order-item/
        data-access/
        store/                   # chosen state owner, when needed
```

`<authenticated-section>` means the section available after authentication.
Choose its name for the project: `core`, `workspace` or `portal`, for example;
replace `<section>` in the route filename consistently. These are placeholders,
not literal paths. `core` is not a reserved layer or a required infrastructure
folder. A folder name does not protect access; use the
[routing and authorization contract](boundaries.md#routing).
Independent public/admin sections may be siblings. Directory nesting does not
require matching URL prefixes.

This is the framework's recommended grouping, not a mandated Angular tree or
an instruction to migrate an established compatible layout. Introduce role
folders only when useful; do not create empty layers. A small section can be
routed directly from the application routes without a separate route file or
layout. Do not force Next.js/FSD routing or Nx libraries on an Angular project.

Avoid application-wide collections of unrelated `components`, `services`,
`models` or Store logic. Domain-local role folders preserve cohesive ownership.
An application-level `store/` is appropriate for provider composition alone;
feature state and transitions remain with their owner. Angular without NgRx
needs neither that folder nor a state library. When NgRx is selected, follow
[its placement and registration rules](../ngrx/state-architecture.md#store-placement).

## Pages, components and layouts

| Role | Responsibility |
| --- | --- |
| Root component | Hosts the application outlet and actual application-wide presentation |
| Section layout | Owns section navigation, shared shell actions and its nested outlet |
| Page | Represents a routed screen; composes state views, local UI state and user intentions |
| Domain component | Presents typed inputs and emits meaningful events; may own small local UI state |
| Shared UI | Provides presentation used across features without importing feature code |

Pages coordinate through the feature's state API. A presentation component does
not fetch domain data, import pages/layouts or reach into feature stores. A
stateful widget may own a cohesive local state service/store when its behavior
requires one; make that responsibility explicit rather than hiding it in a
presentation component. Keep a simple toggle, draft or selection local without
requiring a store extraction.

Each page, component and layout has its own directory with colocated TypeScript,
template, styles and applicable tests. For example, `pages/orders-page/` contains
`orders-page.ts`, `orders-page.html`, `orders-page.scss` and applicable
`orders-page.spec.ts`. Use descriptive Page names for routed screens; preserve
the project's established filename suffix, styling and inline-asset conventions.
Keep independently meaningful components and services in their own files. Do not
promote a component into `shared/ui/` until cross-feature reuse warrants it.

## Dependency direction

- Application composition imports section routes and necessary registration
  contracts. Features must not import `app.config.ts` or root Store wiring.
- Section routes/layout compose their children. A nested domain must not import
  its parent's layout or route configuration; communicate through explicit
  contracts instead of reversing the composition dependency.
- Pages compose domain components and state APIs. Presentation can use readonly
  domain types without depending on their HTTP adapter or Store implementation.
- Data-access owns typed adapters, boundary contracts and decoding; it does not
  depend on UI or stores. State orchestration may call adapters. Extract reusable
  domain calculations when warranted rather than burying them in presentation.
- Shared infrastructure such as config, transport and storage does not import
  features. Root provider composition is a separate responsibility and may
  import feature registration contracts. Shared UI also has no feature imports.

Expose a small feature API. Cross-feature code uses public selectors/events or a
consumer-owned contract, not another feature's pages or private state internals.
A public API can be an explicitly designated module; a barrel is not required.
A facade is useful for an actual boundary or multiple consumers; do not add a
forwarding wrapper around every store method.

## Services, stores and dependency injection

- API services expose typed operations returning Observable/Promise results.
  They map and validate transport data; they do not secretly subscribe, navigate,
  mutate a second cache or notify components through a public Subject.
- A store coordinates state and its transitions. Pure calculations and reusable
  business rules remain functions/classes outside Angular when that independence
  matters. NgRx state is serializable data, not a container of mutable rich classes.
- Choose providers by ownership: root for truly shared application state,
  component for per-instance state, route environment for a route subtree's DI.
  Re-providing a service shadows ancestors and can create inconsistent caches.
- A route provider is not a promise of reset on each URL change or route exit.
  Reuse strategies and injector lifetimes matter. Define reset on parameter,
  tenant/account change or logout explicitly; verify navigation away and back.
- Prefer `inject` in an actual injection context for new compatible code.
  Constructor injection remains valid. Capture dependencies before asynchronous
  callbacks; calling `inject` after `await` or in an ordinary event method is invalid.

## Standalone and NgModules

Standalone components import only used template dependencies. Register router,
HTTP and application services at the composition root; feature providers live
at intentional boundaries. Use lazy route imports where bundle/loading needs
justify them; avoid eager barrels pulling lazy features into the initial bundle.

In NgModule projects, distinguish declarations/imports/exports from providers.
Keep feature modules cohesive, export only intended APIs and register root
services once. Avoid an oversized SharedModule that also installs singleton
state/effects. Interoperate with standalone code using supported APIs rather
than rewriting the application for a small change.

Basis: [style guide](https://angular.dev/style-guide),
[hierarchical DI](https://angular.dev/guide/di/hierarchical-dependency-injection),
[NgModules](https://angular.dev/guide/ngmodules/overview) and
[route definitions](https://angular.dev/guide/routing/define-routes).
The section/domain grouping, bounded role folders and dependency boundaries are
framework policy. Angular's style guide favors feature grouping and discourages
grouping by code type; it does not prescribe this particular folder tree.
