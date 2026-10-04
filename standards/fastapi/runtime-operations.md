# FastAPI runtime and operations

Read when changing execution, streams, middleware/security, deployment, or
performance. Apply only the parts exposed by the task. General concurrency,
timeouts, retries, and cancellation remain owned by
[Python execution](../python/execution-resources.md).
Return to the [FastAPI entry](../fastapi.md).

## Execution and resource budgets

Use `async def` with awaitable I/O or brief nonblocking work. FastAPI runs ordinary
`def` endpoints/dependencies in a thread pool. An ordinary helper called directly
inside `async def` still runs there and can block the event loop; it is not
automatically offloaded. Use a sync endpoint for a blocking stack or explicit
bounded offloading at its boundary. CPU-heavy work may need processes/workers
after measurement; adding `async` or more threads does not make it parallel.
[Execution semantics](https://fastapi.tiangolo.com/async/).

Sync handlers, dependencies, uploads, and other Starlette work can compete for
AnyIO thread capacity. The documented default limiter is 40 tokens; inspect the
actual limiter before tuning. More threads increase memory and downstream load.
Do not assume each offloaded phase uses the same thread or that cancellation
stops a running blocking call. Respect the client's thread-affinity contract.
[Thread pool](https://starlette.dev/threadpool/).

Bound downstream connect/read/write/pool waits, concurrency, page sizes, and
stream duration as needed. A keep-alive timeout is not an end-to-end request
deadline. An HTTPX read timeout is not a total download deadline. Reuse owned
clients/pools, and close streamed upstream responses even when iteration fails.
For retryable effects, establish idempotency and a total retry budget first.
[HTTPX timeouts](https://www.python-httpx.org/advanced/timeouts/),
[stream ownership](https://www.python-httpx.org/async/).

Propagate cancellation; do not turn it into success or detach request work with
unowned tasks. Use the selected runtime's task groups for joined concurrent work.
If cancellation would prevent required async cleanup, use a bounded shield only
around that cleanup and surface failure appropriately. A dropped client is not
a universal guarantee that every handler or blocking call has stopped. Test real
disconnect behavior when that is part of the change.
[AnyIO cancellation](https://anyio.readthedocs.io/en/stable/cancellation.html).

## Exposed security boundaries

Authenticate with the project's established scheme, validate credentials, and
authorize the requested action/object/tenant. `Security` and OAuth2 declarations
help dependency/OpenAPI integration but do not implement authorization policy.
Keep secrets out of request/response logs, validation errors, URLs, and metrics
labels. Do not create a token system or permission framework for every endpoint.
[Security scopes](https://fastapi.tiangolo.com/advanced/security/oauth2-scopes/).

Configure browser origins, methods, headers, and credentials deliberately. CORS
controls browser access; it does not replace authentication or cookie-based CSRF
protection. For JSON endpoints preserve the strict Content-Type default introduced
in FastAPI 0.132.0; loosening it for old clients needs an explicit compatibility
reason and review of the affected trust boundary.
[CORS](https://fastapi.tiangolo.com/tutorial/cors/),
[Content-Type](https://fastapi.tiangolo.com/advanced/strict-content-type/).

Set body/upload limits at the appropriate proxy or validated ASGI boundary, with
bounded reads where needed. Pydantic field limits apply after parsing and do not
bound total received bytes. Starlette's `max_part_size` limits non-file multipart
fields, not uploaded file size; spooling to disk is not a total upload limit.
Treat filenames, MIME types, and supplied URLs as untrusted; use owned storage
names/paths and a controlled destination policy for outbound requests.
[Request parsing](https://starlette.dev/requests/).

Review middleware order where it affects CORS/error headers, sessions, tracing,
or authorization. If using `BaseHTTPMiddleware`, account for its documented
context-variable propagation limits; pure ASGI middleware is an option when
those limits matter, not a mandatory rewrite.
[Middleware](https://starlette.dev/middleware/).

## Deployment and performance

Trust forwarded headers only from the actual trusted proxy path. Verify public
scheme/host, redirects, and `root_path` with the deployment topology. Do not copy
an unrestricted forwarded-IP setting onto a directly reachable server.
[Proxy behavior](https://fastapi.tiangolo.com/advanced/behind-a-proxy/).

Choose worker count with per-process memory, pool sizes, and downstream capacity
in mind. Lifespan initialization runs for each worker; avoid uncoordinated schema
migrations or global singleton assumptions. Distinguish liveness from readiness,
and give graceful shutdown a finite budget that covers owned work/cleanup.
Observe latency, errors, saturation, and cleanup failures without sensitive
payloads. Use server limits supported by the installed version.
[Uvicorn settings](https://uvicorn.dev/settings/),
[deployment concepts](https://fastapi.tiangolo.com/deployment/concepts/).

Measure the actual bottleneck before changing serializers, adding caches,
offloading, or increasing concurrency. Preserve response filtering and isolation
when optimizing; shared mutable caches need keys, lifetime, invalidation, and
authorization boundaries. Standard return models and a simple deployment remain
the default unless evidence justifies additional machinery.
