# NestJS integration with TypeORM

Read only when both technologies are present, together with the relevant
[NestJS sections](../nestjs.md). Nest's dedicated integration is an option, not
a requirement to adopt TypeORM in every Nest project.

## Registration and ownership

Register the connection with `TypeOrmModule.forRoot`/`forRootAsync` and the feature's
repositories with `forFeature`. Keep configuration validation at assembly. For
multiple sources, align names in root registration, feature registration and
`InjectRepository`/`InjectDataSource`; verify async registration naming too.

`autoLoadEntities` includes entities registered through `forFeature`; it does not
discover a class merely because another entity references it in a relation. Ensure
all relation targets are registered. Maintain the CLI DataSource's discovery
separately, with the same schema/naming choices and validated configuration.

Let the selected integration own pool startup/shutdown. Do not create a DataSource
per service/request or close a shared pool from a request-scoped provider. Managed
shutdown must be connected to the actual process signal path.

## Application boundary

Controllers map validated DTOs to named application operations. The operation
loads the required state, authorizes the action, invokes an intent method and
persists through the agreed adapter. DTO validation is not entity validation;
never pass a request body directly to repository `save`, `merge` or `preload`.

Keep TypeORM types inside infrastructure when the core is independent. Bind an
existing consumer-owned port using a Nest provider token; do not wrap each table
in an identical generic CRUD repository. A simple service may use the selected
architecture's persistence boundary without mandatory CQRS or a new mapper layer.

For transactions, an injected repository is not automatically transaction-local.
Use the manager supplied by the transaction to obtain every participating
repository, including repositories hidden behind adapters. Follow
[transaction ownership](transactions-lifetime.md). Translate known persistence
conflicts at the boundary; do not leak SQL or credentials into public errors.

Basis: [Nest database options](https://docs.nestjs.com/techniques/database) and
[Nest TypeORM integration](https://docs.nestjs.com/data/typeorm).
