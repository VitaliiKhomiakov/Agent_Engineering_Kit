# Gin example: presence, bounded JSON, and business errors

Read when choosing a request-binding/error contract; return to
[handlers and binding](../handlers-binding.md).

This original example adapts a publish operation. Its HTTP contract requires a
positive document ID, `application/json`, exactly one JSON value, no unknown
fields, and an explicitly supplied Boolean notification choice. `false` is valid;
omission and `null` are not. The 1 KiB limit is an illustrative endpoint budget,
not a default for other services. Trailing whitespace also counts toward it.

The typed `Publish` function stands for application behavior. That implementation
checks authorization and current state, including the invariant illustrated by
the [Go publication example](../../go/examples/domain.md). A correctly bound
request can still return `ErrConflict`. No HTTP validator decides whether a
document is publishable, and no untyped map crosses into application code.

The standalone file declares the signatures/errors its adapter expects. In a
real project, reuse the existing application-owned commands and errors, or wire
a closure that translates to the use case at the composition boundary. Do not
make an independent application/domain package import this Gin example package.

Save the block as `bindingexample/binding.go` in a temporary module. The local
`singleJSON` binder is optional: use ordinary `ShouldBindJSON` if its parsing
contract is sufficient. This decoder uses `encoding/json`, including its normal
duplicate-key and case-insensitive field matching behavior; it is not a canonical
JSON validator. Do not silently impose this stricter contract on an existing API.
See the [standard decoder contract](https://pkg.go.dev/encoding/json#Unmarshal).

```go
package bindingexample

import (
	"context"
	"encoding/json"
	"errors"
	"io"
	"mime"
	"net/http"

	"github.com/gin-gonic/gin"
	"github.com/gin-gonic/gin/binding"
)

var (
	ErrNotFound = errors.New("document not found")
	ErrConflict = errors.New("publication conflict")
)

type PublishCommand struct {
	DocumentID uint64
	Notify     bool
}

type Publish func(context.Context, PublishCommand) error

type APIError struct {
	Code string `json:"code"`
}

type publishURI struct {
	ID uint64 `uri:"id" binding:"gt=0"`
}

type publishBody struct {
	Notify *bool `json:"notify" binding:"required"`
}

func Handler(publish Publish) gin.HandlerFunc {
	return func(c *gin.Context) {
		command, ok := bindCommand(c)
		if !ok {
			return
		}
		if err := publish(c.Request.Context(), command); err != nil {
			status, code := http.StatusInternalServerError, "internal_error"
			switch {
			case errors.Is(err, ErrNotFound):
				status, code = http.StatusNotFound, "document_not_found"
			case errors.Is(err, ErrConflict):
				status, code = http.StatusConflict, "publication_conflict"
			}
			c.AbortWithStatusJSON(status, APIError{Code: code})
			return
		}
		c.Status(http.StatusNoContent)
	}
}

func bindCommand(c *gin.Context) (PublishCommand, bool) {
	var path publishURI
	if err := c.ShouldBindUri(&path); err != nil {
		c.AbortWithStatusJSON(http.StatusBadRequest, APIError{Code: "invalid_path"})
		return PublishCommand{}, false
	}
	mediaType, _, err := mime.ParseMediaType(c.GetHeader("Content-Type"))
	if err != nil || mediaType != "application/json" {
		c.AbortWithStatusJSON(http.StatusUnsupportedMediaType, APIError{Code: "unsupported_media_type"})
		return PublishCommand{}, false
	}
	c.Request.Body = http.MaxBytesReader(c.Writer, c.Request.Body, 1024)
	var body publishBody
	if err := c.ShouldBindWith(&body, singleJSON{}); err != nil {
		status, code := http.StatusBadRequest, "invalid_request"
		var tooLarge *http.MaxBytesError
		if errors.As(err, &tooLarge) {
			status, code = http.StatusRequestEntityTooLarge, "body_too_large"
		}
		c.AbortWithStatusJSON(status, APIError{Code: code})
		return PublishCommand{}, false
	}
	return PublishCommand{DocumentID: path.ID, Notify: *body.Notify}, true
}

type singleJSON struct{}

func (singleJSON) Name() string { return "single-json" }

func (singleJSON) Bind(request *http.Request, value any) error {
	decoder := json.NewDecoder(request.Body)
	decoder.DisallowUnknownFields()
	if err := decoder.Decode(value); err != nil {
		return err
	}
	var extra json.RawMessage
	if err := decoder.Decode(&extra); err != io.EOF {
		if err == nil {
			return errors.New("multiple JSON values")
		}
		return err
	}
	return binding.Validator.ValidateStruct(value)
}
```

Register `Handler(publish)` on `POST /documents/:id/publish` after the project's
authentication middleware. The binder assumes Gin's default validator remains
enabled and configured before serving. Its `any` parameter is Gin's binder
interface; the application command and error response are concrete types.

For a standalone check, initialize a temporary module, add
`github.com/gin-gonic/gin@v1.12.0`, and run `gofmt`, `go test ./...`, and
`go vet ./...` with a compatible local Go toolchain. Merely compiling this block
does not exercise HTTP behavior: include router-based tests for accepted `false`,
missing/null values, malformed/extra JSON, media type, path and size failures,
wrapped business errors, and context propagation. Assert rejection prevents the
application operation and that public errors contain no private details.

This is a transport example, not a server template. Authentication, persistent
state, transaction/notification atomicity, cancellation-specific HTTP policy,
operational logging, and server shutdown are outside the block. In a real service,
provide those through their existing owners; do not copy the illustrative
unexpected-error mapping as a complete operational policy.

Actual example commands, test results, and retained test sources are recorded in
the [K02 plan](../../../docs/plans/2026-09-21-engineering-practices.md#k02-working-scope).
