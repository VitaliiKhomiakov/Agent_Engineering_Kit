# Symfony

Apply only where Symfony components are used, with [PHP](php.md) and the
[common rules](core.md). Read only task-relevant sections; examples and research
are optional. Record actual component versions, including Validator; the checked
7.4 baseline does not upgrade a project or make 8.1 APIs available.
Doctrine is a separate selection, not implied by Symfony.

## Symfony essentials

- Entry adapters map transport input/results around an application operation;
  business decisions, persistence and external orchestration stay behind them.
- DTO attributes need an executed validation path. Mapping/validation, current
  business state, authorization, ORM mapping and public projection are distinct.
- Inject explicit services; verify their registration and actual lifetime.
  Lazy responses, kernel termination and message dispatch have different success
  guarantees; own required effects before reporting completion.

## Read by task

| Task touches | Read |
| --- | --- |
| Symfony structure, service wiring/configuration, controllers/commands/handlers | [Structure and services](symfony/structure-services.md) |
| Symfony routes, request mapping, Validator/forms, public output or authorization | [HTTP and validation](symfony/http-validation.md) |
| Symfony HttpClient, Messenger, kernel events, workers, transaction handoff or caches | [Runtime and effects](symfony/runtime-effects.md) |
| Symfony tests, container/routes, deployment, upgrades or compatibility | [Verification and compatibility](symfony/verification.md) |

For file moves, preserve PHP autoloading and affected service registrations.
If Doctrine is used, also apply its [profile](doctrine.md) to mapping changes;
a file move alone does not authorize a data-schema migration.

## Basis

[Symfony research](../docs/research/2026-09-21-symfony-engineering-practices.md)
records 7.4 execution evidence, primary sources, alternatives and 8.1 limits.
