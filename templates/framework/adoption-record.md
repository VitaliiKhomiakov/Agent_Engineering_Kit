# AgentsFramework adoption record

<!-- Inactive template. Adapt to target .agents-framework/adoption.md only during
authorized application. Preparation keeps the proposed record outside the target.
Remove guidance/placeholders when filling. Paths below are relative to the named
target root unless explicitly identified as source or external recovery locations. -->

Read only for framework import, update or recovery. This record owns provenance
and managed scope; the canonical adoption task owns decisions and progress.

## Identity and agreement

- Target instruction root and selected projects: `<actual roots>`
- Client/version: `<selected client; unknown version stays unknown>`
- Canonical adoption task: `<reachable location; no copied task ledger>`
- State: `<prepared | applied but unverified | verified | partial>`
- Candidate source: `<accessible location + revision or selected-content manifest>`
- Candidate profiles and layout: `<IDs, target routes and any adapted locations>`
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

List only explicitly adopted files or portions. An `af-` name does not establish
ownership. For shared native files identify the owned fields/section and preserve
the rest. Source removals require a prepared decision, not automatic deletion.
Snapshots needed for comparison/recovery must remain retrievable; hashes prove
equality but cannot reconstruct missing contents. Do not hash this record into
itself; preserve its prior contents/absence in the external operation snapshot.

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
