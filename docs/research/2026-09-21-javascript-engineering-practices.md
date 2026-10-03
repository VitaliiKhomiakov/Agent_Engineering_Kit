# JavaScript engineering practices: evidence and adoption

Research date: **2026-09-21**. Scope: K09 in the [approved plan](../plans/2026-09-21-engineering-practices.md).
This note records evidence and decisions; it is not an automatically loaded rule.
The [combined entry](../../standards/nodejs-typescript.md) owns task-based routing.

## Scope, versions and evidence strength

Research covers language engineering across browser, worker and server hosts.
Existing TypeScript and server responsibilities remain in the combined profile;
their detailed adoption belongs to K10/K11. Framework UI structure, NestJS,
database libraries and native-adapter pilots remain in their own stages. Using
Node to execute JavaScript or TypeScript to check JSDoc does not start those stages.

ECMA-262's 17th edition, ECMAScript 2026, was approved by Ecma's June 30 assembly.
Use the fixed [2026 overview](https://tc39.es/ecma262/2026/multipage/overview.html)
for the language/host distinction; it does not require projects to target every
feature in that edition. See the [Ecma approval announcement](https://ecma-international.org/news/ecma-international-approves-new-standards-14/).
Rolling MDN/spec links can describe newer behavior than a supported engine.

The executed examples use Node **24.13.0**, npm **11.6.2**, TypeScript **5.9.3** and
`@types/node` **24.13.6**. The latter two are pinned development tools in temporary
projects, with npm locks/integrity values; no runtime dependency is installed.
These are evidence versions, not latest-release recommendations. The code is JS
using established ES2022 constructs and host AbortController/AbortSignal APIs.
The checker uses `NodeNext` resolution and ES2022/DOM declarations; declarations
and a target setting do not prove execution on other engines or in a browser.

Recommendation strengths:

- **R — framework requirement:** an existing project-policy obligation or a rule
  needed to preserve explicit contracts, ownership and honest completion semantics.
- **D — recommended default:** a practical choice when its stated conditions apply;
  a documented project contract can justify another choice.
- **O — optional technique:** useful only for a concrete problem that pays its cost.

Language/API semantics are facts distinct from R/D/O policy. None of the sources
mandates a directory tree, class count, Repository layer or functional/OOP ideology.

## Coverage and adopted decisions

| Research area | Decision and strength | Adoption |
| --- | --- | --- |
| 1. Architecture and boundaries | R: cohesive modules, explicit dependency direction and smallest useful exports; host/framework mechanisms stay at their boundary | [Modules](../../standards/javascript/modules-structure.md) |
| 2. Construction and patterns | D: functions/literals for simple operations/data; O: closure, class, factory or strategy when state, creation or variation warrants it | Modules; [input/state example](../../standards/javascript/examples/input-state.md) |
| 3. Contracts, validation and errors | R: named owned contracts and executed boundary validation; distinguish representation, current-state invariants and public errors | [Values/state](../../standards/javascript/values-state.md) |
| 4. State, concurrency and lifetime | R: an owner for mutation, required promises, cancellation and cleanup; D: sequential or bounded parallel work by contract | [Async effects](../../standards/javascript/async-effects.md); [ownership example](../../standards/javascript/examples/async-ownership.md) |
| 5. Persistence and integrations | R: explicit adapter/transaction/commit semantics; promises cannot establish atomic persistence or undo effects | Async effects and serialization in values/state |
| 6. Tests and review | R: observable checks under shared policy; O: JSDoc checking without JS-to-TS migration; real-host checks for host changes | [Verification](../../standards/javascript/verification-compatibility.md) |
| 7. Security, operations and performance | R: control untrusted keys/output and bound work by actual resources; D: measure before worker/cache/general scheduler adoption | Values/state, async effects and verification |
| 8. Versions and migration | R: preserve support/lock/module contracts; distinguish language, host APIs and loader/build; no incidental migration | Entry and verification |

### Modules, construction and dependencies

**Problem:** a shared suffix or barrel can hide unrelated capabilities, cyclic
imports or module initialization effects. **R:** preserve the prior module
grouping/export rules, relocated verbatim to the conditional modules section.
Server transport language is conditional on server work. Browser structure follows
the feature and its view/state/I/O ownership, without manufacturing backend layers.
**Simpler alternative:** a cohesive local module instead of a package or DI layer.
**Cost:** more public modules require consumer and runtime-resolution checks.

**D:** choose a stateless function or literal until behavior/state/dependencies
warrant a closure or class. **O:** centralize a nontrivial creation protocol in a
factory or vary an actual decision through a callback/strategy. A named DTO does
not need a constructor or factory; the invariant-bearing Capacity example does
benefit from private state and intent methods. Repositories/facades are justified
by a meaningful adapter contract, not a blanket pattern quota.

[MDN modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
documents strict module evaluation, live bindings, cycles and dependent evaluation
around top-level await. [Import](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import)
distinguishes imported bindings from a frozen object graph. **Version limit:**
ESM syntax does not select browser/Node/bundler resolution; verify actual consumers.
**D:** explicit startup ownership where import-time effects obscure lifetime.

[Method receiver semantics](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)
explain why extracted methods need a preserved receiver and arrow functions use
lexical `this`. **D:** wrap/bind at the callback boundary when needed; retain
listener identity for removal. **Cost/alternative:** per-instance binding and
closures retain state; direct functions or calls through the object are simpler
when no callback is necessary. Do not mass-convert methods to arrow fields.

### Contracts, value semantics and invariants

**Problem:** successful JSON parsing and editor types can be mistaken for a valid
operation. **R:** validate the actual external representation and produce a named
owned result; keep current business state and authorization decisions with their
owners. Preserve the entry's typed-boundary obligations verbatim. **D:** use an
existing runtime schema; for a tiny isolated JSON contract, explicit checks avoid
a new dependency. **Cost:** handwritten checks become a second schema if a project
already owns one. JSDoc/checkJs is optional tool support, never runtime validation.

[Working with objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects)
distinguishes own and inherited properties. **D:** declare missing/null/default
behavior rather than using truthiness. JSON text creates a different boundary
from arbitrary objects that can execute getters/proxy traps during inspection.
The example requires an own nullable field and rejects unknown keys; other
contracts can intentionally permit omission or extensions if their policy is clear.

[Equality semantics](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Equality_comparisons_and_sameness)
and [safe integers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/isSafeInteger)
motivate explicit comparisons and numeric bounds. **R:** validate the required
representation, not just a post-coercion shape. **O:** BigInt or a decimal library
only for an exact-value requirement with a compatible wire contract. The simpler
alternative for bounded quantities is a safe integer with a range. Neither a
type annotation nor a later guard repairs precision already lost during parsing.

**Problem:** accidental aliasing lets callers bypass state transitions. **R:**
make mutation ownership explicit; **D:** use private state/intent methods and
deliberate snapshots where an invariant requires them. A local variable or plain
record is simpler when no behavior or lifetime must be protected. **Cost:** copying
large graphs adds work, and a wrapper class alone does not provide immutability.
[Object.freeze](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze)
is shallow; spread/assignment also retain nested references. Freezing the example's
fresh primitive-only snapshot is sufficient for that contract, not all objects.

**R:** choose serialization at the integration boundary. [JSON.stringify](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)
has omission, numeric and BigInt limits; [structured clone](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm)
supports data graphs without reconstructing arbitrary prototype/private-state
contracts. **O:** structuredClone where supported and data semantics fit;
**simpler alternative:** explicit field projection. Neither is a generic rich-model
copy mechanism. Version/host support and transferred-resource behavior need checks
if a task adopts them; this stage does not execute a worker transfer.

### Async lifetime, failure and external effects

**Problem:** started work outlives a reported result or a failed sibling. **R:**
return/await required work, preserve failures and own cleanup. **D:** sequential
awaits for dependent work, fixed/bounded parallel reads only when useful.
**Cost:** parallelism consumes resources, and joining cleanup can delay failure.
The example intentionally makes that tradeoff visible instead of implying immediate
failure and guaranteed cleanup can both occur for arbitrary dependencies.

[Using promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises)
explains floating promises and chaining. [Promise.all](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all)
observes its inputs and fails early; it does not cancel siblings or wait for all
cleanup before rejecting. Do not attribute later unhandled sibling rejections to
the combinator itself. **D:** choose all/allSettled/race by outcome semantics and
handle the underlying operation's lifetime separately. `allSettled` does not make
required failures optional; timeout races alone do not terminate work.

[Await semantics](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)
allow other work before a continuation. **R:** examine state assumptions spanning
await; single-threaded execution is not protection against stale decisions across
multiple jobs. **O:** generation checks, revalidation or actual transaction/version
control according to the resource. No in-memory object can establish atomic
database updates simply by placing them in a Promise chain.

[WHATWG DOM cancellation](https://dom.spec.whatwg.org/#aborting-ongoing-activities)
is cooperative API behavior; promises have no built-in abort capability.
**O:** use a signal-aware owned group when cancellation and joined cleanup matter.
**R when used:** account for pre-abort, listener removal, synchronous adapter throw
and late completion; dependencies must eventually settle under their actual
deadline/cleanup contract. A sequential operation with one owner is simpler when
parallelism is unnecessary. A noncooperative operation can make a join wait forever.

**D:** use `try`/`finally` over the awaited resource scope. [Async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for-await...of)
provides iterator closing for early consumer exit, not release of arbitrary
unrelated resources. New disposal syntax is conditional on tool/runtime and API
protocol support; it is unnecessary for these examples. **R:** external writes
need an explicit transaction/idempotency and ambiguous-failure policy. Durable
handoff, retries, repositories, outboxes and sagas are not language requirements.

### Verification, security and compatibility

**R:** use [shared verification](../../standards/verification.md) and actual affected
boundaries. **D:** deterministic promise gates for orchestration checks; an adapter
integration when network/DB behavior changes. **Cost:** mocks cannot establish
real host cancellation or database isolation, and full browser/E2E infrastructure
adds little evidence for a pure local parser. Avoid helper-by-helper test quotas.

[checkJs](https://www.typescriptlang.org/tsconfig/checkJs.html) and the
[supported JSDoc forms](https://www.typescriptlang.org/docs/handbook/jsdoc-supported-types.html)
permit named JS contracts and unknown-value narrowing without changing source
language. **O:** strict no-emit checks when useful; reuse the project's checker.
The temporary examples check source and tests without `any`, suppression or an
unchecked DTO cast. This validates one pinned toolchain, not all compiler versions.

[Prototype pollution](https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/Prototype_pollution)
motivates controlling external keys and explicit projection. **R:** prevent unsafe
interpretation/merging at the affected boundary; output and authorization remain
separate decisions. **O:** Map/null-prototype dictionaries for genuinely dynamic
data; a named ordinary object is simpler for a known result. A new validation
library, modified built-in prototype or global hardening flag is not automatically
required. The example rejects an own JSON `__proto__` key before merging anything.

The [Node blocking-work explanation](https://nodejs.org/en/learn/asynchronous-work/dont-block-the-event-loop)
supports the inherited warning that `async` does not make synchronous computation
nonblocking. **D:** bound work and measure relevant load before caching, workers
or streaming infrastructure. Host-specific operational tuning remains K11/UI work.
**R:** check language syntax, host APIs and module loading separately, preserve
supported targets and locks, and avoid incidental package/module/JS-to-TS migrations.
No specific newest runtime is prescribed from a documentation link.

## Reconciliation and delivery

Four conditional sections and two optional examples are registered as six
resources on the existing `nodejs-typescript` profile. All 17 profile IDs,
technologies, dependencies, globs and selection code remain unchanged. The entry
adds task conditions and preserves mandatory TypeScript/NestJS/Next.js routing,
typed-boundary obligations, server execution responsibilities and file-move checks.
Module grouping is relocated, not replaced with a new hierarchy.

Current package metadata inspection records a `nodejs` fact for any package.json,
even a browser package without `engines.node`; it does not prove a server runtime.
That existing route makes shared JavaScript material available while server rules
remain conditional. There is no separate JavaScript technology fact. A metadata-free
browser script needs explicit profile selection; K09 does not add discovery heuristics.
The delivery checks also exercise Node engines, NestJS/TypeScript dependencies,
a Node-only passport and explicit selection, with unrelated Go exclusion.

Registered resources are copied only with the selected profile, carry existing
digests/ownership and remain reachable after opening a project independently.
They are not concatenated into ENTRY/AGENTS/CLAUDE/Cursor rules or assigned new
automatic native routes. Research stays uncopied as a framework-source reference.
Actual agent reading compliance and token savings require a separate native pilot.

## Executed examples and limits

The [input/state example](../../standards/javascript/examples/input-state.md)
executes 20 scenarios around a small JSON contract and stateful refusal without
mutation. The [async example](../../standards/javascript/examples/async-ownership.md)
executes six scenarios around required results, synchronous/asynchronous failure,
pre-abort, in-flight cancellation, cleanup joining and late results. No sleeps,
sockets or runtime packages are required. [Node's versioned test documentation](https://nodejs.org/download/release/v24.13.0/docs/api/test.html)
is the runner reference; the examples do not prescribe Node for browser projects.

Syntax checks, strict JSDoc checks, npm manifest/installed-version checks and both
runtime test forms passed. The local `--test` subprocess report exposed only a
file aggregate; direct node:test execution exposed 20/6 named results. An isolated
intentional failure returned exit 1 with both forms and with isolation disabled.
This records the observed reporting limit without claiming a universal Node bug
or treating file counts as scenario counts. No example code change was needed.

The [K09 result](../plans/2026-09-21-engineering-practices.md#k09-result-and-verification)
owns final artifact/delivery commands, results and checkpoint. Baseline, temporary
projects/locks and logs are retained at `/tmp/af-k09-javascript-xpgw2_ck`.

No actual browser/DOM/fetch, worker/shared memory, persisted transaction,
multi-process race, timeout/backpressure, durable queue, real network cancellation,
benchmark or multi-version matrix was executed. Deterministic interleavings prove
the demonstrated ownership protocol under its dependency contract. They do not
establish forced cancellation or atomic external effects. No external installation,
native pilot or K10–K19 implementation belongs to this stage.
