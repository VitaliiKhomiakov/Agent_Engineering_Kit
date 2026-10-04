# Superpowers integration

Superpowers is the selected toolkit. Use skills for their actual triggers and load
only the selected procedures and needed references. This file owns skill selection
and workflow adaptations; it does not define a second delivery lifecycle.

## Discovery and authority

Use one installed plugin source. Do not copy its full instructions into AGENTS
or PLANS, install same-named shadow skills, or patch a plugin cache.
The upstream `using-superpowers` skill prioritizes explicit user instructions.
The framework adaptations below record those choices; system, developer, and
actual tool/permission constraints still apply. They are instruction policy,
not changes to the plugin or programmatic enforcement.

Before applying a skill, read the relevant policy below if it is not already in
context. It replaces conflicting upstream defaults. Pass applicable adaptations,
the current stage, and permissions to workers; a bare link is not a loaded policy.

## Skill selection

| Skill | Use it for |
| --- | --- |
| `using-superpowers` | Selecting relevant procedures and actual platform tools |
| `brainstorming` | Clarifying behavior/design before a feature or structural change |
| `writing-plans` | A substantive implementation plan after design decisions are agreed |
| `executing-plans` | Executing a saved plan inline |
| `subagent-driven-development` | Bounded implementation delegated from a plan |
| `dispatching-parallel-agents` | Independent investigations or separately owned work |
| `test-driven-development` | Selected test-first changes, regressions, or domain rules |
| `systematic-debugging` | A bug or failed check; gather evidence before another fix |
| `diagnosing-superpowers` | A reported session failure requiring transcript evidence; not a general assessment of planning rules |
| `requesting-code-review` | A completed scope warranting independent review |
| `receiving-code-review` | Assessing and fixing findings |
| `verification-before-completion` | Evidence supporting a completion claim |
| `using-git-worktrees`, `finishing-a-development-branch` | Authorized isolation and integration |
| `writing-skills` | An actual skill: validate format and relevant behavior; ordinary docs need no skill-testing campaign |

Read the selected skill itself; this table is not a substitute for its applicable
instructions. Actual tool schemas determine available capabilities.

## Explicit adaptations

- **Language:** apply the [reasoning and communication policy](core.md#reasoning-and-communication-language)
  to every skill. Reasoning, internal analysis, working notes, specifications and
  plans (including progress/handoff records) use English unless the user explicitly
  requests another artifact language. Announcements, questions, approval requests,
  review explanations and result reports use the user's response language. English
  examples in a skill do not prescribe the language of user-facing messages. Pass
  both the artifact-language policy and the chosen response language to delegated roles.
- **Planning and decisions:** for a substantive plan, read workspace `PLANS.md`
  ([template](../templates/PLANS.md)); for task/design choices, read relevant [delivery rules](delivery-workflow.md).
  Their artifact ownership, plan depth, and material-design review replace stock
  document recipes. Reuse already granted decisions/approvals and routine local discretion.
  Preserve the goal, design reference, Global Constraints and interfaces needed by
  dependent tasks. Use logical stages and code only to settle ambiguity; review
  concrete failure scenarios without a fixed count or an automatic new test suite.
  Follow the adopted planning policy's [item markers and resumption rules](../templates/PLANS.md#progress-and-stopping)
  in the canonical task; skill helper bookkeeping does not create a second progress owner.
- **Progression and Git:** read [work modes](work-modes.md) for the selected mode.
  Its checkpoint and authorization rules replace continuous execution, mandatory
  plan/spec/task commits, worktree setup, and branch-finishing defaults.
  Choosing inline or delegated execution does not itself authorize automatic
  progression or Git writes. A recorded `Ruling` cannot grant either permission
  or settle a missing material user decision.
- **Tests, review, and retries:** read the relevant [verification sections](verification.md).
  Resolve relevant cadence/review/reset settings through [policy configuration](policy-configuration.md)
  and apply the verification owner's conditions, required gates and evidence reuse.
  Intermediate checks still need the reasons defined there. This replaces universal TDD, full-suite
  completion demands, fresh-test requirements, automatic extra spec/quality or
  final reviewers, and fixed repair-round caps. Required project/CI gates and
  material in-scope defects remain binding. Keep check output compact and pass
  valid results to delegated roles; an internal task handoff does not trigger a
  duplicate cycle.
  Evidence must cover the current relevant state; it need not be regenerated in
  the final message's turn. Apply [evidence reuse](verification.md#reuse-evidence-before-repeating-work)
  before repeating a command or review merely to satisfy a stock freshness recipe.
  A parked finding or exhausted fix budget does not satisfy acceptance criteria.
- **Delegation and models:** read [orchestration](orchestration.md) when delegating.
  Saved model/effort pairs (including the user's `high`), fresh context, bounded
  ownership, and the concurrency ceiling replace a skill's suggested tiers or escalation.
  Its [delegation contract](orchestration.md#delegation-contract) owns the reason,
  sufficient task context and evidence return; use its lifecycle for continuation
  and late results. Skill helpers do not require a new worker per item or correction,
  whole-history handoff, repeated discovery or another review of still-valid results.

## Plans and helper compatibility

Use the canonical plan/native task artifact defined by workspace `PLANS.md`.
Keep an existing store at its supported location; workspace navigation and changing
the implementation checkout do not relocate it or create another progress owner.
For an ordinary task, the common policy and applicable skill are sufficient;
read [helper compatibility](superpowers/compatibility.md) only when using a helper
or resolving an installed-version contract. It owns commands, caveats and dated evidence.

If Superpowers is absent or a helper is unsuitable, read the bounded canonical task
directly, preserve its constraints and baseline, perform the necessary checks, and
review actual scoped changes including new/uncommitted files and prior user edits.
Record decisions, evidence and progress in the canonical artifact. This fallback
neither skips acceptance gates nor adds commits, redundant check runs or a second
ledger. A genuinely required missing capability blocks only its dependent task;
ordinary instruction-guided work can continue. Do not install tools to satisfy bookkeeping.
