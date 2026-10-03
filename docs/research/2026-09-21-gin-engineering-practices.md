# Gin engineering practices: evidence and adoption decisions

**Stage:** K02 of the [practice plan](../plans/2026-09-21-engineering-practices.md).
**Evidence checked:** 2026-09-21. **Adoption target:** the short
[Go/Gin entry](../../standards/go-gin.md), four conditional sections under
`standards/gin/`, and two optional examples. This note is background material;
installed projects do not need to load it to apply the profile.

## Scope and method

K01 owns general Go practice. K02 addresses Gin as an HTTP adapter: construction,
binding, response ownership, middleware, request lifetime, ingress assumptions,
and verification. Persistence and domain invariants remain relevant, but Gin
does not supply a transaction model, an ORM, or an application architecture.
Review those integration boundaries without adopting the later database topics.

Primary evidence comes from official Gin documentation, the tagged Gin module
and source, its validator documentation, Go's HTTP contracts, and maintained
gin-contrib middleware documentation. The tagged module was also downloaded
through the public Go proxy with checksum verification for executable checks.
Tutorial snippets illustrate an API; they are not a complete production policy.

**Strength:** R = Agent_Engineering_Kit requirement protecting an affected contract,
trust boundary, or resource; D = recommended default; O = optional technique
with a present use case. R is a project-policy decision justified below, not a
claim that Gin imposes our architecture. Existing-project exceptions and supported
versions remain binding. Each decision below inherits the evidence date above.

## Version evidence and compatibility

At this check, the upstream release list identifies **v1.12.0** as latest.
The tagged module requires **Go 1.25.0** and declares validator **v10.30.1**.
Gin **v1.11.0** instead declares Go **1.23.0** and validator **v10.27.0**.
These are minimum module requirements, not proof of a deployed compiler or a
promise about future support. [Releases](https://github.com/gin-gonic/gin/releases),
[1.12 module](https://github.com/gin-gonic/gin/blob/v1.12.0/go.mod),
[1.11 module](https://github.com/gin-gonic/gin/blob/v1.11.0/go.mod).

The local compiler reports **go1.26.1 linux/amd64**. Examples use Gin 1.12.0,
the default build tags, and the local toolchain; the strict binding example
explicitly uses `encoding/json`. This is an execution environment, not a current
production patch recommendation. No project dependency or toolchain upgrade is
part of this stage. Earlier Gin versions and other codecs were not executed.

| Version-sensitive area | Evidence and adoption consequence |
| --- | --- |
| Binding and context helpers | Use supported methods from the resolved Gin version. The broad profile uses established `ShouldBind*`, `Next`, and `Abort` forms; newer convenience APIs are not required. [Context API](https://github.com/gin-gonic/gin/blob/v1.12.0/context.go) |
| Form parsing, client IP, escaped paths, response lifecycle | The 1.12 release includes changes in these areas. An upgrade needs tests for the features actually used, not just a successful dependency resolution. [Release notes](https://github.com/gin-gonic/gin/releases/tag/v1.12.0) |
| Validator initialization | Gin's default initializer calls `validator.New()` and uses the `binding` tag. Do not assume the required-struct option used in another example is enabled. [Initializer](https://github.com/gin-gonic/gin/blob/v1.12.0/binding/default_validator.go) |
| Decoder policy | The 1.12 JSON binder uses the selected codec and decodes once. Global strictness flags are shared; replacing a codec can change parsing and error propagation. [JSON binder](https://github.com/gin-gonic/gin/blob/v1.12.0/binding/json.go), [codec API](https://github.com/gin-gonic/gin/blob/v1.12.0/codec/json/json.go) |
| Context forwarding | Gin context methods can depend on `ContextWithFallback`. The application boundary uses the request's standard context explicitly. [Context documentation](https://gin-gonic.com/en/docs/server-config/context/) |

The website's simplified binding explanation describes automatic 400 responses.
The inspected 1.12 module's `MustBindWith` also maps an inspectable
`http.MaxBytesError` to 413, with a comment about codec-dependent propagation.
Consequently the adopted rule is about who owns the response, not an assertion
that all `Bind*` failures always produce 400. Keep explicit size/error mapping
when the API promises it. [Binding tutorial](https://gin-gonic.com/en/docs/binding/binding-and-validation/),
[tagged implementation](https://github.com/gin-gonic/gin/blob/v1.12.0/context.go).

## Architecture, construction, and dependency direction

| Decision and problem | Applicability and chosen form | Simpler alternative, cost, and basis |
| --- | --- | --- |
| R: transport isolation | Business behavior callable through HTTP and another entry receives typed commands and `context.Context`; Gin handles binding and rendering | A small closure can be the adapter. An independent core must not import Gin DTOs. This applies the [shared boundary policy](../../standards/core.md#responsibilities-and-data), rather than a Gin-mandated directory tree |
| D: explicit construction | Assemble dependencies once and pass concrete objects/functions to cohesive handler/registration functions | A local function is enough for one operation. Handler structs help when routes share dependencies; a container, interface per handler, or base controller adds no inherent guarantee. [Go architecture](../../standards/go/architecture.md) owns pattern selection |
| D: deliberate engine setup | Use `gin.New()` for a chosen middleware stack; retain `gin.Default()` when its Logger/Recovery combination fits | Neither is universally superior. Explicit setup requires remembering the required middleware. [Engine source](https://github.com/gin-gonic/gin/blob/v1.12.0/gin.go) |
| R: correct registration order | Complete middleware/groups/routes before serving; group by URL or a real shared access policy | A flat small router is sufficient. Chains are combined during registration, so late middleware can leave earlier routes unprotected. [Router groups](https://github.com/gin-gonic/gin/blob/v1.12.0/routergroup.go) |
| O: shared error responder | Centralize a repeated HTTP error policy with a documented handoff and a committed-response check | Local mapping is clearer for one endpoint. Middleware adds ordering and late-error responsibilities. [Error middleware](https://gin-gonic.com/en/docs/middleware/error-handling-middleware/) |

This adopts ordinary Go dependency injection and Gin function middleware. It does
not invent Gin-specific Repository, Factory, Facade, Strategy, or Result classes.
An abstraction is useful only where an actual boundary or variation needs it.
No mandatory backend layer hierarchy, generic CRUD router, or framework-wide
context service locator is introduced.

## Typed input, state invariants, and responses

**R — preserve input-source and public-error contracts; D — explicit binding.**
Select path, query, headers, and body according to the endpoint. Automatic binding
is useful for intentionally negotiated/form input, but can merge sources that a
query-only API did not intend. `ShouldBind*` lets the handler map errors before
writing. The simpler alternative is explicit parsing of a single scalar, not
a DTO hierarchy for every route. [Binding documentation](https://gin-gonic.com/en/docs/binding/binding-and-validation/).

**R — model presence correctly.** A required scalar bool/number rejects its zero
value. A required pointer lets explicit `false`/`0` differ from absence; JSON
`null` and an omitted field still need a richer representation if they mean
different operations. Adding pointers everywhere complicates consumers without
benefit. [Validator contracts](https://pkg.go.dev/github.com/go-playground/validator/v10@v10.30.1).
The framework requires semantics to be preserved, not a particular field wrapper.

**D — local, pure validation; R — state rules behind transport.** Register shared
validators at startup and keep them free of I/O. A DTO may establish that an ID
and notification option are well formed while the use case rejects publication
because a document lacks a title or is already published. The existing
[Go domain example](../../standards/go/examples/domain.md) owns that illustrative
invariant. Authentication/authorization and transaction protection are additional
requirements, not extra binding tags. [Custom validators](https://gin-gonic.com/en/docs/binding/custom-validators/),
[shared invariant policy](../../standards/core.md#responsibilities-and-data).

**O — strict local JSON.** Default binding suffices when its contract fits. For
an endpoint explicitly requiring one JSON value and no unknown fields, a local
binder can configure its decoder, require EOF, and invoke the existing validator.
This costs code and rejects inputs tolerated by a permissive API; do not impose
it during an unrelated migration. Unknown-field rejection does not also reject
duplicate keys. Body limits must cover the reads needed by the chosen contract.
[JSON binder source](https://github.com/gin-gonic/gin/blob/v1.12.0/binding/json.go),
[standard JSON contracts](https://pkg.go.dev/encoding/json#Unmarshal).

The original [binding example](../../standards/gin/examples/binding.md) chooses
that strict contract explicitly. It accepts `notify:false`, rejects omitted/null
notification values, separates malformed input from a wrapped application
conflict, and passes the request context to the operation. It does not implement
a second publication domain model or infer business validity from `required`.

**R — stable, non-leaking outcomes.** Map inspectable application errors into
agreed public codes/statuses; do not render raw storage or validator errors.
Choose the existing API's 400/422 and conflict semantics rather than prescribing
one code for every service. One handler/responder owns the response; aborting
pending handlers and returning from the current function are separate operations.
These are framework contract/security decisions, using Gin's control-flow API.
[Middleware flow](https://gin-gonic.com/en/docs/middleware/custom-middleware/).

## Middleware, state, cancellation, and effects

| Decision | Condition and rationale | Alternative or cost; evidence |
| --- | --- | --- |
| R: terminating request gate | A denied request must not reach protected work; abort the chain and return | A return alone is insufficient middleware control. Group access does not replace object authorization. [Middleware flow](https://gin-gonic.com/en/docs/middleware/custom-middleware/) |
| R: preserve committed output | A shared responder inspects errors after downstream execution and does not append JSON after writing has begun | Local handling before writing is simpler. Streaming errors require a separate connection/protocol policy. [HTTP writer contracts](https://go.dev/src/net/http/server.go) |
| D: bounded recovery | Place recovery around the intended stack; treat panic as unexpected failure and handle logging/redaction deliberately | It does not undo effects or catch another goroutine's panic. Built-in recovery is adequate only when its response/log policy fits. [Recovery source](https://github.com/gin-gonic/gin/blob/v1.12.0/recovery.go) |
| R: request lifetime | Application operations receive `c.Request.Context()`; do not retain a pooled Gin context or writer | Sequential execution is simplest. `Copy()` helps read-only metadata access but shares referenced values and does not create a background-job lifetime. [Goroutines](https://gin-gonic.com/en/docs/middleware/goroutines-inside-a-middleware/), [request lifetime](https://go.dev/src/net/http/request.go) |
| R: owned asynchronous work; O: durable queue | Use independent lifetime/capacity/shutdown for work intentionally surviving a request; add durable delivery only if required | Detached goroutines are not a reliable job system. Queues add operational and consistency costs. This applies [Go concurrency policy](../../standards/go/concurrency.md), not a Gin queue facility |
| R: use-case transaction ownership | Atomic business operations use the appropriate persistence boundary; DB changes and external effects need their own consistency decision | No universal transaction-per-request middleware or commit-on-2xx rule. A single statement may suffice; [Go resource policy](../../standards/go/resources.md) remains the owner |

The original [middleware example](../../standards/gin/examples/middleware.md)
shows an access gate and error handoff. It demonstrates the alternative to local
mapping when a shared policy is justified, including reporting a late error
without corrupting an already committed body. It is not a token verifier or
a recovery/shutdown implementation.

## Security, operations, and performance

| Decision and problem | Applicability, simpler alternative, and costs | Primary basis |
| --- | --- | --- |
| R: explicit ingress trust | Configure trusted TCP proxies, check setup errors, and verify platform-header/Unix-socket paths where used; with no TCP proxy disable trust | Default all-proxy trust cannot establish client identity. A nil CIDR list alone does not describe every `ClientIP` path. [Proxy docs](https://gin-gonic.com/en/docs/server-config/trusted-proxies/), [implementation](https://github.com/gin-gonic/gin/blob/v1.12.0/context.go) |
| R: actual input bounds | Bound body reads before parsing; define upload size/count/storage ownership when uploads are present | `Content-Length` alone misses unknown lengths; `MaxMultipartMemory` is a memory/disk threshold, not a total quota. [Upload limits](https://gin-gonic.com/en/docs/routing/upload-file/limit-bytes/) |
| D: owned HTTP server | Use an `http.Server` when finite budgets and controlled shutdown are needed | `Run` is simpler for a small demo. Blanket timeouts can break streaming; socket deadlines do not replace cooperative application cancellation. [Gin server configuration](https://gin-gonic.com/en/docs/server-config/custom-http-config/), [HTTP server source](https://go.dev/src/net/http/server.go) |
| R: shutdown completion | Wait for bounded shutdown with a live cleanup context; account for workers and hijacked connections separately | Merely starting shutdown and exiting loses work. A queue/process manager is optional, not needed for every service. [Gin shutdown](https://gin-gonic.com/en/docs/server-config/graceful-restart-or-stop/) |
| R: exposure-specific browser/log policy | Match CORS, credentials, cookies/CSRF, and logging to the actual boundary | CORS is not authorization. Built-in recovery sanitizes Authorization in request dumps but not every secret; broad logging defaults need review. [Security guide](https://gin-gonic.com/en/docs/middleware/security-guide/), [CORS](https://github.com/gin-contrib/cors), [recovery](https://github.com/gin-gonic/gin/blob/v1.12.0/recovery.go) |
| D: measure the endpoint; O: optimization | Profile actual payloads, middleware, and dependencies before codec swaps, pools, body caching, or extra concurrency | Router throughput alone does not predict application latency. Extra buffering and concurrency have memory/lifetime costs. [Existing Go measurement policy](../../standards/go/verification.md) applies |

The official error-handler tutorial renders `err.Error()` and does not illustrate
a committed-response guard. Its useful mechanism is error collection and the
post-handler phase; the adopted policy adds public-code mapping and response
ownership for real API contracts. Likewise the goroutine tutorial's copy is a
metadata technique, not a promise of durable work. These are explicit limitations
of tutorial scope, not a claim that the underlying APIs are defective.

## Verification, adoption, and rejected defaults

Use `httptest` through the real route tree for HTTP/binding/middleware behavior;
use a live server only when transport semantics need it. Select meaningful cases
for changed boundaries rather than requiring every category on every edit.
Domain tests and actual adapter/integration checks retain separate responsibilities.
Global Gin mode/decoder/validator changes must not race parallel tests.
[Gin testing](https://gin-gonic.com/en/docs/testing/),
[shared verification](../../standards/verification.md).

The four sections are grouped by decisions: handlers/binding, routing/middleware,
runtime, and verification/compatibility. The short entry holds only essential
rules and reading conditions. Two longer code examples are reached through their
own sections. Research and examples are optional, with no recursive reading rule.

The catalog keeps **17 profile IDs** and the existing combined `go-gin` identity.
Six Gin resources join the eight Go resources. Selecting Go without Gin therefore
still makes both families available, but Gin instructions are conditional on actual
use. This is the existing profile granularity, not Gin detection or automatic
reading. Unrelated stacks receive neither resource family unless the profile is
explicitly selected. Splitting IDs/resource conditions would require a different
delivery contract and is unnecessary for K02.

Core rules, Go domain/concurrency/persistence guidance, and the verification
lifecycle keep their current owners. Existing K01 sections/examples remain
unchanged. No composer, native adapter, role/model assignment, or later topic
needs modification for this adoption.

Rejected defaults: every handler gets an interface/base class; context stores
services; tags enforce business state; every endpoint uses strict JSON; every
request opens a DB transaction; a new goroutine implements durable jobs; all
proxies are trusted; all endpoints share one timeout; a newer codec is inherently
better; every Gin task loads all sections. Each can only be reconsidered against
a concrete contract, compatible version, and observable benefit.

All eight common coverage areas are addressed. Gin-specific ORM internals and
database isolation algorithms are inapplicable because Gin supplies neither;
their HTTP integration is covered and their deeper adoption retains later owners.
CLI/native-agent behavior and actual context-token savings are outside this stage.

Actual checks, commands, failures resolved, and evidence limits are recorded once
in the [K02 plan record](../plans/2026-09-21-engineering-practices.md#k02-working-scope).
The next topic is K03 Python after the user's review checkpoint.
