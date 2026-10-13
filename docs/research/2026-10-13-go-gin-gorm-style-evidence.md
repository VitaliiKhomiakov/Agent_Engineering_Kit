# Go, Gin, GORM, and style: dated implementation evidence

Date: 2026-10-13. This record separates official-source review from executed
checks. The [specification](../specs/2026-10-13-go-gin-gorm-style.md) owns the
requirements; the [plan](../plans/2026-10-13-go-gin-gorm-style.md) owns progress.
This first entry covers G1 only. It does not replace earlier Go/Gin research or
claim any new Gin/GORM/database execution. Append later stage evidence with its
own versions and scope.

The original G1 execution below predates the requested review corrections. The
[appended correction run](#g1-review-corrections-executed-on-2026-10-13) records
validation of the revised gate, CI commands, and errcheck exclusions.

## G1 source review

| Official source | Bounded conclusion used in G1 |
| --- | --- |
| [Go Code Review Comments](https://go.dev/wiki/CodeReviewComments) and [Effective Go formatting](https://go.dev/doc/effective_go#formatting) | Basis for the accepted R1 conventions: Go formatting, initialisms, receiver names, comments, error strings, and readable control flow. These are guidance, not a new language grammar or fixed line quota. Effective Go is historical guidance. |
| [Go toolchain selection](https://go.dev/doc/toolchain) | A module's Go directive and actual selected compiler are distinct; the fixture explicitly selects a local pinned toolchain. |
| [golangci-lint v2.11.3 manifest](https://github.com/golangci/golangci-lint/blob/v2.11.3/go.mod) | Versioned dependency contract for the bundled tools; actual release-binary metadata was also inspected. |
| [v2.11.3 configuration reference](https://github.com/golangci/golangci-lint/blob/v2.11.3/.golangci.reference.yml) | v2 linter/formatter sections, explicit rule selection, generated-file modes, exclusions, and optional goimports local prefixes. |
| [v2.11.3 Staticcheck integration](https://github.com/golangci/golangci-lint/blob/v2.11.3/pkg/golinters/staticcheck/staticcheck.go) and [check descriptions](https://staticcheck.dev/docs/checks/) | The integration combines multiple analyzer families. Its existing style exclusions were retained, with ST1005/ST1006 additionally assigned to Revive; SA correctness checks stay enabled. |
| [v2.11.3 Revive integration](https://github.com/golangci/golangci-lint/blob/v2.11.3/pkg/golinters/revive/revive.go) | Explicit rules with default/all expansion disabled give a bounded rule set; execution confirmed the effective five-rule list. |
| [v2.11.3 formatter command](https://github.com/golangci/golangci-lint/blob/v2.11.3/pkg/commands/fmt.go) and [CLI documentation](https://golangci-lint.run/docs/configuration/cli/) | Formatting is a separate command, with file/directory scope and non-mutating diff mode. Exit behavior was measured rather than inferred from the flag name. |
| [Toolchain compatibility FAQ](https://golangci-lint.run/docs/welcome/faq/) | Check both the linter's build Go version and its analyzer support against the target Go version. A newer release alone does not authorize a consuming-project upgrade. |

Live documentation was reviewed on the date above; versioned source links and
actual execution bound the claims. The new owner routes, adoption scope, narrow
lint baseline, and shell gate are local engineering policy/implementation, not
claims that Go mandates those choices.

## G1 executed environment

The five named fixture blocks in
[style-tooling](../../standards/go/examples/style-tooling.md) were extracted into
`/tmp/aek-go-style-g1-kdoeill7/runtime/fixture`. No root Go module, dependency,
active linter configuration, editor integration, or CI workflow was installed.

| Component | Observed value |
| --- | --- |
| Platform/compiler | Linux amd64; `go version go1.26.1 linux/amd64` |
| Official linter | `golangci-lint 2.11.3`, built with `go1.26.1`, commit `6008b81b81c690c046ffc3fd5bce896da715d5fd`, build time `2026-03-10T10:25:44Z` |
| Bundled formatter/analysis tools | `golang.org/x/tools v0.42.0` |
| Staticcheck / unused | `honnef.co/go/tools v0.7.0` |
| Revive | `github.com/mgechev/revive v1.15.0` |
| Errcheck | `github.com/kisielk/errcheck v1.10.0` |
| Binary build metadata | `CGO_ENABLED=0`, `vcs.modified=false`; inspected with `go version -m` |
| Fixture environment | `GOTOOLCHAIN=local`, `GOWORK=off`; task-local Go/module/linter caches and `GOPATH` under the temporary runtime directory |
| Python analyzer | Existing external mypy 2.1.0; no analyzer installation in the repository |

The official Go archive SHA-256 was
`031f088e5d955bab8657ede27ad4e3bc5b7c1ba281f05f245bcc304f327c987a`;
the linter archive SHA-256 was
`87bb8cddbcc825d5778b64e8a91b46c0526b247f4e2f2904dea74ec7450475d1`.
Both matched their official download manifests before extraction. Go's download
JSON supplied its checksum; a `.sha256` suffix URL returned HTML and was rejected.
This tuple reproduces this example, not a support matrix for other targets.

## G1 executed checks

The [example](../../standards/go/examples/style-tooling.md#editing-and-non-mutating-checks)
owns reproduction commands and
[negative probe mutations](../../standards/go/examples/style-tooling.md#negative-probes).
Each negative case used a separate disposable copy. Commands were run from the
fixture module root, with the exact pinned binaries on `PATH`.

| Command or scenario | Observed result |
| --- | --- |
| `golangci-lint version`, `go version`, `go version -m <linter>` | Pins/build/dependencies above confirmed |
| `golangci-lint config verify --config .golangci.yml` | Exit 0 against the official v2.11 schema |
| Clean `sh scripts/check-format.sh greeting.go greeting_test.go` | Exit 0, empty diff, source unchanged |
| `golangci-lint run --config .golangci.yml ./...` | Exit 0, `0 issues` |
| Same lint run with `GL_DEBUG=revive,staticcheck` | Exactly five Revive rules; 152 Staticcheck checks, including all SA checks and excluding the eight named ST checks; exit 0 |
| `go test -v ./...` | Three tests passed: successful greeting, blank-ID rejection without output, and wrapped writer error |
| Spacing violation | Raw `fmt --diff` and shell gate both exited 1 with the intended diff; source unchanged |
| Unused import | Raw `fmt --diff` and gate both exited 1 with import removal; source unchanged |
| Editing both formatting variants | `fmt` exited 0 and rewrote the selected file; subsequent gates exited 0 |
| `userId` parameter | Lint exit 1; one Revive `var-naming` diagnostic recommending `userID` |
| Bare `fmt.Fprintf` call | Lint exit 1; one `errcheck` diagnostic for its unchecked error |
| Invalid YAML | Gate exit 3 from configuration loading, even with empty stdout; source unchanged |
| Shell gate with temporary tool stand-ins | A diff on stdout with tool exit 0 produced gate exit 1; empty stdout with tool exit 7 preserved exit 7 |
| Profile selection unittest suite | 33 tests passed, including Go, Gin, and legacy Go/Gin closures with the new Go resources |
| Strict mypy | No issues in the changed profile test and relevant checker import (2 source files) |

Hash comparisons confirmed that clean, lint, diff, and error-path checks did not
rewrite fixture files. Naming/ignored-error probes were formatted first and
produced their intended diagnostics, without package-load or typecheck failures.
The stand-ins verify only the shell gate's status/output handling; they are
separate from the real pinned-binary probes.

The normal `config verify` command needs network access to fetch the official
schema. Initial sandbox DNS failure was not treated as validation; the successful
run used permitted network access with the same pinned toolchain/configuration.
The fixture itself uses only the standard library and needed no module downloads.

Library checks used:

```sh
python3 -m unittest discover -s tests -p 'test_profile_selection.py'
/tmp/aek-portable-roles-mypy/bin/python -m mypy --strict --disallow-any-explicit --disallow-any-unimported --python-version 3.11 --explicit-package-bases --cache-dir /tmp/aek-go-style-g1-kdoeill7/runtime/mypy-cache tools/check_instruction_artifacts.py tests/test_profile_selection.py
```

Artifact/whitespace checks and scoped coordinator review are recorded in the
canonical plan after completion. Logs and the pre-edit baseline remain outside
the repository under `/tmp/aek-go-style-g1-kdoeill7/` through handoff. Temporary
fixture/tool/dependency caches are removed after recording the results; these
paths are execution provenance, not portable reproduction prerequisites.

## Limits and later stages

Only the pinned Linux tuple and stated probes were executed. Format-on-save
integration, other operating systems, every rule/exception, generated/vendor
workflows, multiple module roots, and build-tag combinations were not tested.
Generated/vendor handling is explicit configuration and guidance, not an executed
generator scenario. No claim is made that formatting or linting proves readability,
public API compatibility, or security. No consuming project's supported versions
were changed. G2-G4 require their own authorization and evidence.

## G1 review corrections executed on 2026-10-13

Scope: G1-R1 through G1-R3 from the requested review, with no version or fixture
API changes. The corrected five named blocks were extracted from the example
into `/tmp/aek-g1-fixes-pop4wr3w/runtime/fixture`; its CI block was saved as
`/tmp/aek-g1-fixes-pop4wr3w/ci.sh`. Both official archive hashes matched the pins
above. Runs used the same
Linux amd64 Go 1.26.1 / golangci-lint 2.11.3 tuple, `GOTOOLCHAIN=local`,
`GOWORK=off`, and task-local caches. No tools or active configuration were added
to the repository.

Source review confirmed that the pinned
[formatter error path](https://github.com/golangci/golangci-lint/blob/v2.11.3/pkg/goformatters/meta_formatter.go)
logs formatter errors as warnings and retains the input. The Go 1.26.1
[`bytes.Buffer`](https://pkg.go.dev/bytes@go1.26.1#Buffer.Write) and
[`strings.Builder`](https://pkg.go.dev/strings@go1.26.1#Builder.Write) contracts and
their installed standard-library source confirm nil errors for the eight named
write methods. The
[errcheck v1.10.0 exclusion list](https://github.com/kisielk/errcheck/blob/v1.10.0/errcheck/excludes.go)
confirms their exact concrete-method names. These exceptions do not apply to
generic writer methods or formatting calls that can fail.

| Check against the corrected example | Observed result |
| --- | --- |
| `golangci-lint config verify --config .golangci.yml` | Exit 0 against the official v2.11 schema using permitted network access |
| Exact CI block executed with `sh` on the clean fixture | Exit 0; format gate silent, lint `0 issues`, tests passed |
| `go test -v ./...` | All three original greeting tests passed |
| Invalid Go: raw `fmt --diff` versus corrected gate | Raw exit 0 with empty stdout and parser warning on stderr; gate exit 1 with that diagnostic visible |
| CI on spacing/import variants | Exit 1 with the intended diff; `go test` not reached |
| Editing spacing/import variants, then rerunning their gates | Editing changed source as intended; both repaired gates exited 0 |
| CI on the `userId` variant | Exit 1 with Revive `var-naming`; `go test` not reached |
| Bare and blank-discarded `fmt.Fprintf` | Each lint run exited 1 with the intended errcheck diagnostic |
| Blank-discarded `io.Writer.Write` | Lint exit 1 with errcheck naming `w.Write` |
| Positive test discarding errors from all eight excluded concrete methods | CI exit 0, lint `0 issues`, tests passed; the added test checked both resulting buffer contents |
| Invalid YAML through the gate | Exit 3 preserved, configuration diagnostic displayed |
| Temporary tool stand-ins | Diff with tool exit 0 yielded gate exit 1; silent tool exit 7 remained 7 |

The CI sequencing probes used a forwarding `go` wrapper that recorded whether
`go test` was invoked, then executed the real pinned binary. Only clean/positive
CI cases reached it. No compiler or linter was mocked for those probes. The two
status/output stand-ins separately checked shell handling. SHA-256 comparisons
confirmed every non-editing check preserved fixture contents; lint probes
reported intended diagnostics without package-load/typecheck failures.

The gate treats any formatter output as a failure because the clean pinned
command is silent. This deliberately includes warnings, without parsing their
wording or running a second formatter. A future tool/version change needs a new
compatibility check. Editor integration and other previously stated limits
remain untested.

The unchanged catalog, profile tests, and Python checker retain their original
33-test and strict-mypy evidence; they were not rerun for these three-document
corrections. Artifact/whitespace checks and final review are recorded in the
canonical plan. The baseline, probe script, extracted CI block, and
`logs/results.json` remain in `/tmp/aek-g1-fixes-pop4wr3w/` through handoff;
temporary runtime/tools/caches are removed after recording the results.
