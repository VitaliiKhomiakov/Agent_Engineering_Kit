# Portable role composition — 2026-10-13

The [canonical task](../plans/2026-10-13-portable-agent-roles.md) owns progress and
the [specification](../specs/2026-10-13-portable-agent-roles.md) owns this design.
This note records source review and static evidence, not target-client activation.
Earlier [role evidence](2026-10-12-specialized-agent-instructions.md) and
[capability observations](2026-10-04-orchestration-capabilities.md) retain their dates.

## Source contracts

| Official source reviewed | Application and limit |
| --- | --- |
| [Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents) | Retain native TOML metadata, explicit model/effort examples and read-only defaults. `developer_instructions` now directs an explicit read of the matching shared body; no native include feature is asserted. |
| [Claude Code subagents](https://code.claude.com/docs/en/sub-agents) | Markdown/YAML adapters use documented model aliases and `effort`. Architect/reviewer allow only `Read, Grep, Glob`; omitting shell and MCP access avoids treating removal of Edit alone as a write boundary. Verify effective restrictions and overrides during target setup. |
| [Cursor subagents](https://cursor.com/docs/subagents) | Markdown/YAML adapters use the documented bracketed model/effort selector and `readonly`. Account/admin fallback can change the executing model; sample selector validity is not availability or execution evidence. |

Claude's current page distinguishes definition-level effort from per-invocation
effort (the latter requires v2.1.292 or later); these templates use the definition
field, not a new invocation parameter. Cursor's page describes supported options
per model, so setup must validate the selected pair rather than translate Codex
keys. No universal client version floor is inferred. No local client version or
native role was executed in this stage; the 2026-10-04 version observations are
not recast as tests of the changed contents.

The shared-file read, fail-before-dependent-work behavior and maintenance parity
are AEK policy. The common files are installed inside the project bundle, outside
native discovery. Loading relies on explicit worker instructions and available
read tools; no Markdown link or configuration string is claimed to expand itself.

## Scope inspected

Shared bodies preserve the prior Codex procedures and policy routes. Thin adapters
keep model and permissions separate. Adoption instructions address local custom
embedded bodies, shared-content changes, enabled-client selection and partial
application. No target installer, role activation, new assignment, model pilot,
benchmark or Superpowers modification is part of this change.

## Executed evidence

The initial resource-contract test failed because the shared architect file was
absent from the catalog. After extraction and catalog/adaptor additions, all six
new agent-template tests passed. Their fixtures inspect native syntax, local
body/policy route resolution, negative dependency cases, three-client selections,
explicit pair preservation, write-free preparation and repeated candidates.

The four affected existing suites passed 63 tests (portability, project-skill
adoption, profile selection, and model routing). The source artifact checker
checked 220 artifacts with no errors; explicit checking of six affected documents
also passed. Strict mypy 2.1.0 checked eight Python source files with no issues,
using the documented flags including both disallow-Any options and Python 3.11.
The analyzer and its dependencies were installed only in the isolated temporary
environment `/tmp/aek-portable-roles-mypy`, because system Python lacked pip/mypy.
No repository dependency or global Python installation was changed.

Scoped review compared all three extracted procedures with their pre-stage TOML
bodies: after normalizing the intentionally adapted policy links/reference bases
and example wording, each procedure was preserved. Reviewed the native adapter
metadata/restrictions, single-source routes and update policy. Removed duplicated
update instructions from the composition guide so MIGRATION remains their owner.
No independent subagent review or native trial was performed; the coordinator's
scoped source review is not an independent opinion.

The canonical task records the final checkpoint. Static fixtures do not prove
native configuration loading, instruction obedience, effective restrictions,
actual model/effort, or a general-purpose update engine. Native loading remains
unverified for all three clients on these changed contents.
