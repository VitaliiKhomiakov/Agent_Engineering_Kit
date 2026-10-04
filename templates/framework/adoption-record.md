# Agent_Engineering_Kit adoption record

<!-- Inactive template. Adapt to target .agents-framework/adoption.md only during
authorized application. Preparation keeps the proposed record outside the target.
Remove guidance/placeholders when filling. Paths below are relative to the named
target root unless explicitly identified as source or external recovery locations. -->

Read only for framework import, update or recovery. This record owns provenance
and managed scope; the canonical adoption task owns decisions and progress.

## Identity and agreement

- Target instruction root and selected projects: `<actual roots>`
- Bundle directory: `<target-root-relative directory; .agents-framework for a new import, . for a retained flat import>`
- Client/version: `<selected client; unknown version stays unknown>`
- Canonical adoption task: `<reachable location; no copied task ledger>`
- State: `<prepared | applied but unverified | verified | partial>`
- Candidate source: `<accessible location + revision or selected-content manifest>`
- Candidate profiles and layout: `<IDs, target routes and any adapted locations>`
- Policy configuration: `<defaults/contract content identity or legacy absence; optional project override path and owned scope, if present; no duplicate values>`
- Model-selection outcome: `<checked/reused | configured | explicitly deferred | unresolved; canonical decision and existing routing/native owner references, with scope/activation limits; no duplicate assignments>`
- Last accepted import: `<source identity, selection/layout and snapshot/manifest reference; none on first import>`
- Recovery material: `<external location and operation reference; available/missing>`
- Verification: `<scope, evidence reference, relevant state; client pilot observed or not run>`

Use verifiable content identities for uncommitted source changes as well as sources
without revisions. Accepted contents are the adapted target result, not necessarily
the source bytes. Preserve the last accepted state during an incomplete update.
`verified` describes only the stated scope; it does not imply observed client use.

## Managed paths

| Destination and owned scope | Source/template identity | Accepted content reference or SHA-256 | Recoverable original or prior absence |
| --- | --- | --- | --- |
| `<target-relative path; whole file or explicit fields/section>` | `<source-relative path + content identity; adaptation reference>` | `<accepted snapshot + hash, or hash with its limitations>` | `<snapshot reference or absent>` |

List only explicitly adopted files or portions. A framework-prefixed name does not establish
ownership. For shared native files identify the owned fields/section and preserve
the rest. Source removals require a prepared decision, not automatic deletion.
Snapshots needed for comparison/recovery must remain retrievable; hashes prove
equality but cannot reconstruct missing contents. Do not hash this record into
itself; preserve its prior contents/absence in the external operation snapshot.

## Relocation mapping, only when selected

Source `MIGRATION.md`, "Relocating an existing import", owns the procedure. This
record is documentation, not an installed runtime schema. Reconcile older records
without a bundle field against their recorded paths and actual files before edits.

| Owned old path/scope | Proposed new path/scope | Prior accepted reference B | Current contents C and candidate N | Destination baseline and agreed action |
| --- | --- | --- | --- | --- |
| `<target-relative old path or unchanged root/native entry>` | `<target-relative new path>` | `<immutable snapshot under its original name>` | `<identities and local/adaptation conflict decision>` | `<contents or absent; create/update/retain/retire>` |

Preserve previous accepted snapshots, names and hashes unchanged. Following
successful checks, record a separate new accepted snapshot and the old/new mapping;
do not reinterpret an old snapshot as evidence for relocated or updated contents.
Include root entries and this record in baseline protection. Operation evidence
identifies actual partial writes and later edits; a proposed mapping alone does
not prove that a move, route switch or retirement succeeded.

## Accepted exceptions

| Rule and affected scope | Accepted exception and reason | Decision reference |
| --- | --- | --- |
| `<rule/path or none>` | `<local contract and why it differs>` | `<canonical decision>` |

Entries/passports point here for provenance; operational commands and local
contracts remain in their local owners. Model assignments remain in model routing
and native configuration. Do not duplicate them or maintain a task checklist here.

## Incomplete operation, when applicable

- Attempted source/selection and operation evidence: `<canonical task reference>`
- File outcome and recovery evidence: `<reference identifying written, untouched and uncertain paths>`
- Unresolved differences: `<reference or concise limits>`

Confirm these statements against actual files when resuming. An old record, even
one marked verified, does not prove that a later interrupted operation succeeded.
