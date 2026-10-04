# Workspace model setup and reassignment

Use this procedure for the model-selection step during full integration, authorized
model setup, explicit reassignment, or a relevant configuration conflict. Source
`MIGRATION.md`, "Model-selection step", owns the integration trigger/outcomes;
resolve it through the identified source or adoption provenance. Ordinary tasks reuse a valid saved selection or work inline
in the current session when no selection exists. The current agent edits reviewed
native settings; these instructions require no separate
Agent_Engineering_Kit application, launcher, account or model service.

## Scope and source of truth

Choose one installed Codex, Claude Code or Cursor client for the workspace.
Use its existing account access and supported native controls. Do not copy
credentials, introduce an API key or upgrade the client as part of routine setup.

Record the selected client, enabled roles, model/effort pairs, delegation edges
and concurrency ceiling in `.agents-framework/model-routing.toml`. This is an
instruction-level record;
native clients do not interpret it. The inactive [example](../templates/framework/model-routing.toml)
uses `schema_version = 2` to label its documented layout. It starts unconfigured;
its sample model IDs are suggestions, not assignments or evidence of availability.

The routing record and native destinations below resolve from the target
instruction root regardless of the bundle location. Relative links to inactive
templates resolve from this document. Before installing skills or native role
instructions, adapt their routes to the actual bundle and destination; source
`MIGRATION.md`, "Adapting installation routes", owns that path contract. Moving
inactive resources neither moves native configuration nor changes assignments.

[Orchestration](orchestration.md) owns responsibilities, delegation relationships,
task order and checkpoints. Record additional chosen roles and scheme decisions
without turning optional agents into mandatory steps. Model selection and work
mode are independent. Different workspaces may select different pairs.

An independently opened nested repository needs its own reachable instructions
and, when configured, selection/native settings. Do not assume configuration
outside the client's discovery boundary loads, or silently introduce per-project overrides.

## Routing format version 2

| Field | Contract |
| --- | --- |
| `schema_version` | Integer `2`; read legacy version 1 as described below |
| `status` | `unconfigured` or `configured`; saved agreement, not runtime activation |
| `scope` | `workspace` |
| `client` | `codex`, `claude-code`, or `cursor`; required when configured |
| `max_subagents` | Nonnegative integer excluding the coordinator; zero for single-agent mode |
| `orchestration.mode` | `single-agent` or `delegated` |
| `orchestration.allowed_edges` | List of `parent->child` role IDs, without spaces; these are spawn permissions, not task dependencies or reporting paths |
| `roles.<id>.enabled` | Explicit Boolean for each recorded role; orchestrator is enabled |
| `roles.<id>.model`, `reasoning_effort` | Nonempty explicit pair for every enabled role when configured; client capability validation is separate |

A configured record contains all these fields for its enabled selection. Disabled
roles may retain a prior pair but cannot be invoked; an omitted specialist is not
enabled. Role IDs correspond to the named responsibilities in the saved record;
native specialists use `af-<id>`. There is no framework-wide model whitelist.
The target `.agents-framework/adoption.md` owns adopted source/content identity
and accepted exception decisions. Entries/passports point there for provenance
and retain applicable operational constraints. This model-selection record owns
neither import history nor task progress; ordinary work need not read adoption history.

Single-agent mode has no enabled specialists, no edges and `max_subagents = 0`.
Delegated mode has a positive ceiling. Every edge references enabled roles; the
parent is reachable from orchestrator, and self-edges, duplicates and cycles are
invalid. An enabled role without an allowed incoming edge cannot be spawned.
Nested edges require an explicit user choice and verified client support. A valid
edge permits a justified task handoff; it does not require spawning that role or
authorize work beyond the task. Task order, corrections and checkpoints stay in
the task plan.

The linked template illustrates delegated mode with an optional disabled reviewer.
This alternative illustrates single-agent mode; its pair is also a suggestion,
not evidence of selection or availability:

```toml
schema_version = 2
status = "unconfigured"
scope = "workspace"
client = "codex"
max_subagents = 0

[orchestration]
mode = "single-agent"
allowed_edges = []

[roles.orchestrator]
enabled = true
model = "gpt-6-astra"
reasoning_effort = "high"
```

An unconfigured record may omit undecided fields. Do not complete them from an
example or mark the record configured until choices are explicit, the graph is
valid and intended native settings agree. Syntax alone establishes none of these.

## Legacy records and unknown versions

Version 1 remains readable: retain its recorded pairs and concurrency limit.
Missing client, role enablement and delegation edges are unknown, not defaults.
Respect known choices for work using that assignment; ordinary compatible inline
work needs no migration or repeated onboarding. Resolve missing delegation choices
before spawning; the presence of a legacy role pair does not enable that role.

During authorized setup/reassignment, reuse known choices, ask only for material
missing ones, and prepare version 2 with the necessary native changes. Publish
configured version 2 after agreement checks; preserve unrelated data and retain
the original record for scoped recovery. Do not migrate on ordinary session entry.
For an unknown schema version, report the limitation and obtain clarification
before editing or using it for delegation. Do not reinterpret it as unconfigured,
guess its semantics or rewrite it to a known version.

## Catalog and capability validation

Inspect the installed client's version, available models and supported efforts
through its native interfaces. Validate model and effort together; do not
translate effort levels between clients or guess model aliases. Public examples
and an agent's suggestion do not establish account availability.

If discovery is unavailable, retain the explicit choice as unverified and report
that limitation. Unsupported pairs require an alternative from the user; never
silently substitute. Refreshing availability does not change saved assignments.

## First-use behavior

At workspace entry, check the small selection record once if present. Its absence
does not trigger a setup workflow. Reuse this state within the session; inspect
native configuration only for a relevant assignment or observed conflict.

| Situation | Action |
| --- | --- |
| Missing/unconfigured record; task can run inline | Use the current session and relevant engineering rules. No mandatory questionnaire, profile write or delegation; this is not a saved model assignment |
| User requests model setup | Use `af-model-setup` or this procedure if the skill is unavailable |
| Full integration reaches its model-selection step | Use `af-model-setup` to check/reuse or prepare authorized setup; apply only within the selected adoption intent. Source `MIGRATION.md` owns preparation, explicit deferral and unresolved outcomes |
| User requests a change to saved choices | Use `af-model-reassign`; preserve other choices |
| A required delegated role has missing choices | Resolve only necessary choices before spawning; continue independent inline work |
| Configured selection is consistent | Reuse it; no repeated onboarding after a task, conversation or compaction |
| Pair is unsupported or active settings conflict | Report it and resolve the assignment before dependent work; no silent substitution or claim of conformity |

Using the current session without a configured selection does not authorize a
native configuration write. Existing explicit choices take precedence over examples.
An unconfigured status after a partial update does not revoke known choices or
excuse a reported assignment conflict; resolve it before dependent work.
For preparation, perform the inspection and exact proposal below without target
writes or activation. An explicit integration deferral stays in the canonical
adoption task/outcome; it does not introduce another routing status. If required
choices, capabilities or permissions are missing, report unresolved rather than
silently treating absence as deferral. For authorized setup or repair:

1. Inspect relevant existing role/default settings and instruction discovery.
2. Reuse explicit choices already supplied. Ask one bundled question for missing
   client, mode, enabled roles, pairs, edges and concurrency; wait only for necessary
   answers. Single-agent setup needs only the coordinator's pair, not worker choices.
3. Prepare the exact changes to the selection record and supported native files.
   Preserve unrelated fields, permissions, comments, custom roles and local work.
4. Apply within the task's authorization. Parse the formats, validate enabled
   pairs/edges/ceiling and compare intended native settings. Retain original
   contents/absence for recovery, including managed roles being disabled.
5. Mark the selection configured only after the intended files agree. Explain
   whether the current session adopted it or requires a supported reload/new session.

A new task, conversation or compaction does not reset valid setup. Do not repeat
questions already answered or require a second identical confirmation for an
explicitly authorized change. A copied template, silence or timeout is not consent.

## Role enablement and native agreement

Adopt only enabled specialist definitions. To disable a previously managed role,
use a verified native disable mechanism or move its owned definition outside all
discovered agent directories, preserving a recoverable copy. Inspect alternate
definitions and registrations so an old override cannot remain active. Never
remove an unrelated role or infer ownership solely from an `af-` name; reconcile
a name collision before writing. A disabled reviewer is not replaced by an
anonymous spawn using worker defaults. The coordinator retains routine review;
a required independent review needs an authorized enabled role or a clarified choice.
Disabling a role does not cancel an already running task; report that state and
resolve any required cancellation separately.

Map supported controls for the selected client and report unsupported enforcement.
Allowed edges and unsupported nesting/concurrency controls remain instruction
policy; do not invent keys or claim native enforcement. Single-agent mode prohibits
delegation even if no native switch is available. Describe this limit explicitly.
Saved agreement compares enabled role overrides and relevant defaults/controls;
disabled retained pairs do not need to match worker defaults.

## Role scope and native restrictions

A reviewer or explorer's no-edit instructions define behavioral scope; they do
not establish a filesystem/tool boundary. During authorized native setup, use
supported restrictions for the selected role and verify the effective controls,
including parent/session overrides. Preserve necessary read access to the task,
baseline and evidence. If enforcement is unavailable or cannot be verified, report
the limitation; do not describe the role as sandboxed or silently broaden its task.

Prefer read-only tools for review/exploration where supported. Merely removing an
Edit tool is insufficient when shell, MCP or other tools can still write. A check
that writes caches, artifacts or fixtures goes to an authorized executor, which
returns its evidence; do not loosen reviewer permissions to run it. Read-only
access also does not isolate a reviewer from concurrent changes: review a stable
scope under the [worker lifecycle](orchestration.md#worker-lifecycle-and-continuations).

A planner assigned a draft may write only that authorized artifact; it is not a
read-only explorer and does not gain implementation rights. Follow the adopted
`PLANS.md` ownership rules ([inactive source template](../templates/PLANS.md#progress-and-stopping)) for handback.
Role enablement, write scope and native enforcement are separate decisions.

Codex documents per-agent `sandbox_mode`; Claude Code provides `tools`,
`disallowedTools` and `permissionMode`; Cursor documents `readonly`. These are
client-specific controls, not interchangeable guarantees. Check the installed
schema and effective permissions before using them. For a capability question,
consult the dated [client comparison](../docs/research/2026-10-04-orchestration-capabilities.md);
it is optional source evidence, not a required imported resource or runtime proof.

## Mapping to native Codex files

Use [the inactive native templates](../templates/codex/README.md), checking their
keys against the installed client's schema before adoption:

- Main model/effort: `.codex/config.toml`, `model` and `model_reasoning_effort`.
- Worker defaults and concurrency: supported `[agents]` fields, including
  `max_concurrent_threads_per_session` where available, excluding the main agent.
- Enabled specialists: `.codex/agents/af-<role>.toml`, their explicit pair and
  role instructions. The retained examples cover implementer and reviewer.

For selected single-agent mode, use supported `agents.enabled = false`; do not
translate the framework's zero ceiling into an assumed-valid native thread limit.
Existing positive limits/defaults can remain inactive. Delegated mode uses
`agents.enabled = true` and the selected positive ceiling where supported.
Explicit role pairs remain authoritative for routing; a worker default cannot
authorize another role or replace a missing pair.

Change relevant role files as well as defaults: a role override can defeat a
changed default. Do not map the custom reviewer onto native review-command settings
without checking that distinct path. Preserve unrelated settings and inspect name
collisions instead of overwriting. Native trust and configuration precedence apply.

If the exposed interface supports explicit model/effort spawn parameters rather
than named roles, supply the saved pair and relevant role instructions. Do not
invent parameters or claim a file changed an already running thread.

## Mapping to native Claude Code files

Use `.claude/agents/af-<role>.md` for enabled specialists, with supported `model`
and `effort` YAML fields and Markdown instructions. Select the main-session pair
through the installed version's supported settings or native controls. Codex keys
and effort levels are not interchangeable with Claude's.

Check invocation, environment and managed overrides. Use a verified `CLAUDE.md`
bridge when native AGENTS discovery is unavailable; an inactive [bridge template](../templates/claude/policy-bridge.md)
is retained. Supply relevant policy explicitly to roles that skip normal entry
files. Preserve custom metadata, instructions and unrelated settings. The
[research note](../docs/research/2026-09-20-native-agent-orchestration.md) records
version-specific observations, not universal installation or runtime support.

## Mapping to native Cursor files

Use the installed client's supported `.cursor/agents/af-<role>.md` format for
selected specialists. Check how its selector represents the chosen model/effort
pair, preserving unrelated parameters and rejecting contradictory representations.
Inspect native and compatibility role directories for collisions. Verify main
session model selection separately; project `.cursor/cli.json` permissions do
not represent the coordinator's model choice.

The retained [rule route](../templates/cursor/rule-route.mdc) is an inactive template.
[Cursor research](../docs/research/2026-09-20-cursor-agent-orchestration.md) records
capability limits. CLI and editor behavior require separate checks; do not infer
support or activation from a saved role filename or selector.

## Preview, apply, and repair

Review the before/after values and affected paths before editing. If a manual
change occurs after review, reconcile it rather than overwrite it. Parse only the
affected formats using existing tools. A partial write remains partial: identify
affected paths and restore only this task's changes while preserving newer edits.
Publish a configured record only after all intended writes and agreement checks.
After an interruption, an old `configured` label is not evidence that partially
written native settings agree. Restore this task's changes where possible; if
recovery is incomplete, mark a known-format owned record `unconfigured`, preserve
its choices and report remaining mismatches. Never rewrite an unknown schema for
recovery or claim a partial update succeeded.
An unchanged valid selection needs no rewrite. No application test suite or paid
model pilot is required merely to edit these instructions or model settings.

## Saved selection versus active execution

Configured means saved choices and native files agree. It does not prove a
running main/child thread uses them. Inspect supported native controls, distinguish
saved intent, active settings and runtime-reported model, and keep unavailable
evidence unknown. A worker's self-description is not execution proof.

The first setup conversation uses the model that launched it. Later delegation
uses the chosen native role/pair. Report current-session differences and reload
or start a new session only when supported and needed. Do not automatically
restart tasks, change models or infer missing effort telemetry.

## Reassignment

`af-model-reassign` applies requested pairs, role enablement, mode, edges or ceiling
changes to existing choices. A client switch requires reconciling that client's
native targets within the granted scope; it never translates model IDs or efforts.
Preserve other pairs, scheme, checkpoints, required checks and permissions.
Update affected native overrides too, then report saved agreement and activation
limits. Reassignment does not authorize architecture changes, dependency upgrades,
global-default changes or repeated onboarding.

## Validation and sources

Check syntax, enabled pairs, graph invariants, intended/native agreement and
reachable instruction paths. Check disabled-role retirement separately. Native
loading can be verified during explicitly authorized target-project adoption;
external calls and installation are separate from maintaining this rule library.
No hook or background monitor is installed by these instructions.

- [Codex custom agents](https://learn.chatgpt.com/docs/agent-configuration/subagents#custom-agents)
  and [configuration](https://learn.chatgpt.com/docs/config-file/config-reference).
- [Claude Code subagents](https://code.claude.com/docs/en/sub-agents)
  and [model configuration](https://code.claude.com/docs/en/model-config).
- [Cursor capability evidence](../docs/research/2026-09-20-cursor-agent-orchestration.md).
