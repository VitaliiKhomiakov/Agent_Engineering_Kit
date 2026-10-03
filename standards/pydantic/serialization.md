# Pydantic: serialization, aliases, and schemas

Read when changing response fields, wire names, partial updates, union selection,
or generated schemas. Return to the [entry](../python-fastapi.md).

## Public output is an explicit contract

- Choose fields by the public contract. An input or storage model is not
  automatically a response model; use a separate projection when visibility
  differs. Never dump an entire ORM/object graph and remove a few known secrets
  as the only defense against future fields becoming public.
- `model_dump()` uses Python representations by default; `mode="json"` produces
  JSON-compatible values, while `model_dump_json()` produces JSON text. TypeAdapter
  has corresponding methods, with `dump_json()` returning bytes. Select the form
  the caller needs; avoid double JSON encoding and do not assume all Python-mode
  values are directly encodable by another serializer.
- Field/model serializers change wire behavior, not input validity. Specify
  return types and test the result, relevant JSON mode, and schema. A computed
  field can add public data and execute code during serialization; it must not
  hide database access or unexpected expensive work.
- V2 normally serializes a model-valued field using its annotated model's fields,
  even when its runtime value is a subclass. `SerializeAsAny` or
  `serialize_as_any=True` opts into more runtime fields. Introduce that behavior
  only for a real contract and check disclosure; it is not a routine fix for a
  field missing from output. A direct dump of the subclass is still its own schema.
- `SecretStr`/`SecretBytes` mask common representations; they are not encryption,
  authorization, or a complete redaction policy. Custom serializers and explicit
  secret access can reveal values. Treat include/exclude flags and nested fields
  as contract choices, not proof that every logging/error path is safe.

## Names, presence, and partial updates

Distinguish Python field names from input aliases and output aliases. `alias`
can affect both directions; `validation_alias` and `serialization_alias` can
separate them. In 2.11+, `validate_by_alias` and `validate_by_name` make accepted
input names explicit, and `serialize_by_alias` controls output defaults.
Specify `by_alias` at an important output boundary when that makes the contract
clearer. Check precedence if aliases/generators/inheritance interact; accepting
both old and new names also needs a policy for conflicting simultaneous input.
Do not silently accept a legacy alias as a speculative compatibility feature.

For a patch, track what the caller supplied with `model_fields_set` or
`model_dump(exclude_unset=True)`. These use field presence, not truthiness.
`exclude_none=True` discards explicit clears; `exclude_defaults=True` can discard
an explicitly supplied false/zero/default value. They are not substitutes for
presence tracking. Aliased input is tracked by the Python field name, and later
assignment can change the set. Define null-clearing and nested-patch merge
semantics instead of making every field Optional by habit.

Parse only writable fields, build the complete candidate, then validate it before
replacing/persisting the prior state. `model_copy(update=...)` does not validate
its update. Neither construction nor a shallow merge provides authorization,
concurrency control, or an atomic database write. See [lifecycle](lifecycle.md).
The optional [patch and public-output example](examples/patches.md) preserves
omission/false/null, checks the complete candidate, and excludes server-owned data.

## Unions and generated schemas

For a wire contract with stable named variants, prefer a discriminated union
with Literal tags over overlapping alternatives whose branch choice is accidental.
A small unambiguous union is fine; a single model needs no discriminator.
Smart-union matching can change between Pydantic versions. Use an explicit
discriminator or deliberately ordered `union_mode="left_to_right"` if selection
must be stable, and test ambiguous inputs. A callable discriminator must handle
the forms needed during validation and serialization.

Generate schema in the mode consumers actually use: validation and serialization
can differ in required/computed fields, accepted representations, and output
types. Aliases and references also affect published contracts. `json_schema_extra`
changes documentation, not runtime validation. Custom validators/serializers can
express constraints that JSON Schema does not fully describe; inspect the affected
schema and test real accepted/rejected input and emitted output.

Preserve public schemas during refactoring or treat their change as intentional
compatibility work. Use a focused schema assertion/diff when schemas are consumed
by clients; do not snapshot every generated detail for an internal model. JSON
Schema generation is not proof of the complete OpenAPI/HTTP response contract;
check the consuming framework when that integration changes.

Sources: [serialization](https://docs.pydantic.dev/latest/concepts/serialization/),
[aliases](https://docs.pydantic.dev/latest/concepts/alias/),
[unions](https://docs.pydantic.dev/latest/concepts/unions/),
[JSON Schema](https://docs.pydantic.dev/latest/concepts/json_schema/),
[secret types](https://docs.pydantic.dev/latest/api/types/#pydantic.types.SecretStr).
Public-field ownership and compatibility are framework requirements; projections,
discriminators, and schema checks apply where those boundaries exist.
