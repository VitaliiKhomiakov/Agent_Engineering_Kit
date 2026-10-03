# Instruction framework refinement implementation plan

Date: 2026-09-26. Updated: 2026-09-27. Status: S1–S5 implemented and verified;
library refinement complete. S1–S4 accepted; final handoff awaits user review.

**Goal:** Make instruction selection, saved orchestration choices and task execution
consistent while reducing unnecessary process context.

**Architecture:** Keep the rules-only library and native client mechanisms. Define
reading semantics, complete the saved selection contract, and move compatibility
detail behind conditional routes. Preserve existing native task stores.

**Artifacts:** Markdown, TOML and instruction-only skill templates.
**Spec:** [Instruction framework refinement](../specs/2026-09-26-instruction-framework-refinement.md).
Executors read the specification and this plan; the specification owns R1–R6 and
A1–A8, while this document owns progress and evidence.

## Global Constraints

- Current authorization: after S4, the user instructed completion of S5.
  The authorized library work is complete; P1 remains a separate follow-up.
- Execution: inline, one logical stage followed by user review; reuse
  any later explicit authorization for several stages without repeated questions.
- Workspace and project checkout: `/home/vitalii/Documents/Local_Project/AgentsFramework`.
  The current checkout is the implementation directory; no worktree is selected.
- Canonical task: this plan owns progress; the linked specification owns requirements.
  Both retain their existing workspace paths. No native tool context is needed here.
- No authorized Git writes, target-project installation, global configuration
  changes, external model calls or plugin-cache edits. Git metadata is unavailable
  in the audit environment; use scoped original-content copies when necessary.
- The accepted 2026-09-22 scope and historical plans remain closed. No application,
  installer, CLI, monitor or new permanent testing infrastructure is introduced.
- Use the current session for planning. A target workspace's model selection is
  resolved during its adoption; this plan selects no model or new agent role.
- Preserve strict typing, engineering boundaries, relevant mandatory checks,
  explicit permissions, stage checkpoints and existing user work.
- Before implementing each stage, capture original contents/absence for every
  affected path and record its baseline location here. Never reconstruct a prior
  baseline from already modified files or overwrite it with an intermediate state.
- Proposed new reference files are registered with the portable catalog. Archived
  evidence is referenced rather than rewritten as current verification.

## Sequence and requirement coverage

| Stage | Observable result | Requirements / scenarios | Depends on |
| --- | --- | --- | --- |
| S1 | Unambiguous reading semantics and repaired navigation | R1, R6 / A2, A8 | User instruction to begin, received |
| S2 | Complete saved selection and nonintrusive entry behavior | R2, R3 / A1, A3–A5 | S1 |
| S3 | Compact prompts and conditional Superpowers compatibility | R4 / A6, A8 | S1, S2 |
| S4 | Existing native task stores remain canonical | R5 / A7 | S2, S3 |
| S5 | Integrated library acceptance and accurate handoff | R1–R6 / A1–A8 | S1–S4 |
| P1 | Observed adoption in one chosen client/project | Follow-up only | S5 and separate pilot authorization |

Each stage updates its affected authoritative text and entry summaries together;
do not knowingly leave contradictory active instructions for the next stage.
One accountable scoped review follows each stage. Independent review/delegation
is conditional on a concrete need, not a mandatory step for every document edit.

## Task 1: Reading routes and navigation (S1)

**Create:** `standards/catalog.md`.
**Modify:** `standards/catalog.toml`, `ARCHITECTURE.md`, `MIGRATION.md`,
`templates/AGENTS.root.md`, `templates/policy-entry.md`,
`standards/php/structure.md`, `standards/symfony/structure-services.md`.

**Consumes:** Existing IDs, dependency/resource paths, task conditions and R1/R6.
**Produces:** Documented catalog-v1 semantics and correct model-placement links.

- [x] Capture the stage baseline; explain `dependencies`, `resources`, `required`,
  applicability hints and `when` using the exact distinction in R1.
- [x] Link the catalog guide from the catalog and adoption instructions; include
  it among bundled assets so copied catalogs retain their semantic reference.
- [x] Align entry routes: presence in a bundle is not mandatory reading; broad
  technology/glob matches do not enable absent frameworks or languages.
- [x] Repair both domain-model-placement anchors to the actual Doctrine owner.
- [x] Parse catalog TOML; check unique profile IDs, existing resources/dependencies,
  affected links/anchors and unchanged profile selection coverage.
- [x] Walk through A2 (Python-only, JavaScript React, inline planning) and A8.
  Record selected/excluded sections, actual evidence and the checkpoint.

## Task 2: Saved selection and first-use behavior (S2)

**Modify:** `templates/framework/model-routing.toml`,
`standards/model-configuration.md`, `standards/orchestration.md`,
`templates/skills/af-model-setup/SKILL.md`,
`templates/skills/af-model-reassign/SKILL.md`, `templates/AGENTS.root.md`,
`templates/policy-entry.md`, `templates/codex/README.md`,
`templates/codex/config.toml`, `templates/codex/agents/af-implementer.toml`,
`templates/codex/agents/af-reviewer.toml`, `ARCHITECTURE.md`, `MIGRATION.md`.
Keep the README's setup trigger and first-use paragraph aligned in this stage;
the remaining integrated README work stays in S5.

**Consumes:** R2 field contract, R3 state table, S1 reading semantics.
**Produces:** Version-2 example and a single authoritative setup/reassignment
procedure covering legacy records, disabled roles and ordinary work without setup.

- [x] Capture the baseline and describe all R2 fields, configured-state invariants
  and single-agent/delegated examples. Keep examples inactive and distinguish
  suggested pairs from confirmed assignments.
- [x] Define v1 reading and authorized migration, unknown-version handling and
  partial-write recovery. Preserve unspecified choices and unrelated native settings.
- [x] Describe native mapping for enabled roles, disabled managed roles, model/effort
  and concurrency; report unsupported enforcement without fabricating a setting.
- [x] Update skills and entry routes using R3. Missing configuration permits ordinary
  inline work; explicit setup/delegation requests still resolve necessary choices.
- [x] Align native examples and role instructions with the new contract; remove any
  implication that a role's existence requires its use or that a write activates it.
- [x] Parse affected TOML and skill frontmatter; inspect relative paths at the
  documented installed locations. Check configured and unconfigured sample records
  against the documented fields with disposable fixtures if useful.
- [x] Walk through A1 and A3–A5, including a disabled reviewer, missing legacy fields,
  partial native agreement, invalid edges and an unavailable selected pair. Record
  expected behavior and mismatches without launching models or installing templates.

## Task 3: Prompt simplification and compatibility (S3)

**Create:** `standards/superpowers/compatibility.md`.
**Modify:** `standards/superpowers.md`, `standards/core.md`,
`standards/catalog.toml`, `templates/AGENTS.root.md`, `templates/AGENTS.project.md`,
`templates/policy-entry.md`, `templates/PLANS.md`, `templates/task.md`,
`templates/codex/agents/af-implementer.toml`,
`templates/codex/agents/af-reviewer.toml`, `ARCHITECTURE.md`, `MIGRATION.md`.

**Consumes:** Stable S1 reading semantics, S2 entry behavior and existing process owners.
**Produces:** Short entry/role prompts, a routed core profile and conditional helper guidance.

- [x] Capture the baseline and map each repeated process requirement to its owner.
  Retain short permission/scope/evidence reminders in entry and role instructions.
- [x] Add a core task-to-section table and shorten the root template toward its
  40–70 substantive-line guideline without dropping critical requirements.
- [x] Move helper usage details, caveats and dated 6.4.1 evidence into the new
  compatibility reference; register it as a `superpowers` resource.
- [x] Keep selection/authority/adaptations in the common policy and add the direct
  scoped-task fallback. No ordinary task must inspect unused helper internals.
- [x] Inspect only relevant installed 6.4.2 contracts and record what was checked,
  actual differences and remaining limits. Preserve the 6.4.1 historical evidence;
  do not install, update, activate or patch the plugin.
- [x] Check A6/A8 and before/after entry sizes. Review preservation of no-commit
  defaults, checkpoints, saved choices, fresh scoped handoffs, work preservation,
  required gates and evidence reuse. Report remaining duplication with its purpose.

## Task 4: Canonical planning stores (S4)

**Modify:** `templates/PLANS.md`, `templates/task.md`, `standards/work-modes.md`,
`standards/delivery-workflow.md`, `standards/orchestration.md`,
`standards/superpowers.md`, `standards/superpowers/compatibility.md`,
`templates/AGENTS.root.md`, `templates/AGENTS.project.md`,
`templates/policy-entry.md`, `templates/codex/agents/af-implementer.toml`,
`templates/codex/agents/af-reviewer.toml`, `ARCHITECTURE.md`, `MIGRATION.md`.

**Consumes:** R5, existing native artifact ownership and S3 common policy.
**Produces:** A consistent distinction between workspace navigation, canonical
task storage and the checkout where project edits/checks run.

- [x] Capture the baseline; keep workspace storage as the default for new plain
  plans and preserve an existing native store at its supported location.
- [x] Remove forced-relocation blockers from every affected instruction/role.
  Define relocation as a separately requested migration.
- [x] Extend task handoffs with the canonical artifact location and preserve one
  owner for decisions/progress; workspace navigation does not duplicate checklists.
- [x] Walk through A7 for workspace entry, independent project entry and an
  authorized worktree. Cover an inaccessible store without creating a second copy.
- [x] Search affected active documents for residual unconditional requirements to
  keep every native plan at workspace root. Validate replacement links and routes.

## Task 5: Integrated acceptance and handoff (S5)

**Modify:** `README.md` and this plan. Correct other S1–S4 files only for concrete
cross-document conflicts found during this stage.

**Consumes:** Completed stage evidence and the final R1–R6 contracts.
**Produces:** A reviewable library revision with clearly bounded readiness claims.

- [x] Update README usage/setup/planning routes and adoption limits to match the
  resulting policy. Leave the accepted baseline specification and historical plans intact.
- [x] Parse all five existing TOML files plus any TOML examples introduced by S2;
  check catalog uniqueness, dependencies, complete standards registration and resources.
- [x] Validate affected Markdown links/anchors, fence structure and skill frontmatter.
  Resolve relocatable templates from their documented target base.
- [x] Inspect A1–A8 together for contradictory routes or instructions. Reuse valid
  prior checks unless changed inputs invalidate them; record scenario scope/outcome.
- [x] Review only the accumulated stage changes against their captured baselines.
  Distinguish static instruction evidence from any actual runtime observation.
- [x] Record final changed paths, criteria, checks, residual limitations and pilot
  prerequisites. Library completion requires all R1–R6 criteria; P1 is not its gate.

## Follow-up P1: Bounded adoption pilot

P1 is specified for future execution and is not authorized by the current library
implementation scope. Select the actual target project, client/version, model choices and
allowed configuration edits before starting it. Reuse later explicit authorization.

Exercise the scenarios in the specification's follow-up section in that one client.
Record discovered instructions, actual checks, stage stopping, resumption and
available model/effort evidence. Fix confirmed in-scope issues; report unknown
telemetry honestly. Do not infer compatibility with other clients or launch a broad
benchmark. Store pilot evidence in its own adoption task and link it here.

## Verification method and review focus

Use existing tools: Python `tomllib` for TOML; an available YAML parser or native
skill validator for frontmatter; scoped link/anchor inspection and temporary
scripts for catalog integrity. If a validator is unavailable, record the exact
manual check and limit. No dependency installation is needed for the planning pair.

Review the failure scenarios that motivate the change: accidental recursive reading,
unrequested setup, disabled-role activation, silent v1 migration, helper-driven
commits/retests, loss of critical constraints during shortening, and duplicate or
forced-moved native plans. Stage walkthroughs own these checks. No arbitrary count
of tests/reviewers and no repetition of the removed application's test suite.

## Current handoff

- Authorization: the user accepted S4 and instructed continuation to S5 under
  the stage checkpoints.
- Planning baseline: `/tmp/af-refinement-planning-iylckxyp/baseline.json` records
  prior absence of both files. `inventory.json` records hashes of existing files
  to confirm the planning task changed no existing repository content.
- Current implementation stage: S5 implemented and verified. All S1–S5 library
  criteria are satisfied; final handoff awaits user review. No library stage remains.
- S5 baseline: `/tmp/af-refinement-s5-p_mpl38t/baseline.json`; `original/`
  preserves README, this plan and the two narrowly corrected entry documents.
- S4 baseline: `/tmp/af-refinement-s4-440qzyug/baseline.json`; `original/`
  preserves the 14 affected instruction files and this plan before any S4 write.
- S1 baseline: `/tmp/af-refinement-s1-_4knzqzk/baseline.json`; original contents
  are under its sibling `original/` directory. The new guide's prior absence is
  recorded. Scope includes the eight S1 artifacts and the two planning documents
  for authorization/status updates. No historical acceptance record is changed.
- Preflight: S1 supplies reading semantics to S2/S3; S2 supplies entry behavior
  to S3; S3 supplies policy routes to S4; S5 integrates their evidence. No shared
  interface conflict was found. S1's inline-planning walkthrough assumes an
  existing configured selection; missing-profile behavior belongs to S2.
- P1 remains separately gated by target adoption scope.
- Planning verification: PASS on 2026-09-26. Checked 12 local links/anchors,
  Markdown fences, placeholder absence, six requirements, eight acceptance
  scenarios and five implementation stages. Scope inspection confirmed exactly
  these two new documents and all 178 existing files unchanged. Author review
  checked requirement-to-stage coverage, ownership and authorization boundaries.
  Evidence: `/tmp/af-refinement-planning-iylckxyp/planning-checks.json`.
  At that planning handoff, implementation and runtime scenarios had not run.

### S1 result and evidence

Added `standards/catalog.md` as the owner of catalog-v1 semantics and a bundled
asset. Aligned architecture, migration and entry templates; repaired the PHP and
Symfony domain-model-placement links. Catalog schema, all 19 profile records,
dependency edges and native-template mappings are unchanged.

| Scenario | Inspected route and result |
| --- | --- |
| A2: Python-only signature fix without FastAPI/Pydantic | Entry selects core responsibilities, Python entry and typing/contracts, with relevant verification. Combined-profile resources do not select FastAPI, Pydantic, ORM or database guidance. PASS |
| A2: JavaScript React state fix without Next.js/TypeScript | Entry selects shared JavaScript values/state and React state/identity sections; TypeScript dependency is available but not applicable. No Next.js or Node server rules are selected. PASS |
| A2: substantive inline plan, session selection configured | Planning policy, delivery/design and selected Superpowers adaptations apply. Catalog dependencies do not trigger delegation or model setup. Missing-profile behavior remains S2 scope. PASS |
| A8: S1 artifact integrity and scope | Five TOML files parse; 19 profile definitions preserved; all 134 standards documents registered; 139 catalog paths exist; 57 local links/anchors checked, resolving policy-entry from its intended installed root. PASS |

Command: `python3 /tmp/af-refinement-s1-_4knzqzk/check_s1.py`.
Evidence: `checks.json` and `changes.diff` in that directory. Scope comparison
shows exactly the eight S1 artifacts plus the specification/plan status updates;
171 pre-existing files remain unchanged. Author review checked the actual diff
against the captured baseline and clarified that Next.js rules still apply when
the framework is actually used, including in JavaScript projects. No material
S1 finding remains unresolved.

These are static artifact checks and route walkthroughs, not observed client
execution, measured context savings or full A8 acceptance for later stages.
No model calls, installation, Git writes or delegated review were performed.
Checkpoint resolved: the user accepted S1 and instructed continuation to S2.

### S2 execution scope

Baseline: `/tmp/af-refinement-s2-q54tdjr9/baseline.json`; original contents are
under `original/` in that directory. It includes the 13 planned S2 artifacts,
README and this plan. The README's setup trigger and first-use paragraph move
forward from S5 so the current user-facing entry does not contradict the revised
policy. No remaining S5 work or S3 prompt restructuring is started.

The `writing-skills` procedure is used for narrow triggers and skill structure;
verification follows this plan's static format/scenario checks. The authorized
scope does not include installation or model pressure-test calls. Existing native
Codex keys for enablement, defaults, concurrency and roles were rechecked against
the official subagents documentation on 2026-09-26; this is documentation evidence,
not a live client test. Setup uses the current session and no model assignment
is made for this repository.

### S2 result and evidence

Version-2 routing now records client, enabled roles, pairs, delegation mode/edges
and ceiling. The delegated template keeps its pairs as suggestions and disables
the optional reviewer; the model-configuration standard includes a single-agent
example. Both remain `unconfigured`. Entry routes and skill triggers allow ordinary
inline work without onboarding. Native mapping, disabled-role retirement, legacy
handling and scoped partial-write recovery have one owner in model configuration.

| Scenario | Static walkthrough and result |
| --- | --- |
| A1: documentation edit without a profile | Root and policy-entry permit the current session, relevant rules and artifact checks; absence alone triggers neither skill, model questionnaire nor writes. PASS |
| A3: explicitly selected single-agent setup | Coordinator pair, zero framework ceiling, no specialists/edges; Codex uses its supported disable switch rather than assuming a zero native thread limit. Unsupported client enforcement is reported as policy only. PASS |
| A4: delegated setup with disabled reviewer | Only enabled endpoints and an allowed edge permit a handoff; a retained reviewer pair/file is not enablement. No anonymous worker replacement; required independent review still needs a clarified assignment. PASS |
| A5: configured v1 record | Known pairs and limit remain intact; missing client/enablement/edges are unknown. Compatible inline work proceeds; authorized setup/reassignment resolves gaps before migration. PASS |
| A5: copied unconfigured template or unknown schema | Suggested fields do not satisfy consent; setup returns early only for a consistent configured selection. Unknown versions are clarified before writes/delegation rather than routed through a guessed upgrade. PASS |
| A5: partial native update | Saved status alone does not establish agreement. Recover only task changes; if recovery remains incomplete, preserve choices and expose unconfigured state/mismatches. Known choices still constrain dependent work. PASS |
| A5: unsupported pair or active mismatch | Report and resolve the assignment before dependent work; preserve independent work and do not claim activation from saved files. Unknown telemetry remains unknown. PASS |

Command: `python3 /tmp/af-refinement-s2-q54tdjr9/check_s2.py`.
Result: PASS for five TOML files, the single-agent TOML example, both YAML skill
frontmatters, installed skill-reference paths and 95 local links/anchors. The
temporary structural probe accepts two hypothetical configured examples and
rejects eight malformed examples: missing client/pair, disabled-role edge,
self-edge, cycle, unreachable edge, nonzero single-agent ceiling and unknown schema.
It also compares suggested native pairs/ceiling with the routing example and
confirms legacy sample pairs are retained. No hypothetical record is installed.

Evidence: `checks.json`, `shape-probes.json` and `changes.diff` under the S2 baseline
directory. Exactly 15 scoped files changed; 166 pre-existing files are unchanged.
Author review covered the full scoped diff, preserved S1 behavior and the cases
above. No material S2 finding remains unresolved. These checks establish artifact
consistency and documented behavior, not actual agent adherence or client activation.

Next checkpoint: user review of S2. Proposed next stage: S3 prompt simplification
and conditional Superpowers compatibility, after instruction to continue.

## S3 implementation evidence — 2026-09-26

The user's instruction to continue accepted S2 and authorized S3. The original
S3 file set is unchanged; this plan also records progress. S4's native-store
semantics and the S5 integration/pilot work remain pending.

Baseline: `/tmp/af-refinement-s3-b5_kqbg6/baseline.json`; `original/` preserves all
13 existing affected files, and the new compatibility file's prior absence is
recorded. `inventory.json` covers the surrounding workspace before this stage.

### Ownership and intentional reminders

| Requirement | Detailed owner | Short reminder retained where needed |
| --- | --- | --- |
| Mode, stage checkpoint, Git and integration | `standards/work-modes.md` | Root/entry and implementer retain authorization and stop boundaries; reviewer cannot authorize progression |
| Baseline/user work, checks, scoped review and evidence reuse | `standards/verification.md` | Entry/roles retain before-write preservation, required gates, reuse and honest reporting |
| Stage structure and planning content | `standards/delivery-workflow.md`, workspace `PLANS.md` | Task fields record actual decisions, permissions and evidence; they do not define another procedure |
| Roles, fresh context and bounded handoffs | `standards/orchestration.md` | Root/task route to the contract; workers require assignment/mapping and pass policy explicitly |
| Saved choices and setup | `standards/model-configuration.md` | Entry preserves inline first use and conditional setup; role files remain inactive examples |
| Engineering decisions | `standards/core.md` and selected profiles | Root retains strict typing, boundaries, simple flow and size safeguards; the new table routes detail by task |
| Skill adaptations versus helper contracts | `standards/superpowers.md` / `standards/superpowers/compatibility.md` | Common policy owns fallback; helper/reference loading is conditional |

Permission, scope and evidence reminders intentionally remain in entry and role
prompts because those surfaces can be loaded independently. Detailed verification,
review and integration recipes have a single owner. No line wrapping was collapsed
to achieve the entry target; counts below include all nonempty lines (headings and
tables too), with no tokenizer or runtime context-savings claim.

| Prompt | Before, nonempty lines | After, nonempty lines |
| --- | --- | --- |
| Root AGENTS template | 96 | 60 |
| Policy entry | 48 | 39 |
| Implementer TOML, including metadata | 33 | 26 |
| Reviewer TOML, including metadata | 34 | 26 |
| Common Superpowers policy | 144 | 67 |

### Scoped acceptance

| Scenario | Inspection and result |
| --- | --- |
| A6: ordinary task with an available skill | Common policy selects the procedure and binding adaptations; no helper internals or historic evidence must be loaded. PASS |
| A6: toolkit absent or helper unsuitable | Direct bounded task, preserved baseline, actual changes and required checks remain available; no automatic installation, commits, repeated checks or parallel ledger. Only dependent missing capabilities block. PASS |
| A6: delegated task | Root/task routes require fresh scoped context and permissions; role prompts require saved enabled assignment, incoming edge, checkout/baseline and loaded relevant rules. Applicable Superpowers adaptations must reach the worker. PASS by document inspection, not a live handoff |
| A8: shorter prompts | Reviewed retained no-Git default, checkpoints, existing choices/work, required gates, evidence reuse, incidental-finding limits and strict engineering constraints against the original baseline. PASS |
| A8: unchanged earlier contracts | Catalog selection semantics, v2 role metadata/choices and ordinary inline first use preserved. Existing incoming spec anchors retained. S4's current planning-location rules remain routed through PLANS pending that stage. PASS |

### Compatibility evidence and limits

Local 6.4.2 manifest and eight relevant source files were inspected/compared with
6.4.1. Five helper scripts and both execution skills are byte-identical. Planning
instructions changed toward checkable steps, signatures/interfaces and proportional
plan detail; remaining stock defaults still need the common adaptations. The new
reference preserves the historical 2026-09-20 evidence and distinguishes it from
this source-only inspection. `source-comparison.json` records hashes/results.
No helper execution, native client activation or pilot was performed in S3.

Artifact check: `python3 /tmp/af-refinement-s3-b5_kqbg6/check_s3.py`.
It parses all five TOML files, verifies 19 profile IDs and dependencies, checks all
135 registered standards and catalog paths, resolves affected local links/anchors,
compares native role metadata and catalog changes with the original, and checks
scope against the workspace inventory. `checks.json` and `changes.diff` retain
results and the complete scoped change set. Exactly 14 scoped paths change
(including the new reference and this plan); 168 prior files remain unchanged.
These are library artifact checks, not proof of agent adherence in a real session.

No material S3 finding remains unresolved. Next checkpoint: user review of S3.
Proposed next stage: S4, preserving existing native task stores as canonical,
after instruction to continue.

## S4 implementation evidence — 2026-09-27

The user's instruction to execute accepted S3 and authorized S4 under the existing
checkpoints. All 14 planned instruction files and this plan were updated. Baseline:
`/tmp/af-refinement-s4-440qzyug/baseline.json`; original contents are in `original/`,
and `inventory.json` records the pre-stage workspace hashes. No task store was moved
or created, and no native tool, installation or client pilot was run.

### Contract and scenario review

The planning policy owns storage rules: workspace `docs/plans/` is the default for
new plain plans, while existing canonical tasks retain their supported location.
Entry/role prompts, work modes, delivery, orchestration and Superpowers now distinguish
instruction root, canonical artifact/progress owner and implementation checkout.
Workspace navigation and temporary briefs carry no second editable task checklist.

A7 walkthrough inputs below are illustrative paths, not installed artifacts:
workspace `W`, nested project `P`, canonical native task `C` inside `P`, and an
explicitly authorized implementation worktree `T`.

| Input / entry | Required action and inspected result |
| --- | --- |
| Enter from `W`, resume `C` | Follow workspace navigation to `C`; read/update its existing artifacts and native progress owner. Project changes/checks stay in the mapped `P`. No relocation or duplicate checklist. PASS |
| Open `P` independently | Use reachable local policy and its native task entry to reach `C`; parent discovery or creating a workspace navigation file is not required to resume. PASS |
| Implement from `T` | Handoff retains absolute `C` and its owner, names `T` separately for edits/checks, and supplies the supported native tool context. A tracked task copy in `T` is not promoted to a second progress record. Verify resolved paths when invoking native tools. PASS |
| `C` is inaccessible | Report the specific path/access obstacle; pause dependent work without recreating the task or treating a stale checkout copy as current progress. Independent work can continue. PASS |
| Create a new plain task | Default to `W/docs/plans/`; separate design only when warranted. A small edit still needs no saved plan. PASS |
| User separately requests relocation | Treat as its own migration preserving identity, progress, links and native tracking; unsupported relocation blocks that migration only. No relocation is implied by ordinary task continuation. PASS |
| Cleanup finds a canonical store in `T` | Retain the worktree while the store is needed, or complete an explicitly authorized relocation before removal. Existing Git/integration permissions and user-work preservation remain binding. PASS |

These are document-consistency walkthroughs, not observed OpenSpec/Spec Kit/client
execution. Native path resolution and extension support must be verified in the
chosen installation when those tools are actually used.

### Artifact checks and review

Command: `python3 /tmp/af-refinement-s4-440qzyug/check_s4.py`.
PASS: five TOML files parse; 19 profiles, 135 registered standards and 141 catalog
path references resolve; 73 affected local links/anchors resolve. Catalog contents
and native role metadata/model pairs remain unchanged. The policy-entry links are
resolved from their intended installed workspace root. The task template now
explicitly calls for adapting reference links when adopted at another location.

A scoped before/after review covered the complete instruction diff, preserved S1–S3
constraints and the scenarios above. Targeted searches across active standards,
templates, architecture and migration text found no remaining unconditional demand
to move native plans to the workspace root. Historical evidence remains intact.
The README's current navigation description does not demand relocation; integrated
readiness wording remains S5 work.

`checks.json` and `changes.diff` under the S4 baseline retain the results and scoped
diff. Exactly 15 scoped files changed; 167 pre-existing files remain unchanged.
No material S4 finding remains unresolved. Next checkpoint: user review of S4.
Proposed next stage: S5 integrated library acceptance and README/handoff, after
instruction to continue. The live adoption pilot remains a separate follow-up.

## S5 integrated acceptance — 2026-09-27

The user accepted S4 and authorized S5. The README now describes catalog reading,
conditional setup/delegation, retained native task stores, direct skill fallback
and the distinction between library checks and observed client execution.
Two concrete consistency corrections extend S5 beyond README/progress:

- `templates/AGENTS.root.md`: S3's broad phrase about avoiding helper interfaces
  could prohibit a justified contract. It now permits them for a concrete contract,
  consistent with the core standard and the retained typed-boundary requirements.
- `templates/codex/README.md`: examples are to be adapted during authorized setup;
  the wording no longer implies their suggested pairs were already confirmed.

Both files were added to the S5 baseline before editing. No skill procedure,
routing field, native metadata or saved example pair changed during S5.

### Integrated requirement and scenario acceptance

The review followed the accumulated stage changes against their first captured
contents/absence, reused earlier scoped reviews, and checked the interactions below.
These are static instruction walkthroughs; no task was dispatched to a client.

| Scenario / requirement | Final input, route and outcome |
| --- | --- |
| A1 / R3 | A small documentation edit with no routing record follows entry, work-mode and verification rules inline. No setup questionnaire, profile write, delegation or saved plan is required. README and both entry templates agree. PASS |
| A2 / R1 | Python-only work selects relevant Python sections; JavaScript React selects shared JS and React sections, excluding unused TypeScript/Next.js/FastAPI/Pydantic requirements. A substantive inline plan selects planning/delivery and applicable skills, without following dependency edges into setup or delegation. Catalog/entries/profile routes agree. PASS |
| A3 / R2 | Single-agent choice records client/coordinator pair, no enabled specialists or edges and zero framework ceiling. The native mapping disables agent tools where supported without inventing a zero native thread limit. Template, contract and README agree. PASS |
| A4 / R2 | Delegated example remains unconfigured; an enabled pair, allowed incoming edge, capacity and task authorization are necessary for a handoff. Disabled reviewer templates remain inactive and cannot be replaced by anonymous workers. Role prompts preserve this contract and fresh scoped handoffs. PASS |
| A5 / R2–R3 | v1 values are preserved with missing fields unknown; migration is limited to authorized setup/reassignment. Unknown schemas require clarification before writes/delegation. Partial updates preserve choices and expose mismatches; unsupported pairs are not silently replaced and saved state is not activation. Skills and owning policy agree. PASS |
| A6 / R4 | Ordinary skill use reads common adaptations; helper commands/version evidence are conditional. Missing toolkit or unsuitable helper permits direct scoped work with required checks and actual-change review. No commits, extra ledger or redundant test runs are introduced. Applicable policy and saved choices survive handoff. PASS |
| A7 / R5 | Workspace, independent-project and worktree entry retain the existing canonical task/progress owner; navigation carries no second checklist. Inaccessible storage blocks dependent work without replacement. Relocation is a separate migration; native paths are verified only when tools are used. S4 walkthrough remains applicable. PASS |
| A8 / R4–R6 | Current TOML/YAML, catalog coverage, Markdown fences and affected local paths/anchors pass. PHP/Symfony links reach the Doctrine owner. Critical permissions, baseline preservation, strict engineering constraints, checkpoints and sufficient verification remain explicit or routed to their owner. Accepted historical material is unchanged. PASS |

No unresolved material conflict remains in the reviewed scope. An end-to-end
client run is still needed to establish adherence, discovery and activation;
static acceptance does not answer those runtime questions.

### Final checks and evidence reuse

Command: `python3 /tmp/af-refinement-s5-p_mpl38t/check_s5.py`.
Results: PASS for five TOML files, one TOML example, two skill YAML frontmatters,
19 unique profiles and valid dependency references, all 135 registered standards,
141 catalog path references and 164 affected local links/anchors. Markdown fences
are balanced. Relocatable policy-entry links use the installed workspace root;
skill references also resolve from the intended `.agents/skills/` layout.

S2's two accepted hypothetical records and eight rejected malformed records are
reused from `shape-probes.json`: their routing example, format contract and native
config hashes match the captured post-S2 inventory. Role metadata/pairs are also
unchanged; subsequent role-instruction edits were reviewed in S3–S5. No probe was
installed or treated as runtime enforcement. S3's dated source comparison and S4's
storage walkthrough remain valid for their unchanged contracts.

S5 modifies exactly four scoped files; 178 existing files are unchanged in this
stage. `checks.json`, `changes.diff` and `aggregate.diff` in the S5 baseline directory
record the final checks, stage diff and cumulative diff against earliest baselines.
The cumulative work includes 24 modified existing files and four new documents;
154 files present before planning are unchanged. The accepted 2026-09-20 baseline
specification and closed historical plans are among those unchanged files.

### Final changed paths

| Area | Paths relative to the repository |
| --- | --- |
| Orientation | `README.md`, `ARCHITECTURE.md`, `MIGRATION.md` |
| New refinement documents | `docs/specs/2026-09-26-instruction-framework-refinement.md`, `docs/plans/2026-09-26-instruction-framework-refinement.md` |
| Catalog | New `standards/catalog.md`; updated `standards/catalog.toml` |
| Shared standards | `standards/core.md`, `standards/work-modes.md`, `standards/delivery-workflow.md`, `standards/model-configuration.md`, `standards/orchestration.md`, `standards/superpowers.md` |
| Conditional compatibility | New `standards/superpowers/compatibility.md` |
| Repaired anchors | `standards/php/structure.md`, `standards/symfony/structure-services.md` |
| Entry/planning templates | `templates/AGENTS.root.md`, `templates/AGENTS.project.md`, `templates/policy-entry.md`, `templates/PLANS.md`, `templates/task.md` |
| Routing/native examples | `templates/framework/model-routing.toml`, `templates/codex/README.md`, `templates/codex/config.toml`, `templates/codex/agents/af-implementer.toml`, `templates/codex/agents/af-reviewer.toml` |
| Existing instruction-only skills | `templates/skills/af-model-setup/SKILL.md`, `templates/skills/af-model-reassign/SKILL.md` |

Compared with the initial captured contents, root AGENTS has 89 → 61 nonempty
lines and common Superpowers policy has 144 → 69. Policy-entry has 40 → 41,
implementer TOML 28 → 28, and reviewer TOML 30 → 28: necessary selection/storage
constraints offset some removed duplication. These counts include metadata,
headings and tables; they are not tokenizer measurements or cost-saving claims.

### Completion and remaining limits

R1–R6 and the static A1–A8 criteria are satisfied; S1–S5 library work is complete
and ready for final user review. No application, permanent test infrastructure,
installation, native/global settings change, Git write or external model call was
introduced. The templates remain inactive.

P1 is the remaining separate adoption activity, not unfinished library acceptance.
It needs an actual project, one client/version, explicit model choices where needed
and authorized configuration scope. Observe instruction loading, an inline task,
justified delegation if configured, the stage checkpoint and resumption. Record
runtime-reported model/effort only when available; unavailable telemetry is unknown.
Neither cross-client runtime compatibility nor token/time savings are established.
The dated inspection limits in the compatibility reference remain applicable.
