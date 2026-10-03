# psycopg engineering practices: evidence and adoption

Research started **2026-09-21**, completed **2026-09-22**. Scope: K17 of the
[practice plan](../plans/2026-09-21-engineering-practices.md). The
[entry](../../standards/psycopg.md) owns four conditional sections and two short
examples. The user explicitly requested proportionate instruction checks after K16:
no new example application, server or broad test suite is built in this stage.

## Version and evidence contract

[Release notes](https://www.psycopg.org/psycopg3/docs/news.html) identify **3.3.6** as
current release. The moving manual's **3.3.7.dev1** banner is not a stable-version
recommendation. Instructions use established 3.x contracts and check feature-specific
requirements separately. `psycopg_pool` has its own package/version and is optional;
no pool runtime is selected by these examples.

Reused the existing K16 temporary environment without installing dependencies:
Python **3.12.3**, psycopg/binary **3.3.6**, bundled libpq **18.6** (180006), mypy
**2.1.0**. Client libpq version is not a server version. This stage made no database
connection; SQL execution is deliberately not claimed. Prior-stage database evidence
does not validate these new snippets. Primary sources were checked during this research
across the date boundary; the filename retains its actual start date.

Strengths: **R**, a framework requirement justified by correctness/trust/ownership or
existing policy; **D**, a recommended default in the named situation; **O**, optional
when its cost is justified. Library semantics are facts, distinct from framework policy.

## Coverage and owners

| Area | Adopted decision and owner |
| --- | --- |
| Architecture/dependencies | D: a small driver adapter, preserving Python/core boundaries; no forced repository or ORM |
| Idioms/construction | D: bound execute and explicit resource contexts; O: pool/COPY/pipeline for a real requirement |
| Typed contracts/validation/errors | R: named rows, separate input/domain/database rules and structured failures; [queries](../../standards/psycopg/queries-contracts.md) |
| State/concurrency/cancellation/lifetime | R: transaction and connection owners; [lifetime](../../standards/psycopg/transactions-lifetime.md), [async/pool](../../standards/psycopg/async-pooling.md) |
| Persistence/integrations | R: commit before success, caller transaction preserved, uncertain outcome handled; lifetime; PostgreSQL owns durable invariants |
| Testing/review | D: artifact checks and narrowly verified snippets for instructions; real database checks for affected application semantics; [verification](../../standards/psycopg/compatibility-verification.md) |
| Security/operations/performance | R: separate data/SQL structure, authorization, credentials and budgets; O: measured bulk/prepared techniques |
| Versions/migration | R: actual Python/driver/libpq/server/pool matrix and explicit Psycopg 2 migration; verification |

## Queries and boundary decisions

**Problem:** SQL construction confuses identifiers with data. **R:** bind values and
compose only reviewed structure, because string interpolation crosses a trust boundary.
[Parameters](https://www.psycopg.org/psycopg3/docs/basic/params.html) and
[SQL tools](https://www.psycopg.org/psycopg3/docs/api/sql.html) define the distinction.
**D:** a fixed query, or a small allowed identifier set where variation is real.
**Alternative/cost:** unrestricted dynamic builders add authorization and escaping
obligations; quoted names are still names the caller might not be permitted to access.
Server binding restrictions on utility statements do not justify unsafe interpolation.

**Problem:** typed rows are mistaken for validated input or guaranteed live schema.
[Typing](https://www.psycopg.org/psycopg3/docs/advanced/typing.html) supports **D**:
a named class-row contract with explicit selected columns. **R:** handle absence and
validate at the true boundary under Python policy. **Alternative/cost:** tuples can
suffice locally, but unstructured rows should not leak into public contracts. A dataclass
constructor does not enforce annotations. [Adaptation](https://www.psycopg.org/psycopg3/docs/basic/adapt.html)
requires deliberate exact-number, time, array and JSON semantics; Jsonb is not a schema
validator. Business rules depending on current state remain operation/database rules.
These choices apply to the selected 3.x API, not an automatic Psycopg 2 conversion.

**Problem:** bulk/performance features become default infrastructure.
[Cursors](https://www.psycopg.org/psycopg3/docs/advanced/cursors.html),
[COPY](https://www.psycopg.org/psycopg3/docs/basic/copy.html),
[pipeline](https://www.psycopg.org/psycopg3/docs/advanced/pipeline.html), and
[preparation](https://www.psycopg.org/psycopg3/docs/advanced/prepare.html) support
**O:** select the feature for measured volume/round-trip needs. **Alternative/cost:**
ordinary execute is simpler for small work; streaming retains resources, COPY has
mode-specific restrictions and pipeline adds synchronization/error handling. Prepared
statement compatibility depends on the actual pooler/client matrix, not a universal
“all poolers work” or “all poolers fail” rule. No performance claim was benchmarked.

## Transactions and resource decisions

**Problem:** a cursor closes but an implicit transaction remains open, or a savepoint
is mistaken for the outer commit. [Transactions](https://www.psycopg.org/psycopg3/docs/basic/transactions.html)
and [connection API](https://www.psycopg.org/psycopg3/docs/api/connections.html) support
**R:** explicit ownership and success after the correct commit boundary. **D:** use
contexts with known starting state. **Alternative/cost:** autocommit suits independent
statements; related effects still need a transaction. A prior read on a default
connection can make transaction() nested. Helpers preserve the caller's transaction;
savepoints are **O** for intended partial recovery, not automatic per-query wrappers.

**Problem:** a catch hides an aborted transaction or retries an uncertain write.
[Structured errors](https://www.psycopg.org/psycopg3/docs/api/errors.html) support **R**:
classify known SQLSTATE/constraint outcomes at the adapter, then recover through the
transaction owner. **Alternative/cost:** propagate an unknown failure instead of
inventing a public duplicate/conflict meaning. PostgreSQL/application policy owns
bounded complete-operation retries and uncertain-COMMIT reconciliation. No driver
context can undo external effects or prove a timed-out commit did not happen.

**Problem:** shared connection safety is mistaken for independent transactions.
[Concurrent operations](https://www.psycopg.org/psycopg3/docs/advanced/async.html) explain
serialized commands and shared session state. **R:** independent concurrent business
operations get independent connections. **D:** match sync/async usage to the actual
application. **Alternative/cost:** a shared connection can coordinate related work,
but is neither parallel query execution nor isolation. Cancellation and fork/loop
lifetime require their documented owner; no async cancellation was tested here.

**Problem:** pooling obscures startup, reset and capacity. [Pool guidance](https://www.psycopg.org/psycopg3/docs/advanced/pool.html)
and [API](https://www.psycopg.org/psycopg3/docs/api/pool.html) support **D**: explicit
startup/readiness/shutdown for a service, bounded borrowing and clean return state.
**O:** pooling itself; a one-shot script can own one connection. **Alternative/cost:**
stacking it with SQLAlchemy pooling adds ownership/reset complexity. Check the separately
versioned integration APIs rather than mandating it. Health checks do not repair a
mid-transaction disconnect. **R:** credentials, tenant context and native TLS settings
remain explicit trust boundaries; PostgreSQL security policy owns the broader rules.

## Compatibility and adoption decisions

**Problem:** the package version alone conceals native-library and lifecycle changes.
[Installation](https://www.psycopg.org/psycopg3/docs/basic/install.html) supports **D**:
choose binary/local-C/Python mode for deployment constraints, with explicit libpq
provenance. **Alternative/cost:** wheels simplify setup but bundle native dependencies;
local builds require system maintenance; Python mode still needs libpq. Release fixes
can depend on libpq capabilities, so record the full matrix. No installation change
is required for an ordinary application edit.

[Psycopg 2 differences](https://www.psycopg.org/psycopg3/docs/basic/from_pg2.html) support
**R:** deliberate migration of context closure, binding/adaptation and connection/pool
ownership. **Alternative/cost:** retain a supported existing integration until migration
is authorized; a renamed import is insufficient. Newer optional syntax remains gated
by its Python/driver requirements. Moving-manual and release-note scopes explain
version differences; they are not competing blanket recommendations.

The new profile depends on Python and PostgreSQL instruction profiles: Psycopg's API
is PostgreSQL-specific, so these rules are relevant even without a declared server
version. This dependency adds guidance, not a synthetic metadata fact. Conversely,
Python/PostgreSQL/SQLAlchemy presence alone does not select psycopg. Existing metadata
recognizes `psycopg` including extras; psycopg2-only projects are not silently matched.
The PostgreSQL entry references the conditional profile by ID to avoid a mandatory
link in driver-free bundles. All previous catalog definitions remain unchanged.

## Checks and limits

Two small separate snippets illustrate a typed parameterized lookup and an owned
transaction with a borrowing helper. Syntax/strict types cover both; a tiny offline
probe checks query composition, value placeholders and identifier escaping. No test
classes, fixtures, application scaffold, dependency installation or server were added.
SQL text/schema/transaction assumptions were reviewed against the manual, not executed.

Existing rule tests and focused generated-bundle checks verify selection, portable
resources, native entry routes and independent opening. Exact commands/results and
baseline are in the canonical plan. These are instruction-delivery checks, not native
model adherence or token-saving evidence. No query/row decoding, commit/rollback,
async/pool behavior, migration, TLS deployment, concurrency or load was runtime-tested.
K18–K19 and native adoption P3–P7 remain planned; author review follows the workspace
adaptation and the user's narrower verification preference.
