# Codex role examples

These inactive examples cover orchestrator, implementer and reviewer. The
framework selection example uses schema_version = 2 as a documentation format;
it is separate from the native Codex files below. Add optional roles only when
the selected scheme needs them, following [orchestration](../../standards/orchestration.md).

During setup, adapt these inactive examples to the workspace's confirmed model
selection. The templates do not change this session or any existing project.
See [model configuration](../../standards/model-configuration.md) for the mapping,
conditional setup, legacy handling, reassignment, and actual-runtime checks.

| File | Target location | Purpose |
| --- | --- | --- |
| [config.toml](config.toml) | `.codex/config.toml` | Main model, worker defaults, concurrency ceiling |
| [af-implementer.toml](agents/af-implementer.toml) | `.codex/agents/af-implementer.toml` | Bounded implementation using the selected model/effort |
| [af-reviewer.toml](agents/af-reviewer.toml) | `.codex/agents/af-reviewer.toml` | Independent review when justified |

The shown Astra/Sol high values are suggestions, not fixed routing rules.
The framework example starts unconfigured, with a suggested enabled implementer,
disabled reviewer and `orchestrator->implementer` edge. It is not consent to any
assignment. The main agent plans and performs routine review. Adopt the reviewer
file only after that role and its incoming edge are explicitly selected; its
presence among these templates does not enable it. Other roles are optional.

For selected single-agent mode, install no specialist definitions and set supported
`agents.enabled = false`. Keep the framework ceiling at zero; do not assume zero
is a valid native thread limit. Existing positive defaults/limits may stay inactive.
For delegated mode, enable agent tools and use the selected positive ceiling.
Role pairs override defaults; request an enabled role or its explicit pair and
instructions. Never route a disabled reviewer through an ordinary worker default.
Allowed edges are instruction policy unless native enforcement has been verified.

An absent/unconfigured record permits ordinary inline work without setup or writes.
Explicit setup/reassignment follows the version-2 contract; reuse v1 choices and
resolve only missing material fields before authorized migration. Unknown schema
versions are not automatically rewritten. Disabling an already managed role follows
the contract's retirement procedure, preserving unrelated roles and user edits.

Before applying, verify the installed client schema and available models, then
merge only the intended settings. Preserve unrelated keys, comments, roles,
permissions, providers, plugins, and user changes. Project trust and runtime
configuration overrides affect which settings actually take effect.

Standalone custom roles require `name`, `description`, and `developer_instructions`.
Set model and effort together and update role files as well as defaults during
reassignment. The examples inherit permissions; the reviewer's no-edit instruction
is behavioral guidance, not an independently configured filesystem sandbox.

Parse TOML and compare the intended/native assignments. Then verify actual model
and effort through supported client controls; a file change or successful parser
does not prove a running thread switched. If only explicit model/effort spawn
parameters are exposed, use them with the role instructions. Do not invent tools.

The default workflow uses the current directory without commits or worktrees and
stops after a logical stage for human review. Installing role files does not grant
Git writes, automatic progression, or permission to bypass that checkpoint.

Native agent enablement, defaults, ceiling and role format rechecked in the official
documentation on 2026-09-26:
[Custom agents](https://learn.chatgpt.com/docs/agent-configuration/subagents#custom-agents)
and [Configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference).
Examples are not evidence of installation or successful target-client onboarding.
