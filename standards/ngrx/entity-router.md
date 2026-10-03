# NgRx Entity and Router Store

Use the [entry](../ngrx.md). These are independent optional packages; read only
the applicable subsection. SignalStore has a separate entities plugin described
in [SignalStore](signal-store.md).

## Entity collections

Use `@ngrx/entity` when a normalized ID-indexed collection serves the feature.
Choose a stable `selectId`; configure `sortComparer` only for a required collection
ordering. Keep selection as an ID and derive the selected entity. Do not store a
duplicate array and dictionary that must be manually synchronized.

Use adapter operations according to semantics: `setAll` replaces the collection,
`addMany` adds new records, `upsertMany` accepts complete records and
`updateOne`/`updateMany` apply partial changes. Updates are shallow; build a full
replacement for a nested field when that is the intended transition. Do not
assume Entity enforces domain invariants or performs server requests.

Store query/page result IDs separately from the canonical entity dictionary when
multiple result sets share records. `setAll` for one page can discard records
needed by another view. Define cache eviction and freshness; a normalized record
can exist while a query is missing, stale or failed. Handle absent/deleted IDs in
selectors without non-null assertions. Compose adapter selectors with feature
selectors and derive presentation sorting without mutating the collection.

## Router Store

Use `@ngrx/router-store` when Store selectors/Effects need shared navigation state.
Register the router reducer and `provideRouterStore` once (or the supported
NgModule equivalent) and align `stateKey` with selectors. Angular routing itself
does not require this integration.

Treat the URL as the owner of navigable parameters. Compose a route ID selector
with entity selectors instead of copying that ID into another writable slice.
Use `getRouterSelectors` with the correct state selector; custom serializers need
selectors matching their actual shape. Built-in route-param selection targets
the leaf route; handle parent/child parameters and duplicate names deliberately.
Parse strings and represent missing/invalid entities and IDs explicitly.

Choose a minimal serializable router representation. Full router snapshots contain
nonserializable structures and conflict with serializability checks. A custom
serializer must keep only the data that actual consumers need and preserve its
contract; do not store component classes or ActivatedRoute objects in feature state.

`ROUTER_NAVIGATION` defaults to pre-activation timing; guards/resolvers may still
cancel or redirect. Use the supported post-activation timing or the appropriate
completed-navigation action when the workflow requires a successful navigation.
Define behavior for cancelled navigation, reused components and back/forward.
Do not issue duplicate requests from component init, resolver and a router effect.

Basis: [Entity adapter](https://ngrx.io/guide/entity/adapter),
[Router Store](https://ngrx.io/guide/router-store),
[router selectors](https://ngrx.io/guide/router-store/selectors) and
[configuration](https://ngrx.io/guide/router-store/configuration).
