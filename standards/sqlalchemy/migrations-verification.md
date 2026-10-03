# SQLAlchemy migrations and verification

Read for changed mappings/schema, dependency upgrades, typing or relevant test design.
Use the shared [verification policy](../verification.md).

## Schema ownership

Metadata describes the intended schema; create_all is suitable for a fresh disposable
fixture or explicitly chosen initial setup, not migration of existing tables. Keep
one migration owner and review changes to defaults, constraints, nullability, enums,
indexes and database-specific types. Adopt Alembic only when the project chooses it;
SQLAlchemy does not require switching an existing migration system.

Autogeneration produces candidate changes. Review renames, data transformations,
constraint names and backend-specific operations; an apparent drop/add can lose data.
Use a consistent metadata naming convention when it improves deterministic migration
management, without renaming a live schema as incidental cleanup. A schema diff is not
a backfill, rollback plan or proof of compatibility with older deployed writers.
Check locking, transaction mode, data preservation and recovery with the database's
actual rules. In particular, nontransactional steps cannot be hidden inside an ORM
transaction simply because most fixture DDL works there.

## Compatibility is a concrete matrix

Record Python, SQLAlchemy, driver, database and analyzer versions. The researched
stable baseline is 2.0.54; 2.1.0rc2 is prerelease and is not adopted automatically.
For 1.4 migration, use the official staged migration path/deprecation diagnostics,
then test on the target 2.0 runtime. Removing legacy engine.execute, implicit
library autocommit or old statement argument shapes can change transaction/result
behavior. Legacy Query remains available in 2.0; avoid rewriting unrelated queries
merely for style. A local change does not authorize a project-wide conversion.

Use native 2.0 typed mappings. The legacy SQLAlchemy mypy plugin is deprecated and
only supported through mypy 1.10.1; it is not the strategy for current analyzers.
Conflicting third-party stubs can hide native typing. Check generated constructors
and typed results without Any/cast/ignore bypasses. Prerelease 2.1 has further changes
in defaults, dataclass behavior and dependencies; do not mix its examples into a 2.0
project. Review dialect/driver notes too, not just the ORM version string.

## Evidence for the affected boundary

Keep tests and named DTOs strictly typed. Verify successful commit, expected refusal,
failed flush/rollback, and reuse of an owned clean session where changed. Test that
an adapter does not commit a caller's larger transaction. For concurrency, use
independent sessions/connections and coordinate the relevant milestones. Database
constraints, isolation and SQLSTATE require the real backend; SQLite/in-memory mocks
cannot establish PostgreSQL behavior.

For loading changes, test detached DTO completeness, ordering/cardinality and missing
relationships; guard against accidental I/O. Query counts/plans are useful for a
specific performance contract, not an automatic quota. For async lifecycle changes,
cover relevant cancellation/error cleanup and bound waits. Shared test transactions/
savepoints need dialect support and cannot prove externally visible COMMIT behavior;
use real commits when that is the requirement. Keep fixture schemas isolated.

Examples here execute sync writes and async reads/cancellation on PostgreSQL. They
do not establish every driver's behavior, migration safety, crash recovery or load
capacity. Run migration checks only for actual migrations; this documentation stage
adds no live migration or new application dependency. Synthetic client bundles prove
portable instructions, not actual model reading compliance.

Basis: [metadata DDL](https://docs.sqlalchemy.org/en/20/core/metadata.html),
[Alembic autogeneration](https://alembic.sqlalchemy.org/en/latest/autogenerate.html),
[2.0 migration](https://docs.sqlalchemy.org/en/20/changelog/migration_20.html),
[legacy typing plugin](https://docs.sqlalchemy.org/en/20/orm/extensions/mypy.html), and
[2.1 changes](https://docs.sqlalchemy.org/en/21/changelog/migration_21.html).
