# Python: modules, construction, and dependencies

Read when changing module ownership, imports, construction, package layout, or
dependencies. Return to the [Python entry](../python.md).

## Cohesive modules

A module may contain several classes and functions. Group declarations when
they serve one use case or small domain concept, belong to the same architectural
layer, have related reasons to change, and expose a clear interface under a
meaningful name. Apply the common size signals; do not hide an independent
component among neighboring declarations. Python does not require one class per
file. Independent services, adapters with different dependencies, and large
entities normally deserve separate modules.

| Cohesive group | Boundary that would make grouping misleading |
| --- | --- |
| Small related request/response types and nested input types for one operation | The operation's transport DTO, ORM mapping, router, and application handler in one file |
| A domain value and its small internal enum; an operation's related exceptions | Unrelated domain concepts collected in a global `models.py` |
| A processor and a private helper type used only by it | Several independently useful adapters with different dependencies |

Use functions for stateless operations; a class needs meaningful state, lifecycle,
or an interface role. Avoid global `utils`, `services`, `schemas`, and `common`
modules that collect unrelated responsibilities. A local `schemas.py` can be
clear when its owning operation is unambiguous. Split growing contracts by
operation or ownership, not arbitrary line ranges.

For a service with business behavior, organize around its actual business
capabilities and use cases. Keep presentation, application coordination, domain
decisions, and infrastructure dependencies distinguishable. These can start as
modules; a small CLI or library does not need a backend directory scaffold.
Preserve an established public namespace when improving internal boundaries.
Create only the components the task needs.

In an independent business core, application/domain imports must not depend on
HTTP frameworks, transport DTOs, or vendor clients. Storage dependencies follow
the project's explicit ORM/domain decision. Put application-required behavioral
ports near their consumers and implement them in adapters; another module's
private storage representation is not its integration contract. Bootstrap owns
assembly and resource lifetime, as described in [execution](execution-resources.md).

## Python forms of useful patterns

Apply the common pattern-selection criteria; none of these rows requires a new
class or dependency. Use the [typing rules](typing-contracts.md) for signatures.

| Decision and useful condition | Idiomatic form | Simpler alternative and cost |
| --- | --- | --- |
| Dependency Injection: a collaborator varies or crosses a boundary | Explicit function/constructor parameters, assembled in bootstrap | A concrete typed argument is often enough; containers and service locators add indirection |
| Strategy: behavior is actually interchangeable | A typed callable for one operation; a narrow `Protocol` for a cohesive stateful or multi-operation contract | Keep a clear branch for one local choice; do not manufacture implementations |
| Factory: construction has rules or coordinated dependencies | A named function, or `@classmethod` when construction belongs to the type and must respect subclass construction | Direct construction for simple data; avoid a parallel factory hierarchy |
| Adapter / Facade: external semantics need translation or a subsystem needs a smaller public surface | A function or focused class returning owned types and errors | Direct use when isolation adds no value; a forwarding wrapper alone is not a boundary |
| Decorator: a real cross-cutting concern repeats | A typed wrapper, preserving the callable signature with `ParamSpec` when necessary | A direct call is clearer for one site; `functools.wraps` preserves metadata, not typing, cancellation, or error semantics by itself |
| Repository / Unit of Work: persistence isolation or one use-case transaction needs an owner | Narrow operations and an explicit transaction lifetime aligned with the existing architecture | Direct queries in a permitted adapter can be sufficient; generic CRUD hierarchies often leak storage and duplicate the ORM |
| Result / optional composition: expected outcomes benefit from explicit data | `T \| None` for real absence; a named tagged union when callers need several non-exceptional outcomes | Normal return/exception flow is the default; a Result/monad library has a vocabulary and interoperability cost |

Prefer composition over inheritance for independent collaborators. Use `ABC`
when nominal membership or a genuine shared implementation is needed; Protocol
supports structural substitution. Neither justifies inheritance solely to reuse
unrelated fragments. Avoid mutable default arguments and module-global service
instances that silently couple tests, requests, or event loops.

## Imports, packaging, and versions

- Inspect `pyproject.toml`, the project's lock/constraints files, supported Python
  range, actual interpreter, CI, and dependency versions. `requires-python` states
  compatibility; it does not select the interpreter. Use the existing environment
  and dependency tool rather than introducing another package manager.
- Keep import-time work predictable. Importing a module should not open sockets,
  start workers, migrate a database, or perform application startup. Put script
  execution behind an entry point or `if __name__ == "__main__"` as appropriate.
- Keep `__init__.py` and re-exports deliberate. Avoid wildcard imports, ambiguous
  names that shadow dependencies, and `sys.path` edits as a packaging workaround.
  Resolve an import cycle by reassessing ownership or a real shared contract;
  move an import locally only for an intentional lazy/optional dependency.
- Use `TYPE_CHECKING` for dependencies needed only by the analyzer. A library
  evaluating annotations at runtime may still need those names; verify its
  supported resolution mechanism rather than assuming postponed annotations fix
  every cycle. See [compatibility](verification.md).
- A `src/` layout helps a distributed package test its installed form and avoid
  accidental imports from the checkout; a flat layout can suit a small tool.
  Do not migrate layout for fashion. If installation or public imports change,
  check the built/installed artifact outside the checkout, entry points, and
  packaged resources. Preserve library exports and `py.typed` when applicable.
- Keep reusable-library dependency ranges distinct from an application's tested
  locked environment. Review intentional dependency changes and generated lock
  diffs; do not refresh dependencies during an unrelated source move.

Sources: [modules](https://docs.python.org/3.11/tutorial/modules.html),
[typing library guidance](https://typing.python.org/en/latest/guides/libraries.html),
[src and flat layouts](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/),
[project metadata](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/).
Boundary and pattern choices above are framework policy and conditional design
defaults, not Python language requirements.
