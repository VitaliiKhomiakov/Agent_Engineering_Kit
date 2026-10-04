# Technology profile boundaries — audit and staged implementation plan

**Date:** 2026-10-04.
**Status:** Audit and planning complete. The user approved starting the plan on
2026-10-04. Stages 0–5 and their acceptance checks are complete; awaiting user
review. No commits, pushes or consuming-project writes were performed for this plan.

**Goal:** Check whether existing language, runtime, framework and library topic
directories can be selected independently, identify unwanted coupling, and plan
compatible profile separation with working references in the source library and
selected target bundles.

## Scope and baseline

- Instruction root and execution checkout:
  `/home/vitalii/Documents/Local_Projects/Agent_Engineering_Kit`.
- Canonical audit, findings and follow-up owner: this document.
- Baseline: clean checkout at `0614bb7965875ab57791777609be6eb51bc8500a`;
  this document was absent before the audit.
- Planning expansion preserves the already-untracked audit at
  `/tmp/aek-profile-plan-k7kkuqd6/2026-10-04-profile-boundary-audit.md`.
  The checkout is unchanged from the audit baseline. Keep this scoped copy
  through plan review; capture fresh scoped baselines before implementation.
- Authorized scope: repository-wide investigation of profile separation and
  related routing problems, following the user's PHP and Node.js observations.
  The user's follow-up also requests checking root entry/topic-directory roles
  and preserving combinations such as PHP/Symfony, Node.js/TypeScript and
  Angular/TypeScript, with TypeScript shared across participating technologies.
  The planning request explicitly requires checking cross-file references for
  dead links. The subsequent instruction to start accepts the proposed design
  and starts stage 0 under the existing per-stage human checkpoints. The next
  instruction to proceed authorizes stage 1 under the same checkpoints. The
  subsequent continuations authorize stages 2–5 in sequence, each with its
  review checkpoint.
- Inline work under [local Superpowers adaptations](../../standards/superpowers.md).
  Stage 0 writes only this canonical plan; later profile/test changes follow the
  approved stages and checkpoints. No delegation, target writes, staging, commits
  or pushes. No model setup is needed for this inline work.
- Reviewed all 23 catalog profiles: seven shared policies and 16 technology or
  technology-structure profiles, covering 22 declared technology labels.
  Inspected entry documents, dependency/resource closures, cross-topic Markdown
  routes, relevant topic context, README and target-entry navigation, and the
  checker's catalog contract. This is not a new audit of every technology API,
  example runtime or sentence in the library.
- Preserve historical evidence, existing topic contents and accepted target
  imports. Any future migration needs its own approved scope and compatibility
  decisions under [MIGRATION](../../MIGRATION.md#repeat-and-update).

## Acceptance and progress

- [x] **AUD-01:** Inventory every profile and distinguish directories, entry
  documents, catalog selection and conditional reading.
- [x] **AUD-02:** Calculate dependency closures and reproduce combined-family
  and downstream bundle coupling for the scenarios below.
- [x] **AUD-03:** Inspect cross-topic routes and separate confirmed catalog
  limitations, wording ambiguities and valid optional integrations.
- [x] **AUD-04:** Record findings, remediation boundaries, acceptance scenarios
  and the limits of executed evidence; validate this document and its links.
- [x] **AUD-05:** Classify every root standards file and check additive profile
  composition and shared TypeScript ownership against the user's follow-up.
- [x] **PLN-01:** Prepare the staged graph/compatibility design, affected-file
  groups, reference-validation procedure and acceptance scenarios.
- [x] **REM-01:** Agree the profile decomposition and legacy-ID compatibility
  design before restructuring catalog entries and navigation.
- [x] **REM-02:** Implement the approved changes and verify narrow bundles and
  retained legacy selections. Stages 1–5 and final acceptance checks are complete.

## What the current structure actually means

Topic directories already separate the detailed content. For example, `php/`,
`symfony/` and `doctrine/` exist independently. A short entry plus detailed topics
is a sound arrangement; their coexistence is not evidence of duplicated policy.

The [catalog contract](../../standards/catalog.md#assemble-a-portable-bundle)
includes every resource of a selected profile and its dependency closure.
Task-specific reading remains conditional. Consequently a combined profile can
force unused instruction files into a bundle without requiring installation of
those application packages or unconditional reading of their instructions.
The finding is selection granularity, not a catalog-schema violation or proof
that agents have applied an irrelevant framework.

## Root entries, detailed topics and technology composition

The `standards/` root has 27 files: 15 technology entry documents, the additional
`nextjs-feature-structure.md` architecture topic, seven shared policy owners and
four catalog/policy-configuration files. They are not all shortened technology
instructions. The 15 technology entries range from 39 to 87 lines; task tables
route to focused topics. Longer shared policy documents own their full rules.
File count or root placement alone is not a demonstrated defect.

Preserve these distinct responsibilities:

| Layer | Responsibility | Example |
| --- | --- | --- |
| Shared policy owner | Cross-technology constraints and verification policy | `core.md`, `verification.md` |
| Technology entry | Applicability, essential rules and task routes | `typescript.md` |
| Technology topic | Detailed rule, rationale, relevant checks and examples | `typescript/contracts-structure.md` |
| Framework/host specialization | Integration-specific behavior using shared contracts | Angular templates, Nest validation metadata, Node resource lifetime |
| Catalog | Select available resources and their dependencies | `catalog.toml` |

Short reminders and specialized applications are not automatically duplicate
policy owners. For example, the TypeScript contracts topic explicitly assigns
named-interface/strictness ownership to its entry; Nest transport guidance links
to that entry and explains when actual runtime validation needs DTO classes.
The evidence does not justify deleting all entry summaries or merging all topic
files into the root. This inspection does not certify that every sentence in
every topic is free of redundancy.

Profiles must compose rather than become mutually exclusive:

| Actual stack | Rules that should compose |
| --- | --- |
| PHP with Symfony | Shared policy + PHP + Symfony; Doctrine only if selected/used |
| PHP with Doctrine without Symfony | Shared policy + PHP + Doctrine |
| Node.js JavaScript | Shared policy + JavaScript + Node.js |
| Node.js TypeScript | Shared policy + JavaScript + TypeScript + Node.js |
| Angular TypeScript | Shared policy + JavaScript + TypeScript + Angular; Node application rules only for relevant host work |
| Angular frontend and NestJS backend | One shared TypeScript policy plus each project's framework/host rules |
| React TypeScript without Next.js | Shared policy + JavaScript + TypeScript + React |

These are intended rule combinations, not proposed new runtime requirements.
The existing graph already composes Node.js/TypeScript and Angular/TypeScript;
union/closure inspection also showed that selecting Angular and NestJS shares
one TypeScript entry and its resources. PHP/Symfony is currently provided as a
combined profile that additionally includes Doctrine. The desired improvement
is finer selection while retaining valid combinations and deduplication.

## Complete profile coverage

The shared profiles `core`, `work-modes`, `verification`, `delivery-workflow`,
`superpowers`, `orchestration` and `model-configuration` were included in graph
inspection. Their required availability is an explicit framework policy, not
the same defect as coupling independent technologies. Inactive role resources
do not activate delegation. This audit proposes no split of those seven policies.

| Technology/structure profile | Selection assessment |
| --- | --- |
| `python-fastapi` | Python, Pydantic and FastAPI share one indivisible resource list |
| `php-symfony-doctrine` | PHP, Symfony and Doctrine share one indivisible resource list |
| `go-gin` | Go and Gin share one indivisible resource list |
| `nodejs-typescript` | JavaScript and Node.js share one resource list; TypeScript has its own profile |
| `typescript` | Separate content; dependency on `nodejs-typescript` also includes Node.js for browser-only work |
| `nestjs` | Separate profile; Node.js/TypeScript availability fits the declared local entry contract; TypeORM is optional |
| `typeorm` | Separate from NestJS; includes Node.js/TypeScript through dependencies; assess host conditions during decomposition |
| `angular` | Separate from NgRx; indirectly includes Node.js through TypeScript |
| `ngrx` | Angular dependency is intentional; inherits the TypeScript/Node.js coupling |
| `nextjs` | React and Next.js share one list; TypeScript is a dependency even for the explicitly supported JavaScript React scenario |
| `nextjs-feature-structure` | Next.js-specific topic; dependency on `nextjs` is appropriate; also supplied as a `nextjs` resource |
| `sqlalchemy` | Separate persistence profile; inherits FastAPI/Pydantic resources through `python-fastapi` |
| `psycopg` | Python/PostgreSQL availability fits its entry; the Python dependency also includes FastAPI/Pydantic |
| `postgresql` | Independent database profile; does not select Psycopg or SQLAlchemy |
| `docker` | Coherent container profile with conditional build/Compose sections; no application-language dependency |
| `unreal-engine` | Coherent engine/editor profile; C++, Blueprint and optional editor workflows are task-conditioned; does not select Python/FastAPI automatically |

All standard Markdown/TOML artifacts have catalog ownership through sources,
resources or shared assets. No missing paths, duplicate IDs or dependency cycles
were reported by the source checker. A path used both as a resource and a profile
source is deduplicated availability, not two copies of the same rule.

## Findings

### PB-01 — Five combined families prevent independent selection

Confirmed in [the catalog](../../standards/catalog.toml). Existing folders are
already separated; adding more folders or renaming a single entry will not fix it.

| Intended scope | Current selection | Additional topic resources included |
| --- | --- | --- |
| PHP without Symfony/Doctrine | `php-symfony-doctrine` | Six Symfony and six Doctrine files |
| Python without FastAPI/Pydantic | `python-fastapi` | Six FastAPI and six Pydantic files |
| Go without Gin | `go-gin` | Six Gin files |
| Browser JavaScript without Node.js | `nodejs-typescript` | Six Node.js files |
| JavaScript React without Next.js or TypeScript | `nextjs` | Seven Next.js, six TypeScript, six Node.js files, plus `nextjs-feature-structure.md` |

Counts cover additional topic resources, not entry documents or shared policies.
They are not token-use measurements. Browser build tooling may use Node.js, but
that does not itself make Node.js application-server guidance relevant.

Eleven declared technology labels have no same-named profile ID: `python`,
`fastapi`, `pydantic`, `php`, `symfony`, `doctrine`, `go`, `gin`, `javascript`,
`nodejs` and `react`. Different names are allowed by the schema; the meaningful
limitation is that none offers an independent selection for its existing topics.

### PB-02 — Dependencies propagate the combined-family coupling

Reproduced dependency chains:

- `sqlalchemy -> python-fastapi`: FastAPI/Pydantic accompany SQLAlchemy-only work.
- `psycopg -> python-fastapi`: the same extra resources accompany driver work.
  Its additional `postgresql` dependency is a separate, supported relationship.
- `typescript -> nodejs-typescript`: Node.js accompanies browser-only TypeScript.
- `angular -> typescript -> nodejs-typescript`: the same propagation reaches Angular.
- `ngrx -> angular -> typescript -> nodejs-typescript`: it reaches NgRx as well.
- `nextjs -> typescript -> nodejs-typescript`: the combined React selection
  cannot omit TypeScript or Node.js resources for a JavaScript-only UI.

Splitting entries without redirecting these dependencies leaves the problem in
place. Do not remove legitimate base-language dependencies or equate a catalog
dependency with a runtime package dependency.

### PB-03 — Names obscure the ownership already present in the files

[The Node/JavaScript entry](../../standards/nodejs-typescript.md) names TypeScript
in its path/title, while its catalog technology list is JavaScript and Node.js;
the detailed TypeScript rules and catalog profile are already separate.
Likewise React-only work enters through `nextjs`, and pure Python through
`python-fastapi`. README and the root-entry template accurately repeat those
current routes, so they must change with the catalog rather than being renamed
independently. These are navigation/maintenance limitations, not broken links.

### PB-04 — Two generic topic routes need clearer applicability/ownership

- [PHP structure](../../standards/php/structure.md#modules-and-autoloading)
  directs preservation of the domain/ORM approach to Doctrine-specific model
  placement without explicitly conditioning the route on Doctrine. The target
  describes Doctrine entity mapping choices. PHP without Doctrine, or with a
  different ORM, needs an explicit applicability boundary at this route.
- [React forms](../../standards/react/forms-contracts.md) assigns shared runtime
  validation ownership to the TypeScript entry. The supported JavaScript React
  case should have a language-neutral/core or JavaScript owner, with TypeScript
  guidance conditional on its actual use. Merely splitting the catalog would
  leave this route behind.

These are instruction-routing ambiguities with concrete non-Doctrine/non-TypeScript
scenarios. No observed agent run established an unwanted migration or installation.
The React component rule phrased “under TypeScript” is not classified as an
unconditional requirement to convert JavaScript. Other conditional links must
be assessed in context, not flagged merely for crossing a directory boundary.

## Valid boundaries retained by the audit

- NestJS does not select TypeORM; its entry and lifecycle links condition that
  integration on actual use. TypeORM's Nest integration is also conditional.
- Angular does not select NgRx; its reactivity link explicitly says it is for
  NgRx-specific APIs. NgRx selecting Angular is the reverse, intentional relation.
- React's Next.js verification/feature links are explicitly conditioned on Next.js.
- Doctrine's link to Symfony runtime effects is explicitly conditional.
- PostgreSQL does not select a driver. SQLAlchemy does not select PostgreSQL.
- Docker's illustrative Node/Nest example is not a catalog dependency on those
  profiles. Unreal's Python scripting route is conditional.
- ORM/DBAL, NgRx package alternatives, Docker build/Compose and Unreal subsystems
  do not require mechanical one-file/one-profile splits solely for symmetry.

## Approved design

Keep root entry documents and their existing topic directories. Introduce
independent profiles, compose them through dependencies and retain old combined
IDs/paths as explicitly labelled compatibility aggregates. This adds selection
precision without deleting old routes or duplicating full technology policies.

Alternatives considered: renaming/removing old entries immediately would break
installed selections and historical anchors; adding only conditional prose would
leave bundle coupling unchanged. The recommended approach preserves compatibility
while directing new selections to the independent entries below.

### Profile graph

Each new ID below uses `standards/<id>.md`; existing topic directories retain
their paths. Dependencies mean instruction availability, not package installation.
Seven required shared profiles and catalog schema 1 remain unchanged.

| Profile | Direct technology/base dependencies | Resource ownership |
| --- | --- | --- |
| `php` | `core` | Existing `php/` topics/examples |
| `symfony`, `doctrine` | `php` for each | Their respective directories |
| `python` | `core` | Existing `python/` topics/examples |
| `pydantic` | `python` | Existing `pydantic/` topics/examples |
| `fastapi` | `python`, `pydantic` | Existing `fastapi/` topics/examples |
| `go` | `core` | Existing `go/` topics/examples |
| `gin` | `go` | Existing `gin/` topics/examples |
| `javascript` | `core` | Existing `javascript/` topics/examples |
| `nodejs`, `typescript` | `javascript` for each | Their respective directories |
| `react` | `javascript` | Existing `react/` topics/examples |
| `nextjs-framework` | `react` | Existing `nextjs/` topics/examples and `nextjs-feature-structure.md` |
| `nestjs` | `nodejs`, `typescript` | Existing NestJS resources |
| `typeorm` | `typescript` | Existing TypeORM resources; Node host guidance conditional |
| `angular` | `typescript` | Existing Angular resources |
| `ngrx` | `angular` | Existing NgRx resources |
| `sqlalchemy` | `python` | Existing SQLAlchemy resources |
| `psycopg` | `python`, `postgresql` | Existing Psycopg resources |
| `nextjs-feature-structure` | `nextjs-framework` | Existing structure document |

PostgreSQL, Docker and Unreal retain their existing `core` dependencies/resources.
Select TypeScript alongside Node.js, React or Next.js where authored code uses it;
Angular/NestJS retain their existing mandatory local TypeScript contracts.
Next.js and TypeORM select Node.js guidance for actual Node host work, rather than
assuming that all consumers execute in that host. Before changing host-related
dependencies, check the affected official supported-version contracts and record
the evidence; a conflict requires adjusting this design before dependent edits.
No fixture upgrades or changes to application-language policy are authorized.

`nextjs-framework` is proposed deliberately: `nextjs` currently also selects
React, TypeScript and Node.js resources. Reusing that ID for a narrower meaning
would undermine the promised legacy compatibility. The plan adds twelve entry
files and twelve profile IDs; the five existing aggregates remain available.

### Compatibility contract

| Retained ID and matching source path | Aggregate dependencies after separation |
| --- | --- |
| `php-symfony-doctrine` | `php`, `symfony`, `doctrine` |
| `python-fastapi` | `python`, `pydantic`, `fastapi` |
| `go-gin` | `go`, `gin` |
| `nodejs-typescript` | `javascript`, `nodejs`; TypeScript remains conditional as in its current catalog selection |
| `nextjs` | `nextjs-framework`, `typescript`, `nodejs` |

Aggregate files become compatibility navigation, not second full policy owners.
Retain every existing heading anchor in those five files using short routes to
the corresponding current owner. Their closures must retain all previously
supplied source/resource paths; changed contents are handled by normal reviewed
updates. Do not make independent profiles depend back on an aggregate.
The old `nextjs` also retains `nodejs-typescript.md` as an explicit compatibility
resource after it no longer receives that entry through TypeScript.
The feature-structure file being both a resource and profile source is supported
deduplication; resource inclusion is not an additional dependency edge.

New imports choose independent profiles by actual stack. Existing imports retain
their recorded selections unless a reviewed update changes them. Preserve local
edits, old accepted snapshots and history using the existing B/C/N comparison.
Neither profile separation nor a smaller selection authorizes deletion of
previously imported files. Do not rewrite historical plans/research to describe
the new graph; retain their links through compatibility paths and anchors.

## Implementation stages

Use inline execution in the current checkout after approval. Default to one
completed stage, its checks and user review before the next stage. No routine
commits, push, branches, worktrees, delegation or consuming-project writes.
Record baselines, decisions, checks and progress here; retain existing AUD/REM IDs.

### Stage 0 — Confirm design and capture reference contracts

- [x] **IMP-00:** Review the proposed graph and legacy-ID/anchor behavior;
  resolve material changes in this document and close REM-01 after approval.
- [x] **IMP-01:** Snapshot affected dirty/untracked files or record clean Git
  baselines, old profile resource closures and old entry anchors outside active
  instruction discovery. Preserve both sides of any subsequently approved move.
- [x] **IMP-02:** Inventory incoming/outgoing references for all five aggregate
  files and affected topic owners. Classify Markdown paths/fragments, catalog
  values, inline/fenced path literals, TOML instructions, native imports and
  historical references. Record each route's final owner and applicability.

Result: approved graph plus a bounded route/compatibility inventory. Baseline
searches currently find 12 live files mentioning `python-fastapi`, two mentioning
`php-symfony-doctrine`, 11 mentioning `go-gin`, eight mentioning
`nodejs-typescript`, and 15 mentioning `nextjs`; these are overlapping candidate
sets, not a substitute for the stage inventory or proof of broken references.
Inspect the existing artifact checker; extend it only for an actual unsupported
requirement, not to add a second installer or a permissive link-exemption system.

### Stage 1 — PHP/Symfony/Doctrine and Go/Gin

- [x] **IMP-10:** Create `standards/php.md`, `symfony.md`, `doctrine.md`,
  `go.md` and `gin.md`; distribute existing entry essentials/routes to their owners.
- [x] **IMP-11:** Add their catalog profiles; convert both old combined entries
  to compatibility navigation with retained anchors and equivalent legacy resources.
  Update return links in their topic directories and the affected README routes.
  Explicitly condition the PHP-to-Doctrine route identified by PB-04.
- [x] **IMP-12:** Add focused real-catalog selection scenarios in
  `tests/test_profile_selection.py`, following the existing standard-library
  unittest style. Verify PHP alone, Symfony without Doctrine, Doctrine without
  Symfony, their full combination, Go without Gin, Gin with Go and both old IDs.

Result/checkpoint: both families independently selectable, all affected paths and
legacy anchors working, no technology policy or example behavior changed.
Run the stage verification contract below before marking these items complete.

### Stage 2 — Python/Pydantic/FastAPI and persistence dependencies

- [x] **IMP-20:** Create `standards/python.md`, `pydantic.md` and `fastapi.md`;
  move entry ownership while retaining topic paths and supported-version conditions.
- [x] **IMP-21:** Update the catalog and `python-fastapi.md` compatibility routes;
  redirect `sqlalchemy` and `psycopg` to `python`. Update Python/Pydantic/FastAPI
  return links, persistence entry links and affected README/template literals.
- [x] **IMP-22:** Extend selection scenarios for Python alone, Pydantic without
  FastAPI, FastAPI with its bases, SQLAlchemy without FastAPI/Pydantic/PostgreSQL,
  Psycopg with Python/PostgreSQL but without FastAPI/Pydantic, and the old aggregate.

Result/checkpoint: persistence/language work no longer bundles an unused web stack;
Pydantic/FastAPI combinations retain required language/validation instructions.

### Stage 3 — JavaScript/Node.js/TypeScript and dependent profiles

- [x] **IMP-30:** Create `standards/javascript.md` and `nodejs.md`; retain
  `typescript.md` as the single strict-typing owner. Move shared language rules
  and Node host rules to their respective entries; retain old anchors in
  `nodejs-typescript.md` as compatibility routes.
- [x] **IMP-31:** Rewire TypeScript, NestJS, TypeORM and Angular dependencies as
  approved; inspect NgRx's inherited closure. Update JavaScript/Node/TypeScript
  topic routes, dependent entry links and template/README path literals together.
  Complete the supported-runtime source review before changing TypeORM host scope.
  Add an explicit `nodejs` dependency to the still-combined `nextjs` profile in
  this stage so its legacy resources survive TypeScript's dependency change.
  Retain `nodejs-typescript.md` as an explicit compatibility resource of `nextjs`,
  including after stage 4; the new dependency alone does not preserve that old path.
- [x] **IMP-32:** Extend scenarios for browser JavaScript, browser TypeScript,
  Node JavaScript, Node TypeScript, Angular without NgRx, NestJS without TypeORM,
  TypeORM without NestJS, the legacy aggregate and Angular/NestJS sharing one
  TypeScript resource set. Verify Node host selection separately from TS use.

Result/checkpoint: TypeScript composes across hosts/frameworks without copying its
rules or imposing Node server guidance on browser-only code. Until stage 4,
the existing React/Next aggregate retains its previous dependency behavior.

### Stage 4 — React/Next.js and complete navigation

- [x] **IMP-40:** Create `standards/react.md` and `nextjs-framework.md`;
  convert `nextjs.md` to the legacy aggregate and redirect the structure profile.
  Keep every existing React/Next topic/example path and legacy entry anchor.
- [x] **IMP-41:** Make React form validation route to shared JavaScript/core
  rules, with TypeScript conditional; preserve Next-specific conditions in React.
  Update all affected return links, README stack/map descriptions and
  `templates/AGENTS.root.md` literals. Inspect other entry/native templates for
  affected paths rather than assuming their Markdown links cover every route.
- [x] **IMP-42:** Document atomic and legacy selection in `standards/catalog.md`
  and `MIGRATION.md` without a second update procedure. Update `ARCHITECTURE.md`
  only where the approved resource/selection explanation requires it.
- [x] **IMP-43:** Extend scenarios for React JavaScript without Next/TS/Node,
  React TypeScript without Next/Node, Next JavaScript, Next TypeScript, explicit
  Next Node-host work, feature structure and the old `nextjs` selection.

Result/checkpoint: new UI selections are precise, old UI selections keep their
available resources, and all live navigation uses the intended current owner.

### Stage 5 — Whole-library references, portable bundles and update rehearsal

- [x] **IMP-50:** Run the full source/catalog check and explicitly scan all
  Markdown/MDC/TOML files, including examples, docs and newly created files.
  Check every retained legacy fragment against the stage-0 anchor inventory.
  Review remaining old-name references against the classified route inventory.
- [x] **IMP-51:** Complete the prepared-bundle matrix below in temporary target
  directories. Check actual copied/adapted files, not only the source graph.
- [x] **IMP-52:** Rehearse an unchanged legacy selection and a reviewed change
  to independent profiles using baseline/modified fixtures. Demonstrate unchanged
  local edits and immutable accepted snapshots, explicit conflict/retirement
  handling and no automatic removal of previously managed resources.
- [x] **IMP-53:** Review actual diffs and new files, record check outcomes and
  limits, and close REM-02 only when all acceptance criteria pass. Keep unrelated
  version pins, examples and historical evidence unchanged. Stop for user review.

Result: no unresolved local reference defects in checked source/bundle scopes,
verified independent and combined selections, and a compatible update path.

## Reference and verification contract

At each stage boundary, run scoped artifact/link checks, relevant selection
scenarios, legacy closure/anchor comparisons and `git diff --check`; inspect new
files separately. Repair in-scope failures before the checkpoint. Reuse earlier
results when their inputs remain valid; stage 5 adds cross-family/full-scope checks.

The new selection tests must assert observable bundle boundaries, not copy the
implementation's dependency table as expected output. Include positive and
negative resource expectations and unchanged control selections (PostgreSQL,
Docker, Unreal). Reuse the checker tests for missing paths and unknown anchors;
add only uncovered regressions. If Python tools/tests change, run their focused
unittest suite and the documented strict analyzer, including the new test module.
Do not introduce application dependencies or rerun unchanged runtime fixtures.

Representative commands, with actual selected IDs/paths substituted per stage:

```sh
python3 tools/check_instruction_artifacts.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p 'test_profile_selection.py'
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p 'test_instruction_artifacts.py'
python3 tools/check_instruction_artifacts.py --root /tmp/aek-profile-target --bundle-dir .agents-framework --profile react --profile typescript
git diff --check
```

The temporary target command is planned evidence, not a claim that such a target
already exists. Explicit path arguments replace the checker's default body scan:
perform both the selected-closure check and a pass including every actual copied
instruction artifact, root/native entry and adoption record. For full source
coverage, supply discovered Markdown/MDC/TOML paths including untracked additions;
the default command alone does not inspect historical `docs/` or root `examples/`.

| Reference class | Required check |
| --- | --- |
| Markdown links/images and fragments | Resolve file and heading from the containing document; check source and prepared targets |
| Catalog sources/resources/dependencies | Existing schema/resource/cycle checks plus selection scenarios |
| Inline/fenced paths and profile IDs | Search old/new names; inspect each operational literal against its final root and selected IDs |
| Native imports and TOML developer instructions | Inspect actual installed location/entry routes; Markdown validation alone is insufficient |
| Legacy and historical links | Keep old paths and heading anchors reachable; preserve the original evidence claims |
| Optional cross-profile/history routes | Adapt only inapplicable/omitted routes to documented labelled source references or known source URLs; never blanket-delete unresolved links |

Portable-bundle preparation must include shared/selected closures and adapt
inactive templates versus installed entries according to MIGRATION. Classify a
missing target before changing it: required local targets stay local and checked;
optional absent profiles/history use the existing provenance/reference contract.
Do not copy every technology merely to make the checker pass. Source-relative
success must not substitute for installed-path validation. No blanket external
URL crawl is planned; verify official sources affected by actual contract changes.

Use contained layout for every positive/negative stack scenario in stages 1–4.
Exercise legacy aggregates as well as independent selections. Add flat-layout
representatives for PHP alone, Angular/TypeScript and legacy `nextjs`; include a
non-default contained directory and a nested native task/entry route to expose
incorrect relative-root assumptions. Test a multi-project Angular/NestJS workspace
with one shared TypeScript bundle and independently reachable project entries.

Optional executable examples retain their language/version contracts. A bundled
TypeScript example does not select TypeScript rules or authorize converting a
JavaScript project; choose an applicable example or keep it as an unused reference.

Before completion, demonstrate that deleting a required fixture target or using
a nonexistent fragment is detected; that an explicitly optional omitted route
can be represented without a dangling local link; and that no preservation test
silently treats an unresolved required dependency as optional. Fixtures remain
outside consuming projects, and their outcome is static adoption evidence, not
proof of client discovery, agent adherence or measured context savings.

## Executed evidence and limits

- Standard-library `tomllib` inspection enumerated all 23 profiles, 22 technology
  labels, all declared dependencies/resources and their transitive closures.
  Topic resource counts above were computed from those closures with shared
  required profiles included and duplicate paths removed.
- Inventory comparison found no uncataloged standard `.md` or `.toml` artifacts.
- Root inventory classified all 27 standard files. Closure/union checks for
  Node.js/TypeScript, Angular/TypeScript, Angular/NestJS/TypeScript and the
  current PHP/Symfony aggregate confirmed additive selection and deduplication;
  they do not prove live-agent reading behavior or target installation.
- The existing Markdown parser enumerated cross-topic local links in every
  immediate technology-topic `.md` file, excluding executable examples and the
  Superpowers compatibility directory; candidate routes were reviewed in context.
  Entry files, relevant template literals and README routes were inspected separately.
- `python3 tools/check_instruction_artifacts.py`: **193 artifacts, zero errors**
  against the unchanged baseline. Its declared checks validate catalog structure,
  paths and supported syntax, not whether a dependency is semantically too broad.
- The new audit document passed its explicit artifact check and separate
  whole-file whitespace inspection; `git diff --check` passed. Only this new
  document was added; profile contents, catalog and historical evidence are unchanged.
- No new target bundle was installed, no consuming project was changed, no
  runtime/example tests or live-agent pilot were run, and no token savings were
  measured. This audit establishes source structure and static routing findings.

### Planning expansion — 2026-10-04

Expanded this existing owner at the user's request into stages 0–5, with an
explicit proposed dependency graph, compatibility paths/anchors, per-stage
acceptance, reference-class checks, prepared-bundle scenarios and update rehearsal.
The earlier audit results remain evidence for the unchanged library only.
The expanded plan passed its artifact and whole-file whitespace checks; the
planning diff was reviewed against the saved untracked baseline. No catalog,
technology instructions, tests or target files were changed, and none of the
planned implementation commands has been represented as executed evidence.
An in-memory check of the proposed 35-profile graph found no missing dependency
IDs or cycles. Plan checks confirmed six stages, 20 unstarted implementation
items, unique progress IDs and unchanged historical audit/evidence sections.

### Stage 0 result — 2026-10-04

The user's instruction to start accepts the graph and compatibility design;
REM-01 and IMP-00 are complete. The reviewed graph check remains applicable:
35 planned profiles, no missing dependencies or cycles. TypeScript stays one
shared language profile; its use does not by itself select Node application rules.

Stage baseline and reference inventory: `/tmp/aek-profile-stage0-j8GLxj/`.
`plan-before-stage0.md` preserves the untracked plan exactly before this stage;
`baseline.json` records the checkout, original scoped hashes and 13 absent planned
paths (12 entries and the selection-test module). Clean tracked originals remain
recoverable from `0614bb7965875ab57791777609be6eb51bc8500a` and their paths.
Keep this material through implementation/review; if temporary storage disappears,
reconstruct tracked contracts from that baseline and report unavailable untracked
recovery material rather than treating current contents as the original.

`legacy-contracts.json` records required/shared plus selected resource closures
and all original heading anchors for the five retained aggregates:

| Legacy profile | Available paths including shared assets/templates | Anchors |
| --- | --- | --- |
| `php-symfony-doctrine` | 44 | 7 |
| `python-fastapi` | 44 | 6 |
| `go-gin` | 40 | 5 |
| `nodejs-typescript` | 38 | 7 |
| `nextjs` | 61 | 5 |

`routes.json` classifies 514 route/literal records in 145 files: 407 Markdown
links, 82 inline/prose literals and 25 catalog literals. Each has a source/line,
target, existing fragment where present, ownership/applicability class and planned
treatment. Counts include retained and historical references, not only changes.
`summary.json` summarizes the classes; `inventory.py` retains the reproduction.
Native TOML instructions and Claude/Cursor entry routes contain no affected
hardcoded technology paths; their shared-policy/AGENTS routes remain unchanged.

Context review corrected two mechanical-mapping hazards: external `nextjs.org`
URLs are excluded from old-profile replacements, and the FastAPI integration link
in `pydantic/verification.md` must point to `fastapi.md`, while its general return
link points to `pydantic.md`. Preserve `.agents-framework/` in target-root literals.
The existing `nodejs-typescript.md#typed-boundaries` route needs both a reachable
legacy anchor and a verified new JavaScript owner. PHP/Doctrine applicability and
React's language-neutral validation route retain their PB-04 acceptance criteria.

Verification covered the stage inventory, all discovered source instruction
artifacts (**237 artifacts, zero errors**), new-file whitespace and the scoped
plan diff; `git diff --check` passed. All five legacy closure/anchor contracts
matched the baseline, and all 13 planned new paths remained absent. No checker extension,
technology edits, runtime tests or installed target bundle were needed for stage 0.
The next stage is PHP/Symfony/Doctrine and Go/Gin separation (IMP-10 through
IMP-12); it has not started. Per the agreed direct-mode checkpoint, await review.

### Stage 1 result — 2026-10-04

IMP-10 through IMP-12 are complete. Five independent entries/profiles now own
PHP, Symfony, Doctrine, Go and Gin guidance; the catalog contains 28 profiles.
Symfony and Doctrine depend on PHP separately; Gin depends on Go. The retained
`php-symfony-doctrine` and `go-gin` IDs compose those profiles and preserve their
original resource paths and heading anchors. Their former broad selection globs
now belong to the language profiles; framework selection follows actual use.

README routes and Go/Gin topic return links use the new owners. PHP structure
and state/effect guidance, plus Symfony structure guidance, explicitly condition
Doctrine links on its use. Existing detailed policy, executable examples and
supported versions remain unchanged. The maintenance guide documents the new
selection tests and the strict analyzer command covering all three Python files.

Recovery baseline: `/tmp/aek-profile-stage1-2gfcd4nz/manifest.json` and `baseline/`
in that directory preserve the pre-edit scoped files, including the untracked
plan. The stage 0 compatibility fixture remains authoritative for old paths and
anchors. Final comparison confirmed all five legacy closures retain every original
path and all 30 anchors; only stage 1 tracked paths changed, with no example edits.

Executed checks:

- Test-first selection regressions initially failed for absent independent
  profiles/entries (`red.log`); the completed eight-test suite passes. Assertions
  cover independent/composed selections, excluded families, original topic paths
  and compatibility bookmarks using the real catalog resolver.
- The existing artifact-checker suite passes: **40 tests**. Strict mypy **2.1.0**
  passes for the checker and both test modules with the documented flags,
  `--python-version 3.11` and `--explicit-package-bases`.
- Eight contained temporary bundles pass both selected-closure validation and
  explicit validation of every copied instruction artifact: PHP (34), Symfony
  (41), Doctrine (41), their combination (48), Go (36), Gin (43), old PHP aggregate
  (49), and old Go aggregate (44). `check_bundles.py`, `bundle-results.json` and
  per-scenario logs retain the reproduction and individual route adaptations.
  Only enumerated optional integrations and historical provenance routes were
  adapted; unclassified missing targets fail preparation. Inactive template
  paths were rebased to their installed locations.
- Full source validation includes untracked additions, historical documents and
  root examples: **242 artifacts, zero errors** (`source-check.log`). Actual diff
  review, `git diff --check` and whole-file whitespace checks of new files pass.

Official contract review on 2026-10-04 checked the optional
[Symfony 7.4 Doctrine integration](https://symfony.com/doc/7.4/doctrine.html),
[standalone Doctrine ORM 3.7 setup](https://www.doctrine-project.org/projects/doctrine-orm/en/3.7/tutorials/getting-started.html)
and [Gin v1.12.0 Go constraint](https://raw.githubusercontent.com/gin-gonic/gin/v1.12.0/go.mod).
This supports profile boundaries; it is not new runtime execution evidence.
No PHP/Go fixtures or consuming projects were run or changed. Temporary bundles
provide static adoption evidence only; flat layouts, update rehearsal and live
client behavior are not covered by this stage. The broader planned checks remain
pending. No Git writes were performed. Temporary tool environments, caches and
prepared bundles are removed after checks; recovery copies, scripts and logs stay
available through review. This result remains in the existing canonical plan to
preserve stage evidence and avoid creating a second progress owner.

Next: stage 2, Python/Pydantic/FastAPI and persistence dependencies (IMP-20 through
IMP-22). Await the direct-mode human checkpoint before starting it.

### Stage 2 result — 2026-10-04

IMP-20 through IMP-22 are complete. Independent Python, Pydantic and FastAPI
entries bring the catalog to 31 profiles. Pydantic selects Python; FastAPI selects
Python/Pydantic. SQLAlchemy now selects Python, and Psycopg selects Python plus
PostgreSQL, without either persistence profile bundling FastAPI/Pydantic.
The old `python-fastapi` aggregate preserves its original resources and anchors.
All three essential-rule sections moved verbatim; examples and versions did not change.
README and topic return routes use the new owners, including FastAPI's own return
links. The conditional Pydantic-to-FastAPI integration route targets `fastapi.md`.
No affected template literal was found; the only remaining live `python-fastapi`
references are its compatibility entry and catalog identity.

The pre-stage state, including all earlier uncommitted edits in affected paths,
is preserved at `/tmp/aek-profile-stage2-g3yrsyka/baseline/`; `manifest.json`
records paths, prior absence and HEAD. Scoped diff review found no material open
issue. Keep this baseline, scripts and logs through review; task-only tools,
prepared bundles and analyzer caches were removed after checks.

Verification: **13 profile-selection tests**, including five new scenarios and
extended legacy fixtures, pass; the initial red run exposed missing atomic
profiles and unwanted web/validation resources. The **40 checker tests** pass.
Strict **mypy 2.1.0** passes on the checker and both test modules using the command
in the maintenance guide. Seven contained bundles passed selected-closure and
all-copied-artifact checks: Python (34), Pydantic (41), FastAPI (48), SQLAlchemy
(42), Psycopg (49), legacy Python (49), and FastAPI/SQLAlchemy/Psycopg together
(71). Only historical provenance and reviewed conditional absent FastAPI/React
routes were adapted; unknown missing targets still fail. Reproduction and route
adaptations remain in `check_bundles.py`, `bundle-results.json` and scenario logs.
Full source validation passed for **245 artifacts**. All five legacy closures and
30 anchors remain available. Scoped diff, whole-new-file whitespace and
`git diff --check` passed. Tests ran via standard-library unittest discovery;
selection/checker outputs are retained in their respective logs.

Official source review on 2026-10-04 checked
[FastAPI 0.138.0 dependencies](https://raw.githubusercontent.com/fastapi/fastapi/0.138.0/pyproject.toml),
[Pydantic 2.13.4 dependencies](https://raw.githubusercontent.com/pydantic/pydantic/v2.13.4/pyproject.toml),
[SQLAlchemy 2.0 database integration](https://docs.sqlalchemy.org/en/20/intro.html#installing-a-database-api)
and [Psycopg 3.3.6 metadata](https://raw.githubusercontent.com/psycopg/psycopg/3.3.6/psycopg/pyproject.toml).
These support the dependency boundaries; they do not upgrade fixture versions or
constitute runtime evidence. Prepared bundles are static fixtures, not client
adoptions. No application/database tests, consuming-project writes or Git writes
were performed. Broader layout/update checks remain in stage 5.

Next: stage 3, JavaScript/Node.js/TypeScript and dependent profiles (IMP-30 through
IMP-32), after the direct-mode human checkpoint. Keep this record in the canonical
plan so the earlier evidence and remaining stages retain one progress owner.

### Stage 3 result — 2026-10-04

IMP-30 through IMP-32 are complete. JavaScript and Node.js entries bring the
catalog to 33 profiles. TypeScript now selects JavaScript; NestJS selects Node.js
and TypeScript; TypeORM selects TypeScript with Node host guidance conditional.
Angular's existing TypeScript dependency and NgRx's Angular dependency remain
unchanged: their closures now exclude Node resources unless Node is selected.
Shared language/validation guidance moved to JavaScript, host obligations to Node,
and TypeScript's mandatory strictness/interface rules retain their existing owner.
README, the root-entry template and affected topic/dependent routes were updated.

Compatibility detail: the still-combined `nextjs` now explicitly depends on Node
and retains `nodejs-typescript.md` as a resource. Node alone would preserve host
rules but lose that previously supplied public entry. Carry the resource forward
when converting `nextjs` in stage 4. The old Node aggregate still selects only
JavaScript/Node; TypeScript remains conditional as before. All five old closures
and all 30 original heading anchors passed the stage 0 fixture comparison.

Official host review checked the pinned
[TypeORM 0.3.27 README](https://raw.githubusercontent.com/typeorm/typeorm/0.3.27/README.md),
[current platform documentation](https://typeorm.io/docs/help/supported-platforms/)
and [1.0 platform changes](https://typeorm.io/docs/releases/1.0/upgrading-from-0.3/#platform-requirements)
on 2026-10-04. Both documented generations include non-Node hosts; driver/runtime
compatibility must still be established for actual use. The existing TypeScript
instruction dependency is local policy, not a claim that TypeORM forbids JavaScript.
No runtime example, dependency pin or supported target was upgraded or executed.

Pre-stage recovery copies and hashes are at `/tmp/aek-profile-stage3-eyiss4vh/`
(`baseline/` and `manifest.json`), including earlier uncommitted inputs. Hash
comparison confirmed every pre-existing file outside this stage's scope unchanged.
Actual scoped diff and new entries were reviewed; no material finding remains.

Executed evidence: **24 selection tests** (11 new scenarios plus expanded legacy
coverage), **40 checker tests**, and strict **mypy 2.1.0** on the checker and both
test modules pass. Initial red tests exposed missing independent entries and
unwanted Node resources. Commands follow the maintenance guide; test logs and
resolved analyzer packages remain beside the baseline. Full source validation
passed for **247 artifacts**; affected report checks, whole-new-file whitespace
and `git diff --check` also pass.

Twelve contained bundles passed selected-closure and all-copied-artifact checks:
JavaScript (34), TypeScript (41), Node (41), Node/TypeScript (48), Angular (48),
NestJS (55), TypeORM (48), NgRx (57), legacy Node (42), legacy Next.js (65),
Angular/NestJS (64) and TypeORM/Node (55). The Angular/NestJS fixture has separately
reachable `apps/web/AGENTS.md` and `apps/api/AGENTS.md` entries sharing one physical
TypeScript entry/topic set. Only explicitly reviewed optional integrations and
historical provenance were adapted; unclassified missing targets still fail.
`check_bundles.py`, `bundle-results.json` and scenario logs retain reproduction.
These are static fixtures, not live client adoption or context-saving evidence.
Temporary bundles, analyzer environment and caches were removed after checks;
recovery copies, scripts and logs remain through review. No Git writes were made.

The canonical plan now exceeds 700 lines. Growth review keeps it together because
its approved graph, compatibility contract and dated stage evidence share one
resumption lifetime; separate stage ledgers would duplicate progress ownership.
Next: stage 4, React/Next.js and complete navigation (IMP-40 through IMP-42), after
the direct-mode human checkpoint. Remaining layout/update checks stay in stage 5.

### Stage 4 result — 2026-10-04

IMP-40 through IMP-43 are complete. Independent `react` and `nextjs-framework`
entries complete the approved 35-profile graph. React selects JavaScript;
Next.js selects React. TypeScript and Node host guidance compose separately.
The `nextjs-feature-structure` profile selects the new Next.js profile. The old
`nextjs` retains React, Next.js, TypeScript, Node and its explicit legacy Node
entry resource, preserving all original paths and bookmarks.

React form validation now routes to shared JavaScript/core owners. React props
interfaces and Next.js type-check/version instructions explicitly apply when
TypeScript is used. Runtime-specific Next.js rules, including Cache Components'
Node requirement, remain intact. Entries distinguish deployment from actual
build/toolchain work; narrower selection does not waive relevant host contracts.
All executable examples and version pins remain unchanged and conditional.

README, architecture, root-entry template, topic return routes and JavaScript's
UI routes use the independent owners. The catalog owns selection/legacy-ID
semantics; MIGRATION links that contract and retains its existing reconciliation
procedure. Native/inactive templates were searched for affected literals; only
the root-entry template needed UI route changes. Remaining live old-file routes
are deliberate catalog compatibility entries/resources; historical references
were preserved. Full portable/native layout coverage remains in stage 5.

Source review on 2026-10-04 checked React's
[TypeScript guide](https://react.dev/learn/typescript) and the Next.js manuals
labelled 16.3.7 for [runtime choices](https://nextjs.org/docs/app/api-reference/edge)
and [static exports](https://nextjs.org/docs/app/guides/static-exports).
This supports language/host applicability, not fixture upgrades, a new framework
API audit or execution of a production React/Next application.

Pre-stage copies and hashes are retained at `/tmp/aek-profile-stage4-zdylz19a/`
(`baseline/`, `manifest.json`). Hash checks preserved every pre-existing file
outside stage scope, including earlier work and examples. The actual scoped diff,
new entries and changed applicability rules were reviewed without an open material
finding. The existing documented plan-growth decision still applies: retain one
canonical graph/progress/evidence owner rather than split its stage history.

Executed checks: **30 profile-selection tests**, **40 checker tests**, and strict
**mypy 2.1.0** on the checker and both test modules pass. Six new UI scenarios and
expanded legacy assertions first failed for absent profiles/entries. Seven
contained bundles pass both selected-closure and all-copied-artifact checks:
React (42), React/TypeScript (49), Next.js (51), Next.js/TypeScript (58), Next.js/Node
(58), feature structure (51) and old Next.js (67). Only reviewed optional absent
technologies and historical provenance were adapted; unknown missing targets fail.
Full source validation passes for **249 artifacts**; all five legacy closures and
30 original anchors are preserved. Report checks, new-file whitespace and
`git diff --check` pass. Test/bundle logs, reproduction script, route adaptations,
scoped diff and analyzer package versions remain with the baseline. Task-only
environments, caches and prepared bundles were removed after verification.

No application tests, consuming-project writes or Git writes were performed.
These checks establish static source/prepared-bundle behavior, not live client
adoption. Next: stage 5 (IMP-50 through IMP-53), completing reference/layout coverage
and the update rehearsal, after the direct-mode human checkpoint.

### Stage 5 result — 2026-10-04

IMP-50 through IMP-53 and REM-02 are complete. The final catalog contains
35 profiles. The source check explicitly covered all **249 Markdown/MDC/TOML
artifacts**, including documentation, examples and new files, with zero errors.
All five original aggregate resource closures and their **30 heading anchors**
remain available. Review against the stage-0 route inventory found no remaining
live Markdown navigation to old aggregate owners; catalog compatibility paths
remain explicit. Historical evidence files remain byte-identical to the baseline.

The final matrix passed **40 prepared-bundle scenarios**: 36 contained selections
cover all stages' independent, combined, legacy and unchanged control cases;
three flat installations cover PHP, Angular/TypeScript and legacy Next.js; one
custom `.rules/aek` installation covers React/TypeScript. Each passed both its
selected-closure check and a check of every copied instruction artifact. Native
entry/import literals, installed planning instructions, TOML developer routes
and nested task paths were inspected at their actual fixture locations. The
Angular/NestJS workspace has separately reachable application entries and one
physical shared TypeScript entry/topic set. Only explicitly classified optional
routes and historical provenance were adapted; required routes stayed local.

Negative fixture checks rejected a removed required PHP topic, a nonexistent
heading fragment and an unclassified omitted dependency. Mutated fixture contents
were restored. A React-only fixture retained labelled provenance for its omitted
conditional TypeScript route without a dangling local link.

Update rehearsal used the original legacy PHP closure as accepted baseline B,
local edits as current C and the new library as incoming N. Repeating the original
selection without changes preserved contents and timestamps. A real three-way
merge exposed an aggregate-entry conflict before any target writes. The explicit
resolution kept new compatibility routes and moved the local project rule to the
PHP entry; the unrelated local topic edit retained its contents and timestamp.
Changing the selection to independent PHP retained all **15** formerly selected
Symfony/Doctrine/aggregate paths: no retirement was authorized and none was
removed. Both updated fixtures passed artifact checks, and all three accepted
snapshots retained their original contents and timestamps.

Executed tests: **31 profile-selection tests** and **40 artifact-checker tests**
pass. The added control test protects PostgreSQL, Docker and Unreal from unintended
application-stack selection. Strict **mypy 2.1.0** passes on the checker and both
test modules using the maintenance command. Stage-scoped diff review and hash
comparison confirm that only this plan and the selection-test module changed
since the stage-5 baseline. Earlier implementation reviews remain applicable;
no material issue remains. Final diff/whitespace and updated-plan checks pass.

Recovery copies and the pre-stage manifest are retained at
`/tmp/aek-profile-stage5-ul7zl9f8/`, alongside `reference-audit.json`, test logs,
`bundle_helpers.py`, `check_matrix.py`, `matrix-results.json`,
`rehearse_update.py`, `update-results.json`, conflict inputs/preview, immutable
accepted snapshots and rejection evidence. Task-only environments, analyzer
caches and disposable fixture trees are removed after verification. Earlier stage
baselines remain available through review. This canonical document continues to
own progress and dated evidence; no additional stage ledger is introduced.

These results cover source artifacts and static adoption/update fixtures. The
update script is a procedure rehearsal, not a production installer. No live
client discovery, agent adherence, application runtime or context savings were
tested. Executable examples, version pins and consuming projects were unchanged;
no new vendor contract change required additional source research in this stage.
All planned stages are complete. Stop here for user review; no Git writes.
