# Cursor native agent integration evidence

Date: 2026-09-20. Cursor is the third requested client, selected independently
through the same workspace profile. This note records sources and observations;
[model configuration](../../standards/model-configuration.md) owns the retained configuration guidance
and the [former delivery plan](../plans/2026-09-20-native-client-adoption.md)
retains archived application history; its implementation backlog is closed.

## Roles and model selection

Current official documentation supports custom subagents in the editor and CLI.
Project definitions use `.cursor/agents/*.md`, with YAML metadata and a Markdown
prompt. Relevant fields are `name`, `description`, `model`, `readonly`, and
`is_background`. Model-specific parameters use a selector such as
`<native-model-id>[effort=high]`; support depends on the model. Do not invent a
standalone Claude-style `effort` field or a Codex TOML key for Cursor.

Cursor also discovers compatibility agent locations under `.claude/agents/` and
`.codex/agents/`; native `.cursor/` definitions win matching-name conflicts.
Inspect the effective role set when those directories coexist. Plan/admin
restrictions can make the client substitute a model, so saved intent is not
proof of execution. These are documented capabilities, not a local activation
test. See [Cursor subagents](https://cursor.com/docs/subagents).

## CLI, authentication, and coordinator scope

The installed `agent` command reported version `2026.01.28-fd13201`. Its help
lists `--model`, `--list-models`, `models`, `status`, and `-p` with JSON/stream-JSON
output. `agent status` reported no authenticated session. `agent models`
returned exit zero, but its output was not validated as a complete catalog for
an authenticated account. Neither result establishes model entitlement or
supported effort parameters on this installed version.

Use the normal existing Cursor browser sign-in when available; a missing sign-in
is a setup diagnostic. This inspection did not log in, install or upgrade Cursor,
copy credentials, invoke inference, or write native settings. See
[CLI authentication](https://cursor.com/docs/cli/reference/authentication) and
[CLI parameters](https://cursor.com/docs/cli/reference/parameters).

The documented global settings file is `~/.cursor/cli-config.json`. The project
file `.cursor/cli.json` supports permissions only. Therefore the framework's
project-specific coordinator choice must use a checked session launch/selection
mechanism, initially the documented `--model` control, rather than placing model
keys into project permissions or changing every project's global default.
Verify parameterized selectors for that launch path on the supported version.
Do not relocate authentication/config directories to simulate project settings.
See [CLI configuration](https://cursor.com/docs/cli/reference/configuration).

## Rules and remaining checks

Cursor supports `AGENTS.md` and `.cursor/rules/*.mdc`; rule metadata includes
`description`, `globs`, and `alwaysApply`. Select only applicable guidance and
reconcile existing instructions. Native priority still applies. Independently
opened repositories need reachable shared policy and a verified role-loading
path. See [Cursor rules](https://cursor.com/docs/rules).

P4C must establish version-specific role loading, supported effort values,
coordinator selection, catalog completeness, and controlled native writes. P6/P7
must establish per-agent model/effort observations and available session coverage.
Structured CLI output alone does not establish resolved per-subagent telemetry.
There is no verified native concurrency/depth mapping in this inspection.

The first target is local CLI operation with existing account access; editor
reuse needs its own compatibility check. Cloud Agents, hosted workers, additional
API credentials, and cross-client execution are outside this extension. Native
support on an older installed version must be checked before any activation.
