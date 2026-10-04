# Angular application architecture: design and staged adoption

## Outcome and current stage

Turn the requested application structure into reusable Angular architecture
guidance: application sections, nested domains, pages, presentation components,
data access, root Store composition, feature slices and component-local state.
This document owns the design, stages and handoff. Active technology rules live
in the corresponding standards; this plan is a historical delivery record.

Status: complete, including the requested follow-up correctness review and its
scoped corrections. S1-S3 remain delivered. Work remains in the current checkout,
with no Git writes or application changes.

## Context and Global Constraints

- Workspace/instruction root and implementation checkout:
  `/home/vitalii/Documents/Local_Projects/Agent_Engineering_Kit`.
- Canonical artifact: `docs/plans/2026-10-04-angular-application-architecture.md`.
  The coordinator owns this document; no delegated writers or model setup.
- Direct mode; no staging, commits, branches, worktrees or application changes.
- Pre-stage checkout was clean at
  `fdef22c98d4dab18170ec1cc9f95923afd3fbc04`. This file was absent;
  baseline recorded in `/tmp/aek-angular-architecture-20261004/baseline.json`.
  Capture affected standards' current state before subsequent stage edits.
- S2 pre-edit copies of the four affected standards and this existing untracked
  plan are in `/tmp/aek-angular-architecture-20261004/s2-o_xjmapa/`, with checkout,
  HEAD and Git status in its `manifest.json`. S1's baseline remains intact.
- S3 pre-edit copies and the new example's prior absence are recorded under
  `/tmp/aek-angular-architecture-20261004/s3-vuoiv7a3/`. This baseline includes
  S2's existing entry edits and the untracked canonical plan.
- Follow-up review baseline: `/tmp/aek-angular-architecture-20261004/review-zz_h89v6/`,
  containing the eight reviewed artifacts before scoped corrections, including
  all prior uncommitted edits and untracked documents.
- English artifacts, Russian user-facing communication.
- The supplied application is read-only structural evidence. Do not name it,
  link to it or require access to it in reusable rules or examples.
- Keep one owner per rule; entries route to details, and examples illustrate them.
- Angular does not require NgRx. Store, SignalStore and existing ComponentStore
  remain conditional choices. Do not require an additional state package.
- Do not migrate consuming projects, rename established files automatically,
  upgrade dependencies or rewrite historical verification evidence.
- This is a recommended framework architecture, not an Angular-mandated tree.
  Keep existing compatible conventions and avoid empty placeholder folders.
- User clarification: `core` is only an example name for the section available
  after authentication. Its name is project-specific, not a required layer or
  reserved directory name; carry this distinction into all subsequent stages.

## Observed structure and interpretation

Source inspection covered bootstrap providers, routes, page/component code,
state declarations, feature creators, selectors, reducers and Effects, plus the
manifest. These observations are source review, not executed application checks.

| Observation | Reusable interpretation |
| --- | --- |
| Independent sections own routes, optional layout and pages | Group by application section, then by cohesive domain when needed |
| A protected section contains a simple page and a nested domain | Simple screens need only `pages/`; related API/state/UI belong in a named domain |
| Root `store/` contains provider composition | Root wiring is a legitimate narrow exception to a global Store dumping ground |
| Eager and lazy feature slices have flat, feature-owned Store files | Source ownership and registration timing are separate decisions |
| Pages use selectors, dispatch intent and keep local signals/forms | A page can combine shared read models with its own transient UI state |
| Presentation components use typed inputs/outputs | Child UI does not orchestrate HTTP or reach into feature Store internals |
| No ComponentStore or SignalStore package/implementation is present | A feature Store slice must not be described as a component-local store |

The source manifest declares Angular 22.2.1 and NgRx 22.0.1. These declarations
do not prove installed/resolved or executed versions. The existing library has
recorded Angular 20.3.0 / NgRx 20.0.1 example evidence; retain that history intact.

## Design proposal

### Structure and grouping

Recommend sections with optional nested domains. Compared with a flat list of
domains, this expresses shared navigation/access/layout ownership. Compared with
application-wide technical folders, it keeps a scenario's UI, state and adapter
together. Do not introduce a different architecture system or mandatory libraries.

```text
src/app/
  app.ts / app.html / app.scss
  app.config.ts
  app.routes.ts
  config/                              # shared configuration, if needed
  http/                                # transport policy, if needed
  session/                             # storage adapter, if needed
  store/
    root-store.providers.ts            # classic Store composition only
    root-store.providers.spec.ts
  shared/ui/                           # only genuinely cross-feature UI
  features/
    auth/
      pages/
        login-page/
          login-page.ts
          login-page.html
          login-page.scss
          login-page.spec.ts
      routing/                         # guards and route policy, if needed
      data-access/                     # API, contracts, decoders
      store/                           # auth-owned slice, eagerly registered
    <authenticated-section>/           # project-chosen name, e.g. core or workspace
      <section>.routes.ts
      layout/                          # navigation and nested outlet
      pages/profile-page/              # a simple section-owned screen
      orders/                          # cohesive nested domain
        orders.routes.ts
        pages/orders-page/             # route-level coordination
        components/order-item/         # typed presentation component
        data-access/
          orders-api.ts
          order-contracts.ts
          order-decoders.ts
        store/
          orders-state.ts
          orders-actions.ts
          orders-reducer.ts
          orders-feature.ts
          orders-selectors.ts
          orders-effects.ts
```

`<authenticated-section>` denotes the application section available after user
authentication. Choose a name appropriate to the product, such as `core`,
`workspace` or `portal`, and name its route file consistently. These placeholders
describe a naming choice, not literal folder names. `core` has no special
architectural status and does not denote shared infrastructure in this example.
Access is expressed through route configuration and guards, not the folder name;
backend authorization remains necessary. Independent public/admin sections may
be siblings. Directory nesting does not impose URL prefixes.
A section's route file is useful when it owns a
route group; a tiny section can be wired from the root routes without an empty
route wrapper. Each component/layout/page colocates its own assets and applicable
tests, as illustrated for the login page; preserve existing suffix conventions.

`pages/` names routed screens that compose the domain state API and UI intentions.
`components/` names domain presentation, with typed inputs/events and optional
small local UI state. A stateful reusable widget can own a scoped store when its
behavior warrants one; do not impose Store injection or a facade on each child.
Promote UI to `shared/ui/` only when real cross-feature use warrants that boundary.

### Three state placements

| Placement | Responsibility and lifetime |
| --- | --- |
| `app/store/root-store.providers.ts` | Initialize classic Store once per application; compose eager features, Effects and diagnostics; no domain reducers or HTTP workflows |
| `features/<section>[/<domain>]/store/` | Own a named classic Store slice and its flat state/actions/reducer/feature/selectors/effects files; register eagerly or at the owning lazy boundary |
| Owning page/component directory | Keep simple signals/forms in the component; extract a scoped store beside it only when needed for cohesive local state/async behavior |

A component-local extraction could be
`pages/order-editor-page/order-editor.store.ts`, or a local `store/` subfolder
when several related files warrant it. This is a proposed extension, not an
observed implementation in the supplied source. A new compatible implementation
may use SignalStore; preserve existing ComponentStore where selected. Component
providers give per-instance ownership. Root-provided SignalStore is shared, even
if its file happens to sit next to a component.

Classic feature registration extends the application's Store; it creates neither
a component instance nor automatic page-exit cleanup. Specify cancellation,
cache retention/reset and account changes independently. Local drafts/filters
must not duplicate writable canonical entities from the feature slice. Use the
existing state-choice and lifecycle policies rather than copying them here as
another permanent owner.

### Dependencies and data flow

- Composition roots may import feature registration contracts. Features and
  infrastructure must not import root Store wiring or `app.config.ts`.
- Section routes/layout compose child routes/pages. Nested domains must not
  import their parent layout or route composition.
- Pages read selectors and dispatch semantic actions; presentation emits intent
  through outputs. Effects call adapters; reducers perform pure transitions;
  selectors derive views. API adapters validate transport data and do not own UI.
- A feature creator composes its reducer; its selector module consumes generated
  selectors and adds derivations. Do not introduce a feature-to-selector cycle.
- Cross-feature consumers use explicitly public events/selectors/contracts.
  A public contract can be a named module; a barrel or facade is not mandatory.
  Other sections must not import a feature's pages or private reducers.
- Infrastructure and shared UI do not depend on features. A domain component
  may use its domain's readonly data types without importing its HTTP service.

## Authoritative owners and intended changes

| File | Intended responsibility/change |
| --- | --- |
| `standards/angular/architecture.md` | Recommended section/domain tree, pages/components/layout roles, dependency direction and root-composition exception |
| `standards/ngrx/state-architecture.md` | Root composition versus feature slice versus component instance; flat classic Store placement and registration ownership |
| `standards/angular.md`, `standards/ngrx.md` | Short task routes to these owners; no duplicate detailed policy |
| `standards/angular/examples/application-structure.md` (new) | Annotated folder example and scenario traces linking to the owners; conditional NgRx section |
| `standards/catalog.toml` | Register the new example with Angular; retain the optional NgRx dependency direction |
| `templates/project-architecture.md` | Record section/domain boundaries, root registration and scoped state owners in a consuming project's architecture passport |

Keep `standards/ngrx/signal-store.md` as the owner of SignalStore mechanics.
Existing executable examples need no rewrite merely to match the folder example.
The new example will be an architecture illustration, not an executable fixture.

## Stages and acceptance

- [x] S1.1 Inspect current rules and supplied source; distinguish observed code
  ownership, registration timing and actual local state.
- [x] S1.2 Prepare the concrete design, file ownership and staged change scope.
- [x] S1.3 Verify the design artifact and review its consistency; record evidence
  and stop for user review before changing active rules.
- [x] S2 Update the two architecture owners and their entry routes together.
  Acceptance: recommended grouping is explicit, root composition is permitted,
  feature and component stores cannot be confused, Angular remains usable without
  NgRx, the authenticated section's name is project-specific, and existing
  lifetime/reset/version constraints remain intact. Check the
  four changed Markdown files with the artifact checker and inspect their diff.
- [x] S3 Add the annotated architecture example, its catalog resource and entry
  route, and extend the architecture passport. Acceptance: a reader can place a
  simple page, nested domain, lazy slice, root-shared slice and local editor state
  without consulting the supplied project; optional packages remain optional.
  Run scoped artifact checks, existing profile-selection tests, and diff review.
- [x] R1 Perform the user's requested repeat correctness review of the completed
  Angular architecture package; resolve confirmed instruction ambiguities and
  verify corrected artifacts without claiming application-runtime evidence.

Each stage includes its necessary checks and scoped fixes, followed by a human
checkpoint. No separate stage exists solely to defer verification. New unit tests
or an application harness are not needed for folder/prose-only changes; reassess
checks if an executable contract is changed later.

## Sources and evidence limits

Official sources inspected on 2026-10-04:

- [Angular style guide](https://angular.dev/style-guide): feature organization
  and colocated component assets/tests. The guide discourages grouping by code
  type; our bounded role folders inside a section/domain are an explicit local
  convention, not a vendor-prescribed tree.
- [Angular 20 hierarchical DI](https://v20.angular.dev/guide/di/hierarchical-dependency-injection):
  provider hierarchy and component-owned lifetime.
- [NgRx 20.0.1 reducers guide](https://raw.githubusercontent.com/ngrx/platform/20.0.1/projects/ngrx.io/content/guide/store/reducers.md):
  standalone root/feature registration and slices of the shared state object.
- [NgRx 20.0.1 SignalStore guide](https://raw.githubusercontent.com/ngrx/platform/20.0.1/projects/ngrx.io/content/guide/signals/signal-store/index.md):
  local and root providers, component-scoped lifetime.

The moving NgRx website yielded only its application shell. The attempted
22.0.1-tagged guide was unavailable through the browser tool; no 22.0.1-specific
API verification is claimed. The proposed folder policy introduces no new API
or version floor. Recheck the actual target contract if implementation later
introduces version-specific snippets. No dependency install, compilation,
application tests or browser execution occurred during this analysis.

## Handoff

User clarification incorporated: the authenticated section has a project-chosen
name; the proposed tree now uses a semantic placeholder instead of prescribing
`core`. This refines S1 and does not authorize progression to S2.

The subsequent user instruction to start the description authorizes S2. Its
scope is the four existing architecture/entry documents and this progress owner;
S3's example, catalog and architecture-passport changes remained pending at that
checkpoint. The later instruction to execute authorized S3.

S1 checks on 2026-10-04: the scoped artifact checker reported one checked artifact
and zero errors. The tracked diff whitespace check passed; the new file was
separately inspected for whitespace, scope and consistency. Inline review covered
optional package selection, section versus domain ownership, component versus
classic Store lifetime, import direction and the absence of a source-project
reference. No unresolved design inconsistency was found. These are documentation
checks, not application-runtime evidence.

At the S1 checkpoint, only this proposed design/plan had changed. Active
standards, templates, catalog and the supplied application were unchanged.

S2 delivered on 2026-10-04:

- `standards/angular/architecture.md`: section/domain folder tree, arbitrary
  authenticated-section name, pages/components/layout roles, dependency direction
  and the exception for root Store composition. Existing DI and NgModule guidance
  remains in place.
- `standards/ngrx/state-architecture.md`: root provider composition, flat feature
  Store files, component-local extraction and eager/lazy registration ownership.
  State choice, cache/reset and route-lifetime obligations remain intact.
- `standards/angular.md` and `standards/ngrx.md`: task routes to the appropriate
  architecture headings, without duplicating the detailed policies.

Verification for S2:

- `python3 tools/check_instruction_artifacts.py standards/angular.md standards/angular/architecture.md standards/ngrx.md standards/ngrx/state-architecture.md docs/plans/2026-10-04-angular-application-architecture.md`:
  five artifacts checked, zero errors, exit 0.
- `git diff --check`: exit 0. Scoped whitespace and excluded-source-name checks
  also passed, including separate inspection of the untracked plan.
- Coordinator review inspected the four standards' actual diff against the S2
  baseline and checked optional NgRx selection, public import boundaries,
  arbitrary section naming, flat Store ownership and preserved DI/reset rules.
  Corrected a heading reference during review; no unresolved in-scope findings.
- Reused S1's applicable official-source review; no new API or version floor was
  introduced. Only prose and illustrative directory trees changed. No application
  build/runtime tests, checker-unit suite or independent review was needed for
  this documentation scope; none is claimed.

S3 delivered on 2026-10-04:

- Added `standards/angular/examples/application-structure.md`: an annotated
  section/page/domain tree, optional root/feature/component store placement and
  concrete placement, interaction and lifecycle scenarios. `workspace` is an
  illustrative authenticated-section name, not a prescribed layer.
- Registered the example in `standards/catalog.toml` under Angular and linked
  it conditionally from the Angular entry. Profile dependencies are unchanged.
- Extended `templates/project-architecture.md` with section/access/role paths,
  public boundaries, root and eager/lazy registration locations, and local store
  owners. These are project-record fields, not another copy of the full policy.

Verification for S3:

- `python3 tools/check_instruction_artifacts.py standards/angular/examples/application-structure.md standards/angular.md standards/catalog.toml templates/project-architecture.md docs/plans/2026-10-04-angular-application-architecture.md`:
  five artifacts checked, zero errors, exit 0.
- `python3 -m unittest discover -s tests -p 'test_profile_selection.py'`:
  31 tests passed. Additional catalog-closure assertions confirmed that the new
  example is available through both Angular and NgRx selections while Angular
  still excludes NgRx.
- `git diff --check` passed. Separate whitespace and excluded-reference checks
  passed for the new example and untracked plan.
- Coordinator review inspected S3 changes against their preserved baseline,
  including the complete new file, and checked consistency with S2's owners.
  No unresolved in-scope findings. The final handoff edit received a scoped
  artifact/whitespace check; prior profile-test evidence remains applicable.

All acceptance criteria are satisfied. The example is structural prose, not a
compiled fixture; no new application-runtime evidence is claimed. Historical
research, existing executable examples and the supplied application remain
unchanged. No further implementation stage is planned.

## Requested follow-up correctness review

Scope: six tracked changed files plus the new architecture example and this
plan. Reviewed actual changes against the recorded baseline, including optional
profile routing, plain Angular, classic Store and SignalStore-only use, local
provider scope, arbitrary section naming and list-to-editor navigation.

Applied Superpowers requesting-code-review and systematic-debugging with local
verification adaptations. No configured model-routing record was present;
review ran inline under the orchestration fallback, not as an independent second
opinion. No role/model configuration was changed.

| Finding | Consequence | Scoped correction |
| --- | --- | --- |
| Architecture passport requested classic root/feature wiring under a general NgRx condition | A SignalStore-only consumer could infer that classic Store must be added | Separate classic Store recording fields from SignalStore/ComponentStore provider fields |
| Example did not identify what list-page cleanup preserves for its sibling editor | An adopter could clear needed canonical records or cancel another page's work | Specify list query cleanup, preserved records, editor direct-link loading and separate request ownership |
| Example's local filter had no navigation condition | An adopter could keep shareable navigation state outside the URL | Label it transient presentation state and route navigable filters to the existing URL-state rule |

These are instruction ambiguities, not observed failures of an executable
application. Root cause: the example/template omitted conditions already present
in the authoritative package/state, query ownership and routing rules. Changes
are limited to those two documents and this handoff; the architecture itself
and profile dependencies do not change.

Official-source review on 2026-10-04 reused/rechecked the versioned NgRx 20.0.1
reducers and SignalStore guides listed above, plus
[feature creators](https://raw.githubusercontent.com/ngrx/platform/20.0.1/projects/ngrx.io/content/guide/store/feature-creators.md),
[Angular 20 style guidance](https://v20.angular.dev/style-guide) and the listed
Angular 20 DI guide. The custom folder names and role grouping remain local
policy. Additional retrieval of the versioned provider source and route-reuse
guide was unavailable; no new source-level or runtime claim relies on those
pages. Current-version installation and application execution remain outside
this documentation review.

Follow-up results on the corrected state:

- Scoped artifact checker over all eight task artifacts: eight checked, zero
  errors, exit 0. This includes the example, catalog and architecture passport.
- `python3 -m unittest discover -s tests -p 'test_profile_selection.py'`:
  31 passed, exit 0. Separate closure assertions confirmed example availability
  through Angular/NgRx and that Angular does not select NgRx.
- `git diff --check` and separate new/untracked whitespace and excluded-reference
  checks passed. The final report-only edit received a scoped artifact check.
- Inspected the two corrected documents against the follow-up baseline and
  reconciled the three findings with their authoritative rules. SignalStore-only
  adoption no longer requests classic wiring; list-to-editor/direct-link and
  local-versus-navigable-filter choices are explicit.

Verdict: no unresolved material finding within the changed instruction package.
No application build, live navigation, independent reviewer or validation against
installed Angular/NgRx 22 packages is claimed. Versioned documentation and prose
consistency do not establish runtime correctness of a consuming application.
