# Orchestration and configurable model roles

Use the saved client's enabled roles, model/effort pairs, allowed edges and
concurrency ceiling. Read
[model configuration](model-configuration.md) for setup, reassignment, or a
runtime/configuration conflict; it owns selection and native mapping.
Do not silently substitute a model or effort.

Without a configured selection, an ordinary task can run inline in the current
session without setup or delegation. If a required handoff lacks explicit choices,
resolve those before spawning and continue independent work. The
[format contract](model-configuration.md#routing-format-version-2) owns version 2
and legacy handling; a recorded pair or role file alone is not permission to spawn.

Orchestrate inside the one selected installed client using its native mechanisms
and existing account access. The schemes below are instructions for the
coordinator; inactive native templates provide starting points for configuration.

## Responsibilities

| Role | Work | Output |
| --- | --- | --- |
| Orchestrator | Coordination, risk, delegation, progression, routine review | Bounded contract and accountable decisions |
| Architect, when useful | Design, architectural boundaries, and contracts | Justified design and constraints |
| Planner, when useful | Break an agreed design into actionable work | Plan with dependencies and acceptance criteria |
| Explorer, when useful | Inspect relevant code, stack, and evidence | Findings and focused references |
| Implementer | Assigned implementation and necessary checks | Changes, evidence, questions |
| Test runner, when useful | Test design, execution, or result investigation | Necessary checks and interpreted evidence |
| Reviewer, when warranted | Independent assessment of a completed scope | Concrete findings or no unresolved material finding |

The coordinator's routine review is not an independent second opinion. Do not
start another planner for a task already planned or create agents merely because
roles exist. Delegate bounded implementation; a tiny edit needs only a short
handoff. Responsibilities may remain with the coordinator in a small task;
separate architect/planner/test roles are independently configurable when useful.
Running a test command alone does not require another LLM. In selected single-agent
mode, the coordinator owns these responsibilities; specialists are disabled,
the ceiling is zero and no edges are permitted.

## Editable schemes

Separate the selected role/model/effort pairs, permitted delegation relationships,
and task progression. The user's coordinator-with-specialists examples are
starting profiles, not fixed model assignments or mandatory agent counts.
Changing a model preserves the scheme; changing a scheme preserves unrelated
choices and mandatory project checks.

For each handoff, confirm delegated mode, both enabled endpoints, the allowed
`parent->child` edge, selected pair, remaining concurrency and task authorization.
Do not replace a disabled role with a generic worker/default pair. Disabled optional
roles leave their required responsibilities with the coordinator; a required
independent opinion still needs an enabled role or a clarified assignment.

The default proposed structure has the main coordinator launch selected direct
children. Exploration, design/planning, implementation, tests, and review can
be sequenced through it. A dependency between stages is not permission for a
worker to spawn another worker. Literal nesting requires an explicit selected
edge and supported client/version limits. Return of findings is a report to the
coordinator, not a reverse spawn edge or a cycle in the delegation graph.

Record step conditions, required inputs/outputs, correction handoffs, and human
checkpoints. Reject missing roles and forward dependency cycles. Review findings
return to a bounded correction stage; they do not create unlimited retries or
remove stage permissions. Disabling an optional agent must not remove required
checks or leave a required responsibility without an owner.

Native role files configure workers. Project instructions and selected skills
guide the coordinator's progression. Do not claim that saving a scheme makes
the order mechanically enforced unless a supported control has been verified.

## Delegation contract

Give the implementer:

- Outcome, acceptance criteria, and material user constraints.
- File/component ownership and relevant neighboring contracts.
- Workspace/instruction root, project/repository-to-checkout mapping, absolute
  canonical plan/spec/store paths and progress owner, and pre-stage baseline.
  Include the supported native tool context when different from the execution checkout.
- Applicable workspace/project instructions and only needed profiles.
- Work mode, current stage, human checkpoint, and allowed Git actions.
- Verification approach, commands, dependencies, and known blockers.
- Expected report: changed paths, acceptance, evidence, deviations, and obstacles.

Pass focused references and decisions, not the full conversation or large logs.
Explicitly disable history inheritance with `fork_turns: "none"` when supported,
or the client's equivalent fresh context. A short prompt does not override a
full-history default. If this control is absent, report the limitation and use
the narrowest supported context. Never invent parameters or omit the user's
authorization and requirements. Workers need a specific authorized reason to
spawn further agents.
Keep decisions/progress with the supplied canonical owner; a checkout copy or
temporary brief is not another task ledger. Report an inaccessible store before
dependent work rather than creating a replacement or relocating the task.

For review, supply the same mapping, task changes, baseline, criteria, valid
evidence, and concrete regression questions. Read [review boundaries](verification.md#review-boundaries)
for scope and findings; do not assign incidental unrelated bugs to new workers
without scope authorization.

## Concurrency and isolation

The configured ceiling is not a target; the initial suggestion is two spawned
agents excluding the main agent. Sequential execution is normal. Parallel tasks
need independent results and clear ownership. Avoid concurrent writers to the
same files or tests competing over ports, databases, and fixtures; preserve others' work.

Use the directory mapping and isolation rules in [work modes](work-modes.md#workspace-root-and-project-checkouts).
A non-Git workspace root does not prevent authorized worktrees for nested projects.
Workers stay within the current stage at a human checkpoint. Review a stable
completed scope; after combining independent changes, check affected interactions.
Separate branch checks do not establish integration correctness.

## Runtime behavior

[Codex role templates](../templates/codex/README.md) are inactive examples. Supported
Codex clients may load `.codex/agents/`; Claude Code and Cursor use their native
Markdown/YAML role formats. Their model/effort mappings are client-specific; see
[model configuration](model-configuration.md).
Interfaces exposing only model/effort require that saved pair plus role
instructions. Verify actual capabilities and keep
managed defaults/roles consistent under the model configuration policy.
Saved files cannot switch a running model. Report unavailable models/capabilities
or an execution mismatch; never claim another model performed the work.
Children have no authorization beyond the parent task.

Display agent identity, role, task status, model, and effort from supported native
evidence when available. Distinguish saved selection, active thread settings,
and the runtime-reported model; show mismatches, unknown values, and stale data.
A role filename, spawn request, or agent self-description does not prove which
model executed a particular operation. Observation must not silently alter or
cancel the task. Use available native status/tools and report their limits;
these instructions do not install a monitor or establish access to arbitrary
client sessions.

## Cost

Count coordinator, worker, and reviewer work, including repeated context, reasoning,
and tools. A shorter main conversation or lower elapsed time does not establish
token savings. Compare representative tasks with the same effort, environment,
and quality criteria; remove duplicate context and checks before adding agents.

## Sources

[Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents),
[models](https://learn.chatgpt.com/docs/models), and
[configuration](https://learn.chatgpt.com/docs/config-file/config-reference)
describe capabilities. Role allocation and review scope here are framework policy.
