# TypeScript engineering practices: evidence and adoption

Research date: **2026-09-21**. Scope: K10 of the [approved plan](../plans/2026-09-21-engineering-practices.md).
This note is evidence, not automatically loaded policy. The [TypeScript entry](../../standards/typescript.md)
owns routing and the mandatory user standard; framework/runtime-specific adoption
remains in later stages. [K09](2026-09-21-javascript-engineering-practices.md) retains
ownership of shared JavaScript language behavior and effect-lifetime guidance.

## Scope, versions and recommendation strength

Cover TypeScript's contracts, construction, validation, state/effects, integration,
verification, security/performance and migration across hosts. Preserve the existing
strict/no-any/named-interface policy; language flexibility is not a reason to weaken
it. Node runs the examples, not a newly prescribed runtime for all TypeScript code.
No NestJS/React/Next.js, Node operational, database or native-client stage starts here.

Microsoft's [TypeScript 7 announcement](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/)
dated July 8, 2026 describes the native compiler and lack of the prior programmatic
API. Its compatibility-package aliases support tools still using the 6.x API.
[TypeScript 6 release notes](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/)
describe changed defaults and migration/deprecations. These facts require checking
tool compatibility; they do not authorize an incidental project upgrade.

Executed versions: Node **24.13.0**, npm **11.6.2**, native compiler **7.0.2**,
ESLint **10.11.0**, typescript-eslint **8.70.0**, `@types/node` **24.13.6**. The
`@typescript/typescript6` compatibility package **6.0.2** depends on an aliased
6.x compiler; both npm locks resolve it to **6.0.3**. `tsc6 --version` and importing
the API confirm 6.0.3. A wrapper's package version is not its compiler version.
The examples pin direct tools and retain locks/integrities under `/tmp`; they
have zero runtime package dependencies. A fresh manifest-only install can resolve
different transitive versions. No system/workspace dependencies were changed.

[typescript-eslint's support page](https://typescript-eslint.io/users/dependency-versions/)
and installed peer metadata support the selected ESLint/6.x API arrangement; the
published TypeScript range is `>=4.8.4 <6.1.0` on the research date. It does not
make the native 7.x compiler an interchangeable parser API. The examples check
with both compilers but emit/run only native 7 output. No editor/framework/compiler
performance or broad version matrix was executed.

Strengths used below:

- **R — framework requirement:** existing user policy or necessary contract,
  boundary/ownership or truthful-verification obligation.
- **D — recommended default:** appropriate under its stated condition; an explicit
  project contract can justify a different approach.
- **O — optional technique:** adopt for a concrete problem that warrants its cost.

Static language facts are distinct from these policy strengths. Examples implement
the policy without claiming a type system can validate arbitrary runtime behavior.

## Coverage map

| Research area | Adopted decision | Owner |
| --- | --- | --- |
| 1. Architecture, modules and dependencies | R: contracts live with their owner/consumer; separate type dependencies from runtime identity and actual loading | [Contracts/structure](../../standards/typescript/contracts-structure.md) |
| 2. Construction and patterns | D: literals/functions for simple data/work; O: classes, factories, brands and strategies for state/creation/semantic variation | Contracts/structure; [command example](../../standards/typescript/examples/validated-command.md) |
| 3. Types, validation, invariants and errors | R: named public interfaces and actual unknown-to-owned validation; D: meaningful unions/exhaustive consumers | [Validation/state](../../standards/typescript/validation-state.md); [composition](../../standards/typescript/composition-effects.md) |
| 4. State, concurrency and lifetime | R: readonly/narrowing do not establish exclusive ownership, cancellation or concurrency control | Validation/state and composition |
| 5. Persistence and integrations | R: typed adapters validate/project results; generics/transaction-shaped objects do not provide runtime atomicity | Composition; [operation example](../../standards/typescript/examples/typed-operation.md) |
| 6. Tests and review | R: effective strict project checks plus configured unsafe-operation lint; runtime/consumer evidence for actual changed contracts | [Toolchain/verification](../../standards/typescript/toolchain-verification.md) |
| 7. Security, operations and performance | R: types do not authorize or sanitize external data; D: measure compiler complexity before adding build abstractions | Validation/state and toolchain |
| 8. Version-sensitive behavior and migration | R: verify actual compiler/API/framework versions, support range, emit/loader and locks; no incidental migration | Entry and toolchain |

## Contracts, structure and construction

**Problem:** nominal-looking names and DTO classes can obscure ownership or be
mistaken for runtime validation. **R:** retain named interfaces for public object
and dependency contracts, explicit public signatures and the no-any rule including
tests. Use aliases for unions/tuples/derived types. **Simpler alternative:** infer
ordinary locals and use a small consumer-owned capability instead of an interface
for every class. **Cost:** interfaces/schema copies can drift; schema-derived
contracts remain derived rather than duplicated.

[Type compatibility](https://www.typescriptlang.org/docs/handbook/type-compatibility.html)
is structural and intentionally permits some unsound operations. Extra fields
and compatible shapes do not prove domain identity or exactness. Our interface
preference is user policy, not a TypeScript restriction. **O:** a brand/opaque
type when mixing similar IDs is an actual risk; centralize construction and keep
runtime validation. Distinct fields or a concrete wrapper can be simpler. A brand
does not validate a value or automatically survive a wire round trip.

**D:** plain objects/functions until state, behavior or a creation protocol needs
more structure. A class with private state and an intent operation can protect
a quota invariant; a DTO class/factory for the same fields adds no such protection.
**O:** factory, facade or strategy at a genuine construction/subsystem/variation
boundary. Inheritance and repositories are not required by static interfaces.
The [class handbook](https://www.typescriptlang.org/docs/handbook/2/classes.html)
describes class mechanisms; the architecture choice remains project policy.

Interfaces/types are erased, while constructors, injection tokens and framework
metadata are runtime concerns. **R:** verify the actual registration/validation
path when changing those boundaries. Type-only imports clarify intent but do not
fix architectural dependencies or provide a value at runtime. See the official
[module reference](https://www.typescriptlang.org/docs/handbook/modules/reference.html).
Framework-specific decorator/serialization adoption remains out of K10.

**O:** [satisfies](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-9.html)
for authored configuration/capability literals when useful inference should remain.
It checks assignability at compile time; it cannot replace an executed decoder.
An annotation is simpler when widening is intentional. `as const` can preserve
literal/readonly typing but adds no general runtime freeze. The examples do not
need unchecked `as`, non-null assertions or diagnostic suppression.

## Validation, absence and state

**R:** establish external data as unknown and validate/narrow it at the adapter.
A vendor `any` stays at that boundary; a concrete result leaves it. Ordinary DTOs,
transport validation and current-state invariants have different guarantees.
**D:** reuse the accepted schema mechanism; explicit guards suffice for a small
isolated contract. **Cost:** repeated schemas and type predicates that overpromise
can undermine the apparent type safety. A predicate/assertion function is trusted
by the checker; test its real rejection behavior when it protects a boundary.
See [narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html) and
[assertion limits](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-assertions).

**R:** choose unknown-field/output policy explicitly. A known result needs named
fields, not a broad dictionary. Exact static literals do not prohibit all extra
runtime keys. The command example rejects unknown input; the external-read example
accepts upstream additions and projects only `theme`. Both are deliberate contracts.
Neither types nor parsing authorize a user or establish safety at SQL/DOM/URL sinks.

**D:** express missing, undefined, null and empty values deliberately. Optional
properties and required union-with-undefined fields differ. **O:** additional
[exact optional](https://www.typescriptlang.org/tsconfig/exactOptionalPropertyTypes.html)
and [unchecked indexed access](https://www.typescriptlang.org/tsconfig/noUncheckedIndexedAccess.html)
flags when they address the affected contracts; neither is implied by strict.
**Cost/alternative:** enabling them across legacy code can be a separate migration;
explicit guards and truthful new contracts are still required immediately.

**R:** separate static readonly from runtime ownership. [Object type semantics](https://www.typescriptlang.org/docs/handbook/2/objects.html)
allow mutable aliases and nested changes through a readonly view. **D:** accept
readonly inputs when mutation is unnecessary, hide invariant-bearing state and
return deliberate snapshots. **O:** runtime freezing/copying to satisfy a specific
ownership contract; deep-copying all data adds cost and can lose behavior.
The examples freeze fresh primitive-only output and use `#` fields for runtime
private state. TypeScript `private` is a static restriction, as the class handbook
distinguishes. No readonly annotation replaces persisted concurrency protection.

## Composition, failure and integration

**Problem:** a generic return can pretend to know more than the operation establishes.
**R:** preserve the input/dependency-to-result relationship. **D:** use a concrete
type until variation is meaningful; **O:** `Decoder<T>` when different validators
produce different outputs through the same read protocol. [Generics](https://www.typescriptlang.org/docs/handbook/2/generics.html)
and [function design](https://www.typescriptlang.org/docs/handbook/2/functions.html)
support these relationships. A function that lets a caller choose arbitrary T and
casts raw data does not implement them. Mapped/conditional types and overloads
must express a real relationship; intricate type programs can obscure errors and
increase checker cost compared with a named concrete contract.

**D:** discriminate meaningful outcome/state variants and check exhaustive consumers
with never. The command example has separate changed/below-usage data. A nullable
return or a normal exception remains simpler when there are no extra expected
states. **O:** Option/Result or monadic composition only when repeated operations
and project conventions warrant it; no new functional library is necessary here.
Unhandled defects must not be silently converted to ordinary refusals.

**R:** callbacks accept the promised inputs. [strictFunctionTypes](https://www.typescriptlang.org/tsconfig/strictFunctionTypes.html)
distinguishes function properties from method-syntax exceptions. **D:** use an
honest function-valued capability for callbacks; do not cast a narrower handler
to a broader consumer interface. A typed fake must implement the behavior being
checked, not just satisfy the surface shape. `void` callback contextual typing can
hide a returned value/promise; check whether the invoker actually awaits it.

**R:** typed promises/cancellation/transaction interfaces do not implement runtime
effects. Required work still needs an owner for completion, failure and cleanup;
live state spanning an await needs its real revalidation/concurrency mechanism.
The generic read example checks pre-abort and cancellation before decoding a late
result, under an eventually settling source contract. It does not force I/O to
stop or roll back a remote write. Persistence/serialization/commit/idempotency
belong to actual adapters/use cases, not a generic Repository base class. K09's
language/effect guidance remains the owner of those general mechanisms.

## Verification, toolchain and migration

**R:** preserve the prior enforceability block, relocated verbatim into the
conditional toolchain section. [strict](https://www.typescriptlang.org/tsconfig/strict.html)
does not reject explicit any or all library leaks. [no-explicit-any](https://typescript-eslint.io/rules/no-explicit-any/)
and [unsafe-assignment checking](https://typescript-eslint.io/rules/no-unsafe-assignment/)
illustrate the separate lint boundary; configured typed lint must actually load
project information. [Typed lint setup](https://typescript-eslint.io/getting-started/typed-linting/)
documents project service. **Cost:** typed lint adds tooling/build work; reuse the
project's setup, not a second analyzer by default. [Promise lint](https://typescript-eslint.io/rules/no-floating-promises/)
can identify unowned work but cannot prove resource/transaction completion.

**D:** representative consumer and meaningful negative type checks when a changed
public/generic contract needs them. Isolate deliberate failures and verify exact
diagnostics rather than accepting a missing-module failure. Runtime schema/domain
changes need observable behavior checks; a fake cannot establish real host/DB
guarantees. No type-test library, per-interface test quota or E2E suite is required.

**R:** check the actual tsconfig/project command and framework-generated inputs.
Type-checking, transpilation and runtime type stripping are distinct. [isolatedModules](https://www.typescriptlang.org/tsconfig/isolatedModules.html)
does not replace a full check. `paths` does not rewrite emitted imports; use actual
host/bundler resolution, type/value imports and consumer declarations. `target`,
`lib` and `@types` do not install runtime APIs. **O:** [project references](https://www.typescriptlang.org/docs/handbook/project-references.html)
for real package/build boundaries; they add configuration/declaration obligations.

**R:** preserve supported versions, locks and strictness in a scoped migration.
The 6/7 releases change defaults/deprecations and compiler/API integration; record
effective settings rather than inferring them from a version label. **D:** measure
an observed checker slowdown using the installed tool's supported diagnostics
before restructuring types/builds. The [compiler performance guide](https://github.com/microsoft/TypeScript/wiki/Performance)
is a diagnostic source, not evidence of this application's performance. Published
compiler speedups are not runtime benchmarks. No performance measurement was run.

## Adoption and executed scope

Four conditional sections and two separate examples are added to the existing
`typescript` profile. All 17 IDs, dependencies, globs and selection code are
unchanged. Mandatory rules and the external-data block remain verbatim in the
entry; enforceability/migration details move verbatim to their conditional owner.
No TypeScript-only selection is forced to acquire a Node/server profile. The
shared JS entry/resources and later framework profiles remain unchanged.

The current inspector recognizes a dependency named `typescript`; an npm alias
under that key remains a declared constraint, not proof of an installed compiler
version. NextJS/NestJS select TypeScript through existing profile dependencies.
TypeScript-only passports and explicit profile selection work without package
metadata. A native compiler installed only under another alias is not a new
discovery route; use existing explicit metadata/selection when needed.

Resources are copied with the selected profile and keep manifest digests and
portable links after independent opening. ENTRY/native routes reference the short
profile; they do not embed the conditional files/examples. Research remains a
framework-source reference rather than bundled task instructions.

Both examples passed the two compiler checks, typed lint, native compilation and
execution of emitted ESM on Node: **four command/state tests and five typed-read
tests**, zero failures/cancellations/skips. Five emitted JS files passed syntax
checks. Seven isolated invalid consumers failed under both compilers with the
expected TS2375/TS2540/TS2322 diagnostics. A never-emitted/executed any/promise probe
compiled under strict, then produced all seven expected lint categories: explicit
any, unsafe assignment/argument/call/member access/return and floating promises.
It was removed from normal source/tests afterward; their hashes are unchanged.

Initial temporary installation warned that ESLint 9 was unsupported. The final
examples use the verified compatible 10.11.0 release. Installed source/manifests
also resolved the compatibility-wrapper versus compiler version difference; no
type suppression or runtime-code repair was needed. Package/lock integrity fields,
actual CLI/API versions and no-runtime-dependency manifests were inspected.

The [K10 result](../plans/2026-09-21-engineering-practices.md#k10-result-and-verification)
owns final artifact/delivery commands, results and checkpoint. Stage evidence is
at `/tmp/af-k10-typescript-nsn38qky`, including baseline/before copies, example
projects/locks, diagnostic probes and logs.

No real network, browser/DOM, JSX/framework type generation, decorator injection,
third-party schema library, database/concurrent transaction, monorepo build,
published-package consumer matrix, editor integration or benchmark was executed.
The examples establish one Node runtime and two compiler checks, with one emitted
runtime build per example. Synthetic delivery does not prove model reading
compliance or token savings. No external installation/native pilot or K11–K19
implementation belongs to this stage.
