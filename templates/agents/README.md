# Shared role instructions and native adapters

The [architect](architect.md), [implementer](implementer.md), and
[reviewer](reviewer.md) bodies each own that role's procedure and result contract.
Existing standards own shared policy. Change a role body once for all clients;
do not copy its procedure into each adapter or add a second cross-role policy.

| Client | Inactive adapters | Active destination relative to instruction root |
| --- | --- | --- |
| Codex | [Architect](../codex/agents/af-architect.toml), [implementer](../codex/agents/af-implementer.toml), [reviewer](../codex/agents/af-reviewer.toml) | `.codex/agents/af-<role>.toml` |
| Claude Code | [Architect](../claude/agents/af-architect.md), [implementer](../claude/agents/af-implementer.md), [reviewer](../claude/agents/af-reviewer.md) | `.claude/agents/af-<role>.md` |
| Cursor | [Architect](../cursor/agents/af-architect.md), [implementer](../cursor/agents/af-implementer.md), [reviewer](../cursor/agents/af-reviewer.md) | `.cursor/agents/af-<role>.md` |

Adapters contain native identity, selection descriptions, model/effort examples,
restrictions and a minimal bootstrap instruction. Shared bodies stay outside native
agent-discovery directories. Bundle availability neither enables a role nor installs
its native adapter. Only the selected client's enabled roles are adopted under
[model configuration](../../standards/model-configuration.md).

## Explicit loading and reference bases

The coordinator supplies the exact instruction root, adapted body path, canonical
task, checkout, saved selection and applicable project/Superpowers policy under the
[handoff contract](../../standards/orchestration.md#delegation-contract).
The adapter instructs the agent to read the matching body before role work, or
reuse its complete current contents when already supplied. A bare filename or the
coordinator having read it does not provide the worker's context. This is an
instruction-guided file read, not native Markdown/YAML/TOML inclusion.

Adapter body paths resolve from the supplied instruction root, not the native
file's directory or cwd. The default is
`.agents-framework/templates/agents/<role>.md`; adapt it to
`templates/agents/<role>.md` for a flat bundle or the actual custom bundle prefix.
Policy links inside the body resolve relative to that body; the retained bundle
layout preserves `../../standards/...`. Read only the assigned role and needed
policies. Root entries do not preload every body.

A missing, unreadable, wrong-role or uncertain body/root blocks dependent role
work. Report the specific input to the coordinator; do not search unrelated roots,
fetch a remote replacement or silently embed a divergent copy. Independently
opened child projects need reachable local instructions. Neither source checkout
access nor an author's absolute path is a runtime dependency.

## Native differences

Keep models and tools out of shared bodies. The adapter values are illustrative,
not assignments or availability evidence. Setup must resolve each explicit saved
model/effort pair against the chosen native client/version before activation.
Never transfer a client's model alias or effort encoding to another client.

Codex architect/reviewer examples retain `sandbox_mode = "read-only"`. Claude Code
examples allow only `Read, Grep, Glob`, so they can load local instructions without
shell, edits, MCP tools or spawning. Such reviews consume the coordinator's diff
and check evidence; write-producing checks belong to an authorized executor.
Cursor examples set `readonly: true` and encode effort in the model selector.
The implementer inherits task/session permissions; its common body still controls
scope and any further delegation. Inspect effective restrictions and model settings:
parent, environment or account constraints can affect native behavior. Template
syntax and no-edit text do not prove runtime containment or model execution.

## Adoption and updates

Source MIGRATION, "Model-selection step", owns preparation, native installation
and updates; resolve it through the identified source/adoption provenance. Its
procedure covers managed shared bodies, customized embedded Codex instructions,
body/adapter application order, changed shared content, collisions and recovery.
This guide defines composition, not another installation or update lifecycle.

Tests inspect syntax, routes and fixed preparation scenarios; they do not launch
clients or prove instruction loading. Source `docs/maintenance/verification.md`
owns reproduction commands; see also the optional [dated evidence](../../docs/research/2026-10-13-portable-agent-roles.md).
When source-only evidence is omitted during adoption, adapt its links under the
[catalog contract](../../standards/catalog.md#assemble-a-portable-bundle).
