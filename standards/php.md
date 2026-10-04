# PHP

Apply to PHP work with the [common rules](core.md). Read only task-relevant
sections; examples and research are optional, not a recursive reading queue.
Symfony and Doctrine have separate profiles, selected only when actually used.

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

For class moves, check namespaces and autoloading under
[PHP verification](php/verification.md). Framework DI and ORM registrations
are checked only for the integrations present; a move alone does not authorize
a data-schema migration.

## Basis

- [PHP research](../docs/research/2026-09-21-php-engineering-practices.md) records
  primary sources checked on 2026-09-21, alternatives and version limits; the
  [practice plan](../docs/plans/2026-09-21-engineering-practices.md) records checks.
