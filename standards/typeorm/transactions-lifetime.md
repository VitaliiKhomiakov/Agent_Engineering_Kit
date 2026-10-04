# TypeORM transactions and lifetime

Read for persistence, transaction boundaries, concurrency and durable effects.
Use the [entry](../typeorm.md); database-specific locking/isolation belongs to the
selected database profile.

## Explicit persistence and ownership

A DataSource normally owns a shared pool for an application lifetime. Initialize
and destroy it under one owner; do not connect/disconnect per HTTP request. A
QueryRunner leases one connection and must be released in `finally`, including
failure paths. Do not destroy a shared pool to end one transaction.

Changing an object does not schedule a later global flush. Await `save`/explicit
SQL at the adapter boundary. The transaction internal to one save does not include
an earlier read, another repository call or a remote request. TypeORM does not
guarantee that two loads of one row return the same JavaScript object.

For `save` updates, omitted/`undefined` properties are skipped; assigning undefined
does not clear a stored value. A permitted clear operation must persist explicit
`null` to a nullable column through the named domain/adapter contract. Reload to
verify the stored result, including unchanged omission and rejected null for a
required column. `invalidWhereValuesBehavior` governs filters, not this write
contract. Verify other update/upsert APIs and drivers separately.

For a multi-step atomic operation, use `dataSource.transaction(async manager => ...)`
or an explicitly owned QueryRunner transaction. Every participating read/write
must use that manager: obtain repositories with `manager.getRepository(Entity)`;
rebind extended repositories with `manager.withRepository(...)` where supported.
A singleton injected repository remains bound to its original manager. Do not
assume Nest request scope or async context automatically rebinds it.

Await all transaction work before returning. Catching an error and returning
normally from the callback can commit earlier writes. Propagate failure to roll
back; translate it outside the transaction boundary. Rollback does not restore
mutated JavaScript objects. Discard/reload them before reuse, including retry attempts.

## Concurrent transitions

A read-check-save sequence can lose updates even when wrapped in a transaction.
Choose a protocol for the invariant: lock the row before checking within the same
transaction, condition an update on the expected version/state and check affected
rows, or use appropriate isolation with bounded retry. Cross-row invariants require
a matching constraint/lock strategy; a lock on one arbitrary row is insufficient.

`@VersionColumn` increments are not proof that every write compares an expected
version. Verify the actual WHERE predicate and conflict outcome. An optimistic
check during a SELECT alone leaves a later unguarded UPDATE race. Never silently
fall back to an unconditional save after a conflict. Acquire locks in a consistent
order and keep transactions short; do not hold them across human or remote I/O.

Retry only identified transient errors, with a bounded policy and a fresh read of
state. Do not replay irreversible effects with the transaction. An unknown commit
outcome needs reconciliation/idempotency, not an assumption that nothing happened.

## Effects and exceptional write paths

Perform domain mutation through intent methods. A specialized conditional SQL or
bulk path is acceptable when its named adapter operation explicitly preserves the
same invariant, authorization and concurrency protocol; verify that equivalence.
It is not permission to map arbitrary request attributes into `update` or `upsert`.

Database commit and message/email delivery are separate. Publish after commit when
best-effort delivery is sufficient; where durable handoff is required, persist the
existing outbox/job record in the same transaction and deliver it separately.
Subscriber execution or successful `save` inside an outer transaction is not proof
of commit. Do not add an outbox when the task has no durable-effect requirement.

Basis: [transactions](https://typeorm.io/docs/transactions/),
[custom repositories](https://typeorm.io/docs/working-with-entity-manager/custom-repository/),
[query locks](https://typeorm.io/docs/query-builder/select-query-builder/) and
[repository APIs](https://typeorm.io/docs/working-with-entity-manager/repository-api/).
