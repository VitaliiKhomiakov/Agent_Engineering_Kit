# Adopting AgentsFramework in a project

The goal is to align instructions and development with the target standard
without losing required behavior. An audit records facts; it does not declare
the current code correct. This framework's structure does not derive from any
specific company or existing project.

This document owns adoption of instructions, selected engineering rules, skills
and native configuration templates. The [scope](docs/specs/2026-09-20-agents-framework.md)
is a rules framework. Apply reviewed changes through the current agent or normal
file editing; no AgentsFramework application or installer is required.
Import selected resources from this source library into the target project and
adapt its entry routes. Active AGENTS/PLANS files in the source repository are not
a prerequisite; check instruction loading in the target project. Preserve shared
core and verification rules, including limits on speculative code checks and
redundant tests, while reconciling existing local contracts and required checks.

## New and existing projects

For an existing project, follow inventory, target decisions and scoped instruction
changes. A separately authorized bounded pilot establishes observed client behavior
before further rollout. Preserve required behavior and independent user work.

For a new project, inventory the chosen workspace/client and any parent rules,
record the intended stack and architecture, and prepare selected entry points.
Label intended architecture as proposed, not observed. Skip legacy-code remediation
where there is no existing code. Change native settings only within authorized scope;
verify actual discovery and any selected roles during an authorized pilot.
Neither path requires a Git repository at the workspace root.

## Import inputs and boundaries

Use this procedure for an explicit request to prepare, import or update the
framework. Ordinary development or a missing AGENTS file does not trigger it.
Reuse supplied facts; ask only for material gaps needed by the affected step:

| Input | Establish |
| --- | --- |
| Framework source | Accessible location and revision, or verifiable content identity when no revision exists; never infer a remote revision |
| Target | Selected workspace/projects, instruction roots and implementation checkouts; name independently opened repositories |
| Client | One selected client and known version/capabilities; unresolved capability limits remain explicit |
| Intent | Prepare only, initial import or update; new/existing project context, applicable stack and permitted paths/actions |
| Existing task | Canonical adoption task/store, current stage, granted permissions and checkpoints; preserve existing model choices |

The source library, target instruction root, execution checkout and canonical task
store are separate roles even when some paths coincide. Read source procedures
directly when the target has no installed entry; this does not establish native
skill discovery. Source AGENTS/PLANS installation is not required. Limit changes
to selected targets; import grants no application-code changes, dependency upgrades,
task-store relocation, other-client setup, global settings or plugin-cache edits.

### Integration entry and location

Use [af-integrate-project](templates/skills/af-integrate-project/SKILL.md) for an
explicit framework preparation/import/update request. General audits, ordinary
coding and missing instruction/model files alone do not trigger it. The skill
routes into this document; it replaces the former conceptual migration entry.

Before installation, the agent can read the template from an accessible framework
source named in the request. No global installation is needed. For an authorized
Codex project installation, the proposed layout is
`.agents/skills/af-integrate-project/SKILL.md`; verify discovery in the actual
client/version separately. Other clients require a verified native skill mapping;
until then source-based reading is available without claiming native discovery.

At the source template location, the skill resolves the framework root three
directories above its folder. In an installed target it resolves source identity
from the request or `.agents-framework/adoption.md`, not a relative walk to the
target root. Keep that source accessible for future updates; an installed skill
alone is not a self-contained copy of the migration library. Resolve source-relative
references there and target-relative references against the named target root.
Adapt entry routes to the actual installed skill or accessible source location;
check independent repository opening and any selected role's reachable route.

## Prepare and apply

Phases 1–2 below supply the inventory and selection; phase 3 supplies entry and
native mapping details. Read only the sections needed by the requested operation.
They form one procedure for both new and existing projects.

1. **Inspect and prepare.** Read affected active instructions and current destination
   contents. Select the catalog bundle, resolve its required local references and
   fill entry/passport placeholders with actual paths and known or intended facts.
   Keep optional research outside required reading. Produce a reviewable change set:
   source identity, profiles, target/client, path-by-path create/update/retire actions,
   proposed content or diff, conflict decisions, retained contracts and check scope.
   Mark unresolved material decisions and the paths they block.
2. **Respect intent.** Preparation only leaves target files untouched, including
   directories, configuration and adoption records. Present the preview in the
   response or agreed storage outside the target. An explicit import may already
   authorize the prepared replacements: reuse that permission without per-file
   questions, while honoring selected stage checkpoints. Finish concrete preparation
   before seeking any missing apply approval. Continue independent preparation
   while a material decision blocks dependent replacement.
3. **Preserve and reconcile.** Before the first target write, retain original contents
   or absence, including user edits, outside active instruction/skill discovery.
   Compare current files with the preparation baseline; reconcile intervening edits
   before overwriting. A deletion/retirement needs the same protection. Preserve
   unrelated settings, roles and comments. No Git action or model switch is implied.
4. **Apply the agreed scope.** Edit the actual loaded sources using the conflict
   rules below. Retire obsolete active content only after its necessary contracts
   have reachable owners. Keep reading conditional, including local project and
   delegated-role entry routes. If application stops, report changed and remaining
   paths and retain recovery material; do not declare incomplete work verified.
5. **Verify and report.** Check changed formats, target-relative references,
   placeholders, conflicting loaded content and preserved contracts. Reuse valid
   evidence under the verification policy; copying instructions alone requires no
   application test suite. Report verified files separately from observed client
   discovery/adherence. An unavailable client or unsupported mapping limits that
   claim and does not justify inventing a native setting or running a pilot.

Updates also need comparison with the last accepted import and current local edits;
the current source alone is not a safe replacement baseline. The canonical adoption
task owns decisions, authorization and progress; the source library plan is not a
second progress record for a target import.

## Adoption record and ownership

During authorized application, adapt the
[record template](templates/framework/adoption-record.md) to target
`.agents-framework/adoption.md`. It records source/content identity, target/client,
selection, owned destination paths or portions, accepted exceptions, accepted
contents and recovery references. Entries/passports point to it for provenance;
ordinary tasks do not read it. Keep model assignments and task progress with their
existing owners. A preparation-only request keeps the proposed record outside the
target. Include the record itself in before-write protection, without a self-hash.

Record both source/template identity and the accepted adapted target result. A
revision alone is insufficient for locally modified source files; identify the
selected contents. Preserve retrievable comparison/recovery snapshots as needed;
a hash proves equality but cannot supply missing merge or restoration contents.
Ownership covers only recorded files/portions, never every `af-` name or all fields
of a shared native file. Record source removals and proposed ownership changes in
the preview. Losing access to the record does not grant ownership of target files.

| Agreement state | Meaning |
| --- | --- |
| Prepared | Reviewable candidate; preparation alone writes no target record |
| Applied but unverified | Planned writes finished; specified file checks remain incomplete |
| Verified | Specified checks passed for the recorded contents; state the file/client scope separately |
| Partial | Interrupted/failed application or recovery; actual path outcomes need reconciliation |

Advance the last accepted source/selection/content references only after the agreed
file checks succeed. Keep the previous accepted references through an incomplete
update; on first import there is no accepted base yet. If the record cannot be
written safely, report partial state in the canonical task instead. A record flag
alone cannot establish success or supersede actual files and operation evidence.

## Repeat and update

Read this section only for a repeated import or update. Reuse source, client and
selection choices; ask only for a changed material decision. Compare each managed
scope using **B** (last accepted adapted contents), **C** (current target) and **N**
(new candidate adapted from the selected source, retaining local contracts and
accepted exceptions). Raw upstream template bytes are not a target-ready candidate.
Distinguish an intentionally absent path from unavailable evidence.

| Observed relation | Action in the prepared change set |
| --- | --- |
| Source identity, selection/layout and target still match the accepted state | No rewrite, timestamp refresh, setup questionnaire or repeated valid check; report unchanged |
| C = B; N differs | Propose the scoped source update; recheck C before writing |
| N = B; C differs | Preserve local edits; do not reset the target or silently accept a new base |
| C = N | No content rewrite; reconcile provenance if needed using applicable evidence |
| Both C and N differ from B | Compare the actual edits; combine independent changes while preserving user work, expose overlapping or semantic conflicts before dependent writes |
| Base contents unavailable | Recorded hashes may establish equality; if differing edits need a missing base, report the limit and reconcile explicitly, never claim a safe three-way merge |
| Source removed a resource, selection dropped it, or a managed target is missing | Propose retain/replace/retire/restore explicitly; preserve local content and references, never infer deletion consent or recreate a user deletion blindly |
| Destination has no recorded ownership | Treat it as existing project content; reconcile initial adoption before acquiring scope |

Use the whole planned scope, including changed routes, exceptions and native fields;
do not declare an import unchanged merely because one file matches. If prior work
was partial or unverified, matching bytes avoid rewrites but do not discharge its
outstanding checks. Reuse valid evidence under the shared verification policy;
only changed inputs or concrete unresolved questions require new checks.

## Partial application and recovery

Before writing, choose a recoverable location outside the selected client's active
instruction/skill discovery; do not place old AGENTS/skills in discoverable backup
folders. Preserve exact originals or absence for affected paths, including the
record and shared files, plus the prepared and actually written content identities.
Keep recovery contents accessible through review/recovery; a temporary path alone
is not a durable future merge base. Record unavailable or expired evidence honestly.

On failure or interruption, stop dependent writes and identify written, untouched
and uncertain paths in the canonical task. Mark the record partial if safe; do not
overwrite newer record edits merely to update a status. Inspect uncertain outcomes
before retrying. For each affected path, compare actual contents with this operation's
written result before restoring: restore its original only if no newer work would
be lost. Remove an operation-created file only when it still matches that result;
recreate a deleted file only when its path remains absent. Reconcile intervening
edits or collisions instead of bulk rollback, reset or deletion.

Resume using actual files, the last accepted state and operation evidence. Complete
remaining authorized actions or scoped recovery; record unresolved paths explicitly.
Retain recovery material while it is needed. Safe rollback does not by itself prove
client behavior or authorize a new import. Verify only affected results and pending
gates; never label partial work verified or restart an unchanged full verification
cycle merely because another agent resumes the task.

## Execution rule for the migration

Use [direct mode](standards/work-modes.md) by default: work in the current
directory and checkout without branches, worktrees, commits, staging, or stashes.
Define one small logical stage, finish it, apply
[proportionate verification](standards/verification.md), report the evidence and
limitations briefly, propose the next stage, and stop for user review. Do not start the
next stage or a background implementation while waiting.

Only an explicit user instruction enables autonomous worktree execution. Worktree
permission alone does not grant permission to commit, merge, copy changes into
another checkout, push, or open a pull request. Record each authorized Git action
in the task contract. The phases below describe dependencies; they do not grant
automatic progression through the migration.

## Phase 1: inventory and conflicts

In the selected workspace, establish the launch root, repository boundaries,
one selected client and available version evidence, active instruction/configuration
sources, available skills/plugins, architecture documents, specs, CI commands,
and relevant stack versions including databases and infrastructure. Inspect client
capabilities needed for the selected import; account/subscription access matters
only for authorized setup or execution that depends on it. Do not copy credentials.
Include files from other editors only when the active client reads them or
another instruction links to them; existence alone does not establish loading.

For Codex, inspect relevant AGENTS and override files. For Claude Code, inspect
its native instruction chain and whether an AGENTS import bridge is necessary.
For Cursor, inspect AGENTS, `.cursor/rules/*.mdc`, and agent definitions from
native and compatibility directories. Reconcile names and policy before writing.
Check the root and independent repository launch paths; settings precedence and
instruction precedence are separate mechanisms.

List sources and sizes first, then read affected rules selectively. Do not read
all source code and plans merely to inventory instructions. Preserve current user
work and prepare a reversible diff or a source-instruction copy outside AGENTS and
skill discovery paths.

| Found rule or fact | Problem | Target decision | Preserve |
| --- | --- | --- | --- |
| `<source and scope>` | `<conflict/duplicate/stale/gap>` | `<move/rewrite/remove/keep>` | `<material contract or constraint>` |

For old architectural decisions, state whether requirements confirm them, they
are temporary compromises, or they need replacement. Do not infer best practice
from frequently repeated poor code. Existing projects remain audit evidence.

Ready for review when relevant active sources, conflicts, known versions and any
requested pilot scope are recorded, with capability gaps explicit. Product tests
are unnecessary merely to produce this inventory.

### Resolving active conflicts

Within authorized adoption, selected framework policy replaces conflicting old
process instructions in the files actually loaded by the client. Reconcile each
affected root, nested, alternate or role entry; declaring a new root superior is
insufficient. Classify content by its purpose, not its age or filename:

| Existing content | Treatment |
| --- | --- |
| Generic blanket process, such as full-suite runs after every edit or repeated final reviews | Replace with the relevant framework owner and conditional route |
| Duplicate engineering explanation | Consolidate under one reachable owner and retire the active duplicate |
| Actual build commands, CI/release gates, supported versions, business/security invariants and project contracts | Preserve at the relevant local entry, passport or check document |
| Deliberate project exception | Retain its scope, reason and accepted decision; resolve a conflicting change explicitly |
| Ambiguous behavior requirement or mandatory gate | Clarify before dependent replacement; continue unaffected preparation |
| Superseded instruction content | Preserve recoverable originals outside active discovery before retirement |

A costly mandatory check remains a gate. Its actual trigger differs from a generic
demand to rerun it after every edit. Native precedence, higher-priority instructions
and actual tool permissions still apply. If an opposing rule is outside authorized
control, report its source and affected scope as unresolved; do not claim coherent
adoption for that scope. Never silently substitute framework defaults for unknown
product requirements.

## Phase 2: target profile

Choose the applicable common, language, framework, database, and technology
profiles and complete the
[architecture passport](templates/project-architecture.md), separating actual
state from target state. Record language, framework, database, and ORM versions;
responsibility flow; DTOs; interfaces or Protocols; justified patterns and DI;
and contract owners where applicable. For Unreal, record engine/build and target
evidence, gameplay/module/asset owners and engine-managed composition; do not force
HTTP/ORM fields, backend layers or custom DI constructors. Pattern applicability
follows the core standard; migration does not require adding a Factory, Facade,
Strategy, or monadic abstraction.

Use the [catalog guide](standards/catalog.md) when assembling the bundle: include
shared required profiles, selected dependencies and resources, but derive reading
routes from the task and actual stack. A dependency keeps files available; it
does not make their instructions applicable. Include the guide among shared assets.
Check that Python-only work excludes unused FastAPI/Pydantic sections and that
JavaScript React work excludes TypeScript obligations and unused Next.js sections.
For Unreal, follow `standards/unreal-engine.md`: Blueprint-only work excludes
unneeded C++ details, source-only work does not require MCP, and Python editor
scripting selects relevant Python guidance without unused backend frameworks.
Generic C++ files alone do not select Unreal. Preserve reachable copies of the
entry and all six resources; the mandatory workflow needs no personal skill path.
Inline planning alone does not require delegation or model setup.

For several projects, also fill the root
[workspace map](templates/workspace-architecture.md): responsibilities, contracts,
runtime interactions, and data ownership. Keep internal layers in each passport.

Use compact product features for the frontend target. For Doctrine or TypeORM, explicitly
choose a mapped rich domain model or a separate domain and persistence model
according to project needs. Do not present the user's choice as a framework ban
or requirement.

For NestJS with TypeORM, select both profiles; NestJS with another persistence
tool does not select TypeORM. TypeORM without NestJS needs no Nest profile.
Record intent methods and transaction ownership, preserving existing placement.
For Docker, include Compose-only environments and environment override files in
stack evidence. Record the dev/prod file combinations and operational owners;
importing Docker rules does not authorize running containers or deploying.

Select the execution mode, completion criteria, and risk-based verification
matrix. Do not copy “always run all CI” or “never add tests” from old instructions.
Existing mandatory gates change only through an explicit decision.

Only when model setup is part of authorized adoption or required by authorized
delegation, define workspace model routing through
[the model configuration contract](standards/model-configuration.md). Store the
selection in `.agents-framework/model-routing.toml`, which is framework state and
not native client configuration. Version-2 examples begin `unconfigured`; copying
them is not consent. When model setup is part of the authorized adoption, reuse
explicit choices and ask once for missing client, mode, enabled pairs, edges and
ceiling. An ordinary task without configured selection can run inline in the
current session without onboarding or delegation. Keep task order separate from
allowed spawn edges. Enabled specialist names use `af-<role>`; assignments come
from explicit choices and supported models, not universal IDs. Native examples
cover implementer and optional reviewer; only enabled roles are installed.

Preserve v1 choices and unknown fields; migrate only during authorized setup or
reassignment after resolving material gaps. Clarify unknown schemas before editing.
For single-agent mode, use only the coordinator, no edges and a zero framework
ceiling. Reconcile disabled managed role definitions as well as enabled pairs;
preserve unrelated roles/settings. Report controls that remain instruction policy
and distinguish saved agreement from actual model activation.

Prefer strong models for design/planning/architecture/review when the user wants
them, with separate coding/testing choices. Validate each selected effort and
model against the client/account. Catalog refresh must not change assignments.
Preserve required task ownership and checks when optional roles are disabled.

Ready for review when the target standard has no internal contradictions and
large architecture changes are divided into verifiable stages.

## Phase 3: instruction restructuring

Keep agent-facing instructions, profiles, and templates in canonical English,
with mandatory rules distinct from recommendations. A user-facing Russian README
may remain, but do not load a second Russian copy of rules into agent context.
When token comparison is useful, use an available tokenizer for the target model;
do not substitute byte counts or another unverified encoding.

For every imported project, retain the short reasoning and communication rule from
the [root AGENTS](templates/AGENTS.root.md) or [policy entry](templates/policy-entry.md):
reasoning, internal analysis, working notes, specifications and plans (including
progress/handoff records) in English; user-facing explanations, questions, progress
updates, results and final summaries in the user's language. Honor explicit requests
for a different response or artifact language without conflating the two. The
[core language policy](standards/core.md#reasoning-and-communication-language)
owns details and artifact-language exceptions. Include the short rule in an
always-loaded entry for each supported launch scope, including independently
opened repositories; a conditional route to core alone is insufficient. For Cursor,
if carried by an `.mdc` rule, use `alwaysApply: true` without file-glob restrictions.
For Claude Code, ensure the native entry or import bridge reaches that policy.
Reconcile conflicting loaded language rules and record deliberate exceptions under
the adoption policy. Pass this policy and the selected response language to roles
that do not inherit the entry, including Superpowers handoffs.

Check that prepared/applied entries contain the rule, planning instructions retain
English for specifications and plans, and their references resolve.
During an authorized client pilot, check observable response language, including
progress updates and an explicit request to switch languages. File inspection does
not establish client adherence or prove the language of hidden reasoning.

Create a short root AGENTS from the [template](templates/AGENTS.root.md). Add the
project map and conditional routes to passports and profiles. Reduce nested AGENTS
files to local constraints and links, or remove them from the chain after preserving
their required content. Use the [project template](templates/AGENTS.project.md)
when a local addition is necessary.

Retain the entries' verification default: batch code checks and functional
acceptance at phase completion, with intermediate checks only for concrete reasons
under [verification](standards/verification.md#what-to-run-and-when). Preserve required
project/CI gates, reuse valid results and carry the [compact output policy](standards/verification.md#compact-check-output)
into target routes and role handoffs. Reconcile loaded demands for tests after every
step, automatic full suites or repeated fresh runs under the conflict policy,
including applicable [Superpowers adaptations](standards/superpowers.md#explicit-adaptations).
Verify these rules survive entry adaptation for independently opened projects.

Use the selected client's supported native entry points and imports. Keep shared
policy reachable from each supported launch scope, track derived-file provenance,
and check for drift. A sentence stating that root instructions win does not
change native precedence or resolve conflicting content.

Adapt the [planning policy](templates/PLANS.md) as the root `PLANS.md`, or reconcile
an existing policy. Link it conditionally from AGENTS. For substantive tasks,
default new plain plans to workspace `docs/plans/<task>.md`; for an existing native
task, use only a navigation file pointing to its canonical artifacts. Keep its
supported store, including inside a nested project, and its single progress owner.
Record the instruction root, canonical store and execution checkout separately;
worktree creation does not relocate tasks. Verify actual native tool paths when used.
Independently opened projects retain a reachable native task entry and local policy.
An inaccessible store is a specific access obstacle; do not create a replacement.
Relocation requires a separately requested migration preserving links and native tracking;
it is not a prerequisite for adopting instructions or resuming an unrelated task.
A small local edit needs no persistent plan. Record the authorized stage,
acceptance criteria, evidence, and human checkpoint in the canonical task artifact.

Move technology explanations and long examples out of auto-loaded files. Do not
add an unconditional instruction to read every other document, which preserves
the same context cost under different filenames.

Resolve duplicate skills after comparing content and required capabilities. Do
not assume a root skill automatically replaces a same-named plugin. Choose one
coherent process and record material TDD or review differences. Do not edit an
installed plugin cache as persistent configuration or disable unrelated plugins.
Apply the [Superpowers integration policy](standards/superpowers.md), record the
selected installed version, and route from root instructions to its workflow
adaptations. Read the [compatibility reference](standards/superpowers/compatibility.md)
only for helpers in use or a version-contract question; do not preload it into
ordinary tasks. Pass applicable adaptations explicitly to delegated roles.
During the bounded pilot, check stage stopping and review of actual
uncommitted work. If OpenSpec is selected, also verify its resolved artifact paths,
task tracking, and navigation links; do not assume Markdown relocates CLI outputs.

The integration entry is the inactive
[af-integrate-project template](templates/skills/af-integrate-project/SKILL.md).
Two separate instruction-only model skills also exist:
[af-model-setup](templates/skills/af-model-setup/SKILL.md) and
[af-model-reassign](templates/skills/af-model-reassign/SKILL.md). Install only the
procedures the target workspace needs; copying a template or its unconfigured
example is not consent to model assignments. Only `af-design-change` and
`af-deliver-phase` remain conceptual here.

Use a verified native mapping for the selected client.
Codex role targets are TOML; Claude Code and Cursor role targets are Markdown with YAML
frontmatter. Preview changes to owned fields, preserve unrelated settings and
comments, and detect name collisions or edits after preview. Retain original
contents/absence for repair. Report partial writes without marking setup complete.
Validate saved agreement separately from activation; existing sessions may need
a supported reload or a new session.
For Cursor, verify native coordinator selection as described by
[model configuration](standards/model-configuration.md); do not place model
settings in project `.cursor/cli.json` or change global defaults during adoption.

When adding skills, validate their format with the supported validator, check
their links, and verify trigger precision: a relevant task selects the procedure
without making a nearby simple task run the whole process. Validate generated
TOML, Markdown/YAML, and native settings against the selected client before
activating roles. Do not run a broad benchmark
without a concrete need.

File preparation/application is ready for review when its applicable checks pass
and unresolved decisions or partial writes are explicit. During an authorized
pilot, verify that a new session from the normal root discovers the intended
instructions and selected skills, and entering a nested project selects its profile.
Verify discovery separately when a repository is commonly opened on its own.

## Phase 4: bounded pilot

This phase requires an actual target/client and authorized execution. A verified
file bundle or completion of library maintenance does not itself authorize it.

Run a small real task in the selected project: a known bug, a bounded feature, or
one independent migration step. Do not rewrite the project during initial adoption.
The coordinator works inline or delegates through the configured enabled role/edge;
it performs accountable review or uses an enabled reviewer when risk warrants independence.
Use only the specialist roles justified by the task and selected scheme.

If native settings were changed, inspect available main/subagent model and effort
information and active overrides. Check instruction discovery and checkpoint
behavior during the first authorized ordinary task. Saved files do not establish
execution evidence; keep unavailable native information unknown.

Use only the selected client. Another client's setup, reassignment, resumption
or monitoring needs its own relevant scope; do not turn instruction adoption
into a mandatory multi-client test campaign. Maintaining this library alone
does not authorize external model calls or installation into a target project.

Also exercise a short request. The agent should recover only the necessary
context, select sufficient checks, and finish without scope expansion. Do not add
artificial tests for class counts or line counts.

| Measure | Interpretation |
| --- | --- |
| Aggregate tokens for all agents, when the client reports them | The main chat alone does not represent all work |
| Time to a reviewable result | Include tool and environment waits |
| Required context and files read | AGENTS byte size is only one component |
| Checks and repetitions | A TDD repeat may be useful; an unexplained full rerun is a candidate for removal |
| Added tests and their purpose | Each test should expose a material defect or contract violation |
| Result quality | Criteria are met, contracts preserved, and regression risk assessed |

Use several comparable tasks for comparison. Compare old and new instructions
under the same saved model and effort first, then assess other configured routing
choices separately. Account for environment and cache conditions. Without reliable
data, make no percentage savings claim and do not conflate token use, price, and
subscription limits.

Ready for review when the instructions work in the client, the pilot meets its
acceptance criteria, and remaining cost drivers are understood.
Record exact tested client versions and remaining capability limits. A settings
parser or saved profile alone is not proof of runtime assignment or pilot success.

## Phase 5: architecture improvements and rollout

Application-code remediation and adoption in additional projects are separately
scoped work; they are not required merely to complete an instruction import.

Prioritize discovered violations such as `any`/`Any` leaks, thick entry points,
blurred responsibilities, duplicated object creation, oversized classes, and
implicit cross-module dependencies. Give each stage criteria, a bounded diff, and
risk-based checks. Migrating AGENTS files does not repair application code.

Move the verified standard to another project only after the user authorizes that
stage. Adapt the stack profile, versions, contract map, commands, model routing,
and exceptions. Do not copy the pilot's factual architecture into another language.
Record the framework version and project exceptions.

If a rule change regresses behavior, revert that specific change while preserving
independent user work. Do not hard-reset the repository.
