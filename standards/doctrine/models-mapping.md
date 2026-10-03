# Doctrine ORM models and mapping

Read for ORM entities, repositories, model placement, mapping or associations.
DBAL-only work does not require entities. Apply the [common rules](../core.md)
and preserve the project's supported versions and architecture.

## Domain model placement

Doctrine does not prohibit business methods on an entity. A ban on all logic in
ORM entities therefore cannot be justified as a Doctrine or Symfony requirement.
The project architecture must explicitly choose one of two approaches:

| Approach | Rules and state | Persistence |
| --- | --- | --- |
| `mapped-rich` | A rich domain entity that is also mapped by Doctrine | A repository/infrastructure component persists it |
| `separate-domain` | A separate domain model with behavior | A Doctrine record plus conversion in the repository adapter |

In both approaches, intent methods that protect invariants change the business
model, rather than arbitrary public setters. DTOs and persistence records need
not reproduce its behavior. Do not move every rule into services while calling
the remaining data container a rich domain model.

For a coupled change, expose an operation such as `reschedule(start, end)` and
validate the proposed interval before assigning either field. Do not generate
independent attribute setters or a generic patch method that bypasses the invariant.
A meaningful transition may change one field; unrelated changes need not be grouped.

Do not inject EntityManager, repositories, HTTP clients, message transports, or
the container into an entity, and do not put an entire application use case in it.
Do not hide such a use case in lifecycle callbacks. Appropriate application and
infrastructure components coordinate persistence and external effects.

Preserve the existing approach during ordinary changes. If a new model has no
chosen approach and the decision affects the implementation, clarify it before
creating parallel models. Do not introduce a mapper and second entity automatically.
Simple read models do not require rich domain counterparts.

The [Doctrine tutorial](https://www.doctrine-project.org/projects/doctrine-orm/en/3.7/tutorials/getting-started.html#adding-behavior-to-entities)
recommends rich entities; this is design advice, not a prohibition on persistence
records. Our boundary policy also does not imply banning useful accessors or
requiring an input DTO for each method.

## Repositories and construction

- Keep SQL/DQL, mapping, hydration and persistence errors in infrastructure.
  Inject the correct manager/connection there; do not retrieve a container from
  business code. Multiple managers require explicit ownership, not a default
  manager assumption.
- Expose the operations consumers need, with named results and explicit absence.
  An independent core's port must not return EntityManager, QueryBuilder, a lazy
  ORM query or an infrastructure-specific collection. Implement an existing port
  where required; do not add generic CRUD interfaces or repository wrappers for
  every table solely to mirror Doctrine's API.
- Ordinary constructors or named constructors suffice for ordinary entities and
  values. A factory is useful for genuine creation rules or complex assembly.
  ORM's rehydration bypasses constructors; it is not a replay of creation checks.
  Verify stored data, mappings and database constraints separately.
- Keep mapping discovery, namespaces, service registration and class moves in
  sync. A file move alone does not authorize a schema migration.

## Mapping and contracts

Treat native PHP types, ORM metadata, input validation and SQL constraints as
separate contracts. Specify meaningful nullability, lengths, precision, identity
and relationships; nullable PHP properties do not automatically make columns
nullable. Mapping does not execute Symfony Validator or authorize a write.

Select the DBAL type for the stored meaning. Exact decimals need an exact value
representation rather than a float conversion; DBAL `decimal` converts to a
string, and DBAL 4 `bigint` may be an int or string depending on range. Plain
DBAL fetch results have a different conversion contract; see
[queries](queries-dbal.md#result-boundaries).

For timestamps, choose timezone/precision semantics and a compatible immutable
mapping where appropriate; check round trips on the target platform. JSON storage
does not validate a business schema. Custom types/embeddables help reusable value
semantics but add conversion, schema-comparison and upgrade work; a simple mapped
scalar can be sufficient. Do not store live services or transport objects.

## Association ownership and lifetime

- Model only needed navigation. Unidirectional associations often suffice;
  bidirectional navigation adds synchronization obligations.
- Update the owning side: a many-to-one owns its foreign key; a one-to-many is
  the inverse side. For many-to-many, inspect the chosen mapping. Keep both sides
  coherent when code reads them before reloading; changing only an inverse
  collection does not update the owning foreign key.
- Type mapped collections as `Collection` with element/key PHPDoc; initialize new
  entities with `ArrayCollection`. Doctrine may replace it with a persistent
  collection. Do not expose mutability that bypasses required intent methods.
- Choose `cascade` operations individually. ORM cascading may hydrate a large
  graph; database `ON DELETE` has different lifecycle behavior. `orphanRemoval`
  assumes private ownership: do not use it for children reused by other parents.
- Collection iteration, conversion to arrays and serialization can initialize
  lazy data. Choose a bounded read projection when full navigation is unnecessary;
  use [query guidance](queries-dbal.md#orm-query-shape) for N+1 and pagination.

[Architecture](https://www.doctrine-project.org/projects/doctrine-orm/en/3.7/reference/architecture.html),
[basic mapping](https://www.doctrine-project.org/projects/doctrine-orm/en/3.7/reference/basic-mapping.html),
[associations](https://www.doctrine-project.org/projects/doctrine-orm/en/3.7/reference/working-with-associations.html)
and [DBAL types](https://www.doctrine-project.org/projects/doctrine-dbal/en/4.4/reference/types.html)
provide the framework contracts. See the optional
[ORM example](examples/orm-unit-of-work.md) for persistence and invariant checks;
proxy/version and schema checks belong to [verification](schema-verification.md).
