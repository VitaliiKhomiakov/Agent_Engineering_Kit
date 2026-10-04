# FastAPI engineering practices: research and adoption

Research started and primary sources checked: **2026-09-21**. Scope: **K05,
FastAPI**, under the [practice plan](../plans/2026-09-21-engineering-practices.md).
The [Python/FastAPI profile](../../standards/python-fastapi.md) remains a short
entry; four conditional FastAPI sections and two optional examples supply detail.
This note is reference evidence, not a required instruction or installed resource.

## Baseline and scope

Existing guidance already separated HTTP from independent business code, required
typed DTOs/public output and bootstrap wiring, and preserved routes/OpenAPI during
file moves. K05 explains the framework mechanisms behind those requirements and
their limits. Python/Pydantic resources and essentials retain their owners.
No ORM is selected, no application implementation is added, and dependencies,
common rules, native adapters, and later practice topics are unchanged.

| Checked component | Evidence and applicability |
| --- | --- |
| Python 3.12.3; FastAPI **0.138.0** | Installed execution baseline; FastAPI metadata requires Python >=3.10, Starlette >=0.46.0, and Pydantic >=2.9.0. Examples target 3.11 grammar, not a tested interpreter matrix |
| Starlette **1.3.1**, Pydantic **2.13.4**, pydantic-core **2.46.4** | Installed request/response, lifespan and validation behavior; Pydantic's exact core pairing is retained |
| AnyIO **4.14.0**, HTTPX **0.28.1**, Uvicorn **0.49.0** | AnyIO/HTTPX used in local examples; server metadata/settings inspected, no listening server launched |
| mypy **2.1.0**, pytest **9.1.1** | Existing tools; standard-library unittest runs isolated HTTP examples; no dependency installation |
| Moving [FastAPI releases](https://fastapi.tiangolo.com/release-notes/) and [Starlette docs](https://starlette.dev/) | Newer published documentation exists; the installed baseline is deliberately not described as the latest version |

Local package source was inspected where integration details matter: FastAPI
`routing.py`, `_compat/v2.py`, dependency analysis, and exception handlers;
Starlette Request/app/route signatures and TestClient's import branch. Published
[FastAPI 0.138.0 routing source](https://github.com/fastapi/fastapi/blob/0.138.0/fastapi/routing.py)
anchors the request decoding, direct-response, and cleanup-stack observations.

## Coverage and recommendation strength

**R** means a requirement inherited from Agent_Engineering_Kit's
[core policy](../../standards/core.md), including boundaries, strict typing,
invariants, effect ownership, and public disclosure. **D** is a recommended
default with alternatives; **O** is an optional technique for a stated problem.
Library mechanisms alone do not mandate a project structure or architecture.
Unless stated otherwise, recommendations use the installed baseline above and
were checked on 2026-09-21.

| Research area | Decisions and adoption owner |
| --- | --- |
| Architecture and boundaries | Cohesive routers, HTTP adapters, independent business values, public projection; [transport](../../standards/fastapi/transport.md) |
| Construction, dependencies, patterns | Functions/Annotated providers, conditional app factories/protocols, request caching; [dependencies and lifetime](../../standards/fastapi/dependencies-lifetime.md) |
| Typed contracts, validation, invariants, errors | Actual HTTP input modes, status/error contracts, response bypass and schema behavior; transport |
| State, concurrency, cancellation, lifetime | Sync/async dispatch, pool contention, lifespan and yield scopes, bounded cleanup; dependencies and [runtime](../../standards/fastapi/runtime-operations.md) |
| Persistence and external APIs | Session versus transaction ownership, commit-before-success, lazy loading, upstream stream lifetime and durable handoff; dependencies |
| Tests and review | HTTP/failure/lifespan evidence, isolated overrides, schema compatibility, strict typing and realistic limits; [verification](../../standards/fastapi/verification.md) |
| Security, operations, performance | Auth/object permissions, error disclosure, CORS/CSRF, body/proxy/worker limits and measurement; runtime |
| Versions and migration | Pydantic V1 removal, yield timing, Content-Type, router internals, Starlette/test-client compatibility; verification |

FastAPI does not supply persistence atomicity, a durable job queue, or a universal
authorization policy. Coverage addresses their integration boundaries; detailed
ORM/driver adoption retains its later topic owners.

## Transport and design decisions

| Strength; problem and condition | Adopted form | Alternative, cost, or limitation; primary evidence |
| --- | --- | --- |
| D: related HTTP operations need organization | Cohesive APIRouter groups; preserve bootstrap ownership of inclusion, prefixes, tags and cross-cutting dependencies | A small app can stay in one module; no mandatory service scaffold or base controller. [Bigger applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/) |
| R: HTTP and independent business responsibilities differ | Typed values into the use case; map its expected failures and project public output in transport | A DTO with no distinct semantics need not be duplicated. Do not inject Request/Depends into the core; this is project policy, not a FastAPI restriction |
| O: app configuration/lifetime or test isolation needs separate instances | App factory with ready dependencies; a function provider or closure before a DI container | Extra indirection is unnecessary for a static tiny app. Protocols/adapters serve real external boundaries, not a pattern checklist. [Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/) |
| R: wire input and live invariants are different contracts | Model constraints for local shape/consistency; state owner enforces capacity, authorization and atomic writes | A valid HTTP body does not establish availability. Dependencies may execute while final request validation still fails; keep business writes out of providers/validators |
| D: an ordinary structured JSON response | Accurate public return type or explicit response_model with an accurate Python return annotation | Manual Response owns its bytes and bypasses automatic filtering. Tutorial Any examples do not override strict typing. [Response models](https://fastapi.tiangolo.com/tutorial/response-model/), [direct responses](https://fastapi.tiangolo.com/advanced/response-directly/) |
| R: failure semantics and disclosure matter | Stable mapping of expected errors, safe 422 output where needed, internal failures remain server failures | A fixed error sacrifices field-level diagnostics; an allowlisted typed error can preserve them. Changing an established shape needs API review. [Errors](https://fastapi.tiangolo.com/tutorial/handling-errors/) |

**Observed integration differences.** A focused ASGITransport probe showed that a
strict date accepted by `model_validate_json()` is rejected with 422 through the
ordinary HTTP JSON route on this stack. Source inspection explains why: FastAPI
decodes JSON, then its Pydantic adapter invokes `validate_python`. The recommendation
is to test the wire representation and choose conversions explicitly, not to
declare every field lax or build a second generic parsing layer.
[Pydantic input modes](https://docs.pydantic.dev/latest/concepts/strict_mode/).

The same probe confirmed that default 422 output contains rejected input despite
`hide_input_in_errors=True`, that a dependency ran before final body rejection,
that direct JSONResponse retained a field absent from response_model, and that
an invalid ordinary response produced 500. These are concrete reasons for safe
error/projection ownership and HTTP tests. Model annotations, OpenAPI metadata,
and successful model-only tests are not interchangeable enforcement mechanisms.

## Dependency and resource decisions

| Strength; problem and condition | Adopted form | Alternative, cost, or limitation; primary evidence |
| --- | --- | --- |
| D: request dependencies need reuse | Annotated providers with normal per-request caching | `use_cache=False` is optional for intentional repeated evaluation, not a general freshness rule. Caching does not define process/transaction scope. [Sub-dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/sub-dependencies/) |
| R: a yielded resource has a last consumer | Context-managed cleanup, scope chosen for handler-only versus stream use, exceptions preserved | Earlier closing reduces resource occupancy only when nothing still needs it. Graph scope constraints apply. [Yield dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/) |
| D: reusable process-local clients/pools | Create and close in lifespan; expose through typed providers | A closure is enough for the example. Dynamic state or an app factory does not make resources safe across loops/processes. Legacy events must migrate together. [FastAPI lifespan](https://fastapi.tiangolo.com/advanced/events/) |
| R: success depends on a committed effect | Operation-owned transaction completes before response sending; request teardown releases resources | A direct transaction block is simpler than a unit of work for one operation. FastAPI does not enforce isolation, session safety, or idempotency; existing Python effect policy owns these requirements |
| O: small post-response work may be lost | BackgroundTasks with independent resources and observable failure | For required delivery, persist a handoff and design retries/idempotency; no universal queue requirement. Tasks execute in order and one exception prevents later tasks. [Starlette background tasks](https://starlette.dev/background/) |
| R: a stream consumes an upstream response after endpoint return | Check upstream status before downstream streaming, close after consumption/failure, preserve cancellation | A fully consumed small response can release earlier; buffering an unbounded response is not an acceptable lifetime workaround. [HTTPX streaming](https://www.python-httpx.org/async/) |

Yield timing is explicitly versioned: FastAPI 0.118.0 restored default cleanup
after response sending; 0.121.0 added function scope. Request-scope teardown is
therefore unsuitable as the hidden success-critical commit point on this baseline.
This is an inference from documented cleanup timing and the existing effect
contract, not a database-specific FastAPI guarantee.
[Dependency history](https://fastapi.tiangolo.com/advanced/advanced-dependencies/).

## Execution, security, and operational decisions

**D — follow the actual I/O contract.** Await async I/O; a sync endpoint/provider
offloads blocking work, while an ordinary helper called inside async code does
not. CPU-intensive work needs measured isolation, not an async keyword. **O —
tune thread/concurrency limits** only for measured saturation and downstream
capacity; the documented shared AnyIO default is 40 tokens, not an application
throughput target. [Dispatch](https://fastapi.tiangolo.com/async/),
[thread capacity](https://starlette.dev/threadpool/).

**R — owned work and finite budgets.** Preserve cancellation, join concurrent work,
and give downstream requests/streams and required cleanup appropriate deadlines.
Use bounded shielding only when cancellation would prevent required awaited
cleanup. Keep-alive and individual read timeouts do not establish an end-to-end
request deadline. **D — reuse a client/pool** when its owner/lifetime is stable;
avoid a new client in a hot loop. [AnyIO cancellation](https://anyio.readthedocs.io/en/stable/cancellation.html),
[HTTPX timeouts](https://www.python-httpx.org/advanced/timeouts/).

**R — enforce the actual trust boundary.** Authentication dependencies and OAuth2
metadata do not decide object/tenant permissions. Use the existing scheme and
explicit operation authorization. **D — explicit browser policy** for CORS and
credentialed requests; it cannot replace authentication or cookie CSRF controls.
Keep strict JSON Content-Type checking unless an established compatibility need
justifies changing that boundary. [Scopes](https://fastapi.tiangolo.com/advanced/security/oauth2-scopes/),
[CORS](https://fastapi.tiangolo.com/tutorial/cors/),
[Content-Type checking](https://fastapi.tiangolo.com/advanced/strict-content-type/).

**R — bound exposed parsing/storage work.** Field validation follows body parsing;
file spooling and multipart field limits are not total upload limits. Set the
appropriate proxy/ASGI/read boundary; validate untrusted filenames and outbound
destinations under the project's integration policy. Latest Starlette docs now
mention a `max_body_size` app/route setting, but the inspected 1.3.1 signatures
lack it. K05 does not prescribe that unsupported API.
[Requests](https://starlette.dev/requests/).

**D — deliberate middleware/deployment configuration.** Preserve middleware order
and forwarded-header trust, public URLs, worker/pool multiplication, readiness,
and finite graceful shutdown. Pure ASGI middleware is optional when BaseHTTPMiddleware
context-variable limitations affect tracing or another contract. **O — optimize**
serialization/caching/workers from measurements while preserving filtering and
authorization boundaries; no benchmark-based universal architecture is adopted.
[Middleware](https://starlette.dev/middleware/),
[proxy behavior](https://fastapi.tiangolo.com/advanced/behind-a-proxy/),
[Uvicorn settings](https://uvicorn.dev/settings/),
[deployment concepts](https://fastapi.tiangolo.com/deployment/concepts/).

## Testing, compatibility, and evidence limits

**D — test at the affected boundary.** Business rules can be tested directly;
HTTP cases establish actual parsing/status/projection. Lifespan tests enter
TestClient's context; HTTPX ASGITransport alone does not start lifespan. Use an
async harness for same-loop async integrations. **R — restore isolation** when
overriding dependencies, and retain real integration evidence where fake providers
bypass authorization, storage, or cleanup. Review affected schemas/imports and
provider identities during file moves, without a whole-API snapshot by default.
[Lifespan testing](https://starlette.dev/lifespan/),
[HTTPX transports](https://www.python-httpx.org/advanced/transports/),
[overrides](https://fastapi.tiangolo.com/advanced/testing-dependencies/).

Version review established these additional boundaries from
[FastAPI release notes](https://fastapi.tiangolo.com/release-notes/): 0.126.0 dropped
the Pydantic V1 package; 0.128.0 dropped `pydantic.v1`; 0.132.0 enabled strict JSON
Content-Type by default; 0.137.0 changed included-router internals from a flat
route list into a tree. Compatibility claims about a Pydantic namespace or an
older router traversal recipe must not be carried into this baseline unchanged.

Two cross-library discrepancies were resolved from local evidence rather than
copying current documentation indiscriminately:

- Starlette documents `Request[State]` and typed dictionary-style state access.
  Registering that generic Request directly as a FastAPI 0.138.0 endpoint parameter
  raises FastAPIError in the focused probe. A typed closure/provider works without
  adopting that combination. This finding does not claim generic Request is broken
  in Starlette itself. [Starlette state](https://starlette.dev/lifespan/).
- Starlette 1.3.1 prefers HTTPX2 for TestClient but retains HTTPX with a deprecation
  warning, confirmed in its installed source and
  [official TestClient documentation](https://starlette.dev/testclient/). HTTPX2
  is absent here. An initial `-W error` invocation stopped at import; the examples
  then ran with `-W default`, keeping the warning visible. No dependency upgrade
  or warning-suppression rule was added.

The [HTTP example](../../standards/fastapi/examples/http-boundary.md) illustrates
transport validation versus a state-dependent capacity rule, typed function
injection, explicit public projection, safe errors, and OpenAPI. The
[lifetime example](../../standards/fastapi/examples/lifetime.md) uses a lifespan
client, request/function yield scopes, upstream rejection/timeout, bounded
snapshot accumulation, and cleanup after stream failure. Their five exact Python
blocks passed strict mypy with the Pydantic plugin; 14 unittest cases passed.

The sandbox prohibited sending on a local socketpair used to wake TestClient's
background event loop. A timed empty-app reproduction plus a PermissionError
probe isolated that environment issue; the same bounded example tests passed
outside that restriction using only in-memory transports. This was not repaired
by changing application logic or replacing the existing dependencies.

These checks do not prove real-network backpressure/disconnect behavior,
cancellation under a live server, pool sizing, authentication, database atomicity,
durable background delivery, other-interpreter compatibility, or native client
reading compliance. The [practice plan](../plans/2026-09-21-engineering-practices.md)
records exact commands, catalog/delivery checks, scoped baseline evidence, and the
user-review checkpoint. No live service, benchmark, or external installation is
claimed.

## 2026-10-03 follow-up: PY-01

The [lifetime example](../../standards/fastapi/examples/lifetime.md) now maps
HTTPX errors while buffering `/snapshot`: timeouts to safe 504 and other request
errors to safe 502. [HTTPX's exception hierarchy](https://www.python-httpx.org/exceptions/)
distinguishes receive-time failures; opening a streaming response does not finish
consumption. The dependency still owns closure; cancellation is not caught.
A failure after `/feed` starts remains a propagated stream failure, since an
already started response cannot be replaced with a new error status/body.

Before the fix, the new test produced two errors: 200 upstream headers and a
bounded partial chunk followed by ReadTimeout or ReadError escaped the handler.
After the fix, `python -W default -m unittest -v test_feed_http` passed all eight
tests (including both new subcases). Both return only the safe JSON error, close
the stream, and close the client at lifespan exit. Existing successful streaming,
reuse, non-200 refusal, injected opening timeout, late stream failure, snapshot
size bound and missing-lifespan cases remain. Strict mypy passed both modules
with `disallow_any_explicit`, `disallow_any_unimported`, and the Pydantic plugin
(`init_typed`, `init_forbid_extra`, `warn_required_dynamic_aliases`). No global
suppression or all-expression-Any claim was added.

Execution: Python 3.12.3, FastAPI 0.138.0, Starlette 1.3.1, HTTPX 0.28.1,
AnyIO 4.14.0, Pydantic 2.13.4/core 2.46.4 and mypy 2.1.0 in a temporary venv.
The TestClient thread/portal stalled in the restricted sandbox; the same local
transport tests completed outside it with a 30-second process bound. Starlette's
existing HTTPX deprecation warning remained visible. No network request is made
by the tests; injected exceptions do not establish real timeout, cancellation,
backpressure or server-shutdown behavior. The final two named blocks match the
tested files. Logs, mypy configuration and resolved requirements:
`/tmp/aek-maint-stage1-h090d9fo/fastapi/`. Earlier dated evidence is unchanged.
