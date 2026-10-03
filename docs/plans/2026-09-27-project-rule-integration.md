# Project rule integration implementation plan

Date: 2026-09-27. Status: Tasks 1–4 complete; library integration delivered; target pilot not run.

**Goal:** Provide a repeatable agent-guided import of AgentsFramework into new and
existing projects, replacing conflicting old process rules while preserving local contracts.
**Architecture:** Keep MIGRATION as the procedure owner; add a thin integration skill
and a provenance/recovery record template. Reuse catalog selection, entry templates,
native mappings and verification rules. No installer or runtime service.
**Artifacts:** Markdown instructions, skill frontmatter and existing TOML catalog metadata.
**Spec:** [Project rule integration](../specs/2026-09-27-project-rule-integration.md).
Executors read both documents; requirements belong to the spec and progress belongs here.

## Global Constraints

- The user's instruction to proceed after Unreal U4 authorizes resuming library
  implementation, inline with the existing stage checkpoints. Task 1 is accepted;
  Tasks 2–3 are accepted and the latest continuation authorized Task 4, now complete;
  no target import, configuration change or live pilot is authorized by this work.
- Unreal Engine library support is complete: one profile and six conditional
  resources, reconciled common rules/templates and static acceptance. UE 5.8 is
  the researched reference, not observed target compatibility; no pilot was run.
- Reuse completed Unreal profile/catalog/entry work and its evidence. The current
  catalog has 20 profiles; preserve engine/editor-specific routing and architecture.
- The user explicitly confirmed one skill, `af-integrate-project`, on resumption.
  Preparation and application reuse the same procedure; creation belongs to Task 3.
- Workspace and implementation directory: `/home/vitalii/Documents/Local_Project/AgentsFramework`.
  This plan and its linked spec retain their canonical locations. Git is optional.
- Default execution after authorization: inline, one logical stage and a user checkpoint.
  Reuse any later explicit multi-stage authorization. No Git writes, worktrees,
  personal/global settings changes, plugin-cache patches or external model calls by default.
- Capture original contents/absence before each stage's first write. Preserve user
  changes, project gates, strict engineering constraints and native task ownership.
- Use applicable Superpowers skills through `standards/superpowers.md`. This plan's
  checkpoints and evidence rules replace stock commits, extra reviewers and ledgers.
- A routine library task without configured roles stays inline. Installing the new
  skill or enabling native roles in another project belongs to a separately scoped import.

## Dependency and checkpoints

| Item | State | Exit condition |
| --- | --- | --- |
| Existing instruction refinement and subsequent clarifications | Available foundation | Reuse current rules and applicable evidence |
| Unreal Engine support requested before integration | Library prerequisite complete; no runtime pilot | U1–U4 profile, routing/catalog changes and scoped checks complete; reuse their evidence |
| Library integration | Tasks 1–4 complete | Confirmed single skill, procedure, record and static acceptance I1–I8/A1–A10 delivered |
| Target adoption pilot | Future separate scope | Target/client and permitted operations are specified |

## Task 1: Integration and conflict contract

**Modify:** `MIGRATION.md`, `ARCHITECTURE.md`.
**Consumes:** I1–I5 and completed technology-support results.
**Produces:** One authoritative prepare/apply procedure and explicit conflict semantics.

- [x] Capture the stage baseline and confirm applicable source/target boundary rules.
- [x] Define inputs, new/existing project paths and preparation-only behavior in MIGRATION.
- [x] Define actual replacement of loaded conflicting process rules, preservation of
  local contracts/gates and treatment of material unresolved decisions.
- [x] Align authority and artifact ownership in ARCHITECTURE; preserve native client
  precedence and separate model setup and task-store ownership.
- [x] Walk through A1–A3, A5 and A9 against the resulting procedure; check affected links.
  Report the prepared contract and stop at the selected checkpoint.

## Task 2: Ownership, update and recovery

**Create:** `templates/framework/adoption-record.md`.
**Modify:** `MIGRATION.md`, `standards/catalog.toml`, `standards/catalog.md`, `ARCHITECTURE.md`.
**Consumes:** Task 1 procedure, I6–I7 and existing before-write preservation rules.
**Produces:** A concise provenance template and repeat/update/recovery contract.

- [x] Capture original paths/absence. Define the target `.agents-framework/adoption.md`
  fields from I6; keep model assignments and task progress with their existing owners.
- [x] Register the template as an available catalog asset; retain the catalog schema
  and profile IDs and make record reading conditional on import/update work.
- [x] Define last-accepted-state comparison, unchanged-import completion, ownership
  boundaries, local edits, source removals and unavailable-base handling.
- [x] Define partial-state reporting, safe recovery and resumption; choose recovery
  locations outside target instruction/skill discovery when applying to a real project.
- [x] Check A6–A8 with disposable text examples of unchanged, independently edited,
  conflicting and partially written files; no permanent test framework or client needed.
  Parse the changed catalog and verify the new asset path and reference ownership.

## Task 3: Skill and import routes

**Create:** `templates/skills/af-integrate-project/SKILL.md`.
**Modify:** `MIGRATION.md`, `ARCHITECTURE.md`, `templates/AGENTS.root.md`,
`templates/AGENTS.project.md`, `templates/policy-entry.md`, `templates/project-architecture.md`.
**Consumes:** Tasks 1–2 and I1–I7; confirmed launch preference.
**Produces:** A narrow import trigger and concrete routes into the existing procedure.

- [x] Capture the baseline. Use the skill-authoring guidance for the chosen instruction-only skill.
- [x] Trigger only on explicit framework import/update/preparation requests. Ordinary
  coding, absent routing files and simple edits must not launch integration.
- [x] Keep the skill short: resolve source/target/client/intent, read the needed
  migration sections, apply the authorized scope and report actual evidence/limits.
- [x] Define source-based use before target installation and verify references from
  each proposed installed location; do not promise unverified client discovery.
- [x] Replace the conceptual `af-migrate-project` references with the implemented
  integration entry when it exists, rather than adding a second overlapping workflow.
- [x] Make entry/passport adoption provenance point to the record and require concrete
  selected-profile paths at import time, without loading that record during ordinary work.
- [x] Check skill YAML, intended relative links and A3–A5/A9 trigger/handoff scenarios;
  retain common scope, typing, verification, model and checkpoint safeguards.

## Task 4: Library integration acceptance

**Modify:** `README.md` and this plan. Correct prior task files only for concrete findings.
**Consumes:** Tasks 1–3 and I1–I8.
**Produces:** Documented import entry and scoped library acceptance evidence.

- [x] Describe new/existing project use, preparation versus application, old-rule
  replacement, provenance, repeated import and the target-pilot boundary in README.
- [x] Check changed TOML/YAML, catalog uniqueness/dependencies/assets and affected
  Markdown links, fences and relocatable template paths with existing tools.
- [x] Walk through A1–A10 together; reuse valid results and rerun only for changed
  inputs, unreliable evidence or a concrete remaining question.
- [x] Review the scoped cumulative diff against saved baselines. Resolve in-scope
  findings; avoid unrelated profile audits or application tests.
- [x] Record actual changed paths, criteria, checks and limits here. Distinguish
  a ready library procedure from an installed skill or verified client session.

## Future target adoption

Once the library is ready, a separately scoped adoption names an actual project,
one client/version, accessible source identity, import intent and permitted target
changes. Native model choices are supplied only when setup/delegation requires them.
The integration task then owns its preparation, snapshots, application and evidence.

A bounded pilot checks actual instruction discovery, task-specific reading, retained
local checks, one justified handoff if configured, stage stopping and canonical-task
resumption. Do not extrapolate one client's result to all clients. Unavailable model
telemetry remains unknown. A library-only validation does not run this pilot implicitly.

## Verification and review focus

Use existing Python TOML/YAML parsers and temporary scoped checks where useful.
Prefer document walkthroughs for instruction semantics; disposable file comparisons
can expose overwrite/recovery mistakes. Do not introduce runtime infrastructure to
test a rules-only library. No fixed number of review passes or repeated final runs.

The material failure scenarios are: inactive entry after copying; unresolved old
rules still loaded; dropped mandatory project contracts; unconditional reading of
the bundle; setup triggered by ordinary work; local changes overwritten on update;
false success after partial writes; and duplicate canonical task/model state.
Tasks above own their acceptance checks. Independent review is conditional on a
concrete risk or user request and configured role support.

## Current handoff

- Tasks 1–4 are complete at the library level, covering I1–I8 and A1–A10. The
  procedure, single skill and record template are ready for a separately scoped
  adoption. No target was selected or modified; no native pilot was performed.
- The Unreal prerequisite is complete at the library level. The
  [research](../research/2026-09-27-unreal-engine-engineering-and-mcp.md)
  records official-source findings and version boundaries. The
  [Unreal support specification](../specs/2026-09-27-unreal-engine-support.md) is
  approved. Its [implementation plan](2026-09-27-unreal-engine-support.md) is the
  canonical record of completed U1–U4 and static acceptance A1–A15. The catalog
  now has 20 profiles, preserving the previous 19; Unreal has seven portable
  files and no new mandatory skill. Target adoption and engine/MCP execution
  remain untested. Reuse the engine/editor-specific entry and passport routes;
  do not impose backend architecture on an Unreal target.
- The user's new instruction authorizes this resumption; dependency completion
  alone did not advance the work. No target installation or live pilot is implied.
- Task 1 establishes the procedure/conflict contract. Task 2 adds the inactive
  adoption-record template and repeat/update/recovery semantics. Task 3 adds the
  inactive integration skill and reachable entry routes; Task 4 records final acceptance.

Planning artifact checks on 2026-09-27 passed: eight requirements, ten acceptance
scenarios, four implementation stages, Markdown structure and four local links.
Only these two new documents were created; all 182 existing files were unchanged.
Evidence and prior-absence baseline: `/tmp/af-integration-planning-ms9ia0gn/`.
The subsequent user clarification names Unreal Engine as the prerequisite; this
text-only dependency update changes no checked links, formats or stage structure.

Unreal research handoff: the new research document and its references from this
plan/spec passed scoped Markdown/link checks (11 local links, 36 distinct primary
source URLs) and a content review of the proposed boundaries. Baseline, diff and
check results: `/tmp/af-unreal-research-retx98jj/`. No engine or MCP runtime was
tested. This evidence note adds no new links or executable content.


## Task 1 implementation and acceptance

Baseline: `/tmp/af-integration-t1-fyeh1gvy/`; originals include existing local
contents. Changed paths: `MIGRATION.md`, `ARCHITECTURE.md`, this plan and the linked
specification. The spec adjustment removes stale pending-research/authorization
wording and points to the plan for execution state and the confirmed launch choice;
requirements I1–I8 and scenarios A1–A10 are unchanged.

Pre-flight interfaces: Task 1 produces the prepare/apply and conflict procedure;
Task 2 extends it with ownership/update/recovery and Task 3 routes the single skill
into it. Task 4 consumes those artifacts for library acceptance. The completed
Unreal entry and catalog already fit this procedure: no profile/schema change or
engine-to-backend architecture conversion is needed. No interface conflict found.

Implemented I1–I5 contract: explicit source/target/client/intent inputs, new/existing
project preparation, concrete previews, scoped replacement of actually loaded
conflicts, preservation of gates/exceptions, preparation-only no-write behavior,
before-write protection and separate file/runtime evidence. Detailed update and
recovery comparisons remain Task 2. Catalog selection, task stores and model
configuration retain their existing owners. No role, model or Git setup was needed.

| Scenario | Static walkthrough and outcome |
| --- | --- |
| A1 | A new declared Blueprint-only Unreal target selects its entry and six available resources with task-specific reading. Intended architecture is labelled proposed; no legacy remediation, mandatory C++/MCP setup or backend DI layer is introduced. |
| A2 | An existing nested entry demands full tests after every edit while CI requires a release gate. Inventory identifies both loaded sources; replacement removes the blanket trigger, preserves the actual gate and its condition, and retains business/security contracts. An inaccessible opposing rule is reported unresolved rather than masked by root-precedence prose. |
| A3 | Preparation reads current destinations and produces source/profile/path/action/content/conflict details in the response or agreed external storage. It stops without writing target files, directories, native settings or an adoption record. Existing apply authorization is reused only for an apply intent and within stage limits. |
| A5 | A repository opened independently receives reachable local entry/profile/task routes. A delegated role receives applicable policy explicitly when its discovery does not supply it; parent discovery and full conversation inheritance are not assumed. |
| A9 | Existing native task location and model assignments stay with their owners. Missing model routing does not force setup for inline import. Only separately authorized setup or necessary authorized delegation selects that procedure; source-library progress does not replace the target's canonical task. |

Verification covers these instruction decisions and the changed documents, not a
real import or client session. No permanent test framework, installed skill,
adoption-record template, target write or engine/MCP execution is part of Task 1.


Task 1 checks: PASS. A scoped Python/pathlib check resolved 44 local links and
fragments across the four changed documents and checked balanced Markdown fences.
It confirmed that I1–I8/A1–A10 and the Task 2–4 definitions are unchanged. The five
static walkthroughs above and review of the baseline diff found no unresolved
in-scope issue. One wording correction during review replaced a compulsory installed
client with available version evidence, consistent with preparation without a
client; it changes no links or formats and was reviewed inline.

Evidence: `checks.json` and `changes.diff` under the stage baseline directory.
Final checklist/status reporting adds no new links or executable structure;
the diff was refreshed without repeating valid checks. The catalog and templates
were unchanged, so their Unreal-stage checks were not rerun. Next: Task 2, preserving
this procedure as the owner; Task 3 will implement the confirmed single skill.


## Task 2 implementation and acceptance

Baseline: `/tmp/af-integration-t2-od2xjd11/`. New:
`templates/framework/adoption-record.md`. Modified: `MIGRATION.md`,
`ARCHITECTURE.md`, `standards/catalog.toml`, `standards/catalog.md`, this plan.

The template owns source/target/client identity, managed paths/portions, accepted
adapted contents and exceptions, recovery references and scoped agreement state.
It remains inactive; preparation keeps a proposed record outside the target.
Progress/model assignments retain their existing owners. The catalog adds one
available asset, with conditional reading and no new profile or schema.

MIGRATION owns comparison of accepted base, current target and adapted candidate,
source-removal decisions and missing-base limits. Partial operations preserve the
last accepted state, identify actual path outcomes and restore only changes whose
written result still matches; newer user work is reconciled rather than discarded.
ARCHITECTURE routes to these owners and removes its previous competing claim that
the entry/passport owns revision history. Entry-template provenance routes belong
to Task 3. No automatic importer or permanent test suite is introduced.


Task 2 checks: PASS. `python3 /tmp/af-integration-t2-od2xjd11/check.py` parsed
schema-1 TOML and confirmed all 20 profile definitions and all other catalog
metadata unchanged; exactly one shared asset was added. It resolved 46 local
links/fragments and checked Markdown fences across changed documents. The record
has no source-relative links that would break at its target location; filled
references must identify their target/source/external root as its guidance states.

| Scenario | Disposable evidence and instruction decision |
| --- | --- |
| A6 | Matching accepted/current/candidate text needed no write; unchanged selection and valid prior evidence remain prerequisites. A separate static incomplete-state walkthrough retains outstanding checks despite byte equality. |
| A7 | `diff3 -m` produced an external preview for independent source/local edits, preserving a required check; overlapping edits returned a conflict without modifying current content. A removed base left differing hashes insufficient for a merge. Removing the candidate did not delete the edited target. |
| A8 | A user edit after preparation changed the captured identity and prevented dependent replacement. Simulated partial recovery restored a matching operation write and removed a matching new file, while preserving newer user edits and an untouched file; the unresolved path stayed explicit. |

Eight documented cases comprise seven disposable file comparisons/recovery
examples and one static incomplete-state walkthrough. These validate the contract's
choices, not an implemented importer or client behavior. The temporary script and
`examples/`, `scenarios.json`, `checks.json` and scoped `changes.diff` are retained
under the baseline directory. No permanent runtime/test infrastructure was added.

Scoped review covered all six changed paths against their pre-stage contents and
found no unresolved in-scope issue. Task 1's preparation/conflict contract remains
in place; unchanged profile checks were reused. Final progress/checklist edits add
no new links or formats, so only the saved diff was refreshed. Stop at the agreed
checkpoint; Task 3 will add the skill and update entry/passport provenance routes.


## Task 3 implementation and acceptance

Baseline: `/tmp/af-integration-t3-mgiqn6vx/`. New:
`templates/skills/af-integrate-project/SKILL.md`. Modified: `MIGRATION.md`,
`ARCHITECTURE.md`, `templates/AGENTS.root.md`, `templates/AGENTS.project.md`,
`templates/policy-entry.md`, `templates/project-architecture.md`, this plan.
The passport is included to satisfy this stage's explicit provenance/route step;
its omission from the original Modify list was a file-list gap, now reconciled.

Used Superpowers writing-skills and the local skill-creator guidance with the
framework's proportionate verification adaptations. The existing plan/spec and
confirmed single entry govern scope; no new design questionnaire, model setup,
subagent campaign, global installation, Git action or UI metadata is needed.

The skill has a narrow explicit preparation/import/update trigger and routes to
MIGRATION's existing procedure by operation. At its source location it resolves
the source root; the proposed installed layout instead resolves the source from
the request or adoption record. Source-based reading works before installation;
unavailable source access blocks dependent work without inventing policy. This
replaces the conceptual migration entry in active architecture/migration docs.
Entry and passport templates now require actual profile/skill paths and point to
adoption provenance only for import/update/recovery. Local operational contracts,
typing, sufficient checks, native task ownership and model choices remain binding.

Supported packaging claim: reference resolution for the source template and the
proposed target `.agents/skills/af-integrate-project/SKILL.md` layout. Other client
installation paths require verified native mapping; source-based use remains
available. No native discovery, model adherence or runtime activation is claimed.


Task 3 checks: PASS. The installed skill-creator `quick_validate.py` returned
`Skill is valid!` for the new folder. The skill is 50 lines / 410 whitespace-delimited
words, with only name/description frontmatter and no ancillary runtime files.
`python3 /tmp/af-integration-t3-mgiqn6vx/check.py` checked 57 local links/fragments,
Markdown fences, frontmatter and the passport's TOML example. Policy-entry links
were resolved from the adopted root as intended. No author-machine path or unfinished
skill scaffold remains. Active MIGRATION/ARCHITECTURE no longer reference the
conceptual `af-migrate-project`; historical specifications remain historical.

Disposable location checks copied the skill and directly selected source resources
outside the workspace. They resolved the source-template root, an installed skill's
record-supplied source, request-supplied source before a record exists, and concrete
skill/profile entry paths in an independent target. The target deliberately lacked
MIGRATION/catalog: lookup used the identified source. Missing source was represented
as unavailable, without fallback to unrelated target files. These checks establish
path mechanics, not native skill discovery or a fully deployed target bundle.

| Scenario | Static trigger/route walkthrough |
| --- | --- |
| A3 | An explicit preparation request selects the skill, resolves accessible source/target/client/intent and reads the prepare procedure. Proposed records/content stay outside the target; an existing apply permission does not turn a preparation-only request into application. |
| A4 | Python-only and JavaScript React imports follow catalog applicability and filled concrete profile routes; unused FastAPI/Pydantic, TypeScript and Next.js requirements remain conditional. No unconditional dependency-reading queue is added. |
| A5 | Source-based use needs no installed target skill. Installed use locates the source independently of the target; local routes must work when the repository opens alone. Delegated roles still receive applicable policy under the existing orchestration contract. |
| A9 | Saved task stores and model choices are reused. Import does not request new model assignments, create a competing task record or trigger delegation merely because configuration is absent. |
| Negative triggers | A code fix, general project audit, missing AGENTS and missing model routing alone do not select integration. Explicit framework preparation/import/update does. These are instruction walkthroughs, not observed model activation. |

Scoped review covered all eight changed paths against their originals and found no
unresolved in-scope issue. Shared engineering/checkpoint safeguards are retained;
prior adoption comparison/recovery examples and catalog checks remain applicable.
The baseline directory retains `checks.json`, location fixtures, the temporary
checker and `changes.diff`. Final status/checklist/evidence text adds no new links
or formats; only the saved diff was refreshed. Task 4 remains pending the agreed
checkpoint. No target client, global skill, external model or real import was run.


## Task 4 library acceptance

Baseline: `/tmp/af-integration-t4-z4nvbxyx/`. Changed: `README.md` and this plan.
README now describes the implemented entry, source-based use before installation,
new/existing projects, preparation versus application, actual conflict replacement,
provenance, repeated imports, partial recovery and the target-pilot boundary.

### Requirements and scenarios

| Requirements | Delivered owners |
| --- | --- |
| I1 | Explicit skill trigger, source/target/client/intent resolution and import boundaries: Tasks 1/3 |
| I2–I3 | New/existing project procedure and replacement of actually loaded conflicting rules while preserving gates/contracts: Task 1 |
| I4 | Existing catalog applicability and portable bundle, concrete profile/skill routes and independent project entry: Tasks 1/3 |
| I5 | Reviewable preparation, intent/authorization, originals and intervening edits: Task 1 |
| I6–I7 | Adoption record, accepted-state comparison, managed portions, partial-state recovery: Task 2 |
| I8 | Proportionate checks and scoped file/runtime evidence: Tasks 1–4 |

| Scenario | Acceptance evidence and result |
| --- | --- |
| A1 | Task 1 new-project walkthrough plus Task 3 concrete routes: declared stack and intended architecture, no invented legacy remediation. |
| A2 | Task 1 conflict walkthrough: replace blanket reruns in loaded sources; preserve real gates, product/security contracts and scoped exceptions. An uncontrolled conflict stays explicit. |
| A3 | Tasks 1/3 preparation walkthroughs plus README example: concrete external preview, no target write; an apply permission does not change preparation-only intent. |
| A4 | Task 3 Python-only/JavaScript React walkthrough and retained catalog rules: only used components impose obligations; dependencies provide availability. |
| A5 | Tasks 1/3 independent-entry walkthrough and relocated path examples: local profile/task routes and explicitly resolved source, with applicable policy passed to roles that omit discovery. |
| A6 | Task 2 unchanged/incomplete-state examples: matching import needs no rewrite or repeated valid check; partial/unverified evidence remains pending. |
| A7 | Task 2 independent/conflicting edit, missing-base and source-removal examples: preserve target work, expose conflict/removal decisions; hashes do not reconstruct missing bases. |
| A8 | Task 2 intervening-edit and partial-recovery examples: compare actual written state, protect newer work and leave unresolved paths explicit. |
| A9 | Tasks 1/3 ownership walkthroughs: existing native tasks/model choices persist, ordinary import triggers no setup or competing progress store. |
| A10 | All stage evidence and README: file formats, references and instruction decisions are checked; no real client discovery, adherence or model activation was observed. |

This mapping reuses valid prior results. It is static library acceptance, including
disposable file examples, not observation of a target agent executing all scenarios.
README introduces no new application or configuration behavior. The integrated
reading path is request/entry → skill → relevant MIGRATION sections → selected
catalog/template resources; an update additionally reads target provenance/current
files. Source lookup and target lookup remain distinct, and record availability
never turns ordinary work into an import.

### Cumulative scope and limits

Tasks 1–4 change 13 distinct paths: two new templates and eleven modified files.
New: `templates/framework/adoption-record.md`,
`templates/skills/af-integrate-project/SKILL.md`.
Modified: `MIGRATION.md`, `ARCHITECTURE.md`, `standards/catalog.toml`,
`standards/catalog.md`, `templates/AGENTS.root.md`, `templates/AGENTS.project.md`,
`templates/policy-entry.md`, `templates/project-architecture.md`, `README.md`,
`docs/specs/2026-09-27-project-rule-integration.md` and this plan.

The catalog retains schema 1 and all 20 profiles; one available record template
was added. The procedure/skill/templates are delivered, not installed into a real
target. No importer application, external model invocation, global configuration
change, Git write or native pilot was performed. Actual target/client discovery,
conditional reading, checkpoint behavior and resumption remain pilot observations.


### Final verification and handoff

PASS: `python3 /tmp/af-integration-t4-z4nvbxyx/check.py` checked 53 local
links/fragments and balanced Markdown fences in the two Task 4 documents.
It matched all eleven prior delivered artifacts against their latest reviewed
stage diffs, establishing that their format, catalog and reference evidence remains
applicable. The cumulative baseline inventory confirms 13 paths, with two new
files and eleven modified. Prior checks were reused without repeating validators,
profile audits, merge examples or relocation exercises.

Scoped review of the new documentation and the combined entry/procedure/record
contracts found no unresolved in-scope issue. README's unchanged-import summary
was qualified during review to retain pending checks from partial work; this is
consistent with A6/A8 and introduces no links or format changes. The temporary
checker, `checks.json`, scoped `changes.diff` and cumulative `cumulative.diff` are
retained under the Task 4 baseline. Completion/report-only edits were recorded by
refreshing diffs, without another verification cycle.

Library work is complete. A future adoption needs an accessible source, actual
target roots, one client/version, prepare/import/update intent and permitted scope.
A live pilot is separately scoped and reports observed discovery/adherence and
remaining limits. Saved rules, a valid skill and static scenario acceptance do not
establish those runtime observations or cross-client compatibility.
