# Go example: reproducible formatting and lint checks

Read when adopting or validating the [Go tooling policy](../verification.md#formatting-and-lint-adoption).
[Style](../style.md) owns conventions. This is an inactive, standard-library-only
fixture: extract it into a disposable directory, not the instruction-library root.
It neither upgrades an existing project's toolchain nor installs its CI/editor setup.

## Pinned environment

The checked tuple is Go **1.26.1**, linux/amd64, and the official
**golangci-lint 2.11.3** binary built with **go1.26.1**, commit
`6008b81b81c690c046ffc3fd5bce896da715d5fd`. Its build information records
`golang.org/x/tools v0.42.0` (goimports and analysis tooling),
`honnef.co/go/tools v0.7.0` (Staticcheck/unused),
`github.com/mgechev/revive v1.15.0`, and
`github.com/kisielk/errcheck v1.10.0`.
The bundled govet integration uses the pinned Go/tooling build.

Obtain Go from the [official archive](https://go.dev/dl/) and the linter from
[release v2.11.3](https://github.com/golangci/golangci-lint/releases/tag/v2.11.3).
For the checked Linux archives, verify SHA-256 before extraction:

```text
go1.26.1.linux-amd64.tar.gz
031f088e5d955bab8657ede27ad4e3bc5b7c1ba281f05f245bcc304f327c987a
golangci-lint-2.11.3-linux-amd64.tar.gz
87bb8cddbcc825d5778b64e8a91b46c0526b247f4e2f2904dea74ec7450475d1
```

Use the official Go download JSON (`https://go.dev/dl/?mode=json&include=all`)
and release checksum manifest for other platform archives; this run does not
certify those platforms. Put the extracted `go/bin` and linter directory on a
task-local `PATH`. No system-wide installation or root Go module is required.
Set `GOTOOLCHAIN=local` to prevent automatic toolchain switching; use the exact
compiler above when reproducing this fixture. No standalone goimports binary is
used here: editor/manual formatting uses the same bundled formatter as CI.

## Complete fixture

Save the following five named blocks together, with the script under `scripts/`.
The manifest has no third-party dependencies and needs no `go.sum`.

### `go.mod`

```go
module example.com/style-fixture

go 1.26.1
```

### `.golangci.yml`

```yaml
version: "2"

run:
  timeout: 2m
  relative-path-mode: gomod
  modules-download-mode: readonly

linters:
  default: none
  enable:
    - govet
    - staticcheck
    - errcheck
    - unused
    - revive
  settings:
    errcheck:
      check-blank: true
      disable-default-exclusions: true
      # These concrete methods always return a nil error.
      exclude-functions:
        - (*bytes.Buffer).Write
        - (*bytes.Buffer).WriteByte
        - (*bytes.Buffer).WriteRune
        - (*bytes.Buffer).WriteString
        - (*strings.Builder).Write
        - (*strings.Builder).WriteByte
        - (*strings.Builder).WriteRune
        - (*strings.Builder).WriteString
    staticcheck:
      checks:
        - all
        - -ST1000 # Keep the bundled package-comment default disabled.
        - -ST1003 # Revive: var-naming.
        - -ST1005 # Revive: error-strings.
        - -ST1006 # Revive: receiver-naming.
        - -ST1016 # Revive: receiver-naming.
        - -ST1020 # Revive: exported.
        - -ST1021 # Revive: exported.
        - -ST1022 # Revive: exported.
    revive:
      enable-default-rules: false
      enable-all-rules: false
      rules:
        - name: var-naming
        - name: receiver-naming
        - name: exported
        - name: error-strings
        - name: indent-error-flow
  exclusions:
    generated: strict
    presets: []
    paths:
      - '(^|/)vendor/'

formatters:
  enable:
    - goimports
  exclusions:
    generated: strict
    paths:
      - '(^|/)vendor/'
```

The linter list is explicit; `all` above selects checks inside Staticcheck, not
every golangci-lint linter. The pinned integration already excludes ST1000,
ST1003, ST1016, and ST1020-ST1022 by default. This recipe preserves those choices
and also assigns error-string and receiver-name diagnostics to Revive by disabling
ST1005/ST1006. All SA correctness checks remain enabled. Revive's explicit five
rules prevent its implicit default or all-rule expansion. No line-length linter
or second formatter is enabled. Review this mapping when changing the pins.

`presets: []` avoids broad issue presets. Errcheck includes blank assignments;
its built-in exclusions are replaced with eight concrete write methods on
[`bytes.Buffer`](https://pkg.go.dev/bytes@go1.26.1#Buffer.Write) and
[`strings.Builder`](https://pkg.go.dev/strings@go1.26.1#Builder.Write) whose returned
errors are always nil. This permits intentional discards such as
`_, _ = b.WriteString("ok")` without unreachable error branches or local suppressions.
It does not exclude `io.Writer.Write`, `fmt.Fprintf`, or writes to files/stdout.
Other infallible APIs need their own narrow, contract-backed exception; do not
add meaningless branches to satisfy the linter. See the
[pinned errcheck exclusions](https://github.com/kisielk/errcheck/blob/v1.10.0/errcheck/excludes.go)
for the underlying symbol syntax.

The fixture has no generated or vendor files. Both tool sections exclude vendor paths
and use Go's strict generated-file marker; lint exclusions filter diagnostics,
not necessarily package loading. Do not pass vendor/generated files to an editor
formatter and do not hand-edit them to meet style. Other generation conventions
need deliberate path exclusions in the adopting project.

Goimports uses standard-library and other import groups. For an optional third
group, add `formatters.settings.goimports.local-prefixes` with the project's
actual module prefix and apply it to both editor and CI. This fixture needs no
local-prefix setting. A separate editor goimports binary requires its own exact
`golang.org/x/tools` pin and an output-parity check; its name alone does not prove
it matches this bundled formatter.

### `greeting.go`

```go
// Package greeting writes small personalized greetings.
package greeting

import (
	"errors"
	"fmt"
	"io"
	"strings"
)

// Write writes a greeting for userID and reports a rejected ID or writer failure.
func Write(w io.Writer, userID string) error {
	userID = strings.TrimSpace(userID)
	if userID == "" {
		return errors.New("user ID is required")
	}

	if _, err := fmt.Fprintf(w, "hello, %s\n", userID); err != nil {
		return fmt.Errorf("write greeting: %w", err)
	}

	return nil
}
```

### `greeting_test.go`

```go
package greeting

import (
	"bytes"
	"errors"
	"testing"
)

func TestWrite(t *testing.T) {
	var output bytes.Buffer
	if err := Write(&output, "  user-42  "); err != nil {
		t.Fatal(err)
	}

	if got := output.String(); got != "hello, user-42\n" {
		t.Fatalf("Write output = %q; want %q", got, "hello, user-42\n")
	}
}

func TestWriteRejectsBlankID(t *testing.T) {
	var output bytes.Buffer
	if err := Write(&output, "  "); err == nil {
		t.Fatal("Write accepted a blank ID")
	}

	if output.Len() != 0 {
		t.Fatalf("Write produced output for a rejected ID: %q", output.String())
	}
}

type failingWriter struct {
	err error
}

func (w failingWriter) Write([]byte) (int, error) {
	return 0, w.err
}

func TestWritePreservesWriterError(t *testing.T) {
	want := errors.New("writer unavailable")

	err := Write(failingWriter{err: want}, "user-42")
	if !errors.Is(err, want) {
		t.Fatalf("Write error = %v; want wrapped %v", err, want)
	}
}
```

### `scripts/check-format.sh`

```sh
#!/bin/sh
set -eu

if [ "$#" -eq 0 ]; then
    printf '%s\n' 'usage: sh scripts/check-format.sh <file-or-directory> ...' >&2
    exit 2
fi

aek_fmt_output=$(mktemp)
trap 'rm -f "$aek_fmt_output"' EXIT
trap 'exit 2' HUP INT TERM

aek_fmt_status=0
golangci-lint fmt --config .golangci.yml --diff "$@" >"$aek_fmt_output" 2>&1 || aek_fmt_status=$?
cat "$aek_fmt_output"
if [ "$aek_fmt_status" -ne 0 ]; then
    exit "$aek_fmt_status"
fi
if [ -s "$aek_fmt_output" ]; then
    exit 1
fi
```

## Editing and non-mutating checks

Run from the extracted module directory. These commands assume the pinned binaries
are on `PATH`; POSIX `sh` and `mktemp` are required for the gate.
`config verify` fetches the official v2.11 JSON schema and requires network access;
an unavailable schema is a failed validation, not a passing offline check.

### Validate the selected configuration

```sh
set -eu
export GOTOOLCHAIN=local GOWORK=off
go version
golangci-lint version
golangci-lint config verify --config .golangci.yml
```

### Editing

This command rewrites the selected source files, including imports.

```sh
export GOTOOLCHAIN=local GOWORK=off
golangci-lint fmt --config .golangci.yml greeting.go greeting_test.go
```

For format-on-save, configure the editor's external formatter/save action to run
that `fmt` command from the module root with the saved file as its argument.
The action operates on saved content, so enable editor reload after external
changes and avoid a second save hook with different formatting/import settings.
Editor-specific integration is conditional; only the command is exercised here.

### CI

Run this block after configuration validation. It preserves source and stops on
the first failed check, including when saved as a script and run with ordinary `sh`.
Do not prepend the editing command: that would repair formatting before checking it.

```sh
set -eu
export GOTOOLCHAIN=local GOWORK=off
sh scripts/check-format.sh greeting.go greeting_test.go
golangci-lint run --config .golangci.yml ./...
go test ./...
```

The pinned formatter can report a parse error as a warning on stderr and exit 0.
The gate therefore captures both output streams and fails on any output, whether
a diff or diagnostic, as well as on a nonzero exit status. A clean pinned run is
silent; unexpected warnings must be resolved rather than mistaken for success.
This avoids depending on diagnostic wording or adding a second formatter.

Format arguments are filesystem paths; `run ./...` loads packages. In larger projects,
choose affected files and package patterns deliberately in each module root,
preserving required CI and matching build tags. `run` without `--fix` does not
replace the separate formatting gate. Checks can write caches, but not source.

## Negative probes

Use a fresh disposable copy of the clean fixture for each case. Preserve the
clean source and compare its hashes before/after non-mutating checks. For lint
probes, format first and require the intended diagnostic, not just a nonzero exit:
package-load, typecheck, configuration, or tool failures are not passing probes.

| Variant | Change | Expected evidence |
| --- | --- | --- |
| Formatting | Replace `return nil` with `return    nil` in `greeting.go` | Gate fails and diff contains the spacing correction; source stays unchanged |
| Imports | Add unused `"os"` to the import block | Gate fails and diff removes that import; source stays unchanged |
| Naming | Replace every `userID` in `greeting.go` with `userId` | `run` fails with Revive `var-naming` naming `userID` |
| Ignored error | Replace the checked `fmt.Fprintf` block with a bare `fmt.Fprintf(w, "hello, %s\n", userID)` call | `run` fails with `errcheck` for `fmt.Fprintf` |
| Discarded writer error | Replace that block with `_, _ = fmt.Fprintf(w, "hello, %s\n", userID)` | `run` still fails with `errcheck`; concrete-method exceptions do not hide writer failures |
| Invalid Go | Replace `greeting.go` with `package greeting` followed by unfinished `func Broken(` | Gate fails on the parse diagnostic even though raw `fmt --diff` exits 0 |
| Tool error | Replace `.golangci.yml` with invalid YAML in a fresh copy | Gate preserves the nonzero status and displays the configuration diagnostic |
| CI stops | Run the CI block via `sh` on the naming variant | Nonzero exit from lint; `go test` is not reached |

Then run the editing command in the formatting/import variants; the gate must
pass afterward. The tiny writer tests prove the clean fixture's own success,
rejection, and wrapped-error behavior; lint failures alone do not prove it works.

For a positive exception probe, add a temporary test that discards the returned
errors of `Write`, `WriteByte`, `WriteRune`, and `WriteString` on concrete
`bytes.Buffer` and `strings.Builder` values, then reads their contents. Format
the test and run lint: these eight calls must pass. Contrast this with the
discarded-writer-error case above; do not suppress whole packages or method names.

## Evidence and limits

The [dated style-evidence record](../../../docs/research/2026-10-13-go-gin-gorm-style-evidence.md)
contains executed checks and exact versions, separate from source review.
This fixture does not prove editor integration, every rule/exception, generated
code workflows, multiple modules/build tags, or compatibility with other Go/tool
versions. See the versioned
[configuration reference](https://github.com/golangci/golangci-lint/blob/v2.11.3/.golangci.reference.yml),
[Staticcheck integration](https://github.com/golangci/golangci-lint/blob/v2.11.3/pkg/golinters/staticcheck/staticcheck.go),
and [formatter command](https://github.com/golangci/golangci-lint/blob/v2.11.3/pkg/commands/fmt.go).
The [formatter error path](https://github.com/golangci/golangci-lint/blob/v2.11.3/pkg/goformatters/meta_formatter.go)
explains why the gate checks diagnostics as well as exit status.
