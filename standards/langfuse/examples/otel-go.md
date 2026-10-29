# Local Go OpenTelemetry fixture

This [instrumentation fixture](../instrumentation.md) uses the Go OTel SDK and a
local in-memory exporter. It checks parent/child context, the exact permitted tool
span attributes, explicit span completion and bounded flush/shutdown.

## Fixture and reproduction

Executed on **2026-10-29**, Go **1.26.1** on Linux amd64, `go.opentelemetry.io/otel/sdk` **v1.47.0**.
Use an empty temporary directory and save the two files below there. These are
fixture pins, not application upgrade requirements. Dependency installation needs
registry access; the test itself needs no credentials, model or remote service.

### `go.mod`

```go
module example.com/aek/otel

go 1.26.0

require go.opentelemetry.io/otel/sdk v1.47.0
```

### `trace_test.go`

```go
package example

import (
	"context"
	"testing"
	"time"

	"go.opentelemetry.io/otel/attribute"
	"go.opentelemetry.io/otel/sdk/trace"
	"go.opentelemetry.io/otel/sdk/trace/tracetest"
	traceapi "go.opentelemetry.io/otel/trace"
)

func TestSanitizedChildSpan(t *testing.T) {
	// Local sink: no endpoint, credentials or network requests.
	exporter := tracetest.NewInMemoryExporter()
	provider := trace.NewTracerProvider(trace.WithSyncer(exporter))

	t.Cleanup(func() {
		ctx, cancel := context.WithTimeout(context.Background(), time.Second)
		defer cancel()
		if err := provider.Shutdown(ctx); err != nil {
			t.Error(err)
		}
	})

	tracer := provider.Tracer("aek-example")
	requestCtx, parent := tracer.Start(context.Background(), "answer.request")

	_, child := tracer.Start(requestCtx, "tool.lookup", traceapi.WithAttributes(
		attribute.String("langfuse.observation.type", "tool"),
		attribute.String("app.tool.name", "lookup_note"),
	))
	// Deliberately omit raw input, output, user identity and error text.
	child.SetAttributes(attribute.Int("app.result.count", 1))
	child.End()
	parent.End()

	flushCtx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()
	if err := provider.ForceFlush(flushCtx); err != nil {
		t.Fatal(err)
	}

	spans := exporter.GetSpans()
	if len(spans) != 2 {
		t.Fatalf("got %d spans", len(spans))
	}

	var toolSpan, rootSpan *tracetest.SpanStub
	for i := range spans {
		switch spans[i].Name {
		case "tool.lookup":
			toolSpan = &spans[i]
		case "answer.request":
			rootSpan = &spans[i]
		}
	}
	if toolSpan == nil || rootSpan == nil {
		t.Fatal("missing expected spans")
	}

	if toolSpan.Parent.SpanID() != rootSpan.SpanContext.SpanID() ||
		toolSpan.SpanContext.TraceID() != rootSpan.SpanContext.TraceID() {
		t.Fatal("lost parent context")
	}

	want := map[attribute.Key]attribute.Value{
		"langfuse.observation.type": attribute.StringValue("tool"),
		"app.tool.name":             attribute.StringValue("lookup_note"),
		"app.result.count":          attribute.IntValue(1),
	}
	if len(toolSpan.Attributes) != len(want) {
		t.Fatalf("unexpected attributes: %v", toolSpan.Attributes)
	}
	for _, pair := range toolSpan.Attributes {
		if expected, ok := want[pair.Key]; !ok || expected != pair.Value {
			t.Fatalf("unexpected attribute: %v", pair)
		}
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

This OTel SDK release requires Go 1.26.0. It is not a native Langfuse Go SDK.
The fixture contains no Langfuse endpoint, keys or HTTP exporter and does not
verify server compatibility, attribute ingestion/mapping or persistence. It proves
the local attribute allowlist for this span, not redaction of other instrumentation.
Production export and [privacy coverage](../privacy-evaluation.md) need their actual
selected integration checks.
