# Adoption resource lifecycle

Date: 2026-10-24. Status: accepted for source implementation by the user.
The user explicitly requires architect, implementer, and reviewer agents to
remain available for development after adoption. Consumer-project changes remain
outside this source-maintenance task.
The [implementation plan](../plans/2026-10-24-adoption-resource-lifecycle.md) owns
progress, execution authorization, and verification evidence.

## Outcome and current evidence

An adopted project contains the rules and selected native agents/skills needed
for ongoing work. Installation reads source templates without copying a second,
inactive installation kit into the project. Persistent development agents must
not be removed when integration finishes or when a delegated instance completes.

Inspection at commit `66f139f2ddeecfdc684097a7bf59a3f7b73fc300` established:

- The required `model-configuration` profile in the
  [catalog](../../standards/catalog.toml) includes all nine native role templates,
  setup/reassignment skill templates, and configuration examples as ordinary
  resources, regardless of the selected client.
- The [shared roles](../../templates/agents/README.md) already have one procedure
  per role. The nine adapters contain native metadata and short loading
  instructions, rather than nine independent implementations of the procedures.
- The [integration entry](../../templates/skills/aek-integrate-project/SKILL.md)
  already reads setup procedures from source by default. The unwanted inactive
  copies follow catalog availability, not a requirement to install setup skills.
- An in-memory Codex fixture retained all three native agents and their local
  body references after all nine inactive adapter copies were omitted. An earlier
  catalog-only check reported three missing resources when the three inactive
  Claude adapters were omitted. These are structural observations, not native
  client execution evidence.

The [existing portable-role design](2026-10-13-portable-agent-roles.md) remains
the composition contract. This change replaces its requirement to bundle unused
native templates; it does not replace shared-body loading or role responsibilities.

## Global constraints

- Keep architect, implementer, and reviewer as persistent development roles; install the selected client's enabled native definitions and retain their required local bodies.
- Preserve saved client, role enablement, model/effort pairs, delegation edges, and single-agent mode; cleanup does not change those choices.
- Keep one authoritative procedure per role and thin client adapters; do not introduce a generator, installer service, plugin, or self-deletion hook.
- Ordinary development and review must work without the source AEK checkout or author-machine absolute paths.
- Preserve catalog schema version 1, profile IDs, Python 3.11+ standard-library tooling, and existing contained, flat, and custom layouts.
- Preserve unrelated files, local customizations, historical evidence, and explicit persistent installations; source reclassification alone authorizes no consumer deletion.
- Do not change native model settings, permission semantics, technology examples, or Superpowers plugin contents in this task.

## Selected approach and alternatives

Separate source preparation resources from copied bundle resources in the
existing catalog. Keep native templates in AEK and use the selected ones to
prepare final native files. Keep the shared role bodies locally available in
the target. This is the narrow extension of the direction accepted by the user.

Copying everything and deleting it afterward creates unnecessary target writes,
cleanup ownership, and interruption cases. It is rejected. Embedding complete
role bodies into generated native files would remove the explicit local read,
but adds generation and customization reconciliation obligations. It is also
excluded; the current shared-body architecture already avoids procedure drift.

Client-specific formats still need their adapters: Codex documents TOML custom
agents, while Claude Code and Cursor document Markdown definitions with native
metadata. Their formats do not require shipping all source adapters to a target.
Sources checked on 2026-10-24: [Codex agents](https://learn.chatgpt.com/docs/agent-configuration/subagents),
[Claude Code agents](https://code.claude.com/docs/en/sub-agents), and
[Cursor agents](https://cursor.com/docs/subagents). Native discovery and execution
remain separate from static preparation checks.

## Resource ownership and selection

| Resource | Source library | New target adoption |
| --- | --- | --- |
| Selected standards and existing runtime assets | Authoritative policies and reusable assets | Retain their selected closure |
| `templates/agents/{architect,implementer,reviewer}.md` and composition README | One procedure per role and its loading contract | Retain in the bundle as operational reference content, even though the existing directory is named `templates` |
| `templates/{codex,claude,cursor}/agents/af-*` | Native preparation templates | Do not copy inactive versions; prepare only enabled native definitions for the chosen client |
| `templates/codex/config.toml`, `templates/codex/README.md`, `templates/framework/model-routing.toml` | Setup examples and client preparation guide | Do not copy inactive versions; prepare actual selected configuration/record separately |
| `aek-integrate-project`, `aek-model-setup`, `aek-model-reassign` templates | Import, setup, and later reassignment procedures | Read from source by default; no inactive bundled copies or implicit native installation |
| `aek-design-feature`, `aek-review-changes` templates | Optional ongoing workflow entry templates | Install only explicitly selected native entries; do not retain inactive template duplicates |
| Named catalog `templates` for entry/bridge/rule creation | Preparation inputs | Create the selected adapted entry; omit raw template copies by default |

The three common role bodies remain catalog resources. An enabled role gets its
native adapter and the corresponding local body; a disabled role gains no native
installation or invocation merely because a shared body is available. This
preserves all three requested development specializations without silently
enabling roles in existing single-agent or partially configured projects.

Keep other existing assets, such as planning/task templates and the adoption-record
template, under their current contracts. A wholesale cleanup of every file named
`template`, role-body relocation, or a change to planning ownership is outside scope.

An explicitly requested persistent setup skill remains supported, as does a prior
explicit installation. Its active native entry does not justify also copying its
inactive source template. Installation/update procedures remain owned by
[MIGRATION](../../MIGRATION.md), not by a new lifecycle policy file.

## Catalog and checker contract

Add optional `profiles[].source_resources`, an array of nonempty relative paths,
defaulting to empty. Existing `resources`, profile `source`, and shared `assets`
retain their bundle-availability meaning. Schema version 1 and existing IDs remain
unchanged. Put preparation-only resources from the table above in the new field;
the integration skill already used directly from source need not become a new
bundle dependency. Existing named `templates` remain source preparation inputs.

Maintain one catalog parser and dependency traversal. It must expose separate
selected bundle and source-preparation inventories so fixture preparation cannot
mistake source validation results for a copy list. Source validation checks both
inventories. Target validation requires the bundle inventory and does not require
absent source preparation resources. Present legacy named entry templates retain
their existing optional validation behavior; no check silently deletes them.

Validate new-field types and path boundaries using the existing catalog rules.
Within a selected closure, a path cannot be both a bundle resource and a declared
source-only resource. Repeated paths within one category are deduplicated. Missing
required runtime files remain errors. Old catalogs without the new field keep
their existing resource requirements; the checker does not reinterpret their
paths by filename or infer their lifecycle from the selected client.

The catalog classifies availability, not active installation. Native files outside
the bundle still require explicit checks and managed-scope recording. Do not add
a general deployment engine or infer a client by finding a directory.

## Native installation and local references

For an adoption selecting all three development roles, prepare exactly those
three native definitions for the chosen client, with the saved pairs and limits.
Keep the existing native destinations and identities:

- Codex: `.codex/agents/af-<role>.toml`.
- Claude Code: `.claude/agents/af-<role>.md`.
- Cursor: `.cursor/agents/af-<role>.md`.

Here `<role>` is `architect`, `implementer`, or `reviewer`. Retain the main-session
orchestrator and its configuration; do not create a new orchestrator agent file.
Single-agent mode continues to install no active specialist. Existing unrelated
native files are preserved, including other-client files not owned by the adoption.

Native task-skill installation keeps the currently verified Codex mapping;
adding Claude Code or Cursor skill mappings is outside this change. Without a
verified installed skill entry, ordinary design/review uses the adopted local
guides and core rules. Do not retain an inactive template to imply native activation.

Keep `.agents-framework/templates/agents/<role>.md` as the default shared-body
route, rebased for flat/custom layouts. These files are continuing dependencies,
not disposable setup templates. Preserve explicit loading, root handoff, and
missing-body failure behavior. Ordinary work requires neither an adoption-history
read nor an accessible source repository.

Adapt links in copied guides that refer to omitted setup resources. Installation
examples may become labelled source references resolved through adoption provenance;
selected active entries must point to their actual native destinations. Essential
runtime instructions must remain local. Never label a missing role body, required
policy, or selected skill guide as optional merely to make a checker pass.

Update the adoption record's native skill mapping to distinguish source template
identity from target native destination; remove the assumption that an inactive
bundle template must exist. Required shared bodies and final native files remain
managed target paths with the existing accepted-content and recovery evidence.

## Existing adoptions and recovery

No consumer project changes as a side effect of source maintenance. During an
authorized future update, inventory prior inactive copies and active definitions
separately. Use the existing base/current/new comparison and ownership rules:

1. Preview which proven managed, unchanged inactive copies will be retired and
   repair their affected references in the same proposal.
2. Preserve locally modified or unowned copies until an explicit reconciliation
   decision covers them. Do not delete directories by prefix or matching role name.
3. Preserve active development agents, their bodies, and explicitly retained native
   skills. Reclassification is not a role-disable or model-reassignment request.
4. Keep preparation write-free; preserve originals outside native discovery before
   application. An interruption must not leave retained agents without their bodies.
5. Record accepted retirements/retentions and recovery state in the existing adoption
   record. Repeating an accepted update must not recreate deliberately absent copies.

## Acceptance criteria

| ID | Observable result |
| --- | --- |
| AC1 | A delegated fixture selecting architect, implementer, and reviewer retains all three active definitions and reachable local bodies for each supported client. Single-agent/disabled-role selections remain unchanged. |
| AC2 | New bundles omit all nine inactive role adapters, source setup/configuration examples, and inactive skill-template duplicates. Only the selected client's enabled native definitions are created. |
| AC3 | Source checks detect missing/malformed source resources; target checks accept their absence and still reject missing runtime resources. Legacy catalogs retain their old requirements and IDs. |
| AC4 | Optional design/review skills remain usable from their selected native paths without bundled template copies. Without a persistent skill selection, create no setup skills or empty native skill directory. Explicit persistent setup selections remain supported. |
| AC5 | Contained, flat, custom, and independently opened child fixtures resolve local role bodies, policies, and native skill guides without source-checkout access. Missing runtime dependencies still fail. |
| AC6 | Update preparation preserves current target bytes. Retirement distinguishes owned unchanged, locally modified, unowned, and explicitly retained files; accepted repeats do not resurrect inactive copies or remove active agents. |
| AC7 | Evidence distinguishes source inspection, static fixture checks, and native client observation. This change introduces no self-deletion, generator, model reassignment, or live consumer update. |

The implementation plan maps these criteria to existing checkers, fixtures, and
document owners. Client execution is not claimed from syntax or fixture success;
record a native smoke check only if an appropriate authorized target is available.
