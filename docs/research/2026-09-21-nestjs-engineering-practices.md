# NestJS engineering practices: evidence and adoption

Research date: **2026-09-21**. Scope: K12 of the [approved plan](../plans/2026-09-21-engineering-practices.md).
This is optional research; the [Nest entry](../../standards/nestjs.md) owns conditional
reading. K09–K11 retain shared JS, strict TS and Node ownership. React/Next.js,
database-specific adoption and native-client pilots are outside this stage.

## Versions, evidence and strength

The current [migration guide](https://docs.nestjs.com/migration-guide) documents
Nest 12, ESM core packages, separate runtime/CLI prerequisites and new schema-based
APIs. [Release 12.0.4](https://github.com/nestjs/nest/releases/tag/v12.0.4) and public
npm metadata were checked; examples pin **12.0.4** across common/core/platform/testing
where used. The runtime is existing **Node 24.13.0**, with **Fastify 5.12.5**,
**class-validator 0.15.1**, **class-transformer 0.5.1**, **reflect-metadata 0.2.2**
and **RxJS 7.8.2**. No Nest CLI or application migration is run. The installed
Node patch is historical execution evidence, not a deployment recommendation.

Development tools are native **TypeScript 7.0.2**, compatibility package **6.0.2**
resolving compiler/API **6.0.3**, **ESLint 10.11.0**, **typescript-eslint 8.70.0** and
**@types/node 24.13.6**. Native 7 checks/emits the examples; typed lint uses the 6.x
API arrangement established in K10. The two isolated temporary npm projects have
pinned direct dependencies and saved locks/integrities; a fresh manifest-only
install may resolve different transitive versions. No workspace/global dependencies
were changed. The examples exercise ESM with emitted legacy decorator metadata.

All sources below were checked on the research date. Versioned
[11 validation](https://docs.nestjs.com/v11/techniques/validation) and
[11 serialization](https://docs.nestjs.com/v11/techniques/serialization) distinguish
existing class-based mechanisms from new 12 APIs. Installed 12.0.4 pipe/serializer
source was also inspected and hashed under the stage directory; unsuccessful web
fetches of tagged source were not treated as evidence.

- **R — framework requirement:** existing user policy or a necessary boundary,
  ownership, security or truthful-verification contract.
- **D — recommended default:** a useful choice under its stated condition.
- **O — optional technique:** justified by an actual requirement and its cost.

Nest API behavior and framework policy are different claims. Module layout,
independent business boundaries and proportional verification are project decisions;
they are not requirements imposed by decorators alone.

## Coverage map

| Research area | Adopted decision and owner |
| --- | --- |
| 1. Architecture and modules | R: cohesive feature boundaries with explicit public exports; [modules/providers](../../standards/nestjs/modules-providers.md) |
| 2. Construction and patterns | D: managed DI, explicit tokens and small factories; O: dynamic modules, request scope or CQRS for actual needs; modules/providers and [application](../../standards/nestjs/application-lifecycle.md) |
| 3. Contracts, validation and errors | R: executed metadata/schema path, deliberate transforms, output projection and error mapping; [transport contracts](../../standards/nestjs/transport-contracts.md) |
| 4. State, concurrency and resources | R: context lifetime, awaited effects and owned cleanup; application and Node profile |
| 5. Persistence and external APIs | R: correct transaction manager, idempotency and durable acknowledgment ownership; application |
| 6. Testing and review | R: actual DI/pipe/serializer evidence for changed boundaries; [verification](../../standards/nestjs/verification-operations.md) |
| 7. Security, operations and performance | R: authorization, bounded inputs and secret handling; O: measured scope/cache/adapter/telemetry changes; verification |
| 8. Versions and migration | R: actual packages, emitted metadata, loader and adapter contract; entry and verification |

## Modules, construction and scope

**Problem:** globally visible or duplicated providers hide dependencies and state.
[Modules](https://docs.nestjs.com/modules) and [custom providers](https://docs.nestjs.com/fundamentals/custom-providers)
define the container mechanisms. **R:** retain feature cohesion and explicit exports,
independent component files and named consumer contracts. **D:** inject a concrete
capability through a class/symbol token, and use a small factory for pure application
classes. Interfaces are erased; runtime tokens are not interchangeable with them.
**Alternative/cost:** direct construction suits pure tests and assembly, while
constructing a managed service inside a controller bypasses configured lifetime.

**D:** `useExisting` when an alias must preserve instance identity; `useClass` and
duplicate registrations may construct additional instances. **O:** dynamic modules
for real per-application configuration, not as a generic wrapper for every feature.
The provider example uses a configurable output path and exports only its sink
capability; a parent module constructs the pure use case against that exported token.

[Async providers](https://docs.nestjs.com/fundamentals/async-providers) can delay
dependent construction. **R:** await readiness and own partial acquisition failure.
**Cost/alternative:** ordinary synchronous providers suffice when no asynchronous
resource exists; an async factory alone does not define shutdown or cancellation.
The file fixture tests both successful acquisition and refusal to overwrite an
existing path, rather than assuming a returned promise means startup succeeded.

[Scope documentation](https://docs.nestjs.com/fundamentals/injection-scopes) explains
singleton/request/transient behavior and request-scope propagation. **D:** singleton
stateless services and reusable clients. **O:** request scope for a genuine contextual
dependency; explicit arguments or existing correlation context are often simpler.
**Cost:** allocation and propagated scope can affect the graph. No provider scope is
a transaction or authorization guarantee. [Cycles](https://docs.nestjs.com/fundamentals/circular-dependency)
can also arise from file/barrel imports; **R:** inspect ownership first. **O:** a
supported `forwardRef` only after the legitimate cycle and initialization limits are
understood. CQRS/event buses/repositories remain optional architecture choices.

## Validation, transformation and serialization

[Validation](https://docs.nestjs.com/techniques/validation) describes two different
mechanisms in 12. **R:** class-validator `ValidationPipe` requires the concrete
runtime DTO path, value imports and emitted metadata; schema-based validation needs
an actual attached schema and registered pipe. **D:** preserve the project's chosen
mechanism. **Alternative/cost:** schema-derived contracts avoid unnecessary DTO
classes, but switching validator libraries changes coercion/error/unknown-field
behavior and is not incidental cleanup.

[class-validator](https://github.com/typestack/class-validator) and
[class-transformer](https://github.com/typestack/class-transformer) document nested
validation, optional/null semantics and transformation. **R:** separately validate
container, elements and representation; choose reject/strip/preserve and conversion
rules deliberately. **D:** explicit per-parameter conversion rather than permissive
global coercion. **Cost:** decorators, groups and partial DTOs can silently change
what is accepted. `@Type` supplies construction, not validation, and `@IsOptional`
permits both null and undefined. Whitelist membership is not TS property presence.

The installed 12.0.4 `ValidationPipe` explicitly defaults `forbidUnknownValues` to
false before applying options, despite the validator library's different default.
This is an implementation observation, not a universal default to copy. The example
sets its policy explicitly and rejects fifteen invalid representations before state
change, including nested extras, missing/null fields and numeric strings.

**Problem:** the [serialization page](https://docs.nestjs.com/techniques/serialization)
uses broad wording about decorators applied during plain-object transformation.
The checked `ClassSerializerInterceptor` implementation calls class-transformer;
it does not run class-validator. **R:** do not describe exposure/transformation as
output validation. **D:** explicit result projection; **O:** the class interceptor
with class instances or its verified `type` option where the project needs that
metadata. TS return annotations and input whitelists do not filter response secrets.
**Cost:** nested envelopes and manual adapter responses may follow a different path.

The HTTP fixture returns a plain typed receipt with an internal field, selects a
class-transformer response type, and checks the final adapter response excludes
that field. That deliberate serializer demonstration is not permission to return
raw ORM objects; projection at the application/transport boundary can be simpler.

**O:** 12's Standard Schema serializer when an existing response schema warrants it.
Installed source calls its validation function for objects, maps top-level arrays
per element, and bypasses primitive/null/StreamableFile responses. Thus this is not
blanket validation of every return value. These dispatch details are source-inspected,
not a claimed schema-library integration test; verify the actual envelope/library
when adopting it. No extra schema library is required by this stage.

## Request flow, authorization and effects

The [request lifecycle](https://docs.nestjs.com/faq/request-lifecycle) places guards
before pipes and interceptors around downstream work. **R:** guard code must not
trust a controller DTO that has not yet been validated. [Authorization guidance](https://docs.nestjs.com/security/authorization)
supports transport checks, while resource/state authorization remains project policy
at the reusable operation. **D:** explicit input/identity boundaries; avoid moving
business operations into a generic guard/interceptor. **Cost:** duplicating complete
use-case policy in every entry point drifts and can miss a queue or CLI path.

**R:** register global components with the required DI and transport scope. The
[hybrid application reference](https://docs.nestjs.com/faq/hybrid-application)
documents that HTTP global configuration is not inherited by default. **Alternative:**
configure the actual consumer/transport explicitly; do not assume arbitrary direct
method calls invoke pipes. [Filters](https://docs.nestjs.com/exception-filters) define
error mapping, not automatic domain meaning or a universal authorization response.
**D:** map documented failures and retain unexpected causes without exposing them.

**R, project-policy deduction:** keep current-state invariants and transaction
ownership behind transport. [Database integration](https://docs.nestjs.com/techniques/database)
provides DI and transaction facilities, but all related calls still need the intended
session/manager. **D:** a focused operation and explicit adapter; **O:** an outbox or
other consistency mechanism only when multiple effects require it. **Cost:** local
locks or in-memory examples cannot protect other replicas or establish SQL rollback.

[Queues](https://docs.nestjs.com/techniques/queues) and [interceptors](https://docs.nestjs.com/interceptors)
provide useful integration points. **R:** own completion/acknowledgment, cancellation
and idempotency at the actual effect boundary. **D:** await a required operation;
avoid detached work or repeated cold-observable subscriptions. **Alternative/cost:**
ordinary synchronous application sequencing is simpler when durability/fan-out is
not required. RxJS timeout/unsubscribe does not imply cancellation of arbitrary
promises or rollback of remote writes; K09/K11 retain those general rules.

## Lifecycle, operations and verification

[Lifecycle hooks](https://docs.nestjs.com/fundamentals/lifecycle-events) distinguish
explicit application close, enabled OS-signal handling and request-scoped classes.
**R:** disposal belongs to the component that owns a resource, and required release
must be awaited. **D:** a simple hook on the shared adapter; use explicit ownership
for tightly coupled cleanup order. **Cost/limit:** hook ordering changed in 12;
neither a hook nor app close universally joins detached application work. Failed
startup needs its actual acquisition cleanup; request scope is not a disposal hook.

[Configuration](https://docs.nestjs.com/techniques/configuration) provides assembly
facilities, not proof that every consumed value was validated. **R:** validate known
configuration and redact sensitive values. [Helmet](https://docs.nestjs.com/security/helmet),
[rate limiting](https://docs.nestjs.com/security/rate-limiting) and adapter-specific
facilities are options for applicable deployment requirements, not a mandatory new
security stack. **O:** tracing/profiling/cache/adapter changes after evidence of need;
preserve tenant visibility, bounded capacity and the project's existing tooling.

[Testing](https://docs.nestjs.com/fundamentals/testing) and
[Fastify integration](https://docs.nestjs.com/techniques/performance) support focused
container and HTTP checks. **R:** verify actual registrations and emitted metadata
where changed. **D:** pure checks for business logic, an application context for DI,
and an initialized adapter for transport behavior. **Cost/limit:** providing all
internals manually can bypass missing exports; calling a controller method bypasses
its framework pipeline. In-process injection does not establish TCP/TLS behavior.

**R:** preserve supported existing contracts when upgrading. Check actual package
peers, Node/CLI floors, CJS/ESM loading and compiler metadata; do not infer them from
one engine field. New generator/linter/runner defaults are not retrofit requirements.
The examples use no CLI, and execute only the stated versions on one host. No
Express/legacy-major matrix, real queue/database, OS-signal, schema-library integration,
proxy/load benchmark or native-agent pilot is claimed.

## Adoption and evidence

The entry stays short; its three original requirement blocks move verbatim into
their conditional owners. Four sections and two separate examples are copied only
with the selected `nestjs` profile. Existing 17 IDs, Node/TS dependencies and globs
remain. Extra files are available through task links, not concatenated into ENTRY
or native instructions; research stays outside installed instruction bundles.

The [HTTP example](../../standards/nestjs/examples/validated-command.md) and
[provider example](../../standards/nestjs/examples/provider-lifecycle.md) contain
the exact tested code/configuration. The [plan](../plans/2026-09-21-engineering-practices.md#k12-result-and-verification)
records commands, scoped baselines, delivery checks and limitations. The one-report
file sink demonstrates lifecycle ownership, not atomic publication, crash durability
or a general persistence adapter. K13 React is the next user checkpoint.
