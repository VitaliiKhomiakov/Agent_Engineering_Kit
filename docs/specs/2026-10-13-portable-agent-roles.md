# Portable agent roles for Codex, Claude Code, and Cursor

Date: 2026-10-13. Status: design accepted for implementation by the user on 2026-10-13.
The [implementation plan](../plans/2026-10-13-portable-agent-roles.md) owns progress
and authorization; this document owns the proposed design and acceptance criteria.

## Outcome and scope

Provide architect, implementer, and reviewer definitions for all three clients,
with one authoritative instruction body per role. A maintenance change to a role
must not require editing three independent copies of its behavioral rules.
An adopted project must have all required role instructions locally available;
the source AEK checkout is not a runtime dependency.

The user requested both a specification and a plan. Preparing these documents is
completed in stage D. The user subsequently authorized source implementation;
installing agents in other projects remains outside this task. Documents use English; reports use Russian.

Scope includes extracting existing Codex role instructions, adding Claude Code and
Cursor adapters, updating bundle/adoption routes, and testing instruction portability.
Preserve the existing role responsibilities and Superpowers adaptations. Identical
responsibilities do not imply identical model output or client capabilities.

Exclude new specialist roles, an orchestrator agent definition, automatic model
selection, a general installer/generator, native client upgrades, a new plugin,
modifications to the Superpowers cache, and target-project installation. Planner,
explorer, and test-runner remain optional responsibilities without new templates.

## Current state

- [Codex templates](../../templates/codex/README.md) contain three substantial
  role bodies inside `developer_instructions` in TOML files.
- [Model configuration](../../standards/model-configuration.md) already describes
  native mappings for Codex, Claude Code, and Cursor. It separates role enablement,
  saved model/effort pairs, native settings, and runtime evidence.
- Claude currently has a policy bridge template; Cursor has a rule-route template.
  Neither directory has the equivalent three specialist definitions.
- The [catalog](../../standards/catalog.toml) supplies Codex role files through
  the required `model-configuration` profile. Availability is not activation.
- [Portability tests](../../tests/test_project_skill_portability.py) inspect Codex
  role literals, three bundle layouts, and independent child instruction roots.
  [The routing checker](../../tools/check_model_routing.py) compares project-local
  Codex files only; it is not a cross-client activation validator.
- The [previous role extension](../plans/2026-10-12-specialized-agent-adoption.md)
  explicitly limited new native templates to Codex. Retain its historical evidence.

## Selected architecture

Use shared Markdown role bodies and thin native adapters. The adapter explicitly
instructs its agent to read the installed shared body before performing role work.
This is an instruction-guided read through available tools, not a claim that a
Markdown link, TOML string, or YAML field implements native file inclusion.

| Layer | Proposed source paths | Responsibility |
| --- | --- | --- |
| Existing policy owners | `standards/orchestration.md`, `standards/verification.md`, `standards/model-configuration.md`, `standards/superpowers.md` | Shared lifecycle, evidence, routing and workflow rules |
| Role bodies | `templates/agents/architect.md`, `templates/agents/implementer.md`, `templates/agents/reviewer.md` | Role-specific procedure and output contract, with routes to existing policy owners |
| Composition guide | `templates/agents/README.md` | Body/adapter boundary, loading and path contract, adaptation and evidence limits |
| Codex adapters | Existing `templates/codex/agents/af-<role>.toml` | Native metadata/settings and explicit role-body read instruction |
| Claude Code adapters | New `templates/claude/agents/af-<role>.md` | Native frontmatter, restrictions and explicit role-body read instruction |
| Cursor adapters | New `templates/cursor/agents/af-<role>.md` | Native frontmatter, restrictions and explicit role-body read instruction |

Here `<role>` means exactly `architect`, `implementer`, or `reviewer`.
The common bodies remain outside every native agent-discovery directory. Although
stored under `templates/`, an installed body is deliberately read by its selected
adapter; its presence alone does not activate an agent.

Do not introduce another shared policy file merely to deduplicate phrases across
roles. Existing standards retain ownership of cross-role rules. Extract substantive
role-specific instructions from the current Codex bodies and replace duplicated
policy with focused routes where doing so preserves the worker's required context.

Alternatives considered:

- Three complete copies are easy to install but permit behavioral drift and do
  not satisfy the requested single-source maintenance.
- Expanding common bodies into generated native files avoids a runtime read but
  introduces generation, freshness, and local-edit reconciliation obligations.
  No current requirement justifies adding that machinery.
- Shared bodies plus explicit reads reuse the existing local bundle and adoption
  procedure. The additional read and its failure handling are the proposed tradeoff.

If a selected client cannot read the body under its effective restrictions, that
role is unavailable in that configuration. Do not silently create divergent
embedded copies or claim successful loading. Reconsider composition only with
specific compatibility evidence and a reviewed design change.

## Role and adapter contracts

The architect inspects affected owners/contracts and returns justified decisions,
acceptance cases and implementation steps to the coordinator; it does not edit
the plan or implementation. The implementer completes only its accepted scope,
preserves the baseline and returns changes and necessary evidence. The reviewer
assesses a stable scope and returns located consequential findings or a bounded
no-findings result; it does not fix code. Existing no-spawn restrictions and
conditional delegation rules remain unchanged.

Adapters contain only:

- Native identity and concise selection description for the matching role.
- Client-specific model/effort and permission fields supported by the target version.
- The minimal bootstrap instruction: establish the supplied instruction root,
  read the matching installed body, and report an unavailable essential input
  before dependent work. Architect/reviewer retain an immediate no-edit boundary.
- Client-specific limitations that cannot be represented in the common body.

Short bootstrap safeguards may repeat across adapters; full procedures, review
rubrics and output contracts must not. Keep shared bodies free of client-specific
tool names, model IDs, YAML/TOML keys, and assumed native import syntax.

Do not hardcode new model assignments in the common bodies. Preserve existing
Codex example values as suggestions. New adapter examples must be clearly inactive,
use documented native syntax, and distinguish illustrative values from selected
pairs. Adoption resolves every enabled pair from the existing routing contract;
an inherited/default pair is not proof of agreement with a saved explicit choice.

## Loading and portable paths

For the default layout, the installed role body is
`.agents-framework/templates/agents/<role>.md`, relative to the target instruction
root. The active native adapter is outside the bundle at the selected client's
`.codex/agents/`, `.claude/agents/`, or `.cursor/agents/` location.

Adapt the adapter's body route for the recorded bundle: `templates/agents/<role>.md`
for a flat bundle, or `rules/aek/templates/agents/<role>.md` for the custom fixture.
Resolve it from the supplied instruction root, never from the adapter's directory
or a coincidental shell cwd. Inside a common body, Markdown policy references are
relative to that body; `../../standards/...` works in the source and retained
bundle layout. Instructions must state these distinct reference bases explicitly.

The coordinator supplies the exact instruction root, installed body location,
task, checkout, saved selection, and applicable adaptations using the existing
[handoff contract](../../standards/orchestration.md#delegation-contract). If current
body contents have already been supplied in full, reuse them under the existing
context-reuse rules. A filename or a parent having read the file is insufficient.
No root instruction file preloads all roles.

A missing, unreadable, mismatched or unresolvable role body prevents dependent
role work; report the precise missing input to the coordinator. An independently
opened child project must have its own reachable adopted routes. No author-machine
absolute path, remote fetch or discovery outside the known instruction root is
an implicit fallback.

## Client-specific mapping and evidence

| Client | Adapter boundary | Verification boundary |
| --- | --- | --- |
| Codex | TOML `developer_instructions`; existing per-role model/effort and read-only defaults | Parse TOML, preserve selection, inspect effective parent/session restrictions |
| Claude Code | Markdown body after YAML frontmatter; documented model/effort and tool/permission controls | Validate the chosen native fields and necessary read access; a permission mode alone does not establish a read-only boundary |
| Cursor | Markdown body after YAML frontmatter; documented model selector and `readonly` where appropriate | Validate selector options for the chosen model/version and inspect actual restrictions; distinguish editor and CLI evidence |

Retain native restrictions for architect/reviewer where supported. Checks producing
files go to an authorized executor. Never enable a write-capable tool merely to
make a reviewer load its body. Implementer permissions remain those of the authorized
task/session. Different client controls are not equivalent enforcement guarantees.

Source review on 2026-10-13 used the official pages below. They establish documented
native formats, not tested target activation or execution in this repository:

- [Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents):
  custom TOML agents with developer instructions and role settings.
- [Claude Code subagents](https://code.claude.com/docs/en/sub-agents): Markdown/YAML
  definitions, project agent locations, and native tool/permission controls.
- [Cursor subagents](https://cursor.com/docs/subagents): Markdown/YAML definitions,
  model selector options and read-only configuration. Documented account/admin
  fallbacks mean a configured selector alone does not prove the executing model.

Implementation must record the reviewed native contract and applicable version
limits in new dated evidence. Reuse the prior [capability note](../research/2026-10-04-orchestration-capabilities.md)
only within its original scope; do not relabel earlier observations as new runs.
Do not invent a universal minimum client version or upgrade clients to make a
template pass. Source-template readiness and observed native loading are separate
results. Native smoke trials require their own authorized target and supported
tools; their absence must remain explicit and does not justify a paid pilot.

## Adoption and compatibility

Keep catalog schema 1, routing schema 2, role IDs, and existing Codex adapter paths.
Add the shared bodies, composition guide, and six new native templates to the
`model-configuration` resources. Catalog dependencies provide availability only.

Update [MIGRATION](../../MIGRATION.md) and the existing setup/reassignment routes to
prepare only the selected client's enabled adapters, with their common bodies.
Other client templates may remain inactive in the bundle. Single-agent mode and
disabled specialists must not acquire active native definitions.

Preserve model/effort selections, allowed edges, concurrency, effective permissions,
local customizations, and unrelated roles/settings. Updating an existing Codex
installation must preserve accepted differences in its former embedded role body:
compare recorded accepted contents, local content and the proposed adapter/body;
resolve a conflict before replacement. Do not guess ownership from an `af-` name.

Preparation writes only its reviewable candidate outside the target. Application
uses the existing original-state/reconciliation procedure, includes adapter and
body as one dependent change, and does not leave a switched adapter pointing to
a missing body. Record shared bodies as managed content in the adoption record.
A shared-body update is a behavioral update for every adapter that uses it;
preview its impact even when native adapter bytes remain unchanged. Repeated
unchanged adoption must not duplicate role definitions or rewrite local choices.
An interrupted application remains partial until repaired; no automatic activation
or session reload follows from a source-library change.

Keep `check_model_routing.py` explicitly Codex-only in this scope. Do not report
its result as Claude/Cursor agreement. Adding a general YAML parser, universal
native configuration validator or installer is outside this change.

## Acceptance criteria

| ID | Required result and evidence |
| --- | --- |
| A1 | All three roles have one common body and three thin client adapters. Inspection shows the original role responsibilities and safeguards remain covered. |
| A2 | Every adapter selects the matching body; common bodies and required policies are present in the selected catalog closure. A wrong-role or missing-body fixture is rejected. |
| A3 | Prepared routes resolve for contained, flat and custom bundles, including an independently opened child root and execution from a different cwd. Installed instructions do not require the source checkout. |
| A4 | Codex TOML parses; Claude/Cursor frontmatter fits the reviewed supported template subset. Client-specific controls remain in adapters, with no invented shared native include mechanism. |
| A5 | Fixed preparation scenarios preserve explicit pairs, disabled-role/single-agent choices and unrelated local sentinels; prepare-only leaves targets untouched. Repeated preparation is stable. Static fixtures are not an installer proof. |
| A6 | Documented adoption/update review covers customized embedded Codex instructions, duplicate/native compatibility-directory definitions, partial application and shared-body changes. Unresolved conflicts cannot be called successful setup. |
| A7 | Regression checks cover missing/wrong routes and stale bundle prefixes, and scoped review checks semantic role parity. Artifact success is not presented as proof of instruction loading, permissions or model execution. |
| A8 | Necessary artifact, focused regression and strict Python checks pass for the changed scope. New dated evidence records source/static results and clearly identifies unexecuted native trials. |

## Review focus

Inspect whether extracting the Codex body accidentally drops a role safeguard;
whether a wrapper points to the wrong role or assumes native auto-inclusion;
whether a custom/flat bundle leaves a stale prefix; and whether updating shared
content could overwrite an accepted project exception or affect disabled roles.
Check that read-only controls still permit reading the body and that an unavailable
client capability is reported rather than silently widened. These are specific
failure questions, not an additional general audit or fixed review quota.
