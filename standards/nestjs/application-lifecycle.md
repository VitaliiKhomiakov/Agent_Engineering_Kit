# NestJS application work and lifecycle

Read for use cases, persistence, transactions, external effects, startup or shutdown.
[Node lifecycle](../nodejs/lifecycle-verification.md) owns host-level cancellation
and process limits; this section adds Nest assembly/hook constraints.

## Business core and assembly

- An application service coordinates the use case. The domain model or a focused
  policy protects rules according to the project's architecture. An ORM entity is
  not automatically a rich model or API DTO.
- When TypeORM is present, follow its [model rules](../typeorm/models-mapping.md)
  and [Nest integration](../typeorm/nestjs-integration.md): use business intent
  methods for coupled updates, not generated setters or DTO-to-entity assignment.
- Providers receive dependencies through Nest DI. Do not instantiate a managed
  service with `new` inside a controller, bypassing container configuration and scope.
- Pure types and functions do not require Nest decorators. If the business core
  is independent of Nest, connect it through suitable providers and factories.
- Do not add CQRS, an event bus, or a separate handler for every line of CRUD
  without use-case requirements and an accepted architecture.

## State, transactions and effects

Validation establishes a command's representation, not whether current state
permits it. Keep invariant checks with their owner and enforce them through HTTP,
CLI and worker entry points. Preserve authorization and durable database constraints
when concurrent writers exist. A singleton provider or process-local lock cannot
protect other replicas' writes; use the actual transaction/isolation/version protocol.

Own transaction and leased connection/session in the application operation and
adapter. Parameterize queries and map records to explicit results. Check that every
transactional query uses the intended manager/connection; a root repository call
may escape a transaction started elsewhere. An ORM decorator or Nest injection
alone establishes none of these guarantees. Database-specific practice belongs to
its own profile; do not add a repository per entity solely to imitate a diagram.

Return or await required promises with defined completion and error ownership. For
an observable, return it to a Nest boundary that subscribes, or own its subscription
or conversion to a promise, including completion and errors. Awaiting an observable
itself does not subscribe to it. Multiple subscriptions to a cold observable can
repeat external effects.
An RxJS timeout/unsubscribe does not automatically cancel an arbitrary promise or
roll back a write; propagate an adapter-supported signal and define unknown outcomes.
Keep retries bounded and consistent with idempotency and transaction semantics.

Queue consumers validate input, coordinate their operation and acknowledge only
according to the actual durability contract. Retries/redelivery may repeat a job;
job IDs alone are not proof that a downstream effect occurs exactly once. In-process
events are not a durable handoff. Use the existing queue/outbox mechanism only where
the requirement warrants it, and avoid starting unowned work from a decorator hook.

## Startup and teardown ownership

Await required async provider construction before declaring readiness. Validate
configuration at assembly with its accepted mechanism; loading ConfigModule or
generically typing ConfigService is not sufficient evidence that all values were
validated. A factory that acquires resources then fails owns its partial cleanup;
application creation failing does not prove all acquired clients were released.

Use lifecycle hooks on the component that actually owns a shared resource. Explicit
`app.close()` invokes the application shutdown lifecycle; OS-signal handling requires
`enableShutdownHooks()` and a suitable executable environment. Request-scoped classes
do not receive these application lifecycle hooks, so do not entrust their connection
cleanup to `onModuleDestroy`.

Distinguish stop-admission/drain, resource release and final reporting. Framework
hook phases and ordering are version-sensitive; Nest 12 changes ordering by component
hierarchy. Verify required dependency ordering in the actual graph, and keep coupled
cleanup steps under one owner when their sequence must be guaranteed. Do not assume
closing the app waits for every detached task or that a hook cancels every driver call.
Await asynchronous release and surface failure; each cleanup method should preserve
its intended repeat/cancellation semantics. External termination still needs a budget.

The [provider lifecycle example](examples/provider-lifecycle.md) demonstrates an
async provider, alias/export identity and awaited release without an HTTP application.
It does not prove real database disposal, signal handling or a global hook-order rule.

## Basis

[Custom providers](https://docs.nestjs.com/fundamentals/custom-providers),
[lifecycle hooks](https://docs.nestjs.com/fundamentals/lifecycle-events),
[configuration](https://docs.nestjs.com/techniques/configuration),
[database integration](https://docs.nestjs.com/techniques/database),
[queues](https://docs.nestjs.com/techniques/queues) and
[migration notes](https://docs.nestjs.com/migration-guide) describe Nest integration
points. Domain boundaries, transaction ownership and durable effects are project policy.
