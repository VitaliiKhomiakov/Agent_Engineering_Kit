# PostgreSQL engineering practices: evidence and adoption

Research date: **2026-09-21**. Scope: K15 of the
[approved plan](../plans/2026-09-21-engineering-practices.md), adopted through the
[short PostgreSQL entry](../../standards/postgresql.md), five conditional sections
and two optional SQL examples. SQLAlchemy/psycopg adoption remains K16/K17; an
adapter boundary here does not select either dependency.

## Version and evidence contract

The initial project fixture declares **PostgreSQL 16**. The official
[version policy](https://www.postgresql.org/support/versioning/) lists supported
14–18, with current patches **16.15 and 18.6**; 14 support ends in November 2026.
The [August release notice](https://www.postgresql.org/about/news/postgresql-186-1711-1615-1519-1424-and-19-beta-3-released-3365/)
also lists 19 beta, which is not adopted as a stable target. These are checked-date
facts, not permanent patch recommendations. Review the relevant release/security
notes for an actual upgrade; no upgrade of an existing project is authorized here.

Runtime checks used existing local images reporting **16.15 and 18.4**, with their
bundled psql, not a newly fetched current-major patch. Two task-owned containers
had networking disabled, no published ports, no host binds and database state in
tmpfs. Local trust authentication is an isolated-fixture convenience, not deployment
guidance. Image IDs and SQL logs are retained in the stage record. Passing 18.4
checks is not a claim that 18.6 or every intermediate release was executed.

Primary sources below were inspected on the research date. Versioned 16 manuals
anchor existing-project compatibility; 18 manuals/release notes identify additions.
**R** means a framework requirement grounded in correctness, security or existing
user policy; **D** is a recommended default under stated conditions; **O** is an
optional technique with a demonstrated need. PostgreSQL semantics are facts, not
policy strengths. No mandatory repository/DDD/ORM hierarchy is inferred from SQL.

## Coverage and instruction owners

| Research area | Decision and owner |
| --- | --- |
| 1. Architecture and dependencies | D: explicit SQL adapter and migration owner; [schema](../../standards/postgresql/schema-contracts.md); R: preserve existing core boundaries |
| 2. Idioms and patterns | D: declarative constraints and set-based operations; O: repositories, routines, outbox or partitioning for a concrete requirement |
| 3. Contracts, validation, invariants, errors | R: durable integrity separate from transport shape; SQLSTATE plus known constraint; schema |
| 4. State, concurrency, cancellation, lifetime | R: operation transaction/connection ownership and committed outcome; [transactions](../../standards/postgresql/transactions-concurrency.md) |
| 5. Persistence and integration | R: retry scope, uncertain outcomes, external-effect policy and deployment-compatible data changes; transactions/migrations |
| 6. Testing and review | R: material PostgreSQL semantics tested on PostgreSQL; [verification](../../standards/postgresql/migrations-verification.md) with shared proportionality policy |
| 7. Security, operations, performance | R: actual role/tenant trust and recovery contract; D: measured query work; [security](../../standards/postgresql/security-operations.md), [queries](../../standards/postgresql/queries-performance.md) |
| 8. Versions and migration | R: actual server capabilities and explicit migration scope; verification; 16-compatible examples |

## Contracts and construction decisions

**Problem:** DTOs or read-before-insert checks appear to guarantee durable rules.
[16 constraints](https://www.postgresql.org/docs/16/ddl-constraints.html) and the
[18 counterpart](https://www.postgresql.org/docs/18/ddl-constraints.html) distinguish
row checks, required values, keys and references. **R:** use the appropriate database
boundary where integrity must survive multiple writers; reason: core requires
invariants independently of HTTP entry. **D:** declarative constraints before custom
trigger protocols. **Alternative/cost:** application feedback remains useful but
alone can race; cross-row trigger logic needs its own concurrency design. Composite
tenant references prevent an invalid relation, not unauthorized access. Null-unique
semantics are a deliberate choice; NULLS NOT DISTINCT is available from 15.

**Problem:** database representation loses domain meaning at a driver boundary.
[Numeric types](https://www.postgresql.org/docs/18/datatype-numeric.html),
[date/time](https://www.postgresql.org/docs/18/datatype-datetime.html),
[JSON](https://www.postgresql.org/docs/18/datatype-json.html), and
[sequences](https://www.postgresql.org/docs/18/functions-sequence.html) define distinct
contracts. **D:** exact amounts, meaningful time types and relational keys; **O:**
JSONB for a variable document with a schema owner. **Alternative/cost:** approximate
numbers suit measurements; storing everything in JSON weakens straightforward
constraints and makes updates contend on documents. **R:** preserve exactness and
absence semantics across the actual adapter. An identity value is not a gapless
business counter. These decisions apply to 16/18; newer ID generators are separate.

**Problem:** abstraction hides who changes persistent state. **D:** keep cohesive
SQL/mapping modules and one transaction/migration owner. A repository or stored
routine is **O** when it creates a useful boundary, not because the pattern has a
name. **Alternative/cost:** a direct adapter operation avoids CRUD scaffolding;
a public database routine needs privilege, version and caller coordination. This is
framework synthesis from core ownership rules, not a PostgreSQL architecture mandate.
[Error codes](https://www.postgresql.org/docs/18/errcodes-appendix.html) support **R**:
classify known errors structurally, without exposing SQL or depending on message text.

## Concurrency and effect decisions

**Problem:** individually valid requests together overspend state.
[16 isolation](https://www.postgresql.org/docs/16/transaction-iso.html) defines
Read Committed statement snapshots; [UPDATE](https://www.postgresql.org/docs/18/sql-update.html)
and [data-modifying WITH](https://www.postgresql.org/docs/18/queries-with.html) support
the atomic reservation example. **D:** a conditional update for a one-row bound.
**Alternative/cost:** explicit locking handles multi-step decisions but adds wait/order
protocols; Serializable can protect broader decisions but requires retries. **R:**
choose the protocol for the invariant, not a global isolation preference. A receipt
insert and debit need one atomic boundary. The example owns no external effect.

**Problem:** retrying the last failed statement reuses a stale decision or duplicates
work. [Serialization handling](https://www.postgresql.org/docs/18/mvcc-serialization-failure-handling.html)
and [18 isolation](https://www.postgresql.org/docs/18/transaction-iso.html) support
**R:** restart the full decision transaction when retry is appropriate, within the
operation budget. **Alternative/cost:** return a typed conflict when retries are not
allowed; a bounded retry policy adds delay and final-refusal semantics. Keep stable
operation identity and external effects outside unsafe replay. Uncertain COMMIT is
a reconciliation problem, not proof of rollback. An outbox is **O** for reliable
publication, with its own dispatch/deduplication cost; it is an architectural synthesis,
not a promise of exactly-once external execution from PostgreSQL.

**Problem:** upsert or skipping locks is treated as a universal concurrency solution.
[INSERT](https://www.postgresql.org/docs/18/sql-insert.html) and
[SELECT locking](https://www.postgresql.org/docs/18/sql-select.html) specify narrower
contracts. **O:** upsert for a named conflict, SKIP LOCKED for competing queue claims.
**Alternative/cost:** a normal conditional write is simpler for stock; queue claims
need recovery and fairness decisions. **R:** do not swallow a receipt conflict after
a debit. [Explicit locks](https://www.postgresql.org/docs/18/explicit-locking.html)
justify scoped lifetimes/order and distinguishing session from transaction locks.
The requirements apply to the actual protocol in either supported example major.

## Query and operational decisions

**Problem:** performance advice becomes unconditional indexing or caching.
[EXPLAIN](https://www.postgresql.org/docs/18/using-explain.html),
[statistics](https://www.postgresql.org/docs/18/planner-stats.html), and
[prepared plans](https://www.postgresql.org/docs/18/sql-prepare.html) support **D**:
measure the affected workload and inspect estimates versus observed work before
changing query/index shape. **R:** ANALYZE executes the statement, so fixture safety
matters. **Alternative/cost:** plain EXPLAIN has less runtime evidence but avoids
executing the write; a tiny benchmark cannot establish production latency.

**O:** multicolumn, partial, covering or partitioned designs for access/retention
needs, with write, size, maintenance and planner-proof costs. See
[multicolumn](https://www.postgresql.org/docs/18/indexes-multicolumn.html),
[partial](https://www.postgresql.org/docs/18/indexes-partial.html),
[index-only](https://www.postgresql.org/docs/18/indexes-index-only-scans.html), and
[partitioning](https://www.postgresql.org/docs/18/ddl-partitioning.html).
**Alternative:** a simple B-tree and bounded ordinary query may suffice. Version 18
skip scan makes “a B-tree can never help without its first column” too absolute;
it does not guarantee the planner will use a given index or apply to 16.
[Resource settings](https://www.postgresql.org/docs/18/runtime-config-resource.html)
also argue against copying per-operation memory settings across connection counts.

**Problem:** SQL text or session state crosses a trust boundary.
[Bound execution](https://www.postgresql.org/docs/18/libpq-exec.html) supports **R**:
parameterize values, select/quote identifiers deliberately. **D:** least-privileged
runtime roles and controlled schema creation/path; **O:** SECURITY DEFINER only for
a reviewed privilege boundary, with the costs in
[schemas](https://www.postgresql.org/docs/18/ddl-schemas.html) and
[CREATE FUNCTION](https://www.postgresql.org/docs/18/sql-createfunction.html).
[RLS](https://www.postgresql.org/docs/18/ddl-rowsecurity.html) is **O** for tenant defense,
with **R** tests as the real runtime role; owner/superuser tests can conceal bypass.
**Alternative/cost:** explicit tenant-scoped queries remain simpler, but still need
authorization and reliable coverage. RLS does not authenticate a user-set context.
[TLS verification](https://www.postgresql.org/docs/18/libpq-ssl.html) is a separate
connection contract, not guaranteed by the existence of a pool.

**Problem:** idle work, canceled requests or replicas are mistaken for durable control.
[Timeouts](https://www.postgresql.org/docs/18/runtime-config-client.html),
[vacuum](https://www.postgresql.org/docs/18/routine-vacuuming.html), and
[standby behavior](https://www.postgresql.org/docs/18/warm-standby.html) support **R**:
name lifetime/consistency budgets and the responsible cleanup owner. **D:** diagnose
waits, long snapshots and retention before broad tuning. **O:** replication/PITR for
a recovery objective, with an actual restore test and ongoing WAL/retention cost;
[recovery](https://www.postgresql.org/docs/18/continuous-archiving.html) and
[logical replication limits](https://www.postgresql.org/docs/18/logical-replication-restrictions.html)
make backups, schema and sequence coordination explicit. Simpler managed/local
arrangements can satisfy smaller requirements; no topology is imposed here.

## Migration and version decisions

**Problem:** a schema command succeeds locally but blocks or invalidates deployed
writers. **D:** expand/backfill/validate/contract when versions overlap; **R:**
preserve data meaning, review locks and runner transaction mode. Compare
[16 ALTER TABLE](https://www.postgresql.org/docs/16/sql-altertable.html) with
[18 ALTER TABLE](https://www.postgresql.org/docs/18/sql-altertable.html): 18 adds
not-null forms that must not be copied into 16. The example uses a portable CHECK
helper and keeps it valid until SET NOT NULL finishes. **Alternative/cost:** a final
CREATE TABLE suffices for a new empty fixture; staged migration adds coordination
but permits historical repair before validation. NOT VALID still rejects new bad rows.

**O:** concurrent index build for a live-write requirement, under the constraints in
[CREATE INDEX](https://www.postgresql.org/docs/18/sql-createindex.html).
**Alternative/cost:** a normal build is simpler for an allowed maintenance window;
concurrent work has extra scans/waits and can leave invalid artifacts. **R:** inspect
failed state and repair deliberately, rather than blindly accepting an existing name.
Read [18 release changes](https://www.postgresql.org/docs/18/release-18.html) for features
such as virtual generated columns, UUIDv7 and temporal constraints; none is required
for an existing 16 application. No sources conflict here: versioned capability and
workload conditions explain the differences in recommendations.

## Adoption, verification and limits

The [reservation](../../standards/postgresql/examples/atomic-reservation.md) example
separates representation, positive-quantity/current-stock decisions, durable checks
and atomic receipt creation. The [migration](../../standards/postgresql/examples/online-constraint.md)
example makes existing-data failure and invalid concurrent-index state observable.
Ten published SQL file blocks match the executed files exactly. Six scenario groups
passed on each of 16.15 and 18.4, including a monitored two-session wait, `40001` then
a whole-operation restart, duplicate debit rollback, failed validation and index repair.
The temporary harness uses psql subprocesses and a bounded synchronization protocol;
it does not depend on adopting a Python database driver.

Artifact/composition evidence and exact commands live in the canonical plan's K15
result. Catalog changes only register seven optional resources under the existing
PostgreSQL profile; metadata rules and 17 profile identities are preserved. No new
production behavior or permanent test suite is introduced for these documentation
changes. The inline review follows the workspace adaptation.

Not executed: real ORM/driver or proxy pool, RLS/TLS deployment, durable crash/failover,
backup/PITR restore, production load/plans, live rolling deploy, PostgreSQL 18.6/19,
or native assistant reading compliance. Limits are explicit in both examples.
P3–P7 remain planned. These fixtures establish SQL behavior in their actual environment,
not production readiness, performance targets or token savings.
