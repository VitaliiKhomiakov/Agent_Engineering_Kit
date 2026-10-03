# NestJS modules and providers

Read for feature boundaries, module exports, provider tokens/factories, scopes or
cycles. Use [application/lifecycle](application-lifecycle.md) when assembly changes
resource ownership. The [provider example](examples/provider-lifecycle.md) is optional.

## Feature modules and components

- Group related capabilities into domain-focused Nest modules such as orders. Do
  not organize the entire application solely into global controllers/services/dto folders.
- `@Module()` describes assembly: controllers, providers, imports, and required
  exports. Export only the module's public capabilities.
- Do not use another module's internal ORM models as its API. Do not make every
  provider global to bypass dependencies.
- Put each independent controller, provider, repository adapter, and module in a
  separate file. Small nested DTOs for one operation may share a DTO file; the
  common cohesion and size criteria still apply.
- As a service grows, split it into independent use cases or responsibilities.
  An `OrdersService` containing everything about orders is not cohesive merely
  because its content shares a noun.
- Treat a dependency cycle first as evidence of a misplaced boundary. Do not add
  `forwardRef` or a general global module by default.

## Tokens and construction

A TypeScript interface is erased and cannot itself be an injection token. Define
an explicit class, symbol or accepted string token where the runtime needs one;
keep a named interface for the consumer's capability. Use `@Inject(token)` or a
factory with an explicit `inject` list. `useFactory` can connect a pure use case to
an adapter without decorating the business class. An async factory's resolution
can establish readiness before its consumer is constructed; the factory must
release partial acquisitions if it fails.

Use `useExisting` for an alias to an existing managed instance. `useClass` registers
construction for that token and can create a second instance if the class is also
provided separately. Duplicating a provider in feature modules can duplicate its
state/client. Import the owning module and export the needed capability instead.
Do not use `ModuleRef` as a general service locator to hide dependencies.

A static module is enough for fixed wiring. Dynamic modules or configurable-module
builders are optional for reusable configurable integrations with actual consumers;
keep their options, token identity and exports explicit. `@Global` changes visibility,
not architectural ownership. A barrel/file cycle differs from a DI cycle; first
inspect import/value references and ownership. `forwardRef` is a deliberate escape
for a real supported cycle, not automatic repair or a reason to ignore initialization.

## Scope follows state lifetime

Default singleton providers usually fit stateless use cases and reusable clients.
They must not store the current request/user/transaction as mutable instance state.
Request-scoped providers are recreated for their context and can make dependent
controllers/providers request scoped too. Transient scope gives a consumer its own
instance; it is not a fresh object for every method call. Verify the graph, not just
one decorator, when changing scope.

Choose request scope only for a concrete per-context dependency. Passing explicit
operation data is simpler for many cases; existing AsyncLocalStorage context may
suit correlation without a new provider scope. Request scope is not database
transaction isolation, authorization, cancellation or automatic client disposal.
Some long-lived integrations require singleton components; follow that adapter's
contract. Do not add a tenant cache/durable context without bounded ownership.

## Basis

[Modules](https://docs.nestjs.com/modules),
[custom providers](https://docs.nestjs.com/fundamentals/custom-providers),
[asynchronous providers](https://docs.nestjs.com/fundamentals/async-providers),
[injection scopes](https://docs.nestjs.com/fundamentals/injection-scopes) and
[circular dependencies](https://docs.nestjs.com/fundamentals/circular-dependency)
explain Nest's container. Cohesion, limited exports and explicit dependencies are
our project requirements; a reusable DI mechanism is not a mandatory architecture.
