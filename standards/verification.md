# Proportionate tests, verification, and review

Apply these rules to the changed behavior and its material risks. They define
sufficient evidence, not a quota of tests, commands, tokens, or review comments.
Resolve the relevant `verification.*` and `review.independent` settings through
[policy configuration](policy-configuration.md). This document owns check selection,
required gates, evidence reuse and acceptance; settings do not waive them.

## Before implementation

Identify the acceptance criteria, affected contracts, risk, and relevant existing
checks. A short task does not authorize broader functionality, a coverage campaign,
or a repository-wide audit. For a small change, one sentence can explain the
verification choice; do not create a separate test-plan document by default.

Before the first write to each affected path in a stage, the coordinator ensures
that its original contents or prior absence are recorded. Include existing local
edits and untracked files, and both sides of a rename. A delegated writer confirms
that this baseline covers its paths and captures any newly affected path before
editing it; never replace the original baseline with an intermediate result.

Keep scoped copies or a reproducible reference outside the edited files, accessible
through the stage's review and handoff. For clean tracked files, the repository,
checkout, commit, and path can identify the original; HEAD alone cannot represent
dirty or untracked contents. Use file copies when Git is absent. Record the
baseline location and relevant checkout in the existing plan or handoff, without
commits, staging, a whole-project snapshot, or a separate evidence system.

## When to add tests

- Reuse or extend an existing test when it already protects the changed behavior.
  Add a test for a material requirement or regression that lacks useful coverage.
- A new test should expose a plausible defect or contract violation. Test domain
  invariants, meaningful error paths, and boundary behavior relevant to the change.
- Do not add tests just because a file, class, method, or line was added. Avoid
  trivial accessor tests, implementation-shaped assertions, redundant snapshots,
  duplicate cases, and tests of a library's own behavior.
- Documentation, wording, and reversible low-impact mechanical edits normally
  need artifact checks rather than new unit tests. An executable example or a
  subtle behavior change may require a focused test.
- Select TDD for the behavior that benefits from it; do not impose it on every
  edit or delete valid code merely to reenact a Red–Green sequence.
- Do not introduce a runner, mock framework, E2E environment, or coverage target
  for a local change unless the requested result requires it.

Use the cheapest reliable level: a domain unit test for a rule, an integration
test for persistence or an adapter contract, and E2E for an affected critical
journey or an established gate. Cover distinct failure modes across levels;
do not reproduce the same assertions at every level without a reason.

## What to run, and when

| Change | Typical evidence | Reason to widen it |
| --- | --- | --- |
| Documentation or wording | Relevant links, syntax, rendered output when needed | Executable content or generation changes |
| Local behavior or bug | Focused existing/regression test and applicable static checks | Affected callers or a discovered adjacent risk |
| DTO, API, persistence, adapter | Relevant contract and integration checks | Compatibility, schema, transaction, or shared dependency changes |
| Authorization, isolation, money, concurrency | Material permitted/forbidden cases and integration behavior | Risk can be high even with a tiny diff |
| UI or routing | Affected interaction and relevant build/render checks | Critical journey or Server/Client boundary changes |

Batch code checks and functional verification at the boundary selected by
`verification.timing`: `phase_end` uses a small, coherent
[phase](delivery-workflow.md#phase-boundaries); `task_end` uses the planned task
boundary. A bounded task without phases uses its completed change in either case.
Required intermediate gates and the acceptance checks needed for a human stage
checkpoint remain binding; task-end batching cannot postpone them past that checkpoint. Select
the necessary checks from acceptance criteria before implementation; do not run
them after every edit, file or internal task merely because that step finished.
Design and write needed tests within the implementation phase; execute them at the
selected boundary unless an earlier check is required above. With authorized
progression across internal phases, `task_end` may batch their functional checks
at task completion. Pending evidence is not acceptance: keep criteria and item
markers requiring those results open under the adopted planning policy.

Before the selected boundary, run the smallest relevant check only to reproduce a bug,
resolve a concrete uncertainty, validate a risky contract before dependent work,
follow selected TDD, or meet a required project/CI gate. Briefly state the reason
in the working update. In TDD, use the focused Red–Green–Refactor cycle; a normal
red step is not a failed repair attempt. These exceptions do not require a full suite.

At the selected boundary, cover the changed behavior and affected interactions using
the cheapest reliable checks. Compilation, linting and type checks alone do not
prove functional acceptance. Use relevant domain, API, integration or UI scenarios
for behavioral changes; E2E is needed only where its additional coverage matters
or a gate requires it. Reuse still-valid intermediate results. One cycle may
include several commands and necessary repairs; after fixes, rerun affected checks
and required gates without restarting unrelated successful checks.

Preserve mandatory project/CI gates unless changing them is explicitly in scope.
Complete those gates. Choose the relevant package or subsystem
where supported. A full suite is justified by a gate, broad impact, shared
infrastructure changes, or concrete unresolved risk—not as an automatic finale.

After a successful check, repeat it only if its relevant inputs changed, its
result is unreliable, or a new failure or concern makes it necessary. Changes
to dependencies, environment, configuration, or integrated branches can invalidate
evidence as well as code changes. Reuse applicable evidence for unchanged inputs.

Record the command or inspection, its scope and outcome, and the code state it
applies to in the existing task handoff. Do not create an elaborate evidence
database or repeat tests merely because a different agent now owns the task.

## Compact check output

Prefer a concise runner summary. When output is large, capture the full output in
a task-local log outside versioned source and load only the summary and relevant
failure details into agent context. Retain the command's actual exit status and
report scope, pass/fail/skip counts when available, and the log path. A truncated
output or a successful log-filter command is not proof that the tests passed.

Inspect additional log sections only to answer a concrete failure or coverage
question; do not reread successful logs or rerun a command to obtain a shorter
report. Reuse existing logs and evidence in handoffs. Running a check alone does
not need another agent. Fewer runs or shorter elapsed time do not establish token
savings; compare total agent work under the [cost policy](orchestration.md#cost).

## Reuse evidence before repeating work

These rules apply to test commands, builds, linters, searches, file/diff inspection
and review passes. Select the checks needed for the completed scope, inspect their
results, and reuse them while they remain applicable. One verification pass may
contain several necessary checks; it does not mean every check must run only once
regardless of failures or changed inputs.

Before repeating or widening a check:

1. Look at the existing result and the state it covered. Use the available handoff
   or tool output; do not create a new verification ledger or reread all evidence.
2. Identify the changed input, unreliable/missing result, concrete unanswered
   failure scenario, or explicit requirement for a new run. State the reason
   briefly in the normal progress update; a vague wish for more confidence is insufficient.
3. Run the smallest check that can resolve that reason, including required gates.
   After a fix, verify the affected behavior and interactions; retain unrelated
   valid results. Do not broaden a failed check into a full audit automatically.

Preparing the final answer, reaching a checkpoint, switching agents/tools or resuming
after compaction does not itself invalidate evidence. Nor does a report-only edit
invalidate code tests whose inputs are unchanged; check the edited report's affected
links or structure only when needed. Use the recorded results when reporting completion.
If a required result is genuinely unavailable or its applicability cannot be established,
recover it from existing evidence or repeat the necessary check and report that limit.

Do not repeat an answered inspection under a different command, launch another
reviewer for reassurance, or run an extra final pass after criteria, required checks
and scoped review are satisfied. End verification and deliver the result. A newly
observed failure or changed relevant input can reopen only the affected verification.
Explicitly required fresh project/CI gates and authorized additional reviews remain binding.

## Review boundaries

Start from the task's actual changes and acceptance criteria, including new files
and uncommitted edits. Use the recorded pre-stage state to distinguish those
changes from pre-existing user work. A touched file is not permission to audit
all of its unrelated methods. If attribution is uncertain, report that limit.

Read enough surrounding code to understand the change. Follow callers, callees,
DTOs, persistence, configuration, or consumers only to answer a concrete question
about a changed contract or a plausible regression. A regression path can cross
unchanged files and several layers; do not restrict review to edited lines.
Stop expanding once that question is answered. Do not traverse all imports,
map the whole call graph, or audit neighboring features by default. Explain a
non-obvious scope expansion briefly in the existing review notes.

Perform one accountable review of the completed scope, combining acceptance,
correctness, architecture and evidence. Coordinator review remains required.
Apply `review.independent`: `risk_based` uses material risk/complexity or an explicit
request; `on_request` uses an explicit request or binding project requirement.
Neither setting grants delegation, changes saved roles or overrides actual
capabilities. Report an unavailable required independent review rather than claiming
it happened; continue independent authorized work. Do not add a duplicate pass or
separate specification, style, security and quality reviewers for every small task.

A blocking finding identifies a location, a plausible failure scenario or
violated requirement, and its consequence. A missing test is a finding when
it leaves a material behavior unverified—not because a component has no test file.
Separate optional improvements from defects that must be fixed for this task.

A defect introduced or exposed by this change, a broken affected contract, or
a failure that prevents its acceptance belongs to this review. Fix or resolve it
within the task, or report a blocker when a wider decision is necessary.

If an unrelated or pre-existing bug becomes visible during this work, report it
once as an incidental finding: location, likely consequence, and whether it is
confirmed or suspected. Flag serious impact clearly. Do not start an unrelated
investigation, add tests, dispatch an agent, or fix it without scope authorization.
Separate its severity from whether this task caused it. An incidental finding
alone does not trigger another review pass or block otherwise satisfied criteria;
if it actually prevents acceptance, treat it as the dependency described above.

When reviewing conditions or defensive code, require a concrete supported scenario
before demanding another branch. Apply [simple control flow](core.md#simple-control-flow)
to the changed logic; do not turn it into a cleanup audit of unchanged code.

After fixes, revisit the findings and affected interactions. Do not restart an
unchanged repository-wide review. Do not add another review to confirm an earlier
review that found no unresolved issue. At integration, assess the new interactions;
do not re-review every unchanged phase from scratch. Passing tests and a clean
review are evidence, not a guarantee that all possible bugs are absent.

## Codex review entry points

Choose a native review scope deliberately. The CLI's uncommitted preset includes
staged, unstaged, and untracked changes, which can include other people's work.
Supply the task baseline, affected paths, criteria, and regression questions;
use custom review instructions where supported. A broad preset is not permission
to expand the task. Use a scoped reviewer when the preset cannot express it.

The app's Last turn view can help locate recent edits, but a logical stage may
span several turns. Review the full stage, with prior unrelated work distinguished.
If Git-backed review is unavailable, inspect scoped file changes; do not initialize
a repository or create commits solely to enable the review interface.

Native `/review` and a spawned `af-reviewer` are separate execution paths. The
CLI supports `review_model`; do not assume a custom agent role controls native
review. Confirm the effective model when selecting this path, and avoid a second
review merely because another interface is available.

## Completion and lack of progress

Finish when the acceptance criteria and required checks are satisfied and no
material in-scope finding remains unresolved. Report incidental findings separately.
Report a missing or blocked required check honestly; never label it successful or
waive it to fit a process limit.

At `verification.diagnostic_reset_after_stalled_attempts` consecutive unsuccessful
attempts on the same problem without new evidence, perform a diagnostic reset
with the coordinator: summarize facts, rejected hypotheses and the next
discriminating observation. Legitimate TDD red steps do not count. This is a guard
against repetition, not a fix-round cap, acceptance waiver or limit on meaningful
investigation and necessary repairs.
Do not expand scope to unrelated cleanup after the completion criteria are met.

## Source and policy boundary

Official sources rechecked on 2026-09-17.

[OpenAI's Astra testing guidance](https://developers.openai.com/api/docs/guides/latest-model#testing-and-verification)
recommends matching validation to the change and making additional passes
conditional on changes, failures, or unresolved concerns.
[OpenAI's skills and prompts guidance](https://learn.chatgpt.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra)
also identifies inherited blanket testing instructions as a cause of extra work.
[Codex code review](https://learn.chatgpt.com/docs/code-review) documents selectable
diff scopes, uncommitted changes, custom CLI review instructions, and model choice.

The one-pass default, incidental-finding boundary, risk examples, diagnostic reset,
and [control-flow constraints](core.md#simple-control-flow) are our framework policy,
not numerical test/review/branch limits documented by OpenAI.
Audit active skills for conflicting blanket requirements; layering this policy
over contradictory instructions does not reliably solve the problem.
