# Change contract

Use for a substantive task under the adopted `PLANS.md` ([template](PLANS.md)).
A small task needs only relevant working-plan points. That policy owns locations,
native artifact navigation and progress; do not duplicate a canonical specification.
Remove unused optional sections. The fields below capture task decisions, not a new process.
When adopting this template at a different location, resolve its reference links
against the installed policy; template-relative paths do not select a task store.
For a task at `docs/plans/<task>.md`, the root policy route is `../../PLANS.md`
and the default helper route is
`../../.agents-framework/standards/superpowers/compatibility.md`. Resolve other
native stores from their actual location instead of moving them to fit this example.

- User outcome: `<observable behavior>`.
- Scope: `<what changes and required compatibility>`.
- Current evidence: `<specific files/symbols; not an architectural ideal>`.
- Target decision: `<responsibilities, interfaces, material constraints>`.
- Acceptance criteria: `<checkable scenarios, including material failure cases>`.
- Delivery technique: `<direct edit / phases / TDD within a phase; rationale>`.
- Planning tools and artifact owner: `<Superpowers / OpenSpec + Superpowers / existing>`.
- Design/spec: `<section in this plan or existing canonical document>`.
- Material uncertainties: `<only those that change a decision>`.

## Global Constraints

- Work mode: direct with a human checkpoint by default; `<explicit exception, if any>`.
- Workspace root: `<absolute instruction/navigation root; Git is optional here>`.
- Canonical task: `<absolute artifact/store location; owner of decisions/progress>`.
- Native tool context, if used: `<supported cwd/store setting resolving that task>`.
- Project execution: `<affected project/repository → current checkout or authorized worktree>`.
- Authorized Git writes: none by default; `<exact grants, if the user gave them>`.
- Model selection: `<workspace routing file; do not hardcode a competing mapping>`.
- Binding requirements: `<versions, exact interface constraints, compatibility>`.

## Stages, when useful

| Stage | Observable result | Owner's scope | Depends on | Necessary evidence |
| --- | --- | --- | --- | --- |
| `<1>` | `<complete scenario/contract>` | `<files/module>` | `<condition or none>` | `<command/inspection and risk covered>` |

Current authorized stage: `<stage>`.
Current item: `<stable item ID — in progress / blocked, with reason when needed>`.
Status: `<planned / in progress / awaiting user review / blocked / complete>`.
Next human checkpoint: `<after this stage, unless automatic progression is explicit>`.
Independent reviewer: `<under the adopted review preference or explicit requirement; within permissions>`.
Review scope: `<task changes/baseline and concrete affected-contract questions>`.
Pre-stage baseline: `<saved contents/prior absence or reproducible references for
affected paths, checkout identity, and existing local edits; capture before writing>`.

Give independent actionable items stable IDs under the adopted planning policy.
Example only: replace these sample outcomes with the task's actual items. Here,
implementation and verification have separate acceptance conditions; if an item's
own acceptance includes tests, it remains unchecked until those tests pass.

```markdown
- [x] S1.1. Implement the agreed behavior.
- [ ] S1.2. Verify the required scenarios.

Current item: S1.2 — in progress.
Stage status: in progress.
```

Update the existing item when its criteria are met, before the next item/handoff;
keep blocked items unchecked and explain reopened or cancelled scope. Preserve a
native task store's own status operations instead of copying this sample into a
competing progress list. The adopted `PLANS.md` owns the complete marker semantics.

## Stage handoff

- Changed: `<paths and important decisions>`.
- Acceptance: `<met criteria and remaining work>`.
- Evidence: `<command/inspection → result, applicable code state>`.
- Deviations or blockers: `<facts without full logs>`.
- Incidental findings, if any: `<location, impact, confidence; outside this task>`.
- Next stage: `<proposal; do not begin while awaiting user review>`.

Keep a short current state record. Stage completion does not complete the whole task.

## Delegated task details, only when needed

Remove this section for inline work. For Superpowers task extraction, use numbered
`Task N` headings below, with one independently assignable scope per heading.
The coordinator supplies a fresh scoped handoff under the bundle's
`standards/orchestration.md` (bundle-relative, not task-relative),
including Global Constraints and permissions. For extraction, read the conditional
[helper reference](../standards/superpowers/compatibility.md); do not duplicate the full spec.

### Task 1: <checkable outcome>

- Authorized stage: `<stage containing this task>`.
- Files and ownership: `<exact paths and scope>`.
- Working directory: `<mapped implementation checkout; absolute canonical task and baseline references>`.
- Interfaces: `<consumed/produced contracts and dependencies>`.
- Acceptance: `<observable scenarios or references to the relevant criteria>`.
- [ ] T1.1. `<Implementation step; exact code only where needed to settle ambiguity>`.
- [ ] T1.2. `<Necessary verification, command/inspection, expected outcome>`.
- [ ] T1.3. Record changed paths, actual evidence, and remaining concerns; return to coordinator.
