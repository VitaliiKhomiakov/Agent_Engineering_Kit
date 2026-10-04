# SQLAlchemy

Apply only where SQLAlchemy is used or this profile is explicitly selected.
Use the [Python rules](python.md) and [core boundaries](core.md).
Establish the SQLAlchemy, Python, driver, database and migration-tool versions;
ORM presence does not identify the database or authorize a dependency upgrade.

## Essential rules

- Choose Core or ORM for the actual operation. Keep session/query mechanics in
  adapters; preserve the project's explicit mapped-domain or separate-model choice
  under [mapping and contracts](sqlalchemy/mapping-contracts.md). No universal
  repository, duplicate domain model or ORM migration is required.
- Use explicit typed mappings and named input/output contracts. ORM annotations
  and attribute validators do not replace transport validation or database integrity.
- Give each operation an owned Session and transaction. A Session is mutable
  transaction state, not an application cache; concurrent tasks need separate sessions.
- Distinguish flush, commit, rollback and close. Commit required effects before
  reporting success; preserve the caller's larger transaction and cleanup contract.
- Choose loading and result projection deliberately. Return complete data across
  a closed-session boundary; do not rely on incidental lazy I/O or serialization.
- Verify affected behavior with the real dialect/driver when database semantics
  matter. Database constraints and concurrency protection remain authoritative.

## Read for the task

Read only relevant sections; stop when their applicable rules are known.
Resources are conditionally available; do not load all links recursively.
Examples are optional, not additional automatic instruction routes.

| Task condition | Read |
| --- | --- |
| Core/ORM choice, mapped types, relationships, domain or output boundaries | [Mapping and contracts](sqlalchemy/mapping-contracts.md) |
| Writes, unit of work, flush/commit, conflicts or transaction ownership | [Sessions and transactions](sqlalchemy/sessions-transactions.md) |
| SELECT/result shape, eager loading, bulk DML, pagination or performance | [Queries and loading](sqlalchemy/queries-loading.md) |
| Async work, engine/pool lifetime, cancellation or connection security | [Async and engines](sqlalchemy/async-engines.md) |
| Tests, schema evolution, typing compatibility or SQLAlchemy upgrades | [Migrations and verification](sqlalchemy/migrations-verification.md) |

## Basis and compatibility

The tested historical baseline is **SQLAlchemy 2.0.54**, checked **2026-09-21**.
Examples ran on Python 3.12.3 and PostgreSQL 16.15 with the recorded drivers.
The **2026-10-04** source review covers released 2.1 separately; use the
[version decision](sqlalchemy/migrations-verification.md#compatibility-is-a-concrete-matrix).
Preserve existing 1.4/2.0 project constraints and authorize migrations separately.
Evidence: framework source `docs/research/2026-09-21-sqlalchemy-engineering-practices.md`
(optional research, not a required installed rule).
