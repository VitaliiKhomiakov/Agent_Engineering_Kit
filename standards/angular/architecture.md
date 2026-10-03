# Angular architecture and composition

Use the [Angular entry](../angular.md). Structure follows cohesive product
capabilities; source folders do not determine service lifetime.

## Feature ownership

Keep a feature's pages, UI, state, adapters and tests close together. Introduce
subfolders only when they improve navigation. For example:

```text
src/app/
  app.config.ts                  # composition root
  app.routes.ts                  # top-level route boundaries
  platform/auth/                 # actual application-wide integration
  shared/ui/                     # reusable presentation, no feature imports
  features/orders/
    orders.routes.ts
    order-list/                  # component, template, styles, tests together
    order-details/
    data-access/                 # HTTP adapter and boundary contracts
    state/                       # chosen store, selectors/effects if used
```

This is an illustrative layout, not a requirement to create empty layers. Avoid
application-wide dumping grounds named `components`, `services`, `models` or
`store`. A state directory inside a cohesive feature is appropriate when useful.
Do not force Next.js/FSD routing or Nx libraries on an Angular project.

Pages coordinate intent with a feature's state API. Reusable UI accepts typed
inputs and emits meaningful events; it does not reach into unrelated stores or
fetch domain data itself. A small leaf component may legitimately own local state.
Keep independently meaningful components and services in their own files; colocate
templates/styles/specs and preserve the project's suffix convention.

Expose a small feature API. Cross-feature code uses public selectors/events or a
consumer-owned contract, not deep imports of private state internals. Shared UI
must not import features. A facade is useful for an actual boundary or multiple
consumers; do not add a forwarding wrapper around every store method.

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
The dependency boundaries and example folders are framework policy.
