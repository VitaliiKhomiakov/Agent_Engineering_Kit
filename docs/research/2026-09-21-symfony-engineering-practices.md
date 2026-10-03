# Symfony engineering practices: research and adoption

Research started and primary sources checked: **2026-09-21**. Scope: **K07,
Symfony**, under the [practice plan](../plans/2026-09-21-engineering-practices.md).
The [combined profile](../../standards/php-symfony-doctrine.md) remains the entry,
with four conditional Symfony sections and two optional examples. This note is
evidence, not a required instruction or copied catalog resource.

## Baseline, versions, and evidence

K06 already owns PHP types, PSR-4, construction, state and resource fundamentals.
The original combined profile required thin controllers, executed DTO validation,
independent live business rules, and an explicit domain/Doctrine model choice.
K07 explains the Symfony mechanisms and their limitations. PHP essentials and all
six PHP resources are preserved; Doctrine domain-placement guidance remains for
K08. No application scaffold, ORM, queue, authentication system or new production
dependency is selected for AgentsFramework by this documentation stage.

| Observed evidence | Applicability and limit |
| --- | --- |
| [Symfony 7.4 release](https://symfony.com/releases/7.4) | LTS, PHP 8.2+, latest listed patch 7.4.19 on the verification date; bug fixes through November 2028 and security fixes through November 2029 |
| [Symfony 8.1 release](https://symfony.com/releases/8.1) | Stable branch on the verification date, PHP 8.4+, latest listed patch 8.1.7; not executed on the available PHP 8.3 runtime |
| PHP 8.3.6 CLI NTS, Zend Engine 4.3.6, amd64 Linux | Reused K06's extracted Ubuntu 8.3.6-0ubuntu0.24.04.11 build from 2026-09-02; not claimed as the latest upstream PHP |
| Composer 2.10.3; PHPStan 2.2.14 | Reused previously verified official PHARs; analysis at max = 10 with PHP target 80200 |
| HTTP example lockfile: 35 packages | FrameworkBundle, HttpFoundation, HttpKernel, Serializer and Validator 7.4.19; DI/EventDispatcher 7.4.17; Routing 7.4.18. Component patch numbers are not uniform |
| Client example lockfile: seven packages | HttpClient 7.4.19 and HttpClient Contracts 3.7.3; the mock transport exercises actual component behavior without network I/O |

Dependencies were installed in two new temporary example projects. Composer
plugins/scripts were disabled; no Flex recipe or installer ran. The one additional
Ubuntu XML package was verified against APT's SHA256 and extracted under `/tmp`,
without system installation. Its extensions and K06's PHP modules were loaded
through a temporary configuration. Composer home/cache, lockfiles, vendor code,
kernel caches, analyzer output and logs remain in the stage directory. Direct
requirements were reconciled with imported packages without changing locked
versions; the subsequent offline lock refresh used cached metadata and reported
the network fallback. Its advisory result is not a new live security audit.

## Coverage and recommendation strength

**R** is a requirement inherited from core or the existing combined profile;
**D** is a default with an appropriate alternative; **O** is a technique justified
by the current task. Symfony's capabilities and authors' recommendations are not
independent authority to impose a new architecture or workflow.

| Research area | Adoption and evidence focus |
| --- | --- |
| Architecture/modules | Entry adapters, existing business boundaries, cohesive directories versus reusable bundles; [structure/services](../../standards/symfony/structure-services.md) |
| Construction/dependencies/patterns | Constructor injection, aliases, private/shared services, configuration, direct calls versus buses/decorators/factories; structure/services |
| Contracts/validation/invariants/errors | Request resolution, Validator execution, presence/coercions, public output and expected refusal; [HTTP/validation](../../standards/symfony/http-validation.md) |
| State/concurrency/cancellation/lifetime | Shared container instances, worker reset, lazy HTTP, kernel termination and bounded consumption; [runtime/effects](../../standards/symfony/runtime-effects.md) |
| Persistence/integrations | Commit/handoff ownership, remote atomicity limits, message schemas/idempotency, client contracts; runtime/effects; detailed ORM adoption remains K08 |
| Verification/review | Real kernel versus direct calls, configuration/route checks, static contracts, mock limitations and failure state; [verification](../../standards/symfony/verification.md) |
| Security/operations/performance | Actor/target checks, CSRF, first-match policy, safe errors, deployment/cache/worker lifetime, measured optimization; HTTP/runtime/verification |
| Versions/migration | Component lockfiles, PHP requirements, deprecations, recipes and older mapping/error behavior; verification |

## Structure, services, and simpler alternatives

**R — preserve boundaries and typed operation contracts.** Controllers, commands
and queue adapters receive input and call the appropriate application operation;
business branching, persistence and external orchestration stay behind them.
This strength comes from [core](../../standards/core.md), not an assertion that
Symfony cannot run business logic inside a controller. Request/RequestStack,
container access and transport-specific models do not belong in an independent
business core. Existing compatible contracts need no duplicate DTO just because
a new directory or adapter exists.

**D — simple cohesive application structure.** Symfony's default directories
and ordinary services are a reasonable starting point. Feature namespaces can
help a real boundary; application-only bundles and mandatory backend layers add
configuration without inherently improving it. A reusable integration bundle
needs an actual distribution/configuration contract. A component-only script
need not install FrameworkBundle. The authors explicitly present their
[best practices](https://symfony.com/doc/7.4/best_practices.html) as adaptable
recommendations. Their preference for AbstractController is not a runtime rule:
the executed example uses a plain controller service.

**D — explicit injection with existing autowiring.** Resolve multiple candidate
implementations through deliberate aliases/bindings. Autoconfiguration handles
supported metadata/tags; it does not validate input or select the business
architecture. Services normally stay private. The fixture exposes only the
in-memory operation to inspect failure state; that is not a production visibility
default. [Container](https://symfony.com/doc/7.4/service_container.html),
[autowiring](https://symfony.com/doc/7.4/service_container/autowiring.html).

**R — own the actual service lifetime.** Installed DI source sets services shared
by default. A held reference does not become new on each message even if a
definition is configured non-shared for subsequent retrievals. Stateless services
are simpler; runtime reset or explicit job ownership is needed for retained
request/user/tenant state. [Definition 7.4.17](https://github.com/symfony/dependency-injection/blob/v7.4.17/Definition.php)
and the Messenger worker contract support that distinction.

**O — factories, decorators, buses, events, and compiler passes.** Use them for a
real construction rule, cross-cutting behavior, dispatch requirement, extension
point or compile-time graph change. An injected concrete service, a direct call,
and a configuration parameter are often sufficient. Do not add a universal base
controller/handler, one interface per class, or a service locator in business
methods. Configuration format and Flex recipe changes follow the existing project
workflow; recipe state is distinct from package version locking.
[Flex recipes and package setup](https://symfony.com/doc/7.4/setup.html#installing-packages).

## Request contracts, validation, and response boundaries

**D — use the installed request-mapping path deliberately.** MapRequestPayload
can deserialize a typed input and invoke Validator before the controller runs;
an ordinary constructor or direct method invocation does not execute that path.
Routes still need explicit methods/media-type/output contracts. MapQueryString,
forms and message validation have their own configuration/defaults.
[Controller](https://symfony.com/doc/7.4/controller.html),
[validation](https://symfony.com/doc/7.4/validation.html).

**R — input attributes must have a consumer.** Keep local field/cross-field
validation free of writes/remote decisions; it does not protect live capacity,
authorization or concurrent uniqueness. Enforce current-state refusal at its
business owner, including non-HTTP paths. The
[request example](../../standards/symfony/examples/request-boundary.md) checks eight
invalid body cases, method rejection, successful reservations, conflict without
mutation, private-field projection, explicit non-HTTP validation and the direct
application invariant. Its shared in-memory state is illustrative, not durable
or concurrently safe inventory.

**D — explicit presence/type/unknown-field policy.** Serializer defaults differ
from native scalar strictness and from a JSON schema. The installed normalizer
may supply null for a missing nullable constructor argument unless
require_all_properties is enabled. Extra fields are ignored by default; choosing
rejection has an exception contract that needs HTTP verification. Groups and
PHPDoc type metadata do not themselves perform an authorization check.
[Serializer](https://symfony.com/doc/7.4/serializer.html),
[AbstractNormalizer 7.4.19](https://github.com/symfony/serializer/blob/v7.4.19/Normalizer/AbstractNormalizer.php).

A failed example check exposed a concrete 7.4.19 integration detail:
allow_extra_attributes=false caused ExtraAttributesException and a default 500.
The installed payload resolver converts malformed JSON and selected denormalizing
errors, but does not catch that exception type. The final example maps this known
input-route exception to a fixed 400 and leaves unrelated failures alone. This
does not contradict the Serializer's promise to reject extra fields; HTTP mapping
was an additional assumption that required evidence.
[Payload resolver 7.4.19](https://github.com/symfony/http-kernel/blob/v7.4.19/Controller/ArgumentResolver/RequestPayloadValueResolver.php),
[extra-field exception](https://github.com/symfony/serializer/blob/v7.4.19/Exception/ExtraAttributesException.php).

**R — public projection and honest errors.** A JsonResponse is not an automatic
output field allowlist/schema validator. Explicitly project intended fields or
apply an established serializer context on the actual output path. Input DTOs,
security users and ORM graphs are not default public models. Preserve meaningful
HTTP headers while replacing error bodies, and keep raw payload/type/driver data
out of public messages. The current controller manual notes an 8.1 change to
custom-type error disclosure; it must not be retroactively assumed on 7.4.

**D — forms/security only for the actual flow.** Forms offer configured field
mapping, validation and CSRF behavior; they are not required for a JSON endpoint.
Symfony's recommendations about constraints on an underlying form object do not
override this project's explicit input-DTO policy or decide Doctrine/domain
placement. Object resolution is not access permission. Check actor plus target
through the established policy/voter and preserve other entry paths. First-match
access-control ordering and browser CSRF/session settings are concrete exposure
boundaries. [Access control](https://symfony.com/doc/7.4/security/access_control.html),
[voters](https://symfony.com/doc/7.4/security/voters.html),
[CSRF](https://symfony.com/doc/7.4/security/csrf.html).

## External effects, messaging, and lifetime

**R — consume/check a lazy operation before claiming success.** HttpClient status,
transport and decoding failures arise at different points. getStatusCode disables
the destructor's automatic HTTP-status failure fallback, so the caller must check
it. A dropped response is not a durable asynchronous job. **D — bound and own
consumption:** configure idle/overall budgets, avoid unnecessary buffering, limit
accumulation and cancel on early return or failure. A direct bounded call is
simpler than concurrency or retries unless the workload requires them.
[HttpClient](https://symfony.com/doc/7.4/http_client.html).

The [client example](../../standards/symfony/examples/http-client.md) checks twelve
success/absence/status/data/timeout/transport cases. It accepts zero quantity,
returns a named snapshot, interprets 404 according to its specific contract and
does not return upstream internals. A test initially inspected the factory
MockResponse rather than the distinct issued response. Source inspection showed
the wrapper creation; final checks observe issued-response cancellation through
supported progress metadata, including failure paths. A constructor-options
assumption was also corrected to the supported withOptions API.
[MockHttpClient 7.4.19](https://github.com/symfony/http-client/blob/v7.4.19/MockHttpClient.php),
[MockResponse 7.4.19](https://github.com/symfony/http-client/blob/v7.4.19/Response/MockResponse.php).

**O — Messenger when actual delivery/dispatch needs it.** Dispatch can be
synchronous or routed to a transport; enqueue success is not completed business
work. Validation middleware must be configured if that is the chosen boundary.
Repeated delivery is normal after acknowledgement failure: use stable business
idempotency semantics, concurrency protection where needed, bounded retries and
an owned failure/replay procedure. Persistent service state needs the runtime's
reset mechanism; resetting is not a general rollback guarantee.
[Messenger](https://symfony.com/doc/7.4/messenger.html).

**R — required transaction/handoff timing.** A database transaction does not
atomically include a remote broker or HTTP call. **O — durable handoff/outbox**
where that guarantee is actually required; a direct operation is simpler when it
is not. Detailed Doctrine transaction/mapping adoption stays in K08. Likewise,
kernel.terminate is not a durable queue or a safe place for success-critical
commit: response timing depends on SAPI/mode and it may already be sent.
[HttpKernel](https://symfony.com/doc/7.4/components/http_kernel.html).

## Verification, operations, and migration

**D — verify the affected layer.** A direct controller call misses the route,
container, argument resolvers, listeners and Security. Use actual kernel/functional
tests for those contracts and cheap isolated checks for application behavior.
Check static types and actual wiring; lint:container adds checks beyond an ordinary
container compilation. Existing test/analyzer setup takes priority over a new
framework solely for a small move. [Testing](https://symfony.com/doc/7.4/testing.html),
[container diagnostics](https://symfony.com/doc/7.4/service_container.html#linting-service-definitions).

PHPStan initially reported the fixture's private MicroKernel configuration hooks
as unused. The example now uses the standard PHP configuration files consumed by
MicroKernelTrait, keeping source/config/tests statically checkable without ignores
or a new extension dependency. Its generated cache was rebuilt to exercise that
configuration with debug disabled. All eleven PHP files then passed level 10;
the check does not analyze all vendor internals or prove every framework callback.

**R — preserve exposed contracts during a move/upgrade.** Route names/methods,
service IDs/aliases/tags, serializer/message names, caches and worker restart need
their actual integration checks. A file move is not authorization for schema DDL.
**D — follow supported migration paths** using lockfiles, deprecations, UPGRADE and
recipe/configuration changes, rather than treating current docs as installed APIs.
[Major upgrades](https://symfony.com/doc/7.4/setup/upgrade_major.html).

**D — deployment and performance from actual conditions.** Production debug,
secrets, cache warmup, writable runtime paths, worker lifecycle, proxy/host trust,
safe logs and profiler access depend on the deployment contract. Measure actual
latency, memory, queries/HTTP and cache behavior in its SAPI before changing worker
counts, tracing or OPcache/preloading. Cache/Lock/RateLimiter components can help
a real policy; their backend/scope does not automatically enforce a distributed
business invariant. [Deployment](https://symfony.com/doc/7.4/deployment.html),
[performance](https://symfony.com/doc/7.4/performance.html).

## Evidence limits and checkpoint

Examples ran on one PHP CLI build and the locked Symfony 7.4 components. Static
targeting of PHP 8.2 is not a multi-version execution matrix. No real database,
broker, authentication system, concurrent inventory update, network timing/TLS,
server backpressure/disconnect, FPM/persistent-worker deployment, benchmark,
external installation or native-client pilot was exercised. Researched Messenger,
Security and deployment behavior is not claimed as locally executed integration.

The [practice plan](../plans/2026-09-21-engineering-practices.md) records exact
commands, lock/version evidence, portable delivery checks, scoped baseline and
review checkpoint. K08 and the native-adoption P3–P7 stages remain planned.
