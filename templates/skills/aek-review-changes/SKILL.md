---
name: aek-review-changes
description: Use when reviewing changed code or contracts in a project with adopted AEK rules, on request or at an applicable completion review. Excludes implementation requests without a review boundary, whole-project audits, wording-only edits and framework or model setup.
---

# Review project changes

Assess the actual change against the task and affected technical contracts. Use
the [project-skill contract](../../../standards/project-skills.md) for local
inputs, procedure composition and the review result.

1. Establish the requested review scope, acceptance criteria and actual baseline.
   Include new/uncommitted files while distinguishing prior user work. If the
   baseline is incomplete, state the attribution limit instead of inventing a
   clean Git range or initializing Git to enable a review interface.
2. Select local stack entries for the changed contracts, then their relevant
   topics. Inspect the actual diff and enough surrounding owners/callers/consumers
   to resolve a plausible regression. Apply accepted project exceptions rather
   than treating every difference from a reference example as a defect.
3. Use the existing verification/review boundary and any selected Superpowers
   procedure through local adaptations. Identify whether this is coordinator
   review or an authorized independent review; reading this skill creates neither
   independence nor permission to dispatch another agent.
4. Report consequential findings with locations, affected requirements, failure
   scenarios and evidence. Separate confirmed defects, uncertainties and incidental
   issues; state coverage and unavailable checks. Report no findings when the
   reviewed scope yields none, without claiming the project has no bugs.

A review-only request does not authorize fixes. Within an already authorized
implementation, the existing review owner governs resolution of in-scope defects;
this entry adds no extra review pass, severity quota or permission checkpoint.
