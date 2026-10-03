# Archived native application delivery history

> **Final closure accepted by the user on 2026-09-22.** The current rules-only
> part is complete and accepted, including removal of the additional application.
> No unchecked item or pilot below remains pending for this accepted stage.
> Future changes belong to a new part/version with separate scope and planning;
> they do not automatically reactivate this archived backlog.

> **Closed on 2026-09-22 by explicit user instruction.** The Python application,
> client adapters, CLI, monitor, tests, schemas and packaging were removed. The
> framework retains rules, skills and native templates. All implementation status,
> unchecked tasks and pilot proposals below are historical, not active work or
> authorization for further execution. Current scope: [rules framework](../specs/2026-09-20-agents-framework.md).
> Removal backup: `/tmp/af-remove-application-cgs8b5ja/`; checks are recorded in its
> handoff and in the engineering-practices plan.


> For agentic workers: follow the selected execution method under
> [the Superpowers adaptation](../../standards/superpowers.md). Use
> `superpowers:executing-plans` for inline execution; use
> `superpowers:subagent-driven-development` only for selected, independently
> assignable work. A plan does not authorize implementation or Git actions.

**Goal:** deliver stack-aware rule adoption, editable agent schemes, and model
visibility through one installed Codex, Claude Code, or Cursor client and its subscription.

**Architecture:** one framework-owned TOML profile feeds selected rule composition
and one native client adapter. Deterministic inspection, validation, and scoped
writes support an AI-assisted terminal wizard; native session observations feed
the status panel. Native clients remain responsible for executing agents.

**Tech stack:** Markdown rules/specifications, TOML workspace state and Codex
configuration, Claude/Cursor Markdown/YAML agents and supported settings. The application
core uses Python 3.11+, standard-library TOML/process interfaces, and Pydantic 2;
the versioned contract records the package layout and native integration limits.

**Spec:** [Agent_Engineering_Kit product specification](../specs/2026-09-20-agents-framework.md).
This plan owns delivery progress; [MIGRATION.md](../../MIGRATION.md) owns the
separate procedure for adopting the framework in a target project.

## Global Constraints

- Each active workspace profile selects exactly one installed client.
- Model calls use that client's existing authentication and subscription path.
- The application runs in an existing terminal; it does not implement a terminal emulator.
- Workspace choices persist in `.agents-framework/model-routing.toml`.
- Model and effort choices are explicit, capability-checked pairs; examples are not assignments.
- Catalog refresh never silently changes saved model assignments.
- Shared policy has one owner; nested instructions and explicit exceptions must be reconciled.
- Saved settings, active configuration, and runtime-reported execution are distinct evidence.
- Agent-facing rules and specifications are canonical English; the user README is Russian.
- Default execution is one logical stage in the current checkout, followed by a user checkpoint.
- Git writes, worktrees, installation into other projects, and live pilots need task authorization.
- Documentation completion does not mean adapters, onboarding, or runtime behavior have passed a pilot.

Planning root: `/home/vitalii/Documents/Local_Project/AgentsFramework`, outside
Git in the inspected workspace. This task changes framework files in place;
no nested repository checkout or external project is selected for installation.
The current workspace has no active saved role selection. User examples must
not be used as implicit assignments to future implementation workers.

## Historical authorization and status before removal

Historical authorization (2026-09-22, superseded by removal and final acceptance):
the user accepted K18 and authorized K19
and P3, P4, P4C, P5, P6 and P7 through delegated execution without intermediate
human checkpoints. Workers use the explicitly selected `gpt-6-astra` / `high`.
Status recorded before removal: D0, P1, P1C, P2 and K19 complete. Shared apply, P3 and P4
implementation are complete; P4C implements drafts and guarded mappings but its
installed native write/launch contract remains unverified. P5 implementation is
complete, as is P6 observation/CLI integration. P7 setup checks passed for Codex
and Claude; runtime acceptance remains incomplete because of environment/access
limits. One explicitly approved external Claude retry confirmed native handoff
and reported models, but the pilot write permission blocked the artifact. P7
therefore remains incomplete; implementation is ready for user review.
On 2026-09-21 the user requested sequential engineering-practice research for
the full supported stack before continuing. The proposed sequence and its
topic-level progress are owned by the
[engineering practices plan](2026-09-21-engineering-practices.md).
This document retains ownership of native-adapter delivery. The model choice above
is for implementation workers in this session, not a saved target-project scheme.
There is no authorization to change global client configuration or authentication,
install into unrelated projects, or initialize/commit Git state.

D0 baseline: `/tmp/af-specs-plans-0d8s0fkp/baseline.json`, with copies of existing
affected files and prior absence of the new specification and plan. Retain this
local baseline through review; future stages capture their own affected paths.

P1 baseline: `/tmp/af-p1-contracts-7usafis3/baseline.json`, recording the affected
documents and prior absence of the new package, schema, contracts, and fixtures.

P1C baseline: `/tmp/af-cursor-contract-cok4j8m7/baseline.json`, covering 17 affected
paths before the Cursor extension, including previous P1 edits.

P2 baseline: `/tmp/af-p2-rules-uf6rzgwl/baseline.json`. Temporary Git repositories
are allowed only as isolated discovery test inputs; no project Git workflow or
installation into an external project is part of P2.

## Deliverables and boundaries

| Stage | Observable deliverable | Depends on |
| --- | --- | --- |
| D0 | Agreed scope recorded; architecture, standards, and adoption plan agree | Completed research and user clarification |
| P1 | Versioned configuration and client contracts, implementation stack, fixture matrix | D0 |
| P1C | Cursor included in the profile/schema and checked native integration contract | P1, user request for Cursor |
| P2 | Selected rules and nested entry points can be composed without conflicting policy | P1 |
| P3 | Codex settings can be inspected, previewed, applied, and reconciled | P1, P2 |
| P4 | Equivalent Claude Code configuration through its native formats | P1, P2 |
| P4C | Cursor role configuration and project-specific coordinator launch recipe | P1C, P2 |
| P5 | Terminal wizard supports AI proposals, manual edits, apply, reassignment, and native launch | P2, P3, P4, P4C |
| P6 | Agent status panel shows model evidence for supported native sessions | P3, P4, P4C, P5 |
| P7 | Bounded adoption pilots establish supported versions and observed behavior | P2–P6, including P4C |

P3, P4, and P4C have independent adapter ownership after their shared contracts.
That permits separate work if authorized; it does not require parallel workers.
Deliver a stage's necessary checks with its implementation, not at the final pilot.

## Task D0: consolidate the specification and roadmap

**Files:** create the linked specification and this plan. Update `README.md`,
`ARCHITECTURE.md`, `MIGRATION.md`, `standards/core.md`,
`standards/orchestration.md`, `standards/model-configuration.md`, and
`templates/codex/README.md`. Mark the research note as evidence superseded by
the specification for product decisions. Do not activate templates or change
native settings.

- [x] Record all confirmed goals, orchestration schemes, terminal scope, and model visibility.
- [x] Reconcile Codex-only descriptions and the three-role baseline with the target scope.
- [x] Map each requirement to implementation stages and concrete verification scenarios.
- [x] Check changed Markdown, local links/anchors, requirement coverage, and baseline diffs.
- [x] Record actual evidence and leave P1–P7 planned.

## Task P1: settle configuration and native integration contracts

**Files:** create `docs/specs/native-client-contracts.md` and
`schemas/workspace-profile.schema.json`; define fixture contents under
`tests/fixtures/workspaces/`. The contract document must name the chosen source,
test, package, and command paths before P2–P6 implementation details are expanded.

**Consumes:** specification R02–R05, R08–R10, R12 and inspected native capabilities.
**Produces:** one extended profile schema with explicit v1 conversion, the
application stack decision, and these shared semantic records:

| Record | Contract content |
| --- | --- |
| `WorkspaceInventory` | Workspace root, repository boundaries, instruction sources, stack facts, selected rule references, conflicts |
| `ClientCapabilities` | Client/version, native format and activation support, catalog/effort support, delegation limits, observation coverage |
| `ModelCatalog` | Native IDs, aliases/resolution when known, supported efforts, provenance, observation time, availability evidence |
| `WorkspaceProfile` | Schema/setup state, client, project/profile references, role pairs, delegation relationships, workflow conditions/checkpoints |
| `ChangePreview` | Target paths, owned field changes, source-state preconditions, collisions, diagnostics |
| `ApplyResult` | Applied/unchanged/partial/failed result, affected paths, repair evidence, saved agreement, activation requirement |
| `AgentObservation` | Session/agent/parent/task identity, role, lifecycle, selected/configured/reported model and effort, source, time, unknown/stale state |

- [x] Inspect installed CLI help and supported catalog/session interfaces; verify
  the chosen integration retains native subscription authentication. Resolve
  Claude catalog discovery or document the supported manual-selection fallback.
- [x] Select the implementation language, packaging, initial platforms, and
  version capability policy; record the reasons and exact module/test paths.
- [x] Specify serialized TOML keys, defaults that need consent, role IDs,
  references, limits, correction transitions, setup states, and migration rules.
- [x] Define validation results for unknown schema/client, missing required
  owner, invalid role references, forward cycles, unsupported effort, and
  unavailable or unverified model choices.
- [x] Define fixtures for a new directory, a non-Git workspace with two nested
  repositories, existing custom native files, a v1 profile, and malformed or
  conflicting settings. Include unsupported/version-limited capabilities.
- [x] Validate representative accepted/rejected profiles and preserve the
  explicit distinction between schema validity, saved agreement, and activation.

**Exit evidence:** contracts fit both native formats without invented shared
capabilities; fixtures expose the listed failures; downstream tasks have real
file/command mappings. Record the P1 result here before implementation proceeds.

## Task P1C: extend the native contract to Cursor

**Files:** extend the existing specification, native contract, architecture,
README, adoption/model/orchestration guidance, profile client type and generated
schema. Add `docs/research/2026-09-20-cursor-agent-orchestration.md` and a Cursor
profile fixture; extend existing profile, migration, and catalog boundary checks.

- [x] Verify official role/model/effort formats, CLI settings scope, and local
  executable/help/authentication evidence without activating agents.
- [x] Add the `cursor` client ID to v2 without changing existing pairs or applying
  legacy Codex assignments to the new client.
- [x] Specify native role discovery, selector preservation, a project-specific
  coordinator launch recipe, and separate CLI/editor/runtime evidence.
- [x] Add P4C and extend P2/P5/P6/P7 ownership without renumbering existing stages.
- [x] Check the affected contracts, schema, types, documents, and baseline diff;
  record actual results and retain unverified native behavior explicitly.

**Exit evidence:** Cursor is representable and validated in the shared profile;
adapter work has concrete inputs, targets, commands, and acceptance scenarios.
Adding the client ID does not claim its native adapter or subscription access
has passed a pilot.

## Task P2: compose relevant rules and repository entry points

**Files:** evolve `standards/`, `templates/AGENTS.root.md`,
`templates/AGENTS.project.md`, and `templates/project-architecture.md`; add the
client-specific instruction templates and rule-composition code mapped in P1.
Create database/technology profiles only for the selected pilot stacks, using
checked primary references, and register their applicability.

**Consumes:** `WorkspaceInventory`, `WorkspaceProfile`, `ClientCapabilities`.
**Produces:** a selected rule set, native reading routes, conflict report, and
`ChangePreview` covering workspace and independent repository entry points.

- [x] Inspect project metadata/passports and select applicable common, language,
  framework, database, and technology guidance without loading every profile.
- [x] Preserve local commands/contracts; resolve opposing instructions and
  record explicit exceptions and provenance for derived copies/imports.
- [x] Include conditional Factory/Facade/Strategy/monadic guidance through the
  relevant rule owner, without requiring these abstractions in every project.
- [x] Prepare supported entry points for all three clients; cover clients that need
  a `CLAUDE.md` bridge and specialist roles that need explicit shared instructions.
  Include Cursor's selected `.mdc` routes and compatibility agent discovery.
- [x] Verify fixture discovery from the workspace and each repository opened
  independently. Check that a simple task selects only relevant guidance and
  that changed derived files are reported as drift.

**Exit evidence:** no hidden reliance on parent paths outside discovery; retained
local invariants and required checks; bounded context routes for the pilot stack.

P2 implementation decisions: inspect manifests and an optional structured block
in the architecture passport without running project commands; retain declared
versions/constraints as evidence, not verified installed versions. Register the
existing profiles and conditional reading routes in `standards/catalog.toml`.
Use the existing Python/FastAPI and Next.js fixtures with declared PostgreSQL and
Docker evidence to cover database/technology selection.

Generated policy is a self-contained, versioned subset at each repository entry
point, with source/content digests and a manifest for drift detection. Preserve
unmanaged instruction bytes; require explicit digest-bound review decisions for
existing instructions before treating them as reconciled. The program does not
claim to prove arbitrary natural-language consistency. Required local reading
routes resolve inside each generated bundle; optional explanatory links outside
the selected bundle become source labels, not broken filesystem links.

`inspect_workspace` produces boundaries, sources, facts, and diagnostics;
`load_catalog`/`select_rules` produce registered selections and conditional routes;
`compose_rules` produces a read-only `ChangePreview`, including entry points and
specialist instruction text for later adapters. P2 does not apply the preview.
The exact APIs, review decisions, and preview limits are documented in the
composition contract (`../specs/rule-composition.md`, removed application artifact).

## Task P3: implement the Codex adapter

**Files:** extend `templates/codex/` and the Codex adapter/source tests mapped in
P1; reconcile applicable setup/reassignment template references without installing
them. Native targets remain `.codex/config.toml` and managed agent TOML files.

**Consumes:** P1 contracts and P2 rule previews.
**Produces:** Codex `ClientCapabilities`, `ModelCatalog`, `ChangePreview`, and
`ApplyResult`, with explicit activation and observation support.

- [x] Implement native inspection/catalog access and version-aware role/default
  mapping, covering all selected role/model/effort pairs and concurrency limits.
- [x] Generate field-level previews; preserve unrelated keys, comments, roles,
  permissions, and custom review-command settings.
- [x] Apply only a validated preview whose source preconditions still hold;
  parse and compare results, detect partial writes, and provide scoped recovery.
- [x] Exercise initial setup, one-role reassignment, no-change reapply, collision,
  malformed TOML, unsupported effort, and an edit made after preview.
- [x] Check role-file/default/spawn precedence and project trust/runtime
  overrides. Report saved agreement and activation separately.

**Exit evidence:** meaningful adapter/fixture checks pass; unrelated bytes and
assignments survive; no parser result is presented as a live model switch.

## Task P4: implement the Claude Code adapter

**Files:** create `templates/claude/` and the Claude adapter/source tests mapped
in P1; use managed `.claude/agents/af-<role>.md` and supported native settings.

**Consumes:** the same P1/P2 contracts as P3; no dependency on Codex execution.
**Produces:** equivalent client-specific capability, catalog, preview, and apply
results, including documented unavailable features and activation requirements.

- [x] Implement Markdown/YAML role mapping and supported main-session settings;
  validate effort and invocation/environment overrides against the client version.
- [x] Use existing native sign-in for catalog/assisted operations; do not select
  `--bare` or an integration path that requires replacing subscription access.
- [x] Implement preservation, source-precondition checks, and partial-write
  recovery for existing roles/settings and instruction bridges.
- [x] Verify initial setup, one-role reassignment, no-change reapply, frontmatter
  errors/name collisions, unavailable effort, and managed/environment overrides.
- [x] Verify project-policy loading for configured specialist roles and both
  launch scopes; avoid relying on built-in roles that omit required instructions.

**Exit evidence:** the same observable configuration contract as P3 holds in
Claude's native format. Unverified catalog or runtime support remains explicit.

## Task P4C: implement the Cursor adapter

**Files:** create `src/agents_framework/clients/cursor.py`, `tests/test_cursor.py`,
and `templates/cursor/`; reuse shared change handling. Native specialist targets
are `.cursor/agents/af-<role>.md`; selected `.mdc` rules remain owned by P2.

**Consumes:** P1C contracts, P2 previews, and observed Cursor CLI capabilities.
**Produces:** Cursor capabilities/catalog, native change preview/apply results,
and a validated coordinator launch recipe for the P5 `agents-framework run` command.

- [ ] Establish a supported CLI version and existing account sign-in path.
  Check catalog and model-parameter coverage; treat old/unprobed versions and
  incomplete/unauthenticated catalogs as unverified, without automatic upgrades.
- [ ] Map selected role pairs to supported model selectors in Markdown/YAML.
  Preserve unrelated selector parameters, role instructions, and metadata;
  reject contradictory effort representations and malformed selectors.
- [ ] Reconcile native and compatibility agent directories, matching names,
  local rules, and required specialist instructions in both launch scopes.
- [ ] Prepare a project-specific coordinator launch recipe; validate parameter
  support on this path and keep global preferences/project permissions intact.
  Verify AI proposal execution through non-writing native controls and login.
- [ ] Implement preview preconditions, scoped native writes, no-change reapply,
  partial-write repair, and saved agreement separate from activation.
- [ ] Verify one-role reassignment, preserved unrelated fields, stale previews,
  version-limited features, plan/admin model substitution, and default/session
  mismatch. Record supported observation coverage without fabricating telemetry.

Implementation exists for guarded selector mapping, collision detection, preview,
reassignment and shared apply/recovery; 40 fixture tests passed. The criteria above
remain unchecked as native-supported acceptance because the inspected installed
CLI supplies neither verified controls nor authenticated access. No fixture-only
positive contract is presented as installed support. Proposal execution and
Cursor CLI/editor observation remain unsupported.

**Exit evidence:** native role files and the launch recipe preserve the chosen
project pair; unsupported settings are explained; no global model reset or
cross-client execution is used. Real activation remains a bounded P7 check.

## Task P5: deliver the terminal wizard and editable schemes

**Files:** implement the terminal entry point and setup/reassignment use cases
mapped in P1; update `README.md`, model-configuration guidance, and the scoped
setup/reassignment skill templates once their behavior exists.

**Consumes:** inventories, capabilities/catalogs, profile schema, and previews
from P2, P3, P4, and P4C. **Produces:** a saved profile and native files with an `ApplyResult`.

- [x] Implement inspect → select client/rules → edit scheme and role pairs →
  preview → apply → report agreement/activation. Reuse existing explicit choices.
- [x] Provide `agents-framework run` for the selected client's validated launch
  recipe in the existing terminal; report when a direct native launch would use
  another coordinator default. Do not convert project setup into global settings.
- [x] Add the user's coordinator-based starting scheme and optional roles;
  distinguish task ordering from nested spawning and validate dependencies.
- [x] Invoke the selected installed CLI for a structured AI proposal; validate
  its fields/references before use. Support manual correction and selection when
  assistance, catalog access, or account limits prevent a model-assisted result.
- [x] Keep canceled/invalid proposals from writing files. Report blocked paths,
  collisions, stale catalogs, unsupported pairs, and partial writes specifically.
- [x] Verify an end-to-end fixture setup, restart without repeated onboarding,
  partial reassignment, catalog update without automatic reassignment, invalid
  AI output, optional-role changes, and preservation of mandatory checkpoints.
- [x] Document ordinary direct native-client use after setup; the wizard must
  not become a required proxy for every development task.

Implementation/fixture criteria above are complete. Paid proposal success and
live assignment remain native acceptance evidence, not fixture conclusions.

**Exit evidence:** repeatable configuration through the selected adapter in an existing
terminal; model examples and AI output never act as implicit user selections.

## Task P6: display subagent model evidence

**Files:** implement the observation adapters and terminal status view mapped in
P1, with recorded event fixtures and user-facing coverage documentation.

**Consumes:** `WorkspaceProfile`, `ClientCapabilities`, native session events.
**Produces:** `AgentObservation` records and a live view of supported sessions.

- [x] Support a session started through the application and supported attachment
  where available; identify its client/workspace before attributing events.
- [x] Show role/task/status, configured model/effort, runtime-reported model,
  mismatches, source, and freshness. Keep missing information unknown.
- [x] Handle model replacement, task completion/error, disconnection, stale
  observations, and duplicate/out-of-order events without inventing execution.
- [x] Verify that selected/default/spawn values are not labeled per-operation
  execution proof and that a monitor disconnect does not cancel the native task.
- [x] Verify unavailable attachment falls back to an honest coverage explanation
  and native inspection, without restarting existing sessions.
- [x] Check Cursor observation coverage separately for CLI and editor; do not
  interpret a generic stream or saved selector as resolved per-agent model data.

**Exit evidence:** fixture events produce correct attribution and state changes;
real native evidence remains a P7 requirement. No terminal emulator is introduced.

## Task P7: run bounded adoption pilots and record compatibility

**Files:** update `README.md`, `MIGRATION.md`, client documentation, and this
plan's evidence. Pilot-generated files belong only to explicitly selected
temporary targets or authorized target repositories.

**Consumes:** P2–P6 results and the existing work-mode/verification policies.
**Produces:** an evidence-based compatibility record and adoption decision.

- [x] Select a bounded new-project fixture and an existing nested-repository
  target; preserve their pre-stage state and declare any live calls/writes.
- [ ] Run each client independently through existing subscription access. Check
  initial setup, role loading, model/effort evidence, and a later ordinary task.
  Include Cursor CLI startup through the saved launch recipe and a direct launch
  with different defaults; test editor reuse only under a separately stated scope.
- [ ] Exercise a small selected-role handoff through implementation, necessary
  checks, and warranted review; confirm the user checkpoint and resumption.
- [ ] Confirm independent repository loading, reassignment, catalog behavior,
  model display, and explicit unknown/override cases on the tested versions.
- [x] Record exact client versions, scenarios, observed limits, and unmet
  criteria. Mark only demonstrated capabilities supported; do not substitute
  fixture checks for live assignment evidence or claim unmeasured cost savings.

**Exit evidence:** the specification's acceptance scenarios are met or explicit
limits are recorded for a scope decision. A failed required scenario keeps the
affected deliverable incomplete; it is not waived by recording the failure.

## Review Focus

| Failure scenario | Expected behavior | Evidence owner |
| --- | --- | --- |
| CLI or SDK path excludes subscription sign-in | Select a compatible native route or report the unsupported operation | P1, P1C, P3, P4, P4C, P7 |
| Nested root is not discovered or a role skips policy | Generate a reachable entry point and verify actual role loading | P2, P4, P4C, P7 |
| Manual edit races preview or apply stops midway | Preserve independent changes and report a repairable partial result | P3, P4, P4C, P5 |
| Native overrides select another model or effort | Expose mismatch; saved agreement does not imply activation | P3, P4, P4C, P6, P7 |
| Model alias changes or catalog becomes stale | Preserve intent and show provenance/availability limits | P3, P4, P4C, P5, P7 |
| Cursor coordinator differs from global defaults or compatibility roles collide | Validate the project launch recipe and effective role set without resetting user-wide settings | P1C, P2, P4C, P5, P7 |
| Optional role or preset removes a required check | Preserve required ownership and checkpoints or reject the proposal | P1, P5, P7 |
| Session cannot be observed or event arrives late | Show unknown/stale state; do not attribute it to another agent | P6, P7 |

## Requirement coverage

| Requirement | Stages |
| --- | --- |
| R01 | P2, P7 |
| R02 | P1, P1C, P3, P4, P4C, P5, P7 |
| R03 | P1, P1C, P3, P4, P4C, P5 |
| R04 | P1, P1C, P3, P4, P4C, P5, P7 |
| R05 | P1, P2, P5, P7 |
| R06 | P2, P3, P4, P4C, P7 |
| R07 | P5, P7 |
| R08 | P1, P1C, P3, P4, P4C, P5, P7 |
| R09 | P1, P1C, P3, P4, P4C, P5, P7 |
| R10 | P6, P7 |
| R11 | P2, P5, P7 |
| R12 | P1, P2, P7 |

## Handoff

For each implemented stage, record changed paths, baseline, criteria met,
actual commands/inspections and their results, limitations, and the next stage.
Use this document as the single progress owner. Stage results are recorded below;
P3 is the next product stage after completed P2 and its user checkpoint.

D0 completed on 2026-09-20: created the product specification and delivery plan,
reconciled architecture, adoption, role/model, pattern, and baseline-template
descriptions, and linked the canonical artifacts from the README and research.

Verification: an inline Python artifact check covered all 10 changed Markdown
files, 102 local links including 3 anchors, matching 12 Global Constraints, all
12 requirements mapped to stages, and all 7 planned product stages. It found no
unfinished markers in the new artifacts, missing local targets, trailing
whitespace, unclosed fences, or altered baseline copies. Scoped baseline diffs
and requirement semantics were reviewed. Application tests and subscription
calls were not part of this documentation stage; no native configuration was
activated. At D0 completion, exact application contracts, stack choice, and
compatibility probes remained P1 work.

P1 completed on 2026-09-20, inline in the current directory. Added the
native client contract (`../specs/native-client-contracts.md`, removed application artifact), Python package
metadata and typed validation modules, generated v2 schema, explicit non-writing
v1 draft migration, and the fixture matrix. Clarified purpose, audience, and
new/existing/multiple-project scenarios in the README; updated architecture,
model-configuration guidance, and the specification to reference the implemented
contract. The P1 baseline above covers all 30 changed/new files.

Verification:

- `python3 -m pytest -q --tb=line`: 37 tests passed, including graph/reference
  validation, strict TOML version types, preserved migration choices, catalog
  updates/aliases, unsupported pairs, and unknown native capabilities.
- `python3 -m mypy`: no issues in 8 source/test files, with strict mode,
  explicit/unimported Any forbidden, and the typed Pydantic plugin enabled.
- `PYTHONPATH=src python3 -m agents_framework.schema --check`: generated schema
  matches the model; regeneration was run when the artifact was introduced.
- `python3 /tmp/af-p1-contracts-7usafis3/check_artifacts.py`: checked all 30 files,
  local Markdown links/anchors, JSON/TOML and fixture frontmatter, baseline-copy
  integrity, matching Global Constraints, and coverage of all 12 requirements.
  The intentionally malformed TOML input was checked as an expected failure.
- Reviewed scoped document diffs and the implementation for separation of saved
  intent, capability evidence, and activation; no delegated review was invoked.

Local native evidence: Codex 0.155.1 and Claude Code 2.1.275 command help and
subscription sign-in status were inspected. Codex reported ChatGPT sign-in;
Claude reported first-party claude.ai sign-in. A Codex metadata request did not
yield a validated catalog response: the default SQLite state path was read-only
and a temporary-state retry timed out. The contract retains unverified catalog
state and a manual Claude model-selection fallback. Model inference and native
role activation were not tested. No existing authentication, active profile,
native configuration, Git state, or other project was changed.

Remaining boundaries: P1 checks supplied capability observations and declarative
fixtures. It does not yet discover real repository boundaries, compose/install
rules, write native settings, implement the terminal wizard, or observe running
agents. These are P2–P7 deliverables, not failures waived by this stage's tests.
Next stage after the agreed checkpoint: P2, stack-aware rule composition and
reachable workspace/independent-repository entry points, using the exact module
and test ownership recorded in the contract.

P1C completed on 2026-09-20. Added the `cursor` client ID to the existing v2
profile and generated schema, an inactive Cursor fixture, and extensions to the
existing profile/migration/catalog checks. Updated the specification, native
contract, architecture, README, adoption/model/orchestration guidance, and this
plan. P4C owns the new adapter; P5 owns its profile-aware native launch command.
The P1C baseline covers all 17 affected paths and preserves the completed P1 work.

Verification: `python3 -m pytest -q --tb=line` passed all 40 tests;
`python3 -m mypy` reported no issues in 8 source/test files;
`PYTHONPATH=src python3 -m agents_framework.schema --check` passed after schema
regeneration. The scoped artifact check at
`/tmp/af-cursor-contract-cok4j8m7/check_artifacts.py` checked all 17 files, local
links/anchors, TOML/JSON, unchanged baseline copies, matching Global Constraints,
and all 12 requirements mapped to stages. Scoped diffs were reviewed.

Native evidence and limits are in the
[Cursor research](../research/2026-09-20-cursor-agent-orchestration.md): the installed
CLI is `2026.01.28-fd13201`, and its status reported no authenticated session.
`agent models` exited successfully without establishing an authenticated,
complete catalog. Current documentation supports native role files and model
parameters; support on this local version, account access, coordinator activation,
and per-agent observations remain unverified. No login, CLI upgrade, inference,
or agent activation was performed. Those operations and the native adapter remain
in their planned stages. P2 is still the next implementation stage after review.

### P2 result

P2 completed on 2026-09-21, inline under the already authorized stage. Added typed
workspace/metadata inspection, a 17-profile catalog, rule selection, portable
rendering, ownership/review records, and read-only composition/preconditions.
PostgreSQL and Docker guidance uses the primary references linked in those rules.
Updated the README, architecture, contracts, entry/passport templates, and fixture
descriptions. The stage baseline preserves all 29 affected paths at
`/tmp/af-p2-rules-uf6rzgwl/baseline.json`; the scoped diff is `p2.diff` beside it.

The existing Python/FastAPI and Next.js fixtures now carry actual manifest inputs,
declared PostgreSQL evidence, and Docker presence. Tests create two temporary
Git repositories, compose per-project policies, and open copied repositories
independently for Codex, Claude Code, and Cursor. Native entries contain local
routes and exported specialist instructions; Cursor globs retain project scope.
Tests preserve the API check and explicitly replace the opposing web instruction.
The engine requires digest-bound review decisions and does not claim automatic
natural-language conflict resolution. Required routes resolve inside the copied
bundle; optional omitted-source links are labeled references.

Verification completed:

- `python3 -m pytest -q`: 66 passed (40 existing contract checks and 26 P2 cases).
- `python3 -m mypy`: no issues in 16 source/test files.
- `PYTHONPATH=src python3 -m agents_framework.schema --check`: current schema.
- `/tmp/af-p2-rules-uf6rzgwl/check_artifacts.py`: all 29 files, Markdown/local
  links, TOML/JSON, preserved baseline hashes, shared constraints, and all 12
  requirement mappings passed. Rendered template routes are checked in the
  three-client fixtures instead of against the source template's directory.
- Scoped changes reviewed for selection boundaries, preserved unmanaged bytes,
  inherited rules, native paths, owned retirement, and explicit evidence limits.

Additional P2 cases cover malformed metadata, excluded dependency directories,
symlink boundaries, unknown rule IDs, unselected repositories, deeper instructions,
CRLF preservation, unchanged reapply, stale decisions/metadata/overrides, filename
collisions, and drift in derived files or managed instruction blocks. No extra
review agent, dependency installation, native activation, model call, external
project adoption, or project Git workflow was performed.

Limits: P2 prepares previews only. Captured preconditions do not replace refreshed
discovery of new instruction paths, Git boundaries, or native settings before
apply. Installed-version resolution, native loading/activation, owned writes and
partial recovery, role configuration, wizard behavior, and model observations
retain their later-stage owners. Copies retain inherited shared rules but do not
automatically synchronize with a changed parent. All proposed fixture writes
occurred only in isolated test directories. Next stage after the user checkpoint:
P3, the Codex adapter for inspection, native previews, owned apply, and reconciliation.


## Parallel delivery authorization and interfaces — 2026-09-22

The user selected `gpt-6-astra` / `high` for direct implementation subagents and
requested parallel execution with concise final coordinator review. Use at most
three simultaneous workers (four total agents including the coordinator), fresh
bounded context, disjoint file ownership and necessary verification by each worker.
No nested delegation or mandatory extra review agents. A brief final review still
checks shared interfaces and executed evidence; it cannot waive a required scenario.

Execute K19 first, with independent shared apply preparation permitted concurrently.
After its instruction/catalog changes settle, implement P3/P4/P4C concurrently against
one shared preview/apply/launch contract. Integrate before P5, then P6 and P7. Each
worker preserves a before-state baseline and runs focused checks; the coordinator
runs affected integration checks after combination, without redundant full reruns.
No new example application/test campaign is needed for instructions; new filesystem
write and CLI behavior warrants targeted regression checks.

The shared native delivery baseline is `/tmp/af-native-delivery-vbe3nr4t/baseline.json`.
It preserves known shared paths; each worker captures additional owned paths or prior
absence in its own scoped evidence directory before writing. Plans remain here;
temporary reports and test artifacts are not another progress authority. Existing
K01–K18 and P1/P2 evidence remains valid for unchanged inputs.

Initial executable inspection: Codex 0.155.1, Claude Code 2.1.278, Cursor CLI
2026.01.28-fd13201. Version output establishes neither account access nor runtime
model selection. Client adapters must inspect supported behavior and keep unknown
capabilities explicit. P7 will use disposable owned targets; any unavailable native
access or unmet live criterion stays incomplete, rather than being hidden by fixtures.


### K19 handoff into native delivery

K19 completed on 2026-09-22. Its canonical result remains in the engineering-practices
plan: 13 instruction/catalog/template paths, two JavaScript ownership/selection fixes,
conditional-reading reconciliation and no native source changes. Existing rule tests
passed (28); three-client synthetic delivery covered all 19 profiles and 6,476 portable
links. Coordinator read the scoped diff and report; no blocking interface finding.
The native workers consume this settled policy/catalog output without repeating topic
research or example checks.

Shared formatter choice: tomlkit 0.15.1 and ruamel.yaml 0.18.17, declared in
`pyproject.toml` and installed only into `/tmp/af-native-delivery-vbe3nr4t/venv`.
They preserve native syntax/comments; package version does not validate generated
client settings. Strict typing and actual native-format checks remain required.


### Shared native foundation result

Completed the common preview/apply interface for the adapter wave. `clients/base.py`
owns native evidence, inspection, launch recipes and plans; `apply.py` implements
validated per-file writes and guarded repair; `changes.py` rejects duplicate and
ancestor-conflicting preview targets. All callbacks remain explicit. Native writes
never establish activation, and saved agreement stays unknown when reconciliation
cannot prove it. Formatter dependencies were added by the coordinator.

Worker evidence: 14 focused apply tests passed, 28 existing rule tests passed,
strict mypy passed for four owned/affected source and test files. Tests cover stale
inputs, formats, partial writes, safe repair, permissions, symlink paths and result
semantics. The coordinator inspected the critical write/repair interface and accepted
the reported serialization/CAS and crash-recovery limits. Final combined adapter
checks remain pending. Report/baseline: `/tmp/af-native-delivery-vbe3nr4t/shared-apply/`.


### Adapter integration notes

The adapter wave exposed a real P2/native boundary: P2 does not own generated native
role files, so fresh composition can request review of unchanged managed roles.
Each adapter may discharge that specific instruction-review diagnostic only after
its own ownership record proves both managed fields and the relevant complete role
context unchanged. Edited user instructions still require explicit digest-bound
reconciliation. A reused synthetic preview does not verify reapply; focused tests
must run fresh workspace inspection and rule composition.

P5 implementation may begin against the frozen shared/adapter interfaces while the
last adapter checks finish; its integration/completion still depends on all adapter
results. This overlaps independent coding, without claiming dependent checks passed.


### P3 and P4 implementation results; P4C compatibility limit

P3 Codex: five owned source/test files, **25 focused tests** and strict mypy passed.
Installed **0.155.1** and ChatGPT sign-in verified. Native TOML preserves comments,
custom defaults/review settings and scoped role policy, detects owned-field/context
drift, new role collisions and stale input, and provides a checked interactive launch.
The bounded app-server model/list attempt timed out: catalog/account model availability
remains unverified. Non-writing structured proposal isolation is unsupported on the
inspected route, so the adapter returns an explicit manual fallback. No inference or
runtime activation was claimed. Report: `/tmp/af-native-delivery-vbe3nr4t/p3/report.md`.

P4 Claude Code: four owned files, **19 focused tests** and strict mypy passed.
Installed **2.1.278**, first-party subscription sign-in and relevant native flags
verified. JSON field spans/YAML round-trip preserve user settings and role text;
policy/ownership tracking handles actual P2 recomposition, overrides and collisions.
Programmatic catalog remains unknown. Checked proposal recipe requires an explicit
pair and disables tools/MCP/hooks/session persistence; paid execution remains P7.
Native AGENTS feature gating remains unknown, so the import bridge is retained.
Report: `/tmp/af-native-delivery-vbe3nr4t/p4/report.md`.

P4C Cursor: five owned files, **40 focused tests** and strict mypy passed. Drafts,
selector parsing/preservation, compatibility-role collision handling, ownership and
revalidation are implemented. Positive apply/launch cases use clearly synthetic,
version/time-bound attestations. Actual CLI **2026.01.28-fd13201** is unauthenticated;
role-selector and interactive-selector contracts remain unverified. Actual native
writes/launch/proposals are blocked, not silently enabled from current documentation.
P4C's supported-runtime acceptance and P7 Cursor scenarios remain incomplete.
Report: `/tmp/af-native-delivery-vbe3nr4t/p4c/report.md`.

Coordinator integration run on the settled adapter interfaces:
`/tmp/af-native-delivery-vbe3nr4t/venv/bin/python -m pytest -q tests/test_profile.py
tests/test_compatibility.py tests/test_migration.py tests/test_workspace.py
tests/test_rules.py tests/test_apply.py tests/test_codex.py tests/test_claude.py
tests/test_cursor.py`: **173 passed in 9.12s**. Cursor subsequently added its final
40th focused case; its final scoped run passed. Full final package checks follow
P5/P6 integration. No native-assistant adherence is inferred from these fixtures.

### P5/P6 overlap and P7 preparation

P5 owns setup/CLI/profile serialization and user documentation. P6 independently
owns observation records/streams/status, with a callable CLI seam coordinated directly
with P5; dependent completion waits for integration. P7 prepares only disposable
`/tmp/af-native-delivery-vbe3nr4t/p7/` targets until those APIs are ready. Due to the
platform thread limit, the completed Claude worker continues the bounded P7 assignment
with its relevant P4 context; this reuse is not described as a fresh-context worker.
No extra review agents or nested implementation delegation are introduced.

P7 uses current explicit native user choices only in disposable fixtures: Codex
`gpt-6-astra` / `high`, Claude `opus[1m]` / `high`. No permanent assignments or global
settings are changed. Planned paid probes: one tiny observed role handoff/checkpoint
in a new target and one ordinary task in an independently opened nested repository
per authenticated client, bounded to 120 seconds each. A necessary short native
same-session resume can be added with its exact supported command recorded first.
Cursor's missing sign-in/support remains an unmet native criterion. Real calls must
use actual final setup and observed-launch paths, not synthetic capabilities.

P5's real standalone-project test revealed a P2 portability defect: ENTRY.md embedded
the ancestor-relative scope name, producing a spurious difference on standalone
reopen. Coordinator preserved the current template baseline and changed only its
introductory sentence to a location-neutral description. The exact existing P5 test
failed before and passed after (**1 passed in 0.94s**); no renderer or duplicate test
was added. Evidence: `/tmp/af-native-delivery-vbe3nr4t/integration/`.


### P5 terminal implementation result

The wizard, manual v2 editing, guarded preview/apply, saved-choice resume,
reassignment, optional checked proposals, recovery and native launch are
implemented. P6 commands are integrated. **25 focused tests**, scoped strict mypy
and an installed-console smoke outside the checkout passed. The wheel was
installed only in the task virtual environment; no target/global installation
or authentication change occurred. Rule resources use an explicit framework
checkout. Source/diff/check evidence: `/tmp/af-native-delivery-vbe3nr4t/p5/`.

Recovery retains both apply phases and preserves later edits. A conflicting
native rollback leaves partial profiles visible rather than restoring an old
configured marker. Successful saved agreement still requires native activation.
The coordinator reconciled stale implementation-status wording in architecture,
migration, specification and model/orchestration guidance, preserving separate
before-state evidence under `integration/docs/`.


### P6 observation and combined integration result

The typed monitor, native decoders, bounded event-file reader and separate-session
native launcher are implemented and integrated with terminal `status` and
`run --observe`. **22 focused tests** and strict mypy passed. Actual harmless child
process checks show monitor detach/error does not terminate the task. Imported
streams remain unverified; selected/configured values do not become executed-model
claims. Codex exec provides lifecycle but no verified per-agent runtime model;
Claude child role/effort remain unknown without native metadata. Arbitrary-session
attachment and Cursor CLI/editor observation remain unsupported. P6 report, scoped
diff and logs: `/tmp/af-native-delivery-vbe3nr4t/p6/`.

After stable integration the coordinator ran the complete package suite:
**227 tests passed in 14.22s**, strict mypy passed for **46 files**, and the generated
profile schema was current. The final wheel built/installed only in the task venv;
console help and explicit Cursor coverage reporting passed from `/tmp`. Ten changed
documents passed 122 local link/anchor and Markdown checks. The coordinator review
covered interfaces, phase-aware repair, portable project launch and monitor process
ownership; focused implementation review remained with workers.
Evidence: `/tmp/af-native-delivery-vbe3nr4t/integration/`.

P7's actual Claude previews found a false blocker for matching user modelSettings.
A separate before-state and failing regression preceded a scoped adapter fix:
only exact supported effort entries matching all selected roles are accepted;
other overrides remain review-required. **26 Claude tests** and strict typing passed,
followed by actual new/existing Claude setup, unchanged reapply and standalone
launch checks. No global settings changed. Scoped repair evidence lives in
`/tmp/af-native-delivery-vbe3nr4t/p4-matching-effort/`.


### P7 bounded pilot result and outstanding acceptance

Pilot preparation and setup ran in four owned temporary targets under
`/tmp/af-native-delivery-vbe3nr4t/p7/`: empty non-Git projects for each client and
existing projects within disposable nested Git repositories. Actual P5 preview,
apply, unchanged reapply and independently opened project launch checks passed
for both Codex and Claude. Existing custom instructions/settings were preserved.
Only these disposable Git fixtures were initialized; no user/framework Git,
global native configuration or authentication was changed.

Native versions were Codex **0.155.1**, Claude Code **2.1.278**, and Cursor
**2026.01.28-fd13201**. Codex/Claude inspection confirmed existing subscription
sign-in; no API keys or copied credentials were used. Pilot-only pairs reused
existing explicit settings: Codex `gpt-6-astra/high`, Claude `opus[1m]/high`.

The actual observed Claude invocation initialized and exposed its configured
model `claude-opus-5[1m]` and discovered `af-implementer`. It then retried API access
without an assistant response and reached the owned 120-second deadline. The
monitor parsed native metadata without rejected events and correctly left runtime
model/effort unknown. Discovery/configuration is not specialist invocation or
executed-model evidence. No pilot artifact was created and fixture files remained
unchanged during the call. The owned timed-out process was stopped; observation
itself did not claim task cancellation from missing telemetry.

A requested repeat outside the restricted environment was rejected **before
launch** by automatic approval review. Its stated reason was that authorization
for parallel agents did not specifically authorize the external Claude subscription
call, destination/payload and elevated execution with file/tool permissions.
The user was asked explicitly to authorize one same-target, 120-second Claude
pilot with one `af-implementer` and `pilot-result.txt`. The user subsequently
replied “Да, разрешаю этот пилот” to that exact request. One retry is now
authorized; this does not authorize additional external pilots or alter the
settings/authentication constraints. No denied launch or workaround occurred
before this explicit approval.

Codex's restricted invocation failed before any native JSON/model event while
initializing its in-process app-server: `Read-only file system (os error 30)`.
One supported `--ephemeral` alternative, still with temporary `sqlite_home`, failed
at the same point. Each exited 1 after approximately 16.6 seconds. No broader
retry/client-upgrade/config-relocation loop followed; fixture files were unchanged.
Native state requirements in this environment remain unresolved.

Cursor remains unauthenticated with unverified native selector/launch controls;
no Cursor inference or editor pilot was forced. Codex catalog probes timed out;
availability remains unverified. Live different-pair reassignment was not attempted
without an explicitly selected alternative pair. Successful fixture reassignment
is not presented as live execution evidence.

Outstanding P7 criteria include the implementation/check artifact, successful
checkpoint resumption, later ordinary-task activation, and
per-agent model/effort coverage where the native client exposes it. New/existing
setup success does not waive these. Further restricted calls to the same failing
runtime were not useful. P7 is **incomplete**; implementation and bounded checks
are ready for user review. Detailed scripts, before states, captures, results and
preservation evidence are in `p7/report.md` under the evidence directory above.


#### Explicitly approved Claude retry

After the user's specific approval, automatic review permitted exactly one retry
outside the restricted environment. It finished in **94.12 seconds**, native exit
0, with session `0025c4c2-17bb-4895-a6c1-d1cc819dbacf`. There was exactly one native
`Agent` call to `af-implementer`, no model override, one completed correlated child
task, and no nested agents. Native assistant message records reported
`claude-opus-5` for both coordinator and child. This is runtime-reported model
evidence; selected `opus[1m]` and configured `claude-opus-5[1m]` remain separate
labels, and runtime effort is still unknown. The terminal monitor observed both
agents; 19 unsupported tool/user payloads were rejected without losing accepted
assistant model/lifecycle records. Child role remains unknown in the monitor's
current native-event mapping, rather than being guessed from selected files.

The artifact criterion **failed**: the pilot's `dontAsk`/allowed-tool restrictions
rejected `Write` to the exact authorized `pilot-result.txt` target and rejected a
shell redirect. These were pilot invocation controls, not a failed subscription
or a successful write. No file changed, and no exact-content check could run.
The coordinator inspected the missing artifact and stopped with
`P7_CHECKPOINT_WAITING`. Native exit 0 describes session completion, not acceptance
of the requested task. This one invocation establishes handoff, reported model
and stopping behavior only; it does not complete P7 or demonstrate resumption.

No further external call is authorized by that single-retry approval. Original
attempt recipes/captures remain preserved; any corrected write permission must be
reviewed before another paid pilot. This failed artifact is reported explicitly,
not repaired by the framework coordinator creating the file outside the native
role. Detailed final evidence remains in the P7 report directory above.
