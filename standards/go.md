# Go

Apply to Go work with the [common rules](core.md). Read only the relevant
sections; examples and research are optional, not a recursive reading queue.
Gin has its own profile and is selected only where used.

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

Availability in a bundle does not imply mandatory reading. Stop once the task
requirements are known; follow examples only to resolve a current decision.

## Evidence

[Go research](../docs/research/2026-09-21-go-engineering-practices.md) records
primary evidence, versions and alternatives checked on 2026-09-21.
The [practice plan](../docs/plans/2026-09-21-engineering-practices.md) records
example and delivery checks.
