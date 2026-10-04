# Python: execution, state, and resource lifetime

Read when changing async work, threads/processes, shared state, resource handling,
transactions, or external calls. Return to the [Python entry](../python.md).

## Choose the execution model for the work

Sequential synchronous code is the default when it meets the contract. Use
`asyncio` for overlapping awaitable I/O in an async application, not simply to
rename functions `async def`. Blocking network, disk, SDK calls, and CPU-heavy
loops block the event loop if executed there. Await every owned coroutine or
give its task an explicit supervisor and lifetime.

Use an async-native adapter where available. `asyncio.to_thread` can isolate
blocking I/O if the library and objects are safe to use in that thread; bounding
awaiters alone does not necessarily bound work still running after cancellation.
Cancelling the await does not terminate an already executing thread. Use the
underlying client's deadlines/cooperative stop mechanism, bound submissions, and
keep resources alive until actual work ends. A task timeout is not a hard limit
on side effects.

For measured CPU bottlenecks, consider a process pool or a suitable native
operation that releases the GIL. Account for serialization, process startup,
memory, and platform start methods. Standard GIL-enabled CPython generally does
not parallelize CPU-bound Python bytecode across threads. Optional free-threaded
builds change that tradeoff, not the need for synchronization; check interpreter,
extensions, and benchmarks. Do not choose them through an incidental upgrade.

## Related async work and cancellation

- On Python 3.11+, prefer `TaskGroup` for related tasks whose results are all
  required: it joins children and cancels siblings on a non-cancellation failure.
  Treat resulting exception groups deliberately. Sequential awaits are simpler
  for dependent work. `gather` has different failure behavior: with its default
  settings a child's failure does not cancel the remaining children.
- Bound fan-out and queued work. A semaphore limits active sections but a task
  created for every item can still exhaust memory. Use a bounded queue/fixed
  workers, batches, or sequential iteration when appropriate. Define result
  order and partial-success semantics before parallelizing effects.
- Scope `asyncio.timeout`/`timeout_at` to the operation's budget and catch its
  `TimeoutError` outside the context. Cleanup and cooperative cancellation can
  extend elapsed time. Do not reset the full end-to-end budget at every retry.
- Use `try/finally` or context managers for cleanup. Propagate `CancelledError`
  after necessary cleanup; it inherits from `BaseException`. Swallowing it can
  break structured concurrency. Do not use `shield` as a generic cure: the caller
  can still be cancelled and the shielded work still needs an owner and cleanup.
- A request's tasks normally finish with that request. Longer-lived work needs
  a supervisor that retains task references, observes errors, and drains/stops
  work at shutdown. Use a durable job mechanism only when its delivery/recovery
  contract is actually required; detached tasks provide no such guarantee.

The optional [two-source example](examples/concurrency.md) demonstrates a small
fixed fan-out and cleanup on failure, timeout, and caller cancellation. It does
not provide a worker pool, retry loop, or durable job runner.

## Ownership and cleanup

- Own resources at a visible scope using `with`, `async with`, or `try/finally`.
  Verify what a context manager actually does: transaction handling, releasing
  a pooled resource, and closing a connection are distinct operations. For
  example, a `sqlite3.Connection` context manages a transaction, not connection
  closure. Do not rely on `__del__`, garbage collection, or process exit to clean
  up operational resources.
- Prefer ordinary nested contexts for a fixed set of resources. `ExitStack` or
  `AsyncExitStack` helps when acquisition is conditional or variable; register
  cleanup as resources are acquired so partial setup also unwinds correctly.
- Bootstrap owns long-lived clients/pools and closes them after their users stop.
  Each operation owns its short-lived cursor/session/transaction where applicable.
  Do not pass request-owned mutable resources to work that outlives the request.
- Protect compound updates to shared state or give state one owner. The GIL and
  individual container operations do not make a business transition atomic.
  `asyncio.Lock` coordinates tasks on its loop, not OS threads or other processes;
  use the appropriate synchronization or database constraint for the boundary.
  Await points can expose partially changed state; arrange mutations deliberately.
- Avoid mutable global caches/configuration without a clear lifetime and invalidation
  policy. Context variables can carry scoped correlation metadata, not substitute
  for explicit business dependencies or make a mutable object safe to share.

## Persistence and external integration

Keep transaction ownership at the use-case boundary that requires atomicity and
use the installed driver/ORM's documented context and commit behavior. An adapter
must not unexpectedly commit one step of a larger transaction. Rollback and close
are separate obligations; don't share a mutable transaction across concurrent
tasks without an explicit library guarantee and a coherent transaction contract.
Use parameter binding for values, and allowlisted/driver-supported composition
for identifiers; interpolation is not parameterization.

Map external records/errors at the adapter boundary. Repository abstractions are
conditional design tools, as described in [structure](structure.md); detailed
ORM/driver policies apply only when those technologies are present. Python alone
does not select SQLAlchemy, psycopg, or a database for a project.

When SQLAlchemy is present or explicitly selected, use its separate `sqlalchemy`
profile for mapping, Session, loading and engine details. The Python profile does
not select it automatically, and SQLAlchemy does not imply PostgreSQL. Keep the
transaction ownership above; ORM-specific mechanics belong to the selected profile.
For Psycopg 3, use the separate `psycopg` profile for adaptation, connections and
pools. The `postgresql` profile owns PostgreSQL constraints, isolation and migrations
when that database is used; an ORM alone does not select it.

For outbound operations define connect/read/overall budgets supported by the
client, response-size limits where needed, and who consumes/closes responses.
Preserve TLS verification and constrain user-controlled destinations when that
boundary permits outbound network access. Retry only failures for which replay
is safe within the remaining budget; a timeout after a write can leave its result
unknown. A database transaction cannot roll back a remote effect. Use an explicit
idempotency/reconciliation or outbox design only when the use case needs it.

Sources: [asyncio tasks](https://docs.python.org/3.11/library/asyncio-task.html),
[asyncio development](https://docs.python.org/3.11/library/asyncio-dev.html),
[executor cancellation](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.Future.cancel),
[free threading](https://docs.python.org/3.14/howto/free-threading-python.html),
[context managers](https://docs.python.org/3.11/library/contextlib.html),
[DB-API](https://peps.python.org/pep-0249/),
[SQLite lifetime](https://docs.python.org/3.11/library/sqlite3.html#how-to-use-the-connection-context-manager).
Resource and effect ownership are framework requirements; execution mechanisms
and abstractions remain conditional choices.
