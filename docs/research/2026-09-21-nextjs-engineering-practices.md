# Next.js engineering practices: evidence and adoption

Research date: **2026-09-21**. Scope: K14 of the [approved plan](../plans/2026-09-21-engineering-practices.md).
This optional research supports the [combined entry](../../standards/nextjs.md).
K13 retains React state/component/Effect rules. PostgreSQL and later adoption stages
are outside this scope; database ownership is assessed only at the Next.js boundary.

## Version and evidence contract

Public npm metadata and the installed package identify **Next.js 16.3.5**; current
[documentation](https://nextjs.org/docs/app/getting-started/project-structure) identifies
the same version. The [16.3 release](https://nextjs.org/blog/next-16-3) describes
optional navigation/compiler features and version-matched package documentation.
Installed `next/dist/docs` was inspected for Cache Components, migration, Route
Handlers and TypeScript. Those local source digests are retained with the stage.
The [support policy](https://nextjs.org/support-policy) and
[August security release](https://nextjs.org/blog/august-2026-security-release) were
also checked; an example pin is not a permanent security/support recommendation.

Executed configuration: App Router, `cacheComponents: true`, Node runtime,
production webpack build/start, **Node 24.13.0**, **React/React DOM 19.3.0** and
matching **19.3.0 types**. Next also supplies its internal server-rendering machinery;
the package pins do not describe every internal React implementation. The Node
patch is historical local execution evidence, not a deployment recommendation.

Tools: **TypeScript compatibility package 6.0.2**, reporting **compiler/API 6.0.3**,
**ESLint 9.39.5**, **eslint-config-next 16.3.5**, **typescript-eslint 8.70.0**,
**@types/node 24.13.6** and **server-only 0.0.1**. The exact `tsc6` executable and
Next compiler-API mode run strict authored-code checks. `skipLibCheck` skips vendor
declarations, not the example's contracts. Native TS 7, Turbopack and other routers
were not executed. The temporary project retains its resolved lock/integrities;
manifest-only reinstall can resolve different transitives. No workspace/global
package was changed.

All linked primary sources were checked on this date. Strength labels distinguish:

- **R — framework requirement:** a necessary correctness/trust/ownership contract
  or existing user policy; its reason is stated, not presented as a Next.js opinion.
- **D — recommended default:** a useful starting choice under the named condition.
- **O — optional technique:** an actual requirement justifies its cost.

## Coverage and owners

| Area | Adopted decision and instruction owner |
| --- | --- |
| 1. Architecture and modules | R: thin router adapters and explicit environment boundaries; [routing](../../standards/nextjs/routing-composition.md) and [feature structure](../../standards/nextjs-feature-structure.md) |
| 2. Idioms/construction/patterns | D: reuse a coherent server read/operation or existing backend; O: a BFF/DAL for a real boundary, not mandatory layered scaffolding |
| 3. Contracts/validation/errors | R: validate public inputs, authorize operations and project output; [security](../../standards/nextjs/server-client-security.md) |
| 4. State/concurrency/lifetime | R: distinguish request/host/cache lifetimes and awaited effects; [data](../../standards/nextjs/data-cache-mutations.md), React and Node owners |
| 5. Persistence/integrations | R: authoritative transaction/idempotency and deliberate freshness; data; SQL/ORM internals stay with later topics |
| 6. Testing/review | R: actual build/HTTP/cache evidence when those boundaries change; [verification](../../standards/nextjs/verification-migration.md) |
| 7. Security/operations/performance | R: protect data and verify host capability; O: measured caching/streaming/optimization; [runtime](../../standards/nextjs/rendering-runtime.md) |
| 8. Version/migration | R: router/cache/toolchain-specific guidance and authorized migration; entry/verification |

## Routing and capability organization

**Problem:** framework filenames become universal services or a preferred tree gets
mistaken for framework law. [Project structure](https://nextjs.org/docs/app/getting-started/project-structure)
and [layouts/pages](https://nextjs.org/docs/app/getting-started/layouts-and-pages)
permit different organization and define actual route conventions. **D:** retain
compact product-capability modules with explicit public dependencies and route-local
UI where cohesive. **R:** preserve the user's existing import directions, small-change
scope and React cohesion threshold. No full FSD or backend-style class stack is added.

**Alternative/cost:** one page and private helper can suffice for a small feature;
extract a capability when ownership/reuse warrants it. Route groups and private
folders change filesystem organization without replacing URL/layout semantics.
Parallel/intercepted routes are **O** for a real navigation need, with reload/default
slot costs. **R:** preserve direct URLs and state/focus expectations when moving code.

[Route Handlers](https://nextjs.org/docs/app/getting-started/route-handlers) and the
[route API](https://nextjs.org/docs/app/api-reference/file-conventions/route) define
HTTP adapters. **D:** call an existing server capability directly from server UI;
use a public HTTP entry for actual external/browser consumers. **Cost:** an internal
HTTP hop adds deployment/build dependencies, latency and another transport contract.
The [BFF guide](https://nextjs.org/docs/app/guides/backend-for-frontend) supports
purposeful aggregation but does not make Next a durable job/database service.

**R:** retain router-specific contracts. [Pages server props](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props)
remain request-time loaders with public serialized output, not RSC. App Router
request APIs/params are asynchronous in the verified version. **D:** use generated
helpers after generation; **R:** still validate representation and meaning. Moving
Pages code into App conventions requires an authorized migration, not a local rename.

## Server/client trust and typed operations

**Problem:** server implementation details leak through imports or oversized props.
[Server/Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components)
explain the module boundary and initial rendering. **R:** enforce server-only imports
and minimal public DTOs separately: a guard prevents a dependency leak, but cannot
stop an authorized server function from returning a secret field. **D:** keep the
interactive boundary narrow. **Alternative/cost:** a client wrapper receiving server
children preserves composition; putting the whole tree in the client graph increases
bundle exposure. A `.server.ts` suffix is not enforcement.

[Data security](https://nextjs.org/docs/app/guides/data-security) recommends a server
DAL for new applications and existing HTTP APIs for suitable established systems.
That is ecosystem advice, not an obligation to rewrite an independent backend.
**D:** centralize request identity, permitted reads and public projection in their
existing server owner. **R:** independent business operations retain current-state
and permission rules under core policy. Directory boundaries alone create no trust.

[Authentication](https://nextjs.org/docs/app/guides/authentication) and
[mutation guidance](https://nextjs.org/docs/app/getting-started/updating-data) support
**R:** authorize every public mutation against current server identity/resource
ownership. Layout/Proxy checks improve navigation but do not protect all entry paths.
Treat Action arguments and bound values as untrusted. Hidden buttons, Action IDs or
closure protection are not operation permission. Prefer typed expected refusals;
keep framework redirect/notFound control flow out of broad error mapping.

**R:** parse only intended FormData/JSON fields and project responses. React's
`$ACTION_` fields make blind form-to-record persistence particularly inappropriate.
[Cookies](https://nextjs.org/docs/app/api-reference/functions/cookies) have request
lifetime and write-context rules. **D:** use the established session provider;
**cost:** a homemade auth system adds expiry/revocation/CSRF/secret-management work.
Cookie mutations and explicit-bearer APIs need different request defenses. The
example deliberately uses an isolated opaque-token identity fixture, not production
session code. Public handlers still need suitable ingress/application resource limits.

## Data caches, consistency and transactions

**Problem:** APIs with similar names get treated as one global cache. The current
[caching guide](https://nextjs.org/docs/app/getting-started/caching) and
[previous-model guide](https://nextjs.org/docs/app/guides/caching-without-cache-components)
cover different configurations. **R:** record router/version/cache flags and distinguish
request memoization, reusable server data, prerendered output, router state and CDN
responses. **D:** choose freshness explicitly. **Alternative/cost:** uncached data is
simpler for sensitive/current decisions; caching adds invalidation and key-visibility
obligations. A no-store HTTP response can still contain cached server data.

[`use cache`](https://nextjs.org/docs/app/api-reference/directives/use-cache) and
[`cacheLife`](https://nextjs.org/docs/app/api-reference/functions/cacheLife) define
explicit reusable scopes in Cache Components. **O:** adopt them when the selected
model and host support them. **R:** keys must include meaningful identity/input scope,
and permission checks still occur at their owner. Request credentials do not belong
in an unpartitioned public cache. Private/remote variants add compatibility, storage
and latency considerations; they are not a default substitute for direct private reads.

The [migration guide](https://nextjs.org/docs/app/guides/migrating-to-cache-components)
replaces legacy segment options with explicit scope/lifetime choices and requires
Node runtime. **R:** do not mix its rules with legacy `dynamic`, `revalidate`,
`fetchCache`, `unstable_cache` or experimental PPR recipes. **D:** keep an existing
supported model during ordinary edits; enabling the new one is separate migration
work. Request-time boundaries, retained client state and navigation blocking need
checks when migrating.

**Problem:** the UI appears fresh while a committed change remains hidden in shared
data. [`updateTag`](https://nextjs.org/docs/app/api-reference/functions/updateTag)
provides Server Action-only immediate expiry for read-your-own-writes. **D:** choose
it when that is the requirement and context. [`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag)
with `'max'` accepts stale-while-revalidate; `{ expire: 0 }` fits a Route Handler
requiring immediate next-read freshness. **R:** use a supported profile argument and
assign tags to the intended cached data; do not claim eager refresh of every reader.

[`revalidatePath`](https://nextjs.org/docs/app/api-reference/functions/revalidatePath)
has path rather than shared-tag scope; [`refresh`](https://nextjs.org/docs/app/api-reference/functions/refresh)
is Server Action-only and changes router output without being universal data
invalidation. **Alternative/cost:** a targeted tag can cover consumers in several
routes, while broad path invalidation may add work and still miss external caches.
The choice follows the consistency requirement, not a ritual after every write.

**R:** commit/authorize a mutation at the authoritative backend, then reconcile caches.
An invalidation failure does not roll back a committed operation. Retrying needs its
idempotency contract. React/Next caches cannot reserve stock, implement SQL constraints
or coordinate multiple writers. Transactions/pools have actual backend/host owners;
no specific ORM or Repository is prescribed. Durable side effects need an appropriate
outbox/job mechanism rather than assuming the request process will remain alive.

## Rendering and host behavior

**Problem:** a single slow read blocks useful UI, or request-dependent work accidentally
runs during a build. **D:** deliberate independent reads and meaningful Suspense/error
boundaries under the selected rendering model. **R:** preserve authorization/order
dependencies when parallelizing. **Cost:** streamed failures after headers cannot be
mapped exactly like a pre-response exception; verify status/SEO when relevant.
[Error handling](https://nextjs.org/docs/app/getting-started/error-handling) distinguishes
expected outcomes and unexpected boundary failures. New 16.3 `catchError` and Instant
Navigation tools are **O**, not mandatory changes to all projects.

[Metadata](https://nextjs.org/docs/app/getting-started/metadata-and-og-images) and asset
conventions provide useful owners. **D:** use them when they meet the task; **R:**
keep sensitive fields out of HTML/RSC/metadata and preserve accessibility. Remote
images need constrained sources; build-fetched fonts/content add network dependencies.
A local fixture/asset is a simpler reproducible-build choice where appropriate.

**R:** choose a supported host contract. The [Edge overview](https://nextjs.org/docs/app/api-reference/edge)
contains a generic reference to Proxy, but the more specific current
[Proxy reference](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)
and installed convention document Node as its default and disallow a Proxy `runtime`
config. Adopt the specific version/convention contract, not the older assumption
that every middleware/proxy is Edge. Cache Components also requires Node. A
[static export](https://nextjs.org/docs/app/guides/static-exports) cannot provide this
example's live mutation/session endpoints. Other adapters require their own evidence.

[Environment variables](https://nextjs.org/docs/app/guides/environment-variables)
separate public build-time substitution from server reads. **R:** prove whether a
value is consumed at build or request time before promoting one artifact between
environments; public prefix values are not secrets. [Self-hosting](https://nextjs.org/docs/app/guides/self-hosting)
requires deliberate ingress/streaming, cache storage/tag coordination and deployment
skew handling. **Cost:** local files and one-process memory cannot imply durable
multi-instance state. Legacy incremental cache and `use cache` handlers have different
configuration surfaces. [`after`](https://nextjs.org/docs/app/api-reference/functions/after)
is **O** for bounded post-response work, not a durable delivery guarantee.

## Verification, migration and performance

[Testing guidance](https://nextjs.org/docs/app/guides/testing) distinguishes unit,
integration and browser evidence. **R:** use a real Next pipeline for changed route,
cache and import contracts; a direct function call cannot prove those mechanisms.
**D:** direct tests for pure invariants, production HTTP for server contracts, and
browser/visual evidence for changed critical interactions. **Cost:** HTTP/HTML tests
do not establish hydration, keyboard behavior or navigation state.

[TypeScript integration](https://nextjs.org/docs/app/api-reference/config/typescript)
supplies route type generation and selectable CLI/API checking. **R:** check the
actual compiler and compatible peers, not just an npm script name. The first lint
setup used ESLint 10, but installed React/import/a11y peers accepted only 9; a bounded
metadata lookup selected 9.39.5 and the final peer tree passed. The initial CLI build
path returned unparseable captured configuration in this environment; the documented
API mode passed. This is not evidence of an upstream Next/TS defect. Explicit `tsc6`
avoids relying on the transitive package that happened to provide `tsc`.

[15](https://nextjs.org/docs/app/guides/upgrading/version-15) and
[16](https://nextjs.org/docs/app/guides/upgrading/version-16) upgrade guides mark
request API, caching, bundler, Proxy, lint, runtime and image changes. **R:** preserve
existing router behavior and upgrade only within authorization. A successful current
build does not prove legacy compatibility. **D:** one cohesive route/capability at a
time, with affected callers and real navigation evidence. **O:** measured compiler,
code-splitting and cache improvements; framework performance claims are not project
benchmarks. No blanket upgrade, custom server or new backend architecture is adopted.

## Adoption and verification limits

Five conditional Next.js sections and two separate example documents complement the
unchanged React resources/routes. The existing feature-structure reference gains
router/environment adapter guidance, retaining its original tree and import rules.
It is also registered as an optional combined-profile resource so explicit selection
works in an independently opened project. That does not add an automatic design
profile for React-only metadata. The combined profile copies both topics, but its
short entry keeps Next.js reading conditional; no new profile IDs or dependencies.

The examples share one temporary application to avoid duplicating setup. Six checks
exercise denied/malformed commands, state refusal and direct invariants, public
server/client projection, persistent tagged reuse with authorized expiration and
HTTP method/cache behavior. A separate client-import negative build verifies the
server-only guard. The [plan](../plans/2026-09-21-engineering-practices.md#k14-result-and-verification)
owns exact commands, results and review notes. Example sources/configuration are
published as exact executable blocks; research is not part of automatic native context.

Only the pinned App Router/Cache Components/Node/webpack environment was executed.
No Pages/legacy cache runtime, Server Action dispatcher/updateTag, browser hydration,
critical navigation, visual rendering, real session provider/database, request budget,
concurrent durable mutation, CDN/distributed cache, Edge/static-export deployment,
external adapter, native TS 7, Turbopack or benchmark was tested. The file/token/stock
fixtures demonstrate boundaries, not production infrastructure. Synthetic delivery
checks establish portable artifacts, not model reading compliance or token savings.
P3–P7 remain planned; stop for user review before K15 PostgreSQL.
