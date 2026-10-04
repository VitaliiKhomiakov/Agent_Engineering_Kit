# NestJS verification and operations

Read for tests, adapter behavior, configuration/security, performance or upgrades.
Use the shared [verification policy](../verification.md), [TypeScript checks](../typescript/toolchain-verification.md)
and relevant [Node operations](../nodejs/lifecycle-verification.md), not another
universal test stack or migration workflow.

## Match checks to the changed boundary

Pure use cases/domain functions can be tested directly with narrow typed collaborators.
That check cannot prove Nest module exports, token identity or decorator metadata.
Use `Test.createTestingModule` or an application context for changed DI graphs;
verify the real imports/exports and configured overrides instead of providing every
internal dependency in a test and thereby bypassing the boundary being checked.

For input/output changes, exercise the actual configured Nest adapter path: invalid
nested elements, unknown/missing/null fields and transformations relevant to the
contract; current-state refusal without mutation; final serialized fields and errors.
Calling a controller method directly does not invoke its pipes, guards or interceptors.
A testing module's `compile()` is not a replacement for the app's initialization and
bootstrap configuration. Keep that configuration reusable where an integration test
must match production; copying options into a test can validate a different app.

Use the existing runner. Fastify's injection can check its in-process HTTP pipeline
after initialization/readiness without a listening socket; it does not prove TCP,
TLS, proxy or signal behavior. Use the real relevant transport when those change.
Always await test work and close applications/clients; a test helper's cleanup must
not turn failed startup or a rejected request into a hanging suite.

The [HTTP example](examples/validated-command.md) checks class-based input validation,
state refusal and actual output projection. The [provider example](examples/provider-lifecycle.md)
checks exported capability wiring, alias identity, initialization and awaited teardown.
Both compile actual decorators; neither a TS type assertion nor a mock framework
stands in for those boundaries.

## Security and operational behavior

Keep secrets and request identity out of singleton mutable fields. Authenticate at
the actual entry point; enforce resource authorization at the use-case boundary.
Configure CORS, security headers, cookie/CSRF and rate limits for the chosen adapter
and deployment where required; a guard annotation alone is not a full threat model.
Trust proxy headers only according to known proxy topology. Limit body/upload/array
sizes and external-call capacity before expensive validation or business work.

Use the accepted configuration validator, secret source and logger; do not expose
raw validation targets/values or exception causes in responses. Give tracing and
metrics bounded buffers/cardinality, redact credentials and validate correlation
context propagation. The availability of Nest 12 observability integrations does
not require installing a new SDK or exporting telemetry to an external service.

Measure actual latency, heap, validation cost and pool pressure before introducing
request scope, caching, CQRS, worker pools or a different adapter. Cache keys and
invalidation must respect identity/tenant/data visibility. Express middleware and
Fastify plugins are not interchangeable; adapter changes affect parsing, plugins,
error handling and request/reply APIs, not just a throughput number.

## Existing projects and version changes

Align Nest core/common/platform/testing packages and integration peer ranges from
manifests and locks. Verify Node, the actual TS compiler/loader, emitted runtime
metadata, validator/transformer versions and launch/build artifact. New CLI defaults
are not an obligation to change an existing runner, linter or module format.

Nest 12's core packages are ESM; application and CLI tooling have different Node
requirements. A compatible CommonJS application can use supported `require(esm)`;
that does not authorize converting the application's sources or assume every
host enables it. The standalone type-strip mode in Node does not supply Nest's
legacy decorator metadata. Check actual emitted imports and runtime registrations.

For **Nest 12 with Jest**, the
[migration guide's testing section](https://docs.nestjs.com/migration-guide#testing-stack)
(checked 2026-10-04) requires Node **24.9+** for Jest to load the ESM-only Nest
packages; older runtimes can fail with `ERR_REQUIRE_ASYNC_MODULE`. This test-runtime
floor does not replace separate application, CLI or package compatibility checks.
On an affected migration, run the retained Jest command and application checks on
the selected compatible runtime. Do not apply this floor to older Nest majors or
the existing Node-runner examples, or replace a runner solely because defaults changed.

Consult versioned documentation for existing majors. For 12, specifically assess
new schema-based pipe/serializer APIs, lifecycle ordering and optional-injection
inheritance when affected. Do not extrapolate current documentation or generator
behavior to 10/11. Preserve route, query, null/coercion, response and error contracts
when upgrading; compiler success alone cannot verify them.

## Basis

[Testing](https://docs.nestjs.com/fundamentals/testing),
[Fastify integration](https://docs.nestjs.com/techniques/performance),
[configuration](https://docs.nestjs.com/techniques/configuration),
[authorization](https://docs.nestjs.com/security/authorization) and
[migration](https://docs.nestjs.com/migration-guide) support the relevant mechanisms.
The [research note](../../docs/research/2026-09-21-nestjs-engineering-practices.md)
records executed versions and limits; native instruction delivery is a separate check
from observing how a real agent reads them.
