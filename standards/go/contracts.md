# Go: types, domain contracts, and errors

Read when changing public types, state transitions, validation, receivers, or error behavior. Return to the [Go entry](../go-gin.md).

## Types, state, and construction

- Use concrete types for known contracts. Distinguish absence, a zero value, and
  an empty value when the operation needs that distinction. A pointer is one
  representation of presence, not an instruction to make every field nullable.
- Prefer useful zero values where their meaning is valid. Use a named constructor
  when it establishes a valid initial state or assembles required dependencies;
  a simple literal is sufficient for plain data without those requirements.
- Choose receivers according to mutation, identity, and copying semantics. A
  value receiver does not make referenced slices or maps immutable. Do not copy
  an in-use lock; document who may mutate shared data or retain a returned slice.
- Unexported fields restrict access across packages, not between files or types
  in the same package. Domain methods need a coherent package boundary as well
  as an agreed persistence/concurrency contract.
- Return an actual `nil` on success when the result type is `error`. A typed nil
  pointer placed inside an interface is not a nil interface.
- Default to interfaces for a needed behavioral contract and type parameters
  for a real algorithm or container shared across types. Preserve concrete
  types when neither solves a current problem. Check version support before
  introducing generic syntax; avoid both blanket generics bans and generic
  replacements for an already sufficient interface.

The [language specification](https://go.dev/ref/spec),
[nil-error FAQ](https://go.dev/doc/faq#nil_error), and
[generics guidance](https://go.dev/blog/when-generics) support these distinctions.

## Domain rules and boundary validation

Validate external shape and presence at the boundary. Keep rules about a domain
object's valid transitions with that object; coordinate authorization, other
objects, persistence, and external effects in the use case. Rechecking a domain
invariant on a non-HTTP entry path is not redundant transport validation.

The [publication example](examples/domain.md) shows an incomplete draft, a
permitted transition, and rejection without state mutation.

## Dependencies and errors

Expected operational failures use errors. Choose sentinel or typed errors when
callers need that stable distinction; use `errors.Is`/`errors.As` with wrapped
errors. Do not parse error strings. Add useful operation context without logging
the same failure at every layer. Treat wrapping with `%w` as a decision to expose
the cause; map infrastructure errors where the package promises another contract.
Use panic only for cases where the package contract justifies it, not ordinary
invalid input or a failed external request.

The [dependency and strategy example](examples/dependencies.md) demonstrates
consumer-owned behavior, an ordinary function strategy, and a preserved error
cause. See [Go error wrapping](https://go.dev/blog/go1.13-errors).
