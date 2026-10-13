# Symfony structure and services

Read when changing application structure, controllers/commands/handlers, service
registration, configuration, or framework extension points. Apply the existing
[PHP structure](../php/structure.md) and [core policy](../core.md). These sections
use Symfony 7.4 as their checked baseline, not as an instruction to upgrade.

## Application boundaries

Preserve the application's coherent structure. Symfony's default directories are
a useful starting point; feature namespaces can help a growing application when
they express real responsibilities. Do not create a bundle for every application
feature. A reusable bundle makes sense for a separately distributed integration
with its own configuration/lifecycle contract. A small component-based script
need not acquire a full FrameworkBundle application.
[Framework best practices](https://symfony.com/doc/7.4/best_practices.html).

HTTP controllers, Console commands, and Messenger handlers are entry adapters:
receive the appropriate input, invoke the application operation, and map its
outcome. Keep calculations, business branching, queries/flush calls and external
operation orchestration behind them. Reuse the existing application operation
from each adapter instead of duplicating its orchestration. A direct call is
sufficient; no bus or universal handler base is required.

Preserve named operation contracts without passing Request, RequestStack,
EntityManager, the container, or serialized arrays into an independent business
core. Transport attributes and serialization groups belong where their coupling
is intended. Do not duplicate identical DTOs only to cross directories. When
Doctrine ORM is used, [domain/Doctrine placement](../doctrine/models-mapping.md#domain-model-placement)
remains a separate architecture choice; a framework convention does not decide it.

An AbstractController is a convenient framework base, not a requirement for a
controller to work. A plain callable service with injected dependencies is enough
when no helper is needed. Prefer direct application calls for a local synchronous
operation; a command bus, event, decorator, or factory needs a concrete dispatch,
cross-cutting behavior, variation, or construction problem.
[Controllers](https://symfony.com/doc/7.4/controller.html).

## Serializer roles and application transformations

Before creating or renaming a transformation class, identify its input/output,
responsibility, and actual caller. Choose the mechanism and name from that role;
an array, DTO, or method named `normalize()` does not establish participation in
Symfony Serializer. Apply this decision to HTTP, CLI, messages, and integrations.

| Actual need | Choose |
| --- | --- |
| Conversion already supported by Serializer | Existing normalizers, metadata, and context; no custom extension by default |
| Custom normalized representation within the Serializer path | `NormalizerInterface`: data to arrays/scalars, with the interface's permitted `ArrayObject`/null cases |
| Custom construction of a requested type within that path | `DenormalizerInterface`: intermediate data to the requested type |
| Conversion to/from an encoded format | Existing Serializer/encoder capabilities, or an explicitly required serialization contract |
| Independent payload parsing, DTO mapping, canonicalization, or acceptance decisions | A cohesive application method or class named for that responsibility |

For a custom Symfony normalizer/denormalizer, implement the installed version's
interface, including its `supports*()` and `getSupportedTypes()` contracts. Register
it in the actual Serializer path: FrameworkBundle uses `serializer.normalizer`
tags, often supplied by autoconfiguration; standalone component use supplies the
instance to Serializer explicitly. Check selection through that path for an
affected integration; a direct unit call alone does not prove discovery or dispatch.
[Custom normalizers](https://symfony.com/doc/7.4/serializer/custom_normalizer.html),
[Serializer](https://symfony.com/doc/7.4/serializer.html).

As a local naming rule in Symfony projects, reserve `*Normalizer` and
`*Denormalizer` for those Serializer roles, or an explicitly identified equivalent
contract in another library. Do not use those suffixes for an ordinary application
processor merely because it cleans up data or returns a DTO. Reserve `*Serializer`
for actual serialization responsibilities; do not use it for an arbitrary
array builder, mapper, or business operation. This is an engineering convention
to prevent ambiguity, not a Symfony prohibition on general normalization terms.

For independent transformations, choose a responsibility-specific name such as
`PayloadParser`, `ResponseMapper`, or `AddressCanonicalizer` only when that is what
the component does. An operation that also decides acceptance or recovery needs
a name expressing that operation, not an automatic `Mapper`/`Validator` replacement.
A small local transformation can remain a descriptive method; do not create a
service, generic processor layer, or forwarding Serializer wrapper just to comply
with a naming pattern. Reuse the injected Serializer directly when sufficient.

Do not add an interface, tag, or Serializer dependency merely to legitimize a
misleading name. Keep business acceptance/recovery decisions, persistence, and
external effects with their application owner; a real Serializer adapter may
delegate to an appropriate conversion collaborator. Representation and type checks
required by a conversion contract remain valid in that adapter, but do not replace
the [executed validation boundary](http-validation.md#request-mapping-is-an-executed-boundary).
When changing an existing class, inspect its callers and behavior before choosing
a rename or separation; preserve public contracts and keep repairs within scope.

The framework contracts above were source-reviewed against Symfony 7.4 on
2026-10-13, including
[NormalizerInterface](https://github.com/symfony/symfony/blob/7.4/src/Symfony/Component/Serializer/Normalizer/NormalizerInterface.php)
and [DenormalizerInterface](https://github.com/symfony/symfony/blob/7.4/src/Symfony/Component/Serializer/Normalizer/DenormalizerInterface.php).
This adds no runtime execution evidence or target-version upgrade.

## Container wiring and lifetime

Use constructor injection and the existing autowiring workflow for services.
Autowiring chooses arguments; autoconfiguration applies supported tags/metadata
from interfaces or attributes. Neither executes validation or proves the business
graph correct. Explicitly select the intended alias/binding when several services
implement one interface, and bind scalar/configuration values deliberately.
[Container](https://symfony.com/doc/7.4/service_container.html),
[autowiring](https://symfony.com/doc/7.4/service_container/autowiring.html).

Keep ordinary services private. Public access for a deliberate entry point or a
test fixture is not a reason to expose the whole graph. Avoid injecting the full
container as a service locator. Existing narrow subscribers/locators can be useful
for a genuinely lazy set of optional dependencies, with explicit consumed types.

Services are shared by default within a container. This does not mean a fresh
instance per request, message, or method call in a persistent process. Stateless
services are simplest; isolate/reset per-job state through the runtime's supported
mechanism when necessary. `shared: false` creates a new instance on retrieval,
but does not continually replace an instance held by a long-lived consumer.
Read [runtime/effects](runtime-effects.md) for workers and resource ownership.

Use supported tags/attributes for controllers, commands, listeners, and handlers;
their class existing in `src/` is not proof that discovery registered it. Keep
service imports/exclusions deliberate so DTOs, domain objects, and entities are
not accidentally treated as autowired services. After a move, check route imports,
service IDs/aliases/tags and string references as well as PSR-4 paths.

## Configuration and extension cost

Keep environment-dependent connection settings and secrets in the established
configuration/secret workflow. Resolve them at composition; do not read ambient
environment variables throughout business methods. Configuration parameters,
typed options, and a small factory are usually simpler than a new bundle extension
or compiler pass. Use a compiler pass for a real compile-time graph change, not
for ordinary application initialization or network work.

Attributes, YAML, and PHP configuration have different tradeoffs; retain the
project's supported format. Flex recipes can create or change configuration and
`symfony.lock` records recipe state; it does not replace `composer.lock`.
Review recipe/configuration changes during upgrades and use the project's
Composer script/plugin policy. Generators are starting points whose output still
needs contract, dependency and security review.
[Flex](https://symfony.com/doc/7.4/setup/flex.html).
