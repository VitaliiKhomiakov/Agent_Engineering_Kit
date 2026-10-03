# SQLAlchemy engineering practices: evidence and adoption

Research date: **2026-09-21**. Scope: K16 of the
[practice plan](../plans/2026-09-21-engineering-practices.md). Adoption adds the
[SQLAlchemy profile](../../standards/sqlalchemy.md), five conditional sections and
two optional examples; the existing Python persistence owner is retained. SQLAlchemy
is recognized by metadata already, but previously had no dedicated catalog profile.

## Versions and evidence

The official [download page](https://www.sqlalchemy.org/download.html) identifies
**2.0.54** (September 15) as current stable and **2.1.0rc2** as prerelease. Stable
2.0 manuals are the instruction baseline; [2.1 changes](https://docs.sqlalchemy.org/en/21/changelog/migration_21.html)
are migration context only. This is not permission to update an existing application.
Initial local SQLAlchemy was 2.0.51; it was left unchanged. The stage installed 2.0.54
only in a temporary venv and recorded all resolved dependencies.

Executed: **CPython 3.12.3**, **SQLAlchemy 2.0.54**, **PostgreSQL/psql 16.15**,
**psycopg/psycopg-binary 3.3.6**, **asyncpg 0.31.0**, **greenlet 3.5.6**, and
**mypy 2.1.0**. Examples use 3.11-compatible syntax, but no 3.11 runtime was exercised.
A task-owned PostgreSQL container used network none, tmpfs data, a read-only root and
one stage-local Unix-socket bind. It touched no application database. Fixture drivers
are necessary integration dependencies, not completion or adoption of K17.

All primary sources below were checked on the research date. **R** is a framework
requirement with a correctness, trust, ownership or existing-policy reason; **D** is
a recommended default under the stated condition; **O** is an optional technique.
Ecosystem behavior and framework policy are distinguished. Ordinary SQLAlchemy usage
is not an instruction to introduce FastAPI, PostgreSQL, Alembic or a repository layer.

## Coverage and instruction owners

| Area | Adopted decision and owner |
| --- | --- |
| 1. Architecture/dependencies | D: choose Core/ORM at the actual persistence seam; R: preserve core import/transaction ownership; [mapping](../../standards/sqlalchemy/mapping-contracts.md) |
| 2. Construction/idioms/patterns | D: native typed mappings and explicit assembly; O: mapped dataclasses/repositories/routines only for useful contracts |
| 3. Contracts/validation/errors | R: separate transport shape, operation rules, database integrity and public projection; mapping/[transactions](../../standards/sqlalchemy/sessions-transactions.md) |
| 4. State/concurrency/cancellation/lifetime | R: session per concurrent owner, commit boundary and cleanup; transactions/[async engines](../../standards/sqlalchemy/async-engines.md) |
| 5. Persistence/integration | R: flush is provisional, outer rollback is preserved and retries respect uncertain outcomes; transactions |
| 6. Testing/review | R: real backend for material persistence behavior and strict types for examples/tests; [verification](../../standards/sqlalchemy/migrations-verification.md) |
| 7. Security/operations/performance | R: bind values, protect connection/output context; D: measure load/query shape; [queries](../../standards/sqlalchemy/queries-loading.md)/async engines |
| 8. Versions/migration | R: preserve actual dialect/driver/SQLAlchemy matrix and review generated migration candidates; verification |

## Mapping and construction decisions

**Problem:** a preferred architecture becomes obligatory boilerplate.
The [unified tutorial](https://docs.sqlalchemy.org/en/20/tutorial/index.html) describes
ORM as an additional layer over Core. **D:** choose Core for SQL-shaped operations,
ORM for identity/relationship/unit-of-work needs, and keep their use inside the
existing adapter. **O:** a repository for an actual domain seam. **Alternative/cost:**
a small query module is simpler; redundant CRUD wrappers hide useful SQL contracts.
This architecture recommendation follows core policy, not a library mandate.

**Problem:** annotations or dynamic ORM construction are mistaken for validation.
[Typed declarative mapping](https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html)
and [native typing](https://docs.sqlalchemy.org/en/20/changelog/whatsnew_20.html) support
**D:** Mapped and mapped_column for 2.0 code. **R:** retain precise boundary types and
actual database nullability under Python policy. **O:**
[MappedAsDataclass](https://docs.sqlalchemy.org/en/20/orm/dataclasses.html) for a checked
constructor; **alternative/cost:** an explicit typed constructor/factory avoids its
dataclass semantics when they do not fit. Neither validates external data or guarantees
the pre-flush availability of a database-generated field.

**Problem:** one assignment callback is treated as protection for every writer.
[Validators](https://docs.sqlalchemy.org/en/20/orm/mapped_attributes.html) observe
normal attribute mutations, not all database population/direct DML. **R:** durable
constraints and current-state operation rules survive transport bypass; reason: core
invariants apply to CLI/worker entry too. **Alternative/cost:** application checks
improve feedback but cannot replace concurrent integrity. Use the database's own
[constraints](https://docs.sqlalchemy.org/en/20/core/constraints.html) deliberately.

**Problem:** Python graph behavior diverges from stored state.
[Cascades](https://docs.sqlalchemy.org/en/20/orm/cascades.html) and
[mutable values](https://docs.sqlalchemy.org/en/20/orm/extensions/mutable.html) support
**R:** define deletion and mutation ownership and verify persisted results.
**D:** explicit cascades matching domain lifetime; **O:** custom recursive mutation
tracking only when needed. **Alternative/cost:** replace a validated JSON value
rather than build deep instrumentation. ORM cascades do not automatically cover bulk
SQL, and database cascades require actual backend enforcement. These are relevant to
2.0; do not infer unchanged behavior across an upgrade.

## Session and transaction decisions

**Problem:** an ORM session is used as a global cache or shared transaction across tasks.
[Session basics](https://docs.sqlalchemy.org/en/20/orm/session_basics.html) define its
identity and mutable state. **R:** separate concurrent owners; **D:** reuse factories
at composition scope and create short-lived operation sessions. **Alternative/cost:**
explicitly managed sessions can fit a longer unit of work but need freshness/lifetime
control; contextual lookup does not add synchronization. A driver/pool option cannot
supply authorization or correct use-case scope.

**Problem:** flush/close is mistaken for a committed operation.
[Transaction management](https://docs.sqlalchemy.org/en/20/orm/session_transaction.html)
supports **R:** one clear owner for commit/rollback, success after the context exits,
and no hidden adapter commit inside a larger operation. **D:** context-managed sessions
and transaction blocks. **Alternative/cost:** commit-as-you-go is supported but requires
explicit partial-success semantics. Savepoints are **O** for intentional partial
recovery; their pre-flush and outermost-commit semantics must be accounted for.

**Problem:** returning a tracked entity performs I/O or changes meaning after commit.
[State management](https://docs.sqlalchemy.org/en/20/orm/session_state_management.html)
supports **D:** project loaded data into an owned result while inside the adapter.
**Alternative/cost:** returning mapped objects is acceptable only under an explicit
lifetime/loading contract; keeping sessions open can extend transactions and hide I/O.
**R:** distinguish flush failure recovery, expiration and fresh state. Merge is not
input validation or business conflict resolution. Known errors are classified at the
actual dialect/driver boundary; generic IntegrityError is not synonymous with duplicate.

**Problem:** identity tracking or optimistic versions are overclaimed as concurrency
protection. [Version counters](https://docs.sqlalchemy.org/en/20/orm/versioning.html)
apply to per-instance flushes, with explicit limits for bulk work. **O:** versioning,
locks or stronger isolation for a demonstrated invariant; **D:** a conditional update
for a single-row bound. **Alternative/cost:** a blind load/overwrite can lose decisions;
stronger protocols add conflicts/retries. Retry scope and uncertain-COMMIT reconciliation
remain database/application contracts. K15 owns PostgreSQL details when that backend
is selected; SQLAlchemy itself does not provide exactly-once external effects.

## Query, loading and resource decisions

**Problem:** row/scalar/cardinality assumptions leak through an adapter.
[SELECT](https://docs.sqlalchemy.org/en/20/orm/queryguide/select.html) supports **R**:
choose the actual result shape and explicit output fields. **D:** 2.0-style statements
for new 2.0 code; do not rewrite unrelated legacy Query usage. **Alternative/cost:**
column projection avoids entity hydration for reads; mapped entities retain lifecycle
features. Bind data values and constrain dynamic SQL structure. A result's first()
consumer does not add a query LIMIT.

**Problem:** lazy loading causes N+1 work or I/O after closing a session.
[Loader strategies](https://docs.sqlalchemy.org/en/20/orm/queryguide/relationships.html)
support **D:** select-in for suitable collection reads, joined loading for a suitable
small relation, and an explicit adapter loading contract. **O:** raise-on-access guards.
**Alternative/cost:** column projections avoid graph loading; joined collections
multiply rows and need unique(), while select-in adds queries/backend restrictions.
**R:** account for flush and expired/deferred column exceptions to no-implicit-I/O
claims. The async example proves complete detached DTOs, not a universal query budget.

**Problem:** bulk or streaming APIs are used as interchangeable faster syntax.
[ORM DML](https://docs.sqlalchemy.org/en/20/orm/queryguide/dml.html),
[execution options](https://docs.sqlalchemy.org/en/20/orm/queryguide/api.html), and
[performance guidance](https://docs.sqlalchemy.org/en/20/faq/performance.html) support
**O:** these paths for a measured workload. **R:** preserve synchronization, cascading,
result and connection-consumption contracts. **Alternative/cost:** ordinary unit of
work is simpler for a few entities; all() or incompatible collection loading can
defeat a stream's memory goal. SQL compilation caching is not data caching.

**Problem:** async and pooling are treated as automatic safety/performance switches.
[Async contracts](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html) support
**R:** await owned cleanup and avoid shared sessions/implicit attribute I/O.
**D:** explicit loading, often expire_on_commit=False for async output, with freshness
limits. **Alternative/cost:** sync code fits a sync service; async requires a compatible
driver and cancellation/loop lifetime. run_sync adapts SQLAlchemy calls, not arbitrary
blocking I/O. The fixture cancellation occurs after flush, not during COMMIT.

[Engines](https://docs.sqlalchemy.org/en/20/core/engines.html) and
[pooling](https://docs.sqlalchemy.org/en/20/core/pooling.html) support **R:** process/loop
and credential owners, aggregate connection budgets and no inherited live connections
after fork. **O:** pre-ping for stale checkout recovery; it cannot replay transactions.
**Alternative/cost:** use the pool appropriate to the host rather than universal sizing.
Disposal does not reclaim every active borrower. Driver TLS, tenant scope, secrets and
parameter logs remain separate trust concerns; engine construction does not prove them.

## Compatibility and schema decisions

**Problem:** metadata/autogeneration is treated as safe schema evolution.
[Metadata](https://docs.sqlalchemy.org/en/20/core/metadata.html) and
[Alembic candidates](https://alembic.sqlalchemy.org/en/latest/autogenerate.html) support
**R:** review migrations, old data, renames and deployment overlap. **D:** preserve one
migration owner; **O:** Alembic when chosen. **Alternative/cost:** create_all is enough
for a fresh fixture, not an existing-schema migration. Generated diffs require human
interpretation and cannot invent a correct backfill or recovery plan.

**Problem:** examples from different release lines silently change application behavior.
[2.0 migration](https://docs.sqlalchemy.org/en/20/changelog/migration_20.html) supports
**R:** staged compatibility review and execution on the target version. **D:** native
2.0 mappings; [legacy plugin status](https://docs.sqlalchemy.org/en/20/orm/extensions/mypy.html)
excludes treating that deprecated plugin as a modern strict-typing solution.
**Alternative/cost:** maintain an existing 1.4 compatibility contract until migration
is authorized; a local query edit need not trigger a global upgrade. The 2.1 release
candidate adds further behavior/dependency changes and is not a stable requirement.
Versioned sources describe different scopes, not contradictory universal advice.

## Adoption evidence and limits

The [command](../../standards/sqlalchemy/examples/transactional-command.md) and
[async projection](../../standards/sqlalchemy/examples/async-projection.md) share six
published file blocks: four Python files, dependency pins and analyzer settings.
Nine tests pass on the recorded PostgreSQL/driver matrix with warnings as errors;
strict mypy covers application and test code without bypasses. They exercise real
commits, duplicate-flush rollback, caller rollback, competing sessions, public detached
DTOs, rejected unplanned loads, parallel reads and cancellation after a flushed write.
The sync concurrency barrier coordinates competing attempts, not a measured lock wait.

The catalog adds one `sqlalchemy` profile depending on the existing Python profile;
it does not depend on PostgreSQL. Python-only, driver-only and database-only selection
must not load SQLAlchemy. The generic Python section points to the selected profile
by ID without adding a dangling mandatory link for Python-only installations. All
previous catalog definitions remain unchanged. Synthetic composition/artifact checks
and exact commands are recorded in the canonical plan's K16 result.

Not executed: SQLAlchemy 1.4/2.1, Python 3.11, another database, schema migration,
RLS/TLS deployment, external pooler, actual driver-call/COMMIT cancellation, uncertain
commit recovery, crash/failover, performance benchmark or native assistant adherence.
No result establishes universal driver behavior or production readiness. K17–K19 and
native adoption P3–P7 remain planned. Review is inline under the workspace adaptation.
