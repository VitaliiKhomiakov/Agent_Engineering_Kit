# Doctrine schema, verification and compatibility

Read for Doctrine tests, mapping/schema changes, migrations, deployment or upgrades.
Use the [shared verification policy](../verification.md); this is a menu of checks
for affected behavior, not a requirement to run a database matrix for every edit.

## Establish the actual combination

Record PHP/runtime/extensions, ORM and DBAL constraints/locks, driver/server version,
and actual mapping/cache/proxy configuration. If present, also check Collections,
DoctrineBundle, Migrations and extensions such as custom types or filters. A
framework name or an online `current` page does not select compatible versions.

Primary sources checked on 2026-09-21 identify ORM 3.7.1 and DBAL 4.4.4 as stable.
Their package requirements differ: ORM permits PHP 8.1 and DBAL 3.8.2 or 4; DBAL
4.4 requires PHP 8.2. The examples used PHP 8.3.6, ORM 3.7.1, DBAL 4.4.4 and SQLite
3.45.1. This is execution evidence for that combination, not a project upgrade.

Native lazy objects require PHP 8.4 and compatible ORM configuration. With older
PHP/proxy generation, do not copy a `final` entity or proxy setup blindly. In ORM
3.7, `createAttributeMetadataConfig()` targets native lazy objects; the examples
use `createAttributeMetadataConfiguration()` for PHP 8.2/8.3. Production proxy/cache
preparation differs from disposable `isDevMode: true` examples. See
[configuration](https://www.doctrine-project.org/projects/doctrine-orm/en/3.7/reference/advanced-configuration.html)
and the installed API.

ORM 3.7 changes include `LockMode::NONE` no longer refreshing an identity-map hit,
and deprecation of the old `Paginator` in favor of `OffsetPaginator`/`Window`.
Collections 3 introduces cross-package API changes; our fixture used Collections
2.6.0. Follow the actual [ORM upgrade notes](https://github.com/doctrine/orm/blob/3.7.1/UPGRADE.md)
and [DBAL upgrade material](https://github.com/doctrine/dbal/blob/4.4.4/UPGRADE.md).
Do not combine unrelated PHP/ORM/DBAL major upgrades or rewrite mappings as routine
cleanup; verify the relevant deprecations and supported transition path.

## Choose evidence for the changed behavior

| Changed behavior | Useful check | What it does not prove |
| --- | --- | --- |
| Pure business transition | Direct method checks, including refusal without mutation | Persistence, authorization or concurrency correctness |
| ORM mapping/repository | Mapping validation; write/flush/clear/reload with real storage | All SQL constraints, platform features or loaded associations |
| DBAL query/conversion | Real driver rows, parameters, absence/NULL/zero, affected rows | Another driver's scalar types or SQL semantics |
| Transaction/failure recovery | Fail after an earlier write; verify database and context state | Recovery from an ambiguous network/commit failure |
| Version/locking behavior | Independent managers/connections; stale version or controlled overlap | Target isolation, deadlocks and contention from a sequential SQLite check |
| Fetch/pagination/batch change | Real query counts, row shapes, page boundaries and representative volume | A general throughput or memory guarantee |
| Framework wiring/file move | Autoload, selected manager, mapping discovery, container and cache/proxy loading | A data migration being needed or safe |

Use narrow unit substitutes for a consumer's port where useful. A mock expecting
`persist()`/`flush()` calls does not verify persistence. Clear or recreate the
context before persistence assertions so the identity map cannot satisfy them.
Exercise relevant association ownership, cascades/orphan deletion and constraints
when those mappings change. Query budgets should describe an operation and fixture,
not bind every test to incidental SQL order.

Mapping validation and schema comparison are separate from behavioral and data
checks. ORM skips some expensive mapping validation during ordinary execution;
run the applicable validator when mapping changes. On platform-sensitive work,
use the deployed database/version or an appropriate isolated equivalent. Doctrine's
[testing guide](https://www.doctrine-project.org/projects/doctrine-dbal/en/4.4/reference/testing.html)
is contributor guidance, not a replacement for this workspace's proportionate gates.

## Schema changes and migrations

- Review an actual diff against the intended schema/database. Preserve unrelated
  tables with correct schema ownership/filtering; generated SQL can propose their
  removal. Doctrine Migrations also supports DBAL-only schema providers.
- A class/namespace move calls for autoload/DI/mapping checks first. If persistent
  names are unchanged, do not manufacture a data migration. If schema change is
  intended, use the project's versioned migration workflow.
- Inspect renames, drop/create pairs, nullable/default/precision changes, data
  backfills, constraints and indexes. A schema diff cannot decide data meaning or
  compatibility with both old and new deployed application versions.
- Plan execution order, locks, transaction support and recovery for the actual
  platform. Expand/backfill/contract can help rolling compatibility when needed;
  it is not mandatory for every local schema edit. An irreversible data operation
  needs an honest recovery plan, not a fictitious reversible `down()`.
- `SchemaTool` is useful for disposable fixtures. Do not treat direct schema update
  or `diff` generation as an authorized production migration. Review SQL before
  execution; even an option named `--dump-sql` can be combined with an executing
  option, so inspect the installed command's help and flags.
- Transactional/all-or-nothing settings do not make every DDL statement rollbackable.
  MySQL/Oracle implicit commits require platform-aware separation of DML and DDL.
  Dry-run output is not evidence that a migration succeeds on representative data.

[ORM tools](https://www.doctrine-project.org/projects/doctrine-orm/en/3.7/reference/tools.html),
[migration generation](https://www.doctrine-project.org/projects/doctrine-migrations/en/3.9/reference/generating-migrations.html)
and [implicit commits](https://www.doctrine-project.org/projects/doctrine-migrations/en/3.9/explanation/implicit-commits.html)
are the relevant primary references. Record actual commands, results and unexecuted
platform checks; the [research note](../../docs/research/2026-09-21-doctrine-engineering-practices.md)
and [practice plan](../../docs/plans/2026-09-21-engineering-practices.md) hold K08 evidence.
