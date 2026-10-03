# Pydantic engineering practices: research and adoption

Research started and primary sources checked: **2026-09-21**. Scope: **K04,
Pydantic**, under the [practice plan](../plans/2026-09-21-engineering-practices.md).
The [Python/FastAPI profile](../../standards/python-fastapi.md) remains the entry;
four Pydantic sections and two optional examples provide conditional detail.
This note is evidence, not a mandatory instruction or an installed resource.

## Baseline, scope, and evidence quality

The existing profile already required explicit coercion policy, local field/model
validation without I/O, named typed boundaries, and distinct domain invariants.
K04 explains the library mechanisms and their limits: validation entry points,
presence/defaults, validators, aliases, schemas, serialization, model lifecycle,
integration ownership, static checks, and migration. It preserves Python rules
and FastAPI-specific routing/wiring/file-move guidance. It does not implement
K05, select an ORM, add settings infrastructure, or upgrade any dependency.

| Evidence checked | Applicability |
| --- | --- |
| Installed Pydantic **2.13.4**, pydantic-core **2.46.4**; package metadata requires that exact core version and Python **>=3.9** | Executed library baseline; preserve the installed compatible pair. The workspace separately requires Python >=3.11 |
| Python **3.12.3**, mypy **2.1.0**, pytest **9.1.1** | Actual tools; examples use Python 3.11 syntax/APIs and existing dependencies, not another interpreter |
| [Official documentation](https://docs.pydantic.dev/latest/) labels its overview v2.13.4; [2.13.4 release](https://github.com/pydantic/pydantic/releases/tag/v2.13.4) identifies the release | `latest` is moving, and current documentation can differ from older examples or releases; inspect applicable contracts and local behavior |
| [Alias configuration](https://docs.pydantic.dev/latest/concepts/alias/) and [ConfigDict](https://docs.pydantic.dev/latest/api/config/) | `validate_by_alias`, `validate_by_name`, and `serialize_by_alias` are 2.11+ controls; do not copy them into older projects unconditionally |
| Installed `pydantic.v1.VERSION` is **1.10.26**; local V1 typing code includes a Python 3.14 branch | A V2 package version alone does not identify the V1 compatibility namespace; this stage did not execute Python 3.14 or a V1 model suite |

An evidence discrepancy matters for migration: the
[V1 overview](https://pydantic.dev/docs/validation/1.10/overview/) and earlier
[2.12 announcement](https://pydantic.dev/articles/pydantic-v2-12-release) say V1
does not work on Python 3.14. Later upstream
[change #12636](https://github.com/pydantic/pydantic/pull/12636), shipped in the
1.10.25 line and retained in
[1.10.26](https://github.com/pydantic/pydantic/releases/tag/v1.10.26), adds minimal
support. The adopted recommendation therefore checks the exact V1 release,
namespace, interpreter, and framework instead of repeating a universal ban or
claiming full support from one fix. V1/V2 model nesting is still not a supported
way to mix model generations. [Migration](https://docs.pydantic.dev/latest/migration/).

## Coverage and strength

**R** means an Agent_Engineering_Kit requirement justified by existing contract,
strict-typing, invariant, effect, or disclosure policy in
[core](../../standards/core.md). **D** is a recommended default with a meaningful
alternative; **O** is an optional technique whose stated problem must exist.
Pydantic facts do not independently mandate a design, strict runtime parsing,
or the adoption of another package. Unless identified otherwise, library-specific
recommendations below use the 2.13.4/V2 baseline and were checked on 2026-09-21.

| Research area | Decisions and adoption owner |
| --- | --- |
| Architecture and boundaries | Parse at the owning boundary; keep transport, storage, public output, and independent domain responsibilities clear; [validation](../../standards/pydantic/validation.md) |
| Construction, dependencies, patterns | BaseModel versus TypeAdapter/dataclass/RootModel, Annotated reuse, conditional adapters/projections; validation and [lifecycle](../../standards/pydantic/lifecycle.md) |
| Typed contracts, input, invariants, errors | Coercions, required/null/default, pure validators, state-owner rules and safe error mapping; validation and [verification](../../standards/pydantic/verification.md) |
| State, concurrency, cancellation, lifetime | Revalidation, copying, assignment, shallow freezing and application-owned effects/resources; lifecycle |
| Persistence and external APIs | Explicit projections, attribute loading, settings bootstrap, transactions outside validation; lifecycle |
| Behavior checks and review | Actual Python/JSON mode, failed replacement, output/schema checks, static plugin; verification |
| Security, operations, performance | Disclosure, error-input exposure, parsing bounds, schema/adapter reuse, measured optimization; verification and [serialization](../../standards/pydantic/serialization.md) |
| Versions and migration | V1/V2 contracts, minor-release behavior, aliases, Python/typing/core compatibility; verification |

Pydantic has no transaction manager, task scheduler, cancellation protocol, or
durable persistence mechanism. Those parts of coverage concern integration
boundaries and stay with their existing Python/application owners; inventing
Pydantic-specific counterparts would add no useful guarantee.

## Model and validation decisions

| Strength; problem and condition | Adopted form | Simpler alternative or cost; evidence |
| --- | --- | --- |
| R: a dynamic external payload crosses a typed boundary | Parse to a named owned model at the adapter, not an unchecked cast or dynamic dump passed through the core | A small parser may suffice when Pydantic is absent; a library is not required by a Python task. [Models](https://docs.pydantic.dev/latest/concepts/models/) and existing Python policy |
| D: a named structured record; O: non-record/root contracts | BaseModel for records, typed TypeAdapter for scalar/union/collection, RootModel when root-model identity is useful | Avoid wrapper objects created only to validate a list; preserve an existing dataclass where that is its real role. [TypeAdapter](https://docs.pydantic.dev/latest/concepts/type_adapter/), [dataclasses](https://docs.pydantic.dev/latest/concepts/dataclasses/) |
| D: explicit coercion/extra policy for a public contract | Strict parsing and `extra="forbid"` for a closed write contract when conversions/unwritable keys are invalid | Lax parsing or ignored new upstream fields may be correct elsewhere; changing defaults can reject existing clients. Static strict typing is a separate rule. [Strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/), [conversion table](https://docs.pydantic.dev/latest/concepts/conversion_table/) |
| R: preserve presence and validity; D: declarative constraints | Requiredness, nullable types, explicit defaults, Field/Annotated constraints on the actual element/type; validate defaults where their contract needs it | Avoid truthiness and assumptions that Optional means optional input. Extra validation/default factories have construction semantics to preserve. [Fields](https://docs.pydantic.dev/latest/concepts/fields/) |
| D: parsed field/cross-field checks; O: raw/wrap pipelines | Prefer constraints and after validators; before validators narrow object input without mutating caller-owned data; wrap/plain only when their bypass/order effects are intended | A simple constraint is easier to inspect; pipelines/inheritance can hide ordering or overridden rules. Return value/self accurately. [Validators](https://docs.pydantic.dev/latest/concepts/validators/) |
| R: validation must not coordinate effects or replace live-state decisions | Deterministic local consistency rules, with business transitions/authorization outside transport models | A database lookup inside a validator hides lifetime and repeat-execution risks. This is framework policy, not a limitation on Python method bodies. [Core ownership](../../standards/core.md) |

The [booking example](../../standards/pydantic/examples/boundary.md) deliberately
uses JSON mode: strict JSON accepts date strings while strict Python input needs
date objects. It requires a nullable note, rejects coercions/unknown fields, and
checks date ordering. It does not infer room availability from a valid model.
The existing [Python domain example](../../standards/python/examples/domain.md)
retains ownership of state-dependent publication rules and valid incomplete
drafts; it is referenced rather than rewritten as a Pydantic entity.

**R — typed and inspectable errors.** ValueError/PydanticCustomError can express
rejected input; unexpected TypeError in V2 validators is not automatically a
ValidationError. Keep application error mapping deliberate and never convert a
programming failure into invalid input or success. Do not construct private
validation internals or use removable assertions for required checks.
[Validator migration](https://docs.pydantic.dev/latest/migration/#typeerror-is-no-longer-converted-to-validationerror-in-validators).

## Serialization and schema decisions

**R — public visibility has an owner.** A response model/projection should expose
only the intended fields. Python-mode dumps, JSON-compatible data, JSON text,
and TypeAdapter JSON bytes serve different callers. Separate contracts when
visibility or writability differs; do not duplicate identical DTOs merely to
cross a folder. Field serializers, computed fields, and runtime subtype dumping
can change the output and must preserve its actual public meaning.
[Serialization](https://docs.pydantic.dev/latest/concepts/serialization/).

**D — explicit names and variants.** Input/output aliases can differ; use the
installed version's alias controls and verify the real serialization call.
AliasChoices/generators are optional compatibility/convention tools, with
precedence and static-constructor costs. For genuinely distinct wire variants,
a tagged union is more stable than overlapping smart-union guesses; a simple
unambiguous union needs no tag. The upstream smart algorithm may evolve, so
version pinning and relevant input tests still matter.
[Aliases](https://docs.pydantic.dev/latest/concepts/alias/),
[unions](https://docs.pydantic.dev/latest/concepts/unions/).

**R — preserve partial-update meaning.** Use supplied-field tracking, not falsey
values or excluding None/defaults. Validate the full candidate before mutation
or effects, including rules involving unchanged fields. A generic dump/merge
costs more implicit key handling; for a small named contract an explicit typed
replacement is clearer. Neither approach supplies authorization or database
atomicity. The [patch example](../../standards/pydantic/examples/patches.md) keeps
omission distinct from false/null, denies a server-owned token update, validates
the complete configuration, and constructs a separate public projection.
[Presence and exclusion](https://docs.pydantic.dev/latest/concepts/serialization/#excluding-and-including-fields-based-on-their-value),
[copy API](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_copy).

**R where published — schema compatibility.** Choose validation/serialization
mode, aliases, and relevant references for the consumer. Metadata additions do
not implement runtime validation, and custom Python consistency logic may not
be fully expressible in JSON Schema. Focused schema checks supplement real
parsing/output tests; whole-schema snapshots are unnecessary for every internal
model. HTTP/OpenAPI integration remains K05 or the affected application task.
[JSON Schema](https://docs.pydantic.dev/latest/concepts/json_schema/).

## State, persistence, resources, and performance

**R — owned state; D — validated replacement.** Model creation is not a perpetual
validity guarantee. Ordinary mutation, nested mutable objects, trusted construction,
copy updates, and reused instances each have different behavior. Prefer an owned
immutable snapshot when that suits the contract, but do not infer deep immutability
or thread safety from `frozen`. Validate complete candidates before making them
current; choose revalidation only where trust/lifetime requires it and on the
relevant nested types. Existing instance validation is not always a fresh parse.
[Model lifecycle](https://docs.pydantic.dev/latest/concepts/models/),
[revalidation configuration](https://docs.pydantic.dev/latest/api/config/).

Three focused local observations on 2.13.4 informed the guidance:

- A valid interval with assignment validation raised from an after model-validator
  when its lower endpoint was changed beyond the upper endpoint, yet retained the
  changed field. Treating rejected assignment as rollback would be unsafe.
- `model_copy(update=...)` produced an inconsistent interval without invoking that
  consistency check, as documented by the copy API.
- `hide_input_in_errors=True` removed a fixture input from `str(ValidationError)`,
  while `errors()` still contained that input. Formatted-error hiding is not
  structured-output sanitization.

These are bounded probes, not a library regression campaign or a claim about all
versions/failure types. They justify the complete-replacement and safe-output
contracts tested in the examples. In particular, the assignment observation is
not labeled a defect in Pydantic or used to change installed library code.

**D — explicit projection at integration boundaries.** Attribute-based validation
is useful when intended but can execute properties or ORM lazy loads. Fetch and
map the required values while their session/adapter owns them; do not hide queries,
transactions, or client lifetime inside validators/serializers. A narrow adapter
is optional when it adds a real translation boundary; a forwarding Repository
or Factory for every model is unnecessary. Settings are loaded in bootstrap via
the project's installed `pydantic-settings` policy if present. No ORM/settings
package is added by this stage.
[Attribute models](https://docs.pydantic.dev/latest/concepts/models/#arbitrary-class-instances),
[settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/).

**D — measure; O — specialized optimization.** Reusing TypeAdapters and direct
JSON validation can reduce setup/parsing work; check semantics and before/wrap
validator tradeoffs. Concrete data shapes, tagged unions, custom schemas, and
trusted construction have different costs. Optimize a real measured bottleneck,
not a generic benchmark score. The upstream performance page mentions `Any` to
skip validation; that optional technique conflicts with this framework's strict
contract policy and is not adopted. Likewise its discussion of side-effectful
validators and `model_construct` does not override our rule to keep validators
pure. [Performance](https://docs.pydantic.dev/latest/concepts/performance/).

## Verification, disclosure, and migration

**R — protect exposed data; D — safe error projection.** Raw structured errors can
contain input, custom context, and input-derived locations. SecretStr masks common
representations, not every custom serializer or error/log path. Project only
agreed public error fields/codes and enforce input/resource bounds outside model
validation where needed. Parsed URLs/paths still need authorization and safe
consumption; an accepted model is not a security decision by itself.
[Error handling](https://docs.pydantic.dev/latest/errors/errors/),
[secret type API](https://docs.pydantic.dev/latest/api/types/#pydantic.types.SecretStr).

**R — existing static/gate policy; D — relevant contract checks.** The mypy plugin
plus typed/extra-forbidding generated constructors and dynamic-alias diagnostics
supports the existing no-Any policy. Runtime constraints still require behavior
checks. External values use model validation APIs; deliberately invalid input
tests should not force casts or ill-typed constructors. Schema/error/dump APIs
return dynamic data: keep it local to their adapter/test boundary and state where
expression-Any checks apply. Test the parsing mode, failure cases, replacement
integrity, output exposure, and affected schema rather than every library feature.
[Mypy integration](https://docs.pydantic.dev/latest/integrations/mypy/),
[shared verification](../../standards/verification.md).

**R — preserve versions/contracts; O — staged migration when authorized.** V1/V2
migration includes validator semantics, nullable required fields, defaults,
configuration, dumps, schemas, equality, and subtype serialization. Aliases and
runtime annotation support have later V2 minimums. Follow the installed dependency
set and relevant minor/patch behavior, not an assumption that only majors affect
observable output. Experimental features, including partial validation, need an
explicit suitability decision. An adoption stage does not itself authorize an
upgrade or a V1 compatibility hierarchy.
[Migration](https://docs.pydantic.dev/latest/migration/),
[version policy](https://docs.pydantic.dev/latest/version-policy/).

## Delivery and limits

Keep the 17 existing profile IDs. Add six resources to `python-fastapi` and add
`pydantic` to that profile's technology match: metadata inspection already knows
this fact, so a project declaring only Pydantic in its passport can receive the
combined entry. Ordinary Python projects still receive its available resources,
with Pydantic/FastAPI reading explicitly conditional. Unrelated stacks do not.
No metadata/composer implementation or additional automatic native route changes.

The [practice plan](../plans/2026-09-21-engineering-practices.md) records actual
commands, versions, results, scope preservation, synthetic delivery checks, and
the checkpoint. Example execution covers the stated Python/Pydantic pair only.
No live HTTP/ORM/settings service, V1 or multi-version runtime suite, native-client
pilot, security scanner, or performance benchmark is claimed. Next topic after
review: **K05 — FastAPI**.
