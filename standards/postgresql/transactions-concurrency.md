# PostgreSQL transactions and concurrency

Read for multi-statement operations, conflicting writes, retries, locks or job claims.

## Atomic operations and isolation

Keep transaction ownership explicit in the use case. Choose isolation and locks
for the demonstrated concurrency requirement; do not raise isolation globally
or add locks without a scenario that requires them.

Use one connection for the transaction; a pool call per statement may use different
sessions. Keep transactions short, without user think time or slow remote effects.
A successful statement/RETURNING is provisional until COMMIT succeeds. Roll back a
failed transaction before reusing its connection; a savepoint is an intentional
partial-recovery contract, not permission to hide failure.

For a single-row bound, prefer an atomic conditional UPDATE and inspect its result.
In Read Committed a waiting updater rechecks its condition against the updated row;
a prior SELECT followed by an unconditional overwrite can lose a business decision.
The [reservation example](examples/atomic-reservation.md) connects a decrement and
receipt insert in one statement. In more complex operations, lock the relevant rows
before making the protected decision, or use Serializable with a complete retry
contract. Repeatable Read stabilizes a snapshot but does not eliminate write skew.
Read Committed statements can see different committed snapshots within one transaction.

## Conflicts and retries

Where serialization failure handling is required, retry the complete transaction
under the application's bounded retry/idempotency policy. Do not retry only the
failing statement or duplicate external effects.

Classify `40001` (serialization failure), `40P01` (deadlock), lock unavailability,
statement cancellation and known integrity conflicts separately. Retrying a deadlock
can be appropriate after rollback, with bounded attempts/backoff/deadline and an
observable final outcome. Do not retry every unique violation or every SQL error.
Recompute decisions and reads in a fresh transaction. A lost connection around COMMIT
has an uncertain outcome: reconcile a durable operation identity before replaying.

A unique request key alone is not the full idempotency contract. Define its tenant
scope, payload agreement and stored result. `ON CONFLICT DO NOTHING` after debiting
stock can suppress the receipt conflict while retaining the debit. An atomic upsert
solves its stated insert/update conflict, not every multi-row invariant. Keep external
calls outside replayable work; when reliable publication is required, persist an
outbox record in the transaction and design consumer deduplication/dispatch separately.

## Lock scope and lifetime

Acquire multiple locks in a consistent order. Row locks do not lock nonexistent
rows or arbitrary predicates. Set operation-appropriate lock/statement deadlines
and keep cleanup inside the connection owner. Advisory locks require all cooperating
writers to follow the same key protocol; transaction-scoped locks are usually easier
to contain in pooled work than session-scoped locks.

Use `SKIP LOCKED` for deliberately competing queue consumers, not a consistent
report or an arbitrary stock check. Claim and transition work atomically, then define
lease expiry, crash recovery and duplicate processing. It provides neither fairness
nor exactly-once execution. `NOWAIT` is an explicit immediate-refusal option.
Do not add either for uncontended work that a conditional update already protects.

Basis: [16 isolation](https://www.postgresql.org/docs/16/transaction-iso.html),
[18 isolation](https://www.postgresql.org/docs/18/transaction-iso.html),
[retry scope](https://www.postgresql.org/docs/18/mvcc-serialization-failure-handling.html),
[locks](https://www.postgresql.org/docs/18/explicit-locking.html),
[upserts](https://www.postgresql.org/docs/18/sql-insert.html), and
[locking reads](https://www.postgresql.org/docs/18/sql-select.html).
