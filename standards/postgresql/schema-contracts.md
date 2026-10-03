# PostgreSQL schema and contracts

Read when defining tables, durable invariants, SQL contracts or persistence ownership.
Use the [entry](../postgresql.md) and existing application boundaries.

## Ownership before abstraction

Keep SQL/mapping inside the persistence adapter and transaction orchestration with
its application operation. A small explicit query module may suffice. Introduce a
repository when it protects an actual domain/test boundary; do not wrap every SQL
operation in generic CRUD or force an ORM migration. Views or stored routines are
options for shared database contracts, with privilege, migration and caller-version
costs. A schema groups objects; separate services sharing it still need one owner
for each table and migration stream. Avoid competing migration systems.

## Durable rules

Enforce durable uniqueness, references, and required values with appropriate
database constraints as well as application validation. Choose constraints for
actual invariants; do not use a row CHECK as a cross-table consistency mechanism.

Name constraints that callers or migrations identify. A CHECK accepting SQL NULL
needs a separate NOT NULL when absence is forbidden. Decide whether nullable unique
keys treat NULLs as distinct; `NULLS NOT DISTINCT` requires PostgreSQL 15+. Prefer
foreign keys/unique or exclusion constraints for the rules they express. A foreign
key creates no automatic index on its referencing columns; assess access/delete
cost before adding one. Pick cascade/restrict behavior from the domain lifecycle.
For tenant-scoped references, include tenant identity in the referenced key and
foreign key where cross-tenant links are forbidden.

Application validation improves feedback; the database remains authoritative at
commit. A trigger checking other rows is not automatically concurrency-safe: design
its locking/isolation protocol with every writer. Persisted counts, stock and quotas
need an atomic operation or a deliberate conflict protocol, not a preflight SELECT.
See [transactions](transactions-concurrency.md) and the optional
[reservation example](examples/atomic-reservation.md).

## Types and boundary meaning

Choose column types from the domain and the driver mapping. Use exact numeric or
integer minor units for exact amounts, with explicit scale, rounding and bounds;
binary floats suit approximate measurements. Preserve large integer/decimal values
across language and JSON boundaries. Use `timestamptz` for an instant; it does not
preserve the original zone name. Store a zone separately when future wall-clock
scheduling needs it; a date-only value is not a midnight instant.

Use relational columns for keys, relations and frequently constrained data. `jsonb`
can hold a genuinely variable document, with a defined schema/version owner and
focused indexes; it does not replace validation or justify storing every object as
JSON. Updating a document still contends on its row. Identity/sequence values are
identifiers, not gapless counters or evidence of commit order.

Project query results explicitly and map them into named application contracts.
Distinguish zero rows, a nullable field, and an execution failure. Map expected
SQLSTATE plus the known constraint/operation into a domain outcome; do not parse
localized messages or turn all integrity failures into the same public conflict.
Keep SQL and sensitive row details out of public errors.

Basis: [16 constraints](https://www.postgresql.org/docs/16/ddl-constraints.html),
[numeric](https://www.postgresql.org/docs/18/datatype-numeric.html),
[time](https://www.postgresql.org/docs/18/datatype-datetime.html),
[JSON](https://www.postgresql.org/docs/18/datatype-json.html), and
[SQLSTATE](https://www.postgresql.org/docs/18/errcodes-appendix.html).
