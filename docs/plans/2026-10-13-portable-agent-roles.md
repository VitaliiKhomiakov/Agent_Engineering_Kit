# Portable agent roles implementation plan

## Task and current state

Goal: make architect, implementer, and reviewer templates available for Codex,
Claude Code, and Cursor while maintaining one shared instruction body per role.
Design authority: [specification](../specs/2026-10-13-portable-agent-roles.md).
This plan is the sole owner of progress, authorization and stage evidence.

Status: stage I complete; user requested commit and push on 2026-10-13.
Current authorized stage: I — source implementation and verification.
Current item: none in progress; D1–D2 and I1–I4 complete.
Next action: commit the reviewed task changes and push the current branch.
The user requested both artifacts together; no intermediate approval is needed
to draft the plan. The subsequent instruction to implement authorized stage I.

## Global constraints

- Instruction root and AEK execution checkout:
  `/home/vitalii/Documents/Local_Projects/Agent_Engineering_Kit`.
- Canonical progress owner: this file under that root; design owner: the linked
  specification. The coordinator owns updates. No other task store is introduced.
- Direct mode in the current checkout. The user's post-implementation instruction
  authorizes staging, committing these task changes and pushing the current branch.
  No new branches/worktrees, target installation, client upgrades or global changes.
- The user authorized implementation of stage I. Target adoption and delegation
  remain outside this assignment.
- No saved `.agents-framework/model-routing.toml` exists here. Use the current
  session inline; do not install sample assignments or spawn specialists for this plan.
- Preserve catalog schema 1, routing schema 2, role IDs and Codex native paths.
  Existing standards remain the owners of shared policy and Superpowers adaptations.
- Preserve role behavior and accepted project customizations. Common bodies have
  no client-specific model/tool settings; adapters do not duplicate full role policy.
- Documents are English; user-facing communication is Russian. Historical evidence
  retains its original date and scope.
- Planning baseline: clean checkout at
  `12f92ffb4ba359e90cc7ad45ae47fd16969e1cf7`; both new documents were absent.
  Their prior absence is recorded outside edited files in
  `/tmp/aek-portable-agents-baseline-ka70122a/baseline.json`.
  Capture a new scoped baseline, including intervening edits, before stage I.

## Stages and progress

| Stage | Outcome | Dependencies | Checkpoint |
| --- | --- | --- | --- |
| D — design | Reviewable specification and actionable plan | User request and current source inspection | Deliver documents; no implementation |
| I — source implementation | Shared bodies, nine adapters, adoption routes and regression coverage | Reviewed design and authorization to implement | Necessary checks and scoped review, then user handoff |

Stage I is one coherent library change: its internal items share role paths and
catalog/adoption contracts and do not require separate workers or human stops.
Verification is batched at the phase boundary except focused regression checks
needed to establish or diagnose a contract. Use `executing-plans` with the local
Superpowers adaptations if inline implementation is later authorized.

- [x] D1. Inspect current role templates, native mappings, catalog and portability
  tests; prepare the proposed architecture and implementation sequence.
- [x] D2. Check both new documents, review acceptance coverage and record evidence.
- [x] I1. Extract the three common bodies and compose all three clients' adapters.
- [x] I2. Integrate catalog, adoption/update routes and maintenance documentation.
- [x] I3. Add focused parity/portability regression coverage and run required checks.
- [x] I4. Review actual scoped changes, record evidence/limitations and deliver the stage.

## I1 — shared bodies and native adapters

Create `templates/agents/README.md`, `architect.md`, `implementer.md`, and
`reviewer.md`. Extract the corresponding existing Codex behavior into each body;
retain focused links to authoritative standards instead of copying shared policies.
The README defines instruction-root-relative adapter routes and body-relative
policy links, explicit loading, missing-input behavior and inactive-source status.

Convert the three existing `templates/codex/agents/af-<role>.toml` files into thin
adapters without changing example role identities or model/effort choices. Add:

- `templates/claude/agents/af-architect.md`
- `templates/claude/agents/af-implementer.md`
- `templates/claude/agents/af-reviewer.md`
- `templates/cursor/agents/af-architect.md`
- `templates/cursor/agents/af-implementer.md`
- `templates/cursor/agents/af-reviewer.md`

Each adapter must contain its matching body route and an explicit instruction to
read it before role work. Retain immediate architect/reviewer no-edit safeguards.
Review native metadata and restrictions against the official sources identified
in the specification and the selected client/version when available. Use simple
documented scalar YAML frontmatter, sufficient for these templates, rather than
advanced YAML constructs or an invented include key. Mark any illustrative native
model setting as unselected and require adoption to resolve the actual pair.

Input: the current role bodies and specification sections on composition/loading.
Output: three common bodies, their composition guide and nine adapters with stable
role IDs and exact local routes. No native files outside `templates/` are installed.
Acceptance: A1 and A4, plus the loading behavior required by A2/A3.

## I2 — bundle and adoption integration

Depends on I1's exact body and adapter paths. Modify these owners:

| File | Required change |
| --- | --- |
| `standards/catalog.toml` | Add common bodies/guide and six new adapters to `model-configuration` resources; retain existing IDs and schemas |
| `standards/model-configuration.md` | Route all clients to their adapters and shared bodies; retain pair selection, restrictions and activation boundaries |
| `templates/codex/README.md` | Describe the common body dependency and link to the composition guide; remove the obsolete embedded-body-only description |
| `MIGRATION.md` | Specify adapted body routes, managed shared content, enabled-client selection, legacy customized-body reconciliation and partial-update handling |
| `ARCHITECTURE.md` | Describe shared role instructions with client-specific adapters and source-template/runtime evidence limits |
| `docs/maintenance/verification.md` | Document new regression commands and precisely bounded YAML/route checks; retain the Codex-only routing-checker limit |

Inspect `standards/orchestration.md` and setup/reassignment skill entries for
Codex-only wording that contradicts the new composition. Change only affected
routes; do not duplicate the installation procedure into every skill or rewrite
unchanged lifecycle policy. No new skill is introduced.

Describe how to compare locally customized embedded Codex instructions against
accepted contents before switching to a shared body. Cover body-first dependency
availability, originals/absence for recovery, collisions in alternate native
discovery directories, and shared-body changes even when adapter bytes are unchanged.
Existing MIGRATION remains the owner; this task adds no automatic merge engine.

Output: portable catalog closure and one consistent adoption/update procedure.
Acceptance: A2, A5 and A6, with final executable coverage in I3.

## I3 — focused regression coverage and checks

Depends on I1/I2. Extend the existing fixed-fixture approach; do not build an
installer inside tests. Add `tests/test_agent_templates.py` for source composition
and known native-template syntax, and update `tests/test_project_skill_portability.py`
where its Codex embedded-policy assumptions must become adapter/body route checks.
Reuse existing fixture utilities; adjust `tests/test_project_skill_adoption.py`
only if its shared helper needs the new literal-route adaptation. Add catalog
closure assertions in `tests/test_profile_selection.py` only where existing
resource checks do not already cover the added dependency.

Test observable contract failures rather than exact prose or line-count quotas:

| Scenario | Expected evidence |
| --- | --- |
| Three roles across three clients | Unique matching identities/body references; common body exists, remains outside native discovery and has reachable policy links |
| Body missing or wrong-role route | The fixture's validation reports the dependency/mapping failure rather than accepting a nonempty adapter |
| Contained, flat and `rules/aek` bundles | Both adapter-to-body and body-to-policy routes resolve from their declared bases; stale `.agents-framework/` routes fail |
| Independent child root / different cwd | Required routes stay inside the prepared project and do not rely on the original AEK checkout |
| Explicit selection, one disabled role, single-agent | Candidate native files contain only the selected client's enabled roles; unselected templates remain inactive |
| Prepare-only and repeated candidate | Existing and absent targets remain untouched; repeat preparation is stable and preserves fixed local settings/role sentinels |
| Common body revised | All matching adapters continue to reference that one body; no stale embedded procedural copy is treated as authoritative |

Use `tomllib` for Codex. For the fixed Markdown templates, inspect a deliberately
limited scalar frontmatter subset and reject malformed/unsupported fixture syntax;
do not call that a general YAML or native-client validator. Keep Python standard
library dependencies unless a concrete requirement and reviewed decision justify
otherwise. Behavioral parity needs scoped source review in addition to route tests.

Run the necessary source and regression checks from the repository root:

```sh
python3 tools/check_instruction_artifacts.py
python3 -m unittest discover -s tests -p 'test_agent_templates.py'
python3 -m unittest discover -s tests -p 'test_project_skill_portability.py'
python3 -m unittest discover -s tests -p 'test_project_skill_adoption.py'
python3 -m unittest discover -s tests -p 'test_profile_selection.py'
python3 -m unittest discover -s tests -p 'test_model_routing.py'
git diff --check
```

Run the documented strict mypy command on the affected Python files and their
shared helpers, adding the new test file to that command. Run
`test_instruction_artifacts.py` if the checker is actually changed; a checker
change is not otherwise required. Explicitly check new dated documentation because
default artifact selection excludes `docs/` bodies. Inspect new files separately.
Unavailable tooling must be reported without claiming its check passed.

Output: current-state static evidence for A2–A5 and A7–A8. Existing application
examples need no stack builds. Target-native agent execution is not implied by
fixture preparation; no paid/client trial is required just to maintain the library.

## I4 — scoped review and handoff

Depends on I1–I3. Compare the actual diff and new files with the implementation
baseline. Account for the original architect/implementer/reviewer obligations,
client-specific restrictions, path bases, dependency closure and preservation of
accepted local changes. Review the specification's concrete failure questions.
Resolve in-scope defects and rerun only invalidated checks.

Apply the existing risk-based independent-review policy within actual permissions
and configured role availability. Do not create a reviewer assignment, substitute
an anonymous worker or claim an independent opinion merely to close this item.
Record any required unavailable review explicitly.

Create `docs/research/2026-10-13-portable-agent-roles.md` for new evidence if execution
occurs on this date; otherwise use the actual execution date and record that path
here. Record official contracts checked, source/fixture checks, observed local
versions if inspected, and unexecuted native loading/permission/model trials.
Do not rewrite the previous specialized-agent or client-capability evidence.

Output: acceptance A1–A8 accounted for, checks and limits recorded, implementation
stage awaiting user review. Target adoption remains a separately scoped request.

## Design-stage evidence and handoff

2026-10-13: inspected existing Codex definitions, native mapping/adoption policy,
catalog resources and portability tests. Reviewed official native format pages
listed in the specification. No clients or child agents were launched and no
role templates, settings or implementation files were changed in this stage.

Validation: the artifact checker on these two documents returned
`Checked 2 artifacts; 0 error(s).`; `git diff --check` passed, and a separate
new-file whitespace inspection found no trailing whitespace. Read both complete
new files and checked scope, path bases, acceptance-to-item coverage, update
preservation and source/static/runtime evidence boundaries. Corrected wording
that could imply an already accepted design decision. Only these two new documents
are present in the task diff; no implementation checks or runtime trials are claimed.

At the design-stage checkpoint, implementation items remained unchecked and the
documents were delivered for review. The user subsequently authorized implementation.

## Implementation-stage record

Baseline: `/tmp/aek-portable-roles-impl-2_2x7m8y/baseline.json` records existing
contents and prior absence for affected paths; copies include the untracked design
documents. Tracked files were clean. I1 produces the body routes used by I2 and
I3; catalog closure and adoption mappings must be updated together. No conflicting
interfaces were found. Selected test-first coverage for the new resource contract
failed as expected because the common architect body was absent from the catalog.

I1/I2 complete: three common bodies, nine native adapters and catalog/adoption
routes are present. The six new static template tests pass. Client settings remain
in native adapters; no native installation or model assignment was performed.
I3 is checking affected existing suites and strict typing before the stage review.

## Implementation checkpoint — 2026-10-13

I3/I4 complete. Acceptance A1–A8 is covered at the agreed source/static level:
three preserved shared procedures, nine adapters, catalog closure, portable routes,
explicit selection fixtures, adoption/update policy and scoped parity review.
Source changes remain in the current checkout for user review, without Git writes
or native installation. Setup/reassignment skill entries already route to the
updated model-configuration owner and needed no duplicate procedure. Existing
catalog checks cover the added resources; no profile test or production checker
change was necessary.

Evidence:

- Source artifact check: 220 artifacts, zero errors. Explicit six-document check:
  zero errors. New/untracked files were read and separately checked for whitespace.
- `tests.test_agent_templates`: 6 tests passed; the initial missing-resource test
  failed before the common bodies/catalog resources were added.
- Existing `test_project_skill_portability`, `test_project_skill_adoption`,
  `test_profile_selection` and `test_model_routing`: 63 tests passed.
- Strict mypy 2.1.0 with the documented flags: no issues in eight source files.
  Used `/tmp/aek-portable-roles-mypy/bin/python3`; tools were installed only there.
- `git diff --check`: passed. Compared actual tracked changes and new files to
  the scoped baseline, preserving the initial untracked specification/plan.
- Normalized extraction comparison preserved each original role procedure.
  Scoped source review covered all adapters, restrictions, path bases, shared
  dependencies and update preservation; no unresolved in-scope finding remains.

Only source/template behavior and fixed fixtures were assessed. No independent
reviewer was dispatched under the unchanged inline/no-saved-routing arrangement;
the coordinator review is not an independent opinion. No native loading, effective
permission or runtime model trial is claimed. These target-dependent observations
remain unverified, as allowed by the specification's source-readiness boundary.
New evidence: [portable role composition](../research/2026-10-13-portable-agent-roles.md).
The source implementation has no remaining planned items; target adoption is a
separate user-scoped task.
