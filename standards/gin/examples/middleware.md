# Gin example: a terminating gate and a shared error responder

Read when a repeated cross-cutting policy justifies middleware; return to
[routing and middleware](../routing-middleware.md).

This original example contrasts with local handler error mapping. An existing
access decision gates a route group; denied requests get 403 and never reach
protected work. Handlers that hand off an operational error record it, abort,
and return without writing. One responder reports the last attached error and
maps it to a stable public code. It reports late errors too, while preserving
the already committed body/status. This last-error policy is illustrative;
choose the project's existing policy when several errors matter.

Save as `middlewareexample/middleware.go` in a temporary module with
`github.com/gin-gonic/gin@v1.12.0`. `allow` adapts an already established access
decision, not a user-supplied Boolean or an invented credential parser. `report`
is the designated internal diagnostic owner, must handle concurrent requests,
and must not leak secrets. Both dependencies are called synchronously.

```go
package middlewareexample

import (
	"context"
	"errors"
	"net/http"

	"github.com/gin-gonic/gin"
)

var ErrUnavailable = errors.New("service unavailable")

type APIError struct {
	Code string `json:"code"`
}

func RequireAccess(allow func(*http.Request) bool) gin.HandlerFunc {
	return func(c *gin.Context) {
		if !allow(c.Request) {
			c.AbortWithStatusJSON(http.StatusForbidden, APIError{Code: "forbidden"})
			return
		}
		c.Next()
	}
}

func ErrorResponses(report func(context.Context, error)) gin.HandlerFunc {
	return func(c *gin.Context) {
		c.Next()
		last := c.Errors.Last()
		if last == nil {
			return
		}
		report(c.Request.Context(), last.Err)
		if c.Writer.Written() {
			return
		}
		status, code := http.StatusInternalServerError, "internal_error"
		if errors.Is(last.Err, ErrUnavailable) {
			status, code = http.StatusServiceUnavailable, "service_unavailable"
		}
		c.AbortWithStatusJSON(status, APIError{Code: code})
	}
}
```

Install `ErrorResponses(report)` before registering the group and its handlers.
Create the protected group with `RequireAccess(allow)` before adding routes.
A handler handing off a non-nil error calls `_ = c.Error(err)`, `c.Abort()`, then
returns. A logger that must observe the mapped status belongs outside the error
responder. Code after its `c.Next()` then sees the responder's result.

Tests should send requests through the constructed router, checking denied and
permitted access, a wrapped unavailable error, a sanitized unexpected error,
observer order/final status, and an error after a body has been written. Verify
that the last case reports the error without changing the original body or
status. These assertions protect the sample's response/access contract.

This is not authentication/token verification, object-level authorization,
panic recovery, a retry loop, or transaction rollback. The application still
checks authorization for the actual resource. A recovery middleware needs its
own deliberate placement and committed/broken-response behavior; it is not
automatically supplied by `gin.New()` or by this responder. Handlers must not
continue writing a success response after handing off an error.

Run `gofmt`, relevant `go test` checks, and `go vet` under the project's supported
toolchain. Actual checks and retained test sources are recorded in the
[K02 plan](../../../docs/plans/2026-09-21-engineering-practices.md#k02-working-scope).
