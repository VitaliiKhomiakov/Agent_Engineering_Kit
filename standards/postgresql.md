# PostgreSQL

Apply only to PostgreSQL persistence work with the [core rules](core.md).
Establish the server version, driver/ORM, migration owner, and transaction boundary
from project evidence. A dependency on a driver is not proof of the server version.

## Essential rules

- Protect durable invariants with appropriate database constraints as well as
  application decisions. Transport validation cannot protect concurrent writes.
- Give each operation an explicit transaction owner. Choose isolation and locks
  for its actual conflict scenario; retry a complete transaction only under a
  bounded policy that preserves idempotency and external-effect safety.
- Bind untrusted values, preserve tenant/authorization boundaries, and use the
  intended database role. A schema name or a connection pool is not access control.
- Preserve existing data and deployment compatibility. Assess locks and recovery
  before schema changes; development work does not authorize production migrations.
- Verify changed queries and invariants on PostgreSQL with relevant failure cases.
  Add indexes, abstractions or operational machinery for a concrete requirement.

## Read for the task

Read only sections relevant to the current decision; stop when its rules are known.
Resources are available for conditional use; do not load all links recursively.
Examples are separate and optional.

| Task condition | Read |
| --- | --- |
| Designing tables, durable rules, types or persistence boundaries | [Schema and contracts](postgresql/schema-contracts.md) |
| Changing writes, isolation, locks, retries or work claiming | [Transactions and concurrency](postgresql/transactions-concurrency.md) |
| Changing queries, indexes, pagination or a measured performance problem | [Queries and performance](postgresql/queries-performance.md) |
| Changing roles, tenant isolation, connection lifetime, backup or production behavior | [Security and operations](postgresql/security-operations.md) |
| Changing schema/data, upgrading versions or choosing verification | [Migrations and verification](postgresql/migrations-verification.md) |

When Psycopg 3 is used or explicitly selected, its separate `psycopg` profile owns
parameter/row adaptation and driver lifetime details. PostgreSQL selection alone
does not select that driver; its presence does not establish a server version.

## Basis and compatibility

The initial fixture declares PostgreSQL 16. Research checked the 16 and 18 manuals
on **2026-09-21**; examples ran on **16.15 and 18.4**. Current support/patch status
must be checked for deployment; the locally tested 18.4 is not a patch recommendation.
Use features supported by the actual server and migration tool, not `/current/`
documentation by assumption. Evidence and tradeoffs: framework source
`docs/research/2026-09-21-postgresql-engineering-practices.md` (optional research,
not a required installed rule).
