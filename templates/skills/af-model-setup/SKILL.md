---
name: af-model-setup
description: Use when the user requests AgentsFramework model setup or an authorized delegation requires missing workspace role choices.
---

# Set up workspace models

Establish explicit workspace choices for the client, enabled roles and delegation.
Missing configuration alone does not trigger this skill: ordinary work can continue
inline in the current session. This skill is part of the
AgentsFramework workspace layout, not a standalone global installer.

Read the [model setup contract](../../../standards/model-configuration.md) for
first-use behavior, persistence, native target mapping, and execution limits.

- Resolve the workspace, record version and relevant native settings. For v1,
  preserve known choices; clarify unknown versions before editing or delegation.
- If a configured selection supplies the task's required choices and is consistent,
  return to the task; do not ask again. Route an explicit change to `af-model-reassign`.
- Reuse supplied choices. Ask one bundled question for material missing client,
  mode, enabled role pairs, edges and ceiling. Single-agent setup needs only the
  coordinator's pair. Continue independent work while necessary answers are pending.
- Prepare and apply the authorized settings change within actual permissions.
  Preserve unrelated fields and work. Validate version-2 choices and graph, reconcile
  enabled/disabled managed native roles and compare intended settings before marking
  `.agents-framework/model-routing.toml` configured. Migrate v1 only within this
  authorized setup; report partial writes under the contract's recovery procedure.
- Report the saved mapping, its scope, and whether the running session has
  actually adopted it or needs a supported switch/new session.

Do not treat a copied example as consent, invent unavailable models, change
global defaults, or run product tests for this configuration task. A partial
write or unverified runtime must not be reported as a completed model switch.
