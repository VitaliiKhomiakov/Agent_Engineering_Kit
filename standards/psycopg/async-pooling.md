# psycopg async work and pooling

Read for concurrent work, pool/service lifetime or a connection security boundary.
Use existing Python cancellation/resource and PostgreSQL operational rules.

## Concurrency is not transaction isolation

Connections support coordinated use from threads/tasks, but operations on one
connection serialize and its cursors share one session/transaction. A rollback or
error affects that shared transaction. Cursors themselves are not shared concurrent
work objects. Give independent operations separate connections; do not confuse
thread safety with parallel SQL or isolated business work. Do not inherit live
connections into forked processes.

Use AsyncConnection with awaited connect/execute/fetch and async contexts when the
application actually needs async I/O. `async with await AsyncConnection.connect(...)`
reflects that connect is awaitable; cursor creation itself is not. Preserve the
sync approach for a synchronous application instead of wrapping it in async syntax.
Check platform/event-loop and DNS behavior for the installed driver version.

## Pool ownership and budgets

`psycopg_pool` is separately versioned and optional. A one-off script can own one
connection; a service can benefit from bounded reuse. Bootstrap owns open/readiness/
close; request/operation code owns a borrowed connection. Set startup behavior
explicitly rather than relying on a changing constructor default. For async pools,
use the documented explicit open/context path and await readiness when startup must
establish database availability.

Bound aggregate connections across processes, queued acquisition and wait budgets.
Checkout timeout is not statement timeout. Configure/reset callbacks must return
connections in the state required by the pool; do not leak tenant/session settings
between borrowers. Health checks cannot repair a transaction lost after checkout.
Exhaustion and shutdown need observable outcomes, not an unbounded retry loop.

When SQLAlchemy already owns a pool, use its documented driver integration. Combining
pools adds lifetime/reset complexity; do it only for a concrete integration need with
version-supported return semantics. Psycopg pool APIs are not SQLAlchemy Session APIs.
Keep slow external calls and unconsumed streams out of unnecessarily long checkouts.

## Trust and observability

Use the project's credential provider, PostgreSQL role and actual libpq TLS policy.
For remote libpq connections, verify-full validates trust and hostname; merely using
SSL or creating a pool does not establish those checks. Build connection parameters
through supported conninfo/keyword APIs; do not concatenate untrusted DSN fragments.
Do not log DSNs, parameter values or raw exception payloads by default.

Database privileges and application authorization remain separate. A row factory,
prepared query or correctly quoted identifier cannot authorize a tenant operation.
Measure acquisition wait, transaction duration and relevant errors before tuning pool
sizes or adopting pipeline/COPY. Keep diagnostic data free of sensitive payloads.

Basis: [concurrency/async](https://www.psycopg.org/psycopg3/docs/advanced/async.html),
[pools](https://www.psycopg.org/psycopg3/docs/advanced/pool.html),
[pool API](https://www.psycopg.org/psycopg3/docs/api/pool.html), and
[libpq TLS](https://www.postgresql.org/docs/18/libpq-ssl.html).
