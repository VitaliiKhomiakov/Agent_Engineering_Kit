# Go: verification, security, and performance

Read when choosing checks for changed Go behavior, reviewing an exposed boundary, or investigating performance. Return to the [Go entry](../go.md).


- At changed trust boundaries, review input/resource bounds and exposure of
  secrets or internal error details. Use maintained dependencies and established
  security checks; `govulncheck` can inform affected Go vulnerability analysis,
  but does not prove application security.
- Measure the relevant workload before adding pools, goroutines, reflection
  tricks, or `unsafe` for speed. Use profiles/traces to identify the bottleneck;
  benchmarks should report toolchain, workload, and relevant environment.
- Format changed Go code with `gofmt`. Follow the shared
  [verification policy](../verification.md): use relevant package tests and static
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
