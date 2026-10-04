# FastAPI verification and compatibility

Read when testing, reviewing, moving files, or upgrading the HTTP stack. Follow
the shared [verification policy](../verification.md); do not turn a small change
into a mandatory end-to-end suite or introduce another test framework to move a
class. [Python verification](../python/verification.md) owns analyzer conventions.
Return to the [FastAPI entry](../fastapi.md).

## Behavior and test isolation

Check business rules directly when they are independent of HTTP, then use the
existing HTTP harness for the affected boundary. Select cases from actual risks:
input source/coercion/presence, rejected writes, authorization, public fields,
status/error/header contracts, and unchanged state on expected failure. Test the
real HTTP representation rather than inferring it from a model-only call.

Use `with TestClient(app)` when startup/shutdown behavior matters. A client created
without entering its context does not execute lifespan. HTTPX `ASGITransport`
does not trigger lifespan either; use the project's lifecycle harness when an
async test needs same-loop resources. Keep clients/resources on their owning
event loop. Avoid sleeps for synchronization.
[Lifespan tests](https://starlette.dev/lifespan/),
[HTTPX transport](https://www.python-httpx.org/advanced/transports/).

Construct an isolated app or override the exact provider callable through
`app.dependency_overrides`. Restore the previous override mapping in fixture
teardown/`finally`, including on failure. Overrides bypass the original provider
and its sub-dependencies: a passing test with fake auth/storage does not prove
real authorization, rollback, or integration behavior.
[Overrides](https://fastapi.tiangolo.com/advanced/testing-dependencies/).

Keep normal TestClient exception propagation to expose programming defects.
Use `raise_server_exceptions=False` only when deliberately checking the rendered
500 response. Invalid server output must not be reported as invalid client input.
[Test client](https://starlette.dev/testclient/).

For resource changes, check acquisition, cleanup, failure, and the last consumer.
For streams, check upstream rejection before headers and cleanup after consumption
or failure. An in-process client can buffer responses; it does not establish
network pacing, backpressure, disconnect cancellation, proxy limits, or graceful
server termination. Use a bounded real-server check only when that behavior is
affected. Durable delivery/real database isolation require their own integration
evidence; an in-memory fake cannot establish them.

## Preserve contracts during change

When moving files, preserve public imports, registered routers, serialization,
CLI/string imports, dependency-provider identities, and relevant ORM registration.
Compare affected OpenAPI paths, operation IDs, component names, required/null
fields, aliases, media types, and success/error schemas. Use a targeted schema
assertion or diff, not a snapshot of every unrelated endpoint by default.

Record the compatible Python/FastAPI/Starlette/Pydantic/AnyIO/HTTPX/server set and
use the project's existing lock/constraints workflow. Do not upgrade the runtime
just to use an example or independently force incompatible transitive versions.
The executable baseline is Python 3.12.3, FastAPI 0.138.0, Starlette 1.3.1,
Pydantic 2.13.4, AnyIO 4.14.0, and HTTPX 0.28.1; Uvicorn 0.49.0 was inspected,
not run as a server. Examples target Python 3.11 syntax but ran on 3.12 only.

Version-sensitive review triggers:

- Yield dependencies: 0.118.0 restored cleanup after response sending; 0.121.0
  added `scope="function"`. Recheck streams and commit timing when crossing them.
- FastAPI 0.126.0 removed Pydantic V1 package support; 0.128.0 removed the
  `pydantic.v1` compatibility path. This baseline requires V2. Pydantic's own
  compatibility namespace does not imply FastAPI supports it.
- FastAPI 0.132.0 enabled strict JSON Content-Type checking by default. Correct
  callers and test actual missing/wrong-header behavior before relaxing it.
- FastAPI 0.137.0 changed included-router representation into a tree. Code that
  inspects or mutates a presumed flat `router.routes` list needs review; preserve
  behavior through public HTTP/OpenAPI contracts instead of private traversal.
- Current upstream documentation may describe newer Starlette APIs than the
  installed stack or FastAPI supports. Validate cross-library compatibility
  before copying typed state, body-limit, middleware, or lifecycle recipes.
- Starlette 1.3.1's TestClient prefers HTTPX2 and emits a deprecation warning with
  the installed HTTPX fallback. Warnings-as-errors can stop tests at import before
  exercising the app. Inspect the compatible test stack and migration policy;
  do not hide the warning globally or upgrade dependencies merely for an example.

[FastAPI releases](https://fastapi.tiangolo.com/release-notes/),
[yield history](https://fastapi.tiangolo.com/advanced/advanced-dependencies/),
[Starlette test-client compatibility](https://starlette.dev/testclient/).

Optional examples: [HTTP boundary](examples/http-boundary.md) and
[lifetime](examples/lifetime.md). The
[research note](../../docs/research/2026-09-21-fastapi-engineering-practices.md)
records sources/decisions; the
[practice plan](../../docs/plans/2026-09-21-engineering-practices.md)
records actual checks and limits. Neither is mandatory reading for routine work.
