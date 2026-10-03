# Doctrine ORM unit of work and transactions

Read for EntityManager lifetime, flush, transaction failure, concurrency or
persistence-related effects. For standalone DBAL transactions, use
[queries and DBAL](queries-dbal.md#dbal-transactions).

## Own the persistence context

An EntityManager owns an identity map and tracks managed changes. Loading a
known identity can return the same object, including its local changes; a finder
is not a refresh operation. Do not share a mutable manager across unrelated
requests, overlapping tasks or workers' independent jobs.

`persist()` registers new work; it does not mean an INSERT has completed. Managed
objects normally need no repeated `persist()`. `flush()` synchronizes the pending
unit of work, not just the last entity passed to a repository. Do not hide a flush
in every repository save. Define the operation that owns flushing and its success
boundary; a remaining outer transaction still needs to commit.

`clear()` detaches all managed objects and abandons unflushed tracking. Close or
reset the context at its actual framework/job boundary; re-acquire dependencies
that hold an old manager after reset. Keep identifiers or independent snapshots
across jobs, not serialized managed entities or lazy proxies. Batches need explicit
flush/clear boundaries; do not clear unrelated pending work to reduce memory.

These behaviors follow [working with objects](https://www.doctrine-project.org/projects/doctrine-orm/en/3.7/reference/working-with-objects.html).
The [ORM example](examples/orm-unit-of-work.md) distinguishes an identity-map hit
from a persisted reload.

## Transaction boundary and failure

Use the simplest boundary that covers the operation's database changes. An
ordinary flush already wraps its writes; explicit demarcation is useful when
reads/locks, several flushes or DBAL writes must participate in one transaction.
Keep the transaction short; do not hold it across user interaction or unrelated
network calls.

- ORM `wrapInTransaction()` flushes before committing and closes the manager on
  failure. DBAL `transactional()` does not flush or reset an EntityManager.
- After failed ORM flush/transaction, discard the closed manager. Create/reset
  through the application's infrastructure and load fresh entities for new work.
  Database rollback does not rewind PHP objects; a detached object's values or
  generated identifier do not prove a successful write.
- If using explicit begin/commit/rollback, preserve those cleanup guarantees on
  all failures, including commit. Do not catch an error and return success while
  required writes were rolled back.
- ORM and direct DBAL writes are atomic together only when they participate in
  the same connection transaction. Direct SQL can leave managed state stale;
  explicitly reconcile or discard it without losing unrelated pending changes.
  Separate connections/databases are not one local atomic operation.
- Keep absence, a refused business operation, a recognized constraint conflict
  and infrastructure failure distinct. Translate only understood failures at
  the adapter boundary; a generic integrity exception is not always the expected
  business duplicate. Preserve the underlying cause in infrastructure diagnostics.

[Transactions and concurrency](https://www.doctrine-project.org/projects/doctrine-orm/en/3.7/reference/transactions-and-concurrency.html)
and the versioned [EntityManager implementation](https://github.com/doctrine/orm/blob/3.7.1/src/EntityManager.php)
define failure semantics. Nested DBAL savepoints do not make an inner return a
committed business success; see [DBAL ownership](queries-dbal.md#dbal-transactions).

## Concurrency decisions

An entity method can protect the object it sees; another transaction may hold a
stale copy. A read/check/write sequence alone is not concurrency protection.

| Need | Candidate | Cost and verification |
| --- | --- | --- |
| Detect competing edits | ORM version field and optimistic locking | Handle conflict; preserve the user's expected version across requests |
| Change one row only if current state permits it | Conditional UPDATE and affected-row contract | Own the SQL predicate, constraints and any ORM state reconciliation |
| Protect a read-dependent critical section | Supported pessimistic lock inside an explicit transaction | Lock waits, ordering and deadlocks need target-database tests |

Choose for actual contention and semantics; do not add every mechanism to every
entity. Keep required uniqueness/referential constraints in the database. An
optimistic field does not protect unrelated rows or SQL that bypasses its check.

Retry only recognized transient failures when repeating the complete operation
is valid. Bound attempts and elapsed time, reload state and reapply business rules;
never retry only the failed SQL against stale objects. External effects and
ambiguous commit outcomes need an idempotency/reconciliation design, not a blanket
retry of all exceptions.

## Lifecycle events and external effects

Entity callbacks may handle small lifecycle-local work. Keep whole use cases and
network orchestration out of callbacks, and avoid re-entering flush from flush
listeners. `postPersist`/`postUpdate` and `postFlush` are not a guarantee that an
outer transaction has committed.

When durable message publication must accompany a write, use the project's
existing reliable handoff, such as an outbox with appropriate replay handling.
A local database transaction cannot roll back an email or remote API call. Do not
introduce a message bus/outbox when the operation has no such delivery requirement.
See [ORM events](https://www.doctrine-project.org/projects/doctrine-orm/en/3.7/reference/events.html)
and, only with Symfony integration, [runtime effects](../symfony/runtime-effects.md).
