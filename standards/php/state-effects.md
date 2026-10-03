# PHP state and effects

Read when changing object mutation, resources, generators/Fibers, long-running
workers, persistence, or external I/O. Apply the actual runtime and integration
contracts; PHP language features do not supply a scheduler or transaction design.

## State and lifetime

Give mutation an explicit owner and expose business intent methods instead of
arbitrary setters for invariant-bearing objects. A DTO or read model can remain
data. `readonly` is useful when a property must not be reassigned after
initialization, but nested objects/resources can still change. `clone` performs
a shallow copy unless the copy behavior explicitly replaces nested state. Prefer
immutable values such as DateTimeImmutable when shared mutable dates are unwanted.
[Readonly](https://www.php.net/manual/en/language.oop5.properties.php),
[cloning](https://www.php.net/manual/en/language.oop5.cloning.php).

Do not assume copies, constructor promotion, readonly classes, or an ORM hydrate
path re-run every business invariant. Choose ownership and reconstruction rules
that preserve valid state. References and mutable captured variables also share
state; avoid hidden coupling through `&`, static caches, globals, or reused
container services. Reset request/job-scoped data in persistent worker loops,
including error paths, and separate tenant/authentication context from process
configuration. Establish whether execution is CLI, ordinary requests, or a
persistent application server before relying on request teardown.

## Streams and iteration

Acquire a file, lock, or connection in the scope that owns its use. Check the
API's documented false/error contract, close/release in `finally`, and preserve
the original failure if cleanup also fails. Avoid `return` from `finally` or a
destructor that commits a success-critical effect. Destruction/request shutdown
is not a dependable application transaction boundary; forced termination may
prevent ordinary cleanup altogether.
[Finally semantics](https://www.php.net/manual/en/language.exceptions.php),
[destructors](https://www.php.net/manual/en/language.oop5.decon.php).

Use bounded/chunked reads when input size warrants them. A lazy generator can
avoid materializing all results, but the consumer controls how much runs. A
retained generator stopped by `break` can still hold its resource; do not assume
the provider's `finally` already ran. Put ownership around consumption or define
an explicit close/cancel protocol. A simple loop is preferable when laziness
adds no useful benefit.
[Generators](https://www.php.net/manual/en/language.generators.overview.php),
[bounded fgets](https://www.php.net/manual/en/function.fgets.php).

Distinguish EOF, an empty record, `"0"`, and a failed read. For writes, account for
partial progress and failure when the API permits it. A resource cannot be a
native PHP parameter/return type; use precise PHPDoc and a checked acquisition
boundary. The optional [resource example](examples/resources.md) owns cleanup
on normal EOF, early return, and rejected oversized input.

## Concurrency, deadlines, and cancellation

Fibers (8.1+) suspend/resume execution cooperatively; they do not create threads,
parallel CPU execution, an event loop, or nonblocking network I/O by themselves.
Use the existing async library/runtime when concurrency is required, with bounded
work, explicit task ownership, and its cancellation rules. Do not build a custom
scheduler or introduce Fibers for a sequential operation.
[Fibers](https://www.php.net/manual/en/language.fibers.php).

Set external-client connection/read/overall budgets according to the integration
contract; `set_time_limit` is not a portable wall-clock deadline for database or
network I/O. Client disconnect behavior depends on SAPI, output, and settings,
so do not assume it cancels in-flight work or safely rolls back an effect. Retries
need a bounded budget and an idempotency/reconciliation strategy for ambiguous
outcomes. Required background delivery needs an owned durable handoff where the
product requires it, not a detached process spawned from request code.
[Execution limits](https://www.php.net/manual/en/function.set-time-limit.php),
[connection handling](https://www.php.net/manual/en/features.connection-handling.php).

## Persistence and integration

Use parameterized statements for data values; placeholders do not substitute
SQL identifiers or arbitrary SQL fragments. Select dynamic identifiers from an
owned allowlist. Map external/driver rows to named contracts at the adapter, and
avoid lazy I/O hidden in public serialization.
[Prepared statements](https://www.php.net/manual/en/pdo.prepared-statements.php).

Keep the transaction with the operation that requires atomicity: begin, enforce
the relevant invariant, perform writes, commit, then report success. Roll back
on the applicable failure path, preserving the cause. PDO capabilities vary by
driver/database; some DDL causes implicit commits. A lock, transaction, or unique
constraint solves a concrete concurrency contract, not every problem at once.
A direct transaction block can be simpler than a Repository/unit-of-work layer;
adopt abstractions only when they clarify the actual boundary.
[PDO transactions](https://www.php.net/manual/en/pdo.transactions.php).

Keep HTTP/SDK retries, secrets, timeouts, parsing and protocol-error translation
in the integration owner. Do not claim a database transaction makes a remote call
atomic. Doctrine mapping/domain decisions stay with the existing combined profile
and later ORM research; this language section does not prescribe an ORM or mapper.
