# Python

Apply to Python work with the [common rules](core.md). Pydantic and FastAPI
have separate profiles, selected only where used.
Read only relevant sections; examples and research are optional. Stop once the
task requirements are known, without loading linked files recursively.

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

Availability in a bundle does not imply mandatory reading. Follow examples only
when they resolve a current decision; general design and size rules stay in core.

## Evidence

[Python research](../docs/research/2026-09-21-python-engineering-practices.md)
records primary sources checked on 2026-09-21, alternatives and version limits.
The [practice plan](../docs/plans/2026-09-21-engineering-practices.md) records
example and delivery checks.
