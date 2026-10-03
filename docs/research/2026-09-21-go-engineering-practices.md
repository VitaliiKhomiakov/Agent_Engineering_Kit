# Go engineering practices: evidence and adoption decisions

**Stage:** K01 of the [practice plan](../plans/2026-09-21-engineering-practices.md).
**Evidence checked:** 2026-09-21. **Adoption target:** the short
[`Go entry`](../../standards/go-gin.md) and its conditional sections under
`standards/go/`. Gin-specific behavior remains
owned by K02. This note is reference material, not another mandatory reading
route in installed projects.

## Purpose and method

The user's publication example identifies a useful distinction: transport input
can be structurally valid while an operation violates a business rule. The
research expands beyond that example to all eight coverage areas in the plan.
Recommendations must explain a real problem, their Go form, the simpler choice,
and the cost of introducing an abstraction.

Sources below are the language specification, Go-maintained documentation and
source, and the original Repository catalog entry. Ecosystem facts are evidence;
the choice to turn them into conditional adoption instructions is Agent_Engineering_Kit
policy. The original examples in the profile are applications of that policy,
not excerpts from the documentation or claims that Go prescribes DDD.

**Strength notation:** R = framework requirement for an affected contract or
resource; D = recommended default that can change for a concrete project reason;
O = optional technique requiring a present use case. Existing supported-version
and delivery constraints still apply. Requirements do not authorize unrelated
rewrites or toolchain updates.

## Version evidence and limits

The official release history lists Go **1.27.1** and **1.26.8**, both dated
2026-09-01. Go 1.27.0 was released on 2026-08-19. Applying Go's published
two-newer-major-releases support rule implies that the maintained series at this
check are 1.27 and 1.26. This is a dated assessment, not a permanent version pin.
[Release history and support policy](https://go.dev/doc/devel/release).

The local executable reports **go1.26.1 linux/amd64**. That older patch is the
available example-check environment, not a recommendation for production. No
toolchain upgrade is part of K01. Compilation there does not establish behavior
on 1.27, another operating system, or the newest patch of 1.26.

| Feature or source | Verified applicability | Consequence for adopted guidance |
| --- | --- | --- |
| Module and toolchain versions | `go`, `toolchain`, workspace configuration, and `GOTOOLCHAIN` affect compatibility/selection | Inspect effective configuration and CI; do not infer the installed compiler from `go.mod`. [Toolchains](https://go.dev/doc/toolchain) |
| Loop capture | Go 1.22 introduced per-iteration variables for loop declarations | Consider the effective language version and declaration form before adding historical capture workarounds. Shared referenced state still needs ownership. [Go 1.22](https://go.dev/doc/go1.22) |
| Benchmark loop | `testing.B.Loop` was added in 1.24 | Use when a benchmark needs it and the supported version allows it. [Versioned testing API](https://pkg.go.dev/testing@go1.26.1#B.Loop) |
| Typed error extraction | `errors.AsType` arrived in 1.26 | It is an available alternative; the broadly applicable profile retains `errors.As`. [Go 1.26](https://go.dev/doc/go1.26) |
| Generic methods | Go 1.27 permits methods to declare their own type parameters; interface methods cannot do so or be implemented by generic methods | Avoid the outdated claim that Go universally forbids generic methods. No 1.27-only example is claimed as locally executed. [Go 1.27](https://go.dev/doc/go1.27) |
| JSON packages | Go 1.27 makes `encoding/json/v2` and `encoding/json/jsontext` available; v2 rejects invalid UTF-8 and duplicate object names by default | Preserve the chosen wire contract. The v1 API remains supported; switching APIs needs compatibility checks, not automatic practice adoption. [Go 1.27](https://go.dev/doc/go1.27) |
| Historical idiom sources | Effective Go predates modules and generics and is not a complete modern-language guide | Use it for core idioms, with the current spec/release notes for feature availability. [Effective Go](https://go.dev/doc/effective_go) |

This is a compatibility filter for the researched decisions, not an inventory
of every release feature. Future refreshes should revisit affected APIs and the
supported project range, rather than replacing every example with the newest
syntax. Dependency graph changes remain deliberate and reviewable under
[Go's module workflow](https://go.dev/doc/modules/managing-dependencies).

## Architecture, patterns, and construction

The following rows are framework decisions. Where a source supplies a language
mechanism or a conceptual pattern, it does not mandate our choice of layers.

| Decision and problem | Applicability and chosen form | Simpler alternative and cost | Evidence / version scope |
| --- | --- | --- | --- |
| D: package boundaries | Group cohesive operations and public contracts; introduce a new package for an actual dependency/access boundary | A file split may suffice. Too many packages add exports and import coordination; `internal` is useful where import restriction is intended | [Module layouts](https://go.dev/doc/modules/layout); established Go module practice |
| D: dependency direction | Where business logic needs isolation, assemble concrete infrastructure at the entry boundary and let consumers describe required behavior | A small CLI can use a few concrete packages. A full domain/application/adapter tree has a maintenance cost and is not universal | Framework application of [package-purpose guidance](https://go.dev/blog/package-names) |
| D: explicit DI; O: Strategy | Pass dependencies as arguments. Use a function for one replaceable operation and a small interface for a real behavioral contract | Direct calls or a local branch may be sufficient. Abstracting every producer creates contracts with no consumer benefit | [Consumer interfaces](https://go.dev/wiki/CodeReviewComments#interfaces); framework choices using ordinary Go functions/interfaces |
| O: Adapter and Decorator | Translate a mismatched external API or wrap a boundary for a cross-cutting concern | A wrapper has error/lifetime/capability obligations. Function types can adapt behavior; a struct is not the only form. HTTP wrappers must preserve capabilities needed by their consumers | [Effective Go](https://go.dev/doc/effective_go), [`net/http` source contracts](https://go.dev/src/net/http/doc.go); inspect the actual wrapped API version |
| O: Repository | Introduce a domain-oriented persistence boundary when domain operations need storage independence or concentrated persistence behavior | A focused SQL adapter is enough for many services. A generic CRUD interface per table adds translation and can hide transactions without protecting a domain boundary | [Fowler's original Repository entry](https://martinfowler.com/eaaCatalog/repository.html); conceptual reference, not a Go requirement |
| O: Factory and Facade | Give meaningful creation rules or a coherent subsystem operation one owner; start with a constructor/function or a small API | Zero values, literals, and direct calls remain valid. A creation service or facade that merely forwards calls adds indirection and may obscure dependencies | [Common pattern policy](../../standards/core.md#patterns-when-a-concrete-problem-warrants-them); original Go adaptation |
| D: concrete types; O: generics/monadic composition | Share a genuine type-independent algorithm with type parameters; use an existing composition abstraction if it materially simplifies a pipeline | Interfaces model behavior; `(T, error)` and `(T, bool)` handle ordinary outcomes. New Result/Option infrastructure adds API, debugging, and dependency cost | [When to use generics](https://go.dev/blog/when-generics); composition is framework judgment, and newer syntax is version-gated above |

Do not turn familiar names into completion criteria. A pattern is accepted when
it simplifies the affected behavior or boundary, with its cost explained. This
also avoids a false choice between always building a rich layered model and
always keeping every business rule in an HTTP handler.

## Contracts, domain rules, and errors

**R — preserve operation semantics; D — local domain methods.** Shape validation
answers whether a request can be interpreted. Domain validation answers whether
the operation is permitted on current state. The profile's `Document.Publish`
allows an incomplete draft but rejects publication without a title and rejects
a second publication. Failure leaves state unchanged. These are illustrative
business decisions, not universal document rules. Cross-object checks and I/O
belong to the use case; database constraints and conflict handling protect
concurrent persistence. The simpler alternative for data without behavior is a
plain struct. A method or constructor is useful only where it owns a rule.
[Shared domain policy](../../standards/core.md).

**R — represent the actual contract; D — concrete values.** The Go-specific
consequences are package-level visibility, reference-bearing values, and receiver
semantics. Unexported fields are not private to a single struct. Copying a value
does not deep-copy its slices/maps. Absence and zero should differ only where
the operation needs them to differ. These facts inform our choice to make
ownership explicit rather than making every field a pointer or adding defensive
checks for impossible states. [Language specification](https://go.dev/ref/spec).
Copying an in-use mutex is separately forbidden by its API contract; this is not
a general ban on value receivers. [Mutex](https://pkg.go.dev/sync@go1.26.1#Mutex).

**R — stable error distinctions; D — ordinary error returns.** Wrapping can
preserve an inspectable cause and thereby expose it as part of a package API.
The profile's `PrepareText` chooses to expose its source's error; a domain API
that promises storage independence can instead translate driver errors. The
relevant tests exercise failure propagation and ensure normalization does not
run after a failed read. Avoid error-string matching or a blanket instruction
to wrap every error. [Go error wrapping](https://go.dev/blog/go1.13-errors).
Returning an error interface containing a nil pointer can accidentally report
failure; return a genuine nil interface on success.
[Go nil-error FAQ](https://go.dev/doc/faq#nil_error).

These examples deliberately omit persistence, transport responses, optional
dependencies, and setter collections. Adding them would distract from the
decisions under examination; they remain responsibilities of an actual project.

## Concurrency, state, and lifetime

**R — owned completion and cancellation.** A goroutine's owner must know how
work finishes, how failure is reported, and how outstanding work is joined.
Cancellation is a request, not a join operation. The profile's `Forward` is
synchronous so that the caller owns launching and waiting. A blocked send and
a blocked receive both have cancellation paths. A buffer is a capacity choice,
not a substitute for an exit protocol. The simpler alternative is sequential
execution when concurrency is unnecessary; parallel work introduces ordering,
capacity, and shutdown obligations. [Pipelines](https://go.dev/blog/pipelines).

**D — context propagation.** Pass request context into context-aware work; keep
its cancellation lifetime explicit. Context values carry request-scoped metadata,
not arbitrary dependencies. Do not store an incoming request context in a service
that outlives the request. Cancellation only works when called operations honor
it; a wrapper cannot make an arbitrary blocking function interruptible.
[Versioned context API](https://pkg.go.dev/context@go1.26.1).

**R — synchronize shared mutation; O — choice of mechanism.** Mutexes and channels
solve different coordination problems. The language memory model supports
reasoning about synchronized communication; it does not make unsynchronized map
updates or aliased values safe. Keep sequential ownership when it suffices.
[Memory model](https://go.dev/ref/mem).
When several `select` cases are ready, cancellation has no priority. `Forward`
therefore does not promise atomic delivery or no sends after cancellation.
[Select semantics](https://go.dev/ref/spec#Select_statements).

## Persistence and external boundaries

| Decision | Conditions, simpler choice, and cost | Evidence / applicability |
| --- | --- | --- |
| R: one transaction owner | A multi-step atomic operation uses its transaction throughout and handles commit failure. A single independent statement may not need an explicit transaction. Domain state checks alone cannot serialize competing writers | [`sql.Tx` workflow](https://go.dev/doc/database/execute-transactions); additional driver/database semantics belong to their own profiles |
| D: long-lived pool | Reuse `sql.DB`; tune limits against database capacity and observed waiting. Arbitrary pool constants can waste connections or throttle throughput | [Connection management](https://go.dev/doc/database/manage-connections) |
| R: query contract and cleanup | Parameterize values, distinguish scan/iteration failures, close rows, and propagate deadlines. Placeholders and cancellation support depend on the driver. Escaping strings manually or assuming one placeholder syntax across databases is insufficient | [SQL injection](https://go.dev/doc/database/sql-injection), [query lifecycle](https://go.dev/doc/database/querying), [cancellation](https://go.dev/doc/database/cancel-operations) |
| R: HTTP resource/status handling | Reuse clients/transports and close response bodies. Handle remote statuses as API outcomes. Select request budgets and response limits for the operation; a streaming request may need a different lifetime policy from a short RPC | [HTTP package](https://go.dev/src/net/http/doc.go), [Client contract](https://go.dev/src/net/http/client.go) |
| R: service bounds where exposed | Choose header/body limits, deadlines, and shutdown ownership appropriate to exposure and workload. A header limit does not limit the body; uniform timeouts can break streaming or uploads | [Server contract](https://go.dev/src/net/http/server.go); Gin handler and middleware details are K02 |

The profile requires an explicit resource/transaction contract where relevant;
it does not select a database, ORM, retry library, or universal timeout. Automatic
retries of writes require the remote operation's own idempotency contract and
are not inferred from a generic Go recommendation.

## Testing, security, and performance

**R — evidence for changed contracts; D — the cheapest reliable check.** Domain
unit checks establish local invariant behavior. Driver/HTTP integration checks
are needed when a real boundary is changed; a successful fake does not establish
database semantics. Table-driven cases, cleanup, and examples are available
testing mechanisms, not per-function obligations.
[Testing API](https://pkg.go.dev/testing@go1.26.1),
[framework verification policy](../../standards/verification.md).

**D — targeted concurrency checks.** A race run detects races exercised by the
program under that instrumentation; success is not a proof about all executions
or deadlocks. Coordinate test actors with channels/events and bound failures
with timeouts. This stage tests both blocked directions in `Forward` because
forgetting the send path is a plausible leak, not to satisfy a case-count quota.
[Race detector](https://go.dev/doc/articles/race_detector).

**D — threat-relevant security checks; O — fuzz campaigns.** Consider untrusted
input size, resource exhaustion, dependency vulnerabilities, and what errors or
logs expose. Go's vulnerability tooling provides useful reachability evidence,
not an application-security certificate. Fuzzing is useful for input parsers and
meaningful invariants; adding a fuzz target to every ordinary method has cost
without a demonstrated risk. [Go security practices](https://go.dev/doc/security/best-practices),
[Go fuzzing](https://go.dev/doc/security/fuzz/).

**D — measure before changing for speed.** Profiles, traces, and representative
benchmarks should answer a specific bottleneck question. A pool or worker system
adds ownership and memory-lifetime costs; it is not justified merely because Go
provides the primitives. Record relevant runtime/workload context and avoid
extrapolating one local benchmark into a universal rule.
[Diagnostics](https://go.dev/doc/diagnostics).

## Reconciliation and adoption

The profile keeps the existing catalog ID `go-gin`; Go discovery already selects
it without requiring Gin. The Gin section is retained for its separate research
stage. General principle definitions, scope rules, model selection, and the
verification lifecycle keep their existing owners.

The user's context-size review identified that the initial 347-line profile was
too broad for routine local tasks. The result uses a 63-line entry with essential
rules and explicit reading conditions. Five cohesive sections cover architecture,
contracts, concurrency, external resources, and verification; three example files
are linked where they clarify those rules. The split preserves all example code.

The catalog's optional per-profile `resources` list registers those eight files.
P2 copies them only where Go is selected and tracks their digests/ownership with
the existing safeguards. Native routes still point to the short profile entry;
resources do not become independent automatic routes or inline entry content.
This reduces the initial Go entry from 2,505 to 508 whitespace-separated words,
not a measured token saving for an actual model session. A complex task may need
several sections. Agent adherence to reading conditions requires a native pilot.

Keeping one long file with heading links would leave full-file reads expensive.
Registering every fragment as an automatically matched profile would enlarge
the initial route set. The selected-resource approach keeps explicit delivery
ownership while allowing the agent to read by task. Do not create tiny files for
every named pattern or require this exact Go topic tree for every technology.
This organization is now part of the plan for subsequent research topics.

Research links remain optional background; an installed bundle does not need
this note to apply the instructions. No new profile ID, native configuration,
or model invocation is introduced.

Rejected defaults include an interface per struct, a mandatory Repository per
table, Factory/Facade wrappers without a role, a class hierarchy translated from
another language, mandatory monadic infrastructure, transport-only business
validation, and unmeasured concurrency/performance changes. Their rejection is
conditional on the absence of the concrete problem they would solve, rather
than a language-wide prohibition.

Actual commands, results, baseline, and remaining verification limits are recorded
once in the [K01 plan record](../plans/2026-09-21-engineering-practices.md#k01-working-scope).
The next topic is Gin after the user's K01 checkpoint.
