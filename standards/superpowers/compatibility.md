# Superpowers helper compatibility

Conditional reference: read for helper use or a version-contract investigation.
[Common policy](../superpowers.md) owns skill selection, authority and workflow
adaptations. Ordinary tasks do not need this file. Resolve the installed version
before applying these observations; package presence is not proof of active selection.

## Helper contracts: inspected 6.4.1 and 6.4.2

Use the plan/spec locations and single artifact owner defined in workspace
`PLANS.md`. Execute native task artifacts directly; do not regenerate another
editable plan or start a second planning/review lifecycle for the same change.
Supply the canonical artifact's absolute path, even when its native store is inside
a nested project. Keep that store distinct from the helper's temporary directory
and implementation checkout. An inaccessible canonical artifact is an access obstacle,
not permission to replace it with a copied plan or a new ledger.

Resolve `<sdd-scripts>` from the installed plugin's
`skills/subagent-driven-development/scripts/` directory; inline wrappers live in
`skills/executing-plans/scripts/`. Invoke the selected helper with `bash` rather
than relying on preserved executable bits. Run Git-dependent commands from the
mapped project's checkout, not the plugin directory or an unrelated workspace.

For workspace-level execution, replace `sdd-workspace PLAN_FILE` with a writable,
task-scoped execution directory accessible to workers. In both inspected versions,
the stock helper requires the current directory's Git root, which may be absent
or belong to another project.
Do not initialize Git or move plans into a project to enable it. Keep only temporary
briefs, reports, and review packages there. Resume from the canonical plan/native
task artifact and its applicable evidence, not a second SDD ledger that assumes
task commits. Preserve decisions needed for resumption there; do not infer task
completion solely from Git history. Retain baseline and check evidence through
the required review and handoff, including the human checkpoint.

The [task template](../../templates/task.md) has optional numbered `Task N` headings.
In both inspected versions, use `bash <sdd-scripts>/task-brief PLAN_FILE TASK_NUMBER OUTFILE`
with absolute plan/output paths and an existing output directory to bypass
Git-dependent setup. The extractor includes the task section, not the plan's
Global Constraints, design reference, or earlier interface decisions. Inspect
the brief before dispatch and supply the relevant exact constraints, permissions,
design context, canonical store/progress owner, and project-to-checkout/baseline
mapping with it. If a native task format cannot be extracted, use a scoped temporary brief referencing native
task IDs. A successful extraction alone is not a complete delegation contract.

The inspected inline wrappers `task-start PLAN_FILE TASK_NUMBER` and
`task-done PLAN_FILE TASK_NUMBER BASE -- TEST_COMMAND` depend on Git and the stock
scratch workspace. `task-start` has no explicit output-path argument;
`task-done` reruns the supplied check and records completion in a separate ledger
using a commit range. Bypass these wrappers in the framework workflow: extract
or read the scoped task, run necessary checks directly, and record actual results
and the current stage status in the canonical artifact. Do not rerun valid checks
or mark a stage complete merely to satisfy a helper's bookkeeping contract.

Capture the baseline before writing under [verification](../verification.md#before-implementation).
The inspected `review-package` helper excludes uncommitted changes and requires a
nonempty commit range whose BASE is an ancestor of HEAD. Use scoped
diffs or before/after comparisons against that baseline without staging. Cover new
and uncommitted task files and root documents outside Git; distinguish prior user
edits. Worktree use alone does not imply commits; rejection of an empty commit
range says nothing about the presence or quality of working edits.

When commits are authorized and present, run
`bash <sdd-scripts>/review-package PLAN_FILE BASE HEAD OUTFILE` from the relevant
project's checkout with its own commit range, absolute plan/output paths, and an
existing output directory. Use a separate package per repository; include remaining
uncommitted changes and workspace documents outside that range separately.

## Local 6.4.2 inspection — 2026-09-26

Confirmed `version = 6.4.2` in the installed Codex plugin manifest. Compared the
following files with the locally available 6.4.1 package; this is a bounded source
inspection, not a claim about every package file or an end-to-end client run.

| Inspected contract | Comparison and effect |
| --- | --- |
| SDD `sdd-workspace`, `task-brief`, `review-package`; inline `task-start`, `task-done` | All five scripts are byte-identical. The Git root, extraction omissions, commit-range and separate-ledger constraints above remain. |
| `executing-plans/SKILL.md`, `subagent-driven-development/SKILL.md` | Both are byte-identical. Continuous progression, commit/ledger recipes and automatic reviews still require the common policy's adaptations. |
| `writing-plans/SKILL.md` | Changed: checkable steps replace the 2–5 minute rule; signatures, pinned values and interfaces replace mandatory complete implementation bodies; a proportion check discourages excess detail. Exact test assertions, frequent commits and five review-focus cases remain stock prescriptions subject to the common planning/verification policy. |

Inspected all five helper bodies and the changed planning instructions. Invoking an
outer wrapper through `bash` does not fix direct execution of child scripts inside
`task-start`/`task-done`; they still call children directly. This is another reason
to use the direct scoped-task fallback rather than patching permissions or cache files.
No helpers or model sessions were executed as part of this 6.4.2 source inspection.
Recheck affected contracts on upgrade; this record does not install, activate or modify
any plugin, establish model selection, or complete the adoption pilot.

## Historical 6.4.1 evidence — 2026-09-20

Historical compatibility target: installed Superpowers **6.4.1**, confirmed from its Codex
plugin manifest on **2026-09-20**. Locally inspected skill discovery and the Codex
reference, brainstorming, planning, inline/delegated execution, verification,
session-diagnostic scope, and the helper contracts described above.

Checked the existing task template with an explicit `task-brief` output path
outside Git: extraction succeeds and the plan-level constraints are absent,
so the coordinator must supply them. Confirmed `sdd-workspace` rejects a non-Git
working directory. The commit-dependent review and inline-wrapper contracts
were inspected in source; their complete execution was not exercised here.

Fresh-session instruction discovery, a complete plan-to-stage handoff, stage
stopping, review of actual uncommitted work, and resumption from the canonical
artifact still require the bounded adoption pilot. Recheck changed contracts on
upgrade. Templates remain inactive; this inspection does not establish runtime
model selection or activate the integration in a target workspace.

Upstream documentation was consulted on 2026-09-17; the links below are background,
while this compatibility check used the installed 6.4.1 package.

[Toolkit](https://github.com/obra/superpowers),
[skill priority](https://github.com/obra/superpowers/blob/main/skills/using-superpowers/SKILL.md),
[plan writing](https://github.com/obra/superpowers/blob/main/skills/writing-plans/SKILL.md),
and [delegated execution](https://github.com/obra/superpowers/blob/main/skills/subagent-driven-development/SKILL.md)
document upstream behavior.
[Codex PLANS.md](https://developers.openai.com/cookbook/articles/codex_exec_plans)
is background; this framework does not adopt its exhaustive self-contained format.
[OpenSpec concepts](https://github.com/Fission-AI/OpenSpec/blob/main/docs/concepts.md)
and [customization](https://github.com/Fission-AI/OpenSpec/blob/main/docs/customization.md)
support the native-artifact rules owned by the planning policy.
