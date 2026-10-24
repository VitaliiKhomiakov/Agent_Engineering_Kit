# Adoption resource lifecycle implementation plan

> For execution, use Superpowers `executing-plans` with the repository's
> [local adaptations](../../standards/superpowers.md). Delegated implementation is
> a separate choice, not a requirement of this plan. Stable checkboxes below own progress.

**Goal:** Keep persistent development agents and selected native skills while
excluding their installation-only source templates from adopted projects.

**Architecture:** Retain one shared body per role and thin native adapters.
Separate bundle resources from source preparation resources in the existing
catalog and checker; native installation remains an instruction-guided migration.

**Tech stack:** English Markdown, TOML schema 1, Python 3.11+ standard library,
existing `unittest` fixtures and documented strict type checks.

**Spec:** [Adoption resource lifecycle](../specs/2026-10-24-adoption-resource-lifecycle.md).
The specification owns design and acceptance criteria; this document owns progress.

## Status, workspace, and authorization

- Status: implementation and correction completed; accepted for commit and push
  by the user on 2026-10-24.
- Current item: none; I1–I3, V1 and follow-up correction R1 are complete.
- Authorized scope: source implementation of I1–I3 and V1 in this checkout.
  Architect, implementer, and reviewer remain persistent development agents.
- Execution mode: current checkout, direct work with the existing human checkpoint.
  Git writes were excluded during implementation and correction. The user has now
  explicitly authorized staging, committing, and pushing the completed changes
  from `main` to `origin/main`. Consumer updates and client configuration changes
  remain outside this task.
- Instruction/workspace root and execution checkout:
  `/home/vitalii/Documents/Local_Projects/Agent_Engineering_Kit`.
- Canonical artifacts: `docs/specs/2026-10-24-adoption-resource-lifecycle.md` and
  this `docs/plans/2026-10-24-adoption-resource-lifecycle.md`; the coordinator owns
  this checklist. There is no separate native task store or worktree copy.
- Baseline: clean `main` at `66f139f2ddeecfdc684097a7bf59a3f7b73fc300`;
  both new documents were absent. Pre-edit record:
  `/tmp/aek-adoption-lifecycle-preedit-7u4y6avm/baseline.json`.
- Implementation baseline: tracked paths still match that commit; the accepted
  untracked specification/plan are separately preserved in
  `/tmp/aek-adoption-lifecycle-implementation-5n9jnp7c/baseline.json`.
- Model routing: no workspace `.agents-framework/model-routing.toml` is present.
  Implementation uses the current session inline; it creates no saved model choices.
- Next checkpoint: report the requested commit and push outcome.

## Global constraints

- Keep architect, implementer, and reviewer as persistent development roles; install the selected client's enabled native definitions and retain their required local bodies.
- Preserve saved client, role enablement, model/effort pairs, delegation edges, and single-agent mode; cleanup does not change those choices.
- Keep one authoritative procedure per role and thin client adapters; do not introduce a generator, installer service, plugin, or self-deletion hook.
- Ordinary development and review must work without the source AEK checkout or author-machine absolute paths.
- Preserve catalog schema version 1, profile IDs, Python 3.11+ standard-library tooling, and existing contained, flat, and custom layouts.
- Preserve unrelated files, local customizations, historical evidence, and explicit persistent installations; source reclassification alone authorizes no consumer deletion.
- Do not change native model settings, permission semantics, technology examples, or Superpowers plugin contents in this task.

## Progress

- [x] D1 — Record the agreed lifecycle and persistent-role requirements in the specification.
- [x] D2 — Complete and self-review this plan; validate both documents and report the checkpoint.
- [x] I1 — Implement catalog lifecycle selection and its focused regression coverage.
- [x] I2 — Integrate lean bundles with native agents/skills and portable references.
- [x] I3 — Define and verify safe updates of existing adoptions.
- [x] V1 — Complete implementation-boundary checks and accountable review.

Stage D is the completed, authorized documentation stage. I1–I3 and V1 form one
coherent implementation stage: its interdependent catalog, adoption, and
fixture changes reach the user checkpoint together. Item completion is not an
additional permission gate or a reason to repeat unchanged checks.

## Review focus

| Failure condition | Expected behavior | Owner |
| --- | --- | --- |
| A shared role body is mistaken for a disposable template | Keep the local body and reject its absence for an active role | I2 / AC1, AC5 |
| Source-validation output is reused as the import copy list | Separate inventories exclude preparation inputs without disabling source checks | I1 / AC2, AC3 |
| Missing runtime links are relabelled as optional source references | Only declared preparation/optional evidence routes may be omitted | I2 / AC4, AC5 |
| A prior inactive copy has local changes, or a setup skill was explicitly installed | Preserve it pending the existing ownership/reconciliation decision | I3 / AC6 |
| A repeat update or client choice recreates unused adapters or removes a live role | Preserve selected native roles, deliberate absence, and unrelated files | I2–I3 / AC1, AC6 |

## I1 — catalog selection and validation

**Files:** `standards/catalog.toml`, `standards/catalog.md`,
`tools/check_instruction_artifacts.py`, `tests/test_instruction_artifacts.py`,
`tests/test_profile_selection.py`.

**Interface:** Extend `Profile` with `source_resources: tuple[str, ...]`, defaulting
to an empty catalog array. Introduce a frozen `CatalogSelection` with
`bundle_files: frozenset[Path]` and `source_files: frozenset[Path]`, returned by
`Checker.catalog_selection(selected: Sequence[str]) -> CatalogSelection`.
The implementation also retains `entry_templates: frozenset[Path]` as metadata
for optional legacy entry validation, avoiding a second catalog parse.
Keep `Checker.catalog_files(selected: Sequence[str]) -> set[Path]` as the existing
validation entry point over that single parse/traversal. Source mode validates
both sets; bundle mode requires only runtime files, with existing checks for
present optional legacy named entry templates. New copy preparation uses
`catalog_selection(...).bundle_files` explicitly. Preserve diagnostic formatting
and existing CLI options; do not add an installer or a second catalog parser.
Keep the existing mode selection: CLI `--profile` selects target/bundle validation;
source validation uses the source mode. Source resource declarations must not
become target existence requirements, including for a flat bundle.

**Work and acceptance: AC2, AC3.**

1. Add focused cases for valid source-only declarations, malformed types, escaping
   paths, a selected path classified both ways, missing source input, absent target
   source input, and missing target runtime input. Add a legacy catalog without
   the new field and prove its declared resources remain required.
2. Establish the new behavior's failing cases before changing selection. Use the
   smallest focused test invocation; no baseline rerun of unrelated stack tests.
3. Implement the optional schema-1 field and separate inventories. Source mode must
   retain source-path/existence validation even when a caller requests a copy list;
   bundle mode must not require omitted preparation inputs. Deduplicate same-category
   paths and preserve selected-profile closure and existing diagnostic behavior.
4. Reclassify the nine client role templates, Codex setup guide/config example,
   routing example, and setup/reassignment skill entries under `source_resources`.
   Keep the three shared role bodies and composition README as runtime resources.
   Move the two optional project-task skill templates to their profile's source
   resources. Named catalog entry templates remain preparation inputs outside the
   default bundle copy set. Other shared assets retain their current classification.
5. Update the catalog contract and selection assertions to distinguish source
   inventory from bundle inventory. Preserve all technology profile/aggregate
   selections. Run the focused catalog cases and record the covered state.

Use descriptive regression names such as
`test_source_resources_missing_in_source_fail`,
`test_source_resources_absent_in_target_pass`,
`test_source_resources_do_not_hide_missing_runtime_files`,
`test_source_resources_invalid_declarations_fail`, and
`test_legacy_catalog_resources_remain_required`. The invalid-declaration case
covers the distinct type, boundary, and classification failures above. Run the
new cases with the existing unittest runner, then the affected selection module;
success means zero failures/errors and the intended diagnostics in negative cases.

**Produces:** A single validated selection contract for I2; source templates remain
checked and available in AEK while adoption copy lists omit them.

## I2 — portable adoption with persistent roles

**Files:** `MIGRATION.md`, `standards/model-configuration.md`,
`standards/project-skills.md`, `templates/agents/README.md`,
`templates/codex/README.md`, `templates/framework/adoption-record.md`,
`templates/skills/{aek-integrate-project,aek-model-setup,aek-model-reassign,aek-design-feature,aek-review-changes}/SKILL.md`,
`ARCHITECTURE.md`, `tests/test_project_skill_adoption.py`,
`tests/test_project_skill_portability.py`, `tests/test_agent_templates.py`.
Inspect entry templates for affected installation wording; change only actual
contradictions, not unrelated policies.

**Consumes:** I1's `CatalogSelection`. Existing `prepare_design_fixture(...)`,
`portable_candidate(...)`, `adapt_document(...)`, and `body_route(...)` remain
fixture helpers, not production installers. Reuse the selected source inventory
to classify optional preparation references; do not introduce a path-prefix
exemption that hides missing runtime files.

**Work and acceptance: AC1, AC2, AC4, AC5, AC7.**

1. Change fixture copy selection to the bundle inventory. Continue reading selected
   native adapters/skills directly from source to create final native entries.
   Remove the fixture's unconditional `CLAUDE.md` creation for non-Claude cases;
   keep separately labelled compatibility/syntax cases where they are actually tested.
2. Preserve all three enabled agents and their saved pairs. Assert the exact native
   role set for Codex, Claude Code, and Cursor; no other client's new active
   definitions and no inactive adapter copies. Retain disabled-role and zero-role
   cases without changing enablement defaults or installing an orchestrator file.
3. Keep shared-body paths unchanged. Cover contained `.agents-framework`, flat `.`,
   custom `rules/aek`, and independently opened roots. Existing missing/wrong/stale
   body cases must continue failing for the same runtime reason.
4. Install optional task skills only at their selected native paths. Update tests
   that currently require inactive bundled skill copies. Cover no task skills,
   review-only, both task skills, and explicitly persistent setup; no setup-only
   native directory is created by default. Keep native task-skill cases scoped to
   Codex's verified mapping; other-client role fixtures must not imply that Codex
   skill paths install skills for those clients. Preserve guide-link and metadata checks.
5. Rebase native and document references under MIGRATION. Label omitted preparation
   examples through source provenance while keeping required policy/body/skill-guide
   links local. Update the record mapping from an expected inactive bundle path to
   source template identity plus native destination and existing managed evidence.
6. Update architecture and composition documentation to distinguish retained
   operational role bodies from source-only templates. Keep detailed lifecycle
   rules in catalog/MIGRATION owners and route other entries there.

**Produces:** Source-independent prepared targets with persistent development roles,
selected native skills, and no installation-template duplicates in the changed scope.

## I3 — existing adoption reconciliation

**Files:** Relevant repeat/update and recovery sections of `MIGRATION.md`,
`templates/framework/adoption-record.md`, `docs/maintenance/verification.md`,
and existing adoption/portability fixtures where a fixed scenario is appropriate.

**Consumes:** I2's new candidate layout and existing base/current/new ownership
contract. There is no automated installer or reconciler to extend; do not invent
one or test a fictional production deletion API.

**Work and acceptance: AC6, AC7.**

1. Document the proposed retirement of proven managed, unchanged inactive copies
   separately from continued native agents and shared bodies. Apply the existing
   ownership comparison, recoverable baseline, and accepted exception mechanisms.
2. Walk fixed cases for an unchanged managed copy, a locally customized copy,
   an unowned same-name file, an explicitly retained setup skill, and an interrupted
   update. Record expected retain/retire/conflict outcomes in the maintenance
   reproduction procedure; preparation leaves target bytes untouched.
3. Extend existing preparation/repeat fixtures only for behavior their helpers
   actually implement: source template omission, unchanged target snapshots,
   stable candidate output, and retained native/body references. Document ownership
   reconciliation as a procedure walkthrough, not an executed installer guarantee.
4. Preserve old evidence as historical. Record the new source revision/check scope;
   do not rewrite previous runs as if they covered this lifecycle change.

**Produces:** A reviewable update procedure and bounded evidence that inactive-copy
retirement cannot be mistaken for deleting persistent development agents.

## V1 — implementation verification and handoff

At the coherent implementation boundary, run the existing six-module suite once:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests
python3 tools/check_instruction_artifacts.py
```

The shared checker changes justify the complete repository test suite. Reuse valid
focused results; after a correction rerun affected tests and required gates only.
Explicitly check edited `docs/` files, which the default artifact scan does not
cover, including `docs/maintenance/verification.md` and these planning documents.
Run the documented strict mypy check in
[maintenance verification](../maintenance/verification.md) for the changed checker
and affected tests, using the documented Python target and installed tool version.
Record unavailable evidence rather than changing system tooling or reporting a pass.

Inspect the actual diff and new files, run `git diff --check`, and review AC1–AC7
against their owning items. Native activation is reported only if actually observed
in a separately authorized target; static fixtures do not launch clients or prove
permissions. No live consumer is needed to validate the source change's static contract.
Report a concrete limitation if runtime evidence remains unavailable.

At handoff update item markers, source state, checks, and remaining limitations in
this plan. Stop for the implementation-stage user review under the existing work
mode. Do not stage, commit, or begin a consumer migration as a completion ritual.

## Documentation-stage evidence

Recorded on 2026-10-24 against the stated source baseline plus these two new
documents:

- Explicit artifact/link check of both documents: 2 artifacts, 0 errors.
- Self-review maps AC1–AC7 to I1–I3/V1 and preserves all three development roles.
  It distinguishes source/target validation, Codex-only verified native task-skill
  mapping, and procedure walkthroughs from an automated installer guarantee.
- The specification and plan's Global constraints sections match exactly.
- `git diff --check` found no tracked whitespace errors. Separate new-file
  `git diff --no-index --check` inspections reported no whitespace diagnostics;
  exit 1 is expected for new files compared with `/dev/null`.
- Only the two requested planning documents are new; tracked implementation files
  are unchanged. No implementation tests or client execution are claimed for stage D.

The user subsequently authorized I1–I3/V1. Stage D's evidence remains historical;
implementation evidence is recorded below.

## Implementation progress and decisions

- Pre-flight: I1 supplies the two inventories consumed by I2's fixture preparation;
  I3 uses that candidate and the existing ownership procedure. No ownership or
  lifecycle conflict was found. The canonical plan replaces stock skill ledgers,
  worktree setup, per-task commits, and automatic review cycles under local policy.
- I1 complete: six new catalog regressions pass, with the new rejection cases
  observed failing first (15 subcase failures before implementation). Two real
  selection regressions failed before resource reclassification and now pass.
  Artifact/selection modules: 94 tests passed in 20.599 seconds; evidence in
  `/tmp/aek-adoption-lifecycle-implementation-5n9jnp7c/catalog-green.log`.
- Implementation detail: `CatalogSelection.entry_templates` preserves optional
  legacy entry checks within the single parser/selection flow. A legacy named
  template also explicitly declared as a runtime resource keeps its requirement.
- I2 complete: the fixture regressions reproduced 12 failures for unwanted
  inactive copies and the missing explicitly selected setup entry before changes.
  The four focused cases passed after implementation. A separate task-skill case
  first reproduced acceptance of a missing workflow guide; the fixture now rejects
  that selection before creating the target. Full-suite evidence below covers
  native roles, layout rebasing, disabled roles, and required runtime references.
- I3 complete: the fixed-case walkthrough in maintenance verification was executed
  against a disposable Codex target. Only the proven owned, unchanged inactive
  adapter was retired. Modified and unowned copies, the explicitly installed setup
  skill, and all three native roles and their bodies were retained. Preparation and
  repeated preparation preserved target contents and modification times. Scoped
  recovery restored the interrupted retirement exactly before repeating it.
  Evidence: `/tmp/aek-retirement-walkthrough-_10ks02i/evidence.json`; target artifact
  check: 43 artifacts, 0 errors; explicit native roles plus setup skill: 4 artifacts,
  0 errors. This was a manual file-state walkthrough, not execution of an installer.

## Implementation-boundary evidence

Recorded on 2026-10-24 against baseline `66f139f` plus the current uncommitted
implementation and these planning documents:

- `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests`: 136 tests
  passed in 46.283 seconds. Log:
  `/tmp/aek-adoption-lifecycle-implementation-5n9jnp7c/full-suite.log`.
- Default artifact checker: 233 artifacts, 0 errors. Explicit checks of maintenance
  verification, the specification, and this plan: 3 artifacts, 0 errors.
- Documented strict mypy 2.1.0 check: no issues in eight source files, using Python
  target 3.11 and the existing temporary environment. No system tooling changed.
- Diff inspection found one catalog parser/selection flow, explicit copy-list
  consumers, and narrow source-reference adaptation. Native adapter definitions
  and shared role bodies themselves remain unchanged. `git diff --check` passed;
  separate new-file whitespace checks reported no diagnostics.
- Independent read-only review completed with `/root/review_adoption_lifecycle`,
  a direct child inheriting the user-selected current session model/effort without
  configuration changes. It covered the tracked diff, both new planning documents,
  AC1–AC7, and the review questions above. No critical, important, minor, or plan
  defects were identified. Responsibility placement and scoped readability passed:
  the checker owns one catalog parser/traversal, rendering remains test-only, and
  MIGRATION owns reconciliation. No checks were unnecessarily repeated or writes
  delegated. The reviewer is finished; the coordinator accepts the result.
- Evidence limits: static fixtures and the bounded update walkthrough do not prove
  native client discovery, permission enforcement, or execution by a selected
  model. No live consumer project was changed or client launched in this stage.
  The reviewer set aside native runtime claims and automated reconciliation
  guarantees for these reasons; the coordinator accepts both scope limits.

## Follow-up review correction

- [x] R1 — Reconcile the entry-template table with source-only preparation and
  verify the corrected procedure.

The user requested another independent review and then authorized its correction
on 2026-10-24. Reviewer `/root/review_adoption_usage` found one important issue:
MIGRATION's entry-template table still said `policy-entry.md` was bundled, contrary
to the new named-template lifecycle. The coordinator verified the finding against
the catalog contract. Existing fixture and checker success could not establish
prose consistency because present legacy entry templates remain valid.

This correction changes only that table and adjacent guidance, plus this progress
record. It distinguishes source preparation, adapted active outputs and explicitly
selected or retained inactive copies, preserving the existing reconciliation owner.
Pre-correction copies, including prior uncommitted edits, are preserved in
`/tmp/aek-entry-template-review-fix-ojsbwbai/baseline.json`.

R1 is closed after coordinator review of the scoped correction against the catalog
contract and the independent finding. The table now excludes source templates by
default, active outputs remain managed, and explicit inactive copies retain their
ownership/recovery rules and validation coverage. No further inconsistency was
found in the corrected section and its affected routes.

Verification: explicit artifact/link checks of MIGRATION and this plan passed
(2 artifacts, 0 errors). `git diff --check` and the separate untracked-plan
whitespace check reported no diagnostics. Existing code tests and static portability
evidence remain applicable; no code, native files, consumer projects or Git state
changed in this correction.
