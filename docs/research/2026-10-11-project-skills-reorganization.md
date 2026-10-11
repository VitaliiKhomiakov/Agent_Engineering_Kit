# Project skills: ownership and route inventory

**Date:** 2026-10-11. **Scope:** PS-01, before-state source inventory and proposed
first slice. This record contains observations and proposed dispositions, not
operational instructions or a second progress checklist. The
[canonical plan](../plans/2026-10-11-project-skills-reorganization.md) owns status;
the [specification](../specs/2026-10-11-project-skills-reorganization.md) owns acceptance.

## Baseline and method

- Checkout/instruction root: `/home/vitalii/Documents/Local_Projects/Agent_Engineering_Kit`.
- HEAD: `a725cf28cb4e399e64c13dc421e63ea7cc4ae580`; tracked files were clean.
  Eight untracked planning/research/specification files existed before this stage.
- Preserved state: `/tmp/aek-project-skills-ps01-3_1h1dyf/baseline.json` records
  256 tracked content identities and eight untracked identities. `originals/`
  contains the eight untracked originals. This research file was absent.
  The source commit retains tracked inputs; the temporary copies preserve prior
  user work through this stage's review. They are not consumer update bases.
- Source catalog schema 1 contains 35 profiles, seven required profiles and seven
  shared assets. There are 182 standards Markdown files: 35 profile entry paths,
  42 conditional example files and 105 other policy/topic/reference files.
  The source has 18 template files and three existing skill templates.
- The heading inventory covers 833 headings in standards, including document
  titles, example file headings and evidence sections. It is not a count of
  mandatory rules. Every standards file is declared as a profile source/resource
  or shared asset. All 42 examples have an incoming entry/topic link.
- Inspection combined catalog closure enumeration, supported Markdown links,
  entry task tables, topic headings/applicability clauses, native templates,
  role instruction literals and adoption procedure routes. The inventory below
  retains the source paths, sections, selection conditions and route witnesses.
  Section-specific conditions below refine the parent route; grouping never makes
  all sections or all linked files mandatory reading.
- The source check's supported link parser was reused for the temporary route
  enumeration. Native imports, placeholder routes and TOML/code-span paths were
  inspected separately. A graph path is a structural witness; the applicability
  review establishes a plausible task route, not observed client selection.
- This stage does not revalidate every vendor API or rerun executable examples.
  Technology versions and historical evidence keep their original scope. No
  native client trial, consumer installation or independent review ran.

## Ownership and proposed disposition

The existing file/section remains the authoritative owner for every retained
rule. No policy moves into a skill in the first slice. The new design entry adds
an optional route through the project's local facts and applicable profile entry;
existing direct routes remain. Implementation/review entries remain proposals
until their later stage, with the same ownership constraint.

| Route code | Actual entry and condition | Proposed disposition | Evidence |
| --- | --- | --- | --- |
| E | Adapted root policy or project-local entry and passport selects the evidenced stack; then the profile task table selects the topic/section | Retain E; add design-skill selection of the same local entry when a material design task matches | Source inventory and closure checks; native use pending PS-02/05 |
| P | Root entry selects shared policy by task: scope, language, edits, planning, verification, skills, mode or delegation | Retain direct P even when no skill activates; the new guide does not own those procedures | Shared-policy map and template inspection |
| X | E reaches a topic's optional example link when it resolves a specific decision | Retain conditional example and stated version/evidence limits; never promote it to required reading or runtime check | Example callers and section inventory |
| C | Import selection or an existing adopted route names a legacy aggregate ID; aggregate routes to component entries | Retain ID, source path, anchors and resource closure; do not reinterpret it as a narrow profile | All five aliases and existing compatibility tests |
| N | Explicit integration/setup/reassignment or authorized delegation selects the installed native entry/role | Preserve trigger, permissions and path adaptation; workflow skill activation grants none of these actions | Native/adoption maps below |
| H | Evidence/basis section refers to optional historical research, plans or external sources | Retain evidence condition; adapt omitted source-history links during adoption, without copying history into task context | Catalog and MIGRATION contracts |

The proposed workflow profile is optional. Its availability must not turn P's
model/orchestration resources into a reading queue. These resources already occur
in the required closure and are selected by their own task conditions.

## Shared sections and independently triggered conditions

The section index below enumerates all shared-file sections. This table records
their entry conditions and policy owners without repeating their rules.

| Owner/sections | Current route and condition | Proposed route/disposition |
| --- | --- | --- |
| `core.md`: language, scope, external-content authority | Root language/scope summaries and core task rows; language also applies to questions and documentation | P retained independently of every skill |
| `core.md`: responsibilities/data; practical principles; patterns; simple control flow | Core task rows for changed behavior, composition, abstractions or branches | E/P retained; design selects affected concerns only |
| `core.md`: size/cohesion, functions, splitting, naming | Core task rows and root naming/size links when a responsibility changes or code grows | Same owners and policy settings; no skill-specific size quota |
| `core.md`: versions and completion | Version/API question or completion claim; verification is the detailed evidence owner | Same conditional routes; no version upgrade from inventory |
| `work-modes.md`: checkout, direct mode, opt-in mode, integration | Root session policy and delivery when selecting progression or Git actions | P retained; no autonomous mode from a skill trigger |
| `verification.md`: baseline, test selection, cadence/output, reuse, review, completion | Root pre-edit/evidence route and technology verification entries | P retained; wrappers consume the selected gates rather than adding another cycle |
| `delivery-workflow.md`: task contract, techniques, phases, completion | Root planning route and Superpowers adaptations for substantive delivery | Existing task/store remains owner; design result feeds it |
| `superpowers.md`: selection, adaptations, helper compatibility/fallback | Root skill route before the applicable installed procedure | Retain this owner; new guide links here and does not duplicate adaptations |
| `orchestration.md`: roles, scheme, handoff, concurrency, lifecycle, runtime/cost | Root delegation route only for an authorized bounded delegation | No activation from design/coding/review alone |
| `model-configuration.md`: schema/legacy, capabilities, setup, roles, native mapping, repair, runtime, reassignment | Explicit model task, full integration's selection/reuse step, or missing choices needed by authorized delegation | Existing model skills remain distinct N entries |
| `policy-configuration.md` and `policy-defaults.toml` | Root/verification/core routes when cadence, review or size settings matter | Shared assets retained; no generated overrides for ordinary work |
| `catalog.md` and `catalog.toml` | Root profile selection; MIGRATION import assembly or absent-profile decision | Availability owner retained; task-time selection uses local project routes |
| `templates/PLANS.md` and `templates/task.md` | Installed planning policy for substantive tasks; task template only if selected | Canonical progress stays there; no second checklist in skills |
| `superpowers/compatibility.md` | Helper use or an installed-version compatibility question | Conditional reference; its historical 6.4.1/6.4.2 evidence stays dated |

| Section-level boundary | Condition that must survive skill selection | Source route |
| --- | --- | --- |
| Angular architecture subsections | Feature ownership, presentation/dependencies, services/DI and standalone/NgModule composition have separate entry rows | `angular.md`, Read by task |
| Angular verification: SSR/hydration | Only when those rendering modes exist or are affected | `angular/verification.md`, SSR and hydration, when present |
| NgRx state architecture | Library/state choice, Store placement and eager/lazy providers differ; component-local and SignalStore work must not acquire classic Store wiring | `ngrx.md`, Read by task; `ngrx/state-architecture.md` |
| NgRx Entity versus Router Store | Select only the package/subsection actually used; SignalStore alone does not require Router Store | `ngrx/entity-router.md`; `angular/boundaries.md` |
| Doctrine ORM versus DBAL | Mapping/entities/unit of work require ORM; DBAL-only operations select query/transaction contracts | `doctrine.md`; `doctrine/models-mapping.md`; `doctrine/queries-dbal.md` |
| TypeORM plus NestJS | The NestJS integration topic is available with TypeORM but applies only when both technologies exist | `typeorm.md`; `typeorm/nestjs-integration.md` |
| Python integrations | Python alone does not select validation, HTTP, ORM, driver or database rules; SQLAlchemy does not establish a database | `python/execution-resources.md`; component profile entries |
| Browser versus server JavaScript/TypeScript | Tooling that runs on Node does not make browser code a Node server; TypeScript applies only where used | `javascript.md`; `nodejs.md`; `typescript.md` |
| React versus Next.js | React does not imply Next.js; framework routes require actual Next.js; feature restructuring is conditional | `react.md`; `nextjs-framework.md`; `nextjs-feature-structure.md` |
| Container development versus production | Select the actual environment/build/runtime change; no image build merely for a prose or ordinary code edit | `docker.md`; `docker/development-production.md` |
| Unreal source, assets and editor | C++/Blueprint, build/assets, MCP setup/mutation, and checks have distinct triggers; source-only work needs no MCP setup | `unreal-engine.md`, Read for the task |
| Unreal runtime-performance sections | Concurrency, established networking requirements, and measured performance/specialist systems are separately triggered | Three explicit fragment links in `unreal-engine.md` |
| Optional tools and patterns | Example packages, specialized patterns, Unreal/Blender skills and provider setup stay conditional | Applicable topic body; `unreal-engine/skills.md` |
| Evidence and example sections | Basis, run commands, manifests and observed results describe a conditional example or dated evidence, not unconditional project requirements | X/H routes, including code-span research paths |

## Native entries, roles and adoption routes

All 18 template files remain inactive source artifacts. The table includes
templates that MIGRATION selects separately from the catalog resource closure.

| Source template or owner | Trigger and existing route | Availability and proposed disposition |
| --- | --- | --- |
| `templates/AGENTS.root.md` | MIGRATION adapts root project instructions; sections cover language, mode, engineering, project map and task routes | Source installation alternative; keep direct policy/stack routes and add only the selected workflow route in PS-02 |
| `templates/policy-entry.md` | Catalog named `entry` template; equivalent policy sections plus filled project/routes slots | Client alternative; adapt final location, do not activate a duplicate policy owner |
| `templates/AGENTS.project.md` | MIGRATION Phase 3 for a project supplement or independently opened child | Source-selected template; local contracts, checks, task store and reachable profile routes remain |
| `templates/project-architecture.md` | Project facts, dependencies, stack/version evidence, decisions and conditional Unreal sections | Source-selected passport; resolve ordinary task inputs here, not from adoption provenance |
| `templates/workspace-architecture.md` | Multi-project interaction map and scoped project-reading routes | Source-selected passport; local tasks need not read all projects |
| `templates/PLANS.md` | Substantive planning; language, store, contents, progress and resumption sections | Shared asset; adapted active planning policy remains sole progress contract |
| `templates/task.md` | A substantive task when this format is selected | Shared asset; no mandatory template migration for existing native stores |
| `templates/framework/adoption-record.md` | MIGRATION preparation/import/update/recovery | Shared asset; managed paths/accepted contents will include selected native skills; not ordinary task input |
| `templates/framework/model-routing.toml` | Authorized model setup/reassignment or integration selection | Required model-profile resource, inactive unconfigured example; no model writes in workflow selection |
| `templates/codex/README.md` | Model configuration's Codex mapping and setup | Required model-profile resource; explanatory mapping, not an activation claim |
| `templates/codex/config.toml` | Authorized selected native settings | Required model-profile resource; preserve actual pairs and unrelated settings |
| `templates/codex/agents/af-implementer.toml` | Enabled role and allowed edge for authorized bounded implementation | Required model-profile resource; developer-instruction literals resolve from target instruction root |
| `templates/codex/agents/af-reviewer.toml` | Selected independent review under enabled role/edge and permissions | Required model-profile resource; no-edit text is not a verified filesystem restriction |
| `templates/claude/policy-bridge.md` | Selected Claude native entry imports `@AGENTS.md` | Catalog client alternative; inspect native import separately, retain current behavior |
| `templates/cursor/rule-route.mdc` | Selected Cursor route with filled metadata/instructions | Catalog client alternative; placeholders are not valid activated instructions |
| `templates/skills/aek-integrate-project/SKILL.md` | Explicit prepare/import/update request; source MIGRATION owns its procedure | Source-selected integration skill, not a catalog profile resource; preserve source dependency for adoption operations only |
| `templates/skills/aek-model-setup/SKILL.md` | Full integration selection/reuse, explicit setup, or missing choices for authorized delegation | Required model-profile resource; no setup merely because a record is absent |
| `templates/skills/aek-model-reassign/SKILL.md` | Explicit saved client/model/role/scheme change | Required model-profile resource; preserve unspecified choices |
| `MIGRATION.md` | Import inputs, integration entry/name reconciliation, layouts, route adaptation, prepare/apply, model selection, adoption record, B/C/N update, recovery and phases 1–5 | Source procedure owner; ordinary workflow skills must not require this source checkout |
| Source `AGENTS.md`, `ARCHITECTURE.md`, `README.md` | Source maintenance and public navigation | Do not export source AGENTS as a consumer entry; update public claims only when implemented |
| `examples/document-processing-workspace-architecture.md` and historical `docs/` | Illustrations and dated evidence selected for a concrete question | Not native discovery roots or mandatory catalog closure; retain history |

Code-span/native route review covered root `PLANS.md`, selected profile paths,
`.agents-framework/adoption.md`, `.agents-framework/model-routing.toml`, the
three existing skill destinations, TOML developer-instruction paths, and
Claude's import/Cursor's filled instructions. Source model-skill links resolve
three levels up to source standards; their contained Codex installation links
resolve to `../../../.agents-framework/standards/model-configuration.md` from the
skill folder. Flat/custom layouts need their recorded bundle placement. Those
are adaptation contracts, not evidence of installed discovery.

Official [Codex skill documentation](https://learn.chatgpt.com/docs/build-skills),
opened during the preceding analysis on 2026-10-11, documents required name and
description, explicit/implicit selection, and repository `.agents/skills` discovery
from cwd to repository root. Same-name skills are not merged. This supports the
planned path/collision scenarios; the selected actual client still needs its own
observation. No new Claude/Cursor native support is claimed by this inventory.

## Superpowers 6.4.2 composition review

Installed source inspected under
`/home/vitalii/.codex/plugins/cache/openai-curated-remote/superpowers/6.4.2/skills`.
This is the current session's source, not a promised consumer version. Actual tool
schemas and higher-priority instructions control capabilities; the plugin cache
was not changed. The local owner is
[Superpowers integration](../../standards/superpowers.md#explicit-adaptations).

| Candidate/operation | Observed overlap in installed skill | Effective owner and proposed disposition |
| --- | --- | --- |
| Design entry | `brainstorming` discovers intent, classifies design and has approval paths; `writing-plans` produces implementation plans | AEK contributes affected stack/architecture contracts and design output; delivery/planning owners decide artifact depth and material decisions. Reuse satisfied design/approval; no second brainstorming lifecycle |
| Implementation entry | `executing-plans` specifies continuous execution, worktree/helpers, TDD, commits and a final reviewer | Local work modes, canonical plan and verification adaptations replace these defaults. AEK contributes relevant engineering-rule selection; no automatic setup or delegation |
| Review entry | `requesting-code-review` dispatches a reviewer and uses Git SHAs | AEK review output is located findings against the actual stage baseline, including untracked files. Verification selects independence; orchestration controls an authorized dispatch. Review invocation itself is not permission to fix or spawn |
| Skill authoring | `writing-skills` prescribes failing behavioral baselines, pressure/micro-tests, helper checklists and commit/push | Use skill-creator and writing-skills in PS-02 under local format/behavior and proportionate-verification rules; retain required PS-02/05 native observations, without importing universal repetition or Git recipes |
| Evidence | `verification-before-completion` demands new command output before claims | Existing verification owner permits valid unchanged evidence to be reused and still requires actual acceptance evidence; a new turn does not invalidate results |
| Canonical artifacts | Upstream plans/helpers describe `docs/superpowers/` and a separate ledger | Adopted PLANS and current task store remain authoritative; no new ledger solely for helper compatibility |
| Language | Upstream examples and handoff prompts are English | Agent-facing artifacts are English; user-facing communication is Russian in this task |
| Model/delegation | `using-superpowers` Codex reference gives spawn/default-model recipes; its full-history override description differs from this session's exposed schema | Native schema, saved choices and local orchestration win. No model reassignment, worker launch or global configuration follows from reading a procedure |
| Missing plugin/helper | A wrapper could otherwise fail or attempt installation | Existing direct scoped-task fallback remains; no-skill direct mandatory routes survive |

Proposed trigger/output boundaries:

- `aek-design-feature`: material capability/boundary/contract design; resolve local
  architecture and applicable technical topics, then record owners, dependencies,
  interfaces, alternatives and relevant acceptance evidence in the canonical task.
  A typo, review-only request or already approved implementation does not restart design.
- `aek-implement-feature`: authorized change with sufficient criteria/design;
  select affected technical rules and checks, preserve stage/baseline, implement
  and report actual acceptance. A small fix does not acquire an architecture phase.
- `aek-review-changes`: requested/applicable review with task, baseline and actual
  changes; select affected contracts and return consequential findings plus limits.
  Running the skill in the coordinator is not an independent second opinion.

These are candidate routing benefits to test, not proof that three wrappers are
necessary. The earlier pilot established success with existing routes. Retain,
simplify or omit a candidate according to its observed distinct value.

## Findings and dispositions

| ID | Observation and consequence | Disposition for continuation |
| --- | --- | --- |
| F01 | Five legacy aggregates have no incoming Markdown link in operational source/template files; a link-only orphan scan would misclassify them | Resolved as C routes: explicit catalog selection/retained adopted entry supplies their entry; retain IDs/anchors/closures |
| F02 | `ARCHITECTURE.md` still lists conceptual `aek-design-change` and `aek-deliver-phase`; these overlap proposed feature entries | Treat as conceptual predecessors, not extra skills. Reconcile design naming when PS-02 updates actual architecture; resolve delivery naming in PS-03. No native alias migration is needed for concepts that were never installed |
| F03 | Source Markdown success does not cover installed skill metadata, code-span imports, adapted native destinations or model adherence | Keep explicit native-path/format checks and actual client gates; do not infer success from the existing checker |
| F04 | Conditional cross-profile references can point outside a minimal bundle; availability alone cannot decide their applicability | Preserve the catalog/MIGRATION adaptation procedure and named negative scenarios below; target closure remains a PS-02/04 check |
| F05 | Superpowers stock defaults differ from local stage, Git, tests, model and progress policies | Effective ownership is already settled by local adaptations; test composition in PS-02/05 and keep wrappers free of copied lifecycle rules |
| F06 | Previous successful pilot used already-loaded context and the old packaging | Retain only historical evidence; freeze a new control/candidate task before testing the new slice |
| F07 | Model skills are required-profile resources, whereas the integration skill is source-selected separately | Preserve that packaging distinction; everyday design/coding/review must work without source MIGRATION or model onboarding |

No active source topic remains without an inventory disposition or plausible
entry route. This closes the before-state mapping only. It does not close AC02's
after-state preservation, target installation or behavioral criteria. No unresolved
owner conflict prevents preparing the first slice; client execution inputs remain
prerequisites for its behavioral acceptance.

## Bounded PS-02 manifest

The first slice adds only `aek-design-feature`. Proposed profile:
`project-workflows`, source `standards/project-skills.md`, dependency `core`,
activity `design`, resources containing only the design skill template initially.
No technology dependency or filename glob is needed. The seven existing required
profiles remain available through the unchanged assembly contract.

| Planned source path | Bounded responsibility |
| --- | --- |
| `standards/project-skills.md` | Selection, local project-input resolution and output boundaries; route process decisions to existing owners |
| `templates/skills/aek-design-feature/SKILL.md` | Name/description, design/non-trigger cases, local rule selection and canonical design result; no duplicated language guides |
| `standards/catalog.toml`, `standards/catalog.md` | Optional profile containing only existing slice files; preserve schema 1 and all old IDs |
| `templates/AGENTS.root.md`, `templates/policy-entry.md` | Conditional route to the selected installed design skill; direct rules remain usable |
| `MIGRATION.md` | Selection and final-location adaptation for this slice using existing preparation/apply/recovery procedure |
| `ARCHITECTURE.md`, `README.md` | Describe actual slice/status and reconcile the conceptual design predecessor without advertising later skills |
| `tests/test_profile_selection.py`, `tests/test_instruction_artifacts.py` | Focused closure, omitted-profile, final-location/reference and broken-required-route cases |
| `docs/research/2026-10-11-project-skills-validation.md` | Durable fixture inputs, expected outputs, identities, client observations and evidence limits |
| Canonical plan and this inventory | Progress and observations respectively; update before/after routes without a second checklist |

Do not expand the checker just to create a new production installer or generic
semantic validator. If a deterministic metadata/support-file gap requires checker
code, bound it explicitly, preserve existing CLI/schema behavior and add the
documented strict analyzer to its acceptance. Additional source paths need their
baseline captured before editing. Implementation/review templates and broad
adoption-record/recovery expansion belong to PS-03/04.

First target proposal: a disposable, independently opened Codex project with a
contained `.agents-framework` bundle, selected Python/Pydantic/FastAPI profiles,
root policy, project architecture and one canonical task. Its native candidate is
`.agents/skills/aek-design-feature/SKILL.md`; referenced rules resolve from that
final folder. Existing setup/model templates remain inactive. This is a proposed
fixture shape, not a claim that a client/version or execution envelope is selected.

Proposed design case: extend an in-memory reservation service with idempotent
cancellation under its existing lock. Expected design identifies transport input
and errors, one state-transition owner, concurrency/idempotency boundaries, the
existing resource lifetime and focused acceptance checks. It must preserve the
selected storage model and avoid a new database/queue. A control and candidate
must start from identical retained inputs and fresh contexts; the old pilot's
answer is not supplied as task input. A README typo is the unrelated counterexample;
a small already-specified fix must not start a new architecture workflow.

Before the first native run, record the actual client/version, exposed model and
settings, fixture location and permitted bounded calls. Observe explicit and
implicit selection, actual relevant reading/output, and operation with source
unavailable. Missing observations leave PS-02 open. Later PS-05 extends the matrix
to implementation/review and plugin-absent behavior; no result is claimed now.

Representative static target selections for subsequent stages are Python/FastAPI,
browser React/TypeScript without Node/Next.js, Angular without NgRx, Angular with
NgRx, and Go or Unreal without web profiles. For the first slice, verify that
workflow-only selection adds no stack and a selected-stack bundle adds only its
closure. Keep source and installed checks separate; explicit native-file arguments
replace the checker body selection and do not replace a full selected-bundle scan.

## Evidence and reproduction

The preceding analysis in this conversation ran the baseline commands below on
the same clean tracked HEAD. This stage compared tracked input identities before
reusing those results; only the canonical plan and this research record change.
Defaults are `verification.timing = phase_end` and `review.independent = risk_based`.
Coordinator review is sufficient for this non-operational inventory stage; no
independent review is claimed.

| Evidence | Actual result and limit |
| --- | --- |
| `python3 tools/check_instruction_artifacts.py` | 206 artifacts, zero errors; unchanged operational source, supported syntax/catalog only |
| Scoped checker on spec, plan, earlier roadmap and feasibility note | Four documents, zero errors in the preceding analysis; changed plan needs the stage's scoped recheck |
| `python3 -m unittest discover -s tests -p 'test_instruction_artifacts.py'` | 40 tests passed; no checker/test changes since that run |
| `python3 -m unittest discover -s tests -p 'test_profile_selection.py'` | 31 tests passed, including independent/combined stack and legacy path/anchor cases |
| All 35 profile closures including required profiles/assets | All declared closure files exist; counts retained below. This is not 35 prepared target or native-client runs |
| Source route enumeration and manual condition review | All 182 standards have availability and a route/disposition; 833 heading identities retained below; no unmapped standards file |
| Native literal/template inspection | Three skill templates, two role files, entry alternatives, task/passport/adoption paths inspected; actual native discovery remains unobserved |

Baseline input-set SHA-256:
`90da2cba05c19c42e63f50bab3836205285f72cca3dc15fda489e98ff73693e9`.
It covers 209 paths: sorted `.md`/`.mdc`/`.toml` files under standards/templates,
then checker, two test modules, AGENTS, ARCHITECTURE, README and MIGRATION in that
order. Hash input is UTF-8 records of path, NUL, file SHA-256 and newline. This
identity records what the reused checks cover; it is not a signature or a client
runtime identity. The source commit plus this description reproduces that set.

The profile and section tables below are dated observations. Reproduce their
coverage by parsing schema-1 catalog sources/resources/assets, enumerating all
standards Markdown files, extracting headings outside code fences with the
existing checker's heading rules, and comparing the sets. Start each closure with
the seven required IDs plus its selected ID; follow declared dependencies to a
fixed point and deduplicate sources/resources/assets. Named client-entry alternatives
are separate from the closure file counts. Review task-table conditions and native
literals manually; do not treat graph reachability as semantic or client proof.

Stage-end scoped checks and actual diff review are recorded in the canonical plan.
Historical pilot/runtime results have not been relabelled as new-skill evidence.

## Profile availability inventory

R denotes the seven required profiles: `core`, `delivery-workflow`, `model-configuration`, `orchestration`, `superpowers`, `verification`, `work-modes`.
Each row preserves its source path and ID. The added-closure column excludes R
and the row ID itself. Counts include shared assets and deduplicated profile
sources/resources, excluding separately selected client-entry alternatives.

| ID / owner entry | Selection condition | Dependencies / additional closure beyond R | Files | Disposition |
| --- | --- | --- | --- | --- |
| [core](../../standards/core.md) | Changing behavior, architecture, or code structure; read the relevant sections only. | work-modes, verification, delivery-workflow / none | 22 | P retained |
| [work-modes](../../standards/work-modes.md) | Selecting work mode, stage boundaries, repository scope, or Git actions. | none / none | 22 | P retained |
| [verification](../../standards/verification.md) | Before editing, selecting checks, reviewing, or claiming completion. | none / none | 22 | P retained |
| [delivery-workflow](../../standards/delivery-workflow.md) | Choosing phases, planning artifacts, or a delivery workflow. | superpowers / none | 22 | P retained |
| [superpowers](../../standards/superpowers.md) | Applying an available Superpowers skill; this policy does not install the plugin. | orchestration / none | 22 | P retained |
| [orchestration](../../standards/orchestration.md) | Delegating a bounded task under the saved role choices and task authorization. | model-configuration / none | 22 | P retained |
| [model-configuration](../../standards/model-configuration.md) | Integration model selection/reuse, authorized setup, explicit reassignment, or relevant configuration repair. | none / none | 22 | P retained |
| [python-fastapi](../../standards/python-fastapi.md) | Compatibility aggregate for existing or explicitly requested selections; new imports select component profiles separately. | python, pydantic, fastapi / fastapi, pydantic, python | 44 | C retained |
| [python](../../standards/python.md) | Python language, contracts, resources, tooling, or runtime work. | core / none | 29 | E retained |
| [pydantic](../../standards/pydantic.md) | Pydantic validation, serialization, schemas, model lifetime, or integration; only where Pydantic is used. | python / python | 36 | E retained |
| [fastapi](../../standards/fastapi.md) | FastAPI HTTP contracts, dependency lifetime, runtime, or integration; only where FastAPI is used. | python, pydantic / pydantic, python | 43 | E retained |
| [php-symfony-doctrine](../../standards/php-symfony-doctrine.md) | Compatibility aggregate for existing or explicitly requested selections; new imports select component profiles separately. | php, symfony, doctrine / doctrine, php, symfony | 44 | C retained |
| [php](../../standards/php.md) | PHP work; Symfony and Doctrine are separate selections. | core / none | 29 | E retained |
| [symfony](../../standards/symfony.md) | Symfony components are declared or used; Doctrine is selected separately when used. | php / php | 36 | E retained |
| [doctrine](../../standards/doctrine.md) | Doctrine ORM or DBAL is declared or used; ORM guidance is conditional and Symfony is not implied. | php / php | 36 | E retained |
| [go-gin](../../standards/go-gin.md) | Compatibility aggregate for existing or explicitly requested selections; new imports select component profiles separately. | go, gin / gin, go | 39 | C retained |
| [go](../../standards/go.md) | Go work; Gin is selected separately when used. | core / none | 31 | E retained |
| [gin](../../standards/gin.md) | Gin is declared or used; include Go language rules and relevant Gin topics. | go / go | 38 | E retained |
| [nodejs-typescript](../../standards/nodejs-typescript.md) | Compatibility aggregate for existing or explicitly requested selections; new imports select component profiles separately. | javascript, nodejs / javascript, nodejs | 37 | C retained |
| [javascript](../../standards/javascript.md) | JavaScript language, modules, contracts or effects across hosts. | core / none | 29 | E retained |
| [nodejs](../../standards/nodejs.md) | Node.js host runtime, services, workers, tools or CLI work; not browser code merely using Node-based tooling. | javascript / javascript | 36 | E retained |
| [typescript](../../standards/typescript.md) | TypeScript contracts, validation, or code changes. | javascript / javascript | 36 | E retained |
| [nestjs](../../standards/nestjs.md) | NestJS modules, providers, controllers, or validation boundaries. | nodejs, typescript / javascript, nodejs, typescript | 50 | E retained |
| [typeorm](../../standards/typeorm.md) | TypeORM is declared or used: rich entities, persistence, queries or migrations; NestJS alone does not select this profile. | typescript / javascript, typescript | 43 | E retained |
| [angular](../../standards/angular.md) | Angular is declared or used: components, templates, DI, routes, forms, reactivity or styles; TypeScript/HTML alone does not select this profile. | typescript / javascript, typescript | 44 | E retained |
| [ngrx](../../standards/ngrx.md) | An NgRx package is used or explicitly selected; read only relevant Store/Effects/Entity/Router Store/Signals/ComponentStore guidance, not from Angular alone. | angular / angular, javascript, typescript | 53 | E retained |
| [nextjs](../../standards/nextjs.md) | Compatibility aggregate for existing or explicitly requested selections; new imports select component profiles separately. | nextjs-framework, typescript, nodejs / javascript, nextjs-framework, nodejs, react, typescript | 62 | C retained |
| [react](../../standards/react.md) | React components, state, effects, forms, rendering or integration; not every JSX/TSX file. | javascript / javascript | 37 | E retained |
| [nextjs-framework](../../standards/nextjs-framework.md) | Next.js routes, Server/Client boundaries, caches, rendering or deployment; only where Next.js is used. | react / javascript, react | 46 | E retained |
| [nextjs-feature-structure](../../standards/nextjs-feature-structure.md) | Organizing or reviewing frontend feature boundaries; no mandatory restructuring for small fixes. | nextjs-framework / javascript, nextjs-framework, react | 46 | E retained |
| [sqlalchemy](../../standards/sqlalchemy.md) | SQLAlchemy Core/ORM mappings, queries, sessions, engines, or persistence integration; not every Python task. | python / python | 37 | E retained |
| [psycopg](../../standards/psycopg.md) | Psycopg 3 SQL, adaptation, connection, transaction, async or pool integration; not every Python/PostgreSQL task. | python, postgresql / postgresql, python | 44 | E retained |
| [postgresql](../../standards/postgresql.md) | PostgreSQL schema, query, transaction, or persistence changes. | core / none | 30 | E retained |
| [docker](../../standards/docker.md) | Changing container builds or their runtime contract; an ordinary code edit does not require an image build. | core / none | 31 | E retained |
| [unreal-engine](../../standards/unreal-engine.md) | Declared or evidenced Unreal project/plugin work; read only task-relevant sections. Generic C++ or Python files alone do not select Unreal; source-only work does not require MCP. | core / none | 30 | E retained |

## File and section disposition inventory

One row covers one file owner. Every source heading is listed with its baseline
line; preamble applicability applies before its sections. Current-route cells name
a real entry/topic and its selection condition. Proposed routes retain that owner
and those conditions under the codes above. Evidence for each row is V01 source
inspection plus V02 resource/link checks; native activation and after-state
preservation are pending later stages. Basis/evidence sections are H even inside
an E/P owner. File names inside examples are X, not additional active rules.

### Shared policy and catalog

| Owner file and baseline sections | Availability | Current route and task condition | Proposed disposition |
| --- | --- | --- | --- |
| [standards/catalog.md](../../standards/catalog.md) — 1: Rule catalog: bundling and reading; 8: Field meanings; 32: Assemble a portable bundle; 79: Independent and legacy selections; 113: Read for the current task | shared asset | [standards/policy-configuration.md:62](../../standards/policy-configuration.md#schema-version-1) — relevant Schema version 1 subsection | P retained |
| [standards/core.md](../../standards/core.md) — 1: Core engineering standard; 6: Read by task; 25: Reasoning and communication language; 52: Task scope and context; 69: External content and instruction authority; 87: Responsibilities and data; 123: Practical SOLID, DRY, KISS, and YAGNI; 159: Patterns when a concrete problem warrants them; 180: Simple control flow; 203: Size and cohesion; 233: Small methods and functions; 254: Splitting classes and modules; 288: Names and evolving responsibilities; 352: Versions and documentation; 360: Sufficient evidence and completion | core | Adapted root/project stack route; Changing behavior, architecture, or code structure; read the relevant sections only. | P retained |
| [standards/delivery-workflow.md](../../standards/delivery-workflow.md) — 1: Delivery: specifications, phases, and evidence; 8: Minimal task contract; 32: Delivery techniques; 45: Phase boundaries; 62: Phase completion; 84: Sources | delivery-workflow | Adapted root/project stack route; Choosing phases, planning artifacts, or a delivery workflow. | P retained |
| [standards/model-configuration.md](../../standards/model-configuration.md) — 1: Workspace model setup and reassignment; 11: Scope and source of truth; 40: Routing format version 2; 97: Legacy records and unknown versions; 113: Catalog and capability validation; 124: First-use behavior; 166: Role enablement and native agreement; 186: Role scope and native restrictions; 214: Mapping to native Codex files; 241: Mapping to native Claude Code files; 255: Mapping to native Cursor files; 269: Preview, apply, and repair; 284: Saved selection versus active execution; 296: Reassignment; 306: Validation and sources | model-configuration | Adapted root/project stack route; Integration model selection/reuse, authorized setup, explicit reassignment, or relevant configuration repair. | P retained |
| [standards/orchestration.md](../../standards/orchestration.md) — 1: Orchestration and configurable model roles; 19: Responsibilities; 39: Editable schemes; 70: Delegation contract; 125: Concurrency and isolation; 141: Worker lifecycle and continuations; 171: Runtime behavior; 193: Cost; 206: Sources | orchestration | Adapted root/project stack route; Delegating a bounded task under the saved role choices and task authorization. | P retained |
| [standards/policy-configuration.md](../../standards/policy-configuration.md) — 1: Project policy settings; 10: Locations and resolution; 36: Schema version 1; 73: Legacy and incomplete adoption; 86: Validation and evidence limits | shared asset | [standards/core.md:205](../../standards/core.md#size-and-cohesion) — relevant Size and cohesion subsection | P retained |
| [standards/superpowers.md](../../standards/superpowers.md) — 1: Superpowers integration; 7: Discovery and authority; 20: Skill selection; 42: Explicit adaptations; 87: Plans and helper compatibility | superpowers | Adapted root/project stack route; Applying an available Superpowers skill; this policy does not install the plugin. | P retained |
| [standards/superpowers/compatibility.md](../../standards/superpowers/compatibility.md) — 1: Superpowers helper compatibility; 8: Helper contracts: inspected 6.4.1 and 6.4.2; 68: Local 6.4.2 inspection — 2026-09-26; 88: Historical 6.4.1 evidence — 2026-09-20 | superpowers | [standards/superpowers.md:93](../../standards/superpowers.md#plans-and-helper-compatibility) — relevant Plans and helper compatibility subsection | H/helper reference retained |
| [standards/verification.md](../../standards/verification.md) — 1: Proportionate tests, verification, and review; 9: Before implementation; 29: When to add tests; 51: What to run, and when; 103: Compact check output; 117: Reuse evidence before repeating work; 149: Review boundaries; 200: Codex review entry points; 218: Completion and lack of progress; 233: Source and policy boundary | verification | Adapted root/project stack route; Before editing, selecting checks, reviewing, or claiming completion. | P retained |
| [standards/work-modes.md](../../standards/work-modes.md) — 1: Working directory, checkpoints, and Git actions; 7: Workspace root and project checkouts; 32: Default: direct work with human checkpoints; 66: Explicit opt-in: autonomous worktree execution; 108: Worktree completion: offer merge, then clean up; 139: Unambiguous task examples; 153: Skills and evidence | work-modes | Adapted root/project stack route; Selecting work mode, stage boundaries, repository scope, or Git actions. | P retained |

### Technology entries

| Owner file and baseline sections | Availability | Current route and task condition | Proposed disposition |
| --- | --- | --- | --- |
| [standards/angular.md](../../standards/angular.md) — 1: Angular; 7: Establish the project contract; 15: Essential rules; 34: Read by task; 52: Basis | angular | Adapted root/project stack route; Angular is declared or used: components, templates, DI, routes, forms, reactivity or styles; TypeScript/HTML alone does not select this profile. | E retained; optional design route |
| [standards/docker.md](../../standards/docker.md) — 1: Docker build and runtime boundaries; 7: Essential rules; 22: Read for the task; 35: Basis | docker | Adapted root/project stack route; Changing container builds or their runtime contract; an ordinary code edit does not require an image build. | E retained; optional design route |
| [standards/doctrine.md](../../standards/doctrine.md) — 1: Doctrine ORM / DBAL; 9: Doctrine essentials; 23: Read by task; 36: Basis | doctrine | Adapted root/project stack route; Doctrine ORM or DBAL is declared or used; ORM guidance is conditional and Symfony is not implied. | E retained; optional design route |
| [standards/fastapi.md](../../standards/fastapi.md) — 1: FastAPI; 9: FastAPI essentials; 20: Read by task; 32: Evidence | fastapi | Adapted root/project stack route; FastAPI HTTP contracts, dependency lifetime, runtime, or integration; only where FastAPI is used. | E retained; optional design route |
| [standards/gin.md](../../standards/gin.md) — 1: Gin; 7: Gin essentials; 17: Read by task; 29: Evidence | gin | Adapted root/project stack route; Gin is declared or used; include Go language rules and relevant Gin topics. | E retained; optional design route |
| [standards/go-gin.md](../../standards/go-gin.md) — 1: Go / Gin; 7: Essential guidance; 11: Read by task; 17: Gin essentials; 21: Evidence | go-gin | Adapted root/project stack route; explicit legacy ID go-gin | C retained |
| [standards/go.md](../../standards/go.md) — 1: Go; 7: Essential guidance; 23: Read by task; 36: Evidence | go | Adapted root/project stack route; Go work; Gin is selected separately when used. | E retained; optional design route |
| [standards/javascript.md](../../standards/javascript.md) — 1: JavaScript; 9: Versions and modules; 20: Read by task; 29: Typed boundaries; 46: Verification; 53: Basis | javascript | Adapted root/project stack route; JavaScript language, modules, contracts or effects across hosts. | E retained; optional design route |
| [standards/nestjs.md](../../standards/nestjs.md) — 1: NestJS; 8: Establish the executable contract; 15: Essential boundaries; 31: Read by task; 41: Verification; 51: Basis | nestjs | Adapted root/project stack route; NestJS modules, providers, controllers, or validation boundaries. | E retained; optional design route |
| [standards/nextjs-feature-structure.md](../../standards/nextjs-feature-structure.md) — 1: Organizing a Next.js frontend by features; 8: Compact product-capability structure; 62: Migrating from an existing structure; 77: Router adapters and execution contracts; 97: Architecture decisions to record; 105: Basis and choice | nextjs-framework, nextjs-feature-structure | Adapted root/project stack route; Organizing or reviewing frontend feature boundaries; no mandatory restructuring for small fixes. | E retained; optional design route |
| [standards/nextjs-framework.md](../../standards/nextjs-framework.md) — 1: Next.js; 11: Versions and runtime boundaries; 22: Read by task; 36: Basis | nextjs-framework | Adapted root/project stack route; Next.js routes, Server/Client boundaries, caches, rendering or deployment; only where Next.js is used. | E retained; optional design route |
| [standards/nextjs.md](../../standards/nextjs.md) — 1: Next.js / React; 10: Essential React rules; 14: Read by task; 19: Next.js only: versions and task routes; 24: Basis | nextjs | Adapted root/project stack route; explicit legacy ID nextjs | C retained |
| [standards/ngrx.md](../../standards/ngrx.md) — 1: NgRx; 8: Essential contract; 25: Read by task | ngrx | Adapted root/project stack route; An NgRx package is used or explicitly selected; read only relevant Store/Effects/Entity/Router Store/Signals/ComponentStore guidance, not from Angular alone. | E retained; optional design route |
| [standards/nodejs-typescript.md](../../standards/nodejs-typescript.md) — 1: Node.js / JavaScript / TypeScript; 9: Versions and modules; 15: Read by task; 21: Typed boundaries; 27: Server execution and responsibility; 32: Verification; 37: Basis | nodejs-typescript, nextjs | Adapted root/project stack route; explicit legacy ID nodejs-typescript | C retained |
| [standards/nodejs.md](../../standards/nodejs.md) — 1: Node.js; 9: Versions and modules; 16: Read by task; 25: Server execution and responsibility; 31: Verification; 37: Basis | nodejs | Adapted root/project stack route; Node.js host runtime, services, workers, tools or CLI work; not browser code merely using Node-based tooling. | E retained; optional design route |
| [standards/php-symfony-doctrine.md](../../standards/php-symfony-doctrine.md) — 1: PHP / Symfony / Doctrine; 8: PHP essentials; 12: Read by task; 18: Symfony essentials; 22: Doctrine essentials; 27: Framework integration during file moves; 34: Basis | php-symfony-doctrine | Adapted root/project stack route; explicit legacy ID php-symfony-doctrine | C retained |
| [standards/php.md](../../standards/php.md) — 1: PHP; 7: PHP essentials; 18: Read by task; 32: Basis | php | Adapted root/project stack route; PHP work; Symfony and Doctrine are separate selections. | E retained; optional design route |
| [standards/postgresql.md](../../standards/postgresql.md) — 1: PostgreSQL; 7: Essential rules; 21: Read for the task; 39: Basis and compatibility | postgresql | Adapted root/project stack route; PostgreSQL schema, query, transaction, or persistence changes. | E retained; optional design route |
| [standards/psycopg.md](../../standards/psycopg.md) — 1: psycopg; 8: Essential rules; 21: Read for the task; 33: Basis | psycopg | Adapted root/project stack route; Psycopg 3 SQL, adaptation, connection, transaction, async or pool integration; not every Python/PostgreSQL task. | E retained; optional design route |
| [standards/pydantic.md](../../standards/pydantic.md) — 1: Pydantic; 9: Pydantic essentials; 20: Read by task; 32: Evidence | pydantic | Adapted root/project stack route; Pydantic validation, serialization, schemas, model lifetime, or integration; only where Pydantic is used. | E retained; optional design route |
| [standards/python-fastapi.md](../../standards/python-fastapi.md) — 1: Python / FastAPI; 8: Essential guidance; 12: Read by task; 18: Pydantic essentials; 22: FastAPI essentials; 26: Evidence | python-fastapi | Adapted root/project stack route; explicit legacy ID python-fastapi | C retained |
| [standards/python.md](../../standards/python.md) — 1: Python; 8: Essential guidance; 22: Read by task; 34: Evidence | python | Adapted root/project stack route; Python language, contracts, resources, tooling, or runtime work. | E retained; optional design route |
| [standards/react.md](../../standards/react.md) — 1: React; 11: Essential React rules; 22: Read by task; 32: Basis | react | Adapted root/project stack route; React components, state, effects, forms, rendering or integration; not every JSX/TSX file. | E retained; optional design route |
| [standards/sqlalchemy.md](../../standards/sqlalchemy.md) — 1: SQLAlchemy; 8: Essential rules; 25: Read for the task; 39: Basis and compatibility | sqlalchemy | Adapted root/project stack route; SQLAlchemy Core/ORM mappings, queries, sessions, engines, or persistence integration; not every Python task. | E retained; optional design route |
| [standards/symfony.md](../../standards/symfony.md) — 1: Symfony; 9: Symfony essentials; 19: Read by task; 32: Basis | symfony | Adapted root/project stack route; Symfony components are declared or used; Doctrine is selected separately when used. | E retained; optional design route |
| [standards/typeorm.md](../../standards/typeorm.md) — 1: TypeORM; 10: Essential contract; 29: Read by task; 39: Basis | typeorm | Adapted root/project stack route; TypeORM is declared or used: rich entities, persistence, queries or migrations; NestJS alone does not select this profile. | E retained; optional design route |
| [standards/typescript.md](../../standards/typescript.md) — 1: TypeScript: strict types and interfaces; 12: Mandatory rules; 30: Read by task; 39: External data; 54: Enforceability; 67: Basis | typescript | Adapted root/project stack route; TypeScript contracts, validation, or code changes. | E retained; optional design route |
| [standards/unreal-engine.md](../../standards/unreal-engine.md) — 1: Unreal Engine engineering and editor workflow; 15: Context and essential rules; 36: Read for the task; 61: Version and evidence boundary | unreal-engine | Adapted root/project stack route; Declared or evidenced Unreal project/plugin work; read only task-relevant sections. Generic C++ or Python files alone do not select Unreal; source-only work does not require MCP. | E retained; optional design route |

### Technology topics and conditional examples

| Owner file and baseline sections | Availability | Current route and task condition | Proposed disposition |
| --- | --- | --- | --- |
| [standards/angular/architecture.md](../../standards/angular/architecture.md) — 1: Angular architecture and composition; 6: Feature ownership; 65: Pages, components and layouts; 90: Dependency direction; 112: Services, stores and dependency injection; 130: Standalone and NgModules | angular | [standards/angular.md:38](../../standards/angular.md#read-by-task) — Folder structure, application sections, nested domains or feature ownership; [standards/angular.md:39](../../standards/angular.md#read-by-task) — Pages, components, layouts or allowed imports; [standards/angular.md:40](../../standards/angular.md#read-by-task) — Services or provider scope; [standards/angular.md:41](../../standards/angular.md#read-by-task) — Standalone or NgModule composition | E retained; optional design route |
| [standards/angular/boundaries.md](../../standards/angular/boundaries.md) — 1: Angular routes, forms and external boundaries; 5: Routing; 23: Forms and component contracts; 55: Transport and trust | angular | [standards/angular.md:44](../../standards/angular.md#read-by-task) — Route state, forms, validation, HTTP contracts or security | E retained; optional design route |
| [standards/angular/change-detection.md](../../standards/angular/change-detection.md) — 1: Angular change detection and performance; 6: OnPush is a notification contract; 29: Zoneless and ZoneJS; 47: Reduce work and preserve identity | angular | [standards/angular.md:43](../../standards/angular.md#read-by-task) — OnPush, zoneless, rendering cost, tracking or lazy views | E retained; optional design route |
| [standards/angular/examples/application-structure.md](../../standards/angular/examples/application-structure.md) — 1: Example: Angular application sections and state ownership; 9: Sections, pages and domain components; 84: Optional NgRx state placement; 150: Placement and interaction scenarios; 185: Evidence boundary | angular | [standards/angular.md:49](../../standards/angular.md#read-by-task) — relevant Read by task subsection; optional example when needed | X retained; H evidence |
| [standards/angular/reactivity.md](../../standards/angular/reactivity.md) — 1: Angular reactivity and state ownership; 6: Signals and derived state; 24: Observable flow and subscriptions; 44: Requests and cache ownership | angular | [standards/angular.md:42](../../standards/angular.md#read-by-task) — Local state, signals, Observable ownership, subscriptions or HTTP races | E retained; optional design route |
| [standards/angular/styles.md](../../standards/angular/styles.md) — 1: Angular styles and presentation boundaries | angular | [standards/angular.md:45](../../standards/angular.md#read-by-task) — Component styles, global tokens, themes or encapsulation | E retained; optional design route |
| [standards/angular/verification.md](../../standards/angular/verification.md) — 1: Angular verification and compatibility; 7: Version and build contract; 19: Choose evidence by the changed contract; 44: SSR and hydration, when present | angular | [standards/angular.md:46](../../standards/angular.md#read-by-task) — Builds, tests, SSR, compatibility or performance evidence | E retained; optional design route |
| [standards/docker/build-context.md](../../standards/docker/build-context.md) — 1: Build and context; 6: Inputs and stages; 25: Secrets and cache | docker | [standards/docker.md:29](../../standards/docker.md#read-for-the-task) — Dockerfile, context, base/dependencies, stages, secrets or cache | E retained; optional design route |
| [standards/docker/compose-integration.md](../../standards/docker/compose-integration.md) — 1: Compose and integration; 10: Configuration and dependencies; 33: Network and storage | docker | [standards/docker.md:31](../../standards/docker.md#read-for-the-task) — Compose configuration, service dependencies, networks, mounts or durable data | E retained; optional design route |
| [standards/docker/development-production.md](../../standards/docker/development-production.md) — 1: Docker development and production; 7: Choose the environment contract; 21: Development loop; 46: Compose file composition; 61: Production operation | docker | [standards/docker.md:32](../../standards/docker.md#read-for-the-task) — Local dev loop, Watch/bind mounts, environment overrides or production Compose | E retained; optional design route |
| [standards/docker/examples/build-secret.md](../../standards/docker/examples/build-secret.md) — 1: Build-secret fragment; 8: Dockerfile fragment | docker | [standards/docker/build-context.md:40](../../standards/docker/build-context.md#secrets-and-cache) — relevant Secrets and cache subsection; optional example when needed | X retained; H evidence |
| [standards/docker/examples/compose-contract.md](../../standards/docker/examples/compose-contract.md) — 1: Local Compose contract; 9: compose.yaml | docker | [standards/docker/compose-integration.md:48](../../standards/docker/compose-integration.md#network-and-storage) — relevant Network and storage subsection; optional example when needed | X retained; H evidence |
| [standards/docker/examples/development-production.md](../../standards/docker/examples/development-production.md) — 1: Explicit development and production Compose contracts; 12: Image recipe; 75: Neutral base: compose.yaml; 133: Development addition: compose.dev.yaml; 165: Production addition: compose.production.yaml; 208: Commands and evidence boundaries | docker | [standards/docker/development-production.md:93](../../standards/docker/development-production.md#production-operation) — relevant Production operation subsection; optional example when needed | X retained; H evidence |
| [standards/docker/runtime-lifetime.md](../../standards/docker/runtime-lifetime.md) — 1: Runtime and lifetime; 6: Process ownership; 22: Privilege and operations | docker | [standards/docker.md:30](../../standards/docker.md#read-for-the-task) — Command, user, permissions, signals, shutdown, probes or resource limits | E retained; optional design route |
| [standards/docker/verification-compatibility.md](../../standards/docker/verification-compatibility.md) — 1: Verification and compatibility; 6: Check the affected contract; 28: Version and migration boundaries | docker | [standards/docker.md:33](../../standards/docker.md#read-for-the-task) — Tool versions, migration, platform support or choosing checks | E retained; optional design route |
| [standards/doctrine/examples/dbal-reservation.md](../../standards/doctrine/examples/dbal-reservation.md) — 1: Example: a DBAL reservation with one transaction owner; 24: Files; 26: composer.json; 53: src/ReservationOutcome.php; 69: src/StockReservations.php; 146: tests/run.php; 220: Run and check | doctrine | [standards/doctrine/queries-dbal.md:56](../../standards/doctrine/queries-dbal.md#dbal-transactions) — relevant DBAL transactions subsection; optional example when needed | X retained; H evidence |
| [standards/doctrine/examples/orm-unit-of-work.md](../../standards/doctrine/examples/orm-unit-of-work.md) — 1: Example: ORM persistence and failed units of work; 21: Files; 23: composer.json; 51: src/StockItem.php; 107: tests/run.php; 257: Run and check | doctrine | [standards/doctrine/models-mapping.md:103](../../standards/doctrine/models-mapping.md#association-ownership-and-lifetime) — relevant Association ownership and lifetime subsection; optional example when needed | X retained; H evidence |
| [standards/doctrine/models-mapping.md](../../standards/doctrine/models-mapping.md) — 1: Doctrine ORM models and mapping; 7: Domain model placement; 43: Repositories and construction; 61: Mapping and contracts; 80: Association ownership and lifetime | doctrine | [standards/doctrine.md:27](../../standards/doctrine.md#read-by-task) — Doctrine ORM entities, repositories, model placement, mapping or associations | E retained; optional design route |
| [standards/doctrine/queries-dbal.md](../../standards/doctrine/queries-dbal.md) — 1: Doctrine queries and DBAL; 7: Select the smallest useful query abstraction; 19: Bind values and control SQL structure; 36: Result boundaries; 50: DBAL transactions; 72: ORM query shape | doctrine | [standards/doctrine.md:29](../../standards/doctrine.md#read-by-task) — Doctrine DBAL SQL/results/transactions, ORM query shape, N+1, pagination or batches | E retained; optional design route |
| [standards/doctrine/schema-verification.md](../../standards/doctrine/schema-verification.md) — 1: Doctrine schema, verification and compatibility; 7: Establish the actual combination; 35: Choose evidence for the changed behavior; 61: Schema changes and migrations | doctrine | [standards/doctrine.md:30](../../standards/doctrine.md#read-by-task) — Doctrine mapping/schema tests, migrations, deployment, upgrades or compatibility | E retained; optional design route |
| [standards/doctrine/unit-of-work-transactions.md](../../standards/doctrine/unit-of-work-transactions.md) — 1: Doctrine ORM unit of work and transactions; 7: Own the persistence context; 30: Transaction boundary and failure; 61: Concurrency decisions; 82: Lifecycle events and external effects | doctrine | [standards/doctrine.md:28](../../standards/doctrine.md#read-by-task) — Doctrine ORM identity map/lifetime, flush, transaction failure, concurrency or effects | E retained; optional design route |
| [standards/fastapi/dependencies-lifetime.md](../../standards/fastapi/dependencies-lifetime.md) — 1: FastAPI dependencies and lifetime; 8: Dependency ownership; 27: Match cleanup to the last consumer; 49: Lifespan and persistence; 75: Background and streaming effects | fastapi | [standards/fastapi.md:25](../../standards/fastapi.md#read-by-task) — Depends, caching, yield scopes, lifespan, transactions, background work | E retained; optional design route |
| [standards/fastapi/examples/http-boundary.md](../../standards/fastapi/examples/http-boundary.md) — 1: Example: HTTP validation and a domain capacity rule | fastapi | [standards/fastapi/transport.md:88](../../standards/fastapi/transport.md#errors-and-compatibility) — relevant Errors and compatibility subsection; optional example when needed | X retained; H evidence |
| [standards/fastapi/examples/lifetime.md](../../standards/fastapi/examples/lifetime.md) — 1: Example: lifespan client and request-owned upstream stream | fastapi | [standards/fastapi/dependencies-lifetime.md:90](../../standards/fastapi/dependencies-lifetime.md#background-and-streaming-effects) — relevant Background and streaming effects subsection; optional example when needed | X retained; H evidence |
| [standards/fastapi/runtime-operations.md](../../standards/fastapi/runtime-operations.md) — 1: FastAPI runtime and operations; 9: Execution and resource budgets; 42: Exposed security boundaries; 73: Deployment and performance | fastapi | [standards/fastapi.md:26](../../standards/fastapi.md#read-by-task) — Async/sync execution, streaming, security, middleware, deployment, performance | E retained; optional design route |
| [standards/fastapi/transport.md](../../standards/fastapi/transport.md) — 1: FastAPI transport and contracts; 9: Organization and construction; 31: Input and public output; 67: Errors and compatibility | fastapi | [standards/fastapi.md:24](../../standards/fastapi.md#read-by-task) — HTTP routes, input/output models, domain calls, errors, OpenAPI contracts | E retained; optional design route |
| [standards/fastapi/verification.md](../../standards/fastapi/verification.md) — 1: FastAPI verification and compatibility; 9: Behavior and test isolation; 45: Preserve contracts during change | fastapi | [standards/fastapi.md:27](../../standards/fastapi.md#read-by-task) — HTTP/lifespan tests, dependency overrides, file moves, FastAPI stack upgrades | E retained; optional design route |
| [standards/gin/examples/binding.md](../../standards/gin/examples/binding.md) — 1: Gin example: presence, bounded JSON, and business errors | gin | [standards/gin/handlers-binding.md:86](../../standards/gin/handlers-binding.md#json-limits-and-errors) — relevant JSON, limits, and errors subsection; optional example when needed | X retained; H evidence |
| [standards/gin/examples/middleware.md](../../standards/gin/examples/middleware.md) — 1: Gin example: a terminating gate and a shared error responder | gin | [standards/gin/routing-middleware.md:52](../../standards/gin/routing-middleware.md#control-flow-and-one-response-owner) — relevant Control flow and one response owner subsection; optional example when needed | X retained; H evidence |
| [standards/gin/handlers-binding.md](../../standards/gin/handlers-binding.md) — 1: Gin: handlers, binding, and HTTP contracts; 7: Transport and application boundary; 25: Choose the input contract explicitly; 48: Presence and validation; 66: JSON, limits, and errors | gin | [standards/gin.md:21](../../standards/gin.md#read-by-task) — Gin handlers, request sources, binding, response/error contracts | E retained; optional design route |
| [standards/gin/routing-middleware.md](../../standards/gin/routing-middleware.md) — 1: Gin: route assembly and middleware; 6: Construct the route tree once; 29: Control flow and one response owner; 55: Recovery and cross-cutting behavior | gin | [standards/gin.md:22](../../standards/gin.md#read-by-task) — Gin route assembly, middleware order, authentication gates, recovery | E retained; optional design route |
| [standards/gin/runtime.md](../../standards/gin/runtime.md) — 1: Gin: request lifetime and exposed boundaries; 7: Request state and external work; 35: Serve and stop deliberately; 55: Bound input and establish trust | gin | [standards/gin.md:23](../../standards/gin.md#read-by-task) — Gin request lifetime, background work, server shutdown, proxies, uploads | E retained; optional design route |
| [standards/gin/verification.md](../../standards/gin/verification.md) — 1: Gin: verification and compatibility; 8: Check observable HTTP behavior; 37: Versions and migration; 64: Performance and limits of evidence | gin | [standards/gin.md:24](../../standards/gin.md#read-by-task) — Gin HTTP tests, dependency migration, codec changes, performance checks | E retained; optional design route |
| [standards/go/architecture.md](../../standards/go/architecture.md) — 1: Go: architecture and patterns; 5: Versions and modules; 21: Packages and files; 44: Patterns in Go; 67: Basis | go | [standards/go.md:27](../../standards/go.md#read-by-task) — Packages, dependency direction, construction, patterns, modules/toolchains | E retained; optional design route |
| [standards/go/concurrency.md](../../standards/go/concurrency.md) — 1: Go: cancellation and concurrency | go | [standards/go.md:29](../../standards/go.md#read-by-task) — Goroutines, channels, shared state, cancellation, shutdown | E retained; optional design route |
| [standards/go/contracts.md](../../standards/go/contracts.md) — 1: Go: types, domain contracts, and errors; 5: Types, state, and construction; 31: Domain rules and boundary validation; 41: Dependencies and errors | go | [standards/go.md:28](../../standards/go.md#read-by-task) — Public types, domain state, validation, receivers, errors | E retained; optional design route |
| [standards/go/examples/concurrency.md](../../standards/go/examples/concurrency.md) — 1: Go example: cancel blocked receives and sends | go | [standards/go/concurrency.md:26](../../standards/go/concurrency.md#go-cancellation-and-concurrency) — relevant Go: cancellation and concurrency subsection; optional example when needed | X retained; H evidence |
| [standards/go/examples/dependencies.md](../../standards/go/examples/dependencies.md) — 1: Go example: dependency and function strategy | go | [standards/go/contracts.md:51](../../standards/go/contracts.md#dependencies-and-errors) — relevant Dependencies and errors subsection; optional example when needed | X retained; H evidence |
| [standards/go/examples/domain.md](../../standards/go/examples/domain.md) — 1: Go example: publication invariant | go | [standards/go/contracts.md:38](../../standards/go/contracts.md#domain-rules-and-boundary-validation) — relevant Domain rules and boundary validation subsection; optional example when needed | X retained; H evidence |
| [standards/go/resources.md](../../standards/go/resources.md) — 1: Go: persistence and external resources | go | [standards/go.md:30](../../standards/go.md#read-by-task) — SQL, transactions, HTTP clients/servers, resource lifetime | E retained; optional design route |
| [standards/go/verification.md](../../standards/go/verification.md) — 1: Go: verification, security, and performance | go | [standards/go.md:31](../../standards/go.md#read-by-task) — Choosing Go checks, security boundaries, measured performance | E retained; optional design route |
| [standards/javascript/async-effects.md](../../standards/javascript/async-effects.md) — 1: JavaScript async operations and effects; 8: Completion has an owner; 32: Ordering, parallelism and cancellation; 64: Resources, persistence and integrations; 87: Basis | javascript | [standards/javascript.md:26](../../standards/javascript.md#read-by-task) — Promises, ordering, cancellation, resources, stale results or external effects | E retained; optional design route |
| [standards/javascript/examples/async-ownership.md](../../standards/javascript/examples/async-ownership.md) — 1: JavaScript example: ownership of two required reads; 19: Setup; 34: package.json; 56: jsconfig.json; 87: Implementation and behavior checks; 89: src/overview.js; 142: tests/overview.test.js; 291: Run and verified scope | javascript | [standards/javascript/async-effects.md:5](../../standards/javascript/async-effects.md#javascript-async-operations-and-effects) — relevant JavaScript async operations and effects subsection; optional example when needed | X retained; H evidence |
| [standards/javascript/examples/input-state.md](../../standards/javascript/examples/input-state.md) — 1: JavaScript example: parsed input and current business state; 19: Setup; 34: package.json; 56: jsconfig.json; 87: Implementation and behavior checks; 89: src/reservation-input.js; 137: src/capacity.js; 184: tests/reservation.test.js; 251: Run and verified scope | javascript | [standards/javascript/values-state.md:5](../../standards/javascript/values-state.md#javascript-values-contracts-and-state) — relevant JavaScript values, contracts and state subsection; optional example when needed | X retained; H evidence |
| [standards/javascript/modules-structure.md](../../standards/javascript/modules-structure.md) — 1: JavaScript modules and structure; 7: Cohesion and boundaries; 27: Construction that carries its cost; 52: Module evaluation and actual hosts; 71: Basis | javascript | [standards/javascript.md:24](../../standards/javascript.md#read-by-task) — Modules/imports, file moves, construction, dependencies, classes or callbacks | E retained; optional design route |
| [standards/javascript/values-state.md](../../standards/javascript/values-state.md) — 1: JavaScript values, contracts and state; 7: From external representation to an owned contract; 45: State and behavioral invariants; 71: Serialization and errors; 87: Basis | javascript | [standards/javascript.md:25](../../standards/javascript.md#read-by-task) — JSDoc/data contracts, coercion, null/presence, JSON, mutation or domain invariants | E retained; optional design route |
| [standards/javascript/verification-compatibility.md](../../standards/javascript/verification-compatibility.md) — 1: JavaScript verification and compatibility; 7: Verify the boundary that changed; 36: Compatibility follows the supported project; 56: Security, load and operations when relevant; 78: Basis | javascript | [standards/javascript.md:27](../../standards/javascript.md#read-by-task) — Tests, static checking, host compatibility, security, performance or upgrades | E retained; optional design route |
| [standards/nestjs/application-lifecycle.md](../../standards/nestjs/application-lifecycle.md) — 1: NestJS application work and lifecycle; 7: Business core and assembly; 22: State, transactions and effects; 52: Startup and teardown ownership; 78: Basis | nestjs | [standards/nestjs.md:37](../../standards/nestjs.md#read-by-task) — Use cases, persistence, transactions, external effects, startup or shutdown | E retained; optional design route |
| [standards/nestjs/examples/provider-lifecycle.md](../../standards/nestjs/examples/provider-lifecycle.md) — 1: Exported provider capability and awaited disposal; 27: Setup and checks; 48: package.json; 82: tsconfig.json; 119: eslint.config.mjs; 141: src/report.ts; 155: src/export-total.ts; 174: src/file-report-sink.ts; 198: src/report.module.ts; 225: src/exporter.module.ts; 254: tests/run.ts; 356: Evidence and limits | nestjs | [standards/nestjs/application-lifecycle.md:74](../../standards/nestjs/application-lifecycle.md#startup-and-teardown-ownership) — relevant Startup and teardown ownership subsection; optional example when needed | X retained; H evidence |
| [standards/nestjs/examples/validated-command.md](../../standards/nestjs/examples/validated-command.md) — 1: A validated Nest command and an explicit response; 28: Setup and checks; 49: package.json; 85: tsconfig.json; 122: eslint.config.mjs; 144: src/reserve.dto.ts; 168: src/inventory.ts; 208: src/receipt.view.ts; 223: src/reservations.controller.ts; 249: src/reservations.module.ts; 278: src/application.ts; 304: tests/run.ts; 370: Evidence and limits | nestjs | [standards/nestjs/transport-contracts.md:4](../../standards/nestjs/transport-contracts.md#nestjs-transport-contracts) — relevant NestJS transport contracts subsection; optional example when needed | X retained; H evidence |
| [standards/nestjs/modules-providers.md](../../standards/nestjs/modules-providers.md) — 1: NestJS modules and providers; 7: Feature modules and components; 24: Tokens and construction; 47: Scope follows state lifetime; 63: Basis | nestjs | [standards/nestjs.md:35](../../standards/nestjs.md#read-by-task) — Feature boundaries, module exports, provider tokens/factories, scopes or cycles | E retained; optional design route |
| [standards/nestjs/transport-contracts.md](../../standards/nestjs/transport-contracts.md) — 1: NestJS transport contracts; 7: Entry points, DTOs, and validation; 28: Verify the real input path; 62: Request order, authorization and errors; 84: Output is a separate contract; 104: Basis | nestjs | [standards/nestjs.md:36](../../standards/nestjs.md#read-by-task) — DTOs/schemas, pipes, guards, filters, transformations or response serialization | E retained; optional design route |
| [standards/nestjs/verification-operations.md](../../standards/nestjs/verification-operations.md) — 1: NestJS verification and operations; 8: Match checks to the changed boundary; 36: Security and operational behavior; 57: Existing projects and version changes; 85: Basis | nestjs | [standards/nestjs.md:39](../../standards/nestjs.md#read-by-task) — Tests, actual adapter behavior, configuration, security, performance or upgrades | E retained; optional design route |
| [standards/nextjs/data-cache-mutations.md](../../standards/nextjs/data-cache-mutations.md) — 1: Next.js data, cache ownership and mutations; 10: Identify the actual cache model; 39: Mutation and invalidation are separate responsibilities; 66: Basis | nextjs-framework | [standards/nextjs-framework.md:28](../../standards/nextjs-framework.md#read-by-task) — Server reads, persistence, caches, mutations or revalidation | E retained; optional design route |
| [standards/nextjs/examples/authorized-command.md](../../standards/nextjs/examples/authorized-command.md) — 1: Example: authorized HTTP command with an independent invariant; 26: Setup in a temporary directory; 60: Files; 62: package.json; 96: tsconfig.json; 145: next.config.ts; 156: eslint.config.mjs; 177: features/reserve/stock.ts; 203: features/reserve/session.ts; 221: app/api/reservations/route.ts; 255: tests/http.ts; 377: Evidence and limits | nextjs-framework | [standards/nextjs/server-client-security.md:66](../../standards/nextjs/server-client-security.md#authority-at-the-operation) — relevant Authority at the operation subsection; optional example when needed | X retained; H evidence |
| [standards/nextjs/examples/tagged-read.md](../../standards/nextjs/examples/tagged-read.md) — 1: Example: tagged server data and a minimal client projection; 27: Files; 29: features/catalog/read.ts; 53: app/api/catalog/route.ts; 65: app/api/revalidate/route.ts; 81: features/catalog/CatalogTitle.tsx; 100: app/page.tsx; 113: app/layout.tsx; 123: Observed evidence and limits | nextjs-framework | [standards/nextjs/data-cache-mutations.md:61](../../standards/nextjs/data-cache-mutations.md#mutation-and-invalidation-are-separate-responsibilities) — relevant Mutation and invalidation are separate responsibilities subsection; optional example when needed | X retained; H evidence |
| [standards/nextjs/rendering-runtime.md](../../standards/nextjs/rendering-runtime.md) — 1: Next.js rendering, resources and deployment; 5: Useful rendering boundaries; 34: Host capabilities and lifetime; 64: Basis | nextjs-framework | [standards/nextjs-framework.md:29](../../standards/nextjs-framework.md#read-by-task) — Streaming, errors, metadata/assets, host lifecycle or deployment | E retained; optional design route |
| [standards/nextjs/routing-composition.md](../../standards/nextjs/routing-composition.md) — 1: Next.js routing and application composition; 7: Router and version first; 37: Own the integration once; 58: Basis | nextjs-framework | [standards/nextjs-framework.md:26](../../standards/nextjs-framework.md#read-by-task) — Routes/layouts/parameters, navigation, API shape or feature ownership | E retained; optional design route |
| [standards/nextjs/server-client-security.md](../../standards/nextjs/server-client-security.md) — 1: Next.js server/client and trust boundaries; 7: Execution and data exposure; 37: Authority at the operation; 70: Basis | nextjs-framework | [standards/nextjs-framework.md:27](../../standards/nextjs-framework.md#read-by-task) — Server/Client imports, RSC props, sessions, Actions or trust boundaries | E retained; optional design route |
| [standards/nextjs/verification-migration.md](../../standards/nextjs/verification-migration.md) — 1: Next.js verification and version migration; 7: Verify the changed contract; 36: Compatibility is a scoped decision; 63: Basis | nextjs-framework | [standards/nextjs-framework.md:30](../../standards/nextjs-framework.md#read-by-task) — Build/tests, generated types, performance or version migration | E retained; optional design route |
| [standards/ngrx/effects.md](../../standards/ngrx/effects.md) — 1: NgRx Effects and async workflows; 7: Work ownership; 35: Read state and emit outcomes | ngrx | [standards/ngrx.md:33](../../standards/ngrx.md#read-by-task) — Effects, concurrency, errors, retries or external synchronization | E retained; optional design route |
| [standards/ngrx/entity-router.md](../../standards/ngrx/entity-router.md) — 1: NgRx Entity and Router Store; 7: Entity collections; 27: Router Store | ngrx | [standards/ngrx.md:34](../../standards/ngrx.md#read-by-task) — Normalized Entity collections or Router Store | E retained; optional design route |
| [standards/ngrx/examples/signal-store-request.md](../../standards/ngrx/examples/signal-store-request.md) — 1: Example: component-scoped SignalStore with replaceable reads | ngrx | [standards/ngrx.md:39](../../standards/ngrx.md#read-by-task) — relevant Read by task subsection; optional example when needed | X retained; H evidence |
| [standards/ngrx/examples/store-view-model.md](../../standards/ngrx/examples/store-view-model.md) — 1: Example: immutable Store state and a memoized OnPush view | ngrx | [standards/ngrx.md:38](../../standards/ngrx.md#read-by-task) — relevant Read by task subsection; optional example when needed | X retained; H evidence |
| [standards/ngrx/signal-store.md](../../standards/ngrx/signal-store.md) — 1: NgRx SignalStore; 7: Composition and ownership; 31: Async work with rxMethod; 52: Entities and optional extensions | ngrx | [standards/ngrx.md:35](../../standards/ngrx.md#read-by-task) — SignalStore composition, computed state, rxMethod or signal entities | E retained; optional design route |
| [standards/ngrx/state-architecture.md](../../standards/ngrx/state-architecture.md) — 1: NgRx state architecture; 23: State shape and ownership; 41: Store placement; 60: Flat classic Store files; 87: Component-local state; 104: Providers and feature boundaries | ngrx | [standards/ngrx.md:29](../../standards/ngrx.md#read-by-task) — Library selection or state shape; [standards/ngrx.md:30](../../standards/ngrx.md#read-by-task) — Root Store wiring, flat feature Store files or component-local stores; [standards/ngrx.md:31](../../standards/ngrx.md#read-by-task) — Eager/lazy registration, providers or lifecycle | E retained; optional design route |
| [standards/ngrx/store-selectors.md](../../standards/ngrx/store-selectors.md) — 1: NgRx Store, reducers and selector memoization; 5: Events and pure transitions; 23: Selectors and memoization; 50: Optimization boundaries | ngrx | [standards/ngrx.md:32](../../standards/ngrx.md#read-by-task) — Store actions/reducers, selectors, memoization or selectSignal | E retained; optional design route |
| [standards/ngrx/verification.md](../../standards/ngrx/verification.md) — 1: NgRx verification and tooling; 7: Focused evidence; 33: Runtime checks and diagnostics | ngrx | [standards/ngrx.md:36](../../standards/ngrx.md#read-by-task) — Tests, runtime checks, DevTools or migration evidence | E retained; optional design route |
| [standards/nodejs/examples/bounded-stream.md](../../standards/nodejs/examples/bounded-stream.md) — 1: Bounded byte pipeline; 8: Contract and setup; 26: copy.mjs; 66: run.mjs; 204: Run and evidence | nodejs | [standards/nodejs/io-concurrency.md:5](../../standards/nodejs/io-concurrency.md#nodejs-io-and-concurrency) — relevant Node.js I/O and concurrency subsection; optional example when needed | X retained; H evidence |
| [standards/nodejs/examples/graceful-server.md](../../standards/nodejs/examples/graceful-server.md) — 1: HTTP shutdown with owned application work; 8: Contract and setup; 37: service.mjs; 153: run.mjs; 347: Run and evidence; 367: Limits when adapting | nodejs | [standards/nodejs/lifecycle-verification.md:4](../../standards/nodejs/lifecycle-verification.md#nodejs-lifecycle-and-verification) — relevant Node.js lifecycle and verification subsection; optional example when needed | X retained; H evidence |
| [standards/nodejs/http-integrations.md](../../standards/nodejs/http-integrations.md) — 1: Node.js HTTP and integrations; 9: Incoming boundaries; 31: Outbound boundaries; 54: Persistence and external consistency; 74: Basis | nodejs | [standards/nodejs.md:22](../../standards/nodejs.md#read-by-task) — HTTP servers/clients, body limits, deadlines, persistence or external effects | E retained; optional design route |
| [standards/nodejs/io-concurrency.md](../../standards/nodejs/io-concurrency.md) — 1: Node.js I/O and concurrency; 9: Capacity follows the resource; 25: Stream ownership and backpressure; 48: Files and event-driven APIs; 71: Basis | nodejs | [standards/nodejs.md:21](../../standards/nodejs.md#read-by-task) — Streams, files, CPU work, workers, event callbacks or bounded concurrency | E retained; optional design route |
| [standards/nodejs/lifecycle-verification.md](../../standards/nodejs/lifecycle-verification.md) — 1: Node.js lifecycle and verification; 9: Start, drain and release; 45: Diagnostics and security; 66: Checks and version changes; 88: Basis | nodejs | [standards/nodejs.md:23](../../standards/nodejs.md#read-by-task) — Signals, shutdown, resource cleanup, diagnostics, security checks or runtime upgrades | E retained; optional design route |
| [standards/nodejs/runtime-composition.md](../../standards/nodejs/runtime-composition.md) — 1: Node.js runtime and composition; 10: Server execution and responsibility; 24: Assembly and configuration; 47: Packages and executable contracts; 69: Basis | nodejs | [standards/nodejs.md:20](../../standards/nodejs.md#read-by-task) — Startup/configuration, package loading, dependency assembly or direct TS execution | E retained; optional design route |
| [standards/php/examples/input-domain.md](../../standards/php/examples/input-domain.md) — 1: Example: parse a draft, enforce publication in the domain | php | [standards/php/types-contracts.md:64](../../standards/php/types-contracts.md#business-state-and-errors) — relevant Business state and errors subsection; optional example when needed | X retained; H evidence |
| [standards/php/examples/resources.md](../../standards/php/examples/resources.md) — 1: Example: bounded reading with one resource owner | php | [standards/php/state-effects.md:50](../../standards/php/state-effects.md#streams-and-iteration) — relevant Streams and iteration subsection; optional example when needed | X retained; H evidence |
| [standards/php/state-effects.md](../../standards/php/state-effects.md) — 1: PHP state and effects; 7: State and lifetime; 27: Streams and iteration; 53: Concurrency, deadlines, and cancellation; 72: Persistence and integration | php | [standards/php.md:24](../../standards/php.md#read-by-task) — Mutation, readonly/clone, streams, generators, workers, transactions or I/O | E retained; optional design route |
| [standards/php/structure.md](../../standards/php/structure.md) — 1: PHP structure and dependencies; 8: Modules and autoloading; 31: Construction and useful abstraction; 60: Dependency reproducibility | php | [standards/php.md:22](../../standards/php.md#read-by-task) — Namespaces, PSR-4, packages, object construction, dependencies or patterns | E retained; optional design route |
| [standards/php/types-contracts.md](../../standards/php/types-contracts.md) — 1: PHP types and contracts; 7: Native types, static checks, and coercion; 33: Input presence and parsing; 57: Business state and errors | php | [standards/php.md:23](../../standards/php.md#read-by-task) — Native/PHPDoc types, arrays, parsing, null/presence, domain rules, errors | E retained; optional design route |
| [standards/php/verification.md](../../standards/php/verification.md) — 1: PHP verification and compatibility; 7: Proportionate checks; 40: Exposed security and operations; 65: Versions and migration | php | [standards/php.md:25](../../standards/php.md#read-by-task) — Tests, static analysis, autoload/file moves, security, performance or upgrades | E retained; optional design route |
| [standards/postgresql/examples/atomic-reservation.md](../../standards/postgresql/examples/atomic-reservation.md) — 1: Atomic reservation without a read-before-write race; 7: Contract and setup; 29: schema.sql; 53: reserve.sql; 69: call.sql; 83: Why this statement has the needed boundary; 103: Check competing requests and failure paths | postgresql | [standards/postgresql/schema-contracts.md:36](../../standards/postgresql/schema-contracts.md#durable-rules) — relevant Durable rules subsection; optional example when needed | X retained; H evidence |
| [standards/postgresql/examples/online-constraint.md](../../standards/postgresql/examples/online-constraint.md) — 1: Add a required value without ignoring historical data; 7: Preconditions and phases; 20: legacy.sql; 33: expand.sql; 45: backfill.sql; 58: validate.sql; 69: contract.sql; 80: index.sql; 92: attach.sql; 104: Expected behavior and lock boundaries | postgresql | [standards/postgresql/migrations-verification.md:22](../../standards/postgresql/migrations-verification.md#change-the-deployed-contract-deliberately) — relevant Change the deployed contract deliberately subsection; optional example when needed | X retained; H evidence |
| [standards/postgresql/migrations-verification.md](../../standards/postgresql/migrations-verification.md) — 1: PostgreSQL migrations and verification; 6: Change the deployed contract deliberately; 39: Version and test evidence | postgresql | [standards/postgresql.md:33](../../standards/postgresql.md#read-for-the-task) — Changing schema/data, upgrading versions or choosing verification | E retained; optional design route |
| [standards/postgresql/queries-performance.md](../../standards/postgresql/queries-performance.md) — 1: PostgreSQL queries and performance; 5: Boundaries and predictable results; 20: Evidence before indexing | postgresql | [standards/postgresql.md:31](../../standards/postgresql.md#read-for-the-task) — Changing queries, indexes, pagination or a measured performance problem | E retained; optional design route |
| [standards/postgresql/schema-contracts.md](../../standards/postgresql/schema-contracts.md) — 1: PostgreSQL schema and contracts; 6: Ownership before abstraction; 16: Durable rules; 38: Types and boundary meaning | postgresql | [standards/postgresql.md:29](../../standards/postgresql.md#read-for-the-task) — Designing tables, durable rules, types or persistence boundaries | E retained; optional design route |
| [standards/postgresql/security-operations.md](../../standards/postgresql/security-operations.md) — 1: PostgreSQL security and operations; 5: Identity, privileges and object resolution; 31: Resource budgets and diagnosis; 45: Recovery and replication | postgresql | [standards/postgresql.md:32](../../standards/postgresql.md#read-for-the-task) — Changing roles, tenant isolation, connection lifetime, backup or production behavior | E retained; optional design route |
| [standards/postgresql/transactions-concurrency.md](../../standards/postgresql/transactions-concurrency.md) — 1: PostgreSQL transactions and concurrency; 5: Atomic operations and isolation; 26: Conflicts and retries; 46: Lock scope and lifetime | postgresql | [standards/postgresql.md:30](../../standards/postgresql.md#read-for-the-task) — Changing writes, isolation, locks, retries or work claiming | E retained; optional design route |
| [standards/psycopg/async-pooling.md](../../standards/psycopg/async-pooling.md) — 1: psycopg async work and pooling; 6: Concurrency is not transaction isolation; 21: Pool ownership and budgets; 41: Trust and observability | psycopg | [standards/psycopg.md:30](../../standards/psycopg.md#read-for-the-task) — Async concurrency, cancellation, pools, startup or connection security | E retained; optional design route |
| [standards/psycopg/compatibility-verification.md](../../standards/psycopg/compatibility-verification.md) — 1: psycopg compatibility and verification; 7: Establish the actual stack; 34: Proportionate evidence | psycopg | [standards/psycopg.md:31](../../standards/psycopg.md#read-for-the-task) — Installation, Psycopg 2 migration, feature compatibility or verification | E retained; optional design route |
| [standards/psycopg/examples/owned-transaction.md](../../standards/psycopg/examples/owned-transaction.md) — 1: An explicit transaction owner and a borrowing helper; 14: owned_transaction.py | psycopg | [standards/psycopg/transactions-lifetime.md:22](../../standards/psycopg/transactions-lifetime.md#scope-must-match-the-operation) — relevant Scope must match the operation subsection; optional example when needed | X retained; H evidence |
| [standards/psycopg/examples/typed-query.md](../../standards/psycopg/examples/typed-query.md) — 1: Typed query with separate identifier and value binding; 12: typed_query.py | psycopg | [standards/psycopg/queries-contracts.md:17](../../standards/psycopg/queries-contracts.md#sql-structure-and-data) — relevant SQL structure and data subsection; optional example when needed | X retained; H evidence |
| [standards/psycopg/queries-contracts.md](../../standards/psycopg/queries-contracts.md) — 1: psycopg queries and contracts; 6: SQL structure and data; 25: Row and adaptation contracts; 45: Select bulk tools for a measured requirement | psycopg | [standards/psycopg.md:28](../../standards/psycopg.md#read-for-the-task) — Parameters, dynamic SQL, result types, adaptation or bulk I/O | E retained; optional design route |
| [standards/psycopg/transactions-lifetime.md](../../standards/psycopg/transactions-lifetime.md) — 1: psycopg transactions and lifetime; 6: Scope must match the operation; 31: Failure and cancellation boundaries | psycopg | [standards/psycopg.md:29](../../standards/psycopg.md#read-for-the-task) — Transaction boundaries, savepoints, failures or resource ownership | E retained; optional design route |
| [standards/pydantic/examples/boundary.md](../../standards/pydantic/examples/boundary.md) — 1: Pydantic example: a booking input boundary | pydantic | [standards/pydantic/validation.md:88](../../standards/pydantic/validation.md#validators-remain-local-and-deterministic) — relevant Validators remain local and deterministic subsection; optional example when needed | X retained; H evidence |
| [standards/pydantic/examples/patches.md](../../standards/pydantic/examples/patches.md) — 1: Pydantic example: partial input, validated replacement, public output | pydantic | [standards/pydantic/serialization.md:54](../../standards/pydantic/serialization.md#names-presence-and-partial-updates) — relevant Names, presence, and partial updates subsection; optional example when needed | X retained; H evidence |
| [standards/pydantic/lifecycle.md](../../standards/pydantic/lifecycle.md) — 1: Pydantic: model lifetime and integration boundaries; 6: Validation is a boundary event; 34: Mapping external data without hidden work; 56: Extensions and repeated use | pydantic | [standards/pydantic.md:26](../../standards/pydantic.md#read-by-task) — Pydantic mutation/copying, trust, ORM/SDK/settings boundaries | E retained; optional design route |
| [standards/pydantic/serialization.md](../../standards/pydantic/serialization.md) — 1: Pydantic: serialization, aliases, and schemas; 6: Public output is an explicit contract; 31: Names, presence, and partial updates; 57: Unions and generated schemas | pydantic | [standards/pydantic.md:25](../../standards/pydantic.md#read-by-task) — Pydantic output fields, aliases, patches, unions, JSON Schema | E retained; optional design route |
| [standards/pydantic/validation.md](../../standards/pydantic/validation.md) — 1: Pydantic: models and input validation; 8: Choose the boundary and simplest model; 29: Define accepted input explicitly; 55: Validators remain local and deterministic | pydantic | [standards/pydantic.md:24](../../standards/pydantic.md#read-by-task) — Pydantic model choice, fields, parsing modes, coercions, validators | E retained; optional design route |
| [standards/pydantic/verification.md](../../standards/pydantic/verification.md) — 1: Pydantic: checks, exposure, performance, and migration; 7: Test the contract that changed; 24: Static typing alongside runtime validation; 47: Exposed input and diagnostics; 64: Optimize only an observed cost; 76: Versions and migration | pydantic | [standards/pydantic.md:27](../../standards/pydantic.md#read-by-task) — Pydantic tests, mypy plugin, errors, performance, version migration | E retained; optional design route |
| [standards/python/examples/concurrency.md](../../standards/python/examples/concurrency.md) — 1: Python example: two required results with one lifetime | python | [standards/python/execution-resources.md:52](../../standards/python/execution-resources.md#related-async-work-and-cancellation) — relevant Related async work and cancellation subsection; optional example when needed | X retained; H evidence |
| [standards/python/examples/domain.md](../../standards/python/examples/domain.md) — 1: Python example: an incomplete draft and a protected transition | python | [standards/pydantic/lifecycle.md:10](../../standards/pydantic/lifecycle.md#validation-is-a-boundary-event) — relevant Validation is a boundary event subsection; optional example when needed | X retained; H evidence |
| [standards/python/execution-resources.md](../../standards/python/execution-resources.md) — 1: Python: execution, state, and resource lifetime; 6: Choose the execution model for the work; 29: Related async work and cancellation; 56: Ownership and cleanup; 79: Persistence and external integration | python | [standards/python.md:28](../../standards/python.md#read-by-task) — Async work, threads/processes, shared state, resources, transactions, external calls | E retained; optional design route |
| [standards/python/structure.md](../../standards/python/structure.md) — 1: Python: modules, construction, and dependencies; 6: Cohesive modules; 42: Python forms of useful patterns; 63: Imports, packaging, and versions | python | [standards/python.md:26](../../standards/python.md#read-by-task) — Modules, imports, construction, patterns, package/dependency boundaries | E retained; optional design route |
| [standards/python/typing-contracts.md](../../standards/python/typing-contracts.md) — 1: Python: typing, validation, state, and errors; 6: Strict static contracts; 39: Runtime input and domain state; 72: Error contracts | python | [standards/python.md:27](../../standards/python.md#read-by-task) — Signatures, DTOs, input parsing, domain state, errors, strict analyzer settings | E retained; optional design route |
| [standards/python/verification.md](../../standards/python/verification.md) — 1: Python: verification, exposed boundaries, and compatibility; 8: Match checks to changed behavior; 37: Security and operational behavior when exposed; 58: Measure before optimizing; 69: Version-sensitive decisions | python | [standards/python.md:29](../../standards/python.md#read-by-task) — Tests, exposed security boundaries, measured performance, Python/dependency migration | E retained; optional design route |
| [standards/react/components-boundaries.md](../../standards/react/components-boundaries.md) — 1: React components and dependency boundaries; 6: Cohesive owners; 32: Props, Hooks and assembly; 56: Basis | react | [standards/react.md:26](../../standards/react.md#read-by-task) — Component/hook boundaries, props, module ownership or dependency construction | E retained; optional design route |
| [standards/react/effects-integrations.md](../../standards/react/effects-integrations.md) — 1: React effects, reads and integration lifetime; 5: Synchronization has a lifetime; 25: Reads, races and stale UI; 44: Rendering boundaries and responsiveness; 60: Basis | react | [standards/react.md:28](../../standards/react.md#read-by-task) — Effects, subscriptions, reads, races, cancellation or loading boundaries | E retained; optional design route |
| [standards/react/examples/latest-result.md](../../standards/react/examples/latest-result.md) — 1: Example: publish only the current integration result; 27: Reproduce; 42: Files; 44: src/LatestResult.tsx; 96: tests/latest.test.tsx; 271: Observed evidence and limits | react | [standards/react/effects-integrations.md:40](../../standards/react/effects-integrations.md#reads-races-and-stale-ui) — relevant Reads, races and stale UI subsection; optional example when needed | X retained; H evidence |
| [standards/react/examples/reservation-form.md](../../standards/react/examples/reservation-form.md) — 1: Example: a reservation form and an independent operation; 21: Reproduce in a temporary directory; 43: Files; 45: package.json; 84: tsconfig.json; 126: eslint.config.mjs; 151: tests/setup.ts; 169: src/reservation.ts; 211: src/ReservationForm.tsx; 258: tests/reservation.test.tsx; 334: Observed evidence and limits | react | [standards/react/forms-contracts.md:62](../../standards/react/forms-contracts.md#form-state-and-interaction) — relevant Form state and interaction subsection; optional example when needed | X retained; H evidence |
| [standards/react/forms-contracts.md](../../standards/react/forms-contracts.md) — 1: React forms, commands and user-visible contracts; 15: Representation is not eligibility; 35: Form state and interaction; 66: Basis | react | [standards/react.md:29](../../standards/react.md#read-by-task) — Forms, commands, validation, mutation outcomes or accessible feedback | E retained; optional design route |
| [standards/react/state-identity.md](../../standards/react/state-identity.md) — 1: React state, identity and ownership; 5: Choose an owner and a representation; 29: Identity, snapshots and resets; 48: Basis | react | [standards/react.md:27](../../standards/react.md#read-by-task) — State shape/ownership, keys, reset, reducers, context or external stores | E retained; optional design route |
| [standards/react/verification-compatibility.md](../../standards/react/verification-compatibility.md) — 1: React verification, compatibility and performance; 6: Evidence at the affected boundary; 34: Host and security; 50: Performance and versions; 74: Basis | react | [standards/react.md:30](../../standards/react.md#read-by-task) — Tests, render/build checks, performance, security, SSR or version migration | E retained; optional design route |
| [standards/sqlalchemy/async-engines.md](../../standards/sqlalchemy/async-engines.md) — 1: SQLAlchemy async work and engines; 6: Engine, pool and driver ownership; 33: Async operation scope; 55: Connection and data trust | sqlalchemy | [standards/sqlalchemy.md:36](../../standards/sqlalchemy.md#read-for-the-task) — Async work, engine/pool lifetime, cancellation or connection security | E retained; optional design route |
| [standards/sqlalchemy/examples/async-projection.md](../../standards/sqlalchemy/examples/async-projection.md) — 1: Async loading into an owned public projection; 8: Load before crossing the boundary; 21: projection.py; 79: Executed checks and lifetime; 87: test_projection.py | sqlalchemy | [standards/sqlalchemy/queries-loading.md:37](../../standards/sqlalchemy/queries-loading.md#load-the-required-graph-deliberately) — relevant Load the required graph deliberately subsection; optional example when needed | X retained; H evidence |
| [standards/sqlalchemy/examples/transactional-command.md](../../standards/sqlalchemy/examples/transactional-command.md) — 1: An owned transaction around a typed reservation; 7: Setup and scope; 30: requirements.txt; 39: mypy.ini; 50: Operation and mapping; 62: command.py; 143: Executed checks; 152: test_command.py | sqlalchemy | [standards/sqlalchemy/mapping-contracts.md:42](../../standards/sqlalchemy/mapping-contracts.md#typed-maps-are-not-runtime-validators) — relevant Typed maps are not runtime validators subsection; optional example when needed | X retained; H evidence |
| [standards/sqlalchemy/mapping-contracts.md](../../standards/sqlalchemy/mapping-contracts.md) — 1: SQLAlchemy mapping and contracts; 6: Choose the persistence model; 15: Typed maps are not runtime validators; 44: Relationships and public data | sqlalchemy | [standards/sqlalchemy.md:33](../../standards/sqlalchemy.md#read-for-the-task) — Core/ORM choice, mapped types, relationships, domain or output boundaries | E retained; optional design route |
| [standards/sqlalchemy/migrations-verification.md](../../standards/sqlalchemy/migrations-verification.md) — 1: SQLAlchemy migrations and verification; 6: Schema ownership; 23: Compatibility is a concrete matrix; 51: Evidence for the affected boundary | sqlalchemy | [standards/sqlalchemy.md:37](../../standards/sqlalchemy.md#read-for-the-task) — Tests, schema evolution, typing compatibility or SQLAlchemy upgrades | E retained; optional design route |
| [standards/sqlalchemy/queries-loading.md](../../standards/sqlalchemy/queries-loading.md) — 1: SQLAlchemy queries and loading; 5: Query shape and results; 19: Load the required graph deliberately; 41: Writes and performance | sqlalchemy | [standards/sqlalchemy.md:35](../../standards/sqlalchemy.md#read-for-the-task) — SELECT/result shape, eager loading, bulk DML, pagination or performance | E retained; optional design route |
| [standards/sqlalchemy/sessions-transactions.md](../../standards/sqlalchemy/sessions-transactions.md) — 1: SQLAlchemy sessions and transactions; 5: The owner defines success; 37: Partial recovery and integration; 56: Concurrency is a database contract | sqlalchemy | [standards/sqlalchemy.md:34](../../standards/sqlalchemy.md#read-for-the-task) — Writes, unit of work, flush/commit, conflicts or transaction ownership | E retained; optional design route |
| [standards/symfony/examples/http-client.md](../../standards/symfony/examples/http-client.md) — 1: Example: finish a lazy HTTP response before returning stock | symfony | [standards/symfony/runtime-effects.md:30](../../standards/symfony/runtime-effects.md#http-clients-and-lazy-work) — relevant HTTP clients and lazy work subsection; optional example when needed | X retained; H evidence |
| [standards/symfony/examples/request-boundary.md](../../standards/symfony/examples/request-boundary.md) — 1: Example: mapped input before a state-changing use case | symfony | [standards/symfony/http-validation.md:39](../../standards/symfony/http-validation.md#request-mapping-is-an-executed-boundary) — relevant Request mapping is an executed boundary subsection; optional example when needed | X retained; H evidence |
| [standards/symfony/http-validation.md](../../standards/symfony/http-validation.md) — 1: Symfony HTTP, validation, and public contracts; 7: Request mapping is an executed boundary; 43: Arrays of nested DTOs; 73: Local validity, state, and output; 96: Forms and authorization where applicable | symfony | [standards/symfony.md:24](../../standards/symfony.md#read-by-task) — Symfony routes, request mapping, Validator/forms, public output or authorization | E retained; optional design route |
| [standards/symfony/runtime-effects.md](../../standards/symfony/runtime-effects.md) — 1: Symfony runtime, external effects, and workers; 8: HTTP clients and lazy work; 39: Messenger delivery and process lifetime; 68: Kernel lifecycle and persistence | symfony | [standards/symfony.md:25](../../standards/symfony.md#read-by-task) — Symfony HttpClient, Messenger, kernel events, workers, transaction handoff or caches | E retained; optional design route |
| [standards/symfony/structure-services.md](../../standards/symfony/structure-services.md) — 1: Symfony structure and services; 8: Application boundaries; 39: Container wiring and lifetime; 67: Configuration and extension cost | symfony | [standards/symfony.md:23](../../standards/symfony.md#read-by-task) — Symfony structure, service wiring/configuration, controllers/commands/handlers | E retained; optional design route |
| [standards/symfony/verification.md](../../standards/symfony/verification.md) — 1: Symfony verification and compatibility; 8: Match checks to the affected boundary; 36: Wiring, types, and moves; 58: Versions and operational applicability | symfony | [standards/symfony.md:26](../../standards/symfony.md#read-by-task) — Symfony tests, container/routes, deployment, upgrades or compatibility | E retained; optional design route |
| [standards/typeorm/examples/rich-booking.md](../../standards/typeorm/examples/rich-booking.md) — 1: A mapped rich booking; 8: booking.ts; 78: reschedule-booking.ts | typeorm | [standards/typeorm/models-mapping.md:72](../../standards/typeorm/models-mapping.md#mapping-contracts) — relevant Mapping contracts subsection; optional example when needed | X retained; H evidence |
| [standards/typeorm/models-mapping.md](../../standards/typeorm/models-mapping.md) — 1: TypeORM models and mapping; 6: Rich domain model; 40: Creation and hydration; 55: Mapping contracts | typeorm | [standards/typeorm.md:33](../../standards/typeorm.md#read-by-task) — Rich entities, constructors, intent methods, mapping or model placement | E retained; optional design route |
| [standards/typeorm/nestjs-integration.md](../../standards/typeorm/nestjs-integration.md) — 1: NestJS integration with TypeORM; 7: Registration and ownership; 23: Application boundary | typeorm | [standards/typeorm.md:37](../../standards/typeorm.md#read-by-task) — Actual NestJS TypeORM registration, injection or CLI data source | E retained; optional design route |
| [standards/typeorm/queries-relations.md](../../standards/typeorm/queries-relations.md) — 1: TypeORM queries and relations; 5: Query contracts; 25: Associations and loading; 43: Bounded results | typeorm | [standards/typeorm.md:35](../../standards/typeorm.md#read-by-task) — Queries, null filters, relations, cascades, pagination or projections | E retained; optional design route |
| [standards/typeorm/schema-verification.md](../../standards/typeorm/schema-verification.md) — 1: TypeORM schema and verification; 6: Migrations and deployment; 28: Focused evidence; 44: Compatibility | typeorm | [standards/typeorm.md:36](../../standards/typeorm.md#read-by-task) — Migrations, schema checks, compatibility or test selection | E retained; optional design route |
| [standards/typeorm/transactions-lifetime.md](../../standards/typeorm/transactions-lifetime.md) — 1: TypeORM transactions and lifetime; 7: Explicit persistence and ownership; 38: Concurrent transitions; 56: Effects and exceptional write paths | typeorm | [standards/typeorm.md:34](../../standards/typeorm.md#read-by-task) — Save, transaction ownership, rollback, locks, retries or external effects | E retained; optional design route |
| [standards/typescript/composition-effects.md](../../standards/typescript/composition-effects.md) — 1: TypeScript composition and effect contracts; 8: Preserve a real relationship; 27: Outcomes, states and errors; 47: Dependency callbacks and variance; 61: Types do not own effects; 81: Basis | typescript | [standards/typescript.md:36](../../standards/typescript.md#read-by-task) — Generics, unions/exhaustiveness, callbacks, promises or typed integration contracts | E retained; optional design route |
| [standards/typescript/contracts-structure.md](../../standards/typescript/contracts-structure.md) — 1: TypeScript contracts and structure; 9: Put contracts with their consumers and owners; 36: Construction and actual runtime values; 58: Type imports and module boundaries; 72: Basis | typescript | [standards/typescript.md:34](../../standards/typescript.md#read-by-task) — Interfaces/type ownership, modules, construction, dependencies or public APIs | E retained; optional design route |
| [standards/typescript/examples/typed-operation.md](../../standards/typescript/examples/typed-operation.md) — 1: TypeScript example: a typed operation with an executed decoder; 20: Setup; 41: package.json; 69: tsconfig.json; 104: eslint.config.mjs; 126: Implementation and behavior checks; 128: src/load.ts; 169: tests/run.ts; 252: Run and verified scope | typescript | [standards/typescript/composition-effects.md:5](../../standards/typescript/composition-effects.md#typescript-composition-and-effect-contracts) — relevant TypeScript composition and effect contracts subsection; optional example when needed | X retained; H evidence |
| [standards/typescript/examples/validated-command.md](../../standards/typescript/examples/validated-command.md) — 1: TypeScript example: validated command and stateful refusal; 18: Setup; 39: package.json; 67: tsconfig.json; 102: eslint.config.mjs; 124: Implementation and behavior checks; 126: src/change.ts; 159: src/quota.ts; 231: tests/run.ts; 288: Run and verified scope | typescript | [standards/typescript/validation-state.md:5](../../standards/typescript/validation-state.md#typescript-validation-and-state) — relevant TypeScript validation and state subsection; optional example when needed | X retained; H evidence |
| [standards/typescript/toolchain-verification.md](../../standards/typescript/toolchain-verification.md) — 1: TypeScript toolchain and verification; 9: Enforceability; 41: Check compile-time and runtime contracts separately; 62: Match the host, package and generated contract; 83: Versions, migration and performance; 110: Basis | typescript | [standards/typescript.md:37](../../standards/typescript.md#read-by-task) — Compiler/lint checks, emit/resolution, framework generation, upgrades or performance | E retained; optional design route |
| [standards/typescript/validation-state.md](../../standards/typescript/validation-state.md) — 1: TypeScript validation and state; 8: Establish the boundary before relying on types; 37: Absence, nullability and indexed access; 57: Static readonly and runtime ownership; 78: Basis | typescript | [standards/typescript.md:35](../../standards/typescript.md#read-by-task) — Unknown input, schemas/narrowing, presence/null, readonly state or invariants | E retained; optional design route |
| [standards/unreal-engine/build-assets.md](../../standards/unreal-engine/build-assets.md) — 1: Unreal build, assets and compatibility; 7: Modules and build inputs; 35: Iteration and reload; 52: Binary assets and reference migrations; 74: Loading, cook and package | unreal-engine | [standards/unreal-engine.md:46](../../standards/unreal-engine.md#read-for-the-task) — Module/build/reload, assets/references, migration, cook or package | E retained; optional design route |
| [standards/unreal-engine/cpp-lifetime.md](../../standards/unreal-engine/cpp-lifetime.md) — 1: Unreal C++: contracts, construction and lifetime; 8: Language and reflected contracts; 40: Construction and lifecycle; 67: References and ownership; 84: Guards and diagnostics | unreal-engine | [standards/unreal-engine.md:44](../../standards/unreal-engine.md#read-for-the-task) — Unreal C++, reflection, constructors, lifetime, references or guards | E retained; optional design route |
| [standards/unreal-engine/gameplay-blueprints.md](../../standards/unreal-engine/gameplay-blueprints.md) — 1: Unreal gameplay ownership and Blueprints; 7: Ownership and composition; 40: Native and Blueprint boundaries; 60: Interfaces and dispatch | unreal-engine | [standards/unreal-engine.md:45](../../standards/unreal-engine.md#read-for-the-task) — Gameplay owner, component/subsystem, Blueprint/native boundary or interface | E retained; optional design route |
| [standards/unreal-engine/mcp-editor.md](../../standards/unreal-engine/mcp-editor.md) — 1: Unreal MCP and editor operations; 7: Native provider basis; 28: Context and setup; 46: Bounded discovery; 61: Mutation and recovery; 107: Optional skills and custom tools | unreal-engine | [standards/unreal-engine.md:47](../../standards/unreal-engine.md#read-for-the-task) — Editor-provider setup, discovery, mutation, recovery or missing tool | E retained; optional design route |
| [standards/unreal-engine/runtime-performance.md](../../standards/unreal-engine/runtime-performance.md) — 1: Unreal concurrency, networking and performance; 7: Concurrency and lifetime; 29: Networking and authority; 51: Performance and conditional systems | unreal-engine | [standards/unreal-engine.md:50](../../standards/unreal-engine.md#read-for-the-task) — Async work, thread access or deferred completion; [standards/unreal-engine.md:51](../../standards/unreal-engine.md#read-for-the-task) — Established multiplayer requirement or affected network contract; [standards/unreal-engine.md:52](../../standards/unreal-engine.md#read-for-the-task) — Performance question or a relevant specialist system | E retained; optional design route |
| [standards/unreal-engine/skills.md](../../standards/unreal-engine/skills.md) — 1: Optional skills for Unreal, Blender and MCP; 8: Recommended starting points; 31: Providers and workflow references are separate; 47: Resolve conflicts before using a recipe | unreal-engine | [standards/unreal-engine.md:48](../../standards/unreal-engine.md#read-for-the-task) — Choosing skills for Unreal, Blender asset work or MCP extension | E retained; optional design route |
| [standards/unreal-engine/verification.md](../../standards/unreal-engine/verification.md) — 1: Unreal: sufficient verification and evidence reuse; 8: Complete a coherent block, then verify; 54: Select evidence by changed contract; 72: Reuse checks and tests; 93: Preserve the state being checked; 113: Stop when the evidence is sufficient | unreal-engine | [standards/unreal-engine.md:49](../../standards/unreal-engine.md#read-for-the-task) — Select checks, review evidence or report results | E retained; optional design route |

Inventory reconciliation: **182 unique standards files; 35 profile entries;
42 example files; 833 source headings; no standards file omitted or counted twice.**
The graph check found five entries without an incoming Markdown edge, all covered
by the explicit C-selection route. This is a source inventory result, not proof
that all native clients will load or obey those sections.

## Stage 2 after-state addendum — 2026-10-11

The inventory above remains the PS-01 before-state; its 35 profiles, 182 standards
files and 833 headings have not been relabeled as a run against later contents.
PS-02 adds `standards/project-skills.md` and the fourth inactive skill template,
`templates/skills/aek-design-feature/SKILL.md`. There are now 36 profiles and 183
standards Markdown files. Existing normative topics and their conditions remain;
no old policy owner or direct technical route was removed.

| Added/changed route | After-state responsibility |
| --- | --- |
| `project-workflows` | Optional core-dependent profile; adds only the design guide and template beyond the core closure |
| `standards/project-skills.md` | Local input/result contract and composition with existing procedures; technical rules stay with existing owners |
| `aek-design-feature` | Task entry for capability/material boundary design; inactive source template until selected adoption |
| Root/policy entry templates | Conditional guide/native path, omitted when the profile is absent; direct routes retained |
| MIGRATION | Existing installation/reconciliation owner, now explicitly covers design-skill rebasing and managed native scope |
| Architecture/README | Existing design template replaces the earlier conceptual design name; delivery-phase entry remains conceptual |

The [PS-02 evidence](2026-10-11-project-skills-validation.md) separates passing
closure/link/metadata/type checks from observed Codex CLI 0.162.1 discovery.
Ordinary source-independent execution and trigger/non-trigger behavior remain
unverified because the nested client could not access workspace tools. This is
first-slice V02/V03 static coverage and partial V07, not PS-05 comparison evidence,
PS-07 final preservation acceptance or proof that a model reads every rule.

### Resumed Stage 2 evidence — 2026-10-11

After the owner requested continuation, correcting the disposable harness's
`/proc` and `/dev` mounts allowed native commands without disabling Codex's sandbox.
The unchanged design slice completed one explicit source-hidden design trial and
one unrelated typo trial; only the intended canonical task or README changed.
An implicit trial selected/read the skill and produced a design but timed out
during verification, so it remains partial evidence. The
[validation record](2026-10-11-project-skills-validation.md#resumed-observation--2026-10-11)
retains results, checks and limits. PS-02's selected-client slice is now complete;
the historical inventory and initial failed observation remain unchanged evidence.
No profile, normative topic, trigger or source skill changed during this resumption.

## Stage 3 ownership and overlap disposition — 2026-10-11

PS-03 adds inactive `aek-implement-feature` and `aek-review-changes` templates to
the existing optional profile. There are still 36 profiles and 183 standards
Markdown files, now six source skill templates. The guide's shared task inputs
and selection table cover three entries; existing technical owners and direct
routes remain. Neither a native installation nor behavioral support follows from
source availability. Earlier PS-02 observations tested the recorded earlier guide
and entry contents, not this changed three-entry arrangement.

| Entry/disposition | Distinct responsibility and source route |
| --- | --- |
| Retain `aek-design-feature` | Local owners/contracts, relevant stack topics and design decisions; its unchanged template routes through the expanded shared guide |
| Add `aek-implement-feature` | Connect the authorized code change and affected interfaces/lifetimes to applicable technical topics and actual acceptance evidence; use existing execution procedure |
| Add `aek-review-changes` | Connect the actual baseline/diff and affected consumers to relevant contracts; return located consequential findings and coverage limits; review-only stays read-only in scope |
| Omit conceptual `aek-deliver-phase` | Adds no distinct technical selection/output beyond implementation; reconcile architecture and MIGRATION rather than create a duplicate skill or alias |
| Preserve direct/no-skill routes | Optional profile omission changes neither mandatory technical policy nor existing entry routes; native installation is an independent selected subset |

The following is a source-contract review against installed Superpowers 6.4.2
and current local owners, not an observed agent-compliance matrix. Local policy
replaces the listed conflicting upstream defaults without patching plugin files.

| Overlap | Authoritative owner and effective disposition |
| --- | --- |
| Design approval and small fixes | `delivery-workflow.md#minimal-task-contract` owns material decisions. Implementation reuses accepted design and handles a settled small fix without another architecture phase; neither skill grants unresolved design approval |
| Canonical spec/plan location | Adopted PLANS and existing task own artifacts. No `docs/superpowers/` store or helper ledger is introduced by an AEK entry |
| Stage stopping and Git | `work-modes.md` owns progression/permissions. The implementation entry does not import executing-plans continuous execution, worktree or commit defaults; existing authorization is reused |
| Test selection and cadence | `verification.md` plus resolved policy settings own TDD suitability, required gates and phase/task batching. The skill does not add a universal Red–Green cycle or tests for every edit |
| Review scope and independence | `verification.md#review-boundaries` owns scope and independence conditions. Coordinator use of the review entry is not independent review; requesting-code-review does not force dispatch or a Git-SHA-only baseline |
| Review findings and fixes | Same verification owner governs in-scope resolution during authorized implementation. Review-only requests return findings without fixes; optional/incidental issues do not become scope by being found |
| Delegation and models | `orchestration.md`, model configuration, saved choices and actual tools own a selected dispatch. No role, worker or model setup is selected by these entry triggers |
| Evidence reuse | `verification.md#reuse-evidence-before-repeating-work` owns validity and rerun reasons. A skill load, handoff or new turn does not invalidate unchanged evidence; missing gates remain missing |
| Language | `core.md#reasoning-and-communication-language` owns artifact/response language, independent of English plugin examples |
| Procedure composition and absence | `superpowers.md` owns adaptations and scoped fallback. New composition text does not route back into an AEK skill; the optional guide does not become a required dependency of Superpowers |
| Technical applicability and exceptions | Local project facts plus existing core/technology entries own the rules. Skills follow affected contracts and accepted exceptions without expanding to all profiles or auditing neighboring features |

Selection review covered an authorized feature, a settled bug fix, review-only
work, a completion review, an unresolved material design and a wording-only edit.
The first two fit implementation; review requests/boundaries fit review; unresolved
design follows its existing decision gate; wording-only work retains direct rules.
These are reviewed trigger contracts, not executed trigger tests. PS-05 must test
the final contents with Superpowers present/absent and unrelated work; no current
observation demonstrates improved quality, cost or selection reliability.

## Stage 4 adoption disposition — 2026-10-11

PS-04 retains MIGRATION as the sole adoption/update/recovery owner. Its optional
skill section now requires a selected native subset and explicit handling of
unowned same-name entries, dropped selections and missing accepted contents.
The record template maps inactive resources to native destinations and local guide
references, pointing to existing managed-path evidence rather than duplicating
accepted hashes. The integration skill routes to those sections and includes the
native subset in its result. No task-skill procedure or technology rule changed.

The [adoption observations](2026-10-11-project-skills-adoption.md) distinguish
15 automated layout/profile combinations from 13 coordinator-led import/update/
recovery scenarios. Fixed local exceptions, task location, model choices and gates
survived the applicable operations. Non-Markdown routes received explicit checks.
The shared fixture adapter now accepts an explicit reviewed list of conditional
host/framework source references; unknown missing required routes still fail.
This is test preparation, not a production installer or expanded profile closure.

Inventory remains 36 profiles, seven required profiles, 183 standards Markdown
files and six source skills. None became active in this source checkout or a real
consumer. Current three-entry behavior, Superpowers composition and comparative
benefit remain PS-05 work; the earlier native observations retain their old inputs.

## Final integrated review and acceptance — 2026-10-11

PS-07/PS-08 reconcile the preceding dated inventory with the final source package.
Review was performed by the coordinator, not an independent reviewer. Its boundary
is the whole task delta: 12 tracked-file changes, 20 new task files and the two
previously untracked roadmap/feasibility navigation additions. The four unrelated
older diagnostic/pilot documents remain outside the changed scope. Pre-stage
contents are preserved under `/tmp/aek-ps06-final-ig9vqkad`; no Git write, consumer
rollout, native installation or new model trial is part of this final stage.

### Coverage and preserved ownership

The PS-01 baseline and HEAD retain the original meanings and file identities.
Reconciliation found 183 standards Markdown files and six inactive source skills.
Of the original 182 standards files, 180 are byte-identical; only catalog and
Superpowers received the reviewed additive routing text. Their previous heading
anchors still exist. All 35 original profile records, catalog schema/shared assets,
entry alternatives and seven required profiles are unchanged. The one added profile
is optional `project-workflows`; all 36 closures resolve without diagnostics.
The old 182 file-owner rows above remain applicable, including every conditional
technology/example route; the following entries complete the after-state map.

| Owner or affected surface | Final responsibility and disposition |
| --- | --- |
| `standards/project-skills.md` | New owner for selecting local task inputs and design/implementation/review result boundaries; no technology or lifecycle policy moves here |
| Three `templates/skills/aek-*/SKILL.md` task entries | Narrow native triggers, technical-reference selection and result boundary; each routes to the shared guide and existing procedure owners |
| `standards/catalog.md`, `standards/catalog.toml` | Optional availability; new profile adds only its guide and three inactive templates, with no technology selection or recursive reading requirement |
| `standards/superpowers.md` | Procedure composition and local adaptations; no callback selecting another AEK entry, copied plugin policy or automatic dispatch |
| Root/native entry templates | Keep mandatory direct core/stack routes and fill only selected native paths; source templates remain inactive |
| MIGRATION, adoption record, integration skill | One adoption/update/recovery owner, selected native subset, path adaptation and existing managed-content evidence; ordinary task work needs no source/provenance lookup |
| Architecture, README and maintenance commands | Distinguish source availability, observed Codex native behavior, explicit Superpowers procedure routing and unverified client surfaces |
| Fixture helpers, regression tests and behavioral inputs | Fixed catalog/path, preservation and acceptance checks; no installer, autonomous semantic judge or production runtime added |
| Plans, specification and dated research | Canonical progress/design and conditional evidence; earlier run identities/results remain historical rather than relabelled |

The three observed native copies and their local guide were compared with current
source adaptation and matched. No native task skill was activated in the source
checkout. Review covered exact changed/new contents, previous local work, entry
callers, selected resource closures and native/literal path consumers. It reused
still-valid technology evidence because no technology contract/example changed;
there is no new vendor/API or HTTP-runtime claim.

### Findings and resolved boundaries

| Finding or review question | Consequence and disposition |
| --- | --- |
| Current README still said the three-entry behavior trial was pending | Stale support information after PS-05/06; replaced with dated observed-client evidence and explicit Superpowers discovery limits |
| Architecture still emphasized only the source-contract stage | Linked the bounded final behavior/support record; retained the distinction between valid files, discovery, use and adoption |
| Maintenance navigation mentioned outstanding behavior gates without the completed trial route | Updated the dated record wording and linked standalone fixture commands; the documented source analyzer now includes the preparation helper |
| Original conceptual design/delivery names | Replaced only as concepts by the selected feature entries; no old native alias or consumer file was removed. Existing compatibility paths and the former design-adoption anchor remain |
| Similar summaries in entries, guide and record | Retained as navigation/output reminders; no competing policy values or full lifecycle copies. Technical rules, planning, checks, Git, delegation, models and recovery keep their previous owners |
| Superpowers absent from the private CLI native catalog | Not represented as native plugin activation. Actual composed procedures were read through the identical explicit route in both conditions; unavailable-source fallback was separately observed |
| Optional stronger expression-Any analysis of the behavioral test | Recorded test-analysis limit, not a domain defect or waived required gate; strict required analysis passed and no new `Any` contract/suppression was introduced |
| Verbose trial documents and repeated reading | Recorded overhead limits; no evidence supports a universal quality/cost improvement. No functional regression or new mandatory reading queue was introduced |
| Independent review and other client execution | Neither claimed. Coordinator review is the selected source-review scope; Claude/Cursor retain static/reference support and real consumer adoption remains separate |

No material in-scope finding remains unresolved. Unchanged vendor APIs, unrelated
historical pilot proposals, other-client activation and real consumer installation
were not independently revalidated; their stated limits prevent them becoming
unsupported claims in this package. No old technical route was retired as cleanup.

### Final acceptance map

| Criterion | Disposition and actual evidence |
| --- | --- |
| AC01 | Met: accepted specification and canonical stages distinguish consumer task skills from source maintenance; every execution stage records its boundary |
| AC02 | Met at source/route scope: all 182 original owner rows retained, original technology contents/profiles unchanged, new guide/profile explicitly mapped; V01/V02 reconciliation above |
| AC03 | Met for the observed Codex surface: precise native triggers/local guide routes, implicit reads of all three entries and current explicit review; V03/V07/V09. Distinct value is the named technical-selection/result entry, not a demonstrated benchmark improvement |
| AC04 | Met at the specified file/procedure scope: 84 regression tests, 15 layout/profile combinations and 13 instruction-led adoption/update/recovery outcomes; V02–V06. No autonomous installer-compliance claim |
| AC05 | Met at reviewed source and bounded behavior scope: existing owners retained, no recursive procedure/extra plan/unauthorized write observed; V07/V08/V10. Automatic native Superpowers discovery remains unverified in the private runtime |
| AC06 | Met: current navigation names Codex CLI 0.162.1 observations and preserves explicit static/fallback limits for other surfaces; V03/V07–V09 |
| AC07 | Met: actual integrated source, adapted native copies, new files and earlier local work reviewed; current-information findings repaired, affected checks passed; coordinator-only V10 |
| AC08 | Met: durable inputs/prompts/commands/identities and outcome limits retained inside AEK; recovery uses existing managed contents and intervening-edit reconciliation; no premature technical-path retirement |

Evidence owners: the [validation chronology](2026-10-11-project-skills-validation.md),
[portable adoption cases](2026-10-11-project-skills-adoption.md) and
[current behavior/support record](2026-10-11-project-skills-behavior.md).
The bounded observations satisfy this source-package scope, not arbitrary tasks,
all native clients, statistical superiority or deployment in existing consumers.

### Adoption and rollback handoff

Adopt only in a separately authorized target through
[MIGRATION's selected-task route](../../MIGRATION.md#optional-project-task-skills).
Choose the optional workflow profile independently of technology profiles and
install only the selected native subset. Preserve target gates, settings, task
location and accepted exceptions; record adapted paths/content, then check the
actual selected bundle and native files. Direct core/technology rules remain usable
when the workflow profile or Superpowers is unavailable.

For rollback/update conflicts, the authoritative
[partial application and recovery procedure](../../MIGRATION.md#partial-application-and-recovery)
compares current files with the operation's written result before restoring prior
adapted contents or absence. Keep retrievable accepted/operation snapshots outside
discovery, preserve later user/record edits, and reconcile dropped selections or
unowned same-name entries explicitly. Disposable trial snapshots are not durable
consumer recovery bases. Do not reset this source checkout or delete shared
consumer directories to undo an adoption.

Final checks: 210 source artifacts and 13 task/evidence/fixture documents passed
without errors; strict mypy 2.1.0 passed for six source modules under the documented
Python 3.11 analyzer contract. The 84 PS-04 tests and ten completed PS-05 native
observations retain their unchanged relevant inputs and are reused. No new model
call or application build was needed for these final prose/navigation corrections.
