# Framework rule consistency corrections

Date: 2026-10-03. Scope authorized by the user's request to write the specification,
plan and apply the audit corrections in stages.

This specification owns requirements. The [implementation plan](../plans/2026-10-03-framework-rule-consistency.md)
owns progress, baselines and verification evidence.

## Outcome and scope

Agents receive consistent guidance on target Python compatibility, React browser
checks, component size and the complete Unreal resource bundle. Correct the two
documentation defects and two policy ambiguities identified in the preceding audit.
Retain the recently added responsibility-based naming rules.

This is a documentation change. It does not install rules in a target project,
upgrade dependencies, change model settings, introduce a checker application or
require application/engine execution. Historical research and completed plans
remain dated evidence rather than current policy owners.

## Requirements

### R1. Separate example versions from target compatibility

In [Pydantic verification](../../standards/pydantic/verification.md#versions-and-migration),
keep the recorded example versions as historical execution evidence. Remove the
statement that the workspace's minimum Python version is 3.11. The target project's
declared support range and actual deployment determine compatibility, following
the [Python policy](../../standards/python/verification.md#version-sensitive-decisions).
Importing this profile does not raise that range.

Acceptance: a target supporting Python 3.10 is not assigned a 3.11 floor by this
profile. Examples requiring 3.11 remain labelled and are not silently treated as
compatible with 3.10.

### R2. Make React E2E proportional to the affected contract

[React verification](../../standards/react/verification-compatibility.md#evidence-at-the-affected-boundary)
must select browser E2E when it covers a material changed behavior/risk that cheaper
checks cannot establish, or when a mandatory project/CI gate requires it. Membership
in a critical journey alone does not require rerunning the entire journey.

Preserve actual browser/visual evidence for browser-dependent contracts, including
layout, focus, navigation, hydration and browser networking. A scoped browser check
need not become a full end-to-end suite. Preserve required gates and the shared
[verification policy](../../standards/verification.md#what-to-run-and-when).

Acceptance: a pure pricing calculation can use focused behavior checks when no
browser contract changes; a changed focus/navigation contract uses a real browser;
an explicitly required E2E gate is still completed in either case.

### R3. Resolve size limits through an explicit cohesion decision

[Core size rules](../../standards/core.md#size-and-cohesion) retain the existing
50/400/500-line review signals and the 600–700-line growth review. For a new or
substantially rewritten behavior file/class over 700 lines, require a documented
cohesion review rather than unconditional mechanical splitting.

Split independent responsibilities. Retaining an oversized cohesive component is
an exception requiring its purpose, considered extraction boundaries, why splitting
would worsen cohesion/coupling/readability, and a condition for reassessment. Record
this in the existing task or architecture decision; no separate exception ledger
or additional routine approval is required. Reassess when responsibility or growth
invalidates the rationale. An exception cannot excuse mixed independent duties,
concealed size, weaker checks or violation of an explicit project gate.

Align the decomposition paragraph and [root entry template](../../templates/AGENTS.root.md)
with this policy. Preserve the bounded scope of small legacy fixes and the naming
rules for both extracted components and the remaining owner.

Acceptance: an 800-line cohesive component needs a concrete recorded rationale;
an 800-line component mixing independent concerns is split; a small legacy fix
does not trigger an unrelated rewrite; an explicit project size gate remains binding.

### R4. Make the Unreal catalog the resource-list owner

The `unreal-engine` entry in [catalog.toml](../../standards/catalog.toml) owns the
complete resource list. Replace numeric resource-count prescriptions in active
adoption/architecture/profile/overview prose with references to that list. Preserve
all currently declared resources, including the optional skills reference.

Affected documents: `MIGRATION.md`, `ARCHITECTURE.md`, `README.md`,
`standards/unreal-engine.md`, and `standards/catalog.md`. Bundle availability still
does not imply unconditional reading, skill installation or MCP setup.

Acceptance: all declared Unreal resources exist and remain included by the catalog;
the affected active documents do not prescribe a competing count. Historical records
may retain the counts they actually checked.

## Verification and limits

Use artifact checks for links/anchors, Markdown structure, catalog syntax/resources
and whitespace, plus an inline review of the acceptance scenarios above. Preserve
pre-existing uncommitted naming changes. Static checks establish instruction and
artifact consistency, not observed adherence by an agent or a target-client pilot.
