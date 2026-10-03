# SQLAlchemy mapping and contracts

Read for persistence architecture, mapping changes or boundaries with domain/input/output.
Use the [entry](../sqlalchemy.md); shared strict typing remains in the Python profile.

## Choose the persistence model

Core expressions suit explicit SQL-shaped reads/writes. The ORM adds identity tracking,
relationships and unit-of-work persistence when those help the domain. Both can coexist
behind an adapter. Use a repository only for a useful domain seam; do not wrap every
Session method or force an ORM hierarchy onto a small query. Existing projects may
map domain classes or keep persistence records separate: preserve the chosen import
boundary and do not duplicate identical DTOs solely for folder separation.

## Typed maps are not runtime validators

For 2.0 code, prefer DeclarativeBase, `Mapped[T]` and `mapped_column()` with explicit
relationship types. Align Python optionality with actual database nullability and
state before persistence. A generated/server-default field may not have its eventual
value before flush; constructor defaults and server defaults have different owners.
Use the project's metadata/schema naming and migration conventions.

The ordinary declarative constructor does not provide a fully checked field signature.
Use an explicit typed constructor/factory, or optional MappedAsDataclass when its
constructor/default semantics fit. Mark database-generated fields `init=False` when
appropriate. Dataclass mapping does not add validation or make entities immutable;
SQLAlchemy's dataclass integration has feature limits. Do not use legacy stubs or
the deprecated mypy plugin to erase errors in modern mappings.

Map nullable/exact numeric/time/JSON values according to the actual dialect and driver.
Enforce durable uniqueness, foreign keys and required values in the database.
`@validates` observes ordinary attribute assignment, not every load or arbitrary SQL
write; it is not a universal invariant boundary. State-dependent business rules need
an operation/concurrency contract even if an HTTP DTO already validated its fields.
The [transaction example](examples/transactional-command.md) makes this distinction.

## Relationships and public data

Choose relationship ownership, cardinality and delete behavior deliberately. ORM
`delete`/`delete-orphan` cascades and database ON DELETE act at different boundaries;
match `passive_deletes` and actual foreign-key enforcement. Avoid bidirectional delete
cascades that can walk and remove an unintended graph. Bulk SQL operations do not
provide the same per-instance lifecycle as unit-of-work changes.

Mutable JSON tracking is separate from Python object mutation. Plain JSON fields do
not detect every in-place change; MutableDict/MutableList do not recursively track
arbitrary nested values without additional design. Reassign a new validated value
when that is simpler than custom instrumentation, and verify the stored result.

Project allowed fields into named DTOs while the necessary state is loaded. Do not
serialize an entire ORM object or assume a response model cannot trigger attribute
loads. Session identity, detached objects and `merge()` are persistence mechanics;
merge copies state into a managed instance and is not an input-validation or
conflict-resolution policy. Do not expose session-bound graphs as a public contract.

Basis: [declarative tables](https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html),
[dataclass mapping](https://docs.sqlalchemy.org/en/20/orm/dataclasses.html),
[attribute validation](https://docs.sqlalchemy.org/en/20/orm/mapped_attributes.html),
[cascades](https://docs.sqlalchemy.org/en/20/orm/cascades.html),
[mutation tracking](https://docs.sqlalchemy.org/en/20/orm/extensions/mutable.html), and
[state/merge](https://docs.sqlalchemy.org/en/20/orm/session_state_management.html).
