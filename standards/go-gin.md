# Go / Gin

Apply this entry to the Go part of the task together with the [common rules](core.md).
Read only the relevant sections below; do not load every linked file recursively.
An example is optional when its code helps resolve the current decision.

## Essential guidance

- Check the project's language/dependency constraints and actual toolchain/CI.
  Preserve its supported versions; do not silently upgrade to use a newer idiom.
- Follow Go's package, type, and ownership semantics. Use a concrete function or
  type when sufficient; introduce an interface or pattern for a present need.
- Preserve typed contracts, domain invariants, error behavior, and resource
  lifetimes. Changes to those concerns trigger the relevant detailed section.
- Format changed Go code with `gofmt` and follow the shared
  [verification policy](verification.md) for proportionate checks.

General SOLID, DRY, KISS, YAGNI, and pattern criteria remain in the common rules.
Requirements protect affected contracts/resources; defaults may change for a
concrete project reason. Patterns are optional unless the task or architecture
requires them. Detailed guidance applies when its stated condition is met.

## Read by task

| Task touches | Read |
| --- | --- |
| Packages, dependency direction, construction, patterns, modules/toolchains | [Architecture and patterns](go/architecture.md) |
| Public types, domain state, validation, receivers, errors | [Types and contracts](go/contracts.md) |
| Goroutines, channels, shared state, cancellation, shutdown | [Concurrency](go/concurrency.md) |
| SQL, transactions, HTTP clients/servers, resource lifetime | [External resources](go/resources.md) |
| Choosing Go checks, security boundaries, measured performance | [Verification](go/verification.md) |
| Gin handlers, request sources, binding, response/error contracts | [Handlers and binding](gin/handlers-binding.md) |
| Gin route assembly, middleware order, authentication gates, recovery | [Routing and middleware](gin/routing-middleware.md) |
| Gin request lifetime, background work, server shutdown, proxies, uploads | [Runtime and exposed boundaries](gin/runtime.md) |
| Gin HTTP tests, dependency migration, codec changes, performance checks | [Verification and compatibility](gin/verification.md) |

A task may need several sections; a local fix need not read unrelated ones.
Examples are linked from the section that explains their purpose and limits.
Availability in the installed policy bundle does not mean mandatory reading.
The four Gin routes apply only where Gin is actually used. Stop following links
once the task's relevant rules are known.

## Gin essentials

- Keep `*gin.Context` at the HTTP boundary; pass typed commands and
  `c.Request.Context()` into application work. Binding does not enforce state
  invariants or operation authorization.
- Give each response one owner. Prefer `ShouldBind*` when the API owns errors;
  preserve absence/zero semantics and return after rejecting a request.
- Configure middleware, proxy trust, input bounds, and server lifetime for the
  actual deployment. Do not retain a pooled Gin context beyond the request.

## Evidence

[Go research](../docs/research/2026-09-21-go-engineering-practices.md) and
[Gin research](../docs/research/2026-09-21-gin-engineering-practices.md) record
primary evidence checked on 2026-09-21, versions, and alternatives. They are
optional background. Example execution and delivery evidence belongs to the
[practice plan](../docs/plans/2026-09-21-engineering-practices.md).
