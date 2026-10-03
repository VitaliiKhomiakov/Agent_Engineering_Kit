# Python / FastAPI

Apply this entry to Python work with the [common rules](core.md). Read only the
sections relevant to the task, and stop once its applicable rules are known.
Examples and research are optional; do not load all linked files recursively.

## Essential guidance

- Establish the supported Python range, actual interpreter, and dependency
  versions. Preserve compatibility; do not upgrade to use a newer idiom.
- Keep cohesive modules and explicit dependencies. Related classes may share a
  file; a small script or library does not need a service-layer scaffold.
- Use strict, named typed contracts, including tests. Do not introduce `Any`,
  untyped functions, or typing bypasses. Runtime input validation is separate
  from annotations and from state-dependent business invariants.
- Give mutable state, external effects, resources, and concurrent work explicit
  owners. Preserve cancellation, cleanup, and error contracts.
- Use the project's analyzer and formatting tools, with proportionate checks
  under the shared [verification policy](verification.md).

## Read by task

| Task touches | Read |
| --- | --- |
| Modules, imports, construction, patterns, package/dependency boundaries | [Structure and dependencies](python/structure.md) |
| Signatures, DTOs, input parsing, domain state, errors, strict analyzer settings | [Typing and contracts](python/typing-contracts.md) |
| Async work, threads/processes, shared state, resources, transactions, external calls | [Execution and resources](python/execution-resources.md) |
| Tests, exposed security boundaries, measured performance, Python/dependency migration | [Verification and compatibility](python/verification.md) |
| Pydantic model choice, fields, parsing modes, coercions, validators | [Models and validation](pydantic/validation.md) |
| Pydantic output fields, aliases, patches, unions, JSON Schema | [Serialization and schemas](pydantic/serialization.md) |
| Pydantic mutation/copying, trust, ORM/SDK/settings boundaries | [Model lifetime and integration](pydantic/lifecycle.md) |
| Pydantic tests, mypy plugin, errors, performance, version migration | [Verification and compatibility](pydantic/verification.md) |
| HTTP routes, input/output models, domain calls, errors, OpenAPI contracts | [Transport and contracts](fastapi/transport.md) |
| Depends, caching, yield scopes, lifespan, transactions, background work | [Dependencies and lifetime](fastapi/dependencies-lifetime.md) |
| Async/sync execution, streaming, security, middleware, deployment, performance | [Runtime and operations](fastapi/runtime-operations.md) |
| HTTP/lifespan tests, dependency overrides, file moves, FastAPI stack upgrades | [Verification and compatibility](fastapi/verification.md) |

Availability in an installed bundle does not imply mandatory reading. Several
sections may apply; follow example links only when they resolve a current decision.
General design principles and size thresholds remain owned by the common rules.
Pydantic routes apply only where that library is used; they do not require it
for every Python task.

## Pydantic essentials

- Establish the installed version; these details target V2, with newer APIs
  identified where relevant. Do not apply another major version's rules.
- Choose accepted coercions, extra fields, required/null/default semantics, and
  public output explicitly. Type annotations alone do not settle these contracts.
- Keep field/cross-field validators local and free of I/O or use-case coordination.
  Input consistency does not replace domain invariants, authorization, or transactions.
- Validation does not make later mutation, copying, or serialization safe by
  default. Validate complete updates before effects and expose only public fields.

FastAPI routes and the essentials below apply only where FastAPI is used.

## FastAPI essentials

- Establish FastAPI, Starlette, Pydantic, server, and integration versions before
  using version-sensitive APIs. The researched baseline is FastAPI 0.138.0/V2.
- Keep HTTP parsing, dependencies, and error mapping at the transport boundary;
  independent business code receives ordinary typed values and ready dependencies.
  Make public response fields explicit and verify the actual HTTP contract.
- Match resource lifetime to its last consumer, including streams and background
  work. Complete required effects before reporting success; keep blocking calls
  off the event loop and give startup, cleanup, and cancellation clear owners.

## Evidence

[Python research](../docs/research/2026-09-21-python-engineering-practices.md),
[Pydantic research](../docs/research/2026-09-21-pydantic-engineering-practices.md), and
[FastAPI research](../docs/research/2026-09-21-fastapi-engineering-practices.md)
record primary sources checked on 2026-09-21, alternatives, and version limits.
The [practice plan](../docs/plans/2026-09-21-engineering-practices.md) records
example and delivery checks.
