# NgRx

Use with the [Angular entry](angular.md) and its TypeScript requirements. Select
when an NgRx package is used or explicitly chosen. Installing SignalStore does
not require Store/Effects, and Store does not require SignalStore or Router Store.
Read only relevant package sections; examples and research are optional.

## Essential contract

- Record installed `@ngrx/*` versions, Angular/RxJS compatibility, actual providers
  and the selected state model. Preserve an existing approach unless its migration
  is requested. Optional packages and plugins require an actual use case.
- Give data one authoritative owner with explicit lifetime, reset and cache
  invalidation rules. Choose feature-local or shared state deliberately; separate
  URL state, form drafts, server entities and derived view models.
- In classic Store, express intent/outcomes as typed actions, keep reducers pure,
  handle external work through Effects/adapters and read through selectors.
  Signals can consume Store via `selectSignal` without replacing that architecture.
- In SignalStore, expose read-only state/derivations and named methods; update
  through internal immutable transitions. RxJS interop handles event/concurrency
  needs. Do not mechanically recreate action/reducer/effect layers for each method.
- Distinguish derivation memoization, Observable sharing and remote-data caching.
  None automatically supplies freshness, request isolation or server authorization.

## Read by task

| Task touches | Read |
| --- | --- |
| Library selection or state shape | [State architecture](ngrx/state-architecture.md) |
| Root Store wiring, flat feature Store files or component-local stores | [Store placement](ngrx/state-architecture.md#store-placement) |
| Eager/lazy registration, providers or lifecycle | [Providers and feature boundaries](ngrx/state-architecture.md#providers-and-feature-boundaries) |
| Store actions/reducers, selectors, memoization or `selectSignal` | [Store and selectors](ngrx/store-selectors.md) |
| Effects, concurrency, errors, retries or external synchronization | [Effects and async workflows](ngrx/effects.md) |
| Normalized Entity collections or Router Store | [Entity and Router Store](ngrx/entity-router.md), relevant subsection only |
| SignalStore composition, computed state, rxMethod or signal entities | [SignalStore](ngrx/signal-store.md) |
| Tests, runtime checks, DevTools or migration evidence | [Verification](ngrx/verification.md) |

Optional examples: [memoized Store view model](ngrx/examples/store-view-model.md)
and [SignalStore request flow](ngrx/examples/signal-store-request.md).
[Research](../docs/research/2026-09-29-angular-ngrx-engineering-practices.md)
records official documentation checked on 2026-09-29 and verification limits.
