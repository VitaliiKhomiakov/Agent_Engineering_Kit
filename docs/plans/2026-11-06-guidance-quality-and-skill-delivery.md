# Guidance quality and skill delivery plan

Status: E1 complete on 2026-11-06; retain direct Angular routes at this checkpoint.
Current checkpoint: E1 [x]. S3 integration and broader S4 rollout are deferred.
S1, S5, S6 and S2 remain complete; no production Angular skill was added.

## Goal and design

Improve shared guidance and existing language/technology profiles only where
evidence shows a useful gap, then test one optional Angular reference entry while
retaining the authoritative rule library and existing Superpowers procedures.

Design and acceptance owner:
[Guidance quality and skill delivery](../specs/2026-11-06-guidance-quality-and-skill-delivery.md).
Its Global constraints apply to every stage. This plan owns progress and execution
evidence; the specification owns design. No secondary checklist is maintained.

## Workspace and authorization

- Instruction root and execution checkout:
  `/home/vitalii/Documents/Local_Project/AgentsFramework`.
- Canonical progress owner: this file in that checkout; coordinator-owned.
- Baseline: commit `304feef0cad0e7b04b09c93ddb62eb2bc2acd3fe`, clean tree before
  preparation. Both new task documents were absent; their baseline is recorded
  in the external task directory's `baseline.json`.
- Authorized now: after S2, the user requests Superpowers-based evaluation and
  addition of the Angular skill only if it actually helps. E1 evaluates a temporary
  candidate against the current direct routes before production S3 integration.
  A demonstrated benefit authorizes the corresponding bounded addition and checks;
  an inconclusive result retains direct routes. Earlier research and external
  retention authorization remains valid; consumer/global configuration changes
  and broader technology rollout are not authorized.
- S1 baseline: `/tmp/aek-s1-2026-11-06-s5zdcf4c/baseline.json` identifies this
  checkout, HEAD and six pre-edit file copies. It includes the existing untracked
  specification and plan, whose contents are not represented by HEAD.
- S5 baseline: `/tmp/aek-s5-2026-11-06-gfpy2sdl/baseline.json` records nine affected
  paths, including the new topic's prior absence and current core/plan contents.
  Four other pre-existing changed/untracked files are also preserved for scope
  comparison; S1 edits are part of this baseline, not new S5 work.
- S6 baseline: `/tmp/aek-s6-2026-11-06-1pwa6nml/baseline.json` records the six
  affected files and ten other pre-existing changed/untracked files. Current S1/S5
  contents are preserved; HEAD alone does not represent this stage's baseline.
- S2 baseline: `/tmp/aek-s2-2026-11-06-4z80x24i/baseline.json` records eleven
  affected paths (four previously absent) and fourteen other changed/untracked
  files. The adjacent disposable `runtime/` was removed after verification;
  `evidence/` retains its scoped commands, resolved dependency record and check output.
- E1 baseline: `/tmp/aek-angular-eval-2026-11-06-uwihtq0x/baseline.json` preserves
  current contents/absence for possible evaluation/integration paths and all
  pre-existing changes. Its verified retained copy, compressed fixture snapshots
  and raw results are in the external archive identified in the E1 outcome below;
  the original temporary workspace was removed after retention.
- Mode: inline, current checkout; one coherent stage and its checks before human
  review. No staging, commits, branches, worktrees, client installation or
  publication. S2 permits only the planned temporary example dependencies outside
  the repository, with package lifecycle scripts disabled.
- Model routing: current session, no delegation requested or selected; the source
  library has no active target routing configuration to initialize.
- Procedures: the existing design/planning work is reused; execution uses Superpowers
  executing-plans and verification-before-completion under the local adaptations.

## External research and resumption

The local research index is
`/home/vitalii/.codex/research/aek-guidance-2026-11-06/INDEX.md`.
It identifies pinned snapshots, content checksums, licenses, review coverage,
source status and the detailed comparison matrix. It is reference material,
not another progress owner and not an active skill or project instruction.

The all-technology follow-up is recorded separately at
`/home/vitalii/.codex/research/aek-guidance-2026-11-06/expanded/INDEX.md`, with
`MATRIX.md` and `comparison.json` beside it. Use that record for the complete
profile mapping; the initial index retains the first review's narrower scope.

Read that index when resuming comparative review. Do not copy its source names,
URLs, snapshots or comparative notes into this repository, commit messages,
generated bundles or publications. The user explicitly excluded those identities
from AEK. Public task documents contain independent decisions and official
technical evidence only. Consumer operations never depend on the external cache.

If the cache is unavailable, report the lost comparison evidence and recover the
same pinned material before claiming that comparison repeated. Continue work
supported by approved public contracts; do not substitute a new source revision
or invent prior findings. Reconcile the current checkout and existing item status
before resuming. New source revisions are new evidence, not replacements for an
earlier run.

## Progress

- [x] R1 — Inspect AEK and bounded comparison material; identify candidate gaps,
  incompatible advice, version limits and delivery alternatives.
- [x] R2 — Retain the external research record; prepare and check the specification
  and plan, then present the proposed scope for review.
- [x] R3 — At the user's request, inventory the complete comparison collection,
  map every existing AEK language/technology profile, review applicable material,
  and revise the proposed priorities and evidence without changing active rules.
- [x] G1 — User accepts the proposed direction and requests implementation with
  Superpowers; execute the next stage under the existing checkpoint policy.
- [x] S1 — Adjudicate the recorded cross-stack/profile candidates and apply only
  justified small documentation or routing changes.
- [x] S5 — Add the approved conditional authentication/token contract and routes.
- [x] S6 — Close an approved shared diagnostic gap, or record a no-change outcome.
- [x] S2 — Strengthen selected Angular contracts and independently authored examples.
- [x] E1 — Establish whether an optional Angular skill adds observable value over
  the same content reached through direct routes; gate production S3 integration.
- [ ] S3 — Deferred after E1: the condition for adding a production Angular skill
  and adoption mapping is not established; no source integration was performed.
- [ ] S4 — Broader rollout evaluation deferred with S3; E1 retains its bounded
  pilot results without claiming the full rollout matrix completed.

G1 is a decision checkpoint, not permission to perform every later stage. Unless
the user explicitly authorizes broader progression, each S item ends with its
checks and human review. Item outcomes are described below; pending verification
keeps the corresponding item open.

Existing item IDs are preserved. The proposed order is S1, S5, S6 if warranted,
S2, then S3/S4. Angular is the proposed first delivery experiment, not the only
technology assessed or necessarily the first technical content improvement.

## Stage S1 — Cross-stack decisions and bounded improvements

Depends on G1. Reuse R3's completed inventory and profile dispositions; do not
repeat the full source search. Resolve selected candidate decisions against their
actual AEK owners. Preserve already covered rules; a no-change outcome is valid.
The source review does not require an edit for every profile.

Affected files, only when their responsibility needs a change:
`standards/core.md`, `standards/verification.md`, relevant language topic owners,
and their existing entry routes. A small driver-security route may affect
`standards/typeorm.md` or its existing topic owner only if the selected host/driver
guidance leaves a demonstrable gap. Do not introduce a universal observability,
documentation or infrastructure stack to fill a topic checklist.

Set explicit outcomes for authentication (S5), diagnostics (S6), public-contract
documentation and component accessibility (S2). Keep language-specific GoDoc,
JSDoc and PHPDoc details in their existing owners; any shared clause should explain
otherwise missing caller-visible semantics, not repeat every type annotation.
Do not rewrite framework rules where the evidence supports preservation or no
specialized comparison exists.

For each accepted improvement, record the affected scenario, prior ambiguity,
chosen owner and concrete acceptance condition. Distinguish local policy from
official behavior. Recheck the affected vendor contract when a technical claim
is introduced. Keep comparison identities in the external record.

Completion: all selected candidates have a justified disposition, accepted edits
have no competing owner, and the affected link/format and consistency checks pass.
Run the artifact checker on edited paths plus `git diff --check`; inspect new
files separately. Run runtime/static checks only if executable content changes.
Report actual changed rules or the evidence-based no-change result.

### S1 decisions

The following dispositions were selected on 2026-11-06. They reuse R3 rather
than claim a new audit of all comparison entries.

| Candidate and affected scenario | Decision and owner | Acceptance for S1 |
| --- | --- | --- |
| Public/shared API whose types omit caller-visible constraints such as units or resource ownership | Add concise semantic documentation/comment guidance in core; route Go's existing comment guidance to it while retaining Go declaration conventions | One shared semantic owner; meaningful constraints are documented without requiring boilerplate for every symbol or repeating native types |
| Remote TypeORM DataSource configuration without a selected PostgreSQL profile | Add a connection-settings section to the existing schema/verification topic and route configuration tasks to it; preserve driver/version conditions | The route exposes certificate/hostname verification and effective driver settings without requiring Node, PostgreSQL or another profile |
| Authentication and application-specific token verification | Retain S5 as the next proposed contract stage | Record the decision; preserve existing authorization rules until the dedicated topic and routes are implemented together |
| Shared diagnostic ownership/correlation | Retain S6's bounded assessment; existing redaction, context and capacity rules already cover much of the concern | No new diagnostic owner or mandatory telemetry stack in S1; S6 must demonstrate any remaining gap |
| Accessible component/directive behavior | Retain S2's Angular-specific scope and runtime evidence boundary | No blanket UI rule or unverified Angular example in S1 |
| Other reviewed language/technology practices | Preserve R3's existing-coverage, incompatibility and absent-specialist dispositions | No edits merely to match a topic inventory, replace tools, or expand supported stacks |

Interfaces: Go consumes the new core section; TypeORM's entry consumes its
existing topic with a new anchor. Both targets are already available in their
catalog closures, so no catalog or adoption change is needed. Later shared and
Angular stages retain their own owners and acceptance gates.

## Stage S5 — Conditional authentication and token verification

Depends on the reviewed authentication decision from G1/S1. Implement the
specification's independently authored contract at
`standards/security/authentication.md`; route relevant core tasks to it and
declare it in core's catalog resources. Keep schema 1 and current profile IDs.

Affected integration routes, only where needed: FastAPI runtime/security,
Gin routing/middleware, Nest transport/operations and Next.js server security.
Keep parsing/wiring details at the framework owner and shared trust/verification
semantics at the new topic. Do not copy a complete policy into every entry or
add a native security skill merely because the topic exists.

Resolve application-specific JWT purpose/claims, trusted key discovery, algorithm
selection, expiry, rotation and replay conditions using the RFC references in the
specification and the actual target library if code is included. Preserve other
authentication strategies, operation/tenant authorization and existing client
cookie/CSRF contracts. No provider, token lifetime or cryptographic implementation
is installed by this stage.

Completion: each applicable failure class from the specification has a clear
required outcome and one owner; non-authentication tasks do not acquire another
mandatory reading sequence. Artifact checks cover the new topic, catalog and all
changed routes. Run relevant profile-selection checks for changed availability,
plus whitespace/new-file inspection. If an executable example is added, run its
actual negative/positive verification cases with stated versions. Do not introduce
a runtime dependency merely to test prose.

### S5 implementation decisions

The shared topic is conditional on authentication/session/token work. Its sole
catalog owner is core; its outbound local reference uses already-required shared
verification. Framework topics route to it without introducing another profile,
library, native skill or recursively required reading sequence.

FastAPI runtime/security, Gin routing/middleware, Nest transport and operational
security, and Next.js server security are the affected integration routes. Their
existing operation-authorization, cookie/CSRF and framework-wiring responsibilities
remain in place. No executable authentication example is added in this stage.

The [S5 execution record](#s5-execution-evidence-and-next-checkpoint) reports the
affected artifact/catalog checks, profile-selection regression suite, resource
availability and scoped review. Verifier failure cases are documentation acceptance
criteria, not claimed runtime results.

## Stage S6 — Diagnostic ownership, only if a gap remains

Depends on S1's diagnosis of an actual shared gap. First reuse Node/Nest,
language, database and LLM guidance on redaction, correlation and capacity.
Record no change if those owners already establish the required behavior.

For an accepted gap, prefer a short common clause and relevant routes. Create
`standards/diagnostics.md` as a conditional core resource only if the detail needs
its own owner; reconcile overlap instead of adding competing rules. Keep runtime
context mechanisms in language/host topics. Address error-reporting ownership,
useful safe context, absent/invalid correlation and telemetry failure/capacity
only as needed. Service SLOs and runbooks remain conditional operations guidance.

Completion: the chosen failure scenario is addressed without mandatory exporters,
invented trace IDs, duplicate error reporting or leaked payloads. Use affected
artifact/link/catalog checks and whitespace/new-file inspection; runtime checks
apply only to newly executable material. A no-change disposition closes this
stage's assessment without claiming an implementation occurred.

### S6 gap decision and ownership

The selected failure is a storage/service error propagated through a request or
job boundary and reported repeatedly as if each layer encountered a separate
failure. Before S6, Go already discouraged this in its error contract and Python
named a reporting owner. Core had no shared equivalent, while Node/Nest diagnostic
guidance concentrated on context, redaction and capacity. This is a bounded cross-stack
ownership gap, not a reason to introduce a telemetry platform.

Add a short core section and task route. Go and Python refer to its shared policy
while retaining wrapping, exception, cancellation and public-error contracts.
Node and Nest diagnostic sections route to it while retaining runtime-specific
context mechanisms and existing logging choices. The section fits in core; no
separate diagnostics topic, catalog resource or new profile is needed.

| Candidate | Disposition for S6 |
| --- | --- |
| Repeated error reporting across layers | Add one shared reporting-owner rule; preserve distinct failures and independently required access/audit/trace records |
| Useful context and absent correlation | Require safe context at that owner and correlation only from an actual validated context; runtime propagation stays with existing host/vendor owners |
| Redaction and privacy | Preserve Node/Nest, PHP, PostgreSQL and LLM/Langfuse rules; the shared clause directs reporting to obey them |
| Telemetry capacity and export failure | Preserve Node/Nest buffer/cardinality rules and LLM/Langfuse export/outage contracts; no exporter or universal telemetry-failure policy is added |
| Service SLOs, alerts and runbooks | No new requirement: this stage changes no deployed service's operational contract |

Acceptance: the same propagated failure has a designated diagnostic owner; locally
handled or distinct failures and required audit records remain observable. Shared
wording requires neither raw payload logging nor fabricated correlation fields.
This is local engineering policy and routing, with no changed vendor API/version
claim or executable example. Use the affected artifact and scoped consistency
checks; the unchanged catalog and runtime fixtures need no repeated test run.

## Stage S2 — Angular contracts and examples

Depends on G1 and resolution of any shared rule S2 actually consumes. S1, S5,
S6 and S2 have separate outcomes; completion does not authorize the next stage.

Proposed additions:

- `standards/angular/components.md`: component API, child queries, projection,
  host behavior and accessibility contracts.
- `standards/angular/directives.md`: behavioral directives, composition,
  input/output exposure, lifecycle and cleanup.
- `standards/angular/examples/component-contracts.md`: a focused example and
  meaningful checks for a conditional child/projected-content contract and a
  reusable behavior, with explicit tested versions.

Affected existing owners: `standards/angular.md`,
`standards/angular/boundaries.md`, `standards/angular/verification.md`,
`standards/catalog.toml`, and example reproduction in
`docs/maintenance/verification.md`. Touch reactivity, rendering or architecture
only for a demonstrated gap. Preserve SCSS ownership and existing route anchors.
Use the expanded React/Angular accessibility review to reuse existing native
control/form guidance. Do not add generic CSS, a widget library, global ARIA
requirements or another framework's styling choices. State any selected
accessibility standard and applicable exceptions before prescribing thresholds.

Before authoring examples, choose a supported target from existing evidence and
verify the relevant versioned APIs. Record the toolchain in a new dated evidence
record; do not rewrite earlier research as if it tested the new example.

Completion requires:

- Queries and projection explain absence, ownership and conditional-content
  behavior; directives expose only intended contracts and clean up owned effects.
- Tests exercise observable component/DOM behavior and production notification
  paths without masking a missing update with forced rendering.
- Existing forms, NgModules, ZoneJS, NgRx selection and runner choices remain
  compatible; no consumer upgrade or root application dependency is introduced.
- New resources are declared and task routes resolve.

Checks: affected artifact paths; `test_profile_selection.py` if the resource
selection changes; the example's documented template/build and focused behavior
checks in a temporary harness; `git diff --check` and new-file inspection.
Missing required runtime evidence keeps the example's verification open.

### S2 example and evidence decisions

Reuse the earlier executed Angular 20.3.0 / TypeScript 5.9.3 / RxJS 7.8.2 baseline
on Node 24.13.0. Consult v20 documentation and exact package contracts; moving v22
manuals do not select an upgrade. The new fixture uses `ngc` strict template
compilation, Angular TestBed with explicit zoneless scheduling, Node's test runner
and jsdom 26.1.0. esbuild 0.25.10 bundles the compiler's emitted cross-file imports
for Node execution; it does not replace Angular template compilation. The runner
uses one process for this single suite and resets TestBed between cases. It adds
no application manifest or runtime dependency to AEK and does not prescribe a
consuming project's runner.

The focused scenario is an expandable details panel: an optional view control,
consumer-owned conditional projected action, deliberate host-directive input/output
aliases, native buttons, focus return, and an owned Escape listener. Checks must
observe actual DOM changes through signal/event/render notifications, including
listener removal after destruction. DOM emulation does not establish real-browser
keyboard defaults, visual accessibility or SSR/hydration behavior. No new styles
are needed for this unstyled contract fixture; authored styles retain SCSS policy.

## Stage S3 — Optional Angular reference skill

Now also depends on E1's positive benefit decision under the user's latest request.
A disposable E1 candidate is not completed S3 integration. Implement the
contract from the specification without adding a second Superpowers workflow.

Create `templates/skills/aek-angular/SKILL.md`. Modify only the relevant parts of
`standards/catalog.toml`, `standards/catalog.md`, `MIGRATION.md`,
`templates/policy-entry.md`, and `ARCHITECTURE.md` to describe explicit selection,
local references and the actual client coverage. Keep existing design/review
entries and `project-workflows` selection independent.

Use `angular.source_resources` for source-template availability and the existing
adoption record for managed native paths. No default native installation or new
installer is introduced. Rebase references for contained, flat and custom bundles
and independently opened children. Preserve unowned same-name or official skills.

Extend relevant existing tests in `tests/test_project_skill_adoption.py`,
`tests/test_project_skill_portability.py`, and `tests/test_profile_selection.py`
only for uncovered adoption/resource boundaries. Adjust checker code only if a
new required contract cannot be checked through its supported existing syntax.

Completion: metadata is valid, selected references are locally reachable without
the source checkout, missing dependencies are diagnosed, Angular alone installs
no optional skill, and the new entry installs no sibling design/review skills.
Preserve repeat/update reconciliation and inactive-template omission.

Checks: affected artifact bodies and selected bundle fixtures; the changed
adoption/portability/selection suites; `git diff --check` and new-file inspection.
When authoring the actual skill, apply the available writing-skills procedure
through local adaptations. Static acceptance does not close S4 or prove activation.

## Stage S4 — Comparative evaluation and rollout decision

E1 brings the initial comparison forward before production S3 integration.
Reuse its valid evidence if a useful candidate proceeds; do not repeat it merely
because a template moves into AEK. Wider rollout still requires this stage's
acceptance. Select an available authorized client and
record its version, model/effort, Superpowers configuration, permissions and
fixture/content identities before runs. Do not silently configure other clients,
delegate workers or consume an unspecified external service to obtain results.

Use the specification's scenario table for positive and negative cases. Compare
direct routes with the optional skill using the same approved technical content.
Reuse meaningful existing cases; add only cases needed to expose routing,
compatibility or permission failures. Capture complete run evidence externally
and a sanitized dated result in `docs/research/` when authorized.

Assess observed activation, relevant reading, rule compliance, correctness,
duplicate procedures, unsolicited actions and actual cost when measurable.
Separate a successful explicit invocation from reliable implicit selection.
Use repeated paired runs before a frequency or efficiency claim. Do not call
missing client execution or unmeasured cost a successful result.

Completion: executed coverage and limits are recorded, material regressions are
resolved or the candidate is rejected, and a decision is presented: retain the
pilot as optional, revise it, or keep the improved rules with direct routes.
Further technology skills, additional native clients and hosted publication are
separate decisions after this evidence, not automatic follow-on implementation.

### E1 evaluation protocol

Use Superpowers `writing-skills` retrieval/application checks and
`verification-before-completion` through the local adaptations. The controlled
test subject is the already installed Codex CLI 0.167.0 using its saved
`gpt-6-astra` / `high` defaults and existing ChatGPT account. Keep model/effort,
permissions, source content and selected Superpowers installation fixed across
arms. Runs are read-only and ephemeral in disposable fixtures. This is runtime
evaluation, not delegation of repository work or configuration of persistent roles.
No global settings, credentials, existing skills or consumer projects are changed.

Start with a direct-route baseline. Compare a minimal reference candidate only
where it can address a retrieval/application gap or test the packaging hypothesis.
Check native discovery separately from explicit invocation and actual task use.
Record actual reads, correctness, unnecessary work and available usage evidence;
single observations do not establish frequency or cost savings. Keep ordinary
TypeScript/non-Angular tasks as negative triggers and preserve existing project
versions and optional state/runner choices. If client execution is unavailable,
record that limit and do not substitute static checks for demonstrated benefit.

## Preparation evidence and next checkpoint

R3 was authorized after the first proposal: expand the comparison beyond shared
guidance and Angular to all existing language/technology profiles. The two prior
proposal documents and their hashes were preserved before this revision and are
retained under the expanded external record's `baseline/`, with checkout status
in its `baseline.json`. R1/R2 remain valid for their original bounded scope;
they do not establish completion of the expanded comparison.

R3 research scope now includes a complete source inventory and content search,
52 full skill bodies (eight unchanged bodies reused from R1), six selected-section
reviews, and all 36 AEK technology profiles. The remaining source entries were
inventoried/searched, not audited. All-profile mapping distinguishes named matches,
partial coverage, absent specialized material and compatibility aggregates.
Selected disputed contracts were checked against official Go, Docker, React,
Node/TypeORM, IETF, Python, LangChain, W3C and OpenTelemetry sources. These are
inspection results; no source example was executed.

R3 completed on 2026-11-06 with these preparation checks:

- The expanded external index, full profile matrix, machine-readable coverage,
  helpers and baseline were retained at the resumption location. All 267 source
  files matched manifest byte counts and SHA-256 hashes after copying. Initial
  snapshots were preserved; the original research index links to the expansion.
- Set comparison confirmed that every catalog technology profile occurs exactly
  once in the external matrix and is represented in the specification's table.
  Reading levels distinguish complete entries, selected sections and inventory-only
  material. All six proposed implementation stages retain pending markers.
- The artifact checker on the two proposal documents reported zero errors.
  Whitespace inspection included both untracked files and the actual checkout;
  no diagnostics were reported.
- The identity exclusion scan passed for tracked and untracked, nonignored
  repository files. Scope inspection confirmed only the two existing proposal
  documents changed; tracked rules, templates, tests and the Git index are intact.

The proposed priorities now include conditional authentication and bounded
diagnostic/documentation work across stacks. Angular remains a content-improvement
and delivery-pilot candidate. R3 does not approve S1-S6 or claim runtime results.

R1: source inspection completed on 2026-11-06. General-policy comparison is
bounded, not an audit of every technology in the reference collection. Historical
Angular guidance was retained separately from current source status and checked
against selected current official contracts. No external instructions were
installed or executed. No comparative agent or Angular runtime runs were performed.

R2: preparation completed on 2026-11-06.

- The external index, baseline, retrieval helper and four pinned snapshots were
  saved at the resumption location above. All 96 selected source files matched
  their manifest byte counts and SHA-256 checksums after copying.
- `python3 tools/check_instruction_artifacts.py
  docs/specs/2026-11-06-guidance-quality-and-skill-delivery.md
  docs/plans/2026-11-06-guidance-quality-and-skill-delivery.md` checked both
  artifacts with zero errors.
- `git diff --check` produced no diagnostics. Each untracked document was also
  inspected with `git diff --no-index --check -- /dev/null <path>`: no whitespace
  diagnostics; exit 1 reflects the new-file difference in no-index mode.
- An identity exclusion scan passed across tracked and untracked, nonignored
  repository files. A scope check confirmed exactly these two new task documents,
  with existing tracked files and the Git index unchanged.
- No executable content changed, so application/runtime or regression test runs
  were not selected for this documentation preparation stage.

Preparation checkpoint after R3: present the expanded comparison and checked proposal. S1 resolves
the selected shared decisions after review; conditional authentication (S5) is the
clearest new content candidate. S6 and other profile edits require demonstrated
gaps. The Angular additions and optional delivery experiment remain S2, S3 and S4.

## S1 execution evidence and checkpoint

S1 completed on 2026-11-06 after the user's implementation request. The scoped
baseline above preserves the four previously clean rule files and the two existing
untracked task documents. R1-R3 evidence remains limited to its original scope.

- [Core](../../standards/core.md#public-contracts-and-explanatory-comments) now owns
  shared semantic documentation and explanatory-comment guidance.
  [Go](../../standards/go/style.md#comments-and-errors) routes there while retaining
  its exported-declaration and comment-form requirements. JavaScript/PHP type
  documentation remains with its existing owners.
- [TypeORM connection settings](../../standards/typeorm/schema-verification.md#connection-settings)
  and the entry route cover effective driver configuration and certificate-based
  TLS verification. The existing evidence table now identifies accepted-server,
  untrusted-chain and wrong-host outcomes for actual TLS configuration changes.
- Source review checked TypeORM's current
  [DataSource options](https://typeorm.io/docs/data-source/data-source-options/) and
  [Postgres options](https://typeorm.io/docs/drivers/postgres/), its pinned
  [0.3.27 connection option type](https://github.com/typeorm/typeorm/blob/0.3.27/src/driver/postgres/PostgresConnectionCredentialsOptions.ts),
  [node-postgres TLS configuration](https://node-postgres.com/features/ssl), and
  [Node 24.13.0 TLS](https://nodejs.org/download/release/v24.13.0/docs/api/tls.html#tlsconnectoptions-callback).
  The current TypeORM site describes 1.0; the pinned source and Node reference
  preserve the existing example's version boundary. This is source inspection,
  not execution of a TypeORM/driver handshake or an upgrade of that example.
- `python3 tools/check_instruction_artifacts.py standards/core.md
  standards/go/style.md standards/typeorm.md
  standards/typeorm/schema-verification.md
  docs/specs/2026-11-06-guidance-quality-and-skill-delivery.md
  docs/plans/2026-11-06-guidance-quality-and-skill-delivery.md` checked six
  artifacts with zero errors. After self-review clarified the TLS trust-root
  wording, the affected TypeORM topic was checked again with zero errors.
- `git diff --check` and separate no-index whitespace checks of both untracked
  task documents produced no diagnostics. Identity exclusion passed across all
  tracked and untracked nonignored files. Baseline hashes matched; scope inspection
  found only the four rule changes and two task-document updates, with HEAD and
  the Git index unchanged.
- Coordinator review compared all six files with their pre-stage copies and
  checked the new routes against existing catalog resources. No competing semantic
  owner, mandatory new stack, version change or unresolved in-scope finding was
  identified. The final plan status/evidence update also passed the artifact
  checker and whitespace/identity checks.
- No executable example, checker behavior, catalog resource or native skill changed.
  Runtime tests, regression suites and client activation runs were not selected
  for this prose stage. No such results are claimed.

All S1 candidates received dispositions; G1 and S1 completed. At the S1 handoff,
the human checkpoint was review of these changes under the
[direct-work policy](../../standards/work-modes.md#default-direct-work-with-human-checkpoints).
The proposed next stage was S5's conditional authentication/token contract and its
routes. S6, S2, S3 and S4 were pending; none had begun at that checkpoint.

## S5 execution evidence and next checkpoint

S5 completed on 2026-11-06 after the user's instruction to proceed. The new
[authentication topic](../../standards/security/authentication.md) owns the shared
contract and focused verification scenarios. Core supplies the conditional task
route and catalog resource; FastAPI, Gin, NestJS and Next.js topics link to it.

Source review used the linked sections of RFC 7515, RFC 7519, RFC 8725 and RFC 9700
for the chosen token contract. The topic identifies the review date and separates
RFC semantics from local capacity/failure policy. No provider, JWT library or
cryptographic implementation was installed, and no fixture/runtime version changed.

- `python3 tools/check_instruction_artifacts.py standards/core.md
  standards/catalog.toml standards/security/authentication.md
  standards/fastapi/runtime-operations.md standards/gin/routing-middleware.md
  standards/nestjs/transport-contracts.md standards/nestjs/verification-operations.md
  standards/nextjs/server-client-security.md
  docs/plans/2026-11-06-guidance-quality-and-skill-delivery.md` checked nine artifacts
  and the catalog with zero errors.
- `python3 -m unittest discover -s tests -p 'test_profile_selection.py'` passed
  all 43 existing tests. A separate catalog-selection check confirmed the topic
  is a bundle resource in core and each of the four affected framework closures.
  Schema 1, profile IDs, dependencies and other catalog fields are unchanged.
- `git diff --check` and separate no-index whitespace checks for all three
  untracked documents produced no diagnostics. Identity exclusion passed across
  tracked and untracked nonignored files. Baseline hashes matched; four unrelated
  pre-existing changed/untracked files remained byte-identical. The path inventory,
  HEAD and Git index matched the authorized scope and baseline.
- Coordinator review compared all nine affected paths with their S5 baseline,
  including the new topic's full contents. It mapped the specified acceptance
  and failure classes to the contract and scenario table, checked conditional
  reading and resource reachability, and retained existing framework authorization
  and browser protections. No unresolved in-scope finding remained.
- These results cover instruction content and bundle selection. No JWT verifier,
  provider integration, application authentication flow or native skill activation
  was executed. The new scenario table prescribes evidence for future consumer
  changes; it does not claim those scenarios ran here.

At the S5 handoff, S1 and S5 were complete and the checkpoint was review of S5
under the existing direct-work policy. The proposed next stage was S6: assess shared diagnostic
ownership and make a bounded improvement only where existing owners leave a gap.
S6, S2, S3 and S4 were pending; none had begun at that checkpoint.

## S6 execution evidence and next checkpoint

S6 completed on 2026-11-06 after the user's instruction to proceed.
[Core diagnostic ownership](../../standards/core.md#diagnostic-error-ownership)
now defines the shared reporting rule and conditional context requirements.
Go/Python error contracts and Node/Nest diagnostic sections route to that owner.
The gap decision above records the retained specialist coverage and no-change
dispositions for additional telemetry and operational policy.

- `python3 tools/check_instruction_artifacts.py standards/core.md
  standards/go/contracts.md standards/python/typing-contracts.md
  standards/nodejs/lifecycle-verification.md
  standards/nestjs/verification-operations.md
  docs/plans/2026-11-06-guidance-quality-and-skill-delivery.md` checked six artifacts
  with zero errors. Local links resolve to an existing required core resource;
  no catalog or adoption changes were needed.
- `git diff --check` and separate no-index whitespace checks of the three
  pre-existing untracked documents produced no diagnostics. Identity exclusion
  passed across tracked and untracked nonignored files. Baseline hashes matched,
  and all ten unrelated changed/untracked files stayed byte-identical.
- Scoped comparison confirmed that core gained only the new section and its
  task route, retaining S1/S5 content. The Nest authentication route remains intact.
  The path inventory, HEAD and Git index match the authorized scope and baseline.
- Coordinator review covered all six stage diffs. It checked propagation versus
  local handling, expected refusal, useful safe context, unavailable correlation,
  distinct failures and independently required access/audit/trace records. Native
  error semantics and runtime context mechanisms retain their existing owners;
  no unresolved in-scope finding remained.
- This is local instruction policy and routing. No vendor API/version claim,
  executable example, checker behavior or catalog selection changed. Runtime,
  client-activation and regression suites were not rerun; S5's 43 profile-selection
  results retain their original scope. Artifact checks do not demonstrate a
  consumer application's emitted logs or error-handling behavior.

At the S6 handoff, S1, S5 and S6 were complete and the checkpoint was review of S6 under the
[direct-work policy](../../standards/work-modes.md#default-direct-work-with-human-checkpoints).
The proposed next stage was S2: Angular component/directive contracts and the
corresponding examples and checks. S2, S3 and S4 were pending; none had begun at
that checkpoint.

## S2 execution evidence and next checkpoint

S2 completed on 2026-11-06 after the user's instruction to proceed. New
[component](../../standards/angular/components.md) and
[directive](../../standards/angular/directives.md) topics own the selected
contracts; the Angular entry routes to them. The existing forms section retains
its anchor and form semantics while routing component APIs to their new owner.
The [example](../../standards/angular/examples/component-contracts.md) supplies
eight extractable files and the maintenance guide supplies its selector.

The [dated Angular evidence](../research/2026-11-06-angular-component-contracts.md)
records official v20 source review, resolved versions, runtime outcomes and
evidence limits. Earlier Angular/NgRx and SCSS records were preserved unchanged.

- `npm run build` passed strict Angular 20.3.0 TypeScript/template compilation
  and bundling of the emitted test modules. `npm test` passed six meaningful
  zoneless TestBed/DOM cases, zero failures/skips. The final eight Markdown blocks
  exactly match the compiled source files.
- An isolated invalid consumer produced the expected NG8002 and NG8008 errors;
  omitting listener removal made the destruction assertion fail. Both temporary
  negative probes were removed and the valid fixture passed. Review corrected
  pure type imports; because emitted modules changed, the affected build and all
  six runtime cases were checked again. No type suppression or forced rendering
  was used to obtain a passing result.
- `python3 tools/check_instruction_artifacts.py standards/angular.md
  standards/angular/boundaries.md standards/angular/components.md
  standards/angular/directives.md standards/angular/verification.md
  standards/angular/examples/component-contracts.md standards/catalog.toml
  docs/maintenance/verification.md
  docs/research/2026-11-06-angular-component-contracts.md
  docs/plans/2026-11-06-guidance-quality-and-skill-delivery.md` checked ten artifacts
  and the catalog with zero errors.
- `python3 -m unittest discover -s tests -p 'test_profile_selection.py'` passed
  all 43 tests with the existing Angular topic fixture extended. Catalog comparison
  confirmed only the three intended Angular resources were added; schema, IDs,
  dependencies and prior core authentication availability were preserved. Angular
  alone selects neither NgRx nor Node guidance.
- `git diff --check` and separate no-index checks of all seven untracked documents
  passed. Identity exclusion passed across tracked and untracked nonignored files.
  All fourteen unrelated pre-existing changed/untracked files remained byte-identical;
  the path inventory, HEAD and index matched the authorized scope and baseline.
- Coordinator review covered all eleven stage paths, including the new documents
  and the full embedded fixture. Ownership, version conditions, lifecycle, actual
  notification paths, public API exposure, strict/no-any TypeScript usage, type
  imports and evidence limits were checked. No unresolved in-scope finding remained.
- The temporary runtime, extracted copy and npm cache were removed after checks.
  Baseline copies, source identities, lockfile, resolved tree and logs remain in
  the stage's external directory. No dependency files were installed at the AEK
  root, and no native skill or consuming application was installed or modified.

At the S2 handoff, S1, S5, S6 and S2 were complete and the checkpoint was review of S2 under the
[direct-work policy](../../standards/work-modes.md#default-direct-work-with-human-checkpoints).
The proposed next stage was S3: prepare the optional Angular reference skill and
explicit adoption mapping. S3 and S4 were pending; neither had begun. Passing
DOM/artifact checks does not establish browser accessibility, SSR/hydration or
native skill activation.

## E1 execution evidence and delivery decision

The user's subsequent request made addition conditional on demonstrated benefit.
E1 therefore evaluated an isolated candidate before modifying production templates,
catalog availability or adoption instructions. The
[dated evaluation](../research/2026-11-06-angular-skill-evaluation.md) owns the full
method, outcomes, usage observations and limitations; this plan owns progress.

Eight fresh read-only Codex CLI runs covered three paired scenarios, including a
reverse-order repeat of the component pair. Native discovery and actual skill-body
reads were observed. Both arms met all reviewed technical criteria; the negative
TypeScript task did not select the Angular skill. No material scope violation or
fixture mutation was observed. Lower input totals in Angular runs are retained as
a favorable signal, but higher output/command counts, inconsistent elapsed time,
small coverage and unavailable native Superpowers procedure loading limit the
inference. No general cost, activation-frequency or implementation-quality gain
is claimed.

Decision: retain direct Angular routes. E1's addition condition is not established
by this sample, so S3 integration and wider S4 rollout are deferred, not completed.
The temporary candidate is evidence outside discovery, not a shipped AEK skill.
Reopening it needs a concrete routing/use requirement or stronger comparison;
no new approval or setup is needed to keep using the existing rules.

The retained external archive is
`/home/vitalii/.codex/research/aek-guidance-2026-11-06/angular-skill-evaluation/`.
It contains raw inputs/results, source identities, candidate, fixture snapshots
and baseline copies. All 82 archived payload files matched their recorded SHA-256
hashes after retention; the temporary workspace was then removed. Earlier
comparison archives and S1/S5/S6/S2 changes remain intact.

- The artifact checker on the plan, specification and new evaluation record
  checked three artifacts and the source catalog with zero errors.
- `git diff --check` and separate no-index whitespace checks of all eight untracked
  documents passed. The excluded-identity scan passed across tracked and
  untracked nonignored files.
- Baseline comparison confirmed that only these three task/evidence documents
  changed in E1. All other prior contents and absences, HEAD and the Git index
  were preserved. No Angular template, catalog resource or adoption mapping was
  added; the candidate remains an archived experiment.
- Coordinator review covered the actual three document diffs, complete native
  results and tool traces, discovery/fixture identities, scoring and stated limits.
  No in-scope unresolved finding remained. Runtime/application and profile-selection
  suites were not rerun because their inputs and acceptance were unchanged.

E1 is complete as an assessed delivery decision. Deferred S3/S4 markers do not
claim completed implementation or a completed wider pilot. Existing direct routes
remain usable without any new installation or permission step.
