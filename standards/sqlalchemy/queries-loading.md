# SQLAlchemy queries and loading

Read for SELECT/result contracts, relationship access, bulk DML or query performance.

## Query shape and results

Use 2.0-style `select()` and execute/scalars according to the result contract.
`scalars()` selects a single result element; it does not turn every multi-column row
into a DTO. Choose one/one_or_none/all/iteration by the expected cardinality. A first
result consumer does not add a SQL LIMIT for you. Apply a limit to the statement when
needed, and preserve explicit ordering/tie-breakers for pagination.

Use SQL expression parameters or bound `text()` values. Do not interpolate untrusted
values into SQL, identifiers, literal SQL fragments or relationship configuration.
Dynamic identifiers/order choices need an allowlisted expression/identifier path.
Selecting only needed columns can simplify a read contract and avoid a loaded graph;
fully mapped entities remain useful for identity and lifecycle work.

## Load the required graph deliberately

Choose a loading strategy for the operation, not one global eager/lazy preference.
`selectinload` is often a useful collection default, with extra queries and backend
capability limits such as composite-key tuple IN. `joinedload` can suit small scalar
relations but multiplies rows for collections; collection joined eager loads require
explicit result `unique()`. A loader join does not replace an explicit join used for
filtering or sorting the query's result.

Avoid N+1 access in serializers/templates. `raiseload`/`lazy='raise'` can detect
unplanned relationship access, but unit-of-work flush may still load required state;
they are not a universal no-SQL firewall. Deferred/expired columns also need a loading
contract. Loader options and identity-map contents can affect subsequent reads in the
same session; verify with a fresh session when that is the real request boundary.
Use explicit refresh/populate-existing only with a reason and care for pending edits.

For async work, implicit I/O on ordinary attribute access is especially hazardous.
Load what the DTO needs inside an awaited operation, then copy it into owned data.
The [async projection example](examples/async-projection.md) demonstrates this with
an eager-loaded collection and a relationship access guard. Bound total data volume:
a parent LIMIT alone does not bound the size of every child collection.

## Writes and performance

ORM unit-of-work updates, ORM-enabled set-based DML and Core execution have different
state synchronization, event and cascade behavior. Bulk mappings by primary key are
not interchangeable with one UPDATE predicate. Choose `synchronize_session` behavior
where loaded entities can be affected; do not return stale identities accidentally.
Check RETURNING/executemany support against the actual dialect/driver and SQLAlchemy
version. Do not use a rowcount assumption without its documented execution contract.

Measure database calls, selected rows, hydration cost and query plans before choosing
bulk APIs, caching or streaming. `yield_per`/streaming require compatible loaders and
consumption; calling all() defeats a memory bound. Do not combine incompatible
uniquing/collection loading assumptions with streaming. Close results and their
connections even when consumers stop early. SQL compilation caching is not a cache
of database results; pool sizing is not a remedy for unnecessary queries.

Basis: [SELECT/result forms](https://docs.sqlalchemy.org/en/20/orm/queryguide/select.html),
[relationship loading](https://docs.sqlalchemy.org/en/20/orm/queryguide/relationships.html),
[DML](https://docs.sqlalchemy.org/en/20/orm/queryguide/dml.html), and
[ORM execution options](https://docs.sqlalchemy.org/en/20/orm/queryguide/api.html).
