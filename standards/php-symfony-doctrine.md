# PHP / Symfony / Doctrine

Apply this entry with the [common rules](core.md). Read only sections relevant to
the task; stop once its applicable rules are known. Examples and research are
optional, not an instruction to load all links recursively.

## PHP essentials

- Establish PHP version, SAPI, extensions, Composer constraints, and actual tools;
  preserve the project's supported range and dependency workflow.
- Keep named PSR-4 types in matching, case-correct files. Use typed contracts and
  explicit dependencies; ordinary DTO creation needs no separate factory.
- Parse external values at their boundary. Scalar strictness, static analysis,
  input validation, and state-dependent business rules have different guarantees.
- Give mutable state, resources, transactions, and external effects explicit
  owners; preserve failure semantics and complete required effects before success.

## Read by task

| Task touches | Read |
| --- | --- |
| Namespaces, PSR-4, packages, object construction, dependencies or patterns | [Structure and dependencies](php/structure.md) |
| Native/PHPDoc types, arrays, parsing, null/presence, domain rules, errors | [Types and contracts](php/types-contracts.md) |
| Mutation, readonly/clone, streams, generators, workers, transactions or I/O | [State and effects](php/state-effects.md) |
| Tests, static analysis, autoload/file moves, security, performance or upgrades | [Verification and compatibility](php/verification.md) |
| Symfony structure, service wiring/configuration, controllers/commands/handlers | [Structure and services](symfony/structure-services.md) |
| Symfony routes, request mapping, Validator/forms, public output or authorization | [HTTP and validation](symfony/http-validation.md) |
| Symfony HttpClient, Messenger, kernel events, workers, transaction handoff or caches | [Runtime and effects](symfony/runtime-effects.md) |
| Symfony tests, container/routes, deployment, upgrades or compatibility | [Verification and compatibility](symfony/verification.md) |
| Doctrine ORM entities, repositories, model placement, mapping or associations | [Models and mapping](doctrine/models-mapping.md) |
| Doctrine ORM identity map/lifetime, flush, transaction failure, concurrency or effects | [Unit of work and transactions](doctrine/unit-of-work-transactions.md) |
| Doctrine DBAL SQL/results/transactions, ORM query shape, N+1, pagination or batches | [Queries and DBAL](doctrine/queries-dbal.md) |
| Doctrine mapping/schema tests, migrations, deployment, upgrades or compatibility | [Schema and verification](doctrine/schema-verification.md) |

Availability in a bundle does not imply mandatory reading. Symfony routes and
essentials apply only where that framework is used. Doctrine DBAL works without
ORM; read ORM-specific guidance only where ORM is used. Establish actual component
versions, including Validator and DBAL; linked documentation does not select a
project version.

## Symfony essentials

- Entry adapters map transport input/results around an application operation;
  business decisions, persistence and external orchestration stay behind them.
- DTO attributes need an executed validation path. Mapping/validation, current
  business state, authorization, ORM mapping and public projection are distinct.
- Inject explicit services; verify their registration and actual lifetime.
  Lazy responses, kernel termination and message dispatch have different success
  guarantees; own required effects before reporting completion.

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

## Framework integration during file moves

When moving a class, check its namespace, autoloading, and related DI/ORM registrations. When
changing a model, check the affected mapping and contract; moving a file alone
does not authorize a data-schema migration.

## Basis

- [PHP research](../docs/research/2026-09-21-php-engineering-practices.md) records
  primary sources checked on 2026-09-21, alternatives and version limits; the
  [practice plan](../docs/plans/2026-09-21-engineering-practices.md) records checks.
- [Symfony research](../docs/research/2026-09-21-symfony-engineering-practices.md)
  records 7.4 execution evidence, primary sources, alternatives and 8.1 limits.
- [Doctrine research](../docs/research/2026-09-21-doctrine-engineering-practices.md)
  records ORM/DBAL evidence, alternatives, version limits and executable checks.
