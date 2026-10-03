# NgRx state architecture

Use the [entry](../ngrx.md) and Angular's [DI boundaries](../angular/architecture.md).
Choose a state owner from the actual coordination and lifetime requirements.

| Need | Suitable starting point | Cost or boundary |
| --- | --- | --- |
| Toggle, transient selection or a small draft | Component signal or form | Local lifetime; no library needed |
| Small shared state with a narrow API | Scoped signal/Observable service | Own encapsulation, cleanup and testing yourself |
| Cohesive feature state and async methods | SignalStore, provided at its owner | Can also be root-scoped; not restricted to local state |
| Coordinated events across features, many data sources, action history/tooling | Store + Effects, selectors and optional Entity | More explicit event/reducer infrastructure |
| Existing Observable-based local store | ComponentStore | Preserve valid existing usage; migration is a separate decision |

These are decision criteria, not a component-count threshold or a universal
preference for the newest library. Store and SignalStore may coexist in different
responsibilities. Bridge read-only views/commands at a clear boundary; do not
mirror the same entity into two writable stores or synchronize them bidirectionally.

NgRx recommends Signals for new local-state implementations; ComponentStore
remains supported. This supports the SignalStore choice above without requiring
an automatic migration of existing Observable-based features.

## State shape and ownership

Separate canonical entities, query result IDs/page metadata, per-request status,
UI drafts and derived values. Store IDs rather than duplicated selected entities.
Keep shareable route state in the router. A global loading boolean is inadequate
for independent concurrent requests; use keyed status or correlation IDs.

Define cache keys (including account/tenant and query), freshness/invalidation,
reload and logout behavior. A store is not an automatic server query cache.
Accept mutations through named intentions with explicit success/failure/conflict
outcomes. Keep form objects, subscriptions, browser objects and transport errors
outside serializable Store state; normalize dates and public error information.

Pure domain calculations may operate on these records. Core rich-domain policy
does not require putting mutable class instances into NgRx state or mutating a
selected object through its methods. Reducers/commands apply validated transitions;
the server still owns authoritative business invariants.

## Providers and feature boundaries

In standalone Store applications, register root `provideStore` once and register
feature slices/effects with supported `provideState`/`provideEffects` APIs at an
intentional boundary. In NgModule applications, use `forRoot` once and `forFeature`
for feature registrations. Do not duplicate registration to fix missing injection.

Lazy reducer/effect registration does not make the Store a per-component instance
or guarantee that navigation away cancels work/resets data. Define that behavior
and test it. SignalStore/ComponentStore can use component-scoped providers for
per-instance state. Route scoping needs explicit navigation/reuse expectations.

Keep state/effects/selectors with the owning feature. Shared application slices
are reserved for actual shared concerns. Cross-feature events describe facts or
intent; consumers own their reactions. Avoid effect chains that secretly depend
on sibling registration order or imports of another feature's private reducer.

Basis: [why Store](https://ngrx.io/guide/store/why),
[SignalStore](https://ngrx.io/guide/signals/signal-store),
[ComponentStore](https://ngrx.io/guide/component-store),
[feature state](https://ngrx.io/guide/store/feature-creators) and
[Effects](https://ngrx.io/guide/effects).
The ownership matrix and cache/reset obligations are framework policy.
