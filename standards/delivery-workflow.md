# Delivery: specifications, phases, and evidence

This file defines stage structure and execution order. Read the relevant
[work-mode rules](work-modes.md) when selecting directories, checkpoints, or Git
actions, and [verification rules](verification.md) before implementation or review.
Reuse these decisions within a stage; do not reload the process after every edit.

## Minimal task contract

Establish the observable result, scope, compatibility, material risks, and
acceptance criteria from the affected flow and contracts. Reuse agreed decisions.
Ask about missing choices that change behavior or architecture; continue independent
work while waiting. Routine local decisions need no additional approval. Present
substantial design decisions for review before dependent implementation.

A small change needs a few working-plan bullets. For a substantive task, read the
workspace `PLANS.md` ([template](../templates/PLANS.md)) for artifact location,
ownership, content, and progress. Use the [task template](../templates/task.md) or
the adopted native format. When selecting skills, read [Superpowers integration](superpowers.md).
Resume an existing task in its canonical store; workspace navigation carries no
second checklist. Name that store separately from the implementation checkout in
the handoff. Relocation is a separate requested migration, not a delivery prerequisite.
Use the adopted planning policy's [progress semantics](../templates/PLANS.md#progress-and-stopping)
for stable item IDs, completion markers and resumption; an item update does not
introduce another check/review cycle or permission checkpoint.

If a specification is wrong, resolve the affected decision and update criteria
and implementation with the reason recorded. Distinguish current behavior,
required compatibility, and the intended correction; do not re-plan completed
stages or read historical plans without a concrete dependency.

## Delivery techniques

| Technique | Suitable work | Evidence |
| --- | --- | --- |
| Direct edit | Documentation, wording, configuration, or a clear local change | Artifact checks; relevant behavior checks when needed |
| Phased delivery | A feature, integration, or architectural migration | Changed behavior and affected integration checked at the selected verification boundary |
| TDD within a phase | A reproducible bug, domain rule, algorithm, or complex branching | Focused Red–Green–Refactor, with wider checks at the selected verification boundary |

Spec-Driven Development defines expected behavior; TDD defines implementation
order; boundary verification gathers wider evidence. These can be combined.
Superpowers Subagent-Driven Development is a different use of the abbreviation SDD.
Neither phased delivery nor TDD grants automatic progression, worktrees, or commits.

## Phase boundaries

A phase delivers a checkable outcome: a complete scenario, an implemented contract,
or an independently verifiable migration step. Prefer a vertical use case where
practical. Name its affected area, dependencies, criteria, and necessary checks.
An entire backend with testing deferred until later is too broad; each edit is too small.
Necessary tests belong to the implementation phase.

Use `verification.timing` through the verification owner to select the phase/task
batching boundary. Required phase gates and human-checkpoint acceptance stay binding;
a bounded unphased change has the same completion boundary in either setting. Internal
steps and item markers do not each trigger a cycle. Intermediate checks need a concrete reason
under [verification timing](verification.md#what-to-run-and-when), including selected
TDD or a required gate. Define acceptance and necessary checks before implementation;
reuse valid evidence and rerun affected checks after repairs. Keep summaries compact
under the [output policy](verification.md#compact-check-output).

## Phase completion

For an internal phase whose checks are deferred under authorized `task_end`
progression, record implementation progress and pending criteria without claiming
verified completion. Apply the checks and accountable review below at the selected
boundary. A human stage checkpoint still requires its acceptance evidence under
[verification timing](verification.md#what-to-run-and-when).

1. Capture the pre-stage state under [verification](verification.md#before-implementation),
   then complete the assigned scope and selected checks.
2. Perform the accountable review and resolve confirmed findings under
   [review boundaries](verification.md#review-boundaries), including affected
   interactions and required integration checks. Reuse evidence that still applies.
3. Record changed paths, criteria, actual check results and applicable code state,
   limits, and the proposed next stage in the existing plan or handoff.
4. Apply the [work-mode checkpoint](work-modes.md): stop for human review by default;
   advance only within already authorized progression. A reviewable stage includes
   necessary checks and scoped repairs, and is not a claim that the whole task is done.

Repeated failure follows [the diagnostic reset](verification.md#completion-and-lack-of-progress).
It does not waive a defect, required check, or human checkpoint.

## Sources

These are framework stage definitions, not built-in Codex limits.
[Codex best practices](https://learn.chatgpt.com/guides/best-practices),
[PLANS.md](https://developers.openai.com/cookbook/articles/codex_exec_plans), and
[development workflows](https://developers.openai.com/cookbook/examples/codex/iterating-development-workflows-with-codex#agents-and-plans)
provide background; their continuous execution and commit defaults are not adopted.
[TDD](https://martinfowler.com/bliki/TestDrivenDevelopment.html),
[Spec Kit](https://github.github.io/spec-kit/guides/existing-projects.html), and
[OpenSpec](https://github.com/Fission-AI/OpenSpec) describe optional techniques/tools.
