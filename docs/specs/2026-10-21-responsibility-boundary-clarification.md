# Clarify function extraction and Unreal module boundaries

## Purpose and scope

Resolve the two ambiguities identified in the user's requested review on
2026-10-21. A meaningful step must not automatically require a helper function,
and a meaningful responsibility must not automatically require an Unreal module.
Preserve early separation of independent responsibilities and justified extraction.

This is a proposed correction, not an active standard. The user requested a
specification and plan; this stage does not implement the policy changes.
The existing [implementation plan](../plans/2026-10-21-responsibility-first-implementation.md#review-follow-up--2026-10-21)
owns progress, authorization, baselines and executed evidence. This specification
owns the follow-up design and acceptance cases; it adds no second checklist.

## Confirmed ambiguities

- [Small methods and functions](../../standards/core.md#small-methods-and-functions)
  makes a meaningful purpose or independent inputs sufficient wording for extraction.
  Readers can demand helpers for cohesive steps even though
  [responsibility placement](../../standards/core.md#responsibility-placement-before-implementation)
  permits them to remain together. The Go grouping example exposes that ambiguity.
- [Unreal modules](../../standards/unreal-engine/build-assets.md#modules-and-build-inputs)
  allows a module for a meaningful responsibility or a loading/deployment boundary.
  The common rule requires a reason for the stronger boundary beyond file organization.

These are instruction-interpretation risks, not observed runtime failures or proof
that an agent would necessarily choose the wrong boundary.

## Chosen correction

Change the two existing rule owners. Adding links alone would leave the broad
triggers intact; copying new prohibitions into every role/profile would create
overlapping policy owners. Keep existing anchors, routes and size settings.

### Function extraction

In `standards/core.md#small-methods-and-functions`, replace the extraction bullet
with wording that has the following meaning; the rest of that section remains:

> Extract a block when doing so resolves a concrete problem: mixed independent
> responsibilities, an actually reused rule without a suitable existing owner,
> or detail/complexity that obscures the caller's purpose. A nameable step or
> separate inputs alone does not require a helper. Choose the appropriate owner
> under responsibility placement and split independent responsibilities even below
> the size threshold. Above `size.function_review_lines`, actively assess extraction;
> a straightforward cohesive operation may remain with an explained reason.

Link "responsibility placement" to the existing canonical section. The condition
does not make reuse necessary: a single-use helper remains appropriate when it
clarifies obscuring detail or separates an independent responsibility. Preserve
the existing rules for explicit contracts, related helpers and reuse of owners.
Whitespace grouping remains owned by Go style; do not copy its example into core
or change a correct grouped function merely to satisfy an extraction preference.

### Unreal module choice

In `standards/unreal-engine/build-assets.md#modules-and-build-inputs`, retain the
runtime/editor separation requirement and replace the ambiguous module trigger:

> Apply responsibility placement when deciding whether to add a module. Require a
> concrete need for separately controlled dependencies or public exposure, module
> loading/lifecycle, or target/platform inclusion. A meaningful responsibility alone
> is insufficient; use cohesive files in an existing suitable module when those
> boundaries remain shared. Do not create a module for every small class.

Link "responsibility placement" to core. Target/platform inclusion and editor-only
code are Unreal-specific dependency/deployment boundaries; module lifecycle means
module loading and unloading, not the lifetime of each Actor or Component. Keep
public/private dependency declarations, acyclic imports and engine-owned construction
unchanged. An existing justified module does not require consolidation under this rule.

### Compatibility and authority

These are AEK design criteria, not language/engine restrictions. Epic's
[Unreal Engine Modules documentation](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-modules),
labelled 5.8 when reviewed on 2026-10-21, describes dependency/exposure, loading and
target/platform controls and also permits modules for organization. The narrower
creation criterion above is AEK policy. The version-query URL could not be retrieved;
the linked current page was accessible. No engine build or older-version run was made.
Keep the repository's existing target/version conditions; this change introduces
no API, module descriptor, toolchain, dependency or supported-version-floor change.

## Acceptance cases

Evaluate these against the implemented wording during the existing scoped review.
These are specified expected outcomes, not executed tests or a model evaluation.

| ID | Scenario | Required outcome |
| --- | --- | --- |
| BC-1 | The existing grouped `livenessRouter` has creation, configuration, registration and final-result steps | No extraction finding solely because the steps are nameable. Its compact variant still violates the existing Go spacing rule. Keep both judgments distinct. |
| BC-2 | A single-use calculation's detailed algorithm obscures its caller's operation | Extraction remains supported by the concrete readability problem, even without reuse or a crossed size threshold. Do not invent a helper solely for an obvious step. |
| BC-3 | A short function/file mixes transport handling and an independently owned storage adapter | Separation remains required at an appropriate owner/boundary; the cohesive-step exception must not excuse mixed independent responsibilities. |
| BC-4 | The task needs a business rule already implemented by a suitable owner | Reuse that owner. Do not extract a parallel implementation merely because a local block could be named. |
| BC-5 | A new cohesive gameplay responsibility shares its existing module's intended dependencies, exposure, target inclusion and loading | Separate cohesive files can express ownership. A proposed extra module justified only by the responsibility's name or file organization is insufficient under AEK policy. |
| BC-6 | Editor-only tooling would otherwise become a runtime dependency | Preserve the required editor/runtime boundary; use a suitable existing editor module or establish the missing boundary. Moving files alone must not hide the dependency. |
| BC-7 | A capability requires separate dependency/public exposure, module loading, or target/platform inclusion | A module boundary is justified when it supplies that required control. Reuse a suitable existing boundary first; do not demand all listed reasons simultaneously. |
| BC-8 | Unchanged/moved code has prior review evidence; or a small legacy fix exposes unrelated decomposition debt | Reuse evidence only while code, context and the clarified criterion match. Inspect a missing coverage gap in scope; no automatic consolidation, repository-wide refactor or repeated design round. |

## Delivery and verification limits

Operational changes are limited to the two owner files. Shared roles, verification,
Go style, other profiles, native adapters and catalog IDs already route to them and
need no duplicated correction. New integrations receive the existing core and selected
Unreal resources. Existing integrations use the normal
[B/C/N update procedure](../../MIGRATION.md#repeat-and-update) with local adaptations preserved.

Use the plan's scoped artifact checks and scenario assessment. Do not introduce a
new linter, exact-word unit tests, agents or review rounds for these prose changes.
Artifact checks can validate supported syntax, resources and links; recognizing
cohesion, obscuring complexity and a necessary boundary still requires judgment.
