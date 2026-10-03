# Go example: dependency and function strategy

Read when the example clarifies the linked rule; it is not required on every Go task.
Return to [contracts](../contracts.md).

This example assumes interchangeable text sources and a caller-selected
normalization operation. Its interface describes the consumer's need; the
strategy is an ordinary function such as `strings.TrimSpace`. If those variations
do not exist, a direct function call can be sufficient. The source's errors are
deliberately part of this example's contract.

```go
package practices

import (
	"context"
	"fmt"
)

type TextSource interface {
	ReadText(context.Context) (string, error)
}

func PrepareText(ctx context.Context, source TextSource, normalize func(string) string) (string, error) {
	text, err := source.ReadText(ctx)
	if err != nil {
		return "", fmt.Errorf("prepare text: %w", err)
	}
	return normalize(text), nil
}
```

Assembly supplies a valid source and normalization function. Pass the existing
operation context through the dependency; do not replace it with a background
context to hide cancellation. The transport adapter decides how a returned
error becomes a response. See [error wrapping](https://go.dev/blog/go1.13-errors).

This is an original standard-library-only example. Save its Go block as a
`.go` file in package `practices`; it can be compiled with the other Go examples.
