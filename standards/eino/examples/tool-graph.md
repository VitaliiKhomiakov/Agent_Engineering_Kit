# Eino typed tool and graph fixture

This [Eino tool boundary](../tools-retrieval.md) checks real schema construction,
JSON decoding, explicit range/empty-input validation, cancellation before I/O and
backend denial. A one-node graph demonstrates typed wiring; an application with
only this operation can call the tool directly.

## Fixture and reproduction

Executed on **2026-10-29**, Go **1.26.1** on Linux amd64, `github.com/cloudwego/eino` **v0.9.22**.
Use an empty temporary directory and save the two files below there. These are
fixture pins, not application upgrade requirements. Dependency installation needs
registry access; the test itself needs no credentials, model or remote service.

### `go.mod`

```go
module example.com/aek/eino

go 1.26.0

require github.com/cloudwego/eino v0.9.22
```

### `tool_test.go`

```go
package example

import (
	"context"
	"encoding/json"
	"errors"
	"strings"
	"testing"

	"github.com/cloudwego/eino/components/tool"
	"github.com/cloudwego/eino/components/tool/utils"
	"github.com/cloudwego/eino/compose"
)

// SearchInput contains only model-selectable arguments.
type SearchInput struct {
	Query string `json:"query" jsonschema_description:"Words to search for"`
	Limit int    `json:"limit" jsonschema:"minimum=1,maximum=5"`
}

// Hit identifies one evidence unit returned by the backend.
type Hit struct {
	ID   string `json:"id"`
	Text string `json:"text"`
}

// Search authorizes the bound tenant and retrieves notes within that scope.
type Search func(context.Context, string, string, int) ([]Hit, error)

func newSearch(tenant string, search Search) (tool.InvokableTool, error) {
	if tenant == "" || search == nil {
		return nil, errors.New("missing trusted request dependencies")
	}

	return utils.InferTool("search_notes", "Search notes visible to the current user",
		func(ctx context.Context, in SearchInput) ([]Hit, error) {
			if err := ctx.Err(); err != nil {
				return nil, err
			}

			query := strings.TrimSpace(in.Query)
			if query == "" || len(query) > 256 || in.Limit < 1 || in.Limit > 5 {
				return nil, errors.New("invalid query or limit")
			}

			// The backend must authorize this scope and apply it before retrieval.
			return search(ctx, tenant, query, in.Limit)
		})
}

func TestToolGraph(t *testing.T) {
	ctx := context.Background()
	calls := 0
	backend := func(_ context.Context, tenant, query string, limit int) ([]Hit, error) {
		calls++
		if tenant != "tenant-a" {
			return nil, errors.New("denied")
		}
		if query != "policy" || limit != 2 {
			return nil, errors.New("unexpected search")
		}

		return []Hit{{ID: "doc-1:chunk-2", Text: "Example evidence"}}, nil
	}

	search, err := newSearch("tenant-a", backend)
	if err != nil {
		t.Fatal(err)
	}

	info, err := search.Info(ctx)
	if err != nil || info.Name != "search_notes" || info.ParamsOneOf == nil {
		t.Fatalf("invalid tool metadata: %v, %v", info, err)
	}

	graph := compose.NewGraph[string, string]()

	err = graph.AddLambdaNode("search", compose.InvokableLambda(
		func(ctx context.Context, input string) (string, error) {
			return search.InvokableRun(ctx, input)
		}))
	if err != nil {
		t.Fatal(err)
	}

	for _, edge := range [][2]string{{compose.START, "search"}, {"search", compose.END}} {
		if err := graph.AddEdge(edge[0], edge[1]); err != nil {
			t.Fatal(err)
		}
	}

	runnable, err := graph.Compile(ctx)
	if err != nil {
		t.Fatal(err)
	}

	result, err := runnable.Invoke(ctx, `{"query":"policy","limit":2}`)
	if err != nil {
		t.Fatal(err)
	}

	var hits []Hit
	if err := json.Unmarshal([]byte(result), &hits); err != nil {
		t.Fatal(err)
	}
	if len(hits) != 1 || hits[0].ID != "doc-1:chunk-2" || calls != 1 {
		t.Fatalf("unexpected result: %s, calls=%d", result, calls)
	}

	for _, input := range []string{`{`, `{"query":"policy","limit":0}`, `{"query":" ","limit":2}`} {
		if _, err := runnable.Invoke(ctx, input); err == nil {
			t.Fatalf("accepted invalid arguments: %s", input)
		}
	}

	canceled, cancel := context.WithCancel(ctx)
	cancel()
	if _, err := search.InvokableRun(canceled, `{"query":"policy","limit":2}`); !errors.Is(err, context.Canceled) {
		t.Fatalf("lost cancellation: %v", err)
	}
	if calls != 1 {
		t.Fatalf("invalid/canceled input reached backend: %d", calls)
	}

	denied, err := newSearch("tenant-b", backend)
	if err != nil {
		t.Fatal(err)
	}
	if _, err := denied.InvokableRun(ctx, `{"query":"policy","limit":2}`); err == nil {
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

The backend is an in-memory test double. The host must authenticate and bind the
tenant; the real backend must authorize and scope retrieval. This fixture does not
test a provider, model tool selection, streaming, ADK, durable checkpoints or RAG
quality. Schema inference does not establish strict unknown-field rejection; that
would require a separate decoder/validator contract. See [runtime and recovery](../runtime-recovery.md)
only when those features are used.
