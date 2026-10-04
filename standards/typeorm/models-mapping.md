# TypeORM models and mapping

Read for business models, creation, hydration and mapping. Apply the
[TypeORM entry](../typeorm.md) and the project's explicit model placement.

## Rich domain model

| Placement | Domain behavior | Persistence |
| --- | --- | --- |
| `mapped-rich` | A mapped class owns business invariants and transitions | Infrastructure loads and saves it |
| `separate-domain` | An independent class owns those same rules | A repository adapter converts a TypeORM record |

Both placements require behavior where meaningful business state exists. DTOs,
read projections and separate storage records can be data containers. Preserve
existing placement; clarify a missing material choice before adding parallel
models. For a new simple aggregate, propose `mapped-rich` when its ORM dependency
is acceptable; choose separation for an actual independence or representation need.

Expose operations such as `reschedule(startsAt, endsAt)` or
`changeDeliveryAddress(street, city, postalCode)`. Validate the full proposed state
before assigning any field, so rejection leaves the object unchanged. A transition
may legitimately change one field; do not group unrelated fields just to increase
the argument count. Do not introduce `setStartsAt`/`setEndsAt`, `setStatus`, generic
`update(data)` or `Object.assign(entity, dto)` as alternate domain mutation paths.
`create`, `merge`, `preload`, `save(partial)` and bulk SQL do not invoke intent methods.

Keep state private/protected where compatible with mapping; expose meaningful
read access without leaking mutable Dates, arrays or owned children. TypeScript
`private` is a compile-time boundary, not runtime secrecy. ECMAScript `#private`
slots cannot be treated as ordinary mapped properties. Do not use casts or `any`
to force private persistence fields through typed find/update APIs; use a suitable
mapping/repository boundary and verify its actual hydration behavior.

Entities do not receive DataSource, EntityManager, repositories, Nest services or
HTTP/queue clients. Application operations coordinate authorization, transactions
and effects; entities own local business decisions. Prefer Data Mapper for this
boundary. Rich methods do not require `BaseEntity.save()` or other Active Record
dependencies. Existing Active Record migration is a separate scoped change.

## Creation and hydration

TypeORM normally constructs entities while loading; unlike Doctrine, do not assume
constructors are bypassed. Constructor arguments must allow ORM hydration. Use a
named creation method for required business inputs and keep hydration construction
free of I/O, generated business events and assumptions that columns are populated.
Do not set `entitySkipConstructor` merely to mask incompatible constructors: it
also changes initializer behavior and needs explicit round-trip checks.

Hydration restores persisted state; it does not replay creation/transition methods.
Back the stored representation with constraints and a deliberate legacy-data policy.
Test that a loaded instance retains behavior. `EntitySchema` can separate metadata
from a class without creating a second business model, but its typing and target
must match the actual class. Avoid a new mapper solely to remove decorators.

## Mapping contracts

Specify column types, nullability, lengths, precision, identity and constraints for
the target database. TypeScript types, class-validator, ORM metadata and SQL
constraints give separate guarantees. Decimal/bigint driver values need an exact
representation; avoid implicit conversion to unsafe JavaScript numbers. Define
timestamp timezone/precision and transformer round trips explicitly.

If the domain permits clearing a value, model null explicitly in its typed storage
contract and nullable column; optional/undefined alone is not a clear operation.
Keep intent methods and follow the [save semantics](transactions-lifetime.md#explicit-persistence-and-ownership).

Do not expose an entity as an API response by default. Build a projection with the
intended fields; private keyword, `select: false` and serializer annotations alone
are not a public-output security contract. Listeners/subscribers can handle bounded
persistence-local concerns, but must not hide a use case or remote side effect.

Optional example: [rich booking with a coupled state change](examples/rich-booking.md).
Basis: [entities](https://typeorm.io/docs/entity/entities/),
[Data Mapper](https://typeorm.io/docs/guides/active-record-data-mapper/),
[repository APIs](https://typeorm.io/docs/working-with-entity-manager/repository-api/),
[FAQ](https://typeorm.io/docs/help/faq/) and
[listeners/subscribers](https://typeorm.io/docs/listeners-and-subscribers/).
