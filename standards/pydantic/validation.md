# Pydantic: models and input validation

Read when choosing a model/adapter, defining fields, changing accepted input, or
writing validators. Applies where Pydantic is used; return to the
[Python/Pydantic entry](../python-fastapi.md). Guidance targets Pydantic 2;
check the installed version before adopting an API or changing a contract.

## Choose the boundary and simplest model

Use Pydantic to parse external data into a named typed contract at the adapter,
transport, configuration, or integration boundary that owns that format. It is
not a dependency-injection container, persistence layer, authorization mechanism,
or replacement for state-dependent domain behavior. A valid request can still
be forbidden or impossible in the current business state.

| Need | Suitable form | Simpler alternative or cost |
| --- | --- | --- |
| Named structured external record | A focused `BaseModel` with typed fields | Do not inherit a universal model containing persistence, transport, and business methods |
| Validate a scalar, union, or collection without an artificial wrapper record | `TypeAdapter[T]` with a concrete result type | Direct parsing may suffice for one small boundary; reuse a configured adapter instead of rebuilding it per item |
| An existing dataclass must accept external data | A Pydantic dataclass or a TypeAdapter around the agreed data type | A stdlib dataclass suffices for already typed internal data; changing decorators changes construction behavior |
| A root value needs model identity/methods/schema | `RootModel[T]` | TypeAdapter is often enough for a list/union; neither is an excuse for unstructured payloads |
| Repeated field semantics | A small `Annotated` type with constraints/validators | A local Field is clearer for one occurrence; use generics or custom core schemas only for actual reuse |

Keep DTOs with their operation and layer using the [Python cohesion rules](../python/structure.md).
Reuse identical contracts when meaning and visibility match; separate input,
stored, and public output models when their allowed data or lifecycle differs.
Keep an independent business core free of transport-specific Pydantic models.

## Define accepted input explicitly

- Choose the actual validation entry: `model_validate` for Python objects,
  `model_validate_json` for JSON text/bytes, or the corresponding TypeAdapter
  method. JSON and Python modes can accept different representations. Do not
  assume `json.loads` followed by Python validation is behaviorally identical.
- Preserve the API's coercion policy. Use strict model/field/call settings where
  implicit conversions violate the contract; lax parsing is useful for some
  string-based inputs. Strict JSON still accepts certain wire representations,
  such as ISO dates. Consult the conversion table for the actual type and mode;
  strictness is not an unknown-field, authorization, or input-size policy.
- Decide requiredness, nullability, and defaults separately. In V2, `T | None`
  without a default is required but nullable. `= None` permits omission. Valid
  zero/false values are not missing. For patch semantics read [serialization](serialization.md).
- Set `extra` deliberately. `forbid` is a useful default for closed write
  contracts to catch typos/unwritable fields; `ignore` can suit an evolving
  upstream response. `allow` needs an actual extension contract and bounded,
  typed values. Default extra handling is not a policy decision on your behalf.
- Put ranges, lengths, item constraints, and formats on their actual types using
  `Field`/`Annotated`. A list's length constraint does not constrain every item.
  Choose finite numeric values and precision where the operation requires them.
- Defaults are not validated by default. Use `validate_default` when defaults or
  factories must obey the same contract; keep defaults correctly typed. Prefer
  explicit factories for per-instance mutable values. An earlier-field-dependent
  factory or validator also depends on declaration order.

## Validators remain local and deterministic

Prefer declarative constraints, then an after field validator for a rule on an
already parsed value, or an after model validator for cross-field consistency.
Return the validated value or `self` with an accurate return type. A constraint
such as an end date following a start date is input consistency; resource
availability or permission to schedule belongs to the use case/domain owner.

Use before validators only for deliberate normalization of raw input: accept
`object`, narrow it, and avoid mutating caller-owned data that another union branch
may inspect. Plain validators can terminate normal validation; wrap validators
can skip or alter it. Use them only when their effect is necessary and tested,
not to turn rejected input into a successful default or bypass typing.

With Annotated validators, before/wrap ordering is right-to-left and after
ordering left-to-right; decorator validators join that pipeline. Prefer a
readable pipeline to relying on a clever ordering trick. `ValidationInfo.data`
contains only earlier validated fields, so model validators often express
cross-field rules more clearly. A subclass can override inherited validators;
do not assume all inherited rules still execute.

Validators must not perform network/database I/O, authorize an operation, emit
events, or coordinate a use case. Validation/revalidation can happen more than
once. Keep time/locale/context-dependent inputs explicit and deterministic; do
not use loosely typed validation context as a hidden service locator.

Raise `ValueError` or an appropriate `PydanticCustomError` for rejected input.
Do not manually assemble ValidationError internals or use removable `assert`
checks. V2 does not wrap validator `TypeError` as ValidationError; programming
errors must not be reported as ordinary invalid user input. Follow the
[Python typing policy](../python/typing-contracts.md) rather than copying `Any`
from illustrative upstream examples.

The optional [booking-window example](examples/boundary.md) shows strict JSON
input, a required nullable field, cross-field consistency, and a safe public
failure without moving availability checks into validation.

Sources: [models](https://docs.pydantic.dev/latest/concepts/models/),
[fields](https://docs.pydantic.dev/latest/concepts/fields/),
[strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/),
[conversion table](https://docs.pydantic.dev/latest/concepts/conversion_table/),
[validators](https://docs.pydantic.dev/latest/concepts/validators/),
[TypeAdapter](https://docs.pydantic.dev/latest/concepts/type_adapter/).
Boundary ownership and pure validators are framework policy; model selection
and strictness remain conditional on the real contract.
