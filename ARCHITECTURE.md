# Agent_Engineering_Kit Architecture

Agent_Engineering_Kit is a source framework of engineering rules and configurable agent
role templates imported into new or existing projects. It separates durable constraints, project facts, model
routing, and task procedures. Select guidance by language, framework, database,
and technology while retaining shared responsibility and verification rules.

The repository contains English rules, conditional reading routes, examples,
research and inactive instruction/native configuration templates. Agents use
these resources inside the selected Codex, Claude Code or Cursor client.
[The scope](docs/specs/2026-09-20-agents-framework.md) defines the retained rules
framework; [engineering practices](docs/plans/2026-09-21-engineering-practices.md)
records the completed research. The former Python application was removed at
the user's request; it is not required for instruction adoption.

Existing local projects are audit subjects and migration pilots. Their code,
AGENTS files, specs, and skills are evidence of current state, not normative
architecture. The standard comes from user requirements, verified technology
capabilities, and explicit decisions.

## Components and loading

| Component | Content | When to read it |
| --- | --- | --- |
| Root instructions | Minimal mandatory rules, project map, reading routes, and completion criteria | Through the selected client's discovery rules or a supported bridge |
| Workspace `ARCHITECTURE.md` | Service roles, versions or passport links, relationships, and contract owners | When selecting a project or changing more than one project |
| Workspace `PLANS.md` | When to save a plan, its minimum content, progress, and stopping rules | When creating or resuming a substantive staged task |
| Project passport | Actual stack, target architecture, gaps, and local commands | Relevant sections for the affected project |
| `standards/` | Common, language, framework, database/technology rules, and processes | By stack and work type; never the entire directory by default |
| `.agents-framework/model-routing.toml` | Selected client, enabled roles, pairs, permitted delegation edges and concurrency | Check once if present; setup details only for authorized setup, necessary delegation choices or a relevant conflict |
| `.agents-framework/adoption.md` | Import source, selection, managed paths, accepted contents/exceptions and recovery references | Only framework import, update or recovery |
| Client-native skill directory | Installed procedures with narrow triggers; current templates target Codex | Metadata during discovery; instructions when selected |
| Current change spec or plan | Outcome, boundaries, criteria, and stages | For the corresponding task |
| `.codex/agents/`, `.claude/agents/`, or `.cursor/agents/` | Named roles in the selected client's native format | When creating the corresponding agent |

In this repository, `standards/` contains the target rules and `templates/`
contains inactive templates. The schema-v2 routing template illustrates the
coordinator, implementer and optional disabled reviewer; other roles use the same
documented contract. Native role examples remain limited to Codex. A Markdown link
does not mean the client has read a file; an instruction route or selected skill
must direct it to the relevant resource.

Distinguish the source library from each target project's adopted instructions.
Active root AGENTS/PLANS files for maintaining this library are independent of
whether its resources can be imported or are loaded in a target project. Validate
adoption there. Imported shared rules retain the core limits on speculative guards
and the verification policy's limits on redundant tests; connect them through the
target entry routes and reconcile existing mandatory checks and local contracts.

Agent-facing documentation, profiles, and templates use English as their
canonical language. A user-facing README may remain in Russian and must not be
loaded as a duplicate instruction source.

## Target workspace layout

The native directories below are alternatives selected for the client; adoption
configures one selected client as the execution system.

```text
workspace/
  AGENTS.md                         # Short mandatory entry point
  CLAUDE.md                         # Claude entry/bridge when required
  ARCHITECTURE.md                   # Project and interaction map
  PLANS.md                          # Conditional planning policy
  docs/plans/                       # New plain plans or navigation to canonical native tasks
  standards/                        # Versioned copy of selected rules
  .agents-framework/
    model-routing.toml              # Framework state; not native client config
    adoption.md                     # Import provenance; not task progress or model choices
  .agents/skills/                   # Codex procedures when selected
  .codex/
    config.toml                     # Native Codex settings when used
    agents/
      af-<role>.toml                 # Selected specialist roles
  .claude/                          # Native Claude Code configuration
    settings.json                   # Supported owned settings only
    agents/
      af-<role>.md                   # YAML frontmatter and Markdown instructions
  .cursor/                          # Native Cursor configuration
    agents/
      af-<role>.md                   # YAML model selector and Markdown instructions
    rules/                          # Selected native rules when needed
      af-<rule>.mdc
  projects-or-repositories/
    project-a/
      ARCHITECTURE.md               # Current and target state passport
      CHECKS.md                     # Check commands and conditions, when separate
      AGENTS.md                     # Optional short local addition
      <native-task-store>/          # Existing supported store; retained when present
```

Preserve real directory names; the example does not require moving repositories
under `projects-or-repositories`. For one project, the root passport can combine
the workspace map and project description. Do not maintain two identical documents.

Use the [workspace architecture template](templates/workspace-architecture.md)
for cross-project responsibilities, runtime interactions, contracts, and data
ownership. Use the [project passport](templates/project-architecture.md) for each
project's internal responsibilities and permitted code dependencies. Adapt its
flow and fields to the stack: Unreal gameplay/editor projects use engine-managed
construction and lifecycle owners rather than compulsory backend layers or custom
DI constructors. Common invariants and verification rules still apply. The
[admin/backend/ocr example](examples/document-processing-workspace-architecture.md)
illustrates the distinction; its suggested design is not a verified description
of any specific company or project.

Use the [planning policy template](templates/PLANS.md) for the target root
`PLANS.md` and the [task contract](templates/task.md) for an individual plan.
Preserve an existing specification system. The common `docs/plans/<task>.md`
entry is either the plan or a short navigation file to its native artifacts;
progress and decisions have one owner. Superpowers uses this path through an
explicit location preference; OpenSpec retains its resolved native structure.
An existing store may remain inside a nested repository. Record the instruction
root, canonical artifact location/progress owner and execution checkout separately;
a new worktree does not change task ownership. A tracked copy in another checkout
does not become another editable progress record. Verify native tool paths when
used; relocation is a separately requested migration. If the canonical task cannot
be accessed, report that obstacle without creating a divergent replacement.
`PLANS.md` defines the process; it is not a backlog or the plan for every task.
Unlike AGENTS instruction discovery, architecture and planning files require
explicit reading routes. Merely creating them does not load their contents.

## Adoption boundaries

Adoption is a reviewed instruction/configuration change. Select applicable rules,
reconcile existing instructions and adapt native templates to the installed
client's supported format. Preserve unrelated settings and user work. Keep the
saved model/effort choice separate from native settings and runtime evidence.

[MIGRATION](MIGRATION.md#import-inputs-and-boundaries) owns the single preparation
and application procedure for new projects, existing projects and updates. A skill
or native entry routes into that procedure; it does not define another import
lifecycle. Resolve source, selected target roots/checkouts, client and intent before
dependent work. Preparation only produces a reviewable preview outside the target;
authorized application preserves originals and reconciles intervening edits first.

| Concern | Authoritative owner |
| --- | --- |
| Import steps and treatment of active conflicting rules | MIGRATION; native client precedence and higher-priority instructions still apply |
| Bundle availability and task-specific reading | Catalog contract and selected profile routes |
| Imported provenance, owned scope and accepted contents/exceptions | Target adoption record, adapted from the available template |
| Actual commands, gates, versions and product contracts | Target local entry/passport/check document; preserve accepted exceptions |
| Adoption decisions, permission, progress and evidence | Existing canonical adoption task; keep its native store and single progress owner |
| Saved model choices and activation | Model-configuration contract and native client; import alone triggers no setup |

Replace conflicting generic process rules in the sources actually loaded; preserve
required local contracts with reachable owners before retiring old content. A rule
outside the authorized scope remains an explicit unresolved conflict. Reconciliation
does not change native precedence. Neither importing instructions nor selecting a
profile authorizes code remediation, version upgrades or edits to other projects.
File verification and observed client discovery/adherence are distinct results;
a target pilot needs its own execution scope.

The [adoption-record template](templates/framework/adoption-record.md) is inactive
until adapted in an authorized target. It identifies managed scope and references
accepted adapted contents and recoverable originals. Keep comparison/recovery
material outside active instruction/skill discovery. Update only recorded scope,
preserving independent edits; source names alone grant no ownership. The
[repeat/update](MIGRATION.md#repeat-and-update) and
[partial-recovery](MIGRATION.md#partial-application-and-recovery) contracts own the
details. A matching repeat needs no rewrite; partial state cannot be claimed verified.

Each independently opened repository needs reachable rules and local entry
instructions. Role files that skip normal project discovery must receive the
relevant policy explicitly. Ordinary development takes place in the native
client using its own authentication, controls and status interface.

## Instruction precedence and project boundaries

Codex collects instructions from the project root toward the working directory;
a closer AGENTS file can override an ancestor. `AGENTS.override.md` replaces the
ordinary AGENTS file at the same level rather than making the root file stronger
than every descendant. If no project root is found, discovery checks only the
current directory. These are properties of
[Codex AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md),
and wording inside Markdown cannot change them.

Claude Code has its own instruction discovery and settings precedence. Select
native `AGENTS.md` support or a `CLAUDE.md` import bridge by verified capability;
check required rule loading for specialist roles separately. The version-specific
evidence and sources are in the
[research note](docs/research/2026-09-20-native-agent-orchestration.md).

Cursor requires reconciliation of AGENTS, selected `.mdc` rules, and native or
compatibility agent definitions. Verify the effective role set and independently
opened repositories rather than assuming only `.cursor/` is discovered.

The framework's organizational order is: shared standards define policy; local
documents contain stack facts, commands, and explicitly accepted exceptions.
Migration removes conflicting local instructions. Move long local guidance into
ordinary reference files with conditional reading routes. Do not leave opposing
rules in place and rely on a statement that “the root wins.”

Opening the shared workspace matches the user's normal workflow. When an agent
enters a nested project, it checks only that project's relevant instructions and
passport. If that project is later opened independently, a parent outside its
discovery boundary cannot be assumed to load; the project needs an accessible
copy or supported reference to the standard and its own short entry point.
Its local planning route also reaches its native task entry without requiring
parent discovery or creation of a workspace navigation file.

For each selected repository, copy only applicable rules and their referenced
resources, then adapt a short entry document with task-specific reading routes.
The [catalog guide](standards/catalog.md) defines rule IDs, applicability and
bundle dependencies. Dependencies and shared `required` profiles keep resources
available; their presence does not require reading them for every task. Use the
actual stack, task conditions and profile routes to choose sections. The catalog
is an index, not an installer.
Use the adoption record for source/content identity and accepted local exceptions;
entry/passport provenance points there. Review diffs when
updating copies and preserve independent edits. Native role configuration and
actual instruction loading must be checked in the selected client when adopting
those files; merely writing a link does not load its target.

## Work modes and checkpoints

The default is direct mode in the current directory and checkout. Do not create
branches, worktrees, commits, stashes, or staged changes as routine bookkeeping.
Complete one small logical stage, run necessary checks, report its result and
limitations briefly, propose the next stage, and stop for user review. Do not implement
the next stage in the background while the checkpoint is pending.

An explicit user request can enable autonomous worktree execution for a task.
Permission to use a worktree does not by itself authorize commits, integration,
pushes, or deployment. Record each granted Git action separately and preserve
uncommitted user work. At completion, offer the concrete merge; after the approved
merge and necessary checks succeed, remove the worktree when no work would be lost.
Branch deletion is a separate permission. See [work modes](standards/work-modes.md) for the complete
contract and [proportionate verification](standards/verification.md) for evidence
and review rules.

## Workspace model routing

Model selection and execution mode are independent. Store the intended workspace
selection in `.agents-framework/model-routing.toml`; this is a framework-owned
state file, not a native client configuration file. Profile examples start as
`unconfigured` and contain suggestions rather than universal assignments.

If selection is absent/unconfigured, ordinary work runs inline in the current
session without a questionnaire, profile writes or delegation. For explicit setup
or choices required by delegation, ask only for material missing client, mode,
enabled pairs, edges and ceiling. Reuse choices already supplied; do not repeat
onboarding after a new conversation or ordinary task. The target roles
include orchestrator, architect, planner, explorer, implementer, test runner,
and reviewer. Specialist native names use `af-<role>`; only the selected roles
are installed. Their pairs come from saved choices, not framework-wide IDs.
The existing `af-implementer` and `af-reviewer` templates are a limited baseline.

Version 2 explicitly represents single-agent or delegated mode. Disabled roles
cannot be invoked through native definitions or anonymous worker defaults. Version 1
remains readable without automatic migration; missing enablement/edges stay unknown
until resolved for authorized configuration or a required handoff. Unknown versions
require clarification before editing or delegation. Adoption provenance belongs to
the adoption record, separate from saved model choices and local operational facts.

Keep role assignments, delegation relationships, and task ordering separate.
A coordinator can launch implementation, testing, and review sequentially
without nesting workers. Presets are editable; their existence does not require
all roles to run. Validate client-specific nesting and concurrency capabilities.
Project instructions and scoped skills guide the selected progression; role
configuration alone does not enforce a pipeline.

Refresh catalogs without automatically reassigning roles. Preserve unrelated
native settings and report when saved selection, active configuration, and
runtime-reported model differ. Reports must retain unknown/stale values where
execution evidence is absent.

The full setup, native-file mapping, reassignment, and validation contract is in
[workspace model setup](standards/model-configuration.md).

## Skill design

Superpowers is the selected development toolkit. Its full skill catalog remains
available, while the [integration policy](standards/superpowers.md) defines
conditional use and adaptations to the user's stages, permissions, and checks.
OpenSpec may own change artifacts while Superpowers provides development skills.
The [compatibility reference](standards/superpowers/compatibility.md) owns dated
version evidence and helper contracts; load it only for helper use or compatibility
investigation. Ordinary tasks use the common policy and selected procedure.
If the toolkit or a helper is unavailable, use the policy's direct scoped-task
fallback; only a genuinely required missing capability blocks dependent work.

Technology profiles can describe different integration models, not only languages
or libraries. Unreal is an engine/editor environment with engine-owned lifecycles,
reflection/serialization, binary assets, World/PIE state and cook/package boundaries.
Its profile maps shared principles to those contracts; backend/frontend layering,
DTO/service construction and verification routines are not automatic defaults.
Common scope, invariants, permission and evidence rules remain binding.

Profiles are constraints, not automatically triggered skills. The
`unreal-engine` profile keeps its complete mandatory editor workflow in portable
rules; a compatible installed skill is optional. Its six resources are available
as a bundle and read by task, without forcing MCP setup for source-only work.
No local engine/provider availability follows from selecting the profile.
Skills describe concrete procedures. The current catalog distinguishes implemented
instruction-only templates from conceptual procedures:

| Name | Narrow trigger | Status and resources |
| --- | --- | --- |
| `af-model-setup` | Explicit model setup or missing choices required by authorized delegation | Existing [template](templates/skills/af-model-setup/SKILL.md); absence of a record alone does not trigger it |
| `af-model-reassign` | Explicit change to saved client, roles, pairs or delegation choices | Existing [template](templates/skills/af-model-reassign/SKILL.md); not installed automatically |
| `af-integrate-project` | Explicit framework preparation/import/update request | Existing [template](templates/skills/af-integrate-project/SKILL.md); routes to MIGRATION; ordinary coding or missing files do not trigger it |
| `af-design-change` | An architectural boundary, public contract, or complex behavior changes | Conceptual; would use affected architecture, profiles, and a task template |
| `af-deliver-phase` | User authorizes execution of a defined plan stage | Conceptual; would use the stage contract, selected profiles, work mode, and verification process |

An instruction-only template is inactive for native discovery until adopted through
the selected client's supported mechanism. An agent can explicitly read the source
template before installation. The integration entry resolves MIGRATION/catalog
from the accessible framework source supplied by the request or adoption record;
it does not assume those files were copied to the target. Its proposed local layout
and reference bases are defined in [MIGRATION](MIGRATION.md#integration-entry-and-location).
Keep a skill's frontmatter and procedure short, with reachable references to
the resources it needs. Its description defines the trigger; it must not force
every task to load the entire stack. Shared rules retain one owner instead of
being copied into each skill.

Package skills with portable relative paths or an explicitly resolved source root,
never hardcoded author-machine paths. Check each reference from its declared base.
Choose one source for a procedure rather than installing same-named copies from
plugins and user directories. Use native client controls for enablement. A skill's
directory does not give it special instruction precedence.

[Codex Skills](https://learn.chatgpt.com/docs/build-skills) describes progressive
loading of metadata, instructions, and resources. The size of the reference
library therefore need not equal the context used for every task; precise reading
routes matter.

## Context budget and updates

Do not load the complete README, archived specs, every skill, or every profile
before each task. Use targeted search and reads, and keep command results concise.
When the topic changes, retain current decisions, paths, and verification state.
Do not discard material user constraints to shorten a handoff.

API token cost depends on model and token category, not alphabet. Equivalent text
can still tokenize differently by language and tokenizer. Measure with the target
model's tokenizer when a comparison matters; byte, character, and word counts are
not token counts. No specific savings claim is made here. See
[OpenAI: Understanding and counting tokens](https://help.openai.com/en/articles/4936856-understanding-and-counting-tokens).

As a working guideline, keep a root AGENTS file near 40–70 substantive lines and
a local addition near 10–25. These are signals, not quotas or token guarantees.
Never remove a critical rule merely to meet them. Increasing
`project_doc_max_bytes` is not a context-saving strategy.

When correcting repeated agent behavior, update the rule that owns it instead
of appending another overlapping mandate. Remove stale duplicates and reconcile
conflicts across AGENTS, skills, and role instructions. Keep skill descriptions
short with specific triggers; large or overlapping catalogs can obscure selection.
Recheck the affected workflow when changing models: instructions useful to one
model may cause another to over-test or stop too early. Preserve the user's
explicit stage checkpoints. See
[OpenAI's guidance on skills and prompts](https://learn.chatgpt.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra).

Each adopted workspace records the framework source/content identity in its adoption
record. Update it by reviewing the
diff and project exceptions; a change to personal global rules must not silently
alter every repository's architectural decisions.

The adoption sequence is in [MIGRATION.md](MIGRATION.md), engineering constraints
are in the [core profile](standards/core.md), execution is defined by
[work modes](standards/work-modes.md), and evidence by
[verification](standards/verification.md).
