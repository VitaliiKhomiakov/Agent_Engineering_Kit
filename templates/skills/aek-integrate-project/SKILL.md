---
name: aek-integrate-project
description: Use when the user explicitly opens the Agent_Engineering_Kit integration wizard, requests preparing, importing or updating its rules, or asks to check an existing AEK adoption. Ordinary coding, a general audit or missing instruction/model files alone do not trigger it.
---

# Integrate project rules through a chat wizard

Deliver a reviewable preparation, the authorized import/update, or a read-only
check of an existing adoption. Use the source framework's `MIGRATION.md` as the
procedure owner; preserve the selected stage checkpoints. This is an
instruction-only conversation, with no installer or terminal UI. Full integration
includes the procedure's required model-selection step through the existing model skills.
Read this entry and the model skills from the identified source by default; their
use does not install them in the target. Source `MIGRATION.md`, "Setup procedures
and persistent skills", owns explicit installation choices and existing-copy handling.

## Open or resume the wizard

Use the user's conversation language for the menu, questions and progress; follow
the framework's artifact-language policy for generated project instructions.
When the request already names an operation and supplies its inputs, proceed to
that operation instead of making the user select it again. Reuse the current task
and the adoption record on continuation; do not restart onboarding.

Otherwise show this menu, translated into the user's language, and wait for a
choice by number, label or free text:

1. Integrate instructions into an existing project.
2. Prepare instructions for a new project.
3. Update an existing AEK adoption.
4. Check an existing AEK adoption.

Choices 1–3 begin with preparation; choosing an item alone does not authorize
target writes. Choice 4 is read-only. Keep any explicit import/update permission
already granted in the request; the menu does not add a new approval requirement.

Use the client's actual question controls when available in the current mode;
otherwise use numbered text. Respect the tool's option/input limits and accept
free-form corrections. A text menu is not a rendered widget. Do not invent buttons,
registered slash commands, or a separate terminal window. Reading this source
skill can drive the conversation without a native skill installation.

Ask one focused question at a time, or combine closely related missing inputs
when the client supports it. Wait for required choices; a preselected option or
elapsed time is not an answer. Continue independent inspection only within known
scope. Ask for the target path before inspecting another project's files; reuse
an explicitly supplied path and the known client instead of asking again.

Accept requests to go back, change choices, pause or cancel. A changed choice
invalidates the affected proposal; it does not undo completed writes. On stopping,
report the last completed work and any actual partial changes, following recovery
rules. Do not silently restore files or restart a canceled operation.

## Resolve the source and target

Reuse the supplied source, target roots/checkouts, client, intent and canonical
task. For an existing adoption, read target `.agents-framework/adoption.md` for
source identity and owned scope. Ask only for material missing information.

When read directly at source `templates/skills/aek-integrate-project/SKILL.md`,
the framework root may be three directories above this skill folder only if both
`MIGRATION.md` and `standards/catalog.toml` verify that source context. An inactive
adopted copy is not the full source library. From an adopted bundle or native
installation, resolve the accessible
framework source from the request or adoption record, independently of the skill's
directory. Never assume the target contains MIGRATION or is the source library.
If that source is unavailable, identify the missing resource before dependent
preparation/application. For check-only work, inspect reachable installed resources
under the procedure's read-only checking contract and report comparison limits;
ordinary work continues through reachable local rules.
Do not invent policy or globally install another copy.

## Guide the selected operation

1. **Locate and inspect.** Establish the target roots/components and selected client.
   For initial adoption of an existing project, or an update needing fresh stack
   evidence, follow MIGRATION's "Stack evidence for profile selection" before asking
   the user to enumerate
   technologies. Inspect active instructions and any adoption record. A check uses
   only the additional stack evidence needed for its requested scope. For a new
   project, ask about intended languages, frameworks and goals; keep proposed facts
   separate and leave a nonexistent path uncreated during preparation.
2. **Present the selection.** Show a compact table of component, technology/version,
   evidence, status (observed, inferred or requested), and proposed catalog profiles.
   Explain necessary profile dependencies. Ask only about material uncertainty,
   unsupported choices or desired changes. Preserve recorded selections on updates
   unless changing them is in scope; a newly found dependency is not approval to
   replace a profile. For a check, compare the recorded selection with available
   evidence and report mismatches or unknowns without requiring new profile choices.
3. **Prepare or check.** For preparation/import/update, follow "Prepare and apply"
   and its model-selection step. Present proposed paths/actions and content diffs,
   local contracts/conflict decisions, model-step outcome and verification scope.
   For choice 4, follow "Checking an existing adoption" and return its report;
   do not switch into setup or application automatically.
4. **Apply within authorization.** Apply an agreed change set when authorized;
   otherwise finish the concrete preview and ask for the missing approval. Reuse
   existing scope and permission, including an explicit preparation-only limit.
   A material unresolved decision blocks only its dependent changes. Follow the
   procedure's baseline, conflict, interruption and recovery rules.
5. **Verify and hand off.** Report actual file results and evidence, with model
   configuration and observed client activation stated separately. Explain the
   next normal development action, or how to resume an incomplete adoption, without
   requiring the wizard before every coding task.

Keep progress visible at meaningful transitions: inspecting the project, choosing
profiles, preparing the diff, applying authorized changes and checking the result.
Show completed work, the current action and any decision needed. Use file/operation
counts only when known; do not invent percentages, a background job or success for
pending work. Skip irrelevant or already completed steps, and reuse valid evidence.

## Read the relevant procedure

Paths in this table resolve from the identified framework source. Select sections
by their headings; follow further references only for the requested operation.

| Work | Read |
| --- | --- |
| Any import/preparation | MIGRATION: Import inputs and boundaries; Prepare and apply; Execution rule for the migration |
| New/existing target and conflict inventory | MIGRATION: New and existing projects; Phase 1; Stack evidence for profile selection; Resolving active conflicts; relevant Phase 2 profile choices |
| Explicit check-only request | MIGRATION: Checking an existing adoption; actual adoption record, installed entries/resources and relevant native settings |
| Bundle and target entries | MIGRATION: Setup procedures and persistent skills; Layout and path contract; `standards/catalog.md`, selected catalog profiles and relevant Phase 3 instruction restructuring |
| Selected project task skills | MIGRATION: Optional project task skills; Adapting installation routes; selected templates and native mappings in the adoption record |
| Model selection/reuse | MIGRATION: Model-selection step; `aek-model-setup` or `aek-model-reassign` as selected there; source `standards/model-configuration.md` owns actual settings |
| Proposed/applied record | MIGRATION: Adoption record and ownership; `templates/framework/adoption-record.md` |
| Repeat/update or selected relocation | MIGRATION: Repeat and update; Relocating an existing import; current record and actual managed target contents |
| Before writes or interrupted work | MIGRATION: Partial application and recovery |

For import/update, prepare source/profile/path/action/content and conflict decisions
under that procedure. Preparation-only intent leaves the target untouched. For application,
reuse existing authorization, preserve originals and reconcile intervening edits;
replace loaded conflicts while retaining required local contracts and gates.
Keep existing task stores and model choices. Pass adoption intent, selected mode,
prior choices, source/target roots and write scope to the model procedure. Reuse
consistent selections and explicit deferrals without repeated questions; report
unresolved setup separately. If a model skill is unavailable, use its reachable
contract and disclose the fallback; an inaccessible contract blocks only dependent
setup. Preparation remains write-free. Preserve scope, typing and proportionate verification
rules when adapting entries; catalog availability is not unconditional reading.

Report prepared/applied/checked/unchanged/partial scope, evidence, unresolved decisions and
the next agreed checkpoint, including the model-step outcome and its owner references
when that step applies. A check reports existing model state without initiating setup.
Distinguish valid files and saved choices from observed client discovery/activation.
Neither source-based reading nor copying this skill proves native activation.
For task skills, report the selected native subset separately from source
preparation templates. Include those native paths in comparison, before-write protection
and explicit installed-file checks; a same-name local skill is not owned by default.
