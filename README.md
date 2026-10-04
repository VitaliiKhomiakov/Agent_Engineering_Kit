# Agent_Engineering_Kit

**Engineering standards, project instructions, and workflows for AI coding agents.**

Agent_Engineering_Kit is a reusable library for guiding coding agents in Codex, Claude
Code, and Cursor. It brings together architecture and coding rules, proportionate
verification, project documentation templates, and configurable agent roles.
Adopt the resources that match your project's stack in a new or existing workspace.

The library consists of Markdown instructions, a TOML catalog, and inactive
configuration and skill templates. Adoption happens through an agent following
[the integration procedure](MIGRATION.md); no package installation, dedicated CLI,
or application runtime is required.

## What it provides

- **Shared engineering standards:** responsibility boundaries, domain invariants,
  explicit contracts, practical abstractions, and limits on speculative code.
- **Technology profiles:** focused guidance for backend, frontend, persistence,
  containers, and Unreal Engine projects, with topic sections and examples.
- **Project entry points:** short `AGENTS.md` instructions that route agents to
  relevant rules, architecture, and planning documents.
- **Delivery and verification policies:** small logical stages, human checkpoints,
  checks chosen for the affected behavior, and reuse of still-valid evidence.
- **Optional agent orchestration:** selected roles, model/reasoning-effort pairs,
  permitted delegation relationships, and concurrency limits.
- **An adoption procedure:** preparation, import, updates, conflict resolution,
  provenance tracking, and recovery that preserves local changes.

Rules, templates, and this README are written in English. The shared
[language policy](standards/core.md#reasoning-and-communication-language) calls for
English analysis, working notes, specifications, and plans, while user-facing
communication follows the user's language. An explicit request for a different
response or artifact language takes precedence for that material.

## Getting started

Keep an accessible copy of this library and identify the target project and one
client: Codex, Claude Code, or Cursor. You can ask the agent to read the integration
skill directly from the source; global skill installation is unnecessary.

To preview adoption, replace the placeholders in this request:

> Read `templates/skills/af-integrate-project/SKILL.md` from the Agent_Engineering_Kit
> source at `<framework-path>`. For the project at `<project-path>` using
> `<client>`, prepare an import of the applicable rules. Show the proposed file
> changes and conflict resolutions. Leave the target project untouched.

Preparation produces a concrete change set: selected profiles, destination paths,
proposed contents, retained local constraints, conflict decisions, and checks.
It creates no files or adoption record in the target project.

To apply a reviewed proposal:

> Apply the prepared Agent_Engineering_Kit import to `<project-path>` for `<client>`
> within the reviewed scope. Preserve unrelated changes and existing model choices,
> and follow the agreed checkpoints.

An explicit import request can already authorize the relevant changes; the
procedure reuses that authorization. Model setup and a live client pilot have
separate scopes.

The [integration skill](templates/skills/af-integrate-project/SKILL.md) follows
[MIGRATION.md](MIGRATION.md), which defines the full procedure:

1. Inspect the actual stack, active instructions, local contracts, and client
   capabilities. For a new project, record the intended architecture as proposed.
2. Select profiles from the [catalog](standards/catalog.toml), including shared
   required policies and the selected profiles' dependencies and resources.
   New imports put `standards/` and inactive `templates/` under `.agents-framework/`;
   root project documents and active native files retain their agreed locations.
3. Adapt entry and architecture templates. Reconcile conflicting instructions
   in the files the client actually loads while preserving required project checks.
4. Apply the authorized changes, retaining originals and accounting for edits
   made since preparation.
5. Validate the adopted references and record the import in
   `.agents-framework/adoption.md`, using the [adoption record template](templates/framework/adoption-record.md).

The adoption record tracks source identity, managed files or sections, accepted
contents, exceptions, and recovery information. Updates compare these with local
changes. Read this record for import, update, or recovery; task progress and model
assignments retain their own documents. Keep the framework source accessible for
future updates.

The source library layout stays unchanged. Existing flat imports remain supported;
an ordinary update does not relocate them. For a selected move, follow the
[layout and relocation contract](MIGRATION.md#layout-and-path-contract), preserving
local edits and immutable old accepted snapshots. Portable optional source routes
use known URLs or labelled source paths through provenance, not author-machine links.

## Choose rules by the actual stack

Start with the affected concern and the relevant profile. A combined profile
applies only the components used in the project: Python does not imply FastAPI,
React does not imply Next.js or TypeScript, and Angular does not imply NgRx.

| Area | Entry points |
| --- | --- |
| Common engineering | [Core standard](standards/core.md), [delivery workflow](standards/delivery-workflow.md), [verification](standards/verification.md) |
| Python | [Python / FastAPI / Pydantic](standards/python-fastapi.md), [SQLAlchemy](standards/sqlalchemy.md), [Psycopg](standards/psycopg.md) |
| PHP | [PHP / Symfony / Doctrine](standards/php-symfony-doctrine.md) |
| Go | [Go / Gin](standards/go-gin.md) |
| JavaScript and TypeScript | [JavaScript / Node.js](standards/nodejs-typescript.md), [TypeScript](standards/typescript.md) |
| NestJS and TypeORM | [NestJS](standards/nestjs.md), [TypeORM](standards/typeorm.md) |
| React and Next.js | [React / Next.js](standards/nextjs.md), [feature structure](standards/nextjs-feature-structure.md) |
| Angular and NgRx | [Angular](standards/angular.md), [NgRx](standards/ngrx.md) |
| Database and containers | [PostgreSQL](standards/postgresql.md), [Docker](standards/docker.md), [development and production environments](standards/docker/development-production.md) |
| Unreal Engine | [Unreal Engine](standards/unreal-engine.md), [optional Unreal / Blender / MCP skills](standards/unreal-engine/skills.md) |

The [catalog guide](standards/catalog.md) distinguishes **bundling** from
**reading**. The `required`, `dependencies`, and `resources` fields determine which
files remain available in an adopted bundle. The task, actual stack, and `when`
conditions determine what the agent reads. Availability does not require loading
every profile, example, research note, or historical plan into each session.

These profiles contain opinionated project standards. Numeric size limits,
layering preferences, and testing policies are local engineering choices;
references to technology documentation do not make them universal requirements.
Apply guidance against the target project's actual versions and architecture.

For example, the Doctrine and TypeORM guidance makes domain-model placement an
explicit project decision. Angular and NgRx guidance selects state ownership and
reactivity tools by the feature's needs. Docker guidance covers both dependency-only
Compose setups and containerized applications, including development/production
separation.

Unreal uses an engine and editor model: lifecycle, reflection, garbage collection,
assets, unsaved editor state, and cooking affect how the shared principles apply.
Its topic resources are listed in [the catalog](standards/catalog.toml) and read
by task. Blueprint-only work does not require
C++, source changes do not require MCP, and backend service patterns are not
mandatory gameplay architecture. Blender-to-Unreal work verifies the relevant
import result in the engine. See the [Unreal profile](standards/unreal-engine.md)
for the applicable routes and checks.

## Working model

### Small stages and explicit checkpoints

The default [work mode](standards/work-modes.md) uses the current project directory.
The agent completes one small logical stage, runs the necessary checks, reports
its result, and pauses for human review. Routine work does not create commits,
stage files, create branches or worktrees, or stash changes.

Autonomous worktree execution can be selected explicitly. Permission for commits,
integration, push, and pull requests is handled separately. Cleanup follows an
approved successful merge and checks that changes have been preserved; branch
deletion, push, and deployment need their own authorization.

### Verification proportional to the change

The [verification policy](standards/verification.md) chooses checks for the affected
behavior and its risks while retaining mandatory project and CI gates. Documentation
changes normally need artifact checks; executable examples or behavior changes may
need focused tests.

Checks run together at the boundary selected by `verification.timing` under
[policy configuration](standards/policy-configuration.md). Earlier checks are
appropriate for reproducing a bug, resolving a concrete uncertainty, validating a
risky dependency, selected TDD, or a required gate. After a fix, rerun affected
checks and reuse results whose inputs remain valid. Keep summaries compact and
retain detailed failure logs separately.

Shared [policy defaults](standards/policy-defaults.toml) own cadence/review choices,
size-review thresholds and soft instruction-length ranges. An adopted project may
provide sparse overrides at `.agents-framework/policy.toml`; absence needs no setup.
The checker validates schema and merged constraints. These settings preserve
mandatory checks, acceptance and permissions; they are not model configuration or
limits on test/review counts.

### Architecture and plans with clear ownership

In an adopted workspace:

| Document | Responsibility |
| --- | --- |
| `AGENTS.md` | Mandatory constraints, component map, completion criteria, and conditional reading routes |
| `ARCHITECTURE.md` | System structure, responsibilities, interactions, and project facts |
| `PLANS.md` | When and how to create, maintain, and resume task plans |
| `docs/plans/<task>.md` | Default location for new ordinary Markdown plans, or navigation to an existing canonical task |

Preserve existing OpenSpec, Spec Kit, or other supported task stores in their
canonical locations, including inside nested projects. Keep decisions and progress
in one authoritative place. Changing the implementation checkout or using a
worktree does not move the task's owner. A small edit needs no separate plan file.

Independently opened repositories need reachable local instructions and selected
rules. Use the [root entry](templates/AGENTS.root.md),
[local addition](templates/AGENTS.project.md),
[project architecture](templates/project-architecture.md), and
[workspace architecture](templates/workspace-architecture.md) templates as needed.
The [planning policy](templates/PLANS.md) and [task contract](templates/task.md)
cover substantive work.

### Optional delegation and model configuration

Ordinary work can proceed inline with the current agent when no routing profile is
configured. Model setup is triggered by a request or a missing choice needed for
necessary delegation; having a plan or a role template does not require subagents.

The [model configuration policy](standards/model-configuration.md) defines
`.agents-framework/model-routing.toml`. Version 2 records the client, enabled
roles, model/effort pairs, permitted delegation relationships, and agent limit.
Version 1 choices remain readable and migrate during authorized setup or
reassignment.

- **Single-agent mode:** only the coordinator is enabled; specialist roles and
  delegation relationships are absent, and the framework subagent limit is zero.
- **Delegated mode:** only selected, enabled roles and permitted relationships
  may be used, within the saved limit. A disabled reviewer is not replaced by an
  unnamed worker.

Use the [setup skill](templates/skills/af-model-setup/SKILL.md) or
[reassignment skill](templates/skills/af-model-reassign/SKILL.md) for the respective
operation, following the [orchestration policy](standards/orchestration.md).
Values in the [routing template](templates/framework/model-routing.toml) are
unconfigured examples. Saved choices must be reconciled with supported native
settings; writing a file does not switch an already-running model.
Full integration includes a required [model-selection decision](MIGRATION.md#model-selection-step):
reuse consistent choices, prepare authorized setup, retain an explicit deferral
or report an unresolved step. Ordinary coding does not trigger this workflow.

### Superpowers integration

[The Superpowers policy](standards/superpowers.md) maps skills to relevant tasks
and adapts their workflows to the project's checkpoints, Git permissions, model
choices, planning locations, and verification policy. Installing the plugin alone
does not activate these adaptations.

When the plugin is absent or a helper is unsuitable, a bounded task can follow its
canonical plan directly with the necessary checks and review. Use the
[compatibility notes](standards/superpowers/compatibility.md) when a helper or an
installed-version contract needs investigation.

## Client integration

The library provides instruction routes and templates for three clients. Verify
discovery and supported settings in the selected client and version during adoption.

| Client | Included resources |
| --- | --- |
| Codex | `AGENTS.md` templates, [native configuration and role examples](templates/codex/README.md), integration and model-selection skills |
| Claude Code | A [policy bridge template](templates/claude/policy-bridge.md) and adoption guidance for native instruction/configuration mapping |
| Cursor | A [rule route template](templates/cursor/rule-route.mdc) and adoption guidance for native rules, role discovery, and configuration mapping |

Ready-made native role examples are currently supplied for Codex. Other client
mappings follow the integration procedure and require capability checks. Preserve
unrelated settings and roles, and resolve conflicting loaded instructions at their
actual locations. A statement that root rules have priority does not change a
client's native instruction precedence.

Templates are inactive until adapted and installed. Copying a skill does not prove
that the client discovers it, and valid configuration syntax does not prove that
the intended model or reasoning effort is active.

## Repository map

```text
Agent_Engineering_Kit/
├── AGENTS.md                  # Instructions for maintaining this source library
├── README.md                  # Overview and adoption entry point
├── ARCHITECTURE.md            # Design of this rules library
├── MIGRATION.md               # Preparation, import, updates, and recovery
├── standards/
│   ├── catalog.toml           # Profiles, dependencies, resources, and templates
│   ├── catalog.md             # Bundle selection and conditional reading semantics
│   └── ...                    # Shared policies, stack profiles, topics, and examples
├── templates/
│   ├── AGENTS.root.md         # Short workspace entry
│   ├── AGENTS.project.md      # Project-local addition
│   ├── PLANS.md               # Planning policy
│   ├── codex/                 # Inactive native configuration and role examples
│   ├── claude/                # Policy bridge
│   ├── cursor/                # Rule route
│   ├── framework/             # Adoption record and model routing templates
│   └── skills/                # Integration, model setup, and reassignment procedures
├── examples/                  # Illustrative workspace architecture
└── docs/
    ├── specs/                 # Scope and design decisions
    ├── plans/                 # Implementation and verification records
    └── research/              # Sources, version context, and evidence limits
```

The root [ARCHITECTURE.md](ARCHITECTURE.md) describes this library, and
[AGENTS.md](AGENTS.md) guides agents maintaining its source. Target-project entry
and planning files remain inactive templates; no root `PLANS.md` or client
configuration is installed by this maintenance entry. Target adoption is verified
in each target workspace independently.

## Status and verification limits

The recorded library work is complete for the instruction-framework refinement,
project integration procedure, Unreal support, and Angular/NgRx profiles. The
library is prepared for a scoped pilot in a selected target project.

| Evidence | Scope |
| --- | --- |
| [Framework refinement](docs/plans/2026-09-26-instruction-framework-refinement.md) | Recorded structural checks and acceptance scenarios |
| [Readiness review](docs/plans/2026-09-27-framework-readiness-review.md) | Static library readiness, selected bundles, instruction routes, and role contracts |
| [Project integration](docs/plans/2026-09-27-project-rule-integration.md) | Recorded preparation, import, update, and recovery acceptance checks |
| [Unreal support](docs/plans/2026-09-27-unreal-engine-support.md) | Profile, template, and routing checks; engine/editor execution remains unverified |
| [Angular and NgRx](docs/plans/2026-09-29-angular-ngrx-rules.md) | Profile/catalog consistency and documented checks for conditional applicability |
| [Superpowers compatibility](standards/superpowers/compatibility.md) | Bounded local-source checks for 6.4.2; historical 6.4.1 results are retained separately |

These records establish the stated library checks. They do not establish
successful end-to-end adoption in every client, token savings, active model
assignments, or Unreal build/editor behavior. A target-client pilot after these
changes remains unverified in the recorded evidence.

A pilot should select one project and client version, define any required model
assignments and permitted configuration changes, and observe instruction loading,
a small inline task, justified delegation if selected, checkpoints, and resumption
from canonical task documents. Compare efficiency only on comparable tasks with
the same model and reasoning effort.

When changing the library, run `python3 tools/check_instruction_artifacts.py`
(Python 3.11+, standard library only) for catalog, local-link, fence and TOML checks.
See [maintenance verification](docs/maintenance/verification.md) for scoped commands,
checker tests, syntax limits and example reproduction. Also review affected YAML
and instruction consistency. Validate executable examples with
the relevant stack when their behavior changes. There is no standalone framework
application or application test suite in this repository.
