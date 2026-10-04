# Gin: request lifetime and exposed boundaries

Read for request cancellation, asynchronous work, server startup/shutdown,
proxy trust, uploads, or deployment-facing changes. Return to the
[Gin entry](../gin.md).

## Request state and external work

- Use `c.Request.Context()` for application, DB, and outbound HTTP work. Gin's
  `ContextWithFallback` changes context-method forwarding; accepting
  `*gin.Context` as a `context.Context` is not a reliable cancellation boundary.
- Gin reuses contexts. Never retain the original `*gin.Context` or its writer
  after the request. Prefer copying the small immutable values a worker needs.
  Where Gin metadata is actually needed asynchronously, take `c.Copy()` before
  starting the goroutine and treat it as read-only. It shares the request and
  referenced values; it is not a deep copy or a new response writer.
- Copying a Gin context does not detach or extend the request context. Request
  cancellation still follows `net/http`. Request-scoped parallel work must
  honor cancellation and finish before the handler returns. Do not read the
  request body or write the response concurrently with/after completion.
- Work intentionally outliving the request needs its own owner, deadline,
  capacity, and shutdown path. Use a durable queue only when delivery/retry
  requirements warrant one; a goroutine or `202 Accepted` alone promises no
  durable processing. Follow [Go concurrency](../go/concurrency.md) for ownership.
- Reuse explicitly injected pools/clients. The use case owns its transaction;
  do not open a transaction for every HTTP request by default or commit because
  a handler wrote a success status. Gin does not provide persistence isolation
  or atomicity between a DB change and an external effect. The applicable
  [Go resource rules](../go/resources.md) retain those contracts.

See [Gin goroutines](https://gin-gonic.com/en/docs/middleware/goroutines-inside-a-middleware/),
[context implementation](https://github.com/gin-gonic/gin/blob/v1.12.0/context.go),
and [`http.Request` lifetime](https://go.dev/src/net/http/request.go).

## Serve and stop deliberately

- Where the service needs controlled timeouts or shutdown, serve the router
  through an owned `http.Server`. Set header, read, write, and idle budgets for
  the endpoint mix; include proxy timeouts, uploads, SSE, and WebSockets in that
  decision. A socket write timeout does not itself cancel application work.
- Supply application deadlines to cooperative dependencies. Wrapping work in a
  goroutine and returning a timeout does not terminate it or permit it to write
  through Gin after the response has finished.
- On shutdown, stop admission/readiness as required, call `Shutdown` with a
  bounded context that is not already canceled, and wait for completion before
  process exit. Handle non-`http.ErrServerClosed` serve errors and shutdown
  timeout/errors. Define any force-close fallback explicitly.
- `Shutdown` does not wait for hijacked connections or arbitrary background
  workers. Give those their own close/join path. Do not infer zero downtime or
  successful transaction completion from `Shutdown` returning alone.

See [Gin shutdown](https://gin-gonic.com/en/docs/server-config/graceful-restart-or-stop/)
and [`http.Server` contracts](https://go.dev/src/net/http/server.go).

## Bound input and establish trust

- Bound body reads before any binder/upload parser using `http.MaxBytesReader`
  or the applicable ingress control. `Content-Length` is not sufficient for
  unknown/chunked bodies. Enforce a complete-body contract by consuming/checking
  it under the limit; a successful first JSON decode may leave trailing input.
- `MaxMultipartMemory` controls multipart memory before spilling to disk, not
  total upload size. Define total/file/count limits, safe server-owned paths,
  allowed content, and temporary-file cleanup. A client filename is untrusted.
- For ordinary TCP proxy deployments, explicitly configure trusted proxy
  addresses/CIDRs and check `SetTrustedProxies` errors. With no proxy, use
  `SetTrustedProxies(nil)`. Do not trust the default all-address set for decisions
  based on `ClientIP()`.
- Check the whole client-IP trust path: `TrustedPlatform` headers and Gin 1.12's
  Unix-socket forwarding behavior can take different paths from TCP CIDR checks.
  Prevent direct access/header spoofing at ingress; a nil proxy list alone is
  not a universal guarantee. Client IP is not a user identity.
- For browser-facing endpoints, use explicit allowed origins/credentials and
  appropriate secure cookie/CSRF policy when authentication uses ambient cookies.
  CORS does not replace authentication or protect non-browser callers. Keep
  credentials and private payloads out of request/response logs.

See [upload bounds](https://gin-gonic.com/en/docs/routing/upload-file/limit-bytes/),
[proxy configuration](https://gin-gonic.com/en/docs/server-config/trusted-proxies/),
[client-IP implementation](https://github.com/gin-gonic/gin/blob/v1.12.0/context.go),
and [Gin security guidance](https://gin-gonic.com/en/docs/middleware/security-guide/).
