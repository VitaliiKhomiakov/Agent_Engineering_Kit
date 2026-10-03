# PostgreSQL queries and performance

Read when changing query shape, pagination, indexes or a measured database bottleneck.

## Boundaries and predictable results

Bind values through the driver's parameter API. Dynamic identifiers or sort directions
need an allowlisted query shape and identifier-aware quoting; value placeholders
cannot substitute SQL syntax. SQL PREPARE in examples illustrates server parameters,
not a requirement to manually prepare every driver call. Prepared statement lifetime
and session features must match the actual pool/proxy mode.

Select the needed columns, bound result sizes, and define a total ordering for pages.
A cursor normally includes a stable tie-breaker and matches filters/order/null rules.
Keyset pagination is useful for deep sequential traversal; OFFSET is simpler for
small bounded pages. Neither freezes a changing dataset without a chosen consistency
contract. Batch work deliberately; replacing N+1 reads with a giant join can multiply
rows and memory. Use set-based operations when they express the intended result.

## Evidence before indexing

Verify changed queries and invariants using the affected scenario and realistic
data. Use query plans when performance is the requirement; an extra index or a
repository abstraction needs a concrete benefit.

Compare estimates with actual rows, repeated loops, buffer activity, sorts/spills,
lock waits and end-to-end time using representative cardinality and parameter skew.
`EXPLAIN ANALYZE` executes the statement: use safe fixtures for writes or effects.
ROLLBACK does not undo sequence advances or external trigger effects. Plain EXPLAIN
is a lower-impact first inspection; do not promise production performance from a
tiny fixture or a forced planner setting.

Choose indexes from predicates, joins and ordering. B-tree, GIN, GiST or BRIN solve
different access problems; no universal index type or index-every-column rule applies.
For multicolumn B-trees, leading conditions usually matter; PostgreSQL 18 skip scan
can help some nonleading predicates but is not a reason to copy an 18 plan to 16.
A partial index needs a planner-recognizable predicate; parameterized generic plans
may not prove it. INCLUDE/index-only scans have size/write and visibility costs.
Measure these against the workload, including write amplification and maintenance.

Keep statistics current. Correlated predicates can justify extended statistics;
partitioning can help retention/pruning only when its key and operations fit. A
partition scheme adds constraint/index/maintenance costs and does not replace an
access index. Check prepared-query plans with realistic values: custom/generic plan
choice can matter. Avoid global planner or memory changes to mask a local issue;
per-operation memory can multiply across nodes, workers and connections.

Basis: [parameter execution](https://www.postgresql.org/docs/18/libpq-exec.html),
[EXPLAIN](https://www.postgresql.org/docs/18/using-explain.html),
[multicolumn indexes](https://www.postgresql.org/docs/18/indexes-multicolumn.html),
[partial indexes](https://www.postgresql.org/docs/18/indexes-partial.html), and
[prepared plans](https://www.postgresql.org/docs/18/sql-prepare.html).
