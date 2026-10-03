# Doctrine queries and DBAL

Read for DBAL SQL/results/transactions or ORM query shape, N+1, pagination and
batches. DBAL is usable without ORM or Symfony. Keep persistence access in the
appropriate adapter under the [common rules](../core.md).

## Select the smallest useful query abstraction

Use an existing ORM repository/finder for simple entity retrieval. DQL or its
QueryBuilder describes entity queries; DBAL SQL/QueryBuilder describes database
rows. Choose DBAL/native SQL for appropriate projections, database features or
bulk work; this does not require a second domain model or a migration away from ORM.

A fixed parameterized query is often clearer than a builder. Builders help compose
real optional predicates; generic filter languages and CRUD frameworks add their
own contracts and security surface. Keep tenant/authorization predicates in every
relevant query path, including counts, bulk writes and direct DBAL access.

## Bind values and control SQL structure

Bind values through parameters with appropriate types. Builders do not make
arbitrary expressions safe. Map allowed sort/filter names to trusted SQL or DQL
expressions; placeholders do not bind table names, column names or keywords.
Quote required identifiers through the platform API, not by quoting untrusted SQL.

DBAL `ArrayParameterType` expands lists through connection `executeQuery()` or
`executeStatement()`; it is not a portable way to bind an array to a prepared
statement's single placeholder. Define empty-list behavior and cap list/page
sizes. DBAL QueryBuilder positional parameters start at zero, while statement
`bindValue()` positions start at one; named parameters reduce this confusion.

[DBAL QueryBuilder](https://www.doctrine-project.org/projects/doctrine-dbal/en/4.4/reference/query-builder.html)
and [retrieval/manipulation](https://www.doctrine-project.org/projects/doctrine-dbal/en/4.4/reference/data-retrieval-and-manipulation.html)
document these contracts.

## Result boundaries

Use `executeQuery()` for a result and `executeStatement()` for an affected-row
count. Plain DBAL fetches do not apply all ORM type conversions; driver/platform
and PHP versions can affect returned scalar types. Narrow and validate the actual
row once in the adapter, then expose a named projection or a meaningful scalar.
Do not use unchecked casts or PHPDoc assertions to make a database row fit a DTO.

Distinguish `false` for no fetched row from a zero, empty string or SQL NULL inside
a row. Prefer row fetching when a single-column value could itself be `false`.
Bound full result materialization. For large results, account for driver buffering
as well as application memory, and free a result in `finally` when consumption may
end early. The connection's owner controls closure and transaction lifetime.

## DBAL transactions

Give the complete operation one transaction owner. `Connection::transactional()`
commits a successful callback and rolls back failure; it does not coordinate a
separate EntityManager's pending changes. Use a state predicate and affected-row
check for a conditional write instead of trusting an earlier read. The optional
[DBAL reservation example](examples/dbal-reservation.md) combines that write with
an audit row and verifies rollback when the second write fails.

In DBAL 4, nested boundaries use savepoints within one real transaction; an inner
commit does not commit the outer transaction. An operation that promises committed
success must either own the outer boundary or explicitly hand that responsibility
to its caller. Do not use raw PDO transaction methods behind DBAL: its nesting
state would diverge. DBAL 3 behavior/configuration must be checked separately.

Classify retryable driver failures narrowly; repeat a whole safe operation with
bounded attempts, not every integrity error. Isolation, lock waits, SQL limits and
commit uncertainty are platform concerns. Connection reuse needs known transaction
state; a rollback is not proof that an interrupted connection remains usable.
[DBAL transactions](https://www.doctrine-project.org/projects/doctrine-dbal/en/4.4/reference/transactions.html)
provides the library behavior.

## ORM query shape

Observe SQL count and rows for the actual endpoint/use case. Lazy navigation in a
loop or serializer can create N+1 queries; fetch required associations or project
needed fields deliberately. Making all relations eager can instead create huge
joins and object graphs. A join used for filtering is not necessarily a fetch join.

Collection fetch joins multiply SQL rows. Apply pagination that accounts for root
entity identity rather than a naive joined-row LIMIT; include deterministic order
and a tie-breaker for stable traversal. Choose offset or cursor behavior from the
actual API/version and product requirements, and test duplicates, missing children
and page boundaries. See [pagination](https://www.doctrine-project.org/projects/doctrine-orm/en/3.7/tutorials/pagination.html).

For large ORM jobs, consider bounded `toIterable()` plus explicit flush/clear
chunks. Collection fetch joins cannot be incrementally hydrated this way, and a
driver can still buffer rows. Bulk DQL/SQL bypasses entity methods and parts of
ORM lifecycle/version handling: carry needed invariants, version predicates and
cache/context reconciliation explicitly. Choose entity iteration when those
behaviors matter more than bulk speed; choose database bulk facilities when they
fit. See [batch processing](https://www.doctrine-project.org/projects/doctrine-orm/en/3.7/reference/batch-processing.html)
and [DQL](https://www.doctrine-project.org/projects/doctrine-orm/en/3.7/reference/dql-doctrine-query-language.html).

Metadata/query caches and result caches solve different problems. Result caching
needs a key scope, freshness and invalidation contract, especially for tenant data.
Measure before introducing it; cache invalidation does not refresh an identity map.
