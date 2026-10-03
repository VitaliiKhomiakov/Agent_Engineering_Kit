# Adopted engineering policy

Template: replace `$projects` and `$routes`, copy selected rules, and resolve links
from this entry. Fill selected-profile routes with actual paths. Child repositories
opened independently need reachable policy copies. Preserve local contracts/checks
and resolve opposing instructions explicitly; native instruction precedence applies.

## Reasoning and communication language

Use English for reasoning, internal analysis, working notes, specifications and
plans, including their progress/handoff records. An explicit user request for a
different artifact language takes precedence. Write user-facing explanations,
questions, progress updates, results and final summaries in the user's language,
following an explicit response-language request or otherwise the latest substantive
request. Code, quotes and tool output do not change that choice. Preserve technical
literals and existing conventions for other code/documentation.
See the [language policy](standards/core.md#reasoning-and-communication-language).

## Scope, permissions and evidence

Work within the authorized task and current checkout. Default: one logical stage,
necessary checks, then the user's checkpoint; no staging, commits, branches, stashes
or worktrees. [Work modes](standards/work-modes.md) owns explicit exceptions and integration.
Keep transport entry points thin, validate external input and use strict typed boundaries.
Engine-managed gameplay follows its selected profile's lifecycle and composition;
do not force backend layers or custom DI constructors onto engine-created objects.
Use [core task routes](standards/core.md#read-by-task) for detailed engineering decisions.
Before edits preserve original contents/absence and user work. Reuse valid coverage;
add tests for material uncovered behavior. Batch code and functional checks at phase
completion (or completion of a bounded unphased change). Intermediate checks need
a bug, concrete uncertainty, risky dependency, selected TDD or required gate.
Preserve required project/CI checks; full suites need a gate or concrete impact/risk.
Repeat only for changed inputs, failures or concrete concerns. Name the reason for
early/repeated checks; final reporting or a handoff does not invalidate evidence.
Use concise summaries and relevant failure details; retain full noisy logs and actual
exit status under the verification policy. Report actual results and limits.
[Verification](standards/verification.md) owns baseline, scoped review and evidence.

## Projects and reading routes

Version/passport declarations are evidence, not proof of installed versions.
Record check commands with triggering conditions.

$projects

Start with the selected profile entry and only its applicable sections. Catalog
`required`/dependencies describe bundle availability, not a reading queue. Actual
stack and task control reading: JavaScript React excludes TypeScript/unused Next.js;
Python alone excludes FastAPI/Pydantic. Unreal context selects `standards/unreal-engine.md`;
read only its task routes, without mandatory C++ detail for Blueprint-only work or
MCP setup for a source-only change. Generic C++ alone does not select Unreal.
Examples/research are optional; stop when
relevant rules are known. Bundle changes use the [catalog guide](standards/catalog.md).

$routes

## Planning, skills and roles

Explicit framework import/update/preparation uses `af-integrate-project` at
`<actual installed or accessible source skill path>`. Adoption provenance and
accepted exceptions belong to `.agents-framework/adoption.md`; read it only for
import/update/recovery. Ordinary work or missing instruction/model files does not
trigger integration. Keep applicable local constraints in their operational owners.

Use the existing planning convention, otherwise the [plan rules](templates/PLANS.md)
and [task template](templates/task.md). Preserve the canonical task store; workspace
navigation adds no second checklist. Record the store separately from the execution
checkout. Relocation is a separate requested migration. Templates are inactive;
do not initialize Git for bookkeeping. Planning alone does not select delegation or model setup.
Use available skills through the [Superpowers policy](standards/superpowers.md);
helper references are conditional and direct scoped execution remains available.
Reuse a consistent saved model selection. Missing/unconfigured selection permits
ordinary inline work without onboarding, profile writes or delegation; respect known
explicit choices. [Model configuration](standards/model-configuration.md) owns explicit
setup/reassignment, required delegation choices, legacy/unknown records and conflicts.
Saved/example settings do not prove active execution. [Orchestration](standards/orchestration.md)
owns fresh scoped handoffs: pass applicable policy to roles that omit this entry.
Use enabled roles, selected pairs, allowed edges and the ceiling; single-agent mode
forbids delegation. Role definitions alone do not authorize invocation.
