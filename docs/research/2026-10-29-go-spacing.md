# Go guard spacing: dated follow-up evidence

Date: 2026-10-29. This record covers the stricter standalone-guard rule and the
revised [tooling example](../../standards/go/examples/style-tooling.md).
The [canonical task](../plans/2026-10-29-go-spacing.md) owns scope and progress.
The [2026-10-13 record](2026-10-13-go-gin-gorm-style-evidence.md) remains evidence
for its earlier configuration; it is not rewritten as a run of this revision.

## Versioned source review

| Source | Bounded conclusion |
| --- | --- |
| [golangci-lint 2.11.3 manifest](https://github.com/golangci/golangci-lint/blob/v2.11.3/go.mod) | This release includes `github.com/bombsimon/wsl/v5 v5.6.0`; no fixture upgrade is needed. |
| [2.11.3 configuration reference](https://github.com/golangci/golangci-lint/blob/v2.11.3/.golangci.reference.yml) | WSL supports explicit check selection and the two block-use allowances used by the revised example. |
| [WSL 5.6.0 checks](https://github.com/bombsimon/wsl/blob/v5.6.0/CHECKS.md) and [README](https://github.com/bombsimon/wsl/blob/v5.6.0/README.md) | `if` constrains adjacency above guards; `err` checks spacing between an error assignment and its direct check. The checks are syntactic and configurable. |

Requiring both gates and separating standalone guards of the same input are
library policy choices. The sources do not define semantic business phases or
prove that an agent loaded or followed these instructions.

## Executed environment

- Linux amd64; installed `go version go1.26.1 linux/amd64`.
- Official golangci-lint 2.11.3 binary, built with Go 1.26.1 from commit
  `6008b81b81c690c046ffc3fd5bce896da715d5fd`.
- Downloaded archive SHA-256:
  `87bb8cddbcc825d5778b64e8a91b46c0526b247f4e2f2904dea74ec7450475d1`,
  matching the official release checksum manifest and the retained fixture pin.
- `go version -m` confirmed WSL 5.6.0 and `golang.org/x/tools v0.42.0` in the binary.
- `GOTOOLCHAIN=local`, `GOWORK=off`; Go/module/linter caches and `GOPATH` were
  confined to the task's temporary runtime directory. No root Go module or active
  formatter configuration was installed in the instruction library.

The five named fixture blocks and exact CI shell block were extracted from the
revised example under `/tmp/aek-go-spacing-ctv_dc8e/runtime/`.
The final extracted configuration was byte-identical to the configuration whose
schema validation and initial lint probes passed; those results were reused.

## Executed checks

| Check | Observed result |
| --- | --- |
| `golangci-lint config verify --config .golangci.yml` | Exit 0 against the official v2.11 schema. The initial sandbox DNS denial was not counted as validation; the same command then passed with permitted network access. |
| Exact CI block on the clean fixture | Formatting gate, all configured linters and the existing greeting tests passed. |
| Adjacent independent guards; adjacent guards checking the same `userID` | Formatting passed; CI stopped at WSL with `missing whitespace ... (invalid statement above if)`. Tests were not invoked. |
| A blank line before direct `if err != nil` after `fmt.Fprintf` | Formatting passed; CI stopped at WSL with `unnecessary whitespace (err)`. |
| Scoped WSL repair on each of the three spacing variants | Exit 0; only blank lines changed. The full CI block passed afterward, including the existing tests. |
| Positive direct assignment/error check, separated same-input guards, attached `else if`/`else` chain | Accepted by the enabled checks; the chain also passed formatting and the full fixture CI block. |
| Existing formatting, unused import, naming, ignored writer error and blank-discarded writer error probes | Each failed with its intended formatter, Revive or errcheck diagnostic under the revised configuration; tests were not invoked. |
| Invalid Go and invalid YAML | Formatting gate rejected the Go parse diagnostic; invalid YAML retained exit 3. Neither reached tests. |
| Separated `if !errors.Is(err, want)` | Lint passed. This measured limit is documented: the narrow `err` check does not establish adjacency for every error predicate. |

The final runner recorded 22 command checks in `logs/results.json`; initial
contract probes and schema validation are separate. Hash comparisons showed that
all non-editing commands preserved fixture files. A forwarding wrapper recorded
`go test` invocation and then executed the real compiler, confirming CI stops
before tests on rejected variants. No compiler or linter was mocked. Repair
diffs retained every nonblank line exactly.

The example owns portable commands and probe mutations. The temporary runner,
logs, repair diffs and scoped pre-edit baseline remain under
`/tmp/aek-go-spacing-ctv_dc8e/` through handoff. Extracted runtime files, downloaded
binary/archive and caches are removed after recording results.

## Existing examples and limits

Nine blank lines were added between adjacent standalone guards in the existing
Go domain, Eino, LangChainGo and Go OTel examples. Nonblank document lines stayed
identical. Go 1.26.1 `gofmt -d` reported no differences for their extracted complete
source blocks. A temporary standard-library Go scanner/parser confirmed unchanged
tokens (including comments and inserted semicolons), valid syntax and separation
of successive standalone `if` statements in every parsed block.

Those four examples received static, whitespace-only checks; their earlier
dependency-backed runtime tests were not rerun or represented as a new run.
Their APIs, versions, manifests and behavior remain unchanged. Catalog paths and
profile ownership remain unchanged; the new plan/research are optional source
records, not bundle dependencies. Library artifact checks and the scoped
coordinator review are recorded in the canonical task.

This run does not validate a consuming project's toolchain, install its CI or
editor hooks, prove every meaningful-step boundary, or certify all WSL options.
In particular, the Medical & Pharmaceutical Intelligence project declares Go
1.27.3; its adopted instructions, application files and tools were not changed
or validated by this source-library maintenance stage.
