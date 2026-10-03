# TypeORM queries and relations

Read for query scope, associations, loading, projections and bulk work.

## Query contracts

Bind values; allowlist dynamic identifiers, ordering and selectable fields. Include
the tenant/authorization scope at the data boundary where required. Validate required
IDs and filters before querying; an omitted condition is not an authorization policy.

Check installed null/undefined behavior. Where supported, explicitly set
`invalidWhereValuesBehavior: { null: 'throw', undefined: 'throw' }` and use `IsNull()`
for SQL NULL. TypeORM 0.3 and 1.0 defaults differ. This setting does not protect
direct QueryBuilder `where`/`andWhere`/`orWhere` expressions; validate their inputs
and parameterize them too. Do not pass an absent identifier to `findOneBy` and
interpret a returned row as the requested object. Omitted keys still need checking.

Read results have a deliberate shape: hydrated entities for behavior, explicit
projections for lists/reporting. Raw rows and aggregate values need mapping and
driver conversion; a generic type assertion does not perform runtime validation.
Do not call aggregate business methods on partially selected entities missing the
state those methods require. Avoid putting query builders or lazy promises in core
contracts or serializing entity graphs directly.

## Associations and loading

- Define FK ownership explicitly; a many-to-one stores its join column, one-to-one
  needs its chosen join-column side, and many-to-many needs its join-table side.
  Synchronize the sides used in memory without assuming inverse assignment writes
  the FK. Prefer only the navigation actually needed.
- Keep unloaded and loaded-empty relations distinct. Do not initialize mapped
  relation arrays to `[]` indiscriminately: saving an entity can treat that as a
  requested removal. An intent method needing children must receive a fully loaded
  aggregate or use an explicitly scoped operation; absence is not empty state.
- Choose cascade operations explicitly. Avoid `cascade: true` on incoming graphs.
  Set `orphanedRowAction` deliberately and check the installed version, FK
  nullability and ownership; do not rely on defaults for delete semantics. Database
  `ON DELETE`, ORM remove cascades and orphan handling have different triggers.
- Choose relations/joins for each use case. Eager loading differs between find
  APIs and QueryBuilder; lazy Promise relations can issue hidden I/O during access.
  Inspect query count and cardinality for the changed path before adding caches.

## Bounded results

Bound list/batch sizes and use deterministic ordering with a unique tie-breaker.
To-many joins multiply rows: verify entity-page and count semantics rather than
assuming raw LIMIT gives a page of aggregates. Use the applicable `take`/`skip`
behavior or a deliberate keyset/ID-first query for the actual workload and driver.
Avoid unbounded relation traversal and Promise.all over every row of a table.

Soft deletion does not automatically release unique keys or enforce tenant scope.
Define visibility and restoration rules, including related rows, and use matching
database constraints. Bulk writes must satisfy the exceptional-path contract in
[transactions](transactions-lifetime.md#effects-and-exceptional-write-paths).

Basis: [null/undefined handling](https://typeorm.io/docs/data-source/null-and-undefined-handling/),
[relations](https://typeorm.io/docs/relations/relations/),
[relation FAQ](https://typeorm.io/docs/relations/relations-faq/),
[QueryBuilder](https://typeorm.io/docs/query-builder/select-query-builder/), and
[upgrade guidance](https://typeorm.io/docs/releases/1.0/upgrading-from-0.3/).
