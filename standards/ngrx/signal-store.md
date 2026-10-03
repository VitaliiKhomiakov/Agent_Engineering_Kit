# NgRx SignalStore

Use the [entry](../ngrx.md) for `@ngrx/signals`. SignalStore is an injectable state
owner; it can be local, route-scoped or application-wide. It is not classic Store
with renamed selectors, and does not require installing `@ngrx/store`/Effects.

## Composition and ownership

Compose `signalStore` features in dependency order: state, derived values,
methods and lifecycle behavior as needed. `withState` supplies state;
`withComputed` exposes pure derived values; `withMethods` supplies commands.
Dependencies and additional properties can use supported feature APIs such as
`withProps`, after checking the installed version. Avoid accidental name overrides.

Keep protected state enabled and perform updates inside methods with `patchState`
or typed updaters. Do not set `protectedState: false` merely to let a component
patch fields. Read-only signals are not deep immutability: replace changed nested
objects/arrays. Expose business/UI intent instead of a generic public `setState`
that lets arbitrary consumers bypass transitions.

Use `computed` for derived lists/counts/flags; keep the underlying entities as the
single writable source. Do not copy every computed value into state with Angular
effects. Custom SignalStore features should capture an actual repeated contract,
not create a generic store framework for every future entity.

Provide the store where its state belongs. Component providers create independent
instances and tie cleanup to component destruction; `{ providedIn: 'root' }`
shares an instance. Route environment providers do not guarantee reset on every
navigation. Own account changes, reset and cache lifetime explicitly.

## Async work with rxMethod

`rxMethod` composes an RxJS pipeline. A static input triggers once; a signal or
Observable input connects a reactive source. Register such a source once at an
owned initialization point, not on every effect run or render. Creation and
reactive-input calls must respect the installed API's injection-context/cleanup
contract; bind shorter-lived consumers explicitly when the store outlives them.

Choose `switchMap`/`concatMap`/`exhaustMap`/bounded `mergeMap` by the actual workflow.
Catch errors inside each request, using `tapResponse` or explicit `catchError`,
so subsequent method calls still work. Store pending/success/error outcomes and
allow explicit retry. Place loading initialization after cancellation of the old
inner stream, or guard cleanup by request ID: `finalize` runs on unsubscribe and
can otherwise clear the next request's loading flag.

Signal inputs represent current values and can coalesce intermediate changes;
use an event/Observable source or explicit static method calls when each command
must be preserved. SignalStore does not automatically serialize concurrent writes
or deduplicate calls. Promise-based methods also need error, stale-response and
destruction handling; `await` alone provides none of those guarantees.

## Entities and optional extensions

Use `withEntities` and its typed collection updaters from `@ngrx/signals/entities`
when normalized collections help. Configure collection names/IDs consistently and
compose updates through `patchState`. The plugin is distinct from classic
`@ngrx/entity`; do not mix their adapters. Query membership, pagination, selected
IDs and freshness retain the [Entity ownership rules](entity-router.md).

SignalStore events/resource extensions and third-party persistence/DevTools
plugins are optional, version-sensitive choices. Adopt only for a concrete
cross-store event, async resource or observability requirement. SignalStore's
computed values do not give it classic Store's action history, runtime checks
or replay semantics automatically.

Basis: [SignalStore](https://ngrx.io/guide/signals/signal-store),
[RxJS integration](https://ngrx.io/guide/signals/rxjs-integration),
[entities](https://ngrx.io/guide/signals/signal-store/entity-management),
[lifecycle](https://ngrx.io/guide/signals/signal-store/lifecycle-hooks) and
[events](https://ngrx.io/guide/signals/signal-store/events).
