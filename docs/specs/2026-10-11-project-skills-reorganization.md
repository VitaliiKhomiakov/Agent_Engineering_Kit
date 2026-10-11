# Project skill reorganization specification

**Date:** 2026-10-11.
**Status:** Accepted design implemented and reviewed for the bounded source-library
scope on 2026-10-11. The canonical plan records final acceptance and client limits;
real consumer installation remains a separate authorized adoption task.
**Execution and progress owner:** [Implementation plan](../plans/2026-10-11-project-skills-reorganization.md).

## Outcome and scope

Reorganize selected AEK guidance into skills installed in consuming projects.
These skills help agents design, implement and review those applications; they
are not skills for maintaining the AEK source repository. Preserve the correctness,
applicability and accessibility of existing engineering rules throughout adoption
and updates. A skill is an additional task entry, not a new instruction authority.

The owner requested five connected outcomes: a staged reorganization; no orphaned
operational instructions; correct copying and use in new/existing projects;
compatibility with Superpowers; and a final review of conflicts, inaccuracies,
wording and duplicated rules. This document specifies all five. The original
planning request authorized these documents only. After their analysis, the owner
instructed execution on 2026-10-11. The canonical plan records the current stage
and checkpoints; that instruction does not independently authorize consumer
installation, native configuration changes or unspecified external evaluations.

Non-goals: a new application/runtime, automatic installer, recommendation service,
blanket language-by-phase skill matrix, model reassignment, plugin-cache edits,
technology upgrades, and unrelated consumer-code remediation.

## Current evidence and limits

Source inspection on 2026-10-11 found catalog schema 1 with 35 profiles, seven
required profiles, 182 standards Markdown files, and three inactive skill templates:
aek-integrate-project, aek-model-setup and aek-model-reassign. These counts describe
the pre-change source, not evidence that every instruction is used.

- [Architecture](../../ARCHITECTURE.md#components-and-loading) separates shared
  rules, project facts, native skills, configuration and task procedures.
- [Catalog](../../standards/catalog.md) defines availability and conditional
  reading. Its dependencies are not a reading queue.
- [Adoption](../../MIGRATION.md) already owns new/existing imports, path adaptation,
  three-way update reconciliation and recovery.
- [Superpowers integration](../../standards/superpowers.md) already assigns process
  skills and adapts planning, Git, testing, delegation and evidence reuse.
- [Artifact checks](../maintenance/verification.md#artifact-checker) validate
  declared resources and supported syntax. They do not establish semantic
  reachability, native skill discovery or agent adherence.
- The earlier [pilot outcome](../plans/2026-10-07-agent-behavior-pilot.md#stage-a-completed-in-unblinded-mode--2026-10-11)
  covers one task using the old arrangement. It does not test these proposed skills
  or demonstrate equivalence, benefit or token savings.

Official [OpenAI skill guidance](https://learn.chatgpt.com/docs/build-skills) and
[Claude skills](https://code.claude.com/docs/en/skills), reviewed on 2026-10-11,
support on-demand instructions and reference material. Client installation,
metadata and loading behavior remain version-specific. The installed Superpowers
source reviewed for this proposal is 6.4.2; it is not an assumed consumer version.

## Global constraints

- Preserve mandatory rules, their applicability and required project/CI checks.
- Keep one authoritative owner for each rule; skills route to it without copying full policies.
- Keep catalog schema 1, existing profile IDs, public paths and legacy aggregate semantics compatible.
- Keep existing instructions usable while adding and checking replacement routes.
- Keep operational project skills usable without the AEK source checkout or disposable pilot directory.
- Preserve unrelated edits, accepted exceptions, model choices, task stores and historical evidence.
- Keep source templates inactive; install only the selected skills in the selected client's verified native location.
- Do not infer native activation, rule adherence or semantic correctness from copied files or passing link checks.
- Do not add Git actions, delegation, model changes, installations or consumer-code edits through a skill trigger.
- Keep specifications, plans and agent-facing instructions in English; communicate with the owner in Russian.

## Proposed design

### Separate durable rules from task entry points

Retain standards as the authoritative technical reference. Root/native project
entries retain mandatory constraints and routes to relevant rules even when no
skill activates. Project passports retain actual paths, versions, commands and
accepted architectural decisions. Native skills select and apply the relevant
references for a task. Deterministic enforcement remains in checks where available.

An initial proposed set has three task boundaries:

| Proposed skill | Trigger and input | Output and responsibility | Exclusions |
| --- | --- | --- | --- |
| aek-design-feature | New capability or material boundary/contract change; requirements, actual project architecture and selected stack | Technical design covering owners, dependencies, contracts, alternatives and relevant checks, in the existing canonical task | Simple wording changes; an automatic project-wide redesign; a second planning lifecycle |
| aek-implement-feature | An authorized code change with sufficient acceptance and design; affected project and checks | Scoped implementation applying relevant standards, with evidence for acceptance | Unapproved material design; setup/delegation; mandatory new abstractions or tests for every edit |
| aek-review-changes | A requested review or applicable completion review; baseline, actual diff, task and local gates | Prioritized findings with affected paths, violated contract, consequence and evidence; explicit coverage limits | Automatic fixes; stylistic quotas; a claim that the same agent is an independent reviewer |

These names and boundaries are proposed for review. A small fix can use the
implementation entry without invoking architecture; a review-only request does
not begin coding. Each entry must demonstrate a distinct routing/output benefit
over the current entry tables. If it merely forwards to an existing Superpowers
procedure without adding useful AEK selection or result guidance, simplify or
omit it with a recorded disposition before rollout.

The source locations are proposed as `templates/skills/<name>/SKILL.md`. Reuse
existing topics and examples; add supporting files only for missing task-specific
content. Do not copy a language guide into each phase skill. A skill may package
reference knowledge as well as steps, but shared rules retain their owner.

### Catalog and selection contract

Propose one optional schema-1 profile, project-workflows, whose source is a new
standards/project-skills.md and whose resources are the selected workflow templates
and genuinely required support files. It depends on existing shared policy; it
does not select every technology. Existing technology profiles remain independent.
Do not introduce undocumented catalog fields or silently change old selections.

The new guide owns skill selection, entry composition and result boundaries;
MIGRATION retains installation/update/recovery ownership, and standards/superpowers.md
retains process adaptations. The target import preview explicitly selects native
skills, their client mapping, source identity and destination paths. Bundle resource
availability and native skill installation are recorded separately.

At ordinary task time, skills resolve project facts and relevant installed profile
entries from reachable local routes. Do not make every edit read adoption metadata,
scan all standards, or query the original source. Adoption metadata remains for
import/update/recovery. A task needing an omitted profile reports the missing
guidance and follows the existing scope decision; it does not silently install it.

### Reachability and preservation

Before editing active rules, create a scoped inventory under docs/research for
this migration. Cover active standards, catalog profiles/resources, root/native
entry templates, skills, role instructions and applicable adoption routes. Inspect
both files and independently triggered normative sections within them.

Each inventory row records: source path/section, rule owner, task/stack condition,
current entry route, proposed entry route, bundle/profile availability, consumer
or scenario, disposition, and verification reference. Dispositions distinguish
mandatory policy, conditional reference/example, native entry, compatibility route,
and historical/inactive artifact. A retained rule must have a feasible route from
an actual entry under its applicable condition; catalog membership alone is not enough.

Require every active rule/topic to have a disposition and every applicable route
to have its resources. Label intentionally optional examples and historical records;
absence of use in one pilot does not make them dead or authorize deletion. Group
rows only when their ownership, triggers and route are identical. Inspect shared
cross-profile routes against both minimal and combined selections.

Classify apparent duplication as authoritative rule, short routing reminder,
conditional example, compatibility alias or conflicting normative copy. Remove or
reduce duplicate normative owners; preserve useful reminders with links. A text
similarity search only supplies candidates for semantic review. Do not claim a
static scan proves that the model will actually read or obey every rule.

### Portable adoption and update

MIGRATION remains the single procedure for prepare-only, initial import, repeat,
update and recovery. Extend it to cover the new entries without adding an installer.
Preparation is target-write-free. Application requires a concrete selected scope,
preserved originals and absence markers, and a recheck for intervening edits.

Both new and existing projects receive the selected rule closure and adapted skill
references from their final native location. Preserve contained, recorded flat and
custom layouts. Independently opened nested repositories need locally reachable
entries/resources; an undiscovered workspace parent is insufficient. Skills must
use the actual bundle placement rather than hardcoded author-machine paths.

Keep the existing three skills compatible. The integration skill may still need
the identified source to perform imports/updates; that existing maintenance-of-an-
adoption dependency is explicitly separate from everyday design/coding/review.
Operational skills and required references must work when the source is unavailable.

Record selected skill names, adapted native paths and content identity in the
existing adoption record's managed scope. Preserve current source/B/C/N update
semantics, local modifications, intentionally absent files, same-name unowned skills,
accepted exceptions and model configuration. No implicit replacement by name.
Keep accepted snapshots and recovery copies outside active discovery.

First implement and observe the Codex project mapping using the actual available
client/version. Retain existing Claude/Cursor instruction behavior. Any newly
advertised native skill mapping for another client needs its own official-contract
review and actual discovery/use evidence; until then label it unsupported or
unverified and retain the documented direct-reference fallback. Never describe
all clients as verified from one client's run.

### Superpowers composition and conflict handling

AEK task skills apply local technical standards and define task-specific outputs.
Superpowers owns its selected procedural steps; AEK's existing adaptations and
user authorization govern their application. Select one procedure per applicable
operation, without a second checklist, plan store or approval cycle.

The AEK entry may direct the agent to an applicable Superpowers procedure after
reading local adaptations. Superpowers must not be copied, patched, shadowed by
name, or made to call back into the same AEK entry recursively. Reuse a procedure
already loaded and satisfied in the current task. Missing Superpowers uses the
existing documented fallback; missing native skill support does not erase rules.

Review concrete overlaps: design approval and short fixes; canonical spec/plan
paths; TDD and proportionate testing; independent review versus self-review;
default commits/worktrees versus current-checkout mode; stage stopping and prior
authorization; delegation/models; evidence reuse; language; and task-trigger scope.
Also reconcile project/ancestor/client-native instructions and accepted exceptions.
Markdown cannot change native instruction precedence or grant permission.

## Verification contract

### Evidence levels

1. Structural: selected files, format, native paths, resource closure and links.
2. Semantic: preserved rule meaning, ownership, conditions, routes and absence of conflicts.
3. Observed client behavior: discovery, explicit/implicit activation, actual relevant
   reading, task result and respected boundaries in a named client/version.

Record these separately. Checker enhancements should cover bounded deterministic
gaps such as installed skill reference closure or metadata if justified. Existing
checks do not parse all YAML/native imports/code-span routes; cover such cases
explicitly and document unsupported syntax. Do not build a generic semantic judge.

### Required scenario families

| ID | Scenario | Required evidence |
| --- | --- | --- |
| V01 | Complete active-instruction inventory | Every active rule/topic has owner, condition, feasible route and disposition; no unresolved orphan |
| V02 | Minimal and combined profile bundles | All existing profile selections retain their contracts; new workflow selection adds only its closure; old aggregate IDs/anchors remain valid |
| V03 | New project and independently opened child | Selected native skills and rules resolve from final paths; no placeholders, inactive duplicate discovery or dependency on source access |
| V04 | Existing project initial import and update | Local gates/architecture/task stores/settings survive; same-name unowned skill and B/C/N edit cases reconcile before replacement |
| V05 | Repeat, interrupted import and recovery | Unchanged repeat does not rewrite; partial state is explicit; scoped recovery preserves later user edits and leaves one active skill definition |
| V06 | Contained, flat and custom bundle layouts | Native entries, code-span/native imports and support references resolve correctly; optional omitted profiles/history cause no broken required route |
| V07 | Skill behavior | Matching design, implementation and review tasks load needed rules; explicit invocation works; an unrelated request and small fix do not start excess workflows |
| V08 | Superpowers present and unavailable | Present case respects local adaptations without recursion/duplicate work; unavailable case uses honest fallback and preserves required rules |
| V09 | Existing versus proposed arrangement | Matched fresh workspaces/tasks on the same recorded client/model/settings; compare acceptance, relevant reading, violations and corrections |
| V10 | Final integrated review | No unresolved material rule loss, conflict, inaccurate contract, duplicated normative owner or advertised-but-unverified activation |

Automate source/profile coverage across all catalog profiles. Use representative
target fixtures for Python/FastAPI, browser TypeScript/React without Next.js,
Angular with and without NgRx, plus a non-web selection such as Go or Unreal;
reuse current profile tests for other combinations. Static selection coverage is
not a requirement to build applications in every stack.

Client behavior trials use bounded design, implementation and review cases with
explicit expected outputs and safe/unrelated counterexamples. Review cases include
a known material defect and a legitimate exception to expose both misses and false
positives. At least one implementation case checks actual behavior against acceptance.
Fixture descriptions, relevant starting files/content identities, expected outcomes,
commands, versions and concise results must remain in AEK after temporary workspaces
are deleted. Keep private data and unnecessary full transcripts out of source.

For V09, retain the existing rules and enabled Superpowers in both conditions and
vary only the proposed AEK entry packaging. Freeze relevant inputs and isolate
fresh contexts; record contamination or unavailable model/client settings. A single
pass does not establish statistical benefit. Repeat only to resolve an observed
failure or material uncertainty. No unmeasured cost or universal quality claim.

Unavailable client execution leaves its behavioral gate open. Do not replace that
gate with a simulated model, file inspection, or the previous pilot's success.
Select the actual client and bounded execution scope before these trials; this
planning request alone does not authorize external calls or consumer installation.

## Acceptance and rollout

| Criterion | Completion condition | Evidence |
| --- | --- | --- |
| AC01 | Approved scope distinguishes consumer skills from source maintenance; ownership and stage boundaries are explicit | Spec and canonical plan |
| AC02 | All existing active instructions have a reviewed disposition; mandatory meaning and conditional applicability survive | V01, V02 and semantic mapping |
| AC03 | Installed workflow skills have precise triggers/non-triggers, local references and distinct value without policy duplication | V03, V07, V09 |
| AC04 | New/existing imports, updates, layouts and recovery preserve consumer state and selected resource closure | V02–V06 |
| AC05 | AEK, Superpowers and local/native instructions have no unresolved material conflict or recursive workflow | V07, V08, V10 |
| AC06 | Native support claims match observed client/version results; limitations remain explicit | V03, V07–V09 |
| AC07 | Final review covers actual integrated source, installed copies and changed/new files; findings are resolved and affected checks pass | V10 and review dispositions |
| AC08 | Evidence and rollback guidance remain understandable without disposable projects; old paths are retired only after replacements pass | V01, V05, retained evidence |

Introduce the architecture entry as the first vertical slice: source template,
catalog route, installed target, preserved rules and observed use. Keep the old
direct routes available. Expand to implementation/review only after that slice's
acceptance. Final cleanup follows full mapping and integrated review, not file age
or lack of activation in one trial. Do not flip existing consumers automatically.

Rollback uses preserved adapted contents and scoped reconciliation under MIGRATION,
not a repository reset. An incomplete behavioral or semantic gate blocks the
affected rollout; it does not justify removing checks or declaring equivalence.
The final reviewer inspects conflicts, accuracy, applicability and duplication
across the whole changed system, not only syntax. Record whether the review was
independent; do not invent a second reviewer when unavailable.
