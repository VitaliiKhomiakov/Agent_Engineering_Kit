# LangChainGo tool adapter fixture

This [LangChainGo boundary](../go.md) implements the actual `tools.Tool` string
interface. It checks JSON parsing, one-value input, required values, unknown fields,
trusted scope, cancellation before I/O and backend error propagation.

## Fixture and reproduction

Executed on **2026-10-29**, Go **1.26.1** on Linux amd64, `github.com/tmc/langchaingo` **v0.1.15**.
Use an empty temporary directory and save the two files below there. These are
fixture pins, not application upgrade requirements. Dependency installation needs
registry access; the test itself needs no credentials, model or remote service.

### `go.mod`

```go
module example.com/aek/langchaingo

go 1.26.0

require github.com/tmc/langchaingo v0.1.15
```

### `tool_test.go`

```go
package example

import (
	"context"
	"encoding/json"
	"errors"
	"io"
	"strings"
	"testing"

	"github.com/tmc/langchaingo/tools"
)

// Lookup binds a note reader to authenticated request context.
type Lookup struct {
	Tenant string // Set from authenticated request context, never from tool JSON.
	Read   func(context.Context, string, string) (string, error)
}

var _ tools.Tool = Lookup{}

// Name identifies the tool to its executor.
func (Lookup) Name() string { return "lookup_note" }

// Description documents the string interface's JSON input convention.
func (Lookup) Description() string {
	return `Read a visible note. Input: one JSON object with a nonempty "id" string.`
}

// Call validates arguments before invoking the scoped backend reader.
func (l Lookup) Call(ctx context.Context, input string) (string, error) {
	if err := ctx.Err(); err != nil {
		return "", err
	}

	if l.Tenant == "" || l.Read == nil {
		return "", errors.New("missing trusted request dependencies")
	}

	if len(input) > 1024 {
		return "", errors.New("input too large")
	}

	var args struct {
		ID string `json:"id"`
	}
	decoder := json.NewDecoder(strings.NewReader(input))
	decoder.DisallowUnknownFields()
	if err := decoder.Decode(&args); err != nil {
		return "", errors.New("invalid arguments")
	}

	var trailing json.RawMessage
	if err := decoder.Decode(&trailing); err != io.EOF {
		return "", errors.New("expected exactly one JSON object")
	}

	if strings.TrimSpace(args.ID) == "" || len(args.ID) > 64 {
		return "", errors.New("invalid note ID")
	}

	// Read owns authorization and source scoping; return its error unchanged.
	return l.Read(ctx, l.Tenant, args.ID)
}

func TestLookupContract(t *testing.T) {
	calls := 0
	lookup := Lookup{Tenant: "tenant-a", Read: func(ctx context.Context, tenant, id string) (string, error) {
		calls++
		if tenant != "tenant-a" || id != "n1" {
			return "", errors.New("denied")
		}

		return "Example evidence", ctx.Err()
	}}

	ctx := context.Background()
	if result, err := lookup.Call(ctx, `{"id":"n1"}`); err != nil || result != "Example evidence" {
		t.Fatalf("result=%q err=%v", result, err)
	}

	for _, input := range []string{`{`, `{}`, `null`, `{"id":4}`, `{"id":" "}`,
		`{"id":"n1","tenant":"tenant-b"}`, `{"id":"n1"} {"id":"n2"}`} {
		if _, err := lookup.Call(ctx, input); err == nil {
			t.Fatalf("accepted invalid input: %s", input)
		}
	}

	canceled, cancel := context.WithCancel(ctx)
	cancel()
	if _, err := lookup.Call(canceled, `{"id":"n1"}`); !errors.Is(err, context.Canceled) {
		t.Fatalf("lost cancellation: %v", err)
	}

	if calls != 1 {
		t.Fatalf("invalid input reached backend: %d", calls)
	}

	lookup.Tenant = "tenant-b" // A separate request fixture, not a shared mutable tool.
	if _, err := lookup.Call(ctx, `{"id":"n1"}`); err == nil {
		t.Fatal("backend denial was lost")
	}
}
```

### Checks

```sh
go mod tidy
go test -race ./...
go vet ./...
```

Keep the generated `go.sum` and resolved module graph when reproducing or adopting
the fixture; the short manifest above pins the demonstrated library, not every
transitive dependency. Preserve an application's existing compatible versions.

## Evidence limits

The module requires Go 1.24.4; the fixture deliberately records the newer runtime
actually used. The backend is a test double, not authentication middleware. This
test does not exercise model calls, provider function-calling schemas, agent
execution, stream handling or cancellation during remote I/O. Error mapping for
model/public output belongs to the caller's shared execution contract.
