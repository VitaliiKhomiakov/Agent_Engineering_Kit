# SQLAlchemy sessions and transactions

Read for writes, operation lifetime, rollback, savepoints or concurrency conflicts.

## The owner defines success

A Session tracks identities and pending changes and can acquire a connection lazily.
It is not a query cache or safe shared mutable state. Keep engine/session factories
at their configured lifetime; create sessions per operation/thread and AsyncSessions
per concurrent task. `scoped_session` provides lookup/scoping, not synchronization.

Use an explicit transaction boundary for the operation: `sessionmaker.begin()` owns
session plus commit/rollback/close, while `with Session(...)` alone only scopes the
session. `Session.begin()` scopes its transaction. An adapter participating in an
outer use case must not commit it. Autobegin can start a transaction on a read before
an explicit begin; structure the operation rather than blindly nesting begin calls.

Flush sends pending work but does not commit. ORM queries can autoflush, so an
apparently read-only statement can expose pending invalid writes. `no_autoflush` is
for deliberate object assembly, not a substitute for constraints. Commit flushes
pending changes even when autoflush is disabled. Report success only after commit
has completed, including errors raised while leaving its context manager.

With autoflush enabled, 2.0 distinguishes ORM-enabled execution from a plain
textual statement. In 2.1, `Session.execute()` also autoflushes before Core/textual
statements, including `text("SELECT ...")`; pending writes can fail before that
SELECT runs. This concerns Session execution, not an independent Core Connection.
Explicit autoflush controls remain available; they do not suppress commit's flush.

A failed flush requires rollback before further use of that Session; let the owner
unwind or explicitly recover. Do not catch an integrity error and continue in an
aborted transaction. Close and rollback are distinct obligations. By default commit
expires ORM state, and rollback expires retained state; later attribute access may
issue SQL. Build owned result values before closing and return them only after the
commit boundary. Disabling expiration requires an explicit freshness policy.

## Partial recovery and integration

`begin_nested()` uses a SAVEPOINT and flushes pending state before establishing it.
Keep only the intended recoverable work inside the savepoint. In 2.0, Session.commit
commits the outermost transaction; finish the nested transaction through its own
context/handle. Savepoints do not isolate external effects or authorize accepting a
partial business operation. The simpler default is one atomic operation with rollback.

Classify expected integrity/concurrency errors through the established dialect/driver
adapter using SQLSTATE/known constraint details where available. SQLAlchemy wrappers
alone do not make every IntegrityError a duplicate business key. Preserve causality;
map public errors without leaking statement parameters or credentials.

Retry a complete transaction only for classified replay-safe failures within a bounded
budget. Reacquire a suitable session and recompute decisions; uncertain COMMIT needs
operation-identity reconciliation. Avoid remote calls inside retryable transactions.
When reliable publication requires an outbox, persist its record in the same unit
of work and give dispatch/deduplication their own owner.

## Concurrency is a database contract

For a single-row condition, an atomic conditional UPDATE may be simpler than loading
an object and locking it. Use actual isolation/locking for broader invariants. A
version counter can detect stale per-instance flushes, but does not automatically
protect bulk updates or cross-row write skew. Identity-map reuse is not evidence
of fresh database state. Verify concurrent outcomes with independent connections.

The [command example](examples/transactional-command.md) demonstrates typed values,
conditional DML, receipt flush, outer rollback and a result after commit. A unique
request key there is not a complete idempotency protocol.

Basis: [session basics](https://docs.sqlalchemy.org/en/20/orm/session_basics.html),
[transaction/savepoint contracts](https://docs.sqlalchemy.org/en/20/orm/session_transaction.html),
[version counters](https://docs.sqlalchemy.org/en/20/orm/versioning.html), and
[2.1 autoflush changes](https://docs.sqlalchemy.org/en/21/changelog/migration_21.html#session-autoflush-behavior-simplified-to-be-unconditional).
