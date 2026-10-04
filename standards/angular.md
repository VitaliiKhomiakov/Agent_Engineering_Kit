# Angular

Apply with the [common rules](core.md) and mandatory [TypeScript profile](typescript.md).
Select for actual Angular applications/libraries, not every TypeScript or HTML file.
Read only the relevant sections below. Examples and research are optional.

## Establish the project contract

Record Angular core/CLI/build, TypeScript, RxJS and used NgRx package versions from
the lockfile; bootstrap style, ZoneJS/zoneless configuration, CSR/SSR/hydration,
forms, state and styling choices. Check the installed version's compatibility
matrix and API stability. Current manuals describe Angular 22; they do not upgrade
an older application or authorize converting its NgModules or state model.

## Essential rules

- Organize by product feature. Components own presentation and user intent;
  services own external adapters; stores own their state and transitions.
  Keep public contracts explicit and dependencies directed toward their owners.
- Prefer standalone composition for new compatible code. Preserve functioning
  NgModule boundaries in existing projects unless migration is in scope.
- Prefer OnPush for new application components and make the strategy explicit
  when the installed version does not default to it. Immutable updates, supported
  render notifications and stable list identity are part of that contract.
- Give every datum one owner. Choose local signals, a scoped state service,
  SignalStore or Store/Effects according to lifetime and coordination needs.
  Angular alone does not require NgRx, a global store, or a facade per component.
- Derive values with `computed` or memoized selectors. Keep asynchronous workflows
  explicit through Observable composition or a compatible resource API; do not
  synchronize duplicate writable copies with effects.
- Use strict template checks, typed inputs/outputs and validated external data.
  Client forms, route guards and cached permissions do not enforce server authority.

## Read by task

| Task touches | Read |
| --- | --- |
| Folder structure, application sections, nested domains or feature ownership | [Feature ownership](angular/architecture.md#feature-ownership) |
| Pages, components, layouts or allowed imports | [Presentation roles](angular/architecture.md#pages-components-and-layouts) and [dependency direction](angular/architecture.md#dependency-direction) |
| Services or provider scope | [Services, stores and DI](angular/architecture.md#services-stores-and-dependency-injection) |
| Standalone or NgModule composition | [Standalone and NgModules](angular/architecture.md#standalone-and-ngmodules) |
| Local state, signals, Observable ownership, subscriptions or HTTP races | [Reactivity and state](angular/reactivity.md) |
| OnPush, zoneless, rendering cost, tracking or lazy views | [Change detection and performance](angular/change-detection.md) |
| Route state, forms, validation, HTTP contracts or security | [Routes, forms and boundaries](angular/boundaries.md) |
| Component styles, global tokens, themes or encapsulation | [Styles](angular/styles.md) |
| Builds, tests, SSR, compatibility or performance evidence | [Verification](angular/verification.md) |
| NgRx is used or explicitly selected | [NgRx entry](ngrx.md), then only the relevant package sections |

Optional example: [application structure and state placement](angular/examples/application-structure.md).
Its NgRx sections apply only when that library is selected.

## Basis

[Research](../docs/research/2026-09-29-angular-ngrx-engineering-practices.md)
records primary sources checked on 2026-09-29, version limits and policy choices.
These rules support both Observable and signal view models without imposing a
state-library migration on an existing feature.
