# Pydantic

Apply only where Pydantic is used, with [Python](python.md) and the
[common rules](core.md). FastAPI is a separate selection; validation libraries
do not imply a web framework.
Read only relevant sections; examples and research are optional. Stop once the
task requirements are known, without loading linked files recursively.

## Pydantic essentials

- Establish the installed version; these details target V2, with newer APIs
  identified where relevant. Do not apply another major version's rules.
- Choose accepted coercions, extra fields, required/null/default semantics, and
  public output explicitly. Type annotations alone do not settle these contracts.
- Keep field/cross-field validators local and free of I/O or use-case coordination.
  Input consistency does not replace domain invariants, authorization, or transactions.
- Validation does not make later mutation, copying, or serialization safe by
  default. Validate complete updates before effects and expose only public fields.

## Read by task

| Task touches | Read |
| --- | --- |
| Pydantic model choice, fields, parsing modes, coercions, validators | [Models and validation](pydantic/validation.md) |
| Pydantic output fields, aliases, patches, unions, JSON Schema | [Serialization and schemas](pydantic/serialization.md) |
| Pydantic mutation/copying, trust, ORM/SDK/settings boundaries | [Model lifetime and integration](pydantic/lifecycle.md) |
| Pydantic tests, mypy plugin, errors, performance, version migration | [Verification and compatibility](pydantic/verification.md) |

Availability in a bundle does not imply mandatory reading. Follow examples only
when they resolve a current decision; general design and size rules stay in core.

## Evidence

[Pydantic research](../docs/research/2026-09-21-pydantic-engineering-practices.md)
records primary sources checked on 2026-09-21, alternatives and version limits.
The [practice plan](../docs/plans/2026-09-21-engineering-practices.md) records
example and delivery checks.
