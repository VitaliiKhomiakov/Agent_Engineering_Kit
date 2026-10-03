# Agent_Engineering_Kit scope: rules, instructions and native templates

**Status: current stage completed and accepted by the user on 2026-09-22.**
This specification records the accepted baseline of the current part. The user
confirmed the retained rules/templates and the removal of the additional application.

Originally recorded 2026-09-20; scope corrected by explicit user instruction on
2026-09-22. Agent_Engineering_Kit is a reusable engineering and agent-orchestration
rule library. The additional Python application, adapters, CLI, monitor, tests,
schemas and packaging were removed. Their [delivery record](../plans/2026-09-20-native-client-adoption.md)
is archived history, not a pending implementation plan.

## Purpose

Help agents work consistently inside Codex, Claude Code or Cursor using selected
engineering rules and the client's existing mechanisms. Adopt the instructions
in a new project or reconcile them with an existing repository's contracts.

## Retained deliverables

- Engineering profiles selected by actual language, framework, database and
  technology, with short entries, conditional sections and separate examples.
- Orchestration rules for responsibilities, explicit model/effort choices,
  bounded handoffs, context, concurrency, checks, review and human checkpoints.
- Short AGENTS and project-architecture templates, planning conventions and
  narrow instruction-only skills for model setup/reassignment.
- Inactive native settings/role examples and instruction bridges, adapted to
  the target client's installed capabilities during authorized adoption.
- A TOML rule catalog as an index, plus research notes separate from agent-facing
  instructions. No parser, installer or runtime is required to use this library.

## Ownership and adoption

[Architecture](../../ARCHITECTURE.md) owns document boundaries and reading routes.
[Migration](../../MIGRATION.md) owns reviewed target-project adoption.
[Engineering practices](../plans/2026-09-21-engineering-practices.md) records K01–K19.
[Orchestration](../../standards/orchestration.md) owns roles and handoffs;
[model configuration](../../standards/model-configuration.md) owns native mapping
and saved-choice reuse. These are instructions, not a mechanically enforced pipeline.

## Acceptance

Keep entry documents short and select details by task. Preserve one owner per
shared rule and retain project-specific contracts and accepted exceptions.
Validate affected links, template syntax and consistency. Do not add application
tests, launch models or require a live pilot simply to maintain documentation.

Native templates remain inactive until deliberately adopted. Their installation
must preserve unrelated settings and use explicit model choices. Saved settings
and actual execution are different evidence; unsupported capabilities remain
visible. Target-project installation, external calls and changes to global
configuration require authorization for those actions.

Work in the current directory by default, with proportionate verification and
stage checkpoints. A request for rules does not authorize building a separate
configuration product or returning to the retired application's backlog.

## Completion and future versions

The agreed current scope is complete and accepted: K01–K19 engineering practices,
orchestration rules, instructions, examples and native templates, with the
additional application removed. No implementation or pilot from the retired
application remains required to close this stage. This acceptance does not claim
installation or runtime verification in a target project.

Further improvements belong to a separate part or new version with its own scope,
specification/plan, authorization and acceptance criteria. Reference this accepted
baseline without silently reopening its completed work or the archived application
backlog. The next part/version identifier will be chosen when that work is defined;
this closure does not create a release, Git tag or new execution authorization.
