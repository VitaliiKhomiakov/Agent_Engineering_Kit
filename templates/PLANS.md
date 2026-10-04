# Planning rules

Template: install as PLANS.md at the workspace root.
Default paths below are relative to that root, with imported resources under
`.agents-framework/`. Rebase for the recorded bundle and actual entry location;
links in an inactive bundled copy resolve from its containing file. This file
defines how to plan; task-specific decisions and progress belong in the
corresponding task document.

## Language

Write specifications, design documents and plans in English, including working-plan
bullets, native planning artifacts and their progress/handoff records, unless the
user explicitly requests a different artifact language. Present questions, review
explanations, progress updates and results to the user in the user's response
language. A plan's English text does not switch the conversation language.
Apply the [language policy](.agents-framework/standards/core.md#reasoning-and-communication-language);
resolve this link to the adopted policy when installing this template.

## When to save a plan

For a clear local change, keep a few working-plan bullets; no plan file is required.
Save a plan for several stages, affected boundaries, material uncertainty, or an
explicit user request. A short prompt does not justify expanding the task.

For a new plain Markdown or Superpowers plan, default to workspace
`docs/plans/<task>.md`, combining specification, stages and handoff where sufficient.
Preserve an existing task's canonical location. When using an existing native
artifact system, the workspace entry is a short navigation file to those documents;
keep decisions and progress in their native owners, without a second editable plan
or checklist. On archival or an authorized relocation, update navigation links.
Read this policy when creating or resuming such a task, then the active plan.
Read other plans only to resolve a specific dependency or decision.

For new plain plans, use a separate workspace `docs/specs/<task>.md` only when a
substantial design needs its own review and lifetime. The workspace need not be Git.
Record the instruction/workspace root, canonical artifact location and project
execution checkout separately. Changing cwd or creating a worktree does not change
the canonical owner or promote a checkout copy into another editable task record.

## Native artifact systems

Keep the adopted OpenSpec, Spec Kit or other native format and its supported store,
including a store inside a nested repository. Resume the existing task there.
Workspace navigation points to its canonical artifacts; it does not relocate them.
When invoking a native tool, verify its installed schema, supported working directory
or store setting, and actual resolved task paths. Do not assume it follows Markdown
links or supports an invented path override. If it cannot operate on the canonical
store from the implementation checkout, use its supported context for task operations;
keep implementation edits and checks in their assigned checkout.

An independently opened project retains reachable local instructions and a route
to its native task entry. It does not depend on discovering a parent workspace or
creating a workspace navigation file before resuming its existing task.
If the canonical artifact is inaccessible, report the exact path/access obstacle
and pause only dependent work. Do not create a divergent replacement or use a stale
worktree copy as current progress.

Relocation is a separately requested migration, never a prerequisite for unrelated
work. Such a migration preserves artifact identity, decisions, progress, links and
native tracking, verifies supported paths, and leaves one canonical owner. Unsupported
relocation blocks that migration, not ordinary work in an accessible existing store.
Keep injected global context short; use artifact-specific rules for planning detail.

## What a plan contains

- The observable user outcome, scope, required compatibility, and acceptance criteria.
- Relevant files, contracts, and concise current-state evidence; link architecture
  sections and standards instead of copying their full text.
- Material design decisions, assumptions, and unresolved questions affecting the task.
- Small logical stages, each with a checkable outcome, affected area, dependencies,
  and sufficient verification. Add owners only if work is actually delegated.
- Current status: planned, in progress, awaiting user review, blocked, or complete;
  the currently authorized stage and the next human checkpoint.
- Execution mode, explicitly granted Git actions, and the workspace model-routing
  reference. A plan does not grant actions or override the user's permissions.
- The workspace/instruction root, canonical artifact/store location and progress
  owner, affected project/repository-to-checkout mapping, and pre-stage baseline.
  Record worktree paths and the native tool context when used.

Keep enough context for another session to resume the task. Add detail for complex
interfaces, migrations, or recovery only where it changes implementation decisions.
Include exact code only to resolve ambiguity; use logical stages with checkable outcomes.

## Progress and stopping

Update the current document at meaningful decisions and stage boundaries. Record
what changed, criteria met or outstanding, checks with results and applicable code
state, blockers, and the proposed next stage. Keep a concise state, not full logs
or a transcript; do not rewrite the plan after every edit.

For substantive Markdown plans, give independently actionable items stable IDs
and unchecked/completed markers. Preserve existing IDs; adding an item does not
renumber completed work. Update an item's marker when its own acceptance conditions
are met, before moving to the next item or handing off. Do not postpone all updates
until the stage ends. Keep the current item and stage status explicit.

- `[x]` means the item's stated outcome is achieved. If its acceptance includes
  tests, keep it unchecked until those tests pass. Separate implementation and
  verification items may close separately when their own criteria permit it.
- In-progress and blocked items remain `[ ]`; record their state and a concise
  reason separately. Reopen a completed item if new evidence invalidates it, with
  the reason recorded; retain still-valid evidence for other items.
- Mark cancelled or superseded scope explicitly with its reason; cancellation
  does not count as completed implementation. At each checkpoint, align markers,
  current status, acceptance evidence and remaining work.
- On resumption, reconcile the canonical state with relevant current evidence;
  do not repeat completed work merely because a new session began. Native stores
  retain their supported markers/status operations and single progress owner;
  do not mirror them in a second editable checklist or invent CLI operations.

Item completion is neither a permission checkpoint nor a trigger for extra tests
or reviews. Verification timing and evidence reuse retain their existing owner.
A trivial edit still needs no persistent plan. These progress rules are binding
planning semantics, not a configurable policy switch.

The coordinator normally owns updates to the shared canonical checklist, using
worker evidence after reconciling it with the current task. Concurrent workers
report outcomes; they do not edit that checklist together. A delegated planner
may own a specifically assigned draft. Record that ownership and explicitly hand
it back before another writer updates it; preserve one canonical artifact and
the native store's supported operations. Simultaneous completion reports are
reconciled and recorded sequentially, without losing either result.

At the human checkpoint, mark the stage awaiting user review; a completed stage
is not a completed task. A plan records authorization and never grants it.

| Decision | Detailed owner |
| --- | --- |
| Stage structure and delivery technique | `.agents-framework/standards/delivery-workflow.md` |
| Execution mode, checkpoint exceptions and Git actions | `.agents-framework/standards/work-modes.md` |
| Baseline, checks, scoped review and evidence reuse | `.agents-framework/standards/verification.md` |
| Saved model choices or delegation | `.agents-framework/standards/model-configuration.md`, `.agents-framework/standards/orchestration.md` when applicable |
| Applying a selected skill | `.agents-framework/standards/superpowers.md`; helper detail only when needed |

Reuse already established rules within the stage instead of reloading them per edit.
