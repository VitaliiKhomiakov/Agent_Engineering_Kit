# Go: architecture and patterns

Read when changing packages, dependency structure, construction, or module/toolchain requirements. Return to the [Go entry](../go.md).

## Versions and modules

- Check `go.mod`, relevant `go.work` and `toolchain` directives, the actual
  toolchain/CI, and dependency versions. A manifest is not evidence of the
  installed compiler. Account for automatic toolchain selection before running
  commands in an environment where downloads or upgrades are restricted.
- Keep changes compatible with the project's supported language and library
  versions. Verify newer APIs and syntax in the relevant release documentation;
  do not silently raise the minimum version to simplify an example.
- Scope dependency updates deliberately. Review changes to `go.mod` and `go.sum`,
  including those from `go mod tidy`; preserve reproducibility and required CI
  checks. Language-practice adoption does not authorize a dependency refresh.

See [toolchain selection](https://go.dev/doc/toolchain) and
[dependency management](https://go.dev/doc/modules/managing-dependencies).

## Packages and files

Apply [responsibility placement](../core.md#responsibility-placement-before-implementation)
before adding or changing code; these are its Go-specific boundary choices.

- The package is the primary boundary for organization and public access. Group
  files within a package by cohesive responsibility or operation, not by a “one
  struct per file” rule.
- A file may contain a struct with its methods, a constructor, small related
  types, and private helpers. Place already independent handlers and adapters in
  separate cohesive files from the outset; file size is not the prerequisite.
- Apply the common size signals to files and functions. For a struct with methods,
  consider its aggregate behavior: distributing methods across files does not
  fix an overly broad type responsibility.
- Name a package for its purpose. Do not collect unrelated code in global
  `utils`, `common`, `types`, `interfaces`, or a universal `manager`.
- Splitting a file and extracting a package are different decisions. Another file
  in the same package is sufficient when only organization needs to change. Create
  a package when a distinct dependency or access boundary is needed, accounting for
  import direction. Do not resolve import cycles by moving everything into a
  common package.
- Private server application implementations may live under `internal`. Do not
  create a directory or module for every small type.
- Default to concrete, cohesive packages. Keep entry-point assembly thin and
  construct infrastructure at the application boundary. Introduce an application
  or domain boundary when business behavior needs one; a small tool does not
  need a mandatory layered directory tree.

## Business modules and internal layers

For applications with substantial business functionality, prefer organizing code
by cohesive business capability, with internal layers or adapter packages where
their responsibilities warrant separation. This is an engineering default, not
a Go requirement or a fixed directory template. Preserve an established project
structure unless the task authorizes changing it.

- Choose module boundaries from related operations, rules, and data ownership.
  An entity or database table does not automatically define a module; ordering,
  for example, may own orders, line items, and cancellation rules together.
  A business module here is a group of responsibilities/packages, not necessarily
  a separate `go.mod`, repository, process, or microservice. Full DDD is optional.
- Within a complex module, distinguish domain rules, application use cases,
  transport adapters, and persistence/integration adapters. Apply the
  [shared responsibility rules](../core.md#responsibilities-and-data); separate
  packages only where these roles need distinct dependency or access boundaries.
  A simpler module can retain a few cohesive files without matching its peers'
  directory tree.
- Let additional nesting express a real boundary, such as another transport,
  storage implementation, or independently owned business capability. File count
  alone is not a reason for a package per operation, entity, DTO, or interface.
  There is no required nesting depth or prescribed set of directory names.
- Keep business behavior independent of transport packages and concrete storage
  implementations where those boundaries are introduced. Adapters implement the
  needed contracts; entry-point assembly connects concrete dependencies.
  Other modules use the intended business API rather than another module's
  storage implementation. Avoid a universal service that coordinates every domain.
- Review imports as well as directory placement. Directory nesting does not make
  one Go package private to another; a top-level `internal` does not isolate
  sibling business modules from each other. Choose explicit APIs and allowed
  dependencies, and avoid import cycles.
- Keep shared technical facilities, such as connection setup and observability,
  free of module-specific business rules. Queries, policies, and adapters for a
  business capability stay with that capability unless actual shared ownership
  justifies extraction.

## Boundary models and DTO placement

Apply [shared model separation](../core.md#responsibilities-and-data) and
[Go domain contracts](contracts.md#domain-rules-and-boundary-validation).
Placement follows the contract's owner:

- Transport request/response DTOs and their conversions belong to the relevant
  module's transport adapter; avoid a project-wide DTO package by default.
- Use-case inputs/results belong with the application operation. Domain types
  belong with their rules. Storage-specific records and mappings belong with the
  persistence adapter, when a separate representation is needed.
- Split representations when meaning, lifecycle, exposure, or dependencies
  differ. Do not generate identical models and mappers merely to cross folders,
  or require a dedicated DTO subpackage when local files suffice.
- Keep tests near the package or operation they cover; use a separate integration
  test area only when its scope or fixtures justify it.

## Patterns in Go

Apply the common selection criteria. These are available forms, not a checklist
of structures to add to every package.

| Practice | Simple Go form and useful condition | Simpler alternative or cost |
| --- | --- | --- |
| Dependency Injection | Function/constructor arguments; assemble a DB, clock, or external client once where its lifetime is owned | A concrete argument is enough; no container or interface for every struct |
| Strategy | A function for one replaceable operation; a small interface for a cohesive multi-operation or stateful contract | Keep a local branch when it fully expresses the current variation |
| Adapter | A function, function type, or struct that translates an actual external contract | Direct use is sufficient when no semantic translation or isolation is needed |
| Decorator / Middleware | Wrap a function or interface for a cross-cutting concern at a real boundary | A local call is simpler for one site; wrappers must preserve cancellation, errors, and required capabilities |
| Repository | A consumer-oriented persistence contract for domain operations with meaningful storage isolation | Direct `database/sql` in a focused adapter can suffice; avoid a generic CRUD interface per table |
| Factory | A constructor function; a factory object only for creation with its own dependencies or selection rules | Use literals/zero values for simple data; a factory should not hide a service locator |
| Facade | A small API that gives consumers a coherent operation across an existing subsystem | Call a dependency directly if a wrapper would only rename it |
| Monadic composition | An existing typed composition abstraction when a substantial pipeline benefits from its semantics | Default to `(T, error)` or `(T, bool)` and ordinary branches; account for ordering, debugging, and dependency cost |

Put small interfaces near the consumer that needs them. Return a concrete type
by default when callers do not need an abstract result. Do not copy class
hierarchies from another language. Functions without state can remain functions.
The [Go review guidance](https://go.dev/wiki/CodeReviewComments#interfaces) and
the original [Repository description](https://martinfowler.com/eaaCatalog/repository.html)
inform this policy; they do not mandate a pattern-based architecture.

## Basis

- [Go: Package names](https://go.dev/blog/package-names) explains purpose-driven
  package names and the problems with general packages lacking a clear responsibility.
- [Go: Organizing a module](https://go.dev/doc/modules/layout) describes packages,
  `internal`, and application layout options; there is no single layout for every server.
- [Effective Go](https://go.dev/doc/effective_go) demonstrates Go approaches to
  construction and interfaces, including function adapters. It is historical
  guidance; consult current specifications and release notes for newer features.

The business-module recommendation is local policy informed by source review on
2026-10-13 of [Ardan Labs packaging](https://www.ardanlabs.com/blog/2017/02/design-philosophy-on-packaging.html)
and [Grafana's package guidance](https://github.com/grafana/grafana/blob/main/contribute/backend/package-hierarchy.md).
These are architectural references, not mandatory layouts or executed runtime
checks. Their company-specific conventions need not be adopted together.
