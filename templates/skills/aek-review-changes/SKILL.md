---
name: aek-review-changes
description: Use when the user requests AEK review of supplied code snippets or project changes, or at an applicable completion review in a project with adopted AEK rules. Excludes implementation requests without a review boundary, whole-project audits, wording-only edits and framework or model setup.
---

# Review supplied code or project changes

Assess the supplied code or actual change against the task and available technical
contracts. Use the [project-skill contract](../../../standards/project-skills.md)
for inputs, procedure composition and the review result.

1. Establish the supplied scope, known requirements and permitted actions. For
   snippets or restricted tool access, follow
   [supplied-code review](../../../standards/verification.md#supplied-code-and-restricted-tools).
   For project changes, use the actual baseline and include new/uncommitted files
   within the permitted scope, distinguishing prior user work and attribution gaps.
2. Select available stack entries for the affected contracts through the
   project-skill contract's input routes. Inspect the supplied code or permitted
   diff and enough available surrounding context to assess a concrete failure.
   Apply accepted project exceptions rather than treating every difference from
   a reference example as a defect.
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
