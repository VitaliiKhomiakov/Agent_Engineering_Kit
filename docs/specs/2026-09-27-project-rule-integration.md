# Project rule integration

Date: 2026-09-27. Design and requirements; execution state belongs to the linked plan.

The user requested this specification and its [implementation plan](../plans/2026-09-27-project-rule-integration.md)
so integration can resume after a separate technology-support change. This document
owns requirements; the plan owns dependencies, authorization, progress and evidence.
The prerequisite is Unreal Engine support, including Unreal C++ practices, MCP
workflow and assessment of dedicated skills; see the
[research and proposed support shape](../research/2026-09-27-unreal-engine-engineering-and-mcp.md).
Recording these documents alone grants no implementation or target-import
permission. Later authorization and completed prerequisites are recorded in the plan.

## Outcome and scope

An agent imports selected Agent_Engineering_Kit rules into a new or existing project,
reconciles old active instructions, preserves project contracts and can repeat or
update the import without overwriting independent work. The result is a coherent
set of target-project instructions with routes for reading detail when needed.

The proposed entry is one instruction-only skill, `af-integrate-project`, backed
by the existing migration policy. A separate preparation-only request uses the same
procedure and stops at the prepared change set. A single skill was recommended in
discussion; the user's launch decision is recorded in the implementation plan.
The chosen entry reuses this contract.

Retain the rules-only product scope: no application, installer, workflow engine,
background monitor or automatic external model call. Native model setup remains
owned by the existing model-configuration procedure and runs only when requested
or necessary for an explicitly authorized delegation. Import does not rewrite
application code, change dependency versions or relocate existing task stores.

## Existing foundations and gaps

- [Migration](../../MIGRATION.md) owns adoption, conflict inventory and a bounded pilot.
- [Catalog semantics](../../standards/catalog.md) distinguishes bundle availability
  from conditional reading; its existing profile IDs and dependency rules are reused.
- Entry, architecture and planning templates already preserve local contracts,
  canonical tasks and independent project opening.
- `af-migrate-project` is conceptual. There is no implemented general import skill,
  concrete adoption-record template or unified repeat/update/recovery contract.

Extend these owners instead of creating another delivery or model-setup lifecycle.

## Requirements

### I1. Explicit entry and scope

Accept an accessible framework source, target workspace/project, selected client,
and import intent: prepare only, initial import or update. Reuse facts and choices
already supplied; ask only for material missing information. Do not infer a remote
revision or installed client capability from example names. A missing skill in a
target can be read from the source when accessible; do not require global installation
or claim it is natively discoverable before adoption.

Distinguish source library, target instruction root, implementation checkout and
canonical task store. The source library need not install its own AGENTS/PLANS.
Operate within explicitly selected targets; one import does not change other
projects, clients, personal/global settings or plugin caches.

### I2. One procedure for new and existing projects

For a new project, determine its intended stack and relevant parent instructions,
then prepare selected rules, entry routes and an appropriately sized passport.
Do not fabricate observed architecture or remediate nonexistent legacy code.

For an existing project, inspect active instruction sources, applicable stack,
local contracts, check commands, canonical task entry and relevant native settings.
Resolve actual loading sources for the chosen client, including nested or alternate
instruction definitions when relevant. Do not audit the entire codebase merely to
import rules. An uncertain product requirement is a decision gap, not permission
to replace it with a generic framework assumption.

### I3. Concrete conflict replacement

During authorized adoption, the framework's selected engineering policy replaces
conflicting old process rules within the agreed scope. Implement replacement in
the files actually read by the client; a statement that the new root wins is not
a substitute for reconciling loaded conflicts or native precedence.

| Existing content | Target treatment |
| --- | --- |
| Generic process conflicting with the selected framework policy, such as gratuitous full-suite runs or repeated reviews | Replace with the owning framework rule and a short reading route |
| Duplicate engineering explanations | Consolidate under one owner; remove duplicate active instructions |
| Actual build commands, required CI gates, supported versions, business/security invariants and project contracts | Preserve in the appropriate local entry/passport/check document |
| Deliberate project exception | Record its scope, reason and accepted decision; do not silently discard it |
| Ambiguous conflict affecting behavior or a mandatory gate | Clarify that decision before dependent replacement; continue independent preparation |
| Superseded instruction content | Retain recoverable originals outside active instruction/skill discovery |

Do not classify an actual mandatory check as redundant merely because it is costly.
Distinguish a project gate from a generic instruction to rerun it after every edit.
Framework policy cannot override higher-priority system/developer instructions or
actual tool permissions. Report a conflict outside authorized control rather than
claiming the target has been reconciled.

### I4. Portable bundle and progressive reading

Assemble shared required resources and selected profiles with their catalog
dependencies/resources. Preserve paths or adapt affected references consistently;
resolve required local references beyond catalog entries as well. Keep external
research optional and do not copy unrelated archives into the loaded context.

Fill target entry placeholders with actual profile paths, project facts and reading
conditions. Common safeguards remain visible; detail is selected by task and stack.
Preserve limits on speculative code checks, unnecessary tests and repeated review.
Broad filename matches or dependencies do not select unused frameworks. Independently
opened repositories and delegated roles need reachable routes and applicable policy.

Use the selected client's verified entry mechanism. Unsupported mappings remain
explicit limitations; do not invent settings or install every client/role template.
Existing native task stores retain their locations and single progress owner.

### I5. Preparation, application and authorization

Prepare a concrete change summary: source identity, selected profiles, affected
target paths, create/update/retire actions, conflict decisions and retained local
contracts. Inspect the current contents before proposing replacements.

Preparation-only intent never writes target files. An explicit import instruction
may already authorize scoped replacements; honor it without asking again per file.
Respect the selected human checkpoints and unresolved material decisions. The
integration procedure does not independently grant Git actions or model switches.

Before the first target write, retain original contents or absence, including user
edits. Check for changes since preparation; reconcile intervening edits before
overwriting. Retire obsolete active instructions only after their necessary content
has a reachable owner. Keep recovery material outside discovery paths and preserve
unrelated native settings, roles and comments.

### I6. Adoption record and repeated import

Use a concise target record at `.agents-framework/adoption.md`, described by a
new `templates/framework/adoption-record.md`. It records import provenance and
file ownership, not task progress or competing model assignments:

- Framework source and revision, or a verifiable content identity when no revision exists.
- Target root/client, selected profiles and adopted local exceptions.
- Managed destination paths and their corresponding source/template identities.
- References to the accepted imported contents or hashes and recoverable originals.
- Agreement state: prepared, applied but unverified, verified or partial; verification scope.

For preparation-only intent, the proposed record remains in the preview outside
the target; its planned destination does not authorize writing it there.

Task decisions and implementation progress remain in the canonical adoption task.
Entry/passport provenance points to this record rather than maintaining a competing
version list. Keep it out of ordinary task reading unless import/update needs it.

An unchanged source, selection and matching target require no file rewrite. A new
source version updates only managed scope; do not equate an `af-` prefix with ownership.
Compare source changes, last accepted imported state and current target edits where
available. Preserve independent edits; if the necessary base is missing, report
that limit and reconcile explicitly rather than guessing or claiming a safe merge.
Treat source removals and user-edited managed files as explicit decisions in the
prepared change set. No automatic reset or deletion of unrelated resources.

### I7. Partial failure and recovery

On interruption or failed application, identify which files changed and which did
not. Preserve the recovery material and expose partial state. Restore only this
operation's changes where safe; never overwrite newer user work or mark an incomplete
import verified. Resume from actual files and the canonical task evidence, not an
assumed successful previous run. An import record alone is not proof of agreement.

### I8. Sufficient verification and honest readiness

Check changed formats, reachable target-relative paths, resolved placeholders,
conflicting loaded instructions, preserved local contracts and repeat/update cases.
Reuse valid results; every repeat follows the existing evidence-reuse policy.
No application test suite is required merely to copy instruction text.

Distinguish a verified file bundle from observed client discovery/adherence.
A bounded target pilot can check fresh entry, conditional reading, required task
checks and resumption. It needs an actual selected target/client and authorization;
maintaining this library does not itself grant installation or model execution.

## Acceptance scenarios

| ID | Input | Required outcome |
| --- | --- | --- |
| A1 | New project with a declared stack | Only applicable bundle/routes; intended architecture labelled honestly; no legacy remediation |
| A2 | Existing conflicting rules and required project checks | Conflicting process replaced; actual gates and product contracts preserved; no active opposing duplicate |
| A3 | Preparation-only request | Reviewable path/action/conflict summary; no target writes |
| A4 | Python-only or JavaScript React project | Unused frameworks/TypeScript obligations excluded despite bundled dependencies |
| A5 | Independently opened project or delegated role | Reachable applicable entry/rules without assumed parent discovery or full-history inheritance |
| A6 | Same import repeated with unchanged inputs | No needless rewrites, setup questions or verification reruns |
| A7 | Source update plus local edits, missing base or removed resource | Scoped comparison; preserved user work; unresolved replacement/deletion made explicit |
| A8 | Failure during apply or edits after preparation | Accurate partial report and safe scoped recovery; no false success or overwrite |
| A9 | Existing native tasks and model choices | Canonical store and choices preserved; import alone triggers no relocation or reassignment |
| A10 | Valid files but no client pilot | File verification reported separately; runtime behavior remains unverified |

## Sequencing constraint

Complete the separately requested technology-support work before implementing this
integration. The technology is Unreal Engine; its version scope, canonical task
and completion evidence are recorded in the implementation plan. On resumption, read the completed technology
profile/catalog changes and rebase this design's file assumptions accordingly.
The dependency's completion is not automatic permission to start integration.
