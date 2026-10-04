---
name: af-model-reassign
description: Use when the user requests changing saved Agent_Engineering_Kit model pairs, client, role enablement, delegation mode, edges or concurrency.
---

# Reassign workspace models

Change the requested role assignments without restarting project onboarding.
This skill belongs to the Agent_Engineering_Kit workspace layout.

Read the [model configuration contract](../../../standards/model-configuration.md),
especially native target mapping, active-session limits, and reassignment.
That link is relative to this inactive source/bundle template. Before native
installation, rebase it to the adopted contract: at Codex
`.agents/skills/af-model-reassign/SKILL.md`, the default contained route is
`../../../.agents-framework/standards/model-configuration.md`. Use the recorded
bundle for a flat or custom layout; resolve independently of the process cwd.

- Load the selection version and relevant native settings. For an absent or known
  unconfigured record, use `af-model-setup` with the choices already supplied. Read
  v1 without inventing enablement/edges; clarify an unknown schema before editing.
- Extract the requested changes, preserving unspecified choices. Validate enabled
  pairs, mode, graph and ceiling; reuse known v1 choices during authorized migration.
  A client switch requires explicit compatible pairs, not translated model aliases.
- If invoked during integration, retain its preparation/application intent and
  source `MIGRATION.md` model-step reporting contract. Preparation returns the exact
  proposal without target writes or activation; a rules update alone requests no
  reassignment. Reuse existing authorization without expanding native/global scope.
- Show affected before/after values and paths. The user's explicit instruction already
  authorizes that change; do not demand a second identical confirmation.
- Reconcile every affected managed native target, including role overrides and
  disabled-role retirement. Preserve unrelated settings, roles and work. Publish
  configured version 2 only after intended settings agree; report partial updates.
- Parse and compare the result. Report the changed roles, saved state, and
  actual runtime assignment or the required switch/new session. Do not claim
  that existing main or child threads changed merely because files were edited.

If files disagree or an update is blocked, expose the specific conflict and
resolve only the intended change. Do not silently substitute a model, reset
configuration, weaken permissions, or rerun application tests.
