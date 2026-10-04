# SQLAlchemy async work and engines

Read when configuring an engine/pool, using AsyncSession or changing resource/security
behavior. General cancellation and blocking-work rules stay in the Python profile.

## Engine, pool and driver ownership

Create engines at application/process startup or another explicit composition owner,
not for each request. Select an explicit dialect/driver URL and a compatible sync or
async engine. SQLAlchemy is not the database driver, and async syntax alone does not
make a synchronous driver nonblocking. Use Core/Session synchronous paths for a
synchronous service; adopt async only for a supported workload and driver.

For 2.1 asyncio use, declare `sqlalchemy[asyncio]`: base installation no longer
includes greenlet. In 2.0 its automatic installation is platform-dependent; the
extra explicitly requests it. Keep the selected async database driver as well.
For PostgreSQL, bare `postgresql://` selects psycopg2 in 2.0 and psycopg 3 in 2.1.
Use `postgresql+psycopg2://`, `postgresql+psycopg://` or the chosen async-driver URL
to preserve an intentional driver choice; check it against the engine mode.

Budget pool_size, overflow, checkout timeout and connection count across processes/
replicas. Validate options against the selected pool; not all engines use QueuePool.
Pre-ping can identify stale connections at checkout but cannot repair a failed
transaction or replay a lost write safely. Closing a pooled connection typically
returns it to the pool, so session state and reset behavior need an explicit contract.

Do not share live pooled connections across forked processes. Recreate/dispose the
child's pool under the documented multiprocessing recipe. Async engines/pools also
have event-loop affinity; do not move a pooled engine across unrelated loops without
a supported lifetime/reset strategy. Stop users before disposing engines; disposal
does not forcibly reclaim all checked-out connections. Await AsyncEngine.dispose().

## Async operation scope

Use one AsyncSession per concurrent task; a shared async_sessionmaker is a factory,
not shared transaction state. Await database work within owned async contexts. For
output needed after commit, `expire_on_commit=False` is a common async choice, but it
does not load missing relations or keep values fresh indefinitely. Prefer explicit
loading/projection; AsyncAttrs.awaitable_attrs or explicit refresh can support an
intentional attribute I/O boundary.

`run_sync` adapts SQLAlchemy synchronous callables through its async integration; it
is not a general thread offloader for filesystem/network work. Metadata fixture DDL
can use connection.run_sync. Ordinary blocking calls inside that function still block
the event loop. Avoid broad cascades that expire related state unexpectedly in an
async read path; configure the actual ownership behavior.

On cancellation, allow transaction/resource owners to unwind and propagate the
cancellation. A request timeout is not proof of database rollback, especially around
COMMIT; use the application's uncertain-outcome policy. Check driver cancellation
and connection reuse for the actual failure scenario. A test canceled after flush
is not evidence for a network loss during commit. Close streaming results in their
own lifetime before releasing the connection; background tasks acquire new resources.

## Connection and data trust

Use the established credential provider and driver TLS settings; engine construction
does not prove peer verification or database authorization. Build URLs with URL.create
when credentials contain reserved characters; do not log the resulting secrets.
`echo`/statement parameter logs may expose data; use redaction/hide_parameters where
appropriate and check exception handling too. ORM filters alone are not tenant
authorization, and a shared identity map must not cross unrelated authorization scopes.
Use the selected database profile for actual role/RLS/operational rules when applicable.

Basis: [engines](https://docs.sqlalchemy.org/en/20/core/engines.html),
[pooling/disconnects/forking](https://docs.sqlalchemy.org/en/20/core/pooling.html),
[async contracts](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html),
[dialects](https://docs.sqlalchemy.org/en/20/dialects/index.html),
[2.1 asyncio installation](https://docs.sqlalchemy.org/en/21/orm/extensions/asyncio.html), and
[PostgreSQL driver change](https://docs.sqlalchemy.org/en/21/changelog/migration_21.html#default-postgresql-driver-changed-to-psycopg-psycopg-3).
