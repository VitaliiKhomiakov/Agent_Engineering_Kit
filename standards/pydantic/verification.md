# Pydantic: checks, exposure, performance, and migration

Read when choosing model checks, changing exposed validation/serialization, or
upgrading Pydantic and its integrations. Return to the [Pydantic entry](../pydantic.md).
Use the shared [verification policy](../verification.md) to choose check depth.

## Test the contract that changed

- Exercise the real parsing mode and relevant differences: required/omitted/null,
  false/zero, coercions, extra fields, ranges, cross-field checks, and union tags.
  Select meaningful cases for the change, not all possible Pydantic behaviors.
  Constructor tests alone do not establish a JSON endpoint's parsing contract.
- For updates, check omission versus explicit clear/default, full-state validity,
  and no mutation/effect on rejection. For output, check public fields, aliases,
  representations, and exclusion of internal/subclass data when those can leak.
- When schemas are a published artifact, compare the affected validation/output
  schema and relevant consumers. Do not test only schema generation or copy a
  large schema snapshot as a substitute for runtime behavior.
- Use typed tests/doubles and the project's runner. A model test does not prove
  database uniqueness, authorization, concurrency, framework error mapping, or
  actual ORM attribute loading; use the appropriate adapter/integration check
  when that behavior changes. Documentation-only edits need artifact checks.

## Static typing alongside runtime validation

Retain the [Python strict baseline](../python/typing-contracts.md). For mypy with
Pydantic V2, enable `pydantic.mypy` and the existing policy settings
`init_typed = true`, `init_forbid_extra = true`, and
`warn_required_dynamic_aliases = true`. Pin compatible checker/plugin versions;
do not suppress diagnostics globally to make generated constructors pass.

Typed constructors accept values matching the internal annotated contract;
external unknown data belongs in `model_validate`/`model_validate_json` or a typed
adapter. A checker does not enforce Field ranges or model-validator logic. Test
the runtime rules separately. Prefer Annotated constraints to dynamically created
constrained types when the former preserve the intended static type clearly.
Static tools may not infer defaults/aliases hidden in Annotated metadata; use
normal Field assignment where constructor analysis needs those facts.

Methods such as `model_dump`, schema generation, and error details expose dynamic
library data. Keep it at the serialization/diagnostic boundary; do not return a
`dict[str, Any]` as an application contract or assign a concrete annotation to
pretend it was validated. State the actual analyzer scope and any library-API
limits of expression-Any checks. No custom mypy plugin or alternate checker is
required simply to add a model.

## Exposed input and diagnostics

Validation does not bound request bodies, parsing work, queue size, or a property's
I/O. Enforce upstream body/collection limits relevant to the interface, avoid
expensive unbounded custom validators, and preserve the operation's time budget.
Define finite numbers, allowed destinations/paths, and authorization where the
actual consumer requires them; a parsed URL is not permission to fetch it.

Map ValidationError to the agreed safe public error contract. Its details may
contain the original input, locations derived from input, and custom error
context. Do not log or return raw `errors()`, `json()`, or exception strings by
default. `hide_input_in_errors=True` hides input in the formatted message, not
every structured error representation. Even `include_input=False` does not
sanitize custom messages/context; an allowlisted projection and deliberate
redaction are safer when exposing diagnostics. Never convert an internal
TypeError into a successful result or silently discard a rejected record.

## Optimize only an observed cost

Prefer the direct JSON validation path when JSON is the input and it preserves
the required semantics; before/wrap validators can change performance tradeoffs.
Reuse TypeAdapters for repeated work. Typed concrete containers and discriminated
unions may reduce unnecessary work, but measure representative payloads and
failure paths. Do not replace validation with `Any`, `SkipValidation`,
`model_construct`, or ignored serialization warnings to satisfy a benchmark.
Trusted construction and custom core schemas need a real use case and explicit
validation ownership. Partial/experimental validation is not complete acceptance
of an untrusted write request.

## Versions and migration

Check the actual Pydantic, pydantic-core, Python, checker, framework, and optional
package versions. This stage researched/executed **Pydantic 2.13.4**, whose installed
metadata requires **pydantic-core 2.46.4** and Python **>=3.9**. The examples target
this pair and Python 3.11+; these are example compatibility limits, not the target
project's Python floor. Preserve its declared support range and actual deployed
interpreter under the [Python compatibility policy](../python/verification.md#version-sensitive-decisions).
Adopting this profile does not raise that range or make a 3.11-only example
compatible with an older interpreter. Do not pin or upgrade pydantic-core
independently of the supported Pydantic dependency set.

| Compatibility trigger | What to verify |
| --- | --- |
| V1 to V2 | `model_validate`/`model_dump` APIs, ConfigDict, validator signatures/error semantics, required nullable fields, coercions, schema, equality, and subclass serialization; renaming methods alone is insufficient |
| V1 coexistence | Keep V1/V2 contracts separate and verify framework support; mixing model generations inside a model's fields/generics is unsupported. Python 3.14 compatibility depends on the exact V1 release/namespace: 1.10.25 added minimal support, despite older documentation saying V1 cannot run there |
| Aliases on V2 before 2.11 | Newer `validate_by_name`/`validate_by_alias`/`serialize_by_alias` controls are unavailable; use that version's documented configuration rather than copying current settings |
| Minor/patch dependency upgrade | Check affected coercion, union choice, serializers, schema and integration behavior; `latest` documentation is not proof of the installed behavior |
| Runtime annotation/typing changes | Check supported Python/checker versions, forward-reference resolution, generics, and libraries that inspect annotations; avoid unrequested interpreter migration |
| BaseSettings or optional types | V2 settings live in `pydantic-settings`; email/other optional types may need extra packages. Use the project's existing dependency policy |

Keep migration bounded to the authorized contract, including public formats and
callers. `pydantic.v1` can be a staged compatibility tool, not permission to create
an indefinite dual model hierarchy. No migration is triggered by adopting this
profile. FastAPI integration belongs to the separate
[FastAPI entry](../fastapi.md), applied only where FastAPI is used; SQLAlchemy and psycopg have separate profiles
selected only when those dependencies are present or explicitly requested.

Sources: [mypy integration](https://docs.pydantic.dev/latest/integrations/mypy/),
[errors](https://docs.pydantic.dev/latest/errors/errors/),
[performance](https://docs.pydantic.dev/latest/concepts/performance/),
[migration](https://docs.pydantic.dev/latest/migration/),
[version policy](https://docs.pydantic.dev/latest/version-policy/),
[2.13.4 release](https://github.com/pydantic/pydantic/releases/tag/v2.13.4),
[V1 Python 3.14 change](https://github.com/pydantic/pydantic/pull/12636).
