# Python: typing, validation, state, and errors

Read when changing public signatures, data contracts, external input, domain
state, or error behavior. Return to the [Python entry](../python.md).

## Strict static contracts

- Annotate parameters, returns, and model fields, including `__init__ -> None`,
  callbacks, and async functions. Precise local inference is appropriate. The
  policy includes tests and doubles; CI must run the agreed static analyzer.
- Do not introduce `Any`, `dict[str, Any]`, bare containers, untyped functions,
  or bypasses through `cast`, `# type: ignore`, untyped decorators, or dynamic
  `getattr`. These are framework restrictions, not a claim that Python forbids
  dynamic programming. Isolate an untyped dependency with a precise adapter or
  stub rather than spreading its unknown types into business code.
- Accept genuinely unknown external values as `object`, validate/narrow them,
  and return a concrete contract. An annotation on a dynamic result is not
  validation. Do not use `object` to erase a contract already known to the caller.
- Name boundary data with a dataclass, enum, typed model, or a `TypedDict` when
  the interface really is a mapping. Typed collections and domain maps are valid;
  avoid undocumented key sets standing in for a named result.
- Accept `Mapping`, `Sequence`, or `Iterable` when their weaker contract suffices;
  use mutable/container-specific types when the operation needs those guarantees.
  An iterable may be consumable only once; a read-only view can still reflect
  mutation by its owner. Copy when the contract needs a stable snapshot.
- Define narrow behavioral ports with `Protocol`. A function can satisfy a
  callable contract; an implementation need not inherit from a Protocol. Use
  `ABC` for nominal/shared behavior. Do not add an interface for each private type.

Use one agreed analyzer with a pinned version and command. For mypy the baseline
is `strict = true`, `disallow_any_explicit = true`, and
`disallow_any_unimported = true`. `strict` does not reject every dynamic expression;
use `disallow_any_expr = true` in business modules where applicable, and record
the checked scope and remaining limits. Verify flags in the installed version;
another analyzer must enforce the policy, not merely offer a similar setting.
Adopting legacy checks is a separate phase, not permission for global suppression
or a wholesale rewrite during a small fix. New and modified contracts add no `Any`.

## Runtime input and domain state

Annotations, `TypedDict`, `NewType`, and ordinary dataclass construction do not
validate external data. Even `@runtime_checkable` Protocol checks attribute
presence rather than method signatures or payload meaning. A parser/validator
must enforce the actual accepted input, including missing versus `None`, false
versus absent, coercions, ranges, and unknown fields when relevant. For integer
inputs, remember that `bool` is a subclass of `int`; an integer-only wire contract
may need to reject it explicitly. Do not implement another validation framework
for a small boundary; use the project's existing compatible validator.

Transport shape rules and state-dependent business rules have different owners.
A draft may be incomplete; its publication method can still require a title and
reject repeated publication from HTTP, CLI, or a worker. Validate all required
conditions before changing state or performing effects. Ordinary typed internal
calls need not repeat external shape checks, but they must preserve invariants.
Use explicit exceptions for required runtime checks; `assert` is removable under
optimization and is not input validation or authorization.

Dataclasses suit data and value objects; generated methods do not make an object
a domain model. `__post_init__` can enforce a construction invariant but cannot
protect later arbitrary mutation. For stateful behavior, expose intent methods
and read-only views instead of public setters or mutable internals. Python's
underscore convention and properties guide clients; they are not a security
boundary. `frozen=True` blocks ordinary field reassignment but does not freeze a
nested list or establish thread safety. Choose owned immutable contents or
defensive copies when required; use `field(default_factory=...)` for per-instance
mutable defaults. Do not add rich entities to simple read results.

The optional [draft and publication example](examples/domain.md) separates a
small input parser from the domain owner and shows valid incomplete drafts.
It uses no Pydantic/FastAPI-specific behavior.

## Error contracts

- Return `None` when absence is an agreed normal result. Use a specific exception
  for a failed operation; a small tagged result is optional when callers routinely
  handle several expected outcomes as data. Avoid sentinel strings and silently
  successful fallback values.
- Catch the specific failure at the boundary that can recover or translate it.
  Keep the protected `try` region narrow. Translate an SDK/storage error to the
  owned contract and preserve causality with `raise OwnedError(...) from exc`.
  Do not classify failures by parsing their human-readable message.
- Subclass `Exception` for application errors. Broad catches belong at deliberate
  reporting/cleanup boundaries; do not catch `BaseException` to convert process
  exits or cancellation into success. Log a failure with suitable context at its
  owner, and map public errors without leaking payloads, credentials, or internals.
- If concurrency introduces `ExceptionGroup`, decide where grouped failures are
  part of the contract and where specific members are handled with `except*`.
  Do not select the first exception and silently discard the rest. Preserve
  cancellation as described in [execution](execution-resources.md).

Sources: [typing](https://docs.python.org/3.11/library/typing.html),
[dataclasses](https://docs.python.org/3.11/library/dataclasses.html),
[exceptions](https://docs.python.org/3.11/tutorial/errors.html),
[mypy flags](https://mypy.readthedocs.io/en/stable/command_line.html).
Strictness and ownership are framework policy; static typing's runtime limits
come from Python's contracts.
