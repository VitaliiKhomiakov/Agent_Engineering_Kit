# Read-only adoption diagnostics specification

**Status:** Conditional proposed design, awaiting review. No implementation or
target inspection is authorized by this document.
**Date:** 2026-10-07.
**Updated:** 2026-10-08, optional reuse of the owner-supplied AEK_TEST sandbox.
**Implementation plan:** [Diagnostics plan](../plans/2026-10-07-adoption-diagnostics.md).
**Rationale:** [Feasibility assessment](../research/2026-10-07-development-feasibility.md).

## Outcome and decision to build

Answer a specific question about an adopted AEK setup with a bounded, evidence-backed
report: what is configured, what may conflict, what is known to work, and what
remains unobserved? The report leaves the target unchanged and points to the
existing owner for any proposed repair.

The owner currently reports no critical problem. Therefore this is a conditional
design, not a commitment to build `aek-doctor`. First use the existing adoption
owners and artifact checker for a concrete diagnostic need. Package a new procedure
only if it helps; package a skill only if repeated invocation adds practical value.
If diagnosis has no recurring value, the manual report is a sufficient outcome.

## Global Constraints

- Preserve the rules-library scope; no diagnostic application, CLI, daemon, MCP server, new database or automatic repair.
- Diagnosis is explicitly selected and read-only for the target; ordinary coding and missing optional files do not trigger it.
- Reuse MIGRATION, catalog, verification, policy and model owners; diagnosis does not define new precedence, merge or setup rules.
- Separate inspected files, documented client behavior and observed runtime behavior; unknown evidence is not a confirmed defect.
- Preserve flat, contained and custom layouts, local exceptions, existing task stores and saved model choices.
- Keep reports in the response or an explicitly selected canonical location; do not create target records, hashes or caches as a diagnostic side effect.

## Scope and exclusions

In scope: selected entry routes, bundle/profile evidence, active-instruction
conflicts when evidence permits, optional policy state, adopted provenance and
managed-file drift. Inspect only the selected question's relevant concerns.

Out of scope: validating application architecture or every source file; evaluating
all technology APIs; forcing model setup; launching an agent pilot; auditing every
client; accessing global credentials; changing instructions; applying updates;
or automatically claiming a root cause for a previous model decision.

Use Superpowers `diagnosing-superpowers` for an actual reported Superpowers session
failure when suitable tools and transcript evidence are available. This diagnostic
can supply setup facts, but does not replace that skill or copy its process.

## Inputs and path resolution

| Input | Treatment |
| --- | --- |
| Diagnostic question | Explicit setup/adoption question or named symptom; no broad scan by default |
| Target instruction root | Supplied project/workspace, independently opened repository if relevant, and actual execution checkout |
| Client | One selected client/version, supplied native evidence and allowed scope; capability unknowns remain unknown |
| Adoption state | Existing `.agents-framework/adoption.md` if present, its owned paths, source identity and accepted exceptions |
| Bundle layout | Resolve from record and actual files; do not guess between multiple present bundles |
| Profiles | Actual selected IDs and relevant stack facts; globs alone cannot establish a framework |
| Source | Accessible identified AEK source, if a source comparison or source-owned procedure is needed |

Reuse the source resolution behavior of the integration entry: a copied inactive
skill is not the full source library. Resolve source identity from the request or
adoption record and verify required source resources before using them.
Unavailability prevents only dependent comparison/procedure claims; reachable
local files can still support a partial inventory.

When a diagnostic input is missing, continue independent inspection and ask only
about decisions that change the selected scope. Do not resolve ambiguity by
creating a record, installing a bundle, selecting another client or promoting an
old copy to the current source. An intentionally absent optional file is normal.

## Inspection sequence

1. Record the question, selected roots/client and evidence limits. Read applicable
   entry constraints and the relevant adoption record once.
2. Identify candidate entry/native files using the installed client's documented
   contract and available observation. Merely finding a file does not prove loading.
3. Follow only the selected entry/profile routes. Distinguish files available in
   the bundle from instructions required for this task.
4. Reuse the artifact checker for a known compatible catalog/layout. Report its
   exact scope, command/result and unsupported cases. Inspect non-catalog native
   files explicitly where relevant. Do not invent CLI flags or auto-install tools.
5. Assess selected semantic questions: opposing applicable requirements, preserved
   local exceptions, missing owners or a relevant configuration inconsistency.
6. If drift/update was selected, use the existing accepted-base contract. An
   adapted candidate requires integration preparation; a raw source diff alone
   cannot establish target behavior or a safe replacement.
7. Return a compact report, with evidence for each material finding, unanswered
   questions and the smallest useful next action. Do not start the repair.

Ordinary filesystem reads and documented read-only validation are sufficient.
Do not run target builds/tests or native initialization commands solely for this
inspection. Do not scan every installed skill, historical plan or profile.
If invoking a target-owned command could execute hooks or write state, treat it
as a separate execution action rather than assuming a `check` name is read-only.

## Evidence and finding model

These fields describe a report, not a required machine schema or new database.

| Field | Meaning |
| --- | --- |
| Finding ID | Stable within this diagnostic report; future updates preserve its identity |
| Concern and scope | Exact instruction/configuration/route and affected task or project |
| Classification | Confirmed finding, potential conflict, information, or not assessable |
| Evidence | Inspected path/section or available native event, command outcome, date/state |
| Evidence class | Artifact inspection, official client contract, observed client/task event, or historical record |
| Consequence | Concrete behavior or decision that may be affected; no speculative severity inflation |
| Owner and next action | Existing authoritative procedure and proposed scoped action; no repair authorization |

A confirmed file defect can be established by a broken link or invalid supported
TOML. A confirmed active-rule conflict needs both incompatible applicable contents
and adequate evidence that the selected client uses them. Otherwise report a
potential conflict. Native precedence is client behavior, not a rule invented by
AEK. A short reminder and its detailed owner are not automatically duplication.

The report must distinguish these statements:

- A file exists and its checked format is valid.
- The client's documented discovery mechanism should select the file under the
  recorded conditions; this remains a source-based expectation.
- Available client evidence shows that the instruction was supplied in a specific
  session, or shows a particular observable task behavior.

None proves hidden reasoning or universal future adherence. Missing read events
do not establish that auto-loaded instructions were absent. An agent's final
claim of compliance without supporting evidence is not a runtime certificate.

## Required edge behavior

| Condition | Required result |
| --- | --- |
| No adoption record | Identify unrecorded provenance; inspect reachable entries within scope; do not initialize adoption |
| No optional policy override or deferred model selection | Treat as allowed when the relevant owner permits it; no setup questionnaire |
| Invalid override or unsupported schema | Report exact field/schema and dependent uncertainty; do not treat it as absent or substitute defaults |
| Flat or custom bundle | Use recorded/verified bases; do not relocate it or hardcode `.agents-framework/standards/` |
| Multiple possible bundles | Identify ambiguity and ask for the applicable one before dependent validation |
| Missing accepted contents | Hash equality can establish equality; differing edits cannot be called a safe three-way merge without the required base |
| Old research date | Mark evidence scope/date; do not infer that a rule is wrong or demand blanket dependency upgrades |
| Client/model capability unobserved | Report unknown/stale as appropriate; do not activate a role or switch model |
| Accepted local exception | Preserve and identify its owner; difference from the shared default is not itself a defect |
| Shared native file has unrelated fields | Limit comparison to the recorded scope; no whole-file ownership assumption |
| Source or optional plugin unavailable | Continue supported independent inspection; report the precise unavailable comparison or runtime observation |

## Update explanation within the existing workflow

For an explicitly selected update question, show a small table: changed rule,
affected adopted scope, expected behavior change, retained local exception and
evidence/uncertainty. [MIGRATION](../../MIGRATION.md#repeat-and-update) continues
to own B/C/N comparison, action proposals and application. Diagnosis may identify
where an update needs preparation, but never silently prepares an adapted target
candidate, rewrites accepted snapshots or starts an import.

Do not add an independent update skill or change log that duplicates adoption
ownership. If the diagnostic is unnecessary but semantic summaries are useful,
add that reporting detail to the existing integration procedure independently.

## Optional sandbox reuse

The owner supplied `/home/vitalii/Documents/Local_Projects/AEK_TEST` for tests
on 2026-10-08. The [pilot specification](2026-10-07-agent-behavior-pilot.md#selected-sandbox--aek_test)
owns its application, layout and adoption contract; do not create a second fixture
or require application tests merely to inspect adoption. The sandbox is scheduled,
not provisioned by this document update.

After pilot stage S, a selected diagnostic exercise can reuse its verified bundle:

1. Prepare a disposable copy at `runs/diagnostic-healthy/project/`; inspect the
   selected routes and intentionally absent optional policy override. Expect a
   clean artifact scope with explicit native-discovery limits.
2. Prepare a separate copy at `runs/diagnostic-broken-route/project/`; change one
   selected entry link to a nonexistent local resource, without creating a second
   defect. The diagnostic must name that link and its authoritative repair path.
3. Keep the seeding manifest and expected result in sandbox evidence outside the
   inspected target. Record target contents after seeding and after diagnosis to
   establish that inspection did not repair, initialize or rewrite anything.

Fixture creation and deliberate corruption are coordinator setup actions under
the sandbox grant; they are not read-only diagnostic actions. The diagnostic
itself remains read-only. Do not modify the healthy seed or original observation
project to create a failure case. Other edge cases from the acceptance table are
optional when a specific question warrants them, not an automatic test matrix.

Label these as synthetic cases. Correctly detecting an intentionally broken route
validates a narrow diagnostic capability; it does not demonstrate a naturally
recurring problem, justify `aek-doctor`, or establish that the client loaded the
file. Apply the existing recurrence gate even if both synthetic cases pass.
The pilot's restrictions on exposed reference answers also apply to any claimed
independent behavioral probe; directory separation alone does not hide evidence.

## Minimal implementation shape, if the gates pass

1. **Manual use:** existing source owners/checker and an ordinary scoped report;
   no library feature is required.
2. **Reusable procedure:** `docs/maintenance/adoption-diagnostics.md` owns the
   bounded inspection/report procedure and routes to current policy owners.
3. **Optional wrapper:** `templates/skills/aek-doctor/SKILL.md` supplies a narrow
   explicit trigger and source-resolution route to that procedure. It remains
   inactive until deliberately installed; direct source reading is supported.

As with the existing source-resolved integration entry, the wrapper is an opt-in
source resource, not a new required catalog profile or shared asset. Maintain
source navigation in README/ARCHITECTURE and check its paths explicitly. If a
future design requires copying the procedure as a bundle resource, that is a
separate catalog/adoption decision; do not silently change schema 1 here.

Keep common policy in its existing owners. The wrapper contains no policy engine,
client-settings database, global installer, session hook or automatic trigger on
every task. The existing checker remains unchanged unless a concrete, independently
specified artifact bug is found; semantic diagnosis is not represented as an
exhaustive static validator.

## Acceptance scenarios

| ID | Scenario and required result |
| --- | --- |
| DIA-AC01 | Healthy selected bundle with optional override absent: report evidence-backed clean scope and runtime limits; no changes/setup |
| DIA-AC02 | Broken selected route or invalid supported policy: cite exact source and checker/inspection evidence; propose owner-directed repair |
| DIA-AC03 | Conflicting text without discovery evidence: report potential conflict, not a confirmed runtime cause |
| DIA-AC04 | Missing record/base/source: complete independent inventory and expose limits; no invented provenance or safe-merge claim |
| DIA-AC05 | Accepted local exception and unrelated native settings: preserve both and avoid false-positive drift findings |
| DIA-AC06 | Flat/custom/ambiguous layout: resolve verified bases or pause only dependent validation; no relocation |
| DIA-AC07 | Missing model record or explicitly deferred setup: follow existing policy; no model/role configuration |
| DIA-AC08 | Explicit diagnostic task: no target write, external model launch, application test, installer or repair side effect |
| DIA-AC09 | Ordinary coding request or missing optional file: `aek-doctor` is not automatically invoked |
| DIA-AC10 | Wrapper read outside source tree: resolve source explicitly or report unavailable procedure; no hardcoded author-machine path |
| DIA-AC11 | Read events absent for native auto-loading: do not classify instructions as missing without additional evidence |
| DIA-AC12 | No recurrence or added value is demonstrated, including when only synthetic sandbox cases pass: finish the manual investigation and defer wrapper creation |

## Verification and adoption limits

Use focused document checks and realistic positive/negative invocation scenarios
for any actual skill. A disposable bundle may exercise real checker/path behavior;
no application stack or semantic-LLM test suite is required for prose alone.
Inspect before/after target state to substantiate read-only operation when running
an authorized diagnostic. Client discovery and wrapper usefulness require selected
runtime evidence later; correct source frontmatter alone is insufficient.
