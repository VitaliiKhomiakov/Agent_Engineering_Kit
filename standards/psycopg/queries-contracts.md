# psycopg queries and contracts

Read for SQL construction, row contracts, adaptation or bulk I/O. Use the
[entry](../psycopg.md); PostgreSQL owns durable invariants and query-plan guidance.

## SQL structure and data

Pass values as execute's second argument with `%s` or named placeholders. Do not
quote placeholders or interpolate values with Python formatting/f-strings. A single
positional value still needs a one-element sequence. Values remain parameters even
when they contain quotes, percent signs or SQL-looking text.

Parameters cannot name tables/columns or replace arbitrary SQL syntax. Use SQL and
Identifier composition for trusted templates and identifiers; select object/order
choices from the operation's allowed set. Correct quoting is not authorization to
read any named table. Never wrap untrusted text in SQL and assume it is escaped.
The [typed query](examples/typed-query.md) separates an enum-selected identifier from
a value placeholder without building a query framework.

Default server-side binding has PostgreSQL statement restrictions. For an affected
utility/DDL statement, use its supported parameter form or reviewed composition;
ClientCursor is an optional client-binding alternative with different capabilities.
Do not switch every query to string composition because one statement cannot bind.

## Row and adaptation contracts

Choose class_row or another precise row factory for stable application outputs;
keep Connection/Cursor generics consistent with it. Select explicit columns and
aliases matching the contract. fetchone can return None; distinguish no row from a
nullable field or an error. A dataclass factory constructs rows but does not check
Python annotations against values or validate the server schema.

Validate public input at its entry; enforce state-dependent rules in the operation
and durable invariants in PostgreSQL. Preserve Decimal precision, UUID, null and
datetime/time-zone meaning at serialization boundaries. Python integers are not
bounded by a PostgreSQL integer column. Json/Jsonb wrappers select adaptation, not
a document schema or permission policy. Prefer local adapter registration when a
custom type requires it; global adaptation changes can affect unrelated callers.

For a list predicate, use the supported array/ANY form where appropriate rather
than treating a sequence parameter as SQL syntax for IN. Decide empty-list and NULL
semantics explicitly. Keep unstructured database results inside the adapter instead
of spreading Any or type-checking bypasses into business contracts.

## Select bulk tools for a measured requirement

Ordinary execute/iteration is enough for small work. Use server cursors/streaming
when result volume warrants their connection/transaction lifetime; close them on
partial consumption and do not fetchall an intended bounded stream. For COPY, use
its context manager and choose row adaptation or preformatted block data deliberately.
Row-oriented COPY APIs have format/option restrictions; check the chosen mode.

Pipeline mode reduces client/server round trips, not server execution time or the
need for transaction ownership. Handle synchronization/error boundaries explicitly;
COPY and cursor features have compatibility limits. Prepared statements are a
connection-level performance feature, not a separate injection defense. Check their
support through the actual pooler and libpq/driver matrix before changing thresholds.

Basis: [parameters](https://www.psycopg.org/psycopg3/docs/basic/params.html),
[SQL composition](https://www.psycopg.org/psycopg3/docs/api/sql.html),
[typing](https://www.psycopg.org/psycopg3/docs/advanced/typing.html),
[adaptation](https://www.psycopg.org/psycopg3/docs/basic/adapt.html),
[cursors](https://www.psycopg.org/psycopg3/docs/advanced/cursors.html),
[COPY](https://www.psycopg.org/psycopg3/docs/basic/copy.html),
[pipeline](https://www.psycopg.org/psycopg3/docs/advanced/pipeline.html), and
[prepared statements](https://www.psycopg.org/psycopg3/docs/advanced/prepare.html).
