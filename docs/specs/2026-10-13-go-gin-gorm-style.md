# Go, Gin, GORM, and code readability specification

Date: 2026-10-13. Status: prepared for user review; implementation is not started.
Progress and execution evidence belong to the
[canonical plan](../plans/2026-10-13-go-gin-gorm-style.md).

## Outcome and scope

Extend this instruction library so agents produce readable, idiomatic Go, organize
Gin features with explicit dependencies, and use GORM safely when it is actually
present. Supply formatting/lint guidance and bounded reproducible examples.
The deliverable is library guidance, not an application scaffold or an adoption
into a consuming project. This stage prepares the specification and plan.

The user's input is the 472-line file
`/home/vitalii/Documents/Local_Projects/go-gin-architecture-guidelines-v2.md`,
SHA-256 `5f8ef568db273948ecbc01de72d770fcd426a244eb9ea85834bc320900ef199c`.
It was reviewed on 2026-10-13 alongside the preceding request for human-readable
code, `gofmt`/`goimports`, and a small explicit `golangci-lint` configuration.
The source remains unchanged. This specification records the resulting decisions
so subsequent work does not depend on access to that author-machine path.

## Global constraints

- Work in the current checkout; no staging, commits, branches, or worktrees.
- Instructions, specifications, plans, and example explanations use English.
- Preserve supported target versions, public contracts, and unrelated edits.
- Apply new conventions to new or meaningfully changed code; no blanket rewrite.
- Keep one authoritative owner per rule and conditional read-by-task routes.
- GORM is optional; Go, Gin, and the legacy go-gin aggregate must not require it.
- Examples and tool configurations remain inactive until explicitly adopted.
- Historical evidence retains its original date, versions, and executed scope.
- Run checks proportionate to changed artifacts and behavior; retain project gates.

No new root Go module, application dependencies, CI workflow, model setup, or
automatic installation is part of this change. Existing public names and HTTP
statuses are not renamed merely to match an illustrative convention.

## Existing owners and gaps

At baseline `37202a4029fd3870273c24dc26499e38dd3a500a`, the Go entry already requires
`gofmt`. Go architecture already covers concrete dependencies, consumer-owned
interfaces, useful package boundaries, and conditional patterns. Gin already
covers binding, context lifetime, route registration, middleware, and responses.
There is no dedicated Go style topic, reproducible lint configuration, or GORM
profile. Most middleware guidance should be extended in place, not duplicated.

The shared [core](../../standards/core.md) remains the owner of responsibility,
simple control flow, names, and size/cohesion policy. The shared
[verification policy](../../standards/verification.md) retains check selection.
Existing [Go contracts](../../standards/go/contracts.md),
[resource rules](../../standards/go/resources.md), and
[Gin middleware rules](../../standards/gin/routing-middleware.md) retain their
respective semantic contracts.

## Input reconciliation

Section numbers below refer to the supplied v2 document. Adopt means the rule is
accepted with the scope and corrections specified here; it does not mean deployed.

| Input | Disposition and authoritative destination |
| --- | --- |
| Goal; sections 1 and 6: Handler and optional Service | Adopt in `standards/gin/handlers-binding.md`; CRUD may call a concrete Store directly |
| Section 2: Store and consumer interfaces | Extend `standards/go/architecture.md`; GORM-specific usage belongs in its new profile |
| Section 3: feature-first layout and routes | Adopt as an HTTP application default in `standards/gin/architecture.md`, not a universal Go layout |
| Section 4.1: concrete GORM Store | Adopt in `standards/gorm/stores-models.md`; no compulsory Repository wrapper |
| Sections 4.2-4.4: lifetime, errors, queries, writes | Adopt with API/driver caveats in `standards/gorm/queries-lifetime.md` and `stores-models.md` |
| Sections 4.5-4.6: transactions and migrations | Adopt in `standards/gorm/transactions-migrations.md` |
| Section 5: middleware placement and behavior | Extend existing Gin middleware/runtime owners; placement belongs in Gin architecture |
| Section 7: composition and packages | Reuse Go architecture; correct the explanation of `internal` |
| Section 8: idioms and error handling | Reuse Go contracts and Gin handlers; add Go-specific style details only |
| Section 9: testing | Extend Go/Gin verification and add GORM verification; replace unconditional full-stack commands with relevant checks |
| Sections 10-11: incremental adoption and agent work | Preserve shared delivery/verification ownership; use technical prompts in the affected topics, not a second workflow |
| Section 12: readiness | Translate into the acceptance criteria below |
| Section 13: source status | Keep vendor contracts distinct from local architectural choices |
| Conversation: formatting and readability | Add `standards/go/style.md` and `standards/go/examples/style-tooling.md` |

## R1: Go formatting and readability

`standards/go/style.md` owns the following Go-specific conventions. Entry files
route to it instead of repeating a style guide. Gin and GORM inherit it via Go.

- The required format is `gofmt`-compatible output. Recommend `goimports` for
  format-on-save and import maintenance; its output must be reproducible in CI.
- Group standard-library imports first, followed by other imports. A separate
  project-local group is optional and requires an explicitly configured module
  prefix. Avoid dot imports and unnecessary aliases; preserve justified exceptions.
- Use Go capitalization and initialisms: `userID`, `HTTPClient`, `URL`.
  Names reflect purpose and scope; `i`, `err`, `ctx`, and short consistent receivers
  remain appropriate when immediately understandable. Avoid package-name stutter.
- Use Go guard clauses for failures and keep the normal path easy to scan.
  Link shared control-flow rules; do not introduce another nesting quota.
- Separate meaningful steps with blank lines, keep related statements together,
  and split unwieldy calls/literals or name complex predicates when that helps.
  No new fixed line-length gate, mandatory blank line after every statement, or
  automatic extraction solely to satisfy a line count.
- Document exported declarations and non-obvious contracts. Declaration comments
  identify the declaration; implementation comments explain reasons, constraints,
  or invariants. Avoid comments that merely repeat the statement beneath them.
- Error strings normally start lowercase and omit terminal punctuation, with
  proper-name/acronym exceptions. Error wrapping and classification remain owned
  by Go contracts, not the formatting tool.
- Keep related declarations together. Do not mandate one type per file, a global
  declaration ordering scheme, or a new hard function/file-size limit. Route to
  existing package and size/cohesion owners.
- Preserve wire names, generated/vendor code, and intentionally stable APIs.
  A style fix must not silently change a JSON field, error contract, or exported API.

The base is [Go Code Review Comments](https://go.dev/wiki/CodeReviewComments) and
[gofmt guidance](https://go.dev/doc/effective_go#formatting), complemented by the
local readability choices above. Effective Go is historical core-language
guidance, not a complete account of modern Go features.

## R2: Tooling and enforcement

`standards/go/verification.md` owns adoption and check behavior. A complete
inactive example in `standards/go/examples/style-tooling.md` owns the concrete
configuration, fixture, commands, and version pins.

The proposed new-project baseline uses golangci-lint v2 configuration with
`version: "2"`, `linters.default: none`, and explicit `govet`, `staticcheck`,
`errcheck`, `unused`, and `revive`. Configure revive with only `var-naming`,
`receiver-naming`, `exported`, `error-strings`, and `indent-error-flow`; disable
implicit/default and all-rule expansion. Review overlapping diagnostics from the
pinned Staticcheck version and select one owner for duplicate style diagnostics.
Keep correctness checks enabled. Do not enable every available linter.

Choose `goimports` under v2 formatters. Formatting and lint checks are separate:
`golangci-lint run` is not proof that formatting passed. Document an editing
command and a non-mutating CI gate that fails on differences and on tool errors;
merely running a listing command successfully is insufficient. No additional
formatter such as gofumpt or forced line-length linter is part of this baseline.

Pin the Go toolchain and compatible golangci-lint binary/build version for the
fixture; record the bundled formatter/analyzer versions. If standalone goimports
is used, pin its `golang.org/x/tools` version too. Never use floating `latest` in
reproduction instructions. These pins describe the fixture, not an upgrade rule
for existing projects. Validate configuration using the pinned binary.

For existing repositories, inspect actual formatter, lint configuration, module
roots, build tags, and CI first. Retain compatible working conventions; a v1-to-v2
lint migration is explicit work. Apply checks to the relevant packages/files
while retaining mandatory CI. Generated/vendor exclusions must be deliberate.
Any existing-debt baseline or suppression must have a narrow scope and reason;
do not silently disable checks or reformat the whole repository.

Sources: [goimports](https://pkg.go.dev/golang.org/x/tools/cmd/goimports),
[v2 configuration](https://golangci-lint.run/docs/configuration/file/),
[formatters](https://golangci-lint.run/docs/formatters/),
[revive settings](https://golangci-lint.run/docs/linters/configuration/#revive), and
[toolchain compatibility](https://golangci-lint.run/docs/welcome/faq/).

## R3: Feature organization and explicit dependencies

For new or substantially changed Gin features, prefer a cohesive package such
as `internal/user`, containing the needed handler, routes, Store, DTOs, and tests.
Add Service/UseCase only for independent business rules or orchestration. The
simple flow is Handler to Store; the richer flow is Handler to Service to Store.
Neither flow requires a layer for each noun or an interface for each type.

Keep the Go architecture owner generic: sqlc-generated Queries, database/sql,
pgx, and existing adapters remain valid. Store is a naming preference for new
persistence components, not a reason to rename an existing Repository.
Consumer-owned interfaces require a real behavioral seam; testing a meaningful
boundary may justify one, while a mechanical mirror of every Store method does not.

Composition initializes dependencies and injects them before route registration.
Registration attaches prepared handlers to a parent-selected route group and
does not open a database. Entry points remain small. Cross-feature business
scenarios use a cohesive operation owner and needed contracts; a handler must not
reach into another feature's persistence internals.

`internal/platform` is an optional infrastructure convention. Place generic HTTP
middleware there and feature authentication adapters with their feature, or keep
an existing coherent layout. The router composition package may import feature
constructors; generic infrastructure and middleware must not depend on feature
Stores. Do not manufacture subpackages or public `pkg/` directories in advance.

Correct the source shorthand: Go's `internal` rule limits importers to the tree
rooted at the parent of the `internal` directory; it is not simply a prohibition
on imports from other modules. Ordinary package files share a package, with
Go's external `_test` package convention as a valid testing exception.
See [module layout](https://go.dev/doc/modules/layout) and
[Go command documentation](https://pkg.go.dev/cmd/go).

## R4: Optional GORM profile

Add `gorm`, dependent on `go` only, selected by declared or actual GORM usage.
GORM does not imply Gin, PostgreSQL, Docker, or a change of ORM. The entry routes
to four topics and one example; no GORM detail is copied into generic Go rules.

### Stores, models, and writes

Use a concrete Store around an injected root `*gorm.DB`. Separate HTTP/persistence
models when visibility, meaning, or lifecycle differ; do not create duplicate
domain models for ordinary CRUD without a reason. Whitelist writable fields and
public response fields; never bind untrusted JSON directly into privileged state.
`gorm.Model` is optional. Hooks may protect suitable model-local concerns, but
must not conceal cross-feature business orchestration.

Traditional `Updates(struct)` omits zero values by default. Use explicit selected
fields or maps when zero is an intended update, preserving omission/null semantics
from the transport contract. Do not use `Save` as an automatic generic persistence
operation; its update/create behavior needs an intentional contract.
See [updates](https://gorm.io/docs/update.html).

### Queries, errors, and lifetime

Initialize and own pools at application startup, close them during controlled
shutdown, and derive each operation with its request context. Reuse the root
handle or an intentionally safe session; do not keep mutable query-chain state
in a shared Store. Traditional and generics APIs have different calling forms;
generics availability from v1.30.0 does not mandate a migration.

Check `.Error` and meaningful row counts. `First`/`Take`/`Last` not-found behavior
must not be generalized to all queries/deletes. `TranslateError` additionally
depends on dialect support; otherwise interpret documented driver errors. A zero
update count alone is not a portable proof of absence: verify the operation and
driver's affected-row semantics before mapping it to an application error.

Parameterize values and allowlist dynamic SQL identifiers. Bound collections and
pagination; select needed fields and load associations deliberately to avoid N+1.
Keep slow-query diagnostics useful and sensitive values out of logs. Raw SQL is
allowed when it expresses the operation more clearly.
Sources: [chaining](https://gorm.io/docs/method_chaining.html),
[context](https://gorm.io/docs/context.html),
[errors](https://gorm.io/docs/error_handling.html),
[security](https://gorm.io/docs/security.html), and
[v1.30.0 translation configuration](https://github.com/go-gorm/gorm/blob/v1.30.0/gorm.go).

### Transactions and migrations

A Store may own one cohesive atomic operation. A use case coordinating several
Stores owns their shared transaction through a small explicit runner only when
needed. Every participating operation uses its transaction-bound handle. Do not
store a transaction in context values or share it across unrelated requests.

Check the returned transaction error, including commit failure. Callback success
requests commit; it does not guarantee persistence. Database rollback does not
restore Go object fields populated during attempted writes. Keep transactions
short and keep slow remote calls outside them. Outbox is conditional on an actual
delivery contract, not a mandatory subsystem.

Retain default write transactions unless a measured, reviewed change justifies
otherwise. AutoMigrate may support prototypes/disposable fixtures. Production
schema changes use the project's versioned migration process with recovery
planning; neither handlers nor route registration migrate schema.
Sources: [transactions](https://gorm.io/docs/transactions.html),
[v1.30.0 transaction implementation](https://github.com/go-gorm/gorm/blob/v1.30.0/finisher_api.go),
and [migration behavior](https://gorm.io/docs/migration.html).

## R5: Gin handlers and middleware

Extend existing owners rather than rewriting their stricter contracts. Prefer
Handler terminology for new code without compulsory renames. Keep query details
outside handlers and Gin types outside application/persistence contracts. Preserve
explicit DTOs and the project's existing 400/422, 403/404, and conflict policies.

Describe global, group, and endpoint middleware registration and placement.
Authentication establishes identity; stateful object authorization belongs to
the operation and must hold for worker/CLI callers too. Pass principal values
explicitly and use typed HTTP accessors for request metadata. A verifier failure
must not be reported as an invalid credential; select a suitable sanitized 5xx.
No hidden DB/Store dependency lookup through Gin context keys.

Retain `Abort` plus `return`, one response owner, and writer-committed handling.
Do not copy the input router's middleware order as universally correct: reason
about before/after flow, panic unwinding, recovery coverage, CORS preflight, and
whether observers see the final status. Register middleware before the routes
that need it; avoid duplicate Logger/Recovery installation.

Retain existing request-context, proxy-trust, shutdown, and goroutine rules.
A context deadline is cooperative cancellation, not forced completion or license
to replace an already written body. A copied Gin context is not a new writer or
an independent background-work lifetime. The auth example illustrates a verifier
boundary; do not present a token parser as complete production authentication.
Sources: [middleware](https://gin-gonic.com/en/docs/middleware/using-middleware/),
[Gin v1.12.0 context](https://github.com/gin-gonic/gin/blob/v1.12.0/context.go), and
[Gin v1.12.0 route groups](https://github.com/gin-gonic/gin/blob/v1.12.0/routergroup.go).

## Resource ownership and bundle contract

| Owner | Planned responsibility |
| --- | --- |
| `standards/go/style.md` | Go-specific formatting/readability rules |
| `standards/go/examples/style-tooling.md` | Inactive lint configuration, fixture, exact reproduction |
| `standards/go/architecture.md`, `verification.md` | Generic dependencies and tooling adoption/check behavior |
| `standards/gin/architecture.md` | Feature organization and composition, including a labelled schematic tree |
| Existing Gin handler/middleware/runtime/verification topics | Extend HTTP-specific details in their present owners |
| `standards/gin/examples/middleware.md` | Preserve its existing access/responder contract; extend only needed examples/tests |
| `standards/gin/examples/authentication.md` | Small independent verifier/principal example and route-level tests |
| `standards/gorm.md` | Conditional profile entry and read-by-task routes |
| `standards/gorm/stores-models.md` | Concrete Store, model boundaries, write policy |
| `standards/gorm/queries-lifetime.md` | Context, query reuse, errors, SQL and pool lifecycle |
| `standards/gorm/transactions-migrations.md` | Atomicity owner, transaction handle, schema delivery |
| `standards/gorm/verification.md` | Version applicability, DB-backed checks and evidence limits |
| `standards/gorm/examples/store.md` | Bounded reproducible Store fixture and tests |
| `standards/catalog.toml`, `standards/catalog.md`, `README.md` | Resource availability and selection/navigation |
| `tests/test_profile_selection.py` | Independent and combined profile closure regressions |
| New dated research record | Official contracts, executed versions, and limits without changing historical runs |

Keep catalog schema 1 and all existing IDs/anchors. `gin -> go` remains unchanged;
new `gorm -> go` does not imply Gin. Add the style resources to Go and architecture/
auth resources to Gin. Add GORM resources only to its own profile. Update the Go
and Gin entry task routes. Avoid unconditional links from Go/Gin to an optional
GORM profile; adapt any conditional cross-profile route in prepared bundles under
the existing catalog contract. Research/spec/plan files are optional source history.

## Acceptance and evidence

| ID | Required result and evidence |
| --- | --- |
| A1 | All input sections and the style request are accounted for in the reconciliation table and implementation tasks |
| A2 | Style has one owner; existing shared size/control-flow policies remain authoritative; no forced API rename |
| A3 | Pinned lint configuration validates; a clean fixture passes; malformed formatting and representative naming/ignored-error violations fail their intended gates |
| A4 | Feature layout is conditional; direct Handler-to-Store is allowed; no automatic Service/Repository scaffolding |
| A5 | Go-only, Gin-only, GORM-only, combined Gin/GORM, and legacy go-gin selections have correct resource closures and no accidental ORM/framework dependencies |
| A6 | GORM fixture demonstrates intended zero updates, absence/error translation, independent query state, and rollback using a real test database |
| A7 | Gin examples verify permitted/denied routes, verifier failure, context/principal propagation, and committed-response behavior; recovery/order claims have matching scenarios |
| A8 | Changed docs pass artifact/reference checks and whitespace checks, including new files; examples disclose exact versions and evidence limits |

Use a disposable SQLite database for a compact GORM fixture, with pinned GORM
v1.30.0 and SQLite driver v1.6.0 as a proposed starting pair. Their
[GORM manifest](https://github.com/go-gorm/gorm/blob/v1.30.0/go.mod) and
[driver manifest](https://github.com/go-gorm/sqlite/blob/v1.6.0/go.mod) were source-reviewed;
the pair has not been executed here. Reconfirm resolution before implementation.
SQLite checks do not certify PostgreSQL/MySQL SQL, isolation, locking, or error
codes. Target-specific claims require that actual database and driver. Make CGO
and compiler prerequisites explicit instead of silently substituting another driver.

Preserve existing Gin v1.12.0 fixture pins and their supported Go requirements.
Choose compatible, pinned formatting/lint tooling when executing the tooling task;
there is no selected consuming application/toolchain to upgrade in this task.

Official sources above were reviewed on 2026-10-13. Live documentation is not a
versioned runtime guarantee; Gin v1.12.0 and GORM v1.30.0 sources provide bounded
contract anchors. This stage executes artifact checks only. No Go build, linter,
Gin server, GORM operation, or database scenario is claimed to have run yet.
