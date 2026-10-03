# TypeORM schema and verification

Read for migrations, deployment, version changes and evidence selection. Apply
the [shared verification policy](../verification.md).

## Migrations and deployment

- Use reviewed migrations for shared/staging/production databases. Keep
  `synchronize: false` and `dropSchema: false` there. Schema synchronization is
  acceptable only for explicitly disposable development/test data, not as the
  default development process that hides broken migrations.
- Generate a candidate migration against the intended schema, inspect its SQL,
  and check drops, renames, locks, backfills and compatibility. A class/file move
  is not authorization to rename/drop a table. Generation is not a review.
- Choose one migration runner per deployment; app replicas must not race startup
  migrations. Do not use `migrationsRun` on every replica as a concurrency protocol.
  Separate schema-changing credentials from runtime access when the deployment
  supports it. Migration failure prevents dependent rollout.
- Preserve the project's CLI wrapper, ESM/CommonJS mode and DataSource export.
  Check that compiled entities and migrations exist in the deployment artifact;
  do not mix stale `.js` and source `.ts` discovery. The Nest container does not
  automatically configure the standalone CLI.
- Select migration transaction mode for the real database operation. Some DDL
  cannot run inside a transaction. Record recovery/forward-fix and backup needs;
  a `down` method or old image does not guarantee safe data rollback. Use staged
  expand/backfill/contract changes when old and new application versions overlap.

## Focused evidence

| Changed contract | Relevant evidence |
| --- | --- |
| Intent method | Accepted/rejected transitions; invalid multi-field change leaves state unchanged |
| Mapping or hydration | Save/reload retains identity, values and behavior; precision/nullability round trips |
| Transaction/concurrency | Rollback and competing writer outcome on the target engine; verify scoped manager |
| Query scope | Missing ID/tenant filter, explicit NULL and bounded result/relations for affected path |
| Migration/artifact | Apply on disposable schema with representative prior state; inspect packaged CLI inputs |
| Nest wiring | Actual provider token/data-source registration, including related entities |

Use existing tests and the cheapest level covering the change. Repository mocks
can check orchestration but cannot prove SQL constraints, locks or migration safety.
SQLite/sql.js is useful for a mapping example, not proof of PostgreSQL/MySQL
concurrency or DDL. Do not build a new integration suite for wording-only changes.

## Compatibility

Record TypeORM, Nest integration (if present), driver/database, Node/TypeScript and
decorator toolchain separately. Current official docs describe 1.0, while many
projects use 0.3. Check version-specific defaults/APIs rather than copying upgrade
instructions into an unrelated change. In particular inspect null filters, orphan
handling, naming and discovery before accepting an upgrade-generated migration.

Basis: [migration purpose](https://typeorm.io/docs/migrations/why/),
[setup](https://typeorm.io/docs/migrations/setup/),
[execution](https://typeorm.io/docs/migrations/executing/) and
[0.3 to 1.0 changes](https://typeorm.io/docs/releases/1.0/upgrading-from-0.3/).
