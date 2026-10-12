# Configurable specialized agents in adopted projects

## Status and scope

Current stage: S2/S3 complete; library changes await user review at the
stage boundary. The user accepted the design and requested prepared agent
instructions informed by official examples. This document remains the canonical
design, plan and progress owner.

Instruction root and execution checkout:
`/home/vitalii/Documents/Local_Projects/Agent_Engineering_Kit`.
Canonical artifact: `docs/plans/2026-10-12-specialized-agent-adoption.md` in that
checkout. Coordinator owns progress; execution is proposed inline under the
[local Superpowers adaptations](../../standards/superpowers.md).
The checkout was clean at baseline
`0503133c585d61b9ed8b6dfe158b954e91e3db25`; this document was absent.
Default direct mode applies: no staging, commits, branches or worktrees.
No target project or live model assignment has been selected for this task.
The source routing template is an example, not this session's configuration.
The pre-implementation copy of this previously untracked plan is preserved in
`/tmp/aek-specialized-baseline-mky2kjjm/2026-10-12-specialized-agent-adoption.md`.
Tracked inputs still match the recorded baseline; new architect and research
files were absent. No target configuration or worker launch is authorized here.

## Outcome and agreed requirements

AEK must supply reusable specialized agent roles for adoption into both new and
existing projects. Each enabled role must support independently selected model
and reasoning effort, using the existing setup and reassignment mechanism.
The user's article describes custom agents launched as subagents, not a team of
independently managed client sessions. Keep native client execution and AEK's
instruction-library scope.

The proposed minimal set is the existing coordinator and implementer/reviewer
roles plus an optional architect. Selection does not require all roles to run.
Architecture assistance is conditional on a material design need; independent
review follows the existing risk-based/project policy. Small tasks may stay inline.

## Design

### One configuration contract

Retain routing schema version 2 and `roles.<id>.enabled`, `model` and
`reasoning_effort`. The existing contract already supports `architect`; no new
schema, parallel settings file or model-selection skill is needed. Keep
`aek-model-setup` and `aek-model-reassign` as the setup and change entry points.

Add an optional disabled architect to the inactive routing example. Keep its
model/effort values explicitly illustrative, preserving current assignments for
other example roles. During adoption, obtain the target user's missing choices
for each selected role and check model/effort support together. Do not assign
models from this plan, the article or a copied example. Same-model roles are valid.
Unsupported pairs remain unresolved; no silent fallback or effort reduction.

For Codex, map the selected architect to `.codex/agents/af-architect.toml` with
explicit `model` and `model_reasoning_effort`, as for the existing specialists.
Keep native formats and supported effort values client-specific. Claude Code
and Cursor retain the existing native mapping procedure; this stage extends
the Codex template set without claiming new tested native templates for them.

### Architect responsibility and handoff

The architect receives the bounded outcome, affected paths, relevant current
decisions, canonical task and applicable engineering rules. It returns the
smallest justified design: owners, interfaces, compatibility, material tradeoffs,
acceptance cases and sufficient implementation steps. It reports a concrete
blocker instead of reopening settled decisions or investigating the whole project.

The new native template uses supported read-only sandbox defaults and prohibits
application edits. The coordinator records its returned design in the existing
canonical artifact; this role does not require write access or create a second
plan. Effective parent/session permissions must still be checked before claiming
enforced read-only access.

Use `aek-design-feature` only when selected and available through the adopted
project entry. Otherwise follow existing design/delivery rules directly. Do not
make the optional `project-workflows` profile or Superpowers installation a
requirement for this agent. The existing reviewer has the analogous optional
review entry. Native role files route to policy owners instead of duplicating
their full procedures; no mandatory architect/developer/reviewer pipeline.

### Adoption and update

The existing [migration procedure](../../MIGRATION.md#model-selection-step) remains
the single entry for new projects, first integration into existing projects and
updates. The [model owner](../../standards/model-configuration.md) retains field
semantics, enablement, native agreement, recovery and runtime reporting.

| Situation | Required outcome |
| --- | --- |
| New project or first adoption without saved choices | Include optional specialized roles in the existing model-selection step; prepare selected pairs and native destinations, or retain an explicit deferral |
| Existing configured project | Reuse saved roles, pairs, edges and ceiling; adding an available architect template does not enable it |
| User adds or reassigns an architect | Change only the requested role/pair, permitted edge and affected managed native settings through the existing setup/reassignment contract |
| Preparation only | Produce reviewable proposed contents outside the target; do not create the target, install roles or activate configuration |
| Ordinary repeat/update | Preserve assignments, unrelated agents/settings, accepted local adaptations and canonical task; do not restart onboarding |
| Single-agent or disabled specialist | Install no active specialist for that selection; do not bypass it through an anonymous worker |

Apply the recorded bundle layout to role instruction paths and installed skill
routes, including contained, flat and custom imports and independently opened
repositories. Preserve original contents/absence and reconcile collisions or
intervening edits before authorized writes. Keep migration's existing partial
recovery procedure and v1/unknown-version handling.

## Implementation stages and acceptance

- [x] S1: Complete and verify this design/plan for user review.
- [x] S2: Implement the specialized-role extension as one coherent library stage.
  Add `templates/codex/agents/af-architect.toml`; update
  `templates/framework/model-routing.toml`, `templates/codex/README.md`,
  `standards/catalog.toml`, `standards/model-configuration.md`,
  `standards/orchestration.md`, `MIGRATION.md` and `ARCHITECTURE.md` where their
  existing ownership requires it. Refine implementer/reviewer instructions and
  add dated source evidence in `docs/research/2026-10-12-specialized-agent-instructions.md`.
  Use a read-only native default for the reviewer as well as the new architect;
  retain the effective-permissions caveat. Setup/reassignment skills already accept
  arbitrary selected roles; preserve them unless inspection finds an actual gap.
  Acceptance: the architect is available but disabled by default, pairs remain
  independently selectable, and new/existing-project adoption uses one procedure.
- [x] S3: Verify S2 at its completion boundary and report for user review.
  Extend `tests/test_project_skill_portability.py` only for the new architect's
  native instruction routes and preservation of its model/effort during layout
  adaptation, reusing the existing fixture mechanism. Check source resources,
  affected links/TOML, profile selection and existing adoption fixtures. Review
  disabled-role, missing-pair, collision, reassignment and prepare-only cases
  against the policy text. Do not present fixture construction as an installer
  or tests of native activation/agent behavior.

S2 and S3 form one implementation/checkpoint stage after review of S1; S3 is its
verification item, not a separate approval or extra review cycle. Use inline
execution as the existing missing-selection fallback; no delegation is needed
to edit this closely related instruction scope. A target installation is a
separate task requiring an identified destination and target model choices.

## Verification and evidence limits

For S1, run the artifact checker on this document, inspect its complete contents,
and check whitespace including the new untracked file. No runtime tests apply.
For S2/S3, planned commands are:

```sh
python3 tools/check_instruction_artifacts.py
python3 tools/check_instruction_artifacts.py MIGRATION.md ARCHITECTURE.md docs/plans/2026-10-12-specialized-agent-adoption.md
python3 -B -m unittest tests.test_profile_selection tests.test_project_skill_adoption tests.test_project_skill_portability
git diff --check
```

Inspect new files separately and parse the architect's native TOML; inspect its
developer-instruction path literals because Markdown link checks do not cover
them. If executable checker behavior is changed, select its regression tests
as well; such a change is not currently required.

Official [Codex custom-agent documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents#custom-agents)
was inspected during this conversation on 2026-10-12. It supports project-scoped
TOML roles and per-role model/effort settings; parent runtime overrides can affect
permissions. This is source evidence, not proof of support in a target account
or installed client. No native agent execution, target installation, token-cost
comparison or runtime enforcement test has been performed.

## Stage evidence

S1: requirements and scope reviewed against the existing owners and templates.
The explicit-path artifact checker passed with 1 artifact and 0 errors.
`git diff --check` passed; the new-file `git diff --no-index --check` comparison
reported no whitespace diagnostics (exit 1 indicates the added file differs).
S1 was accepted by the user's subsequent request to prepare the instructions.
S2: added the inactive architect, refined implementation/review contracts, added
read-only defaults and integrated availability into the existing catalog/adoption
routes. Role IDs, schema v2, enabled examples and existing model/effort suggestions
are preserved; the architect is disabled. Source guidance and limits are recorded
in the dated research note. No live native configuration or consumer project changed.
S3: portability fixtures now inspect all three roles, including preservation of
model/effort/permission fields during route adaptation. Completed checks:

- `python3 tools/check_instruction_artifacts.py`: 210 artifacts, 0 errors.
- Explicit artifact check of MIGRATION, ARCHITECTURE, this plan and the new
  research note: 4 artifacts, 0 errors.
- `python3 -B -m unittest tests.test_profile_selection tests.test_project_skill_adoption tests.test_project_skill_portability`:
  44 tests passed. This includes contained/flat/custom paths, independently opened
  fixtures, preservation of local files and prepare/repeat behavior.
- `git diff --check`: no whitespace errors. New files inspected separately.
- Coordinator reviewed tracked changes against the recorded baseline and the
  complete new files, including optional-role enablement, independent pairs,
  missing skills, read-only output ownership and new/existing adoption routes.
  No unresolved material finding remains within this scope.

Tests verify artifacts and fixed fixtures, not an installer or model behavior.
No independent agent review or native runtime trial is claimed. Final wording
clarifies that an implementer follows supplied decisions without requiring a
design for every task, and that reviewer findings retain impact as well as evidence;
these edits do not change tested routing or field-preservation behavior.
The library stage is complete; any target adoption needs its destination and
selected roles/pairs. No target installation is pending within this source task.
