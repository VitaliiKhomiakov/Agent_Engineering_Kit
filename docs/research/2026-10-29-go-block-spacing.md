# Go completed-block spacing: dated follow-up evidence

Date: 2026-10-29. The [canonical task](../plans/2026-10-29-go-block-spacing.md)
owns the approved scope and progress. This record extends, rather than rewrites,
the [earlier guard-spacing run](2026-10-29-go-spacing.md).

## Reviewed contracts and diagnosis

| Source | Relevant contract |
| --- | --- |
| [gofmt documentation](https://pkg.go.dev/cmd/gofmt) | Standard formatting does not supply configurable logical-block spacing; `-r` rewrites Go expressions, not whitespace rules. |
| [WSL 5.6.0 checks](https://github.com/bombsimon/wsl/blob/v5.6.0/CHECKS.md#after-block) | `after-block` separates a completed block from following code. A direct error guard can remain adjacent to a `defer` referring to the preceding assignment. |
| [WSL 5.6.0 implementation](https://github.com/bombsimon/wsl/blob/v5.6.0/wsl.go) | Nested bodies are visited; `checkNewlineAfterBlock` handles the following statement, attached branches and the related-`defer` exception. The exception checks variable intersection, not cleanup intent. |
| [golangci-lint 2.11.3 manifest](https://github.com/golangci/golangci-lint/blob/v2.11.3/go.mod) and [configuration reference](https://github.com/golangci/golangci-lint/blob/v2.11.3/.golangci.reference.yml) | The existing fixture includes WSL 5.6.0 and configures its check set. No dependency or toolchain upgrade is required. |

Requiring this check and narrowing the `defer` exception to cleanup are local
engineering policy. They do not imply a Go language requirement or universal
community preference. The previous configuration intentionally enabled only
`if` and `err`; its declared limits did not enforce the newly selected boundary.

The preceding investigation used an exact extraction of the reported CIDR loop,
Go 1.26.1 and standalone WSL 5.6.0. `gofmt` accepted the compact loop. `if,err`
rejected the missing line before parsing; its auto-fix added that line but left
the missing separator before `append`, after which the same gate passed.
`after-block` rejected the remaining gap and accepted the two-separator layout.
It also rejected the old guard-plus-configuration layout, which is why the rule
and router example change together. Those diagnostic artifacts are retained at
`/tmp/aek-go-loop-or8f9e5r/`; they are not a full application or Go 1.27.3 check.

## Current fixture qualification

The unchanged fixture pins are Go 1.26.1, linux/amd64, and official golangci-lint
2.11.3 built with go1.26.1, commit `6008b81b81c690c046ffc3fd5bce896da715d5fd`,
including WSL 5.6.0. The release archive matched the existing SHA-256 pin before
extraction. All dependencies, caches and generated fixtures are task-local under
`/tmp/aek-go-block-spacing-fnsq1vu7/runtime/`.

`golangci-lint config verify` accepted the updated configuration against the
official v2.11 schema. The six named fixture files, CI block and cleanup probe
are extracted directly from the revised tooling example; reproduction commands
remain owned there.

| Check | Observed result |
| --- | --- |
| Exact CI block on the clean fixture | Formatting, every configured linter and the existing greeting tests passed. |
| Missing separator before parsing, before appending, after the outer loop, or both internal loop separators | Formatting passed; CI rejected each variant with `after-block` and stopped before tests. Non-mutating commands preserved source hashes. |
| Earlier `if,err` configuration on the append-only variant | Exit 0 under the same pinned integration, confirming the previous coverage gap. |
| Adjacent independent/same-input guards and detached direct error check | Rejected by WSL; these existing requirements remain enforced. |
| Scoped repair of all seven spacing variants | Exit 0, with only blank lines changed. Repaired CIDR variants exactly matched the clean source; ordinary CI passed afterward. |
| Attached `else if`/`else` chain | Formatting and full CI passed without separating the branches. |
| Resource passed explicitly to deferred cleanup after a direct error guard | Formatting and full CI passed with no separator before `defer`. Error handling inside the deferred function remained intact. |
| An unrelated deferred log before the real cleanup | Rejected with `after-block`; adding the separator through repair preserved cleanup and passed formatting/CI. |
| Resource captured only inside the deferred closure | Rejected without a separator. Whitespace-only repair added it, after which formatting and full CI passed. |

The initial cleanup candidate used implicit capture and failed the intended
positive probe. Inspection of WSL's identifier collection confirmed that block
bodies are skipped for this intersection check. The rule and executable probe
now state the explicit receiver/argument boundary, and the initial rejection is
retained as evidence of the capture limitation. No analyzer suppression, source
behavior change or tool upgrade was used to hide that finding.

The task logs contain 44 command invocations, including negative controls and
the diagnosed initial cleanup failure. A forwarding wrapper recorded whether
`go test` was reached, then invoked the real compiler; no compiler/linter was
mocked. Unchanged fixture and loop results were reused after the cleanup-only
correction. Earlier naming, writer-error and malformed-input probes remain in
their historical record; they are not represented as new executions here.

## Existing examples and source-library verification

- Four blank lines were added across the Gin binding, LangChainGo and Go OTel
  examples. Nonblank document lines and scanned Go tokens, including comments
  and inserted semicolons, remained identical. APIs, versions and behavior are
  unchanged; their dependency-backed runtime suites were not rerun.
- All 18 current non-manifest Go source blocks passed Go 1.26.1 formatting and
  syntax checks. Complete files retained package comments; partial excerpts used
  temporary wrappers for parsing. AST inspection confirmed completed-block
  separators in the non-tooling examples; the tooling fixture and cleanup
  exceptions used the actual typed lint runs above.
- All 268 default instruction artifacts and both new documents passed artifact
  checks. `git diff --check` and separate new-file whitespace/link inspection
  passed. The canonical task records the scoped coordinator review.

Baselines, runners, fixture copies and logs are retained under
`/tmp/aek-go-block-spacing-fnsq1vu7/` through handoff. Downloaded tools, extracted
runtime variants and build/lint caches are removed after evidence capture.

## Evidence limits

The parser helper is a spacing fixture, not a complete trusted-proxy policy.
Example compilation and style acceptance do not validate proxy trust semantics.
Semantic grouping between ordinary statements still requires source review.
The check does not recognize every compound or wrapped error predicate.

The separate Medical & Pharmaceutical Intelligence application and its imported
instructions are outside this maintenance stage. No consumer migration, editor
save-hook qualification, application build or newer toolchain validation is
claimed. Historical dependency-backed runs of existing examples remain historical.
