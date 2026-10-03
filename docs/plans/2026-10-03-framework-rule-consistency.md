# Framework rule consistency implementation plan

Date: 2026-10-03.

**Goal:** Apply the four audit corrections without introducing conflicting rules
or changing unrelated framework behavior.

**Spec:** [Framework rule consistency corrections](../specs/2026-10-03-framework-rule-consistency.md).

**Method:** Execute inline using Superpowers `writing-plans`, `executing-plans`
and `verification-before-completion`, with the adaptations in
[the framework policy](../../standards/superpowers.md). Documentation needs scoped
artifact checks and accountable review, not a new application test suite.

## Global constraints

- Workspace/instruction root and execution checkout:
  `/home/vitalii/Documents/Local_Projects/Agent_Engineering_Kit`.
- Canonical spec and progress owner are the two linked documents in `docs/specs/`
  and `docs/plans/`; this plan is the sole progress record.
- The user authorized specification, planning and staged application of these
  corrections. Execute stages 1–3 sequentially, checking each before advancing.
- Direct current-checkout execution; no staging, commits, branches, worktrees,
  deployment, target adoption, model setup or delegation.
- Preserve the existing uncommitted naming edits in `standards/core.md`,
  `templates/AGENTS.root.md` and `templates/policy-entry.md`.
- Pre-edit baseline, including dirty file contents and prior absence of these
  two documents: `/tmp/aek-rule-consistency-4k5i1a6g/manifest.json` and scoped copies.
  Repository HEAD at capture: `19f6a8558050aee4442112ce7e16c7af0fc2d593`.
- English artifacts, Russian user-facing reports. Historical records are not
  rewritten to match current resource counts.
- Each stage preserves mandatory project/CI gates, existing compatibility
  contracts, conditional reading and the separation of bundled and active resources.

## Stages

### Stage 1: Target compatibility and React verification

Requirements: R1 and R2.

- [x] Update `standards/pydantic/verification.md` to distinguish the example's
  interpreter floor from the target project's supported Python range.
- [x] Update `standards/react/verification-compatibility.md` to select E2E by
  material coverage or required gates; retain scoped real-browser obligations.
- [x] Check affected links/Markdown and `git diff --check`; inspect the scoped diff.
- [x] Walk through Python 3.10 adoption, pure calculation, browser focus/navigation
  and mandatory-E2E scenarios; record results before stage 2.

### Stage 2: Cohesion-based size decisions

Requirement: R3; consumes the unchanged shared verification/gate policy.

- [x] Update the size table and decomposition guidance in `standards/core.md`:
  mandatory review and documented cohesive exception above 700 lines; independent
  responsibilities still require extraction within the authorized scope.
- [x] Replace the unconditional size shorthand in `templates/AGENTS.root.md`
  with a route to the owning core policy.
- [x] Check affected links/Markdown and `git diff --check`; inspect against the
  captured dirty-file baseline, preserving all naming additions.
- [x] Walk through cohesive/mixed 800-line components, a bounded legacy fix and
  an explicit size gate; record results before stage 3.

### Stage 3: Catalog-owned Unreal resource list

Requirement: R4.

- [x] Replace duplicated numeric counts in `MIGRATION.md`, `ARCHITECTURE.md`,
  `README.md`, `standards/unreal-engine.md`, and `standards/catalog.md` with
  catalog-owned resource references.
- [x] Parse `standards/catalog.toml` using `tomllib`; verify that all declared
  Unreal resources exist and that the catalog is unchanged from the audit state.
- [x] Check affected links/Markdown and `git diff --check`; search the active
  documents for stale six/seven-resource wording and review the scoped changes.
- [x] Confirm optional skills remain bundled references and conditional reading
  remains intact; finish the acceptance/evidence record and report the result.

## Verification approach

At each stage, use a temporary Python artifact checker outside versioned source
to resolve local Markdown links and fragments, validate fenced-block balance and
report failures with nonzero status. Resolve template links from their declared
installation base where applicable. Run `git diff --check` for whitespace.
Use baseline comparisons for attribution, since HEAD excludes earlier naming work.

Review semantic scenarios against R1–R4 once at their owning stage. Do not assert
that a textual scenario walkthrough proves runtime compliance. Reuse successful
checks while their inputs remain unchanged; check later reporting edits only for
their own affected structure and links.

## Progress and handoff

- Preparation: specification and plan written; requirements mapped to stages 1–3.
- Current stage: all three stages complete.
- Status: complete; ready for user review.
- Stage 1 evidence: artifact checker passed for the spec, plan and two changed
  profiles (4 files, 17 local references); `git diff --check` passed. Scoped diff
  review confirmed that Python 3.10 support is not raised, examples retain their
  3.11 limit, pure calculations can use focused checks, browser-dependent changes
  retain browser checks and mandatory E2E gates remain binding. These are static
  scenario assessments, not executed application or agent-compliance tests.
- Stage 2 evidence: artifact checker passed for core, root template and plan
  (3 files, 25 local references); whitespace check passed. Baseline diff review
  confirmed that a cohesive 800-line component needs a recorded rationale, mixed
  responsibilities still require extraction, a small legacy fix stays bounded and
  an explicit size gate remains binding. The prior naming section was compared
  with the captured baseline and is byte-identical. A subsequent prose line-wrap
  adjustment changes no rule or link and is included in stage 3 artifact checking.
- Stage 3 evidence: artifact checker passed for the five resource-list documents,
  core's line-wrap adjustment and the plan (7 files, 144 local references);
  `git diff --check` passed. Catalog bytes match the unchanged repository version;
  `tomllib` parsing and resource inspection confirmed all seven current Unreal
  resources, including `skills.md`. The active scope has no remaining six/seven
  resource-count wording. Scoped review confirmed that catalog availability,
  conditional reading and optional skill installation remain distinct.
- Verification tool: `python3 /tmp/aek-rule-consistency-4k5i1a6g/check_artifacts.py`
  with each stage's listed files. Successful results apply to their recorded
  contents; the final progress-only edit requires only a plan artifact check.
- Acceptance: R1–R4 satisfied by the scoped edits and static scenario review;
  no unresolved in-scope findings. No runtime/client adherence is claimed.
- Delivered: nine existing policy/overview/template files updated and the two
  requested specification/plan documents created. Earlier naming changes are
  retained; `templates/policy-entry.md` received no additional edits in this task.
- Final checkpoint: user review of the completed corrections and recorded evidence.
