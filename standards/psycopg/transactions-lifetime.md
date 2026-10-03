# psycopg transactions and lifetime

Read for transaction ownership, commit/rollback, failure translation or savepoints.
General concurrency/isolation policy belongs to the PostgreSQL profile.

## Scope must match the operation

By default, even a SELECT starts a transaction. Avoid leaving a borrowed connection
idle in transaction. Autocommit is useful for independent statements or commands that
cannot run in a transaction, but does not make several statements one atomic operation.
Use an explicit transaction block for related effects.

In Psycopg 3, the connection context commits on normal exit, rolls back on exception
and closes the connection. A cursor context closes only the cursor. Closing a connection
with uncommitted work does not turn it into success. A pool connection context returns
the resource to its pool under that pool's transaction/reset contract.

Connection.transaction commits/rolls back its block, or uses a savepoint when a
transaction is already active. In particular, a prior SELECT on a default connection
can make a later transaction block nested: leaving it does not commit the outer work.
Use a clearly owned boundary, not an assumed connection state. The
[owned transaction example](examples/owned-transaction.md) starts from an owned
autocommit connection and keeps its helper free of commit/rollback calls.

For an adapter borrowing a connection, state the caller's active-transaction contract.
Do not hide a new connection, change autocommit or commit an outer use case. Savepoints
are optional for deliberately recoverable suboperations, not a default wrapper around
every query. Catch an expected error outside the block that must roll back; swallowing
it inside can leave an aborted transaction or change the intended outcome.

## Failure and cancellation boundaries

After a statement failure in a transaction, recover through the owning rollback or
savepoint before reuse. Use Psycopg exception classes/SQLSTATE and known constraint
metadata to classify expected errors; do not parse localized messages or classify
all IntegrityError instances as the same business conflict. Transport error mapping
must not expose SQL, parameters or credentials.

A statement result is provisional until the required commit succeeds. An error on
connection loss around COMMIT can leave the outcome unknown. Reconcile a durable
operation identity before replay; retrying only the failed statement or replaying
external effects is not a recovery strategy. Use the existing bounded full-transaction
retry policy for classified serialization/deadlock failures where appropriate.

Cancellation requests and application timeouts have separate completion/cleanup
semantics. Verify the actual driver/libpq cancellation path when changing it, allow
owners to unwind, and keep rollback/reset failures observable. A canceled client
operation is not proof that a database write never committed. Do not add custom
transaction frameworks or retry schedulers for a small driver integration.

Basis: [transaction contexts](https://www.psycopg.org/psycopg3/docs/basic/transactions.html),
[connection API](https://www.psycopg.org/psycopg3/docs/api/connections.html), and
[structured errors](https://www.psycopg.org/psycopg3/docs/api/errors.html).
