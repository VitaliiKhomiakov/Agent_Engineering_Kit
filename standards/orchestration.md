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

The coordinator's routine review is not an independent second opinion.
Responsibilities may remain with the coordinator in a small task;
separate architect/planner/test roles are independently configurable when useful.
Use the [delegation contract](#delegation-contract) to decide whether a handoff is justified.
In selected single-agent
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

Delegate a coherent bounded result for a concrete reason: required independent
assessment, useful independent parallel work, or isolation of substantial noisy
investigation. State the reason briefly in the existing handoff. Keep small,
tightly coupled work inline when rebuilding context would outweigh the benefit;
required independent review remains binding. A checkbox, available slot, configured
role or test command alone is not a reason. Do not create a planner for an agreed
plan, a progress-update worker or agents that repeat completed investigation.

Supply the minimum sufficient brief for any assigned role:

| Part | Required content |
| --- | --- |
| Outcome | Task/item ID, observable acceptance, assigned paths, interface dependencies and reason for delegation |
| Location and state | Exact instruction root/checkout mapping; absolute canonical task/spec sections and pre-edit baseline; native task-tool context when different |
| Decisions and constraints | Material user choices, uncertainty, known failures, work mode, current permissions, Git scope and human checkpoint |
| Role | Selected enabled role, saved model/effort pair, allowed edge and applicable capability limits |
| Instructions | Essential project constraints and applicable Superpowers adaptations as current text; precise reachable routes for other required task rules |
| Evidence and return | Relevant valid checks with covered state, pending criteria, required commands/inspection and concise result format |

Supply substantive required policy once, as current text or an explicit worker
read. A filename, bare link or the parent's having read a rule does not establish
worker context. Do not require rereading unchanged text already supplied. Expand
context only for a named missing decision, dependency or concrete failure; load
an adjacent contract when it answers that question. Do not preload whole plans,
profiles, history or successful raw logs. Shortening a brief must not remove a
global constraint or substitute a stale excerpt. If an essential route cannot be
read, ask the coordinator for that input before dependent work; continue only
independent authorized work, without restarting broad discovery.

Explicitly disable history inheritance with `fork_turns: "none"` when supported,
or the client's equivalent fresh context. A short prompt does not override a
full-history default. If this control is absent, report the limitation and use
the narrowest supported context. Never invent parameters or omit the user's
authorization and requirements. Workers need a specific authorized reason to
spawn further agents.
Fresh context is the selected isolation policy, not a cost guarantee. Do not
enable history inheritance or lower the selected effort merely to save tokens.
Keep decisions/progress with the supplied canonical owner; a checkout copy or
temporary brief is not another task ledger. Report an inaccessible store before
dependent work rather than creating a replacement or relocating the task.

For review, supply the same mapping, task changes, baseline, criteria, valid
evidence, and concrete regression questions. Read [review boundaries](verification.md#review-boundaries)
for scope and findings; do not assign incidental unrelated bugs to new workers
without scope authorization.

Return acceptance outcome, changed paths or located findings, baseline and covered
state, actual check results, remaining risks/blockers and focused evidence routes.
Leave successful raw logs/transcripts outside the main context. The coordinator
checks actual scoped changes and unresolved risks, reusing applicable evidence
under [verification](verification.md#reuse-evidence-before-repeating-work); a worker's
return alone triggers neither duplicate discovery nor another test/review cycle.

## Concurrency and isolation

The configured ceiling is not a target; the initial suggestion is two spawned
agents excluding the main agent. Sequential execution is normal. Parallel tasks
need independent results and clear ownership. Avoid concurrent writers to the
same files or tests competing over ports, databases, and fixtures; preserve others' work.
Check native capacity separately: running work, pending tools and retained agent
threads may occupy different resources. Do not assume a finished/idle thread
releases a slot or invent a close operation; use the supported lifecycle controls.

Use the directory mapping and isolation rules in [work modes](work-modes.md#workspace-root-and-project-checkouts).
A non-Git workspace root does not prevent authorized worktrees for nested projects.
Workers stay within the current stage at a human checkpoint. Review a stable
completed scope; after combining independent changes, check affected interactions.
Separate branch checks do not establish integration correctness.

## Worker lifecycle and continuations

The coordinator tracks each relevant assignment in the canonical task/handoff:
worker identity, owned scope, applicable baseline, expected result and actual state.
Use supported native status and tool results; a timeout, partial report or idle
thread is not evidence that its assigned work and outstanding tools finished.

Before transferring ownership, starting dependent review, removing recovery
material or reaching the human checkpoint, reconcile relevant workers and pending
commands. Wait for completion or confirm an authorized stop and its actual effect.
An interrupt request alone does not prove a background command stopped. Preserve
recovery material while writes remain possible; never cancel unrelated work or
discard partial edits to obtain a clean status. If stopping is unavailable, report
that limitation and hold only the dependent transition.

Continue the same bounded assignment when its context and capabilities remain
applicable. Send changed requirements, findings and invalidated inputs instead of
replaying the entire brief. A different assignment or required independent review
gets an appropriate separate context. Use supported completion notifications or
bounded waits, keeping the user informed; avoid repeated polling or cache keepalives.
Resumption is not a promise of lower cost and does not reset task permissions.

Before accepting a late result, compare its assignment, baseline, affected files
and evidence with the current task. After reassignment or intervening edits, retain
only still-applicable findings/results; reconcile overlapping changes before any
dependent application. Preserve current user work. A stale completion claim cannot
close an item. Plan updates follow serialized progress ownership in the adopted
`PLANS.md` ([inactive source template](../templates/PLANS.md#progress-and-stopping)),
including a planner's explicit draft handback; no worker creates a second ledger.

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

Count coordinator and all worker/reviewer work, including handoffs, repeated
context, reasoning, tools, corrections and review. Separate reported input/output,
reasoning and cached usage when available; avoid double-counting client aggregates.
Unknown telemetry remains unknown. Tokens, elapsed time and billed cost are
different measures; a shorter main conversation proves no total savings.

Savings claims need comparable authorized runs with matching scope, model/effort,
environment and quality criteria. Remove duplicate context and checks before
adding agents. Do not create a mandatory paid benchmark, monitoring service,
prompt-size quota or cache setting; keep evidence in the existing task owner.

## Sources

[Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents),
[models](https://learn.chatgpt.com/docs/models), and
[configuration](https://learn.chatgpt.com/docs/config-file/config-reference)
describe capabilities. Role allocation and review scope here are framework policy.
