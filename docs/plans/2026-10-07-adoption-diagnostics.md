# Read-only adoption diagnostics development plan

> Use Superpowers with [local adaptations](../../standards/superpowers.md).
> Execute selected stages inline with `executing-plans`. Use the relevant skill
> authoring procedure only if the optional wrapper stage is actually selected.

**Goal:** Resolve a concrete adoption/setup uncertainty without changing the
target, and create reusable support only when actual reuse justifies it.
**Spec:** [Adoption diagnostics](../specs/2026-10-07-adoption-diagnostics.md).
**Architecture:** Existing authoritative procedures and checker, a scoped human-
readable report, optionally a source-owned procedure and a thin inactive skill.
**Stack:** Markdown; existing Python 3.11+ standard-library artifact checker.
**Status:** Updated 2026-10-08. AEK_TEST is available as a future diagnostic
substrate; no specific diagnosis or feature implementation is selected.
Every execution item remains unstarted.

## Global Constraints

- Preserve the rules-library scope; no diagnostic application, CLI, daemon, MCP server, new database or automatic repair.
- Diagnosis is explicitly selected and read-only for the target; ordinary coding and missing optional files do not trigger it.
- Reuse MIGRATION, catalog, verification, policy and model owners; diagnosis does not define new precedence, merge or setup rules.
- Separate inspected files, documented client behavior and observed runtime behavior; unknown evidence is not a confirmed defect.
- Preserve flat, contained and custom layouts, local exceptions, existing task stores and saved model choices.
- Keep reports in the response or an explicitly selected canonical location; do not create target records, hashes or caches as a diagnostic side effect.

## Ownership and authorization

- Source workspace/instruction root and current checkout:
  `/home/vitalii/Documents/Local_Projects/Agent_Engineering_Kit`.
- This plan owns the diagnostic workstream and source-support progress. A selected
  existing target task owns private observations and any later repair; link it
  without copying its detailed checklist or private contents.
- [Roadmap](2026-10-07-development-roadmap.md) owns prioritization and the current
  documentation-only stage. Preparing this plan does not approve its implementation.
- The owner supplied `/home/vitalii/Documents/Local_Projects/AEK_TEST` for setup
  and tests. The pilot plan owns its scheduled provisioning. A bounded synthetic
  diagnostic may reuse it; a real adoption uncertainty or recurring need is still
  required before claiming user value or promoting reusable support.
- The current continuation schedules sandbox work and updates documentation.
  Later fixture setup reuses the sandbox grant; diagnosis itself remains read-only.
  No new feature, model batch, native activation, plugin edit, delegation or Git
  write is authorized merely by availability of a test directory.
- Before future source edits capture affected originals/prior absence and relevant
  local changes. Before authorized read-only diagnosis record enough target state
  externally to substantiate preservation; do not write a baseline into the target.
- Use existing model/effort choices inline. An absent or deferred selection does
  not trigger model setup merely to run this diagnostic.

**Current item:** DIA-01 — planned, awaiting a diagnostic need and scope.
**Next checkpoint:** Review this proposal. Proceed only when there is a concrete
question or the bounded synthetic exercise is selected; absence of a real need
is a valid reason to leave feature stages deferred.

## Review focus

- Optional or legacy absence is easily mistaken for broken adoption.
- Native discovery expectations and runtime evidence are different claims.
- Local exceptions and adapted contents must survive drift inspection.
- A copied skill cannot assume it lives beside the full AEK source.
- A general audit or ordinary task must not launch integration, setup or repair.

## Stage A — Manual diagnosis before a reusable feature

**Optional sandbox prerequisite:** Reuse the verified fixture only after
[pilot stage S](2026-10-07-agent-behavior-pilot.md#stage-s--final-preparation-provision-aek_test).
For a selected synthetic exercise, prepare the healthy and broken-route copies
named in the spec; record the one deliberate mutation before diagnosis and store
preservation evidence outside each target. Use the existing source checker with
each resolved copy root, contained bundle and selected profiles. No application
server, package installation, new diagnostic runtime or wrapper is required.
Keep setup writes separate from the read-only inspection boundary.

**Files:** Read only the selected target entries, relevant adoption/managed files
and necessary source owners. Report in chat or the explicitly selected canonical
location. No new source implementation files are required.
**Consumes:** Diagnostic question, one target/client, verified layout/profile facts.
**Produces:** The spec's evidence-backed findings, limits and smallest next action.

- [ ] **DIA-01:** Establish the actual question and scope. Resolve roots, client,
  bundle and relevant ownership using available evidence. Capture preservation
  evidence outside the target and identify missing inputs without automatic setup.
- [ ] **DIA-02:** Perform the bounded inspection and compatible artifact checks.
  Cite file/section or native evidence for material findings; distinguish potential
  conflicts, accepted exceptions and unsupported observations.
- [ ] **DIA-03:** Review the report and target preservation. Decide whether the
  direct existing procedure was sufficient, a reusable procedure is useful, or
  repeated invocation warrants an eventual wrapper. Record the reuse rationale.
  A synthetic defect is capability evidence only; it does not establish real
  recurrence or satisfy the feature-investment gate.

**Checks:** Cover applicable DIA-AC01 through DIA-AC08 and DIA-AC11. Use the existing
checker command only after explicit root, bundle and profile resolution. Supply
non-catalog installed entries explicitly if they are in scope; preserve existing
containment rules. Before/after evidence must show no target changes attributable
to the diagnosis. Concurrent unrelated changes must be reported, not undone.

**Exit:** A useful report or precise evidence limitation. A one-off result can end
this workstream. No recurring need means defer stages B/C, satisfying DIA-AC12.

## Stage B — Promote a small reusable diagnostic procedure

**Entry gate:** Stage A or existing equivalent evidence demonstrates value in a
repeatable procedure. The owner selects this source-library change.
**Files:** Create `docs/maintenance/adoption-diagnostics.md`; modify a short
conditional route in `README.md` and the relevant source-maintenance/adoption
description in `ARCHITECTURE.md`. Do not change catalog schema, core policy,
model configuration, accepted-record format or checker behavior.
**Consumes:** Reviewed inspection/report practice and existing policy owners.
**Produces:** One operational procedure; the specification remains design history.

- [ ] **DIA-04:** Write the bounded inputs, source/path resolution, inspection
  sequence and report fields. Link authoritative owners for policy, B/C/N updates,
  verification and setup instead of duplicating their full requirements.
- [ ] **DIA-05:** Add conditional source navigation and document the difference
  between inspection, expected discovery and observed client behavior. State the
  no-target-write boundary and the no-automatic-trigger rule.
- [ ] **DIA-06:** Review concrete healthy, defective and ambiguous examples against
  the acceptance table. Validate new/changed links and format. Record which cases
  were source inspections versus actually executed diagnostic observations.

**Scenario coverage:** A healthy bundle with no override; one broken route; an
invalid override; absent accepted base; accepted local exception; flat/custom or
ambiguous bundle; unobserved native loading; missing source. These are acceptance
cases, not a demand for a new fixture framework or full client matrix.

Run after the selected files exist:

```sh
python3 tools/check_instruction_artifacts.py README.md ARCHITECTURE.md docs/maintenance/adoption-diagnostics.md
git diff --check
```

Expected: exit 0, no artifact diagnostics, and explicit inspection of the new
file. The checker can validate artifact/path cases in disposable bundles when
useful; it cannot prove semantic diagnosis or native discovery. No test additions
are required solely for Markdown, and no source tools are changed in this stage.

**Exit:** A reviewable conditional procedure with evidence limits. Direct access
to this procedure may be the final implementation; the skill is optional.

## Stage C — Optional `aek-doctor` wrapper

**Entry gate:** The owner identifies a recurring invocation need and approves
the narrow skill, with the existing procedure already sufficient in substance.
**Files:** Create `templates/skills/aek-doctor/SKILL.md`; update only its source
navigation in `README.md` and the skill table in `ARCHITECTURE.md`. No new required
catalog profile/resource and no automatic native installation.
**Consumes:** The procedure from stage B and established source-resolution behavior.
**Produces:** A portable inactive instruction-only wrapper with a narrow trigger.

- [ ] **DIA-07:** Follow the applicable skill-authoring instructions with local
  adaptations. Write name/description, explicit invocation scope, portable source
  resolution and a link into the operational procedure. Retain one policy owner.
- [ ] **DIA-08:** Exercise selected positive and negative trigger cases in an
  authorized client/sandbox or report the corresponding unverified behavior.
  Verify source-tree and copied-wrapper resolution without author-machine paths.
- [ ] **DIA-09:** Review the actual scoped diff and evidence, run affected artifact
  checks, and present source readiness separately from native activation/usefulness.

| Invocation or state | Required behavior |
| --- | --- |
| Explicit AEK setup/health check for a named project | Select the diagnostic; inspect only relevant concerns |
| Ordinary bug fix, formatting request or missing optional override | No diagnostic-triggered setup or automatic wrapper invocation |
| Explicit import/update request | Route to existing integration, not an overlapping repair implementation |
| Reported long Superpowers session | Use its session-diagnosis procedure when applicable; this wrapper supplies adoption facts only if selected |
| Copied wrapper with source identity | Resolve the actual source procedure; do not assume a fixed relative source root |
| Source procedure unavailable | Explain the limitation; no invented procedure, global install or unintended import |

Run after the selected files exist:

```sh
python3 tools/check_instruction_artifacts.py README.md ARCHITECTURE.md docs/maintenance/adoption-diagnostics.md templates/skills/aek-doctor/SKILL.md
git diff --check
```

Use source/manual review for YAML frontmatter and trigger semantics: the artifact
checker is not a skill-discovery validator. A real behavioral probe must preserve
target state and distinguish invocation, successful procedure use and native
discovery. Missing runtime evidence limits readiness claims; source validity does
not satisfy DIA-AC08 through DIA-AC10 by itself. No external run is implied by this
plan; its actual scope must be selected before executing a probe.

**Exit:** Optional wrapper ready for the explicitly tested scope, or an honest
source-only draft with remaining runtime evidence. Installing it in a consuming
project follows the existing adoption process and separate task authorization.

## Acceptance coverage and conditional follow-up

| Spec criteria | Owning stage |
| --- | --- |
| DIA-AC01, DIA-AC02, DIA-AC04, DIA-AC05, DIA-AC06, DIA-AC07 | A, B |
| DIA-AC03, DIA-AC11 | A, B, C |
| DIA-AC08 | A, C |
| DIA-AC09, DIA-AC10 | C |
| DIA-AC12 | A and each packaging gate |

If the only useful outcome is a clearer update explanation, propose a bounded
change to MIGRATION's existing B/C/N reporting and the integration skill's route.
Do not build the diagnostic merely to deliver that improvement. Prepare that
change against its actual findings rather than a speculative universal formatter.

No phase adds a monitoring service, new settings schema or source-freshness
database. A concrete discovered checker bug has its own diagnostic/fix scope;
it is not permission for a checker rewrite within this documentation-led plan.
At each selected stage stop for the ordinary user checkpoint and reuse valid
evidence on resumption. Deferred stages remain explicitly deferred, not completed.

## Execution evidence

None yet. The supplied sandbox remains unprovisioned. No diagnostic copies or
seeded defects exist; source implementation, native invocation and usefulness
are unverified.
The roadmap tracks preparation of this proposal; future work records actual stage
outcomes here with links to the single owner of detailed target evidence.
