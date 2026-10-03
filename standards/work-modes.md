# Working directory, checkpoints, and Git actions

Execution mode and model selection are separate decisions. Use the saved role
assignments in either mode. The default is direct, incremental work with human
checkpoints; an explicit task instruction can enable autonomous work in a worktree.

## Workspace root and project checkouts

The selected workspace root owns instruction/navigation routes and is the default
location for new plain plans; it may contain several independent Git projects and
need not itself be Git. Preserve an existing canonical task store, including one
inside a project, under workspace `PLANS.md` ([template](../templates/PLANS.md)).
Record the root, canonical store and implementation checkout separately. Changing
cwd or entering a worktree does not change artifact ownership.

Resolve each affected project's repository from its own path, for example with
`git -C <project-path> rev-parse --show-toplevel`, rather than from the workspace
root. In direct mode, edit and check the affected projects in their current
directories/checkouts; absence of Git at the workspace root changes nothing.
When worktree use is authorized, create or reuse a worktree for each affected
repository whose project files will be changed. Projects sharing one repository
can share its worktree; a worktree of a parent does not isolate nested repositories.

Record the mapping from project/repository to selected checkout or worktree in
the task handoff. Project edits and checks use those mapped directories. Plans and
specifications retain their canonical locations in either mode; do not maintain a
second editable task copy in a worktree. Use the supported native tool context for
task operations, separately from project checks. Pass absolute canonical artifact
paths and applicable workspace instructions to workers,
including when a worktree is outside the normal instruction-discovery boundary.

## Default: direct work with human checkpoints

Work in each affected project's current directory and checkout. Do not create a
worktree, branch, commit, pull request, or stash, and do not stage changes as routine bookkeeping.
Read-only Git inspection is allowed when Git is available. Do not initialize a
repository merely to satisfy an agent workflow.

Break substantive work into small logical stages with observable results. A
stage may complete one behavior, contract, or coherent documentation update;
it is neither every keystroke nor an entire multi-feature rewrite. Name the
current stage, its boundary, and completion evidence before substantial edits.

Finish that stage, run its necessary checks, and report:

- What changed and where to inspect it.
- Which criteria and checks were satisfied, and any unresolved limitation.
- The proposed next stage, without starting it.

Then stop and wait for the user's review and instruction to continue. Do not
start writing the next stage through a background agent while waiting. An agent
review supports this checkpoint; it does not replace the user's decision.
Feedback can refine the current stage before advancing.

Approval to continue authorizes the next agreed stage, not silently switching to
autonomous execution. Do not request approval for every ordinary edit or relevant
check inside the authorized stage. If the user explicitly approves several stages
without intermediate stops, follow that task-specific progression while retaining
the other direct-mode limits, including the no-commit default.

Preserve existing user changes. Never use reset, clean, checkout, restore, or
stash to obtain a convenient clean baseline or undo unrelated work. When a task
requires reverting an agent change, identify that exact change and preserve
intervening edits. Lack of commits is not permission to lose local work.

## Explicit opt-in: autonomous worktree execution

Enter this mode only when the user requests a worktree and automatic execution
for the current task. Record the outcome, phases, base/target when needed, and
authorized Git actions in the task contract. Continue the agreed phases without
human checkpoints; report meaningful progress and the final result.

Apply the project-to-checkout mapping above using the current client's supported
worktree mechanism or a suitable Git worktree. Detect and reuse existing isolation
for each affected repository rather than nesting another worktree. Missing Git at
the workspace root is not an isolation failure for a nested Git project. If an
affected project's isolation is unavailable, report that specific obstacle; do not
initialize a repository or silently edit its main checkout instead.

Run focused setup/baseline checks only where they establish necessary evidence.
Account for required uncommitted inputs explicitly: a new Git checkout does not
automatically represent every local modification or ignored file. Do not create
a stash or commit to transfer them without authorization. Keep parallel writers
in separate areas/checkouts and prevent shared test-resource conflicts.

Worktree permission alone does not authorize every Git write:

| Action | Rule |
| --- | --- |
| Create/use a worktree | Authorized by the explicit mode choice, within actual filesystem permissions |
| Create a task branch | Only as needed for the agreed worktree workflow; do not switch the user's local checkout |
| Stage/commit changes | Only if the user also permits local commits; otherwise leave changes uncommitted |
| Merge/cherry-pick/copy changes into another checkout | Requires an agreed integration target and permission to integrate |
| Push/create a PR/deploy | Requires its own explicit authorization |
| Remove worktree | After the approved merge succeeds, required integration checks pass, and no work would be lost |
| Delete a branch | Separate authorization; deleting the worktree does not require deleting its branch |

Do not ask whether to commit when leaving an uncommitted result satisfies the
task. If the requested integration genuinely needs an ungranted action, prepare
the reviewable result first and clarify that specific action. Reuse authorization
already given; do not ask again at every phase or commit.

Apply [proportionate verification](verification.md) in automatic mode too. Stop
for a material unresolved requirement, an action outside authorization, a real
environment block, or the final completion condition. Automatic mode does not
justify endless tests, speculative cleanup, or review loops.

## Worktree completion: offer merge, then clean up

At task completion, present the reviewable changes, checks, source worktree/branch,
and intended target branch. Offer to merge the changes and remove the worktree
afterward. Automatic implementation normally ends at this integration checkpoint.
If integration into that target was already explicitly authorized, use the
existing authorization instead of asking for it again.

Git merges committed history, not an uncommitted directory. If local commits
have not been authorized and are required, include them explicitly in the one
concrete proposal: create the task commit, merge into the named target, then
remove the worktree. Do not make the commit just to prepare the proposal.

After an approved successful merge, complete the necessary integration checks
and confirm the task changes are retained in the target. Then remove the task
worktree using the supported client/Git mechanism without a second routine
permission question. Check for remaining uncommitted/untracked user work first;
never force-remove it or use recursive deletion to bypass worktree safeguards.
Also check whether the worktree contains a canonical task store: retain it while
that store is still needed, or complete an explicitly authorized relocation first.

If merge, checks, retention verification, or removal fails, keep the remaining
worktree and report the exact state. A failed verification does not authorize
resetting the target or discarding either side's changes. Branch deletion, push,
and deployment remain separate permissions. For several worktrees, apply this
rule to each integrated result and its dependencies.

Report what was merged, the relevant checks, and which worktrees were removed
or retained. Return to the default mode for the next unrelated task unless
the user explicitly changed the project default.

## Unambiguous task examples

- “Complete the next stage in the current directory, without commits or
  worktrees. Run the relevant checks and stop for my review.”
- “Use a worktree and complete the agreed phases automatically. Leave the result
  uncommitted in that worktree for my inspection.”
- “Use a worktree, complete the plan automatically, and make local commits.
  Keep the result on its task branch for review.”

An instruction such as “finish automatically” changes progression only; it does
not by itself request a worktree or grant commits. “Use a worktree” alone changes
isolation, not the human-checkpoint policy. Resolve any missing material intent
without treating those independent choices as one blanket permission.

## Skills and evidence

The user's selected mode takes precedence over generic skill recipes that would
create worktrees, commit a plan or .gitignore, run a full baseline suite, or finish
with a merge/PR. Do not trigger those procedures merely because they are installed.
Carry the selected mode, current stage, and Git permissions into every delegation.

[Codex worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees)
documents optional isolation and Local/Worktree handoff. The default checkpoint
behavior and no-commit policy above are this user's choices, not Codex requirements.
