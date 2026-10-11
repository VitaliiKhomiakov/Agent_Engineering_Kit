---
name: aek-implement-feature
description: Use when implementing an authorized feature, code change or settled bug fix in a project with adopted AEK rules. Excludes design-only or review-only requests, wording-only edits and framework or model setup.
---

# Implement a project change

Apply the affected project's technical rules to the authorized change. Use the
[project-skill contract](../../../standards/project-skills.md) for local inputs,
procedure composition and the implementation result. Resolve this link from the
installed skill folder: contained Codex adoption uses
`../../../.agents-framework/standards/project-skills.md`; other layouts use their
actual bundle placement. The source checkout is not a task-time dependency.

1. Resume the canonical task and authorized stage with its acceptance criteria,
   accepted design, baseline and project constraints. A settled small fix can
   proceed directly; a missing material design decision follows the existing
   delivery rules before dependent implementation.
2. Select the affected stack's local entry and relevant topic sections. Connect
   them to the owners, interfaces, state/resource lifetimes and verification gates
   touched by this change. Follow an affected caller or consumer when needed to
   preserve its contract; do not infer optional frameworks from a language.
3. Continue the selected execution procedure through local Superpowers adaptations
   when applicable. Apply the chosen test cadence and review boundary from their
   existing owners; loading this entry adds no separate TDD cycle, worker or plan.
4. Implement within the authorized scope, preserving unrelated changes and accepted
   exceptions. Record actual behavior and acceptance evidence in the canonical
   task/result, including unavailable gates and unresolved material findings.

Completion and the next stage follow the existing work mode and verification
rules. This entry does not authorize Git writes, setup, model reassignment or
consumer changes beyond the requested implementation.
