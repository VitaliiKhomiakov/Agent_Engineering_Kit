---
name: aek-model-setup
description: Use when full Agent_Engineering_Kit integration reaches model selection, the user requests model setup, or authorized delegation requires missing workspace role choices.
---

# Set up workspace models

Establish explicit workspace choices for the client, enabled roles and delegation.
Missing configuration alone does not trigger this skill: ordinary work can continue
inline in the current session. This skill is part of the
Agent_Engineering_Kit workspace layout, not a standalone global installer.

Read the [model setup contract](../../../standards/model-configuration.md) for
first-use behavior, persistence, native target mapping, and execution limits.
That link is relative to this inactive source/bundle template. Before native
installation, rebase it to the adopted contract: at Codex
`.agents/skills/aek-model-setup/SKILL.md`, the default contained route is
`../../../.agents-framework/standards/model-configuration.md`. Use the recorded
bundle for a flat or custom layout; resolve independently of the process cwd.

- Resolve the workspace, record version and relevant native settings. For v1,
  preserve known choices; clarify unknown versions before editing or delegation.
- If a configured selection supplies the task's required choices and is consistent,
  return to the task; do not ask again. Route an explicit change to `aek-model-reassign`.
- For integration, honor the supplied preparation/application intent and source
  `MIGRATION.md` model-step outcome contract. Preparation produces an exact proposal
  without target writes, skill installation or activation. An explicit deferral
  returns to the adoption task without inventing configured state; missing choices
  without that decision remain unresolved. Preserve known choices in either case.
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
