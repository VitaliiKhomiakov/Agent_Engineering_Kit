# Doctrine ORM / DBAL

Apply only where Doctrine is used, with [PHP](php.md) and the
[common rules](core.md). Read only task-relevant sections; examples and research
are optional. Doctrine DBAL works without ORM: ORM-specific guidance applies
only to ORM use. Establish actual ORM/DBAL and integration versions.
Symfony is not required by this profile; its integration rules apply only when used.

## Doctrine essentials

- Preserve the explicit `mapped-rich` or `separate-domain` architecture; ORM
  permits entity behavior. Use intent methods for invariants and keep services,
  persistence orchestration and whole use cases outside entities/callbacks.
  [Model placement](doctrine/models-mapping.md#domain-model-placement) owns the
  decision rules; do not create a second model or mapper automatically.
- Give the ORM unit of work and database transaction explicit owners. `persist`
  schedules work; `flush` synchronizes it, and an outer commit determines success.
  Rollback does not restore PHP object state; replace a failed, closed manager.
- Bind query values, control SQL identifiers, bound result sets and inspect query
  shape. Mapping and input validation do not replace database constraints or
  concurrency protection. Public contracts must not expose ORM machinery.

## Read by task

| Task touches | Read |
| --- | --- |
| Doctrine ORM entities, repositories, model placement, mapping or associations | [Models and mapping](doctrine/models-mapping.md) |
| Doctrine ORM identity map/lifetime, flush, transaction failure, concurrency or effects | [Unit of work and transactions](doctrine/unit-of-work-transactions.md) |
| Doctrine DBAL SQL/results/transactions, ORM query shape, N+1, pagination or batches | [Queries and DBAL](doctrine/queries-dbal.md) |
| Doctrine mapping/schema tests, migrations, deployment, upgrades or compatibility | [Schema and verification](doctrine/schema-verification.md) |

When moving a mapped class, check PHP autoloading and affected mapping;
check DI registration only where present. A file move alone does not authorize
a data-schema migration.

## Basis

[Doctrine research](../docs/research/2026-09-21-doctrine-engineering-practices.md)
records ORM/DBAL evidence, alternatives, version limits and executable checks.
