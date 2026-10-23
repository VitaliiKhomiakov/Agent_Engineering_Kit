# Go: verification, security, and performance

Read when choosing checks for changed Go behavior, adopting formatter/linter
configuration, reviewing an exposed boundary, or investigating performance.
Return to the [Go entry](../go.md).

## Formatting and lint adoption

- Apply [Go style](style.md); it owns readability and formatting conventions.
  Inspect the existing formatter, lint configuration/version, module roots,
  build tags, generated sources, and CI before changing tooling. Preserve working
  compatible conventions and supported target versions. A v1-to-v2 golangci-lint
  migration is explicit work, not an incidental style edit.
- The [inactive tooling example](examples/style-tooling.md) supplies a small,
  explicit new-project baseline and a validated version tuple. Adopt it only for
  the selected project; do not install it at this instruction library's root.
  Pin the Go toolchain and linter binary/build, and validate the configuration
  with that binary. Its build toolchain and bundled analyzers must support the
  project's Go version; a release label alone does not prove compatibility.
- Use reproducible editor import/format settings and a separate non-mutating CI
  gate. `golangci-lint run` does not run the formatting gate. A diff/list command's
  success is insufficient: fail on nonempty differences and on tool errors.
- Scope formatting to selected source files and lint/tests to affected packages
  in their module roots, retaining mandatory CI. Review generated/vendor handling
  explicitly; an issue exclusion does not necessarily prevent package loading.
- Adopt incrementally in existing repositories. Record existing debt separately;
  any temporary baseline or suppression needs a narrow scope, reason, and removal
  condition. Do not silently hide debt with new-issues-only filtering, broad
  exclusions, disabled checks, or a repository-wide reformat.
- Review overlapping diagnostics when selecting or updating analyzers. Give each
  duplicated style diagnostic one owner while retaining correctness checks.
  Configuration validation and negative probes in the example demonstrate
  enforcement; linters do not replace review of names, contracts, and readability.

## Readability acceptance

Use this Go check within the shared
[readability acceptance](../verification.md#readability-acceptance), which owns
inspection after formatting, fixing, recording and acceptance by role. The detailed
requirement and examples have one owner:
[Go flow and spacing](style.md#readable-flow-and-spacing).

Identify the changed functions and meaningfully affected surrounding code, and
determine their steps by purpose using that rule; do not expand a local change into
a review or reformat of unrelated functions. A concise evidence statement can read:
`cmd/api/main.go: livenessRouter — creation, configuration, registration and
final-result groups checked; no violations.` Use actual project paths, and report
unresolved violations or accepted exceptions. Reuse valid evidence for unchanged or
moved code under [evidence reuse](../verification.md#reuse-evidence-before-repeating-work).

## Behavior, security, and performance

- At changed trust boundaries, review input/resource bounds and exposure of
  secrets or internal error details. Use maintained dependencies and established
  security checks; `govulncheck` can inform affected Go vulnerability analysis,
  but does not prove application security.
- Measure the relevant workload before adding pools, goroutines, reflection
  tricks, or `unsafe` for speed. Use profiles/traces to identify the bottleneck;
  benchmarks should report toolchain, workload, and relevant environment.
- Follow the shared [verification policy](../verification.md): use relevant package tests and static
  checks, adding cases for material uncovered behavior, not file/constructor
  presence. Check exports, imports, and route registration after package moves.
- Test domain failures as well as success; check that rejected transitions leave
  state intact. At an external boundary, cover the real error/status/transaction
  contract at the appropriate level rather than proving a mock was called.
- For changed concurrent behavior, check cancellation, ownership, and completion;
  use `go test -race` where the environment supports it. A clean race run covers
  executed paths and is not proof against all races, deadlocks, or goroutine leaks.
  Coordinate concurrent tests with events, using timeouts as failure bounds.
- Use fuzzing for meaningful parser/input properties and benchmarks for an actual
  performance question. Neither is required for every edit. `testing.B.Loop`
  requires Go 1.24+; preserve older supported versions when choosing a harness.

See [security practices](https://go.dev/doc/security/best-practices),
[diagnostics](https://go.dev/doc/diagnostics),
[race detection](https://go.dev/doc/articles/race_detector),
[fuzzing](https://go.dev/doc/security/fuzz/), and
[`testing`](https://pkg.go.dev/testing@go1.26.1).
