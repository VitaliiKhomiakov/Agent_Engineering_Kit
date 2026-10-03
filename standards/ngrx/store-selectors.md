# NgRx Store, reducers and selector memoization

Use the [entry](../ngrx.md); select this section for classic `@ngrx/store`.

## Events and pure transitions

Use typed action creators/groups with unique source/event names and meaningful
payloads. Express page intent and API outcomes rather than arbitrary property
setters or a generic patch of the entire feature state. One event may update
several slices coherently; components need not dispatch a sequence of setters.

Reducers are synchronous, deterministic and side-effect-free. No HTTP, DI, storage,
time/random generation or dispatch inside a reducer. Include required timestamps,
IDs and validated data in the event. Replace changed branches while retaining
unaffected references; shallow spread does not copy nested values. Do not sort,
push or mutate a selected array or action payload.

Use `createFeature`/`createReducer` where supported; preserve established equivalents
in older code. Feature selectors require the slice to be registered before use.
Keep discriminated status variants meaningful rather than combinations of flags
that permit impossible states.

## Selectors and memoization

Expose typed feature selectors and compose `createSelector` for projections and
view models. Input selectors should read narrow, stable inputs; allocate/filter/
sort inside the projector. Returning a new array from an input selector on every
call defeats downstream memoization even when data did not change.

The default cache retains the most recent arguments/result, comparing inputs by
identity/value, not by deep content. An unrelated root update can reuse a projector
result when its selected inputs retain identity. Replacing every branch causes
unnecessary work; mutating an old branch can produce stale results. Selectors must
remain pure and must not dispatch or fetch.

Reuse selector instances. For parameterized selection, prefer composing an ID
selector or create a selector factory once per owned parameter/lifetime. Do not
call a factory in a template/getter on every render or build an unbounded global
map of selectors per search string. Selectors with props are deprecated; do not
introduce them in new compatible code. Calling `.projector` directly tests a
calculation, not the full dependency chain or its memoization.

Create store-derived view models in composed selectors rather than duplicating
the same `map`/`combineLatest` logic in multiple components. RxJS composition is
still appropriate for view-local external streams and time/event behavior.
Consume with `store.select(selector)` + `AsyncPipe`, or `store.selectSignal`
when available. Do not manually subscribe just to mirror Store into another
writable signal. Signal consumption does not remove actions, reducers or Effects.

## Optimization boundaries

Derived state generally stays derived instead of being stored and synchronized.
Custom selector memoizers or equality functions require evidence and a correctness
contract; an equality function that ignores a visible field can suppress a valid
update. Bound any multi-key cache and account for retained objects.

Selector memoization does not cache HTTP responses or establish freshness.
`shareReplay` is also not selector memoization. Use
[verification](verification.md) to check identity preservation and avoid a new
performance test for a trivial selector without a material risk.

Basis: [actions](https://ngrx.io/guide/store/actions),
[reducers](https://ngrx.io/guide/store/reducers),
[selectors](https://ngrx.io/guide/store/selectors),
[selector implementation](https://github.com/ngrx/platform/blob/main/modules/store/src/selector.ts),
[Store signals](https://ngrx.io/guide/store/selectors#using-signal-selector) and
[runtime checks](https://ngrx.io/guide/store/configuration/runtime-checks).
