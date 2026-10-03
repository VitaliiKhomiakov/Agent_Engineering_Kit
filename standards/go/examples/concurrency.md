# Go example: cancel blocked receives and sends

Read when the example clarifies the linked rule; it is not required on every Go task.
Return to [concurrency](../concurrency.md).

This synchronous stage demonstrates cancellation during both receiving and
sending. Its caller owns any goroutine, waits for completion, and owns the
channels. The function does not close the caller's output channel.

```go
package practices

import "context"

func Forward(ctx context.Context, input <-chan string, output chan<- string) error {
	for {
		select {
		case <-ctx.Done():
			return ctx.Err()
		case value, ok := <-input:
			if !ok {
				return nil
			}
			select {
			case <-ctx.Done():
				return ctx.Err()
			case output <- value:
			}
		}
	}
}
```

Cancellation is cooperative: when multiple cases are ready, `select` does not
prioritize cancellation. This is not a guarantee of zero sends after cancellation
or atomic delivery; use a stronger protocol when that is the actual requirement.
See [context](https://pkg.go.dev/context@go1.26.1),
[pipelines](https://go.dev/blog/pipelines), the [memory model](https://go.dev/ref/mem),
and [Go 1.22 loop changes](https://go.dev/doc/go1.22).

This is an original standard-library-only example. Save its Go block as a
`.go` file in package `practices`; it can be compiled with the other Go examples.
