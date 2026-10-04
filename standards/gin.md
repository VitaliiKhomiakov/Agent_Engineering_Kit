# Gin

Apply only where Gin is used, with [Go](go.md) and the [common rules](core.md).
Read only relevant sections; examples and research are optional. Preserve the
project's supported Go/Gin versions and actual runtime contract.

## Gin essentials

- Keep `*gin.Context` at the HTTP boundary; pass typed commands and
  `c.Request.Context()` into application work. Binding does not enforce state
  invariants or operation authorization.
- Give each response one owner. Prefer `ShouldBind*` when the API owns errors;
  preserve absence/zero semantics and return after rejecting a request.
- Configure middleware, proxy trust, input bounds, and server lifetime for the
  actual deployment. Do not retain a pooled Gin context beyond the request.

## Read by task

| Task touches | Read |
| --- | --- |
| Gin handlers, request sources, binding, response/error contracts | [Handlers and binding](gin/handlers-binding.md) |
| Gin route assembly, middleware order, authentication gates, recovery | [Routing and middleware](gin/routing-middleware.md) |
| Gin request lifetime, background work, server shutdown, proxies, uploads | [Runtime and exposed boundaries](gin/runtime.md) |
| Gin HTTP tests, dependency migration, codec changes, performance checks | [Verification and compatibility](gin/verification.md) |

Availability in a bundle does not imply mandatory reading; a Gin task may
also require relevant Go language, concurrency or resource sections.

## Evidence

[Gin research](../docs/research/2026-09-21-gin-engineering-practices.md) records
primary evidence, versions and alternatives checked on 2026-09-21.
The [practice plan](../docs/plans/2026-09-21-engineering-practices.md) records
example and delivery checks.
