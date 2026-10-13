# Go, Gin, GORM, and code readability implementation plan

Date: 2026-10-13. Current stage: G1, Go style and reproducible tooling.
Status: Stage P and corrected G1 accepted; G1-R1 through G1-R3 are resolved.
Checkpoint: the user authorized committing and pushing the completed G1 scope.
G2-G4 are not authorized or started.

**Goal:** Extend the reusable library with human-readable Go style, explicit
format/lint checks, feature-oriented Gin guidance, and an optional GORM profile.

**Specification:** [Go, Gin, GORM, and code readability](../specs/2026-10-13-go-gin-gorm-style.md).
It owns requirements R1-R5, the input reconciliation, and acceptance A1-A8.
This plan is the sole progress owner. The specification does not track execution.

**Architecture:** Extend existing topic owners, add a Go style topic and Gin
architecture topic, and introduce independent `gorm -> go` catalog selection.
Examples remain conditional, reproducible source artifacts.

**Repository runtime:** Markdown/TOML and Python 3.11+ artifact tooling. Go, Gin,
GORM, SQLite, and golangci-lint are subjects of disposable examples, not new root
runtime dependencies.

## Authorization, locations, and baseline

- The user requested examination of the supplied v2 guideline and preparation of
  final specifications and plans including formatting/readability. Stage P is
  complete and accepted. On 2026-10-13 the user accepted the specification and
  plan and authorized G1 only, followed by a user review checkpoint.
- Execution mode: inline in the current checkout with a user review checkpoint
  after each authorized coherent stage, following
  [work modes](../../standards/work-modes.md).
- No Git writes, worktrees, external publication, or target-project adoption are
  granted. No agent delegation or model reconfiguration is selected. Existing
  session execution is sufficient; a saved model-routing setup is not a planning
  prerequisite under [local skill adaptations](../../standards/superpowers.md).
- Workspace/instruction root and the only repository/execution checkout:
  `/home/vitalii/Documents/Local_Projects/Agent_Engineering_Kit`.
- Canonical store: this root's `docs/plans/` and linked `docs/specs/`; the
  coordinator owns progress. No secondary task store is created.
- Pre-P Git HEAD: `37202a4029fd3870273c24dc26499e38dd3a500a`;
  `git status --short` was empty. Both new document paths were absent.
- Baseline record: `/tmp/aek-go-gin-design-qe38hjl_/baseline.json` records paths,
  prior absence, checkout, HEAD, clean status, and the supplied input hash.
  The specification also retains the source identity and decisions permanently.
- On resumption, preserve the then-current contents/absence of every newly
  affected path before editing. This stage's clean baseline does not describe
  future user edits or authorize replacing them.

## Global constraints

- Work in the current checkout; no staging, commits, branches, or worktrees.
- Instructions, specifications, plans, and example explanations use English.
- Preserve supported target versions, public contracts, and unrelated edits.
- Apply new conventions to new or meaningfully changed code; no blanket rewrite.
- Keep one authoritative owner per rule and conditional read-by-task routes.
- GORM is optional; Go, Gin, and the legacy go-gin aggregate must not require it.
- Examples and tool configurations remain inactive until explicitly adopted.
- Historical evidence retains its original date, versions, and executed scope.
- Run checks proportionate to changed artifacts and behavior; retain project gates.

Use Superpowers `executing-plans` for authorized inline implementation, with
the repository adaptations. Neither the stock skill's commit steps nor its
default review/delegation recipes override this plan's permissions and local rules.

## Stage P: source reconciliation and reviewable documents

- [x] P01 — Read all sections of the supplied guideline, compare current Go/Gin
  owners and catalog/tests, and check relevant official contracts. Outcome:
  specification reconciliation table, corrected caveats, and dated source links.
- [x] P02 — Write the specification and this implementation plan, including
  readability/tooling, optional GORM selection, exact owners, stage dependencies,
  acceptance criteria, compatibility, and execution limits.
- [x] P03 — Verify both documents, inspect their complete new-file contents,
  reconcile specification coverage with G1-G4, and report the review checkpoint.

Current checkpoint: publication of accepted G1. G1.1-G1.4 are complete;
the requested review findings and their verified corrections are recorded below.
G2-G4 remain planned and unchecked.

For each future stage, artifact/profile checks include the documented strict
Python analyzer whenever that stage changes a Python test file. Do not defer a
required stage check to G4. Final acceptance reuses still-valid earlier results.

## G1: Go style and reproducible tooling

Requires: review of Stage P and authorization to implement G1.
Covers: R1-R2; A2-A3 and the Go resource portion of A5/A8.

Create `standards/go/style.md`, `standards/go/examples/style-tooling.md`, and
`docs/research/2026-10-13-go-gin-gorm-style-evidence.md`.
Modify `standards/go.md`, `standards/go/verification.md`,
`standards/catalog.toml`, and `tests/test_profile_selection.py`.

- [x] G1.1 — Establish the single style owner with the exact R1 conventions;
  route from the Go entry and verification topic, linking existing core owners.
  Add both resources to the Go profile and its existing topic expectations.
- [x] G1.2 — Create the complete inactive v2 lint/format configuration and a
  tiny reproducible Go fixture. Use R2's explicit linter/revive sets and
  goimports formatter. Record an exact compatible Go/tool binary/build version
  tuple and any standalone goimports pin; validate it before dependent examples.
- [x] G1.3 — Demonstrate editor formatting and a separate non-mutating CI gate.
  The gate must fail for nonempty formatting/import differences and execution
  errors. Keep generated/vendor handling explicit and package/file scope bounded.
  Document incremental adoption without silently suppressing pre-existing debt.
- [x] G1.4 — Verify configuration, the clean fixture, and representative bad
  inputs; run affected artifact/profile checks and record versions/results.

Concrete checks in a disposable fixture directory:

```sh
golangci-lint version
golangci-lint config verify --config .golangci.yml
golangci-lint fmt --config .golangci.yml --diff
golangci-lint run --config .golangci.yml ./...
go test ./...
```

Confirm command flags against the pinned binary. The fixture's formatting gate
must explicitly evaluate diff output and execution status, rather than assume
the diff/list command exits nonzero for unformatted code. Probe one unformatted
file, a wrongly named initialism, and a meaningful ignored returned error in
separate disposable variants; confirm intended diagnostics and reject tool-load
errors as false positives. Retain only the accepted clean fixture and concise
reproduction/probe instructions. No new test framework is needed.

Outputs consumed later: authoritative style path, catalog resources, validated
tooling recipe and compatibility limits. Other examples reuse these owners.

## G2: Go dependencies and Gin feature/middleware guidance

Requires: G1's style/tooling contract and authorization for G2.
Covers: R3/R5; A4/A7 and Gin resources under A5/A8.

Create `standards/gin/architecture.md` and
`standards/gin/examples/authentication.md`.
Modify `standards/go/architecture.md`, `standards/gin.md`,
`standards/gin/handlers-binding.md`, `standards/gin/routing-middleware.md`,
`standards/gin/verification.md`, `standards/catalog.toml`, and
`tests/test_profile_selection.py`. Extend `standards/gin/runtime.md` or
`standards/gin/examples/middleware.md` only where an actual R5 gap requires it.
Append new evidence to the dated research record without rewriting old runs.

- [ ] G2.1 — Add a labelled schematic feature tree and concrete decision rules
  for direct Handler-to-Store, optional Service, consumer interfaces, and routing
  composition. Keep shared Go package/pattern rules in Go architecture, correct
  `internal` wording, and preserve established project layouts and API names.
- [ ] G2.2 — Extend middleware placement and semantic guidance in existing
  owners: registration timing, public/private routes, explicit dependencies,
  identity versus object authorization, one response owner, and panic/log order.
- [ ] G2.3 — Add a complete standalone authentication-boundary example with
  verifier injection, a typed principal accessor, invalid-credential versus
  verifier-failure errors, and explicit principal/context handoff. Retain
  existing middleware-example behavior; do not turn either into an auth framework.
- [ ] G2.4 — Check the changed executable examples with their pins, format/lint,
  Go tests/vet, and the specific HTTP scenarios below; run affected artifact and
  profile checks. Record what remains illustrative or unverified.

Exercise the constructed router via `httptest`: a public route remains public;
missing/invalid credentials produce 401 and no protected effect; valid identity
reaches the protected operation with the original context/principal; verifier
failure produces sanitized 5xx; a denied permission produces 403; an already
committed body is preserved. Reuse existing access/responder scenarios where
unchanged. Any example claiming panic observation must verify logger/recovery
ordering and the final observed status on panic. A fake verifier tests the
boundary, not cryptographic token validation. Apply `-race` when examples change
concurrent behavior; preserve required project gates.

Outputs: Gin architecture/task routes and verified HTTP boundary examples; no
new persistence dependency and no automatic GORM route in the legacy aggregate.

## G3: independent GORM profile and database-backed example

Requires: R4 and G1's style/tooling contract; authorization for G3.
Execute after G2 by default to keep one active stage, although the GORM profile
must remain usable without Gin. Covers: R4; A5-A6/A8.

Create `standards/gorm.md`, `standards/gorm/stores-models.md`,
`standards/gorm/queries-lifetime.md`,
`standards/gorm/transactions-migrations.md`,
`standards/gorm/verification.md`, and `standards/gorm/examples/store.md`.
Modify `standards/catalog.toml`, `standards/catalog.md`, `README.md`, and
`tests/test_profile_selection.py`; append the dated research record.

- [ ] G3.1 — Add the conditional entry and four topics from R4, distinguishing
  local architectural policy, Traditional/Generics API contracts, and
  dialect-specific behavior. Route shared Go rules instead of copying them.
- [ ] G3.2 — Add a small Traditional-API Store fixture with complete named
  source/test blocks, a pinned manifest, and a disposable SQLite database.
  Start from GORM v1.30.0 and SQLite driver v1.6.0; confirm the resolved graph and
  compatible Go/CGO prerequisites before accepting this reproduction contract.
  Include lookup, an explicit allowed zero-value update, and an atomic two-write
  operation. Keep Gin out of this fixture.
- [ ] G3.3 — Add and run focused DB-backed tests for absent lookup, valid zero
  updates, rejected privileged field updates, uniqueness/conflict translation,
  independent sequential/concurrent query state, and rollback after a failed
  second write. Verify stored rows after rollback, not only returned errors.
  Exercise request cancellation; check race safety where the environment supports
  it. State SQLite-specific row-count/error behavior and limits explicitly.
- [ ] G3.4 — Register `gorm -> go` with every new resource, update the profile
  selection table/README, and extend existing selection tests. Verify independent
  and combined closures and the complete GORM example; record versions and limits.

The example owns an explicit fixture schema setup; if it uses AutoMigrate, label
that setup as disposable-test-only. It must not prescribe production startup
migrations. A successful rollback test does not establish distributed atomicity,
all isolation levels, or PostgreSQL/MySQL compatibility.

Profile tests must assert: Go excludes Gin/GORM; Gin includes Go but excludes
GORM; GORM includes Go but excludes Gin and database/deployment-specific profiles;
Gin plus GORM includes both without the legacy aggregate; legacy go-gin retains
its former resources/anchors and excludes GORM. Extend existing TOPICS/test cases
instead of introducing a parallel checker. The new exclusion cases protect
selection behavior, not mere filename existence.

## G4: final consistency and portable bundle acceptance

Requires: accepted results from G1-G3 and authorization for the final stage.
Covers: A1-A8 as an integrated library change. Modify only scoped findings,
the existing plan, and the new research record when required.

- [ ] G4.1 — Reconcile the full diff against the specification and input matrix:
  one owner per rule, all resource routes, no forced ORM/service/repository,
  preservation of existing shared policy and historical evidence.
- [ ] G4.2 — Check prepared disposable bundles for `go`, `gin`, `gorm`,
  `gin + gorm`, and `go-gin`, adapting optional history/cross-profile links per
  the catalog contract. Verify all required links without copying unrelated
  profiles, activating templates, or changing a consuming project.
- [ ] G4.3 — Complete remaining required artifact/profile/static checks, reuse
  still-valid example evidence, and report acceptance, limits, and the user
  checkpoint. No automatic commits or adoption follow completion.

Run `python3 tools/check_instruction_artifacts.py` for the integrated source
and explicitly include changed research/spec/plan files because `docs/` bodies
are opt-in. Run
`python3 -m unittest discover -s tests -p 'test_profile_selection.py'` when the
catalog/profile changes require it. If that Python test file changes, run the
documented strict analyzer scoped to the changed file and relevant imports under
[maintenance checks](../maintenance/verification.md#artifact-checker).
Run `git diff --check` and separately inspect/check new files. Do not run unrelated
application stacks or unchanged checker regression suites by default.

## Review focus and evidence limits

| Failure mode | Owning item and evidence |
| --- | --- |
| Lint passes while formatting is unchecked, or tool failure is mistaken for a lint finding | G1.4: clean and negative format/lint probes, config validation |
| Style guidance renames a wire field or forces layers into simple CRUD | G1.1/G2.1 and G4.1: scope/contract review |
| Group middleware added too late leaves a private endpoint reachable | G2.4: actual route registration and denied-route tests |
| Panic unwinding or a late error corrupts response/observed status | G2.4: existing committed-response test and explicit panic-order scenario where claimed |
| Zero-value updates are lost, query state leaks, or transaction uses the root DB | G3.3: DB-backed state assertions and concurrent query isolation |
| GORM silently becomes mandatory in unrelated/legacy selections | G3.4/G4.2: closure regressions and prepared bundles |

Stage P source review is complete. G1 tooling/example execution is recorded below;
Gin/GORM examples remain future work in G2/G3. Exact tooling pins were selected
and validated in G1.2 against the actual fixture toolchain, not guessed from a
release name. No consuming target versions are changed. An unavailable required
tool/database check remains pending with its
reason; it cannot be reported as passing or replaced with a weaker claim.

## Stage evidence and handoff

P01: local guideline and owner inspection; official Go/Gin/GORM/golangci-lint
source review on 2026-10-13, linked in the specification. No runtime execution.

P02: both documents created from a recorded absent baseline. Scope is limited to
these two files. Source guideline and active library standards are unchanged.

P03: scoped artifact checker passed (`Checked 2 artifacts; 0 error(s)`).
`git diff --check` passed; both complete new files were inspected separately and
checked for trailing whitespace and final newlines. The identical Global
constraints blocks and R1-R5 to G1-G4 mapping were checked; A1-A8 have explicit
owning stages and verification. No material unresolved design finding remains.
No runtime/linter/database check was executed in Stage P.

At the Stage P checkpoint, implementation was unstarted and G1 was proposed next.
The user's subsequent acceptance and G1 execution are recorded below; the P
evidence above still describes only the original two-document check.

## G1 execution record

Authorization: user accepted Stage P and requested G1 inline in this checkout,
without commits or worktrees. The two untracked Stage P documents are preserved
in the pre-edit baseline; the specification remains unchanged.

Baseline: `/tmp/aek-go-style-g1-kdoeill7/baseline.json` and its `baseline/`
scoped copies record the current HEAD, status and original contents/absence of
all G1 paths. At resumption only the specification and plan were untracked.

Pre-flight: G1.1 supplies style routes/resources; G1.2 supplies the pinned
configuration consumed by G1.3-G1.4 and later examples. No interface conflict
with R1-R2 was found. Checks are batched at G1 except early tool/config validation
to settle version compatibility. Coordinator review is sufficient for this
bounded documentation/tooling stage under the risk-based review policy; no
delegation is selected.

G1.1: added the single style owner and Go entry/verification routes; registered
both new Go resources and extended existing profile topic expectations. Shared
naming, control-flow, error semantics, and size/package owners remain authoritative.
Artifact/profile verification is recorded under G1.4.

G1.2: the complete inactive configuration/fixture uses official Go 1.26.1 and
golangci-lint 2.11.3 built with Go 1.26.1 (commit `6008b81b`). Archive hashes
matched official manifests. Build metadata confirmed bundled x/tools v0.42.0,
Staticcheck v0.7.0, Revive v1.15.0, and errcheck v1.10.0. Configuration validation
passed; the initial clean lint run reported `0 issues`. The standard validation
command loads the official v2.11 JSON schema and needed network access outside
the DNS-restricted sandbox. No tools were installed in the repository.

G1.3: documented bounded edit/save commands and a separate non-mutating shell
gate. Spacing/import variants failed then passed after formatting; hashes
confirmed checks did not rewrite source. The pinned formatter returns 1 for
differences, but the wrapper also rejected a simulated diff with exit 0 and
propagated an empty-output tool failure (7). Invalid YAML failed with status 3.
Generated/vendor exclusions and incremental adoption remain explicit.

G1.4: all three clean Go tests passed; naming and ignored-error
variants produced the intended Revive/errcheck diagnostics, without tool-load
errors. The 33 existing profile-selection tests passed with the new Go topic
expectations. Strict mypy 2.1.0 passed on `tests/test_profile_selection.py` and
its relevant `tools/check_instruction_artifacts.py` import (2 source files).
The scoped artifact command checked all 8 affected Markdown/TOML documents,
including the accepted specification, this plan, and the new research record:
`Checked 8 artifacts; 0 error(s)`. `git diff --check` passed; separate new-file
checks covered all five untracked documents, trailing whitespace, and final
newlines. All five delivered fixture blocks match the executed source exactly.

Coordinator review covered the actual tracked diff, full new-file contents, and
plan delta against the pre-G1 copies. R1-R2 and acceptance A2-A3 plus the G1
resource/reference portions of A5/A8 are satisfied. The style owner routes to
shared policies, all existing profile dependencies/legacy anchors remain intact,
and the configuration remains inactive. No material in-scope finding is open.
Review aligned the reproduction command with the already-tested `GOWORK=off`
environment; this changed no fixture input or executed runtime condition.

Detailed commands, versions, diagnostics, and limits are in the
[dated evidence](../research/2026-10-13-go-gin-gorm-style-evidence.md).
Runtime evidence is limited to the pinned Linux tuple. Editor integration and
generated/vendor workflows are not claimed as executed. Temporary fixture/tool
directories and caches were removed after recording evidence; pre-edit copies,
source-review files, and probe logs remain under the baseline directory through
handoff. HEAD and the accepted specification are unchanged; no Git writes were
performed. G1 is ready for user review. Proposed next stage: G2, only after the
user authorizes it.


## G1 requested review: 2026-10-13

The user requested a review for inconsistencies, inaccuracies, and excessive
instructions. This review changed only plan status/evidence; no standards or
fixture fixes were applied. The pre-review plan is preserved at
`/tmp/aek-g1-review-20261013/plan-before-review.md`.
The earlier execution record above describes the checks completed before these
additional cases were identified; its completion assessment is superseded here.

- **G1-R1 (important, G1.3/G1.4): formatter errors can pass the gate.** With the
  exact pinned binaries/configuration, `greeting.go` containing `package greeting`
  and an unfinished `func Broken(` produced a goimports parse warning on stderr,
  empty stdout, and shell-gate exit 0. The pinned MetaFormatter logs formatter
  errors as warnings and retains the input; the wrapper's stdout/exit checks do
  not detect this case. Correct error handling and add this negative scenario.
- **G1-R2 (important, G1.3/G1.4): the CI command sequence can hide failed lint.**
  Running the published three CI commands under ordinary `sh` on the `userId`
  variant emitted Revive's naming error, then passed `go test`, and exited 0.
  Provide a separate CI block with fail-fast behavior; keep the mutating editing
  command outside it. The child gate's `set -eu` does not configure its parent.
- **G1-R3 (minor, optional simplification): errcheck adds checks for infallible
  APIs.** `disable-default-exclusions: true` plus `check-blank: true` rejects
  `_, _ = b.WriteString("ok")` for a concrete `bytes.Buffer`, whose contract
  guarantees a nil error. Preserve narrow exceptions for genuinely infallible
  APIs so the baseline does not encourage unreachable branches or repeated
  suppressions; retain checks for meaningful writer errors.

The three observations were reproduced in separate temporary copies using Go
1.26.1 and golangci-lint 2.11.3; both archive hashes matched the G1 pins. Results
are retained in `/tmp/aek-g1-review-20261013/probes.json`, with the probe script
and relevant downloaded source. Review runtime/tools/caches were removed. Existing
G1 test results remain valid for their original cases; they did not cover these
new failure modes. No unrelated suites or application stacks were rerun.
G1.3/G1.4 remain open pending corrections and focused verification. G2 is not started.


## G1 review corrections: 2026-10-13

The user authorized all three requested improvements. Work remains inline in the
current checkout, without Git writes, worktrees, or progression to G2. Baseline:
`/tmp/aek-g1-fixes-pop4wr3w/baseline.json` and `baseline/` preserve the current
example, evidence, and plan before edits, plus hashes of the other local changes.

- [x] G1-C1 — Reject formatter diagnostics even when its exit status is zero;
  preserve diff/status handling and non-mutating behavior (G1-R1).
- [x] G1-C2 — Separate editing from CI and make the CI block stop on the first
  failed check, including under ordinary POSIX sh (G1-R2).
- [x] G1-C3 — Allow explicitly named infallible buffer/builder write methods
  without suppressing meaningful writer errors (G1-R3).

G1-C1: the gate captures both output streams in its existing temporary file and
rejects diagnostics, diffs, and nonzero status. The pinned parser-warning case
now exits 1; invalid YAML still exits 3. Stand-in status/output cases and source
hash checks passed without adding a formatter or matching diagnostic wording.

G1-C2: editing and CI have separate command blocks; the CI block starts with
`set -eu`. Its exact published commands passed on the clean fixture and stopped
before `go test` on spacing, import, and naming failures under ordinary `sh`.

G1-C3: eight explicit `bytes.Buffer`/`strings.Builder` write-method exclusions
allow guaranteed-nil errors without restoring broad defaults. A positive test
exercising all eight calls passed lint and tests. Bare/blank-discarded
`fmt.Fprintf` and blank-discarded `io.Writer.Write` still produced errcheck errors.

The existing review probes supplied the failing baseline. Corrected configuration
validation, clean lint, all three original Go tests, and focused regression
probes passed with the same pins. New evidence is appended to the
[dated record](../research/2026-10-13-go-gin-gorm-style-evidence.md#g1-review-corrections-executed-on-2026-10-13).
Unchanged catalog/profile/Python checks retain their original G1 evidence.

G1.4 correction verification: the scoped artifact checker passed for the three
changed documents (`Checked 3 artifacts; 0 error(s)`). `git diff --check` and
separate new-file whitespace/final-newline checks passed. All five delivered
fixture blocks and the CI block match the executed inputs. Coordinator review
covered the complete correction diff against the pre-correction copies; no
material in-scope issue remains open. These results supersede the requested
review's pending status above, while preserving its original observations.

Hashes confirm the accepted specification and all unrelated local changes are
unchanged. HEAD and Git status match the pre-correction baseline. Only the
example, evidence record, and this plan changed during corrections. Temporary
runtime/tools/caches were removed after recording results; baseline and probe
logs remain through handoff. G1 is complete and awaits user review; G2-G4 have
not started. No commits, staging, branches, or worktrees were created.

## G1 publication authorization: 2026-10-13

After reviewing the corrected G1 result, the user requested a commit and push.
This authorizes staging the nine Stage P/G1 files, one commit in the current
`main` checkout, and a normal push to its existing upstream `origin/main`.
It supersedes the earlier no-Git-write restriction for this handoff only;
G2-G4, new branches, and worktrees remain outside the authorized scope.

The pre-publication plan is preserved at
`/tmp/aek-g1-publish-xigjw1lu/plan-before-publish.md`. Implementation inputs and
recorded checks are unchanged; this update records authorization only. The
commit identifier and push outcome are reported in the user handoff.
