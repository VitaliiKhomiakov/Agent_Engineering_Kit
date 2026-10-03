# Pydantic: model lifetime and integration boundaries

Read when models are mutated, copied, reconstructed, reused across tasks, or
mapped from persistence/SDK objects. Return to the [entry](../python-fastapi.md).

## Validation is a boundary event

A successfully parsed model is not a permanent proof that all future operations
are valid. Keep state-dependent business transitions with their domain owner,
as in the [Python domain example](../python/examples/domain.md). Pydantic models
can represent data/configuration snapshots; rich behavior and live-state checks
do not belong in transport validators merely because a model has methods.

| Mechanism | What to account for | Recommended response |
| --- | --- | --- |
| Ordinary assignment | Not validated by default | Keep snapshots owned/immutable where useful, or choose assignment validation for a genuinely mutable DTO |
| `validate_assignment=True` | Validates assignment, not a transactional state transition; in-place container changes are not attribute assignment | Do not rely on rollback after an after model-validator rejects a change; validate a candidate before publishing it |
| `frozen=True` | Prevents ordinary reassignment, not mutation inside lists/dicts or arbitrary bypasses | Use immutable owned contents or copies when the contract needs them; no implied thread safety |
| Existing model instances | `revalidate_instances` defaults to `never` and is configured on the relevant model type | Establish trust/ownership, or choose revalidation where instances may be stale or mutated; verify nested types separately |
| `model_copy(update=...)` | Update data is not validated; copying is shallow unless requested otherwise | Build and validate a complete candidate for untrusted changes; deep copying is not validation |
| `model_construct()` | Skips normal validation and nested conversion; `extra="forbid"` does not make it a validating path | Restrict to proven trusted data and a measured need; never use for raw input or failed validation |

The assignment rollback limitation was reproduced on 2.13.4: changing one end
of a valid interval raised from its after model-validator yet left that field
changed. This is an observed version-specific reason to avoid treating assignment
as atomic; it does not imply every kind of field-validation failure mutates state.

`Model.model_validate(existing_model)` is not a universal revalidation shortcut.
Likewise, accepting an already constructed nested instance does not guarantee
its internals were rechecked. Keep validators deterministic and idempotent where
they can run again; do not count their calls to drive effects. Configuration
inheritance also does not automatically configure separately nested model types.

## Mapping external data without hidden work

Keep database sessions, transactions, client lifetimes, and cancellation in their
application/adapter owners, following the [Python resource rules](../python/execution-resources.md).
Pydantic defines no transaction, persistence identity, or durable concurrency
protocol. An ORM model and a DTO can share values while serving different owners.

Use `from_attributes=True` only when attribute-based input is intended. Reading
properties or nested ORM relationships can trigger lazy I/O, fail outside a live
session, or traverse more data than expected. Fetch the needed data explicitly
and map the selected fields while their owner is valid. Explicit typed projection
is often clearer than accepting every arbitrary object with matching attributes.
Validate external records in the adapter and return owned contracts, not sessions
or model dumps with undocumented keys.

Where settings management is present, use the installed `pydantic-settings`
package and its actual source/precedence contract. Load settings at bootstrap,
inject the resulting typed configuration, and keep secret handling deliberate.
Do not move environment/network access into ordinary validators or create a
global BaseSettings instance at import time. Settings, ORM, or HTTP integration
is conditional; installing Pydantic does not require those components.

## Extensions and repeated use

Prefer declarative constraints, Annotated helpers, and focused adapters before
generic base classes or custom core schemas. A shared BaseModel is useful only
for shared contract policy; global aliases/strictness/serialization changes can
affect unrelated consumers. An adapter for an untyped SDK should expose concrete
types, not add `Any` or cast its way through a changing contract.

Reuse a TypeAdapter/schema when repeated parsing makes construction material;
do not reconstruct it per row by default. Keep validation contexts local to the
operation and avoid mutable validator globals. Library validation does not make
shared mutable application data safe across tasks/threads. Pydantic has no async
resource-lifetime mechanism; I/O and parallel work remain explicit outside the
validation pipeline.

Sources: [model semantics](https://docs.pydantic.dev/latest/concepts/models/),
[configuration](https://docs.pydantic.dev/latest/api/config/),
[copy contract](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_copy),
[TypeAdapter](https://docs.pydantic.dev/latest/concepts/type_adapter/),
[settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/).
The lifecycle/ownership requirements apply existing framework policy; none
requires making every domain entity a Pydantic model.
