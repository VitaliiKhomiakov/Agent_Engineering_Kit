# Review follow-up

Status: awaiting user review. The authorized R1 correction found by independent
review is complete. Coordinator owns this record; earlier evidence stays historical.

## Outcome and boundaries

Repair the two confirmed Markdown checker false negatives, add the user-selected
offline routing/native agreement check, and exercise the documented update and
recovery decisions in disposable fixtures. Preserve existing local changes.
This is not an installer, scheduler, provider benchmark or client activation.

Instruction root, repository and execution checkout:
`/home/vitalii/Documents/Local_Projects/Agent_Engineering_Kit`.
Canonical task: this document. Execute inline; no applicable saved source model
assignments. Target assignments are evidence only. No Git writes, global changes,
historical evidence changes or writes to the existing AEK_TEST run are authorized.

Baseline: HEAD `0503133c585d61b9ed8b6dfe158b954e91e3db25` plus the initial
status, staged/unstaged patches, file hashes and dirty-file copies in
`/tmp/aek-followup-20261013-wr1d79ho`. Clean tracked originals are reproducible
from this HEAD. New-path absence is recorded there. Earlier review evidence is
`/tmp/aek-review-20261013-bOJTEj`; reuse its unaffected findings and checks.

## Design and acceptance

- The Markdown checker remains a bounded standard-library parser. Unsupported
  indented list content must fail explicitly instead of silently hiding links;
  standalone indented code remains excluded. Detect quoted fences before code
  span removal. Regression tests must demonstrate both prior false negatives.
- A separate read-only CLI checks configured routing schema 2 and the shipped
  Codex file layout. Validate types, pairs, mode, graph, native role definitions
  and concurrency. An explicit default-role input permits comparison of worker
  defaults without inventing a policy mapping. Incomplete, legacy and unsupported
  client inputs cannot produce a successful agreement claim. Preserve custom data.
  Native loading, capabilities, precedence and effective permissions remain unknown.
- Exercise B/C/N, repeat application and interrupted recovery manually in `/tmp`;
  record actual file outcomes and limitations without claiming a general updater.
- Run focused red/green regressions, the maintenance suites, source artifact
  checks, strict typing for affected tools, and a scoped accountable review.
  Inspect new-file whitespace and preserve all baseline user edits.

## Progress

- [x] R1 — Fix Markdown false negatives with regression evidence (correction below).
- [x] R2 — Add and document offline routing/native agreement validation and tests.
- [x] R3 — Record disposable update/recovery exercise and its evidence limits.
- [x] R4 — Complete required checks, scoped review and preservation audit.

R1 evidence: `r1-red.log` has 11 expected failing subcases; `r1-green.log`
passes all 44 checker tests. Source scan: 210 artifacts, zero errors.
The documented subset now explicitly diagnoses indented list blocks.

R2 evidence: all 19 routing tests pass in the final suite. Existing AEK_TEST
read-only saved-agreement check passes, including explicit implementer defaults.
Three disposable code mutations disabling graph, pair and ceiling checks were
caught by their focused tests; source code was never mutated for that exercise.
No native execution was repeated.

R3 evidence: seven actual disposable file scenarios passed. The dated research
record retains definitions, outcomes and limits; raw results and hashes are in
`update-recovery-results.json` under the baseline directory. No general updater
was implemented or claimed. Partial recovery deliberately preserves newer edits.

R4 evidence for the completed implementation:

- `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests`: 107 tests,
  all passed (27.098 seconds); raw output `all-tests.log`.
- Source artifact check: 210 artifacts, zero errors. Explicit maintenance,
  task and research bodies: three artifacts, zero errors.
- The changed artifact checker also passed the existing target's selected bundle
  (61 artifacts) and explicit native/skill/task/routing files (nine artifacts).
  These were read-only instruction checks, not target application execution.
- Documented strict mypy command: success for seven source files, mypy 2.1.0
  in an isolated `/tmp` environment; `mypy.log`. Initial system pip/ensurepip
  were unavailable; authorized temporary installation resolved the gate.
- `git diff --check` and separate new-file whitespace checks passed.
- Scoped review used `scoped.diff` against the original dirty baseline, including
  new files. No material in-scope finding remains. Coordinator review was inline;
  no independent native role execution is claimed.
- `preservation.json` confirms no existing path outside the six intended edited
  files changed. Original specialized-agent edits remain; shared edited files
  have only the intended follow-up additions. No staging, commits or activation.

The user explicitly selected R2 after its optional scope was clarified.
Superpowers planning, inline execution, TDD and completion verification use the
adaptations in `standards/superpowers.md`; this is the sole progress owner.
Remaining limitations: bounded Markdown subset, project-local Codex static
agreement only, manual update decisions, unverified provider/permission telemetry,
and no Claude Code/Cursor semantic adapter. These are documented limits, not
claims that those behaviors were exercised successfully.

## Independent-review correction — 2026-10-13

R1 reopened: a fenced block indented inside a list resets list context, allowing
a later four-space-indented broken link to pass silently. Reproduction and the
earlier fixes' before/after evidence are in `/tmp/aek-independent-review-dkft8ip6`.
The user authorized this bounded correction and regression coverage.

Keep the bounded-parser contract: explicitly reject an indented fence while list
context is active, before resetting that context. Do not introduce a list parser.
Top-level fences and indented fences outside list context must remain accepted,
with code examples excluded from link checks. Document the conservative boundary.

Pre-correction file copies, repository hashes and index patch are preserved in
`/tmp/aek-fence-fix-20261013-_yxwdv1t`. Scope: checker, its regression tests, maintenance
syntax documentation and this canonical task. Existing adoption/routing evidence
and all unrelated changes remain untouched. Execute inline, without Git writes.
Acceptance: demonstrate the failing regression, then pass maintenance tests,
strict typing, affected artifact checks and scoped preservation review.

Correction outcome: the checker reports unsupported indented list content at the
opening fence instead of accepting the document silently. The maintenance syntax
contract explicitly describes this conservative boundary; no full list-container
support is claimed. No change to routing validation or target configuration.

Verification for the corrected state:

- The focused fence tests first failed in all four new nested-fence subcases
  (backticks/tilde fences with two/three spaces). After the fix all four selected
  test methods passed, including standalone and outdented-fence acceptance.
- Full maintenance suite: 109 tests passed (31.797 seconds).
- Strict mypy 2.1.0: seven source files passed using the documented flags.
- Source artifacts: 210 passed. Existing AEK_TEST selected bundle: 61 passed;
  this is a read-only artifact check, not a repeated native run.
- Scoped review against the correction baseline covered all code/test/doc edits;
  only the four intended files changed and the index is unchanged. Earlier
  specialized-agent changes and historical evidence were preserved.

R1 is closed again with these scoped results. The bounded Markdown-parser and
native-runtime evidence limitations above still apply.
