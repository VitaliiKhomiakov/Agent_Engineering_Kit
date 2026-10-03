# Symfony verification and compatibility

Read for tests/review, routing or container changes, upgrades, deployment, or
performance/security work. Use [shared verification](../verification.md) and
[PHP checks](../php/verification.md); do not install a new test/analyzer platform
for a routine move when the existing project already has suitable checks.

## Match checks to the affected boundary

Test state rules without HTTP where possible. Exercise the actual request/kernel
path for controller registration, mapping/validation, authorization and public
response changes: invoking a controller directly skips routing, argument resolvers,
listeners and Security. Check meaningful valid and rejected inputs, state after
refusal, safe output/error fields, and affected status/headers.

Use the project's KernelTestCase/WebTestCase and configured client for integration
or functional tests where present. Kernel/browser reboot and service reset can
hide persistent-state bugs or detach held test objects; account for that when
testing several requests. Isolate/reset fixtures deliberately instead of relying
on test ordering. Keep external calls behind the installed mock transport; use a
live server/browser only for a behavior that needs it.
[Testing](https://symfony.com/doc/7.4/testing.html).

For HttpClient, test expected status, malformed/oversized data, transport failure,
early exit and ownership. MockHttpClient issues a distinct response from the
MockResponse factory fixture; observe the issued response or supported progress
metadata when checking cancellation. Do not infer cleanup from an untouched
fixture's metadata. Mocked timeout chunks do not prove wall-clock enforcement.

For messages, check the configured bus/routing and the relevant validation,
handler effect, duplicate delivery or failure behavior. An in-memory transport
does not prove broker acknowledgement, concurrent idempotency or durability.
Authentication/authorization changes need allowed and denied actor/target cases;
checking only a logged-in happy path misses the exposed contract.

## Wiring, types, and moves

Run applicable PHP syntax/static checks over owned source, configuration and tests.
Use the project's PHPStan/Psalm configuration and framework extension where needed;
framework reflection is not permission for unchecked casts, blanket mixed values,
new ignores, or weakened checks. Keep precise PHPDoc at integration APIs and narrow
external values before business use.

Check the affected container and routes using supported commands such as
`lint:container`, `debug:container`, `debug:autowiring`, `debug:router` and
`router:match`. A successful boot/container compile does not prove a public route
resolves with the intended methods, arguments and authorization. Check the actual
environment, service aliases/tags, route imports and relevant generated caches.
[Container diagnostics](https://symfony.com/doc/7.4/service_container/debug.html),
[routing](https://symfony.com/doc/7.4/routing.html).

Preserve route names, DTO/serializer contracts, service IDs, reflection/string
registrations, message identifiers and ORM mappings during a file move. Coordinate
cache invalidation/rebuild and worker restart where deployment needs them. Moving
an entity file does not itself authorize schema DDL or a new domain/persistence
model. Keep the existing Doctrine guidance until its dedicated adoption stage.

## Versions and operational applicability

Record component versions from Composer's lock/installed metadata, PHP/SAPI and
extensions, plus actual enabled bundles, configuration and recipes. On 2026-09-21,
7.4 is an LTS branch requiring PHP 8.2+; 8.1 is the stable branch requiring PHP
8.4+. Existing 6.4/7.x/8.x projects retain their supported target. Component patch
numbers can differ; a 7.4 profile does not mean every package is exactly 7.4.19.
[7.4 release](https://symfony.com/releases/7.4),
[8.1 release](https://symfony.com/releases/8.1).

Before a major upgrade, follow the project's supported minor/patch path, resolve
relevant deprecations, inspect UPGRADE/recipe/configuration changes and verify the
affected integrations. Do not copy current-documentation features into an older
runtime or use ignored platform requirements as a migration strategy. Mapping
attributes, serializer type extraction, service discovery and error behavior have
version-specific details; preserve API contracts or explicitly plan their change.
[Major upgrades](https://symfony.com/doc/7.4/setup/upgrade_major.html).

For deployment changes, verify production environment/debug settings, secret
provisioning, cache warmup, writable runtime directories, worker restart and
rollback sequencing. Run dependency/advisory checks under the existing policy;
a clean advisory result does not prove application security. Preserve appropriate
proxy/host trust, cookie/CSRF behavior, redacted logs and profiler access.
[Deployment](https://symfony.com/doc/7.4/deployment.html).

Measure the relevant production SAPI and workload before changing OPcache,
preload/JIT, container/serializer caches or worker counts. Development/profiler
overhead and HttpClient tracing can distort memory/latency observations. A CLI
fixture is not evidence for FPM concurrency, real TLS/disconnects or persistence.
[Performance](https://symfony.com/doc/7.4/performance.html).

Optional [research](../../docs/research/2026-09-21-symfony-engineering-practices.md)
records evidence and alternatives; the
[practice plan](../../docs/plans/2026-09-21-engineering-practices.md) records exact
executed tools/checks and limits. Neither is routine mandatory context.
