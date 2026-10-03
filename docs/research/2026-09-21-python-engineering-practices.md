# Python engineering practices: research and adoption

Research started and sources checked: **2026-09-21**. Scope: **K03, Python** in
the [engineering-practices plan](../plans/2026-09-21-engineering-practices.md).
The adopted entry remains [Python / FastAPI](../../standards/python-fastapi.md);
the profile ID and detection rules stay unchanged. This note is optional evidence,
not another instruction file to inject into every Python task.

## Scope, evidence, and versions

The previous profile already required cohesive modules, strict typing without
`Any`, and separation of transport validation from business rules. Gaps were
conditional construction choices, import/package behavior, mutable state and
resource ownership, concurrency/cancellation, integration semantics, and runtime
compatibility. K03 expands those language concerns and moves details behind
task-based routes. Its existing FastAPI/contracts and file-move sections are
preserved verbatim for K04/K05. Pydantic, FastAPI, SQLAlchemy, and psycopg are not
adopted or upgraded by this stage.

Sources below are language/project documentation, specifications, or official
packaging guidance. Architectural choices are the framework's synthesis under
[core](../../standards/core.md), not claims that Python mandates a backend tree.
The service-architecture skill informed the conditional service boundary; its
defaults do not supersede the existing permission for cohesive multi-class
modules or require DDD folders in scripts, tools, and libraries.

| Version evidence | Consequence |
| --- | --- |
| [Python release status](https://devguide.python.org/versions/): 3.14 and 3.13 in bugfix support, 3.12/3.11/3.10 in security support, 3.15 prerelease | Verify support when choosing a runtime; this research does not select a universal minimum or prerelease |
| This workspace: `requires-python = ">=3.11"`; executable interpreter Python 3.12.3 | Examples use 3.11-compatible syntax/APIs; running them here proves behavior on 3.12.3 only, not the entire supported range or suitability of that patch for deployment |
| Installed mypy 2.1.0 and pytest 9.1.1 match `pyproject.toml` development pins | Keep pins unchanged; use actual installed analyzer flags and the existing relevant tests |
| Online [mypy command-line reference](https://mypy.readthedocs.io/en/stable/command_line.html) currently labels itself 2.3.1 | `stable` is moving documentation, not evidence that 2.3.1 is installed. Local `python3 -m mypy --help` confirms the adopted strict/Any flags on 2.1.0; the attempted versioned docs URL was unavailable |
| [PEP 695](https://peps.python.org/pep-0695/) (3.12) and [PEP 742](https://peps.python.org/pep-0742/) (3.13) | New generic/type-alias syntax and `TypeIs` have distinct minimums; a typing backport cannot make newer grammar parse on an older interpreter |
| [3.14 changes](https://docs.python.org/3.14/whatsnew/3.14.html) and [free-threaded execution](https://docs.python.org/3.14/howto/free-threading-python.html) | Check runtime annotation readers, process start methods, and optional interpreter builds when actually migrating; keep unrelated source edits compatible |

Python 3.11 documentation anchors stable example APIs; 3.14 documentation covers
newer behavior explicitly. This is a compatibility decision, not an instruction
to copy an old documentation version's deployment defaults.

## Coverage and recommendation strength

**R** is an Agent_Engineering_Kit requirement justified by its existing typed-boundary,
invariant, contract, or resource-ownership policy. **D** is a recommended default
with a simpler alternative or a documented project-specific reason to vary it.
**O** is an optional technique for the stated condition. Neither a standard
library feature nor a familiar pattern name makes a technique mandatory.

| Required research area | Decision and adoption owner |
| --- | --- |
| Architecture and module boundaries | Cohesion, import direction, capability/use-case ownership; [structure](../../standards/python/structure.md) |
| Construction and useful patterns | Direct construction/injection, callables, Protocol/ABC, factories, adapters, optional persistence/result abstractions; structure |
| Typing, validation, invariants, errors | Static versus runtime guarantees, concrete contracts, state transitions and error mapping; [contracts](../../standards/python/typing-contracts.md) |
| State, concurrency, cancellation, lifetime | Ownership, TaskGroup semantics, cleanup, bounded work, thread/process limits; [execution](../../standards/python/execution-resources.md) |
| Persistence and external APIs | Explicit transaction/effect boundaries, parameterization, client lifetime and replay decisions; execution; driver-specific adoption remains later |
| Tests, review, appropriate checks | Behavioral state/parser/async tests, analyzer scope, actual adapter checks when needed; [verification](../../standards/python/verification.md) and shared policy |
| Security, operations, performance | Exposed input/process/file boundaries, bounds, shutdown, measured optimizations; verification and execution |
| Versions and migration | Runtime/dependency evidence, installation/import checks, feature minimums and migration triggers; structure and verification |

All eight areas apply to the language, with conditions. An isolated pure function
does not acquire HTTP, database, concurrency, or service-architecture obligations
merely because the profile discusses those subjects.

## Organization and construction decisions

**D — cohesive modules, explicit dependency direction.** Python modules naturally
contain multiple definitions; the language does not impose a class-per-file rule.
The framework adds cohesion/layer/dependency criteria. A small function/module is
the simpler alternative to a service hierarchy. For a growing service, separate
entry-point mapping, application coordination, independent domain decisions, and
infrastructure implementations around actual capabilities. Additional layers
cost navigation and assembly; create them only where an existing responsibility
needs an owner. [Modules](https://docs.python.org/3.11/tutorial/modules.html).

**R — preserve imports and public contracts; D — predictable packaging.** Module
imports execute code, so connection/startup effects need explicit ownership.
Small re-export surfaces and import-safe entry points reduce accidental lifecycle
coupling. A `src/` layout helps test installed packages but adds an installation
step; a flat tool need not migrate. After a packaging change, installation outside
the checkout is stronger evidence than adding the source directory to `sys.path`.
Published libraries need deliberate exports/type information; application lock
policy differs from a reusable library's dependency compatibility range.
[Packaging layouts](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/),
[metadata](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/),
[typed library guidance](https://typing.python.org/en/latest/guides/libraries.html).

| Strength and problem/condition | Python form | Simpler alternative, cost, and evidence |
| --- | --- | --- |
| D: explicit collaborator or external boundary | Inject a ready object/function; assemble at its lifetime owner | Concrete arguments suffice; no mandatory container or interface for every type. Framework DIP and [Protocols](https://mypy.readthedocs.io/en/stable/protocols.html) |
| O: real interchangeable behavior | Typed callable for one operation; Protocol for a richer behavioral port | A local branch may be clearer; ABC adds nominal/shared behavior only when needed. [Typing](https://docs.python.org/3.11/library/typing.html) |
| O: creation rules or coordinated assembly | Function or appropriate named classmethod | A dataclass/simple constructor needs no factory hierarchy. Framework construction policy; [dataclasses](https://docs.python.org/3.11/library/dataclasses.html) |
| O: subsystem isolation or repeated cross-cutting behavior | Focused adapter/facade, or a correctly typed decorator | Avoid forwarding-only layers. Wrapper metadata does not establish signature typing or preserved effects. [ParamSpec](https://docs.python.org/3.11/library/typing.html#typing.ParamSpec), [wraps](https://docs.python.org/3.11/library/functools.html#functools.wraps) |
| O: a meaningful persistence boundary or multi-step atomic use case | Narrow Repository/Unit of Work aligned with the actual ORM/domain decision | Direct queries in an allowed adapter are often enough; a generic CRUD API can leak storage. Framework boundary policy; [DB-API](https://peps.python.org/pep-0249/) supplies mechanisms, not an architecture |
| D: ordinary return/exception flow; O: several expected data outcomes | Optional return for real absence, named tagged union when outcome handling benefits | A Result/monad library introduces vocabulary/composition costs; do not require one for a failure branch. [Exceptions](https://docs.python.org/3.11/tutorial/errors.html) and framework KISS/YAGNI |

These are alternative forms for current problems, not a pattern inventory to
instantiate. Properties/underscores express ownership conventions; inheritance
or a DI framework does not independently prove a dependency boundary.

## Contracts, validation, and invariants

**R — strict typed boundaries without bypasses.** This follows existing framework
policy, although Python permits dynamic code. Preserve precise signatures and
named data; isolate an untyped integration with an adapter/stub. Unknown input
can enter as `object` and become a concrete validated value. A checker accepting
an annotation or cast would not prove its runtime shape. A Protocol is structural
typing; even its optional runtime check inspects attribute presence rather than
payload types. Dataclass-generated construction and `TypedDict` similarly do
not replace validation. [Typing contracts](https://docs.python.org/3.11/library/typing.html).

The analyzer baseline retains mypy strict plus separate explicit/unimported-Any
restrictions. Enable expression-Any checks where applicable and state limits;
strict's flag set can change across versions. Broad suppressions or a blanket
legacy rewrite are rejected. Different analyzers may implement the same policy
without identical options. [mypy flags](https://mypy.readthedocs.io/en/stable/command_line.html).

**R — invariants at their state owner; D — choose the lightest data form.** Parse
external shape once, then enforce state rules wherever the operation can be
called. Incomplete drafts remain valid when the domain permits them. Intent
methods check a transition before mutation; plain read models need no rich entity.
Frozen dataclasses provide shallow reassignment protection, not deep immutability
or synchronization. Mutable default factories avoid shared instance defaults.
The [domain example](../../standards/python/examples/domain.md) keeps its input
DTO/parser and entity in separate modules, uses no HTTP dependencies, and tests
rejected publication without state change. No factory/repository is needed for
that operation. [Dataclass semantics](https://docs.python.org/3.11/library/dataclasses.html).

**R — meaningful error and cancellation contracts.** Catch only where recovery
or translation is possible, preserve causes, and keep public messages free of
implementation details. Use a normal absent value only when absence is part of
the contract. Exception groups need deliberate handling; selecting one error or
catching `BaseException` to invent success loses semantics. Explicit exceptions
protect runtime input/state; removable assertions do not. These requirements
apply core error/invariant policy using Python's
[exception mechanisms](https://docs.python.org/3.11/tutorial/errors.html).

## Execution, resources, and integration

**D — sequential first; O — concurrency for a concrete need.** `async` is useful
for overlapping awaitable I/O, with bounded work and explicit task ownership.
For two required independent results the example uses 3.11 `TaskGroup`, with
sibling cancellation on ordinary failure. `gather` is not a drop-in equivalent:
its default error behavior leaves other children running. Cancellation propagates
after cleanup; cooperative timeout is not a hard side-effect deadline.
[Task semantics](https://docs.python.org/3.11/library/asyncio-task.html).

Blocking calls must leave the event-loop thread or use an async adapter. Running
them in a worker thread has library-safety and lifetime costs: a running executor
call cannot be cancelled like its awaiting task. Underlying deadlines, submission
bounds, and resource ownership remain necessary. CPU work may justify processes
or appropriate native operations, with serialization/startup costs. Optional
free-threaded builds require compatible extensions and synchronization; container
implementation locks do not guarantee compound application invariants.
[Async development](https://docs.python.org/3.11/library/asyncio-dev.html),
[executor contracts](https://docs.python.org/3.14/library/concurrent.futures.html),
[free threading](https://docs.python.org/3.14/howto/free-threading-python.html).

**R — resource/effect lifetime; O — context stacks.** A clear `with`/`async with`
or `finally` owner beats relying on finalization. Ordinary contexts suffice for
a fixed set of resources; ExitStack/AsyncExitStack handles conditional acquisition
and partial setup at the cost of another abstraction. A context manager's actual
contract matters: SQLite's connection context commits/rolls back but does not
close the connection. Do not generalize that behavior to all drivers.
[Contextlib](https://docs.python.org/3.11/library/contextlib.html),
[SQLite context contract](https://docs.python.org/3.11/library/sqlite3.html#how-to-use-the-connection-context-manager).

**R — explicit transactions and external effects.** The use case that needs
atomicity owns the transaction; adapters must not commit its partial steps
implicitly. Parameterization, close/rollback behavior, and sharing guarantees
come from the installed driver. Integration code owns parsing, deadlines, response
consumption, and error translation. Remote writes cannot be rolled back by a local
transaction. Retry/idempotency/outbox mechanisms are optional only where the actual
effect contract requires them; replaying an ambiguous write can duplicate it.
This is framework ownership policy, not a Python-mandated ORM abstraction.
[DB-API](https://peps.python.org/pep-0249/) grounds driver obligations; K16/K17
retain ownership of SQLAlchemy/psycopg adoption.

## Verification, security, and performance decisions

**D — behavioral evidence sized to the risk; R — required project gates.** Run
affected behavior and actual adapter checks when their contracts change; keep
tests typed. Parser and entity examples exercise distinct responsibilities.
Async tests coordinate events, observe cleanup, and use isolated loops; they
cannot prove arbitrary scheduling or real client behavior. Documentation edits
alone do not call for a new test framework. Preserve the shared
[verification policy](../../standards/verification.md).
[Isolated async tests](https://docs.python.org/3.11/library/unittest.html#unittest.IsolatedAsyncioTestCase).

**R where exposed — constrain executable/external input.** Never treat untrusted
pickle or `eval`/`exec` input as passive data. Use controlled subprocess arguments,
validated executable/options, and explicit result/resource handling; a shell-free
call still permits option injection, and Windows batch handling needs its own
documented treatment. File/path boundaries need containment and symlink/race
consideration, not prefix matching. Redact sensitive diagnostics. These are
conditional applications of boundary policy, not a compulsory audit on each edit.
[Pickle](https://docs.python.org/3.11/library/pickle.html),
[subprocess security](https://docs.python.org/3.11/library/subprocess.html#security-considerations).

**D — profile a representative bottleneck; O — optimization.** Caching, slots,
generator pipelines, extra concurrency, and interpreter builds have tradeoffs.
Profile code and traced allocations when relevant, then measure the proposed
change in its actual workload. Tracemalloc does not measure all process/native
memory, and profiler timings are not a substitute for a suitable benchmark.
[Profiling](https://docs.python.org/3.11/library/profile.html),
[allocation tracing](https://docs.python.org/3.11/library/tracemalloc.html).

## Adoption and explicit limits

Four conditional sections group related decisions; two optional example files
contain executable modules and stdlib tests. Six catalog resources are copied
only with `python-fastapi`; no new profile ID, native route, dependency, composer
implementation, or automatic expansion of resources is introduced. Shared rules
retain their existing owners. Research remains outside installed instruction
bundles and native context routes.

The profile is useful for Python without FastAPI: framework-specific sections
remain explicitly conditional. Rejected defaults include one class per file,
mandatory backend layers, universal Repository/Factory/Result classes, treating
typing as validation, blanket async conversion, depending on the GIL for compound
state changes, and migrating every project to the current interpreter or layout.

The [practice plan](../plans/2026-09-21-engineering-practices.md) records exact
checks, commands, results, delivery/independent-opening evidence, and the review
checkpoint. Stage execution does not establish a multi-version runtime matrix,
real ORM/client behavior, packaging of an application, process/free-threading
performance, or native-client reading adherence. Those require an affected task
and its own appropriate evidence. Next topic after review: **K04, Pydantic**.
