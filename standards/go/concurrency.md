# Go: cancellation and concurrency

Read when adding or changing goroutines, channels, shared state, cancellation, or shutdown. Return to the [Go entry](../go.md).


- Pass `context.Context` explicitly, conventionally first, across operations
  that support cancellation/deadlines. Do not use its values as a dependency
  container or general options bag. Call the cancel function for a derived
  context and avoid storing request contexts in long-lived service structs.
- Give every started goroutine an owner and a completion path. Bound work when
  input can exceed capacity, propagate failures, and account for shutdown. A
  cancel signal requests termination; it does not wait for goroutines to finish.
- Make potentially blocking sends, receives, and external operations interruptible
  when their contract requires cancellation. A channel buffer alone does not
  solve a lifetime problem. Define who closes a channel after all sends finish;
  a receiver must not close a channel while another goroutine can still send.
- Synchronize shared mutable data. Choose a mutex for protected state or channels
  for a communication/ownership protocol; neither is universally superior.
  Do not assume a map is safe for concurrent reads and writes.
- Check the effective language version before changing loop-variable captures.
  Go 1.22+ gives loop-declared variables per-iteration identity; that does not
  make shared pointed-to data or variables assigned outside the loop independent.

Cancellation is cooperative. When multiple `select` cases are ready, cancellation
has no priority; use a stronger protocol if atomic delivery or zero sends after
cancellation is required. The [forwarding example](examples/concurrency.md)
shows interruptible receives and sends with caller-owned completion.

See [context](https://pkg.go.dev/context@go1.26.1),
[pipelines](https://go.dev/blog/pipelines), the [memory model](https://go.dev/ref/mem),
and [Go 1.22 loop changes](https://go.dev/doc/go1.22).
