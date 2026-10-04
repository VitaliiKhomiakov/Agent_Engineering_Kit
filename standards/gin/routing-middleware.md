# Gin: route assembly and middleware

Read for route registration, middleware order, request gates, recovery, or shared
response handling. Return to the [Gin entry](../gin.md).

## Construct the route tree once

- Assemble dependencies and routes before serving. Pass a use-case function or
  cohesive dependency to registration/handler constructors. Do not retrieve DB
  pools or service objects from an untyped context store inside business code.
- `gin.Default()` installs Logger and Recovery. `gin.New()` installs neither;
  use it when choosing the stack explicitly, supplying required observability
  and recovery behavior. Neither constructor alone defines deployment policy.
- Register engine/group middleware before the groups/routes that must inherit
  it. Gin combines handler chains when registering them; adding middleware later
  does not retroactively secure previously registered routes. Avoid concurrent
  route or configuration mutation.
- Group by a real URL or shared policy boundary. Apply authentication to all
  intended methods/routes, while object-level authorization stays in the use
  case. Test the registration path, including any deliberate public routes.
- Preserve path normalization, redirects, wildcard handling, and method behavior
  when reorganizing routes. `NoRoute`, `NoMethod`, and `HandleMethodNotAllowed`
  need deliberate configuration if the API promises uniform 404/405 responses.
  Do not change routing options merely for stylistic consistency.

See [engine construction](https://github.com/gin-gonic/gin/blob/v1.12.0/gin.go)
and [group/route registration](https://github.com/gin-gonic/gin/blob/v1.12.0/routergroup.go).

## Control flow and one response owner

- `c.Next()` runs downstream handlers before the middleware's following code.
  Use before/after behavior deliberately: a logger outside an error responder
  can observe its final status. Normal post-processing is not a substitute for
  `defer` when cleanup must survive a panic.
- `c.Abort()` prevents pending handlers but does not return from the current
  function or undo an already executed handler. Use `AbortWithStatusJSON` (or
  the chosen equivalent) followed by `return` on a rejected request. Returning
  alone from middleware does not stop Gin's remaining chain.
- `c.Error(err)` records an error; it does not itself abort or render it. Choose
  local handler mapping or a shared responder with an explicit handoff. A handler
  handing off an error must stop before writing a success response.
- A responder after `c.Next()` must respect `c.Writer.Written()`. Once the
  response is committed, log/report a late error under the streaming/connection
  contract; appending a new JSON error corrupts the existing body. An unwritten
  response does not imply that application side effects can be rolled back.
- Store only necessary request metadata in Gin context keys, with a typed
  accessor at the transport boundary. Prefer explicit principal/tenant arguments
  when invoking the use case; a parsed identity is not an authorization decision.

See [middleware flow](https://gin-gonic.com/en/docs/middleware/custom-middleware/)
and [error handling](https://gin-gonic.com/en/docs/middleware/error-handling-middleware/).
The optional [middleware example](examples/middleware.md) shows a terminating
access gate and a shared responder that preserves an already written response.

## Recovery and cross-cutting behavior

- Recovery is a last HTTP panic boundary, not ordinary error handling, a
  transaction manager, or recovery for separately launched goroutines. Ensure
  its position covers the intended downstream stack. If a JSON API needs a
  custom recovery response, preserve committed-response and broken-connection
  behavior rather than blindly writing JSON after every panic.
- Review both recovery and access-log fields for the deployed configuration.
  Gin's built-in request-dump sanitization masks Authorization, not every cookie,
  custom credential, or sensitive query parameter. Release mode alone is not
  a redaction policy. Use appropriate structured/sanitized diagnostics.
- CORS, authentication, compression, rate limiting, and tracing are independent
  policies. Choose compatible middleware for actual exposure; a wildcard CORS
  setting is not access control. Account for preflight and error responses when
  ordering CORS and authentication.
- A writer wrapper must preserve the capabilities the route uses, including
  streaming flush or connection hijack where applicable. Do not introduce a
  response-buffering or timeout wrapper without checking memory and streaming
  behavior. One shared concern does not justify a universal middleware framework.

See [Recovery source](https://github.com/gin-gonic/gin/blob/v1.12.0/recovery.go),
[query logging](https://gin-gonic.com/en/docs/logging/avoid-logging-query-strings/),
[CORS configuration](https://github.com/gin-contrib/cors), and
[`net/http` writer contracts](https://go.dev/src/net/http/server.go).
