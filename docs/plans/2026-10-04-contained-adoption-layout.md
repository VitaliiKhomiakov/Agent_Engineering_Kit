# Adoption, policy settings and agent orchestration — specification and plan

> Use Superpowers with [local adaptations](../../standards/superpowers.md).
> Execute the approved source-library implementation inline under the stage
> checkpoints below. This document does not authorize writes to a consuming project.

**Goal:** Put imported rules and inactive templates under one target directory,
`.agents-framework/`, while preserving discoverable entries, local project work,
portable references and safe updates from earlier imports. Make task completion
markers explicit and expose a small validated set of project policy settings.
Clarify delegated-work ownership and lifecycle, and make model selection/reuse
an explicit integration step using the existing model skills. Bound delegation
overhead through task-specific context and evidence reuse without weakening acceptance.

**Status:** Stage A is complete and accepted by the user on 2026-10-04.
Stage B is complete and accepted by the user's subsequent confirmation, which
authorized **stage C**. Its implementation, verification and inline review are
complete in the current checkout; stage C is **awaiting user review**, not yet
accepted. Consuming-project migration remains pending and unauthorized. Earlier
specification/audit evidence below retains its historical meaning.

**Stage C baseline:** `/tmp/aek-orchestration-C-5q69zlyr/baseline` held pre-write
copies of 16 affected files, including prior local changes. The scope record captured
prior absence of the new capability note; the inventory recorded 238 source-file
hashes. Task-only baselines, fixtures and review material were removed after scoped
review and evidence recording. This historical path is no longer a recovery location.
No Git writes, delegation, target writes, native setup or session changes occurred.

**Stage B baseline:** `/tmp/aek-policy-B-xe8nwsy4/baseline` held pre-write copies of
20 existing affected files, including prior dirty/untracked work and accepted stage-A
contents. The scope record captured prior absence of the two new policy assets;
the inventory recorded 236 original file hashes. After scoped review and evidence
recording, this task's temporary baseline, fixtures, logs, tool environment and caches
were removed. This historical path is no longer a recovery location. No Git writes,
delegation, target writes, plugin edits or session/model changes were performed.

**Stage A baseline:** `/tmp/aek-contained-A-d424ysts/baseline` held pre-write copies
of all 23 initially affected paths, including dirty/untracked contents; its manifest
recorded 236 source-file hashes and initial Git status. No new repository paths were
created. The task-only temporary area was removed after the scoped acceptance review
and evidence recording; this historical path is no longer a recovery location. No source layout change, Git writes, target
writes, plugin edits, delegation or model/session changes are authorized.

**Architecture:** Distinguish the source library, target instruction root, bundle
directory and native client locations. Keep catalog paths bundle-relative and
make the checker accept an explicit bundle directory. Adapt project entries and
installed procedures to actual destinations; preserve source-relative topic links.
Keep progress in the existing canonical task. Store configurable defaults once,
with optional sparse target overrides; Markdown owns their meaning and binding rules.
Reuse the existing routing format and setup/reassignment procedures; integration
owns when to invoke them, while model configuration owns the actual assignments.

**Stack:** Markdown instructions, TOML catalog/templates, Python 3.11+ standard-library
checker and unittest. No installer, runtime framework dependency or release manager.

**Spec:** The design and acceptance sections here are the specification; no second
design document or progress ledger is required under the repository planning policy.

## Scope and authorization

- Source workspace/checkout: `/home/vitalii/Documents/Local_Projects/Agent_Engineering_Kit`.
  This document is the canonical task owner. Preserve all earlier audit changes.
- Observed target: `/home/vitalii/Documents/Local_Projects/angular-login-registration-example-with-ngrx-store`.
  Development is active there. Inspection was read-only; do not run its tests,
  change entries, relocate files or write its task store as part of source work.
- Use the current source checkout, inline; no staging, commits, worktrees,
  delegation, native-client setup or changes to installed plugin caches.
- Source-library layout stays unchanged. Root `AGENTS.md` remains its maintenance
  entry; it is never exported as the consumer's entry.
- Keep required catalog closure and conditional reading. Placement and policy
  settings do not remove profile resources or activate optional agents.
- Preserve target plans/specifications at their canonical locations. The observed
  target's local-only `docs/` policy remains binding; do not reproduce those private
  task contents in the source repository or a tracked replacement.
- Keep temporary baselines through review, record results, then remove only this
  task's temporary files. A durable accepted import base is not disposable scratch.
- The marker workflow is inspired by the user's OpenSpec example, without requiring
  OpenSpec installation or converting existing task stores to a new format.
- Policy settings cannot grant actions, waive required checks, mark incomplete work
  successful or override explicit user instructions and applicable higher-priority rules.

## Consolidated scope and execution order

This inventory links the complete pending scope; execution checkboxes stay with
their tasks below. Previously completed technology-audit work is not reopened.

| Stage | Included work | Specification and task owner |
| --- | --- | --- |
| A | Contain adopted standards/templates; separate project and bundle roots; adapt checker, catalog, entries and skill routes; preserve legacy imports, accepted bases and local changes | [Target layout](#intended-target-layout), [stage A](#implementation-stage-a--contained-adoption-in-the-source-library) |
| B | Explicit completion markers and canonical progress; single-owner policy defaults, sparse overrides and semantic validation; preserve proportional checks/reviews | [Stage B](#implementation-stage-b--progress-markers-and-configurable-policy) and preceding policy specification |
| C | Worker lifecycle and stale results (ORCH-01); serialized plan updates (ORCH-02); supported role restrictions (ORCH-03); client capability evidence (ORCH-04); required model step during integration (ORCH-05); efficient delegation and task context (ORCH-06) | [Orchestration specification](#orchestration-audit--2026-10-04), [model integration specification](#model-selection-during-integration), [context specification](#efficient-delegation-and-task-context), [stage C](#implementation-stage-c--orchestration-and-integration-model-step) |
| Separate target stage | Relocate the active consuming project's import and, if separately selected, observe real-client behavior | [Target stage](#subsequent-target-stage--separately-selected) |

Default proposed order is A, B, C with a review checkpoint after each. C uses A's
path contract and B's marker ownership; it introduces no dependency that blocks A.
Source stages prepare reusable instructions and templates. They do not activate
roles, choose models for this session or change the observed target project.

## Review findings

| Finding | Consequence and required treatment |
| --- | --- |
| `MIGRATION.md` separates source and target but not target root from bundle directory consistently | Add one authoritative layout/path contract and use it throughout prepare, apply, update and recovery |
| Catalog paths are already bundle-relative | Preserve schema version 1 and current IDs/paths; do not prefix every catalog entry |
| Checker `Checker.root`, catalog lookup and default scan assume bundle = project | Separate the two roots without changing existing command meanings |
| Root templates contain installed-root paths in Markdown and code spans | Adapt both representations; ordinary Markdown link checks cannot prove all instruction routes |
| Model skills use `../../../standards/...` while native role text says `standards/...` from instruction root | These work under some old placements but break after nesting; distinguish inactive and installed contexts |
| Integration skill resolves source by walking upward at its source-template location | A copied inactive skill must not mistake the adopted bundle for the full source library |
| A source-only task/helper reference may become deeper when installed | Resolve from the destination and canonical task location, not by blanket prefix replacement |
| Accepted snapshots record target-relative names and adapted contents | Old snapshots remain immutable; migration needs explicit old/new path mapping and current-file reconciliation |
| Portable policy currently allows reachable author-machine source links | Define portable external source references; a path working locally is insufficient after clone |

The preceding target review found all 62 imported/adapted files present and all
accepted-content hashes valid. Only the three root project documents had changed
since import; selected rules/templates retained their accepted contents. Eleven
selected profiles had their catalog dependencies available. Physical-path review
resolved 216 local links and parsed five TOML files. It also found 29 machine-bound
source links in 18 documents. The standard checker reported 27 failures because
it interprets leading `/` as repository-relative URLs, not host filesystem paths.
Do not describe that run as passing, or weaken containment to hide the difference.
This evidence covers inspected artifacts, not live client discovery or adherence.

## Intended target layout

```text
project/
  AGENTS.md
  ARCHITECTURE.md
  PLANS.md
  .agents-framework/
    adoption.md
    accepted/
    policy.toml              # optional project overrides; defaults stay in the bundle
    model-routing.toml       # existing or authorized setup; may be absent if deferred
    standards/
      catalog.toml
      catalog.md
      <selected profiles and their examples>
    templates/              # inactive selected resources
  src/
  <existing canonical task store>
```

`AGENTS.md` remains the project discovery entry. `ARCHITECTURE.md` and `PLANS.md`
remain project-owned documents at their accepted locations. Native `.codex/`,
`.agents/skills/`, `CLAUDE.md` or `.cursor/` files retain their actual client-defined
locations when separately authorized; `.agents-framework/` does not replace them.
The checked [official AGENTS discovery contract](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
supports retaining the root entry. Existing native mappings are not redefined here.

### Path contract

| Path category | Resolution base |
| --- | --- |
| Source procedure, templates and content identity | Identified accessible source checkout |
| Catalog assets, profile sources/resources and template values | Bundle root: target `.agents-framework/` by default; source root in this repository |
| Root AGENTS/PLANS routes and native role instruction paths | Target instruction root, including the actual bundle prefix |
| Ordinary topic-to-topic and inactive template-to-topic Markdown links | Containing file directory |
| Adoption managed paths, rename mappings and accepted snapshot names | Target instruction root, not the bundle root |
| Canonical task artifacts | Existing task-store contract; never implicitly moved |

Record the bundle directory explicitly in adoption metadata. Existing records
without that field must be reconciled with their recorded layout and actual files;
do not infer consent to a move. `.agents-framework/adoption.md` and optional
`model-routing.toml` remain at their existing target-root-relative locations.

Keep catalog schema 1 and paths such as `standards/core.md`: with a nested bundle,
they name `.agents-framework/standards/core.md`. Preserve relative topology of
`standards/` and `templates/`; most internal links then need no change. Change
project/native entry routes, installation bases and explicitly external routes.

### References and templates

- Root-entry templates should show the consolidated default explicitly. For
  source inspection, the checker may map the documented installed prefix
  `.agents-framework/` to the source bundle only in a small declared set of
  root-installed templates (`AGENTS.root.md`, `policy-entry.md`, `PLANS.md`).
  Document this virtual source check. Never apply it to actual target entries,
  arbitrary Markdown or missing links to make them pass.
- Other inactive templates retain their valid source-relative links. Installation
  instructions must adapt routes from actual final locations, including task files,
  nested project entries, installed skills and native role text. Validate installed
  copies separately; inactive-template validity is insufficient.
- Source-template integration skills may use source-relative discovery only after
  verifying both source `MIGRATION.md` and catalog. Bundled or natively installed
  copies resolve the source from the request/adoption record, independently of
  their containing directory. Missing source blocks updates, not ordinary coding.
- Portable optional research/cross-profile references use an actually known source
  URL with content identity where available, or a clearly labelled non-link source
  path resolved through adoption provenance. Do not invent a remote URL, copy all
  history, or leave `/home/...` Markdown links in the portable rule bundle.
  Required local routes stay local and checked. A local source path in provenance
  may describe this machine, but is not a portability guarantee.
- Check path literals inside code spans, TOML developer instructions and native
  import syntax through focused acceptance scenarios. Do not pretend the bounded
  Markdown parser checks these mechanisms.

### Existing imports, concurrency and recovery

Continue supporting the flat layout; ordinary rule updates must not silently move
an existing adoption. A selected layout migration prepares an explicit mapping of
managed old/new paths and changes only those owned files or sections. Unrelated
target `standards/` or `templates/` contents never become framework-owned.

Compare B (last accepted adapted content), C (current target) and N (new candidate).
Keep the old accepted snapshot and its original names; after successful verification,
record the new mapping and accepted contents separately. A rename is not evidence
that C still equals B. Preview collisions, modified destinations, removed files,
and changes between preparation and application; resolve overlapping edits before
dependent writes. Include root entries and provenance in baseline protection.

Prefer a placement-only migration before a separately reviewed source-content
update, so current project adaptations and later library fixes remain distinguishable.
Switch active routes only when their new resources exist. Retire only authorized
owned old paths after checking current contents; never recursively delete shared
directories. On interruption, retain the old accepted base and record actual
partial outcomes. Recovery must preserve edits made after this operation began.

## Checker interface

Keep current commands and their meanings. Add an explicit option:

```sh
python3 tools/check_instruction_artifacts.py
python3 tools/check_instruction_artifacts.py --root /tmp/flat-target --profile angular
python3 tools/check_instruction_artifacts.py --root /tmp/nested-target --bundle-dir .agents-framework --profile angular --profile ngrx
python3 tools/check_instruction_artifacts.py --root /tmp/nested-target --bundle-dir .agents-framework --profile angular AGENTS.md .agents-framework/adoption.md
```

- `--root` remains the source/target instruction root. `--bundle-dir` defaults to
  `.` for backward compatibility and resolves within `--root`; a non-default value
  requires explicit `--profile` selection. Do not guess between two present layouts.
- Catalog lookup and catalog paths use the bundle root. Explicit input paths,
  repository-root Markdown URLs, diagnostics and root-entry scanning use `--root`.
  Validate catalog resources remain inside the bundle, and document links remain
  inside the project. Reject traversal/symlink escapes; no external filesystem mode.
- Selected mode scans closure resources, present client templates and root Markdown,
  plus the existing adoption record. Explicit paths replace body selection while
  keeping the selected catalog check. Native installed paths outside that scan must
  be selected explicitly for applicable syntax checks and reviewed for path literals.
- Source template virtual-link mapping applies only in source mode, never to an
  installed bundle, and only to the three declared root-installed templates above.
- No network access, writes, Markdown adoption-record parser, profile auto-detection
  or universal native-config validator is added. Preserve Python 3.11+, stdlib only.

## Task progress contract

For substantive Markdown plans, give independent actionable items stable identifiers
within the canonical task, with unchecked/completed markers. Reuse existing IDs;
do not renumber completed work merely when adding another item. For example:

```markdown
- [x] A1. Define the selected layout and compatibility contract.
- [ ] A2. Implement project/bundle root separation.
- [ ] A3. Verify nested and legacy bundles.

Current item: A2 — in progress.
Stage status: in progress.
```

- Update the item's state when its independently defined outcome is achieved,
  before proceeding to another item or handing off. Do not defer all markers to
  the end of a large phase, or rewrite the plan after every file edit/tool call.
- `[x]` means the item's own acceptance conditions are met. If implementation and
  verification are separate items, code completion can close the former while the
  latter remains open. If testing is part of that item's acceptance, keep it open
  until the required evidence is available. Never treat "started" as "completed".
- Keep in-progress or blocked items unchecked; record the current item, status and
  concise reason separately. At checkpoints, align item markers, stage status,
  valid evidence and remaining work. Stage completion does not complete the task.
- If later evidence invalidates completion, reopen the affected item and state why;
  retain still-valid results for unrelated work. Mark removed/superseded items as
  such with a reason; do not count cancellation as completed implementation.
- A native store such as OpenSpec retains its supported completion markers/status
  operations and canonical location. Do not mirror it in a second editable checklist
  or invent a native CLI command. A simple task still needs no persistent plan.
- Item completion is not a new permission checkpoint or automatic test/review
  trigger. The phase/check selection rules remain applicable. Before resumption,
  reconcile the recorded state with relevant current evidence instead of redoing
  already completed items solely because the session changed.

This is a planning requirement, not a TOML switch that disables truthful progress.
`templates/PLANS.md` owns it; task templates show the format and entries route there.

## Small policy configuration

### Ownership and loading

Add `standards/policy-defaults.toml` as the single owner of configurable default
values and `standards/policy-configuration.md` as the schema/loading contract.
Both are shared catalog assets, not additional technology profiles. Catalog schema
version stays 1. The policy file has its own independent `schema_version = 1`.

The target may supply sparse overrides at `.agents-framework/policy.toml`; do not
create an identical active copy merely on import. This override remains relative
to the target instruction root, including when the selected bundle is flat.
Source maintenance uses the source defaults without installing target settings.

Resolve values as bundled defaults plus explicitly present valid override fields.
Missing override fields inherit; omission never means disabled or zero. With no
override file, use bundled defaults without a questionnaire. A genuinely older
adoption without these assets continues under its recorded Markdown policy until
an authorized update; do not silently introduce settings or rewrite its catalog.
An override without its default/schema owner is an unsupported partial setup.

Read settings relevant to the current task and reuse them while valid. Do not load
all technology topics to interpret a small policy file. Changed relevant settings
invalidate only affected decisions/evidence, not all earlier work. No background
monitor, automatic reload, template generator or runtime enforcement is implied.

Explicit task instructions and mandatory project/client requirements take
precedence over configurable preferences. The Markdown owners retain conditions,
exceptions, required evidence and scope. Replace their competing numeric defaults
with references to the named fields; do not maintain independent numeric values
in root entries, role text and prose examples. `model-routing.toml` continues to own
models, efforts, roles and concurrency; `policy.toml` duplicates none of those.

### Initial schema and defaults

The complete default data, with no arbitrary run-count limits, is:

```toml
schema_version = 1

[verification]
timing = "phase_end"
diagnostic_reset_after_stalled_attempts = 2

[review]
independent = "risk_based"

[size]
function_review_lines = 50
class_review_lines = 400
file_review_lines = 500
growth_review_from_lines = 600
documented_review_above_lines = 700
react_component_review_lines = 250

[instructions]
root_guideline_lines = [40, 70]
local_guideline_lines = [10, 25]
```

After implementation, the canonical default file owns these numbers; this block
remains a dated design record and must not become a second operational source.

| Field/group | Meaning and validation |
| --- | --- |
| `schema_version` | Required integer 1 in defaults and overrides; independent of catalog/model schemas |
| `verification.timing` | `phase_end` (default) or `task_end`, selecting batching at the logical phase or planned task boundary, never every file/edit; retain still-valid earlier results |
| `diagnostic_reset_after_stalled_attempts` | Positive integer; consecutive unsuccessful attempts on the same problem without new evidence trigger a diagnostic reset, not abandonment; legitimate TDD red steps do not count |
| `review.independent` | `risk_based` (default) or `on_request`; coordinator review remains required, explicit project review requirements remain binding, and a preference cannot authorize delegation or an extra duplicate pass |
| `size.*` | Positive integers; review thresholds, not automatic splitting quotas; the growth threshold cannot exceed the documented-review threshold |
| `instructions.*` | Exactly two positive integers in ascending order, describing soft substantive-line ranges, not truncation limits |

Reject Boolean values where integers are required, unknown keys, unsupported
schema versions, invalid enum values and invalid ranges. Defaults must be complete;
overrides may omit recognized fields/tables but must declare their schema. Report
the file and field; preserve invalid/unknown contents without automatic repair.
An invalid override must not be silently treated as missing and replaced by defaults.
Only decisions dependent on those unresolved settings are affected; unrelated work
can continue under its existing authorization and known binding rules.

Do not introduce `max_tests`, `max_reviews`, `max_fix_rounds`, token/time budgets or
test-count quotas. The normal procedure remains one combined review and one batch
of necessary checks at the selected boundary, followed by focused checks after
relevant fixes. A new configured boundary does not invalidate an already valid
result. Mandatory gates and unresolved in-scope defects survive every preference.
The independent-review setting selects the usual reviewer policy; it does not
force creating an agent when capabilities or authorization do not permit it.

### Integration and acceptance

The existing checker should validate packaged defaults and a present override,
including the merged result, in source/selected-bundle mode. This policy check runs
alongside catalog validation even when explicit body paths narrow Markdown checks.
Do not require new policy assets in old catalogs which never declared them. For an
older catalog with no defaults and no override, preserve legacy artifact behavior.
Report unsupported partial policy setup when an override exists without defaults.

Validate syntax and schema/data consistency only; the checker cannot prove the
agent actually follows a cadence or honors completion markers. Native-model/client
limits are separate. Instructions must explicitly route the agent to these settings
and preserve the local Superpowers adaptations so conflicting stock repetitions
do not return through another skill path.

## Implementation stage A — contained adoption in the source library

Run the following tasks as one coherent source change; report its checked result
before any real-target migration. Capture affected originals before each write.
The policy/progress work below is a subsequent coherent stage, not permission to
skip this stage's review checkpoint. Do not start either during specification review.

### 1. Checker and behavior coverage

Files: `tools/check_instruction_artifacts.py`, `tests/test_instruction_artifacts.py`,
`docs/maintenance/verification.md`.

- [x] Introduce explicit project/bundle roots, option validation and scoped source
  template mapping; preserve existing source/flat behavior and diagnostics.
- [x] Add CLI regressions before implementation for nested valid bundles and
  selected dependencies; missing nested resource/fragment; a broken root AGENTS
  route; scoped paths; invalid/outside bundle directories and symlink escapes;
  both layouts present with explicit selection; source-template mapping that cannot
  hide an invalid actual target route. Retain existing flat/source tests.
- [x] Update invocation, link bases and limits in the maintenance owner. Keep
  the full-source command usable without creating a fake adopted directory here.

Checker evidence: 31 CLI unittests passed after the intended red run (the missing
option/source mapping caused 11 failing assertions). Strict mypy 2.1.0 with the
documented flags passed for both Python files, targeting Python 3.11 on Python
3.12.3. Default source artifacts passed (191 files, zero errors). Catalog schema,
IDs and source topology are unchanged. Source mode is explicitly no profiles with
bundle `.`; selected flat and nested targets receive no virtual template mapping.

### 2. Adoption contract and installation routes

Primary files: `MIGRATION.md`, `standards/catalog.md`,
`templates/framework/adoption-record.md`, `README.md`, `ARCHITECTURE.md`.

Route/template files: `templates/AGENTS.root.md`, `templates/policy-entry.md`,
`templates/PLANS.md`, `templates/task.md`, `templates/AGENTS.project.md`,
`templates/project-architecture.md`, `templates/workspace-architecture.md`,
`templates/skills/af-integrate-project/SKILL.md`,
`templates/skills/af-model-setup/SKILL.md`,
`templates/skills/af-model-reassign/SKILL.md`,
`templates/codex/README.md`, `templates/codex/agents/af-implementer.toml`,
`templates/codex/agents/af-reviewer.toml`, `standards/model-configuration.md`.
Change only affected contracts; a reviewed unaffected file need not be rewritten.

- [x] Make MIGRATION the layout/relocation owner; catalog and entries link to the
  appropriate local owner or explain the necessary bundle semantics briefly.
- [x] Add adoption bundle location, managed old/new path mapping and accepted-base
  preservation, without treating example metadata as an installed runtime schema.
- [x] Adapt root templates and installation guidance for source, inactive bundle
  and native installed contexts. Preserve native settings paths, planning stores,
  model assignments, conditional reading and source-maintenance instructions.
- [x] Review unchanged `templates/framework/model-routing.toml`, native config,
  Claude bridge and Cursor route for correct declared bases; do not change model
  IDs, settings schemas or activation solely for directory consolidation.
- [x] Use the applicable writing-skills guidance for actual skill edits, with
  local adaptations; validate their frontmatter, references and narrow triggers.

### 3. Verify the complete procedure

- [x] Prepare disposable source-derived selected bundles in both flat and nested
  layouts, adapting only optional source links and intended installation paths.
  Confirm root and native-role/skill routes, catalog closure, TOML and Markdown.
- [x] Review relocation scenarios: existing destination collision; unrelated files
  sharing old directories; locally edited managed file; edit after preview; missing
  prior base; interrupted route switch; repeated unchanged invocation; independent
  child-project opening; an unavailable source with locally usable ordinary rules.
  These are instruction-procedure acceptance checks, not claims of an automated installer.
- [x] Run focused unittest, strict mypy on changed Python, default source artifact
  check, scoped changed-document checks and `git diff --check`. Inspect new files
  and actual diffs against the captured baseline; do not run unrelated app suites.
- [x] Record exact results and evidence limits here, remove temporary fixtures/tools,
  and report the source-library stage for review. Do not claim a native-client pilot.

### Stage A implementation and acceptance evidence — 2026-10-04

User review accepted on 2026-10-04. This closes stage A's human checkpoint; it
does not authorize automatic progression, Git writes or a consuming-project migration.

Implemented in 20 existing files against the captured pre-stage contents, including
four files already untracked before this stage. No new repository file was created.
The other 216 inventory files remain byte-identical, including earlier technology
audit work, catalog TOML, source maintenance AGENTS, native config/bridge/route
examples and model-routing values. Existing role model/effort values are unchanged.
Reviewed `AGENTS.project.md`, project/workspace architecture templates, the routing
example, Codex config, Claude bridge and Cursor route without unnecessary rewrites.

MIGRATION owns placement, installation bases and relocation. Root-entry templates
show the contained default; ordinary topic and inactive skill links remain relative
to their containing files. Installed copies are rebased independently. Catalog
schema 1, IDs, dependencies and paths remain unchanged. Old accepted snapshots
retain their bytes/names; new mappings and accepted contents are separate records.
No implementation of stages B/C, model setup or real-target migration was performed.

Verification commands and results for the completed relevant state:

- `python3 -B -m unittest discover -s tests -p 'test_instruction_artifacts.py'`:
  **33 passed** on Python 3.12.3. The original 22 tests remain. The initial 31-test
  run established the missing option/mapping failures before implementation; review
  added a non-required transitive dependency and a symlink-loop regression. The
  latter reproduced three traceback failures before correction; final checks now
  report argument/artifact errors without traceback. The Python 3.11
  [Path.resolve contract](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path.resolve)
  was checked on 2026-10-04 for loop exceptions. Python 3.11 execution itself was
  unavailable; the static compatibility target remains 3.11.
- Temporary venv `python -B -m mypy --strict --disallow-any-explicit
  --disallow-any-unimported --python-version 3.11 --cache-dir <scratch>/mypy-cache
  tools/check_instruction_artifacts.py tests/test_instruction_artifacts.py`:
  **no issues in 2 files**, mypy 2.1.0. The system lacked pip/ensurepip/mypy;
  approved network bootstrap installed only into this task's isolated venv, with
  no application-stack or repository dependencies. Resolved tool packages: pip
  26.2.1, mypy 2.1.0, ast-serialize 0.12.1, librt 0.16.0, mypy-extensions 1.1.0,
  pathspec 1.1.1 and typing-extensions 4.16.0.
- `python3 -B tools/check_instruction_artifacts.py`: **191 artifacts, zero errors**.
  Explicit changed-document/TOML selection: **18 artifacts, zero errors** before
  this evidence-only plan update; the final plan is checked separately.
- Disposable source-derived flat and contained bundles selected `angular` and
  `ngrx`, closing over **11 profiles** and **61 imported resources/templates**.
  `--root <fixture> [--bundle-dir .agents-framework] --profile angular --profile ngrx`:
  **65 artifacts per layout, zero errors**. Explicit native skill/role, task,
  Claude and Cursor paths: **8 artifacts per layout, zero errors**. Missing
  installed model-contract trials reported both missing resources and links.
  Reused these success-path results after the isolated exception-handling fix.
- Optional omissions were reviewed: **23 source-route identities**, confined to
  research/history and inapplicable NestJS/React routes. They became labelled
  non-link source paths through provenance; required local routes were retained.
  Root AGENTS/PLANS/policy code-span paths and TOML developer-instruction paths
  were resolved separately. That inspection caught an inapplicable Unreal literal
  left in the disposable policy copy; adapting it to the fixture's selected stack
  resolved the issue, with no checker exemption. Corrected policy checks passed.
- The installed `skill-creator/scripts/quick_validate.py` validator passed all
  **3 edited source skills** and **6 installed flat/nested fixture copies**.
  Inline trigger review retained explicit integration, authorized model setup and
  requested reassignment triggers; missing files/ordinary coding remain excluded.
  Source and copied integration-entry locations were inspected: copied templates
  lack the verified full-source MIGRATION/catalog pair and must use provenance.
  Cursor fixture frontmatter parsed with available PyYAML; Claude `@AGENTS.md`
  resolved at its installed root. These are syntax/route checks, not client pilots.
- Independently opened child fixture, with its own local bundle and task route:
  **65 artifacts, zero errors**, including after its source provenance was changed
  to an unavailable location. Ordinary local policy remained usable; integration
  would report the source access obstacle before dependent updates.

Inline relocation walkthrough used disposable files, not a new installer or an
agent-behavior benchmark. The instruction decisions were checked against these
concrete states and preservation assertions:

| Scenario | Observed decision and result |
| --- | --- |
| Destination already contains project data | Dependent copy blocked; both endpoints preserved and no ownership inferred, including identical unowned destinations under the written contract |
| Unrelated file shares old `standards/` | Remained byte-identical; no recursive shared-directory retirement |
| Managed C differs from accepted B | Placement candidate retained C and its local contract; no assumption that rename means C = B |
| Old file changes after preview | Stale preview detected; current content reconciled before the candidate write, without overwriting the original baseline |
| Previous B contents unavailable | No fabricated base or claimed three-way merge; dependent relocation requires explicit reconciliation |
| Interrupted route switch | AGENTS switched while PLANS stayed flat; both resource sets and the old accepted snapshot remained available; acceptance was not advanced |
| New edit after interrupted write | Recovery retained the newer AGENTS edit and removed only an unchanged operation-created file; the old source and adoption record remained intact |
| Repeated verified unchanged operation | No-op decision retained all fixture bytes and mtimes; matching partial work still requires its pending checks |
| Child opened independently / unavailable source | Local entry, selected closure and canonical task routes remained reachable; source-dependent integration and ordinary coding were distinguished |

Scoped inline review covered actual pre-stage diffs, new/untracked status, path
bases, required routes, catalog containment and the above recovery cases. It found
and resolved the symlink-loop diagnostic defect and fixture-only route omission.
The final `git diff --check`, per-file baseline whitespace checks and separate
whole-file checks of the four modified pre-existing untracked files passed. No
repository files were added or removed; 20 changed and 216 unchanged source-file
hashes account for the original inventory. Temporary fixtures, baseline copies,
review diff, bootstrap, venv and caches under this task's exact scratch directory
were removed after recording these results. Permanent accepted snapshots were
not accessed or removed. No material stage-A finding remains. The checker has no installer, adoption-record
parser, network validation or universal native-settings validator. No consuming
project files/tests, installed plugins, client sessions, role activation or paid
model pilots were touched. File evidence does not establish native discovery or
instruction adherence. Stages B/C and the separate target stage remain pending.

## Implementation stage B — progress markers and configurable policy

Depends on the accepted root/bundle contract from stage A. Preserve its results;
do not rerun unrelated relocation checks unless this stage changes their inputs.

Current item: none — all stage-B acceptance items are complete.
Stage status: accepted by the user; stage-C progression authorized.

### 4. Explicit task completion markers

Modify `templates/PLANS.md`, `templates/task.md`, and affected routes in
`standards/delivery-workflow.md` and `standards/superpowers.md` only where needed.

- [x] B4.1. Establish stable item IDs, immediate completion-state updates at meaningful
  item boundaries, unchecked in-progress/blocked state and evidence-based reopening.
- [x] B4.2. Make the task template demonstrate `[ ]` to `[x]`, current item and stage
  status; preserve native task stores and avoid duplicate progress owners.
- [x] B4.3. Review scenarios: an item completed while the next is underway; code done
  with tests outstanding; blocked item; revoked evidence; cancelled scope; a new
  session; an existing native checklist. Confirm markers do not trigger extra
  tests, reviews, user approvals or a mandatory plan for a trivial edit.

B4 evidence: the scoped artifact check passed for the four edited planning/routes
files (zero errors). Inline scenario review confirmed that completed S1.1 can stay
checked while S1.2 is underway; an item whose criteria include outstanding tests
stays unchecked; blocked work stays unchecked with a reason; revoked evidence
reopens only affected items; cancelled scope is labelled, not counted as completed.
A resumed session reuses applicable evidence, and an existing native checklist
retains its own operations without a duplicate store. Markers add no check/review
cycle, approval requirement or persistent plan for a trivial edit.

### 5. Defaults, overrides and schema validation

Create `standards/policy-defaults.toml`, `standards/policy-configuration.md`.
Modify `standards/catalog.toml`, `tools/check_instruction_artifacts.py`,
`tests/test_instruction_artifacts.py`, `docs/maintenance/verification.md`,
`templates/AGENTS.root.md`, `templates/policy-entry.md`,
`templates/framework/adoption-record.md` and `MIGRATION.md` for loading/ownership.
Update `standards/verification.md`, `standards/core.md`,
`standards/react/components-boundaries.md`, `ARCHITECTURE.md`, `README.md` and
affected native role instructions to route to the single settings owner.

- [x] B5.1. Add the complete defaults and optional sparse override contract; register
  the default/schema assets, document conditional reads and clarify setting changes
  are reviewed project policy changes, not automatic effects of copying templates.
- [x] B5.2. Add failing meaningful tests, then implement semantic validation: defaults
  only; valid partial overrides; unknown field/schema; invalid enum; zero/negative
  or Boolean numeric threshold; malformed/inverted range; inconsistent growth
  thresholds; missing defaults with an override; legacy absence of both files;
  explicit Markdown path selection still checking policy. Cover flat and nested roots.
- [x] B5.3. Keep external input typed/validated, strict Python and standard library only.
  Syntax-only `tomllib` success must not stand in for schema or merged-value checks.
- [x] B5.4. Replace duplicate operational numeric defaults with routes/field references.
  Preserve threshold semantics, exceptions, required CI gates and completion criteria.
  Keep concurrency/model settings in their existing owner; do not parameterize
  dependency versions or runtime facts found in technology documentation.
- [x] B5.5. Check instruction scenarios: absent overrides require no onboarding; one
  threshold override changes only that decision; a changed value invalidates only
  relevant evidence; `task_end` does not rerun a valid phase result; a requested
  independent review still respects authorization/capabilities; a failure cannot
  be waived because a check/review count or diagnostic threshold was reached.
- [x] B5.6. Run the focused tests and strict analyzer for changed Python, source and
  affected bundle/document artifact checks, then review the scoped diff. Record
  results and limits, mark actual completed items and remove temporary artifacts.

B5 implementation checkpoint: defaults and schema/loading owner are added as shared
assets without changing catalog schema or profile IDs. Numeric defaults now have
one operational owner; prose and native role templates route to the named fields.
The focused policy suite passed all seven methods after a red run with 50 failing
assertions; it covers source/flat/nested and a custom bundle, explicit-path checks,
legacy/partial setups, invalid fields and merged constraints. The initial fixture
mistook an override-created directory for an assembled nested bundle; corrected
that test setup before interpreting the red run. Subsequent verification passed:
40 CLI tests, strict mypy 2.1.0 on both Python files targeting Python 3.11, the
193-artifact source check and 20 changed-document/TOML checks.

B5.5 scenario review: absent overrides use bundled defaults without onboarding;
a single threshold override changes that field while omitted fields inherit.
The configuration contract invalidates only affected decisions/evidence after a
setting change. `task_end` retains valid phase results and required intermediate
gates, including acceptance before a human checkpoint. Requested/required
independent review still needs actual permissions and capabilities; unavailable
review is reported, not claimed or silently replaced. Neither rejected quotas nor
the diagnostic-reset threshold waive a failure, and ordinary TDD red steps do not
count as stalled repairs. These are instruction consistency findings, not observed
agent behavior in a consuming client.

### Stage B verification and scoped review — 2026-10-04

- `python3 -B -m unittest discover -s tests -p 'test_instruction_artifacts.py'`:
  40 tests passed on Python 3.12.3, including the retained stage-A regressions.
- Temporary venv `python -B -m mypy --strict --disallow-any-explicit
  --disallow-any-unimported --python-version 3.11 --cache-dir <task-scratch>/mypy-cache
  tools/check_instruction_artifacts.py tests/test_instruction_artifacts.py`:
  success for both files with mypy 2.1.0. No runtime dependency was added.
- `python3 -B tools/check_instruction_artifacts.py`: 193 artifacts, zero errors.
  Explicit selection of the 20 changed Markdown/TOML files: zero errors.
- Temporary flat and contained bundles used the actual source catalog closure
  for `angular` and `ngrx`: 11 profiles and 62 imported resources/templates.
  Each default scan passed for 66 artifacts; explicit native-role/deep-task scans
  passed for three. Root and native literal policy routes were resolved separately.
  Sparse single-threshold overrides passed the scoped entry check and preserved
  other resolved values; `task_end`/`on_request` overrides passed the two-file
  entry/override check. All runs had zero errors. The 24 conditional omitted-route
  identities were adapted to labelled source references under the catalog contract,
  including the unselected React route; required local routes were retained.
- The [Python 3.11 tomllib contract](https://docs.python.org/3.11/library/tomllib.html)
  was checked for parse results and errors. Execution used Python 3.12.3; Python
  3.11 compatibility has static-target evidence, not a run on that interpreter.
- Accountable inline review compared all 22 paths with their pre-stage contents:
  20 existing files and two new policy assets. All 216 other inventoried files
  retained their hashes. Catalog schema, profile IDs/dependencies and native
  role names/models/efforts are unchanged. `git diff --check` and whole-file
  whitespace inspection of all 22 paths, including new/untracked files, passed.
  No blocking acceptance finding remained.
- Cohesion review retained the shared CLI test class above the class-review
  threshold: it owns one checker regression suite using the same temporary-root
  fixtures and subprocess assertions. A policy-only class would duplicate or
  introduce shared fixture machinery without separating production behavior.
  New production helpers keep field validation separate from path/loading checks;
  the pre-existing catalog procedure was not expanded into unrelated cleanup.

Evidence reuse: unchanged Python results and earlier stage-A relocation evidence
remain valid; the final plan/task wording passed a scoped artifact check (two
artifacts, zero errors). Task-only temporary material was removed after review.
No live client, native task-store operation or agent-behavior pilot was performed.
Settings validation does not demonstrate actual cadence, honest markers or client
adherence. No consuming-project files/tests, accepted snapshots, installed plugins,
session/model settings or Git index/refs were changed. Stage C remains unauthorized.

Stage B completion requires both honest progress markers and a validated, reachable
settings contract. File presence alone does not establish agent adherence; that
remains an explicitly scoped consuming-client observation.

## Subsequent target stage — separately selected

After the active target's current development stage reaches a suitable checkpoint,
prepare its relocation using a fresh target baseline and canonical target task.
Preserve its three locally edited root documents, ignored task store and current
source selection. Do not reuse the earlier read-only snapshot as write permission
or assume it still represents current files. Present the concrete path changes,
then apply within the authorization available at that time. A real-client pilot
and any source-rule upgrade are separate scopes, not consequences of moving files.

## Review-stage evidence

Reviewed the existing integration skill, prepare/apply/update/recovery procedure,
catalog semantics, root/task/native templates and checker assumptions. The inventory
found path references in Markdown, code spans, skill procedures and TOML role text;
these were classified by resolution base rather than scheduled for global replacement.
The accepted layout from the conversation is retained. The explicit checker option,
legacy compatibility, source-only template mapping and immutable old snapshot rules
above make the implementation reviewable without editing the active target.

Self-review covered catalog/source/template base consistency, native discovery,
local changes and partial recovery, external-link portability, unchanged source
layout and canonical task ownership. The named tests/scenarios cover those risks.
Only this plan is created in the review stage; production instructions/tools and
the consuming project remain unchanged. Review scratch is removed after verification.

## Requirements extension — 2026-10-04

The user requested adding completion markers inspired by OpenSpec and following
the recommended restrained TOML approach to both specification and plan. Both
remain in this canonical document; the deferred adoption agreement is preserved.

- [x] Inspect current progress, check/review cadence and numerical policy owners.
- [x] Define explicit completed-item markers without another task store.
- [x] Specify single-owner defaults, sparse overrides, validation and evidence limits.
- [x] Add implementation ownership, dependencies and acceptance scenarios for the extension.
- [ ] Review/agree the combined implementation scope and stage progression.
- [ ] Complete source stage A with its required evidence.
- [ ] Complete source stage B with its required evidence.

Current item: implementation agreement — deferred by the user while requirements
are refined. Current stage: specification/plan update only. No consuming-project
relocation, new policy file, checker implementation or native setup has been performed.

Specification review checked the extension against existing policy ownership,
legacy imports, task-store preservation and mandatory evidence requirements.
The scoped artifact check and `git diff --check` passed; the proposed TOML block
parsed successfully. This is syntax/design evidence, not an implemented policy
validator or a runtime check. All other pre-existing source files stayed unchanged.

## Orchestration audit — 2026-10-04

Scope: planning/design, implementation, checks and review in the instruction
library. Compared orchestration, model configuration, delivery/verification,
planning and native templates with current official documentation and installed
Superpowers 6.4.2. This is source review, not a live multi-client pilot. Existing
dated research remains historical evidence. Implementation agreement is still deferred.

### Assessment and sources

The role allocation is coherent: the coordinator can plan and review routine work;
architect/planner roles are conditional; the implementer owns coding and necessary
checks; an independent reviewer assesses a stable scope when warranted. Separate
agents for every activity are unnecessary. Bounded handoffs, baseline preservation,
independent parallel ownership and integration checks are already covered by
[orchestration](../../standards/orchestration.md) and
[verification](../../standards/verification.md).

- [Official OpenAI subagent guidance](https://learn.chatgpt.com/docs/agent-configuration/subagents)
  supports focused delegation and cautions about concurrent writes. Its reviewer
  example uses a read-only sandbox. The
  [configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference)
  confirms the retained enablement, worker default and concurrency keys; the
  spawned-thread ceiling excludes the main thread.
- [Claude Code subagents](https://code.claude.com/docs/en/sub-agents)
  distinguishes fresh agents, inherited-context forks and resumed agents. Built-in
  Explore/Plan omit ordinary project instructions; explicit policy handoff remains
  necessary. Nested spawning and concurrency have version/mode-specific controls.
  Parent permission modes can override a child's `permissionMode`, so setting
  `plan` alone is not universal evidence of enforced read-only access.
- [Cursor subagents](https://cursor.com/docs/subagents)
  documents shared-checkout writes, bounded nesting, a `readonly` option and
  possible model substitution under plan/admin restrictions. Existing framework
  research already records substitution; this audit does not rediscover it as a bug.
- [Upstream Superpowers SDD](https://github.com/obra/superpowers/blob/main/skills/subagent-driven-development/SKILL.md)
  describes fresh implementers, task reviews and final review. The installed skill
  also prescribes repair rounds and escalation. Our
  [local adaptations](../../standards/superpowers.md) intentionally replace those
  defaults with authorized routing, proportionate review and existing checkpoints.
  This is a declared local policy, not a vendor requirement or a missing review.

No blocking contradiction was found in the reviewed role model. The following
are targeted clarifications and optional hardening, not evidence that installed
agents currently violate the rules.

### Orchestration specification

| ID | Gap or opportunity | Proposed acceptance and authoritative owner |
| --- | --- | --- |
| ORCH-01 | No explicit end-to-end lifecycle for background workers and late results | In `standards/orchestration.md`, distinguish fresh dispatch from continuation of the same bounded assignment. Before ownership transfer, dependent review, cleanup or a stage checkpoint, reconcile relevant workers and their outstanding tools; wait for completion or confirm an authorized stop. Treat timeout/partial output as incomplete. Check late results against the current task/baseline before accepting them. Do not automatically cancel unrelated work or create a fresh worker for each correction. |
| ORCH-02 | A canonical progress owner is named, but write serialization is implicit | Clarify in `templates/PLANS.md` that the coordinator normally updates the common checklist from worker evidence. Workers report completion; concurrent workers do not edit the shared plan. A delegated planner can own its assigned draft, with an explicit handback before another writer takes over. Route to this rule from orchestration instead of copying it. |
| ORCH-03 | Native restrictions differ; reviewer no-edit text is expressly behavioral | In `standards/model-configuration.md` and affected inactive role templates, distinguish behavioral scope from verified native tool/filesystem restrictions. When selected and supported, restrict reviewer/explorer access without treating a read-only role as an isolated execution environment. Preserve necessary evidence access; checks needing writes go through an authorized executor. Keep planner draft-writing rights explicit. Unsupported controls stay reported limitations. |
| ORCH-04 | Client limits and context behavior are scattered across general rules and dated evidence | Add a compact dated capability comparison under `docs/research/`, referenced conditionally from model configuration. Cover fresh/fork/resume, nested spawning, concurrent running work versus retained thread slots, role permissions, model overrides and instruction loading. Record documented capability separately from the installed version and tested behavior. Do not hardcode vendor limits into shared policy or claim the routing TOML enforces them. |
| ORCH-05 | Integration currently makes model setup conditional and can omit an explicit selection decision | Make model selection/reuse a required integration step using existing `af-model-setup` and `af-model-reassign`; specify preparation, existing assignments, deferral, updates and partial outcomes below. |
| ORCH-06 | Focused handoffs and total-cost accounting already exist, but the context assembly and delegation-overhead decisions are underspecified | Extend the existing delegation/cost sections with the task-context contract below; reuse verification and lifecycle owners. Do not add a mandatory role pipeline, prompt generator, separate ledger or automatic cost benchmark. |

These items do not require a new agent manager, monitoring service, workflow
engine, additional default reviewers or another configuration format. Keep model
pairs, allowed edges and the chosen concurrency ceiling in `model-routing.toml`;
the proposed policy TOML remains limited to the already specified settings.

### Model selection during integration

The integration workflow must account for models explicitly. A required step
means a checked/reused selection, authorized setup, explicit user deferral or a
reported unresolved state; it does not require creating specialist agents or
silently assigning template defaults. Ordinary coding remains free of onboarding.

| Situation | Required behavior |
| --- | --- |
| Full initial integration | Route through `af-model-setup` at the model-selection step. Resolve the selected client and existing routing/native state before deciding whether changes are needed. |
| Existing consistent assignments | Reuse choices and return without writes or repeated questions. A consistent single-agent selection satisfies the step. |
| Missing or incomplete selection | Reuse supplied choices; ask once for material missing client, single/delegated mode and enabled model/effort pairs, plus edges/ceiling for delegation. Await necessary answers before dependent writes or spawns. |
| User defers model setup | Record deferral in the canonical adoption task and summarize it in the adoption outcome. Rules may be integrated and ordinary inline work may continue; do not invent a configured record or enable delegation. Preserve any existing file and known choices. |
| Preparation only | Read the skill/contract to prepare the exact proposal and unresolved choices. Do not write target routing/native files, install skills, launch a model pilot or switch the running session. |
| Ordinary rules update | Check/reuse the existing selection relevant to the update; no repeated setup questionnaire or assignment changes. Preserve a prior explicit deferral. A newly requested setup uses `af-model-setup`. |
| Requested reassignment or client change | Route through `af-model-reassign`; preserve unrelated choices and reconcile the selected client's supported settings. |
| Unavailable skill | Follow the accessible authoritative model-configuration procedure and disclose that fallback; do not claim a skill was invoked. If that procedure is also inaccessible, report the model step unresolved and continue only independent authorized adoption work. |
| Unsupported pair, unknown schema, conflicting settings or partial write | Preserve contents/known choices and follow existing conflict/recovery rules. Report the affected setup incomplete; never silently substitute, label it deferred without a user decision or claim successful activation. |

The full-integration entry invokes the existing setup procedure with the adoption
intent, selected mode, prior choices, actual source/target roots and write scope.
Authorization already granted for setup/application is reused; merely invoking
the skill or importing rules does not grant unrelated native/global writes.
Compare concrete intended changes before applying within existing authorization.

`MIGRATION.md` owns the integration trigger and outcome; the skill entry routes
there. `standards/model-configuration.md` owns setup, reuse, reassignment and
recovery; the model skills remain thin entries. Keep model values solely in the
routing/native owners. The adoption record links to those owners and summarizes
checked/reused, configured, deferred or unresolved outcomes without a second
model table, checklist or new routing status. Preserve `unconfigured`/`configured`
semantics and separate saved agreement from observed runtime activation.

### Efficient delegation and task context

Reviewed official sources on 2026-10-04 in response to the user's token-cost
concern. [OpenAI subagent guidance](https://learn.chatgpt.com/docs/agent-configuration/subagents)
warns that workers perform additional model/tool work; reduced coordinator
context does not prove lower total usage.
[Cursor](https://cursor.com/docs/subagents) describes context startup overhead
and advises considering whether a simple task is better handled by the main agent.
[Claude Code cost guidance](https://code.claude.com/docs/en/costs) recommends
specific prompts, conditional workflow instructions and concise results from
verbose work, whose worker calls still consume usage.
[Claude's context contract](https://code.claude.com/docs/en/sub-agents)
distinguishes fresh context, resumption and forks; cache sharing can favor forks
for tasks needing the same context. Therefore fresh context is our isolation
default, not a universal cost guarantee. These observations are documentation
evidence, not measurements of this framework's savings or client activation.

The following are local design requirements. Retain the current no-full-history
handoff default and selected model/effort pairs. If reconstructing shared context
would outweigh a useful handoff, prefer inline execution when independence is not
required. Do not silently enable full-history forks or lower effort to save cost.

| Decision | Required behavior |
| --- | --- |
| Whether to delegate | Use an authorized worker for a bounded result with a concrete reason: independent assessment, useful independent parallel work or isolation of substantial noisy investigation. State that reason briefly in the existing handoff; no separate decision document. Keep small, tightly coupled work inline. A configured role, checkbox, test command or available slot alone is insufficient. |
| Unit of work | Delegate a coherent result with stable ownership and acceptance, not each file, edit or command. Do not create a planner for an already agreed plan, a progress-update agent or agents that repeat the coordinator's investigation. Mandatory independent review remains binding. |
| Minimal sufficient handoff | Include task ID/outcome and acceptance, assigned paths and interface dependencies, exact workspace/checkout and canonical plan/spec sections, pre-edit baseline, material decisions/constraints, selected role/model/effort, current permissions/checkpoint, relevant verification evidence and required result format. Preserve uncertainty and known failures. Scale the brief to the task; no arbitrary prompt-token cap. |
| Instruction loading | Put essential constraints and applicable Superpowers adaptations in the brief; give precise reachable paths/sections for remaining required policy, contracts and checks. Pass substantive required policy once, either as current text or through an explicit worker read. A link, copied filename or parent having read a rule does not establish worker context. Do not require rereading text already supplied unchanged. Load adjacent contracts when needed for a concrete dependency; never omit necessary constraints merely to shorten input. |
| Progressive context | Do not preload every profile, example, historical plan, unrelated skill or full log. Keep reusable role prompts short and route to the authoritative rules. Expand context only for a named missing decision, dependency or failure; ask the coordinator for unavailable essential context rather than restarting broad repository discovery. Never substitute a stale excerpt for a changed source. |
| Continuations and waiting | Under ORCH-01, resume the same bounded assignment when its context remains useful and supported. Send changed requirements, findings and evidence instead of replaying the whole brief; identify invalidated inputs. A new assignment or independent review gets its own appropriate context. Do not claim resume is always cheaper, issue keepalive messages for cache warmth or repeatedly poll status; use supported completion notifications/bounded waits while preserving required user updates. |
| Returned result | Return outcome against acceptance, changed paths or located findings, check commands/status and applicable state, remaining risks/blockers and focused evidence references. Keep raw successful logs and transcripts out of the coordinator context. The coordinator checks actual scoped changes and unresolved risks, reusing valid evidence rather than rerunning discovery/tests solely because a worker returned. |
| Cost evidence | Count coordinator and all worker work, including handoffs, repeats and reviews. Separate reported input/output/reasoning and cache usage when available; avoid double-counting client aggregates. Token counts, latency and billed cost are distinct, and unknown telemetry stays unknown. Savings claims need comparable authorized runs with matching scope, model/effort and quality criteria; no mandatory paid comparison or new monitor. |

Source ownership: extend `standards/orchestration.md` for delegation/context/cost;
reuse `standards/verification.md` for evidence and compact logs, and
`standards/model-configuration.md` for model choices. Relevant native-role templates
receive concise routes and output expectations, not copies of the whole policy.
Keep client-specific context/cache observations in the planned capability research.
No new default quotas, cache settings or policy-TOML keys are introduced.

### Implementation stage C — orchestration and integration model step

Current item: none — ORCH-01 through ORCH-06 and ORCH-CHECK are complete.
Stage status: awaiting user review.

Implement after the combined source scope is agreed, using A's path contract and
B's progress semantics. Files: `standards/orchestration.md`, `templates/PLANS.md`,
`standards/model-configuration.md`, `MIGRATION.md`,
`templates/skills/af-integrate-project/SKILL.md`,
`templates/skills/af-model-setup/SKILL.md`,
`templates/skills/af-model-reassign/SKILL.md`,
`templates/framework/adoption-record.md`, affected inactive native role templates
and `templates/codex/README.md`. Create
`docs/research/2026-10-04-orchestration-capabilities.md` for dated client evidence.
Update overview routes only where behavior changes; do not duplicate full policies.

- [x] ORCH-AUDIT: Compare the retained instructions with official client sources
  and installed Superpowers; distinguish existing safeguards from new proposals.
- [x] ORCH-01: Specify lifecycle/continuation and stale-result handling.
- [x] ORCH-02: Specify serialized progress updates and planner draft ownership.
- [x] ORCH-03: Specify optional native role restrictions and their evidence limits.
- [x] ORCH-04: Record the bounded client capability comparison with dated sources.
- [x] ORCH-05: Add the required integration model step and its situation-specific
  outcomes above. Reconcile the integration entry's current no-model-setup wording,
  the setup skill trigger and model contract's first-use table. Keep ordinary work
  exempt and reuse existing reassignment/recovery logic. Adapt routes to real source,
  bundle and installed locations; use writing-skills for actual skill edits.
- [x] ORCH-06: Specify the delegation decision and minimal sufficient handoff in
  the existing orchestration owner; align affected role prompts and Superpowers
  routes without copying policy. Preserve selected models/efforts and required
  reviews; reuse ORCH-01 for continuations and verification for evidence reuse.
- [x] ORCH-CHECK: Check changed links/formats and instruction consistency; review
  scenarios for a late result after reassignment, a partial worker report, two
  workers completing together, a resumed correction, missing project rules in a
  built-in planner, and a reviewer whose native permissions remain writable.
  Also cover initial setup, existing valid assignments, single-agent reuse,
  preparation without writes, explicit deferral followed by an ordinary update,
  requested reassignment, unavailable skill with/without its contract, unknown
  schema, unsupported model and an interrupted native write. Validate edited skill
  frontmatter with an available supported validator; report unavailable validation.
  For ORCH-06, inspect representative briefs for a tiny inline edit, independent
  frontend/backend work with a shared API contract, a risk-based reviewer, and a
  correction to an existing assignment. Verify no whole-plan/history preload,
  omitted global constraint, duplicate discovery/check cycle, stale evidence reuse
  or repeated unchanged-policy read. Include a missing essential route and absent
  usage telemetry; report limitations without invented savings or a new benchmark.
  Reuse existing evidence; no application tests or paid client runs for prose alone.

Completion requires reachable, consistent instructions and evidence for these
scenarios. An explicit user deferral completes the integration decision step,
not model configuration or a delegation prerequisite. Updating source templates
never constitutes completed target setup or proof of runtime adherence.

Historical audit-stage evidence, before implementation: the scoped artifact check passed (one document, zero
errors); `git diff --check` passed. Separate inspection and whitespace checking
covered this untracked plan against its pre-edit copy. Hash comparison confirmed
235 other files unchanged. The audit temporary baseline was removed after review.
Native instructions and templates remain unchanged; follow-up checkboxes describe
future work. No live client execution or paid model pilot was performed.

### Stage C scenario review and evidence — 2026-10-04

Implemented ORCH-01 through ORCH-06 with the agreed owners. Baseline review found
the integration skill explicitly excluded model setup and the setup trigger only
covered an explicit request/delegation; these routes now include the required
integration decision. The ARCHITECTURE skill table, README route and catalog `when`
hint needed the same update; their pre-write copies were added to the stage baseline.
No schema, catalog resources/dependencies, model pair or session setting changed.

Inline instruction scenarios were evaluated against the final owners and skill
entries, not by launching workers or changing a consuming client:

| Scenario | Observed instruction outcome |
| --- | --- |
| A late T1 report uses baseline B after ownership moved to T2/current C | Lifecycle requires reconciliation against current assignment/files; stale completion cannot close T2 or overwrite C. |
| A partial report has a pending shell command, or an interrupt merely returns | Completion/stop must be confirmed before ownership transfer, dependent review or cleanup; recovery material remains available. |
| Two workers finish together | Both report evidence; the coordinator reconciles and serializes canonical marker updates. A planner hands back its draft before another writer edits it. |
| Same bounded assignment needs a correction | Continue the supported worker with the changed input and invalidated evidence; no fresh worker or whole-history replay merely for a correction. |
| Built-in planner lacks project instructions | Supply essential constraints and explicit reads of missing rules; parent knowledge is not inherited evidence. Missing required context holds only dependent work. |
| Reviewer still has writable native tools | Report unverified enforcement, retain behavioral no-edit scope and use a stable baseline. A cache-writing check goes to an authorized executor; planner draft rights stay separate. |
| Initial integration has no assignments | Required setup step reuses known choices and resolves only material missing choices before dependent writes/spawns. No template pair becomes a selection automatically. |
| Existing delegated or single-agent selection agrees with native state | Check/reuse without repeated onboarding or writes; single-agent mode satisfies the integration decision. |
| Preparation includes a requested model change | Produce exact proposed paths/values and unresolved inputs; no target files, skill installation, session switch or pilot. |
| Explicit deferral followed by an ordinary rules update | Canonical decision and adoption outcome retain deferral; rules proceed independently without setup or configured-state claims. Mere absence is unresolved, not an invented deferral. |
| Explicit reassignment/client change | Reassignment skill preserves unspecified choices, prepares the requested mapping and uses existing authorization/recovery; an ordinary rules update never requests this implicitly. |
| Model skill unavailable, contract reachable/unreachable | Disclose contract fallback when reachable; otherwise report the step unresolved and continue independent authorized adoption work. |
| Unknown schema or unsupported pair | Existing model owner preserves contents/choices and blocks dependent editing/delegation; no reinterpretation or substitution. |
| Native write interrupted | Existing recovery preserves newer edits; configured status requires agreement, and incomplete recovery stays reported partial/unresolved. |
| Ordinary coding, general audit or source-library maintenance with missing configuration | Integration/setup skills are not triggered by absence alone; current inline work continues without onboarding. |

ORCH-06 representative briefs were inspected as synthetic handoffs, not executed
assignments. For delegated examples, the shared envelope used instruction root
`/fixture`, checkout `/fixture/repo`, canonical `/fixture/docs/plans/change.md#s1`,
baseline `/fixture/recovery/B`, current stage and human checkpoint. The hypothetical
saved selection enabled implementer `gpt-5.6-sol`/`high` and reviewer
`gpt-6-astra`/`high`, with direct coordinator edges, a two-worker ceiling and known
capacity for the assigned work. These are scenario inputs, not new defaults or
changes to this session. Essential constraints were supplied
as current text: no Git writes or outside-scope edits, preserve B/user changes,
fresh context, local Superpowers adaptations and required gates. Remaining reads
named only task-relevant sections; evidence identified the input state it covered.

| Brief | Inspection result |
| --- | --- |
| Tiny README wording correction | Kept inline; an available worker/checkbox gave no benefit or permission. Only its affected artifact check was selected. |
| Independent frontend/backend work | F1 owned `web/form.ts`; B1 owned `api/submit.ts`; both received the agreed request/response contract, while its common owner retained `contracts/submit.ts`. Overlapping contract edits required coordination; affected integration evidence was pending after combining results. |
| Risk-based reviewer | Received the completed scope/diff against B, relevant spec section, stable file state and valid check summaries. No implementation rights, full-plan preload, raw success logs or duplicate test run; returned located findings and evidence limits. |
| Correction to F1 | Same assignment received only the revised response field, affected current state and invalidated F1 evidence. Unchanged constraints/check results were reused; stale output could not be applied automatically. |
| Missing essential API route | Worker reports the exact missing input to the coordinator; dependent implementation waits without broad rediscovery or a stale excerpt. |
| Missing usage/cache telemetry | Cost stays unknown; no savings claim, lower-effort substitution, extra agent or mandatory paid benchmark. |

Executed verification:

- Source artifact check: 193 artifacts, zero errors. Explicit affected-file check:
  14 artifacts, zero errors; the subsequent overview/catalog/plan change passed a
  four-file scoped check. The checker/Python tests were unchanged, so stage-B
  unittest and strict-mypy evidence was reused instead of repeated.
- Existing `skill-creator/scripts/quick_validate.py` with `python3 -B` passed for
  all three edited skill directories. This validates frontmatter/basic structure,
  not runtime discovery or agent adherence; no new validation dependency was needed.
- Source-derived flat and contained temporary bundles: 11 profiles, 63 copied
  resources/templates. Each closure scan checked 64 artifacts with zero errors;
  explicit installed-role/skill and inactive-template scans checked seven with
  zero errors. Native TOML and applicable path literals were checked separately.
  Policy override/adoption-state path literals retained their instruction-root
  base in both layouts. Integration-skill source/provenance resolution was inspected
  against supplied full-source and native locations. File preparation did not
  establish native activation.
- All 29 omitted-route identities were conditional research/history or unselected
  technology references, adapted to labelled source references through provenance;
  required routes stayed local. The disposable fixture initially mishandled empty
  fragment paths and unselected root-template literals; those fixture assumptions
  were corrected before recording passing results. Production checks were not weakened.
- Accountable inline review covered the actual pre-stage diff, including the new
  capability note. Sixteen existing files changed and one was added; all 222 other
  inventoried files retained their hashes. Native role metadata and catalog topology
  were compared separately. `git diff --check` and separate whole-file whitespace
  inspection of all 17 paths, including new/untracked files, passed. The final
  evidence-plan artifact check passed. No blocking acceptance issue remained.
  Task-only temporary material was removed after review and evidence recording.

The dated [capability comparison](../research/2026-10-04-orchestration-capabilities.md)
records official sources, local version commands and tool-schema limits separately.
There was no live delegation, native-permission/adoption pilot or cost benchmark.
Behavioral scenarios are source-instruction review, not demonstrated client behavior.
No target-project reads/writes/tests, installed plugin edits, active templates,
model/session changes, Git writes or permanent accepted-snapshot changes occurred.

### Stage C review follow-up — lifecycle and duplication

The user requested explicit confirmation of lifecycle coverage and a duplication
review. Used Superpowers review skills with local adaptations, inline. This is a
targeted stage-C follow-up, not acceptance of stage C or target-migration permission.
Before edits, `/tmp/aek-C-review-fizeidl4/baseline` captured the current orchestration
owner and this plan, including existing local changes; 239 file hashes were recorded.

Lifecycle acceptance was traced to `standards/orchestration.md`, "Worker lifecycle
and continuations": assignment/baseline/state; pending tools and partial reports;
confirmed completion or authorized stop before transfer/review/cleanup/checkpoint;
same-assignment continuation; stale-result reconciliation after reassignment; and
preservation of current work. The section routes checklist serialization and planner
handback to the single planning owner. These cover ORCH-01/02 as instruction policy;
runtime compliance remains untested.

Duplication scope: executable checker/test code and the stage-C orchestration,
model, planning, migration, Superpowers and affected skill/native-template routes.
AST inspection covered 66 Python functions; no identical bodies with at least
three statements were found. A search for repeated five-nonblank-line windows of
at least 160 characters found none. Exact substantive prose-paragraph matching
also found none. These bounded searches were complemented by manual semantic
review; they are not proof that every similar fragment in the library is absent.

Manual review found repeated delegation criteria in Responsibilities and Delegation
contract, plus a repeated full-history/raw-log sentence. Removed the redundant
wording and routed Responsibilities to Delegation contract; no lifecycle requirement
was removed. Kept role-specific constraints and thin skill routes because separate
entry contexts need them. Historical specification/evidence is not a second
operational policy owner. Python schema/default loading already shares validation;
different bundle/project path boundaries are intentional, and independent policy
test values must not be replaced with production defaults. No Python change needed.

The scoped artifact check passed for both changed documents (zero errors), as did
`git diff --check` and separate whole-file whitespace inspection. The actual diff
was reviewed against the saved pre-edit copies; all 237 other files retained their
hashes, and the lifecycle section remained byte-for-byte unchanged. Unchanged Python
evidence was reused. Task-only baseline material was removed after review; the
historical scratch path above is no longer a recovery location. Stage C remains
awaiting user review; no target, Git, native settings or model changes occurred.

### Final framework logic review — user-requested follow-up

The user authorized a full final logic review of framework rules using Superpowers.
Review current operational policy, catalog/profile applicability, adoption and
native/template routes as one system; distinguish normative rules from illustrative
examples and historical evidence. This does not authorize target migration, native
activation, model changes, Git writes or delegation. Keep one canonical record here.

Current item: none — FINAL-01 through FINAL-04 complete.
Review status: awaiting user review; stage C acceptance remains with the user.

- [x] FINAL-01. Check authority, planning, progression, verification and policy-setting
  contracts for contradictions, circular prerequisites and unclear ownership.
- [x] FINAL-02. Check profile and topic rules against shared policy and their stated
  applicability; follow examples/vendor sources only for concrete uncertain contracts.
- [x] FINAL-03. Check adoption, root/native entries, skills and catalog/checker routes;
  resolve confirmed logic defects without changing the agreed design.
- [x] FINAL-04. Check affected artifacts/scenarios and the actual review diff;
  record findings, fixes and evidence limits, then remove task-only scratch.

Pre-edit baseline: `/tmp/aek-final-logic-watoo846/baseline`; initially this plan,
with each additional affected file saved before its first edit. The inventory
records 239 existing file hashes. Earlier successful checks retain their original
meaning and will be repeated only for changed inputs or specific new concerns.

Review findings and resolutions:

- FINAL-L1 — verification timing had conflicting consumers. The owner allowed
  `task_end`, but its next paragraph forbade later-phase functional acceptance;
  delivery also demanded evidence at every phase. Clarified test design/writing
  versus execution, pending acceptance markers and authorized internal progression.
  Delivery and Unreal block cadence now route to that same timing owner. Human
  checkpoints, dependency checks, selected TDD and mandatory gates remain binding.
- FINAL-L2 — the architecture overview still said import never triggers setup,
  despite the accepted full-integration model-selection step. Updated its reading
  route and ownership row to distinguish the required decision from authorized
  native writes and actual activation. MIGRATION and model configuration remain
  the owners; no model values, roles or session settings changed.
- FINAL-L3 — the policy-entry template selected inactive bundled `templates/PLANS.md`
  as a fallback working policy. It now selects the adopted root `PLANS.md` or agreed
  local/native route; the inactive template is explicitly an adoption reference.
  Existing task stores and the source library's maintenance route are preserved.

The logic review covered shared authority, work modes, delivery, planning/progress,
policy settings, verification, orchestration/model ownership, Superpowers adaptations,
catalog applicability and adoption/recovery. Reviewed all technology entry routes
and normative clauses with surrounding context in 102 topic files across 22
technology families, comparing them with shared constraints. The catalog has
23 profiles including shared process profiles. Examples and dated research remained conditional
evidence, not new mandatory policy or a repeated vendor/version audit. No further
confirmed cross-profile contradiction or competing rule owner was found.

Decision scenarios reviewed against the resulting rules:

| Scenario | Required outcome |
| --- | --- |
| Default phase boundary | Complete necessary checks before its human checkpoint |
| `task_end`, two internal phases, explicit continuous progression | Write needed tests with implementation; batch execution at task boundary; pending acceptance remains open |
| `task_end`, human checkpoint or risky dependency before task end | Run the required intermediate checks before that transition |
| Implementation item closed while a separate verification item is pending | Allowed only by its own criteria; never claim verified task/stage completion |
| Existing valid evidence, compaction or a report-only edit | Reuse evidence; no new execution cycle without a relevant change or required gate |
| Full integration, existing selection / explicit deferral / preparation only | Account for the model decision through its owner; reuse, report deferral, or prepare without activation respectively |
| Ordinary inline work, absent routing record | No model questionnaire, delegation or native writes |
| Root policy, inactive planning template, existing native task store | Use the adopted root/local policy and canonical store; inactive copy does not become runtime authority |
| Worker timeout, pending command, reassignment or late result | Hold dependent ownership transitions until actual state is reconciled; stale evidence cannot close progress |
| Relocation with local changes, collision, interruption or repeat | Preserve B/C/N and old accepted snapshots; reconcile owned paths and pending checks rather than bulk overwrite/rollback |

These are instruction/decision reviews, not executed agent or editor behavior.
Fresh artifact checks passed for 193 source artifacts and six affected documents.
Disposable flat and contained Unreal bundles each passed the selected eight-profile
closure (35 artifacts) and five installed root/plan/skill documents. Both used a
project-root `task_end` override. Root `PLANS.md` and native model-skill routes were
also resolved explicitly because code-span routes are outside Markdown checking.
Four optional source references, including the inapplicable React size-rule route,
were labelled during fixture adaptation under the catalog contract; required links
were retained. The fixture builder initially exposed that conditional React route;
it was reconciled explicitly, without changing source selection or weakening checks.

No checker/Python, catalog, defaults, native skill or runtime example was changed.
The prior 40-test checker suite, strict Python analysis and lifecycle/code-duplication
results retain their original scope; they were not rerun or relabelled as new evidence.
No client pilot, model switch, target migration, stack build or measured token-saving
claim is part of this review. The actual diff against the saved pre-review contents
was inspected: only five rule/overview documents and this canonical plan changed;
233 other inventoried files retained their hashes, with no new or deleted paths.
`git diff --check` and separate whole-file whitespace inspection of the changed
files, including pre-existing untracked files, passed. Historical plan sections and
accepted snapshots were preserved. After recording results and completing scoped
review, the exact task-only scratch directory (baseline, extracts and fixtures) was
removed; its historical path above is no longer a recovery location. No unresolved
confirmed logic finding remains in the reviewed scope. This is not proof of native
client adherence or an assertion that all possible defects are absent.

## Consolidation evidence — 2026-10-04

At the user's request, consolidated stages A/B and ORCH-01 through ORCH-05 in
this combined specification/plan using Superpowers writing-plans with local
adaptations. Added the integration model-step contract, owners, dependencies and
acceptance scenarios. Implementation remains pending; future task boxes stay
unchecked. The scoped artifact check passed (one document, zero errors), the
actual plan diff was reviewed and tracked/untracked whitespace checks passed.
Hash comparison confirmed 235 other source files unchanged. Temporary review
material was removed after verification; no target or native settings were edited.

## Context-efficiency review evidence — 2026-10-04

Added ORCH-06 after official-source review and comparison with existing handoff,
cost and verification rules. The specification defines context assembly and
proportional delegation; stage C owns implementation and scenario checks. Reviewed
the scoped diff for requirement loss, duplicate policy, model-choice preservation
and unsupported savings claims. The artifact check passed (one document, zero
errors), tracked/untracked whitespace checks passed, and 235 other source files
matched their pre-edit hashes. Removed temporary review material after recording
evidence. No delegated pilot, token benchmark, native configuration change or
production-instruction implementation was performed.
