# TypeORM

Apply with the [common rules](core.md) and [TypeScript profile](typescript.md).
Select this profile when TypeORM is declared or used, with or without NestJS.
Nest supports other persistence tools; its presence alone does not select TypeORM.
Select [Node.js](nodejs.md) only for actual Node host work; TypeORM also supports
non-Node hosts, subject to the installed version and driver.
Read only the task's sections; examples and research are optional.

## Essential contract

- Establish the installed TypeORM, driver, database and runtime versions, decorator
  settings, entity discovery and migration artifact. Documentation for 1.0 does
  not select an upgrade for a 0.3 project. These rules target relational usage;
  MongoDB needs its own transaction/query contract.
- Use a rich domain model for business state: named operations protect invariants
  and change related fields together. Do not generate attribute setters, generic
  patch methods or DTO-to-entity assignment as the domain write API.
- Record `mapped-rich` or `separate-domain` placement. Mapping a rich class does
  not require Active Record; persist through infrastructure. Preserve the chosen
  placement and do not automatically create a second model or generic CRUD layer.
- Await explicit writes. TypeORM does not provide Doctrine's application-wide
  identity map/unit-of-work/flush contract. A transaction must use its supplied
  manager throughout; in-memory mutation and database commit are distinct.
- Keep query scope, SQL constraints, concurrent updates and public projections
  explicit. Decorators, validation DTOs and version columns alone do not establish
  business authorization or a safe concurrent state transition.

## Read by task

| Task touches | Read |
| --- | --- |
| Rich entities, constructors, intent methods, mapping or model placement | [Models and mapping](typeorm/models-mapping.md) |
| Save, transaction ownership, rollback, locks, retries or external effects | [Transactions and lifetime](typeorm/transactions-lifetime.md) |
| Queries, null filters, relations, cascades, pagination or projections | [Queries and relations](typeorm/queries-relations.md) |
| Migrations, schema checks, compatibility or test selection | [Schema and verification](typeorm/schema-verification.md) |
| Actual NestJS TypeORM registration, injection or CLI data source | [NestJS integration](typeorm/nestjs-integration.md) |

## Basis

[Research and verification](../docs/research/2026-09-27-typeorm-engineering-practices.md)
records official sources checked on 2026-09-27 and the limits of executable checks.
Rich-model boundaries and the prohibition on attribute setters are framework policy
requested by the user, not requirements imposed by TypeORM.
