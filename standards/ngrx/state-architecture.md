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

## Store placement

Source ownership, registration timing and instance lifetime are separate
decisions. For the Angular [section/domain structure](../angular/architecture.md#feature-ownership),
use these placements when the corresponding state model is selected:

| Location | Responsibility | Scope |
| --- | --- | --- |
| `app/store/root-store.providers.ts` | Compose classic Store initialization, eager slices/Effects and diagnostics | One application Store; not the owner of every domain's implementation |
| `features/<section>[/<domain>]/store/` | Keep the feature's state model and transitions together | A classic Store slice is part of the application Store even when registered lazily |
| Owning page/component directory | Keep local signals/forms, or an extracted scoped state service/store | Per-instance state when provided at the component; the path alone grants no lifetime |

The root provider entry is called from application configuration. It may import
eager feature registration contracts, but must not collect domain reducers,
selectors or HTTP workflows into a shared implementation folder. A shared auth
slice can stay in its owning feature while being registered eagerly for use by
other sections. Keep lazy-only feature registrations out of root composition.
Features and infrastructure must not import this root wiring.

### Flat classic Store files

Within a cohesive domain, keep the following used responsibilities together:

```text
features/<section>/orders/store/
  orders-state.ts        # state type and related state-model definitions
  orders-actions.ts      # typed intentions and outcomes
  orders-reducer.ts      # initial state and pure transitions
  orders-feature.ts      # feature identity, reducer and generated selectors
  orders-selectors.ts    # public base selectors and derived views
  orders-effects.ts      # async orchestration through adapters
```

This is a flat directory, not one subfolder per technical role. Colocate
applicable tests; preserve existing naming conventions and do not add empty
Effects or other files for unused responsibilities. Split a growing store by
cohesive domain responsibility, not merely to reproduce the tree.

The feature module above is a TypeScript module using a feature creator, not an
Angular NgModule. It composes the reducer; the selector module consumes its
generated selectors and exposes public views. Do not import that selector module
back into the feature creator or reducer. Effects consume actions, state views
and API adapters; none of these state modules imports pages or presentation.
For behavioral contracts, use [Store/selectors](store-selectors.md) and
[Effects](effects.md) rather than duplicating their policies here.

### Component-local state

A page may read the shared Store while owning a filter or form draft locally.
Keep simple state in its signals/forms. For a cohesive local workflow that needs
extraction, place a file such as `pages/order-editor-page/order-editor.store.ts`
beside its owner; use a local `store/` subfolder only when multiple related files
improve navigation. A reusable stateful widget follows the same ownership rule.

Choose the mechanism using the matrix above. New compatible local stores may use
SignalStore; existing ComponentStore remains valid. Neither requires a local copy
of the classic actions/reducer/effects file structure. Use component providers
for independent component instances; a root-provided store remains shared even
when its source file sits next to one component. See
[SignalStore composition and ownership](signal-store.md#composition-and-ownership)
when that package is selected. Do not duplicate canonical entities into a second
writable store to supply a local view.

## Providers and feature boundaries

In standalone Store applications, register root `provideStore` once and register
feature slices/effects with supported `provideState`/`provideEffects` APIs at an
intentional boundary. Root composition registers slices needed before navigation;
the owning route registers lazy slices before their consumers run. Root and route
registration must not both register the same slice/Effects. In NgModule
applications, use `forRoot` once and `forFeature` for feature registrations.
Do not duplicate registration to fix missing injection.

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
The ownership matrix, file placement and cache/reset obligations are framework
policy; the chosen folders do not establish NgRx instance scope.
