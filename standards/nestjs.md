# NestJS

Use with the [common standard](core.md), [Node.js entry](nodejs.md)
and mandatory [TypeScript profile](typescript.md). Read only sections relevant to
the task and stop when its applicable rules are known. Examples and research are
optional; do not load all links recursively.

## Establish the executable contract

Identify Nest core/common and integration versions, Node, the HTTP or message
adapter, the validator/serializer and the compiler's decorator/metadata setup.
Verify the actual bootstrap registrations and launch artifact. Nest 12 features
are not assumed in older projects; upgrades are separate changes.

## Essential boundaries

- Feature modules assemble cohesive capabilities and export only their public API.
  Each independent controller, provider, repository adapter and module has its own
  file; cohesive nested DTOs can share a DTO file. Apply the common size criteria.
- Controllers/consumers validate transport input, invoke a use case and map outcomes.
  Business calculations, resource authorization, SQL and transactions stay behind them.
- Use explicit named contracts and Nest-managed DI for managed components; pure
  application/domain code need not carry decorators. Do not instantiate a managed
  service in a controller or make everything global to bypass module dependencies.
- Validation, transformation and response serialization are distinct mechanisms.
  DTO classes and value imports are required where runtime class metadata is used;
  a TypeScript annotation alone establishes none of those mechanisms.
- Input validity does not replace live business invariants. An HTTP pipe does not
  protect an arbitrary direct call, CLI or queue consumer.

## Read by task

| Task touches | Read |
| --- | --- |
| Feature boundaries, module exports, provider tokens/factories, scopes or cycles | [Modules and providers](nestjs/modules-providers.md) |
| DTOs/schemas, pipes, guards, filters, transformations or response serialization | [Transport contracts](nestjs/transport-contracts.md) |
| Use cases, persistence, transactions, external effects, startup or shutdown | [Application and lifecycle](nestjs/application-lifecycle.md) |
| TypeORM is actually used: rich entities, repositories, transactions or migrations | [TypeORM profile](typeorm.md), then its task-specific sections |
| Tests, actual adapter behavior, configuration, security, performance or upgrades | [Verification and operations](nestjs/verification-operations.md) |

## Verification

NestJS does not require TypeORM. Select and bundle the TypeORM profile only when
the project uses or explicitly selects it; another ORM retains its own contracts.

Check affected use cases without booting an HTTP server when their logic is pure.
For changed registration/metadata or a transport boundary, verify the real Nest
container and configured pipe/serializer/adapter. Use the existing runner and
checks proportionate to the changed behavior; avoid a new E2E suite per small fix.

## Basis

[NestJS research](../docs/research/2026-09-21-nestjs-engineering-practices.md) records
primary sources checked on 2026-09-21, version limits and alternatives. The
[practice plan](../docs/plans/2026-09-21-engineering-practices.md) owns executed checks
and the review checkpoint. Module layout and boundary obligations are project
policy, not a Nest requirement to introduce CQRS, repositories or a class per operation.
