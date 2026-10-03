# FastAPI dependencies and lifetime

Read when changing dependency wiring, `yield`, lifespan, transactions, streaming
resources, or background work. General resource/concurrency rules remain in
[Python execution](../python/execution-resources.md). Checked: FastAPI 0.138.0.

## Dependency ownership

Use `Annotated[T, Depends(provider)]` for typed transport injection. Ordinary
functions are usually sufficient providers; a callable instance is useful for
configuration or state with an explicit owner. Do not add a DI container or
service locator just because FastAPI supports dependency graphs. Application
objects receive ready dependencies and can be called without FastAPI.

FastAPI normally caches a dependency result within a request. This is neither a
process singleton nor a transaction guarantee. Use `use_cache=False` only when
repeated evaluation is intended and its effects/lifetime are understood. Do not
use dependency caching as authorization-result caching across users or requests.
[Dependency reuse](https://fastapi.tiangolo.com/tutorial/dependencies/sub-dependencies/).

Use router/app dependencies for cross-cutting request requirements where they
apply to every matched operation. If the handler needs a returned value, declare
that dependency in its parameters. Make object/tenant authorization explicit at
the operation boundary; an authentication provider alone cannot decide it.

## Match cleanup to the last consumer

Use `try/finally` or a context manager inside a `yield` dependency. Release on
normal and exceptional paths and re-raise exceptions unless deliberately mapped.
Swallowing an exception after `yield` hides the failure; it does not recover a
valid response.

| Consumer | Appropriate lifetime on the checked stack |
| --- | --- |
| Handler consumes everything and returns an independent value/body | `Depends(..., scope="function")` can release before sending the response |
| Stream still reads a cursor, file, or upstream response | Default `scope="request"` keeps the dependency through response sending; bound stream duration and resource use |
| Reused client/pool for many requests | App lifespan, with a separate request/operation scope for sessions or streams |
| Work continuing independently of the request | Its own resource acquisition and cleanup; pass stable IDs or immutable data |

`scope="function"` was added in FastAPI 0.121.0. Default cleanup moved back to
after sending in 0.118.0; do not apply current timing to older deployments.
A request-scoped dependency cannot depend on a function-scoped resource that
would disappear before its cleanup. A function-scoped dependency can use either
scope. Keep dependency graphs small enough to inspect their lifetime ordering.
[Yield scopes](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/),
[history](https://fastapi.tiangolo.com/advanced/advanced-dependencies/).

## Lifespan and persistence

Prefer `FastAPI(lifespan=...)` for startup/shutdown resources: create loop-bound
clients and pools there, release them on exit, and avoid import-time network I/O.
Supplying lifespan disables legacy startup/shutdown event handlers; migrate their
behavior together. Test mounted applications and included-router lifespans in the
actual composition rather than assuming each sub-application starts automatically.
[Lifespan](https://fastapi.tiangolo.com/advanced/events/).

Expose resources through a typed provider or container with clear initialization
and ownership. Dynamic `app.state` access is not an excuse for unchecked casts.
A closure captured by an app factory is enough for a small app. Lifespan resources
exist per worker process; shared persistent state needs an external owner.

A yielded session controls lifetime, not the business transaction. Complete the
required commit and map expected commit failures before a success response is
sent. Do not hide the commit in default request-scope teardown, where failure can
arrive after the client saw success. On failure, roll back through the session's
own contract. Build public output while required data is available; do not let
serialization trigger unplanned lazy loads after closing the session.

An operation context manager or unit of work is optional when several effects
must be atomic. A direct transaction block is simpler for one cohesive operation.
Use the installed ORM/driver's concurrency and transaction rules; FastAPI does not
make a shared session safe. No ORM or Repository abstraction is required here.

## Background and streaming effects

`BackgroundTasks` suits small in-process work whose loss/failure contract is
acceptable. It runs after response sending, is not a durable queue, and cannot
retroactively change an already sent success. Sequential tasks stop when one
raises. Acquire needed resources inside each task instead of retaining a request
session or request object. Required durable delivery needs an explicit persisted
handoff, retry/idempotency policy, and worker only when the product requires it.
[Background tasks](https://starlette.dev/background/).

For streaming, validate upstream status/authorization before returning the stream
where possible. Once headers/body start, a later failure cannot become a fresh
JSON error response. Own cleanup for exhaustion, failure, disconnect, and shutdown;
avoid accumulating the whole body solely to simulate streaming. See
[runtime limits](runtime-operations.md) and the optional
[resource lifetime example](examples/lifetime.md).
