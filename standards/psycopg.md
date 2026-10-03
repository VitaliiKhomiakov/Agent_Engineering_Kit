# psycopg

Apply to Psycopg 3 (`psycopg`), not automatically to legacy `psycopg2`.
Use the [Python](python-fastapi.md) and [PostgreSQL](postgresql.md) rules.
Record the driver/implementation, libpq, Python, server and optional pool versions;
a driver dependency identifies its integration, not the deployed server version.

## Essential rules

- Keep SQL and adaptation in the persistence adapter. Bind values separately;
  compose identifiers with the driver's SQL tools and constrain allowed objects.
- Use named typed row contracts. A row factory or annotation does not validate
  external input, enforce a business rule or prove the live schema matches.
- Give the connection, cursor and transaction explicit owners. A SELECT can begin
  a transaction; cursor cleanup does not commit it. Report success after commit.
- Preserve a caller's transaction. Shared connections serialize commands and share
  transaction state; independent concurrent operations need independent connections.
- Distinguish expected database refusal, cancellation and uncertain commit. Retry
  only a complete replay-safe operation under the existing bounded policy.

## Read for the task

Read only relevant sections and stop when their rules are known; do not load all
links recursively. Separate examples are optional, not automatic reading routes.

| Task condition | Read |
| --- | --- |
| Parameters, dynamic SQL, result types, adaptation or bulk I/O | [Queries and contracts](psycopg/queries-contracts.md) |
| Transaction boundaries, savepoints, failures or resource ownership | [Transactions and lifetime](psycopg/transactions-lifetime.md) |
| Async concurrency, cancellation, pools, startup or connection security | [Async and pooling](psycopg/async-pooling.md) |
| Installation, Psycopg 2 migration, feature compatibility or verification | [Compatibility and verification](psycopg/compatibility-verification.md) |

## Basis

Research started 2026-09-21 and completed **2026-09-22**, targeting **3.3.6**.
The moving manual currently labels itself 3.3.7.dev1; release status and installed
capabilities take precedence. Snippets received syntax/type and offline composition
checks, not database execution. Evidence: framework source
`docs/research/2026-09-21-psycopg-engineering-practices.md` (optional research).
