# FastAPI

Apply only where FastAPI is used, with [Python](python.md),
[Pydantic](pydantic.md) and the [common rules](core.md). Select persistence
profiles separately for the actual database/driver stack.
Read only relevant sections; examples and research are optional. Stop once the
task requirements are known, without loading linked files recursively.

## FastAPI essentials

- Establish FastAPI, Starlette, Pydantic, server, and integration versions before
  using version-sensitive APIs. The researched baseline is FastAPI 0.138.0/V2.
- Keep HTTP parsing, dependencies, and error mapping at the transport boundary;
  independent business code receives ordinary typed values and ready dependencies.
  Make public response fields explicit and verify the actual HTTP contract.
- Match resource lifetime to its last consumer, including streams and background
  work. Complete required effects before reporting success; keep blocking calls
  off the event loop and give startup, cleanup, and cancellation clear owners.

## Read by task

| Task touches | Read |
| --- | --- |
| HTTP routes, input/output models, domain calls, errors, OpenAPI contracts | [Transport and contracts](fastapi/transport.md) |
| Depends, caching, yield scopes, lifespan, transactions, background work | [Dependencies and lifetime](fastapi/dependencies-lifetime.md) |
| Async/sync execution, streaming, security, middleware, deployment, performance | [Runtime and operations](fastapi/runtime-operations.md) |
| HTTP/lifespan tests, dependency overrides, file moves, FastAPI stack upgrades | [Verification and compatibility](fastapi/verification.md) |

Availability in a bundle does not imply mandatory reading. Follow examples only
when they resolve a current decision; general design and size rules stay in core.

## Evidence

[FastAPI research](../docs/research/2026-09-21-fastapi-engineering-practices.md)
records primary sources checked on 2026-09-21, alternatives and version limits.
The [practice plan](../docs/plans/2026-09-21-engineering-practices.md) records
example and delivery checks.
