# Guidance quality and skill delivery

Status: design accepted for staged implementation on 2026-11-06.
Prepared on 2026-11-06. Current stage authorization is recorded in the plan.
Progress and execution evidence belong to the
[canonical plan](../plans/2026-11-06-guidance-quality-and-skill-delivery.md).

## Outcome and scope

Improve the guidance an agent actually applies to a task while keeping one
authoritative library of engineering rules. Review shared guidance and all
existing language/technology profiles, close evidenced contract gaps, strengthen
concrete Angular guidance, and evaluate one optional Angular reference skill
before expanding native skill delivery.

The expanded research requested after the first proposal covers the complete
technology inventory. Angular remains a proposed delivery pilot, not the limit
of the content assessment or an already approved first implementation priority.

Superpowers remains the existing procedural toolkit. AEK supplies engineering
constraints, task-specific technical references, and result expectations through
the [current composition policy](../../standards/superpowers.md).
This proposal does not create another design, implementation, or review lifecycle.

## Current state

The source review used AEK commit `304feef0cad0e7b04b09c93ddb62eb2bc2acd3fe`
with a clean working tree before these documents were added.

- [Core](../../standards/core.md) already covers responsibility placement,
  practical abstraction, state invariants, scoped changes, and conditional rules.
  [Verification](../../standards/verification.md) already selects checks by risk
  and preserves valid evidence. A broader checklist is not automatically better.
- [Angular](../../standards/angular.md) already covers feature ownership, provider
  lifetime, reactive state, request concurrency, forms, security, SCSS, rendering,
  SSR and verification. It protects existing project versions and form/state choices.
- The reviewed Angular topics lack dedicated guidance for view/content query
  contracts, projection, host behavior and directive composition. Component and
  test examples can make these contracts easier to apply without reproducing an
  entire vendor manual.
- [Project task skills](../../standards/project-skills.md) already provide optional
  design and review entries. Native templates are preparation inputs, and current
  documented native task-skill installation targets Codex. Their availability is
  distinct from installation and observed client activation.
- [Hosted publication](../maintenance/agensi-publication.md) is an existing,
  separate delivery channel. Its dated references do not synchronize an adopted
  project. This proposal does not change that publication or its active task.

These are source-review findings. They do not establish measured improvements in
agent behavior or prove that an example has run.

## Technology coverage and dispositions

All 36 catalog profiles carrying a technology selection were mapped, including
five compatibility aggregates and the additional Next.js structure profile.
The assessment read profile entries and relevant contract owners; it is not a
claim that every example or supported version was revalidated. The external
research record owns detailed comparisons and their reading coverage.

| Existing AEK profiles | Current strengths to retain | Follow-up justified by this review |
| --- | --- | --- |
| `python`, `pydantic`, `fastapi`, `python-fastapi` | Typed/runtime contracts, cancellation, dependency and transaction lifetime; independent component selection | Shared authentication, diagnostic and documentation candidates only; no default package-manager, async-driver or deployment migration |
| `php`, `symfony`, `doctrine`, `php-symfony-doctrine` | Autoload/types, actual validation paths, worker lifetime, ORM/DBAL distinction and unit of work | Preserve framework-specific guidance; investigate shared candidates without imposing repositories or redundant PHPDoc |
| `go`, `gin`, `go-gin` | Consumer-owned contracts, package cohesion, cancellation, pooled HTTP context and resource cleanup | Conditional authentication/diagnostic routes; no mandatory package tree, interface-first design or router replacement |
| `javascript`, `typescript`, `nodejs`, `nodejs-typescript` | Host separation, validation of unknown values, precise inference, streams, capacity and shutdown | Shared documentation/diagnostic candidates; no automatic TypeScript conversion, UI framework or new validator |
| `nestjs` | Actual module/DI/metadata, transport, authorization and adapter behavior | Conditional token-validation route; retain selected ORM and proportionate checks |
| `typeorm` | Transaction-scoped managers, rich domain transitions, query scope and migration safety | Check discoverability of driver-specific TLS verification; add a concise route only if current selected rules leave a gap |
| `react` | State identity, effect cleanup, stale-result handling and accessible form contracts | Reuse existing interaction checks; extend widget guidance only for a demonstrated need |
| `nextjs`, `nextjs-framework`, `nextjs-feature-structure` | Router/runtime/cache distinctions, server-operation authority and capability-based structure | Reuse shared authentication guidance where applicable; no styling, state or hosting stack replacement |
| `angular`, `ngrx` | Provider/state ownership, reactivity, forms, rendering, SCSS and explicit state-library selection | Component/query/projection/directive work below; preserve NgRx-specific contracts |
| `sqlalchemy`, `psycopg` | Session/connection ownership, transaction recovery, result boundaries and driver-specific behavior | Preserve existing depth; generic ORM/SQL advice alone does not justify changes |
| `postgresql` | Durable constraints, real-role RLS checks, TLS, pool/lock lifetime and recovery evidence | Preserve existing rules; only concrete query/schema/operational gaps warrant additions |
| `docker` | Build secrets, current Compose capabilities, signals, readiness and recovery | Preserve existing rules; no routine image build or new operations stack |
| `rag`, `llm-tools` | Source authority/access, corpus lifecycle, trusted executor context and uncertain effects | Retain the shared boundaries; do not substitute illustrative tool calls for permission enforcement |
| `llamaindex`, `langchain`, `langgraph` | Language/version distinctions, retrieval/synthesis separation, reducers and replay boundaries | Version-check any accepted recipe; no automatic provider, vector-store or graph adoption |
| `langfuse`, `eino` | Vendor-specific privacy/exporter and Go execution contracts | No comparable specialized material established a change; generic tracing/agent advice is insufficient |
| `unreal-engine`, `godot` | Engine-managed lifetime, assets, interop and editor evidence | Preserve engine-specific rules; generic C++/C# or another engine's recipes are not substitutes |

A preserved profile is a valid outcome. A named counterpart is not evidence of
equal coverage, and absence of one does not establish that AEK is complete.
Compatibility aggregates remain routing choices rather than new policy owners.

## Global constraints

1. Keep each technical or procedural rule in one authoritative owner. Native
   skills route to those owners; they do not maintain independent policy copies.
2. Keep the two user-supplied comparison repositories' identities, URLs, snapshots
   and comparison notes outside this repository and all distributable outputs.
   Author new prose and examples independently from verified contracts; do not
   vendor or closely reproduce third-party text or examples.
3. Preserve Superpowers composition, current-checkout execution, human stage
   checkpoints, and existing Git permissions. A selected skill grants no actions.
4. Preserve supported language, runtime, framework, driver and engine versions,
   existing package managers, ORMs, test runners and deployment choices. For
   Angular preserve NgModule/standalone interoperability, ZoneJS/zoneless,
   form choices, state ownership and SCSS policy. Do not upgrade fixtures or
   consuming projects to make an example work.
5. Keep catalog schema 1, stable existing profile IDs and bundle-relative paths.
   Dependencies supply resources, not an unconditional reading queue.
6. Native skill installation remains explicit. Ordinary Angular selection does
   not install a skill, NgRx, another application stack, a plugin or a client.
7. Required technical rules remain reachable through project instructions when
   no native skill activates. A source checkout or private research cache must
   never become a consumer project's operational dependency.
8. Distinguish inspected sources, static checks, executed examples, native
   discovery and observed task behavior. Preserve dated historical evidence.

## Approaches considered

| Approach | Benefit | Cost or limitation |
| --- | --- | --- |
| Improve existing rules and reading routes only | Smallest change and no new native entry | Does not test whether native discovery improves access to Angular guidance |
| Keep the library and pilot one Angular reference skill | Reuses rule ownership and gives a bounded comparison of delivery mechanisms | Requires explicit installation mapping, portability checks and behavioral evidence |
| Convert technology profiles into a broad skill collection | More individually discoverable entries | Larger metadata surface, overlapping triggers and update scope without evidence of benefit |

The second approach is the recommendation for review. Content improvements can
remain useful even if the optional skill pilot does not justify broader adoption.
The recommendation is not recorded as a user-approved implementation decision.

## Shared guidance assessment

Classify each candidate as already covered, useful gap, incompatible advice, or
unverified. A useful gap needs an affected task, a concrete failure or ambiguity,
an existing owner, and an explanation of why the proposed wording improves AEK.
Add nothing merely to match another collection's topic count.

| Candidate | Initial disposition | Owner and next evidence |
| --- | --- | --- |
| Naming, cohesion, scoped changes and justified abstraction | Preserve existing coverage | Core already defines context-sensitive requirements; retain them |
| Tests for every exported function, conflicting small-function targets, default branching and universal retries | Exclude as blanket requirements | Existing verification, size, work-mode and effect contracts remain authoritative |
| Authentication and JWT verification | A dedicated conditional contract is missing | Existing authorization rules remain; propose one shared authentication topic and relevant transport routes |
| Public-contract documentation and comments explaining constraints | Investigate a bounded cross-language gap | Go already covers this directly; supplement missing semantics without requiring repeated native-type documentation |
| Error context, safe diagnostics and operational correlation | Substantial existing coverage; investigate limited ownership/routing gaps | Node, Nest, language, database and LLM owners already cover many requirements; avoid duplicating them or mandating a monitoring stack |
| Performance and dependency practices | Reconcile by actual task and version | Preserve measured optimization and compatibility; do not add default infrastructure |

A completed assessment may conclude that no shared-policy edit is warranted.
Detailed comparison provenance stays in the external research record; publishable
decisions cite AEK requirements and relevant official contracts.

## Proposed shared contract work

**Authentication, priority candidate.** Propose
`standards/security/authentication.md` as a conditional shared resource, reachable
from core's task routes and relevant transport topics. It applies when changing
authentication or token verification; it does not select JWT, OAuth, a provider,
a library or a new profile automatically. Keep object/tenant authorization at
the application operation even after a credential is verified.

For actual JWT use, define the application's token purpose, allowed algorithms,
trusted issuer/key source, audience, required claim presence/types and time
validation. Decoding is not verification. A key lookup must not treat an
untrusted token header as permission to fetch an arbitrary destination. Describe
rotation/cache/replay and refresh behavior only where the selected protocol
requires them; no universal token lifetime or key-ID requirement is proposed.
Use established libraries rather than new cryptographic implementations.

Acceptance includes rejected wrong-purpose/issuer/audience/algorithm tokens,
missing application-required claims, expired/not-yet-valid tokens, untrusted key
sources, and unchanged operation authorization. For an executable example, verify
these cases with its pinned library; prose inspection alone does not prove them.
The contract basis checked on 2026-11-06 is
[JWT BCP](https://www.rfc-editor.org/rfc/rfc8725.html),
[application-defined JWT claim requirements](https://www.rfc-editor.org/rfc/rfc7519.html),
and conditional [OAuth security](https://www.rfc-editor.org/rfc/rfc9700.html).

**Diagnostics and public documentation, bounded candidates.** First reconcile
existing Node/Nest/language/LLM owners. A shared addition should settle a concrete
missing obligation such as who reports an error once, safe correlation across a
changed boundary, or documentation of non-obvious caller-visible constraints.
Preserve redaction, bounded telemetry and actual runtime context mechanisms.
SLOs, alerts and runbooks apply only to selected service operations. Do not require
trace fields when no trace exists, external export, a universal JSON logger,
comments repeating every type, or a test for every documented export.

Prefer a short common clause plus existing specialist details. If shared diagnostic
detail needs a separate owner, propose `standards/diagnostics.md` and declare it
as a conditional core resource; create it only after the gap decision. Public
documentation semantics belong in core with language-specific syntax retained in
the corresponding owners. These decisions do not justify expanding every profile.

**Technology follow-ups.** A driver-security route in TypeORM and accessible
component/widget contracts are bounded candidates, not a general rewrite of
database or UI profiles. Verify them against selected driver/framework contracts
before editing; retain a no-change outcome if existing routes are sufficient.

## Angular improvements

Prioritize bounded failure cases rather than coverage of every Angular API:

| Area | Required result | Proposed owner |
| --- | --- | --- |
| Component inputs, outputs and child queries | Explain ownership, optional/required query results, view versus projected content and version-compatible APIs | New `standards/angular/components.md`; existing boundary text routes to it without conflicting copies |
| Projection and host behavior | Explain slot contracts, conditional content, native semantics, focus and host binding responsibilities | The same component topic; preserve existing SCSS and presentation boundaries |
| Directives | Explain reusable host behavior, cleanup, composition and exposed input/output contracts; preserve SSR compatibility when relevant | New `standards/angular/directives.md` |
| Component and directive checks | Demonstrate meaningful DOM behavior after production-like notifications, query absence and event/cleanup cases | Existing `standards/angular/verification.md` and new `standards/angular/examples/component-contracts.md` |
| Forms, reactivity, routing and SSR | Add only an evidenced gap; preserve correct existing contracts and version guards | Existing topic owners; no wholesale migration or duplicated tutorial |

New topics and examples must be declared in the Angular catalog resources and
reachable through its task table. Preserve existing headings used by links, or
update their affected routes with a compatible anchor where needed.

Examples state their tested Angular/TypeScript/test-runner versions and exact
scope. A dependency-free explanation is not an executed example. A minimal
temporary harness may validate an example without adding an application runtime
to the AEK root. Preserve an existing consumer runner instead of requiring Vitest.

The initial public contract review covered
[queries](https://angular.dev/guide/components/queries),
[projection](https://angular.dev/guide/components/content-projection),
[directive composition](https://angular.dev/guide/directives/directive-composition-api),
[component testing](https://angular.dev/guide/testing/components-scenarios),
[zoneless notifications](https://angular.dev/guide/zoneless), and
[form selection](https://angular.dev/guide/forms/signals/overview) on 2026-11-06.
The current pages describe Angular 22-era behavior; implementation must also
check the exact target-version contract for each selected example or change.

## Optional Angular reference skill

The user's subsequent benefit-first instruction makes source integration
conditional on E1's observed value assessment. The
[2026-11-06 evaluation](../research/2026-11-06-angular-skill-evaluation.md)
did not establish sufficient incremental value in its bounded scope. The proposal
below is retained for possible reassessment; it is not selected for installation
or source-template delivery at this checkpoint. Existing improved rules and
direct routes remain the chosen Angular delivery path.

Proposed name and source: `aek-angular` at
`templates/skills/aek-angular/SKILL.md`.

The entry selects technical guidance for implementation, design or review of an
actual Angular application/library with adopted AEK rules. Generic TypeScript,
HTML, React, prose-only changes and unrequested setup are negative trigger cases.
The entry must:

1. Reuse the task, local instructions, approved design and actual version/configuration facts.
2. Read the Angular entry and only the topics relevant to the changed contract.
3. Apply the already selected Superpowers procedure through local adaptations
   once; do not restart planning or add another review or progress record.
4. Return technical decisions, changes or findings through the existing task's
   output contract, including relevant evidence and limits.

The first proposal uses the existing `angular` profile's `source_resources` for
template availability. Selecting Angular alone still installs no native entry.
The existing `project-workflows` profile continues to select only its design/review
entries; the Angular reference entry must not depend on installing those skills.
`MIGRATION.md` remains the owner of explicit selection, destination adaptation,
managed-file reconciliation and recovery.

Pilot native mapping follows the existing Codex project location:
`.agents/skills/aek-angular/SKILL.md`. Rebase references to the actual adopted
bundle, including flat/custom layouts and independently opened repositories.
Do not install raw preparation copies in the bundle or rely on the AEK checkout.
Claude Code and Cursor retain their existing direct routes until native mappings
and activation have separately been verified for a selected client/version.

Existing official or custom Angular skills may coexist. Preserve unowned entries;
define the AEK entry's role and avoid competing automatic setup or duplicate
procedures. Missing guidance is a reported input limitation, not permission to
install dependencies or adopt AEK automatically.

## Acceptance and pilot decision

All content changes need a documented disposition and an authoritative owner.
Every native output needs valid metadata and reachable local references. Static
checks must also show that unselected skills and unrelated profiles stay absent.

Compare the existing direct routes with the same approved rule content exposed
through the optional skill. Hold task inputs, model/effort, client version,
permissions and Superpowers configuration constant. Record rule/content identity,
actual reads, rule compliance, task outcome, unnecessary actions and measured
cost where available. Do not confound better rule content with better packaging.

| Scenario | Observable acceptance |
| --- | --- |
| Small fix or supplied-code review | Correct scope and result without unsolicited adoption, planning, fixes or unrelated checks |
| Conditional child or projected content | Correct query contract and content ownership; absence handled when permitted |
| Directive behavior | Intended inputs/outputs, keyboard/focus behavior and owned cleanup; SSR conditions respected |
| Existing forms or older Angular setup | Compatible guidance without forced upgrades, state-library changes or runner replacement |
| Reused route and stale response | Existing state/concurrency rules remain effective through the new entry |
| SSR request state | No cross-request state leakage or browser-only initialization on the server |
| Non-Angular task or absent optional skill | No false activation; direct task routes remain sufficient |
| Overlapping skill or missing resource | No duplicate workflow or unowned replacement; a precise limitation is reported |

Use repeated paired runs for claims about frequency or cost; one demonstration
establishes only that observed run. A pilot succeeds only with working native
discovery and no unresolved material scope, compatibility or rule-compliance
regression. Broader skill rollout requires an observed usability/routing benefit
and a reviewed cost tradeoff. If results are inconclusive, retain the improved
rules and direct routes and leave expansion unapproved.

No live client evaluation or Angular runtime check has been executed in this
preparation stage. Their results must be recorded when those stages are authorized.
