# JavaScript async operations and effects

Read for promises, ordering, cancellation, iterators, resource cleanup, stale
results or external effects. Use [values/state](values-state.md) when mutable
objects cross these operations. The [two-read example](examples/async-ownership.md)
is optional; it illustrates explicit ownership without a concurrency library.

## Completion has an owner

Return or await promises whose completion belongs to the caller's operation.
An unreturned promise prevents that caller from observing its result and failure.
Writing `void operation()` does not handle rejection, provide cancellation or
transfer responsibility. Intentional detached work needs an actual lifecycle,
error reporting and shutdown owner; durable work needs an appropriate durable
handoff. Do not report completed effects merely because they were started.

`async` returns a promise; synchronous work still runs on the executing thread.
An `await` continuation can interleave with other work even when the awaited value
is already fulfilled. Identify assumptions spanning that boundary: a selection,
balance or cached value may have changed. Recheck the relevant state/version or
use the actual transactional/serialization mechanism. Cancellation or an operation
generation can prevent stale UI results from being applied; neither rolls back
an already completed remote write.

Use normal promise-returning APIs directly. Wrap a callback API only when needed
and account for both success and error paths; avoid an `async` Promise executor.
Keep `try`/`catch`/`finally` around the work they own. Returning an unawaited promise
from a `try` block can run `finally` before that work finishes; use `return await`
when the local error/resource scope must remain active. Do not let cleanup's
`return` or a careless replacement error hide the original outcome.

## Ordering, parallelism and cancellation

Use a sequential `for...of` with `await` when order or shared state requires it.
`forEach` does not await an async callback. `map` can create promises; observe
their aggregate outcome. Choose fixed or bounded parallelism for independent
work; creating promises for every item first does not impose a concurrency limit.
For arbitrary input, prefer the project's existing bounded mechanism or a simple
sequential loop over a new general-purpose scheduler.

Choose the combinator for the result contract:

- `Promise.all` requires every success and rejects on a failure. The other work
  can continue; the returned rejection is not cancellation or a wait for cleanup.
- `Promise.allSettled` waits for outcomes, which the owner must inspect. It does
  not make a required failed operation optional or stop it on a sibling failure.
- `Promise.race` observes the first settlement. A timeout winning a race does not
  stop or release the losing operation.

These combinators observe their input promises; `Promise.all` does not inherently
leave later input rejections unhandled. The separate problem is owning unfinished
effects/resources. Observe work from the point it starts, including a dependency
that can throw synchronously before returning its promised result.

When the API supports cancellation, pass a caller-owned signal down the relevant
operation. Check pre-aborted signals and remove listeners/release timers on every
exit. `AbortController` is cooperative host functionality, not a promise feature
that forcibly kills arbitrary code. An owned group can relay cancellation, abort
siblings on failure, and await their settlement/cleanup before returning its
original failure. This requires adapters that settle and release resources after
abort; joining an operation that ignores cancellation can wait indefinitely.
Set real deadlines at the adapter/host boundary according to the contract.

## Resources, persistence and integrations

Acquire a resource with a clear release scope, normally `try`/`finally` around
the awaited operation. Remove event listeners/subscriptions when their owner
ends. Garbage collection and promise settlement are not general resource-release
protocols. Use newer disposal syntax only with verified compiler/runtime support
and an API implementing that protocol; do not add a disposal abstraction by default.

For an async iterator owning a resource, implement cleanup at that owner. Early
`break` from `for await...of` calls and awaits the iterator's available `return()`;
this does not close unrelated handles or cancel every promise created beforehand.
Verify the particular producer's failure/early-exit behavior instead of assuming
all iterators or runtime versions provide the same cleanup guarantee.

Language-level promise composition is not a database transaction. Bind connection,
transaction and retry ownership to the relevant adapter/use case. Await required
commit or durable-handoff completion before reporting its success. A catch cannot
undo prior external effects or guarantee whether a timed-out write committed.
Use existing idempotency/transaction mechanisms for retryable writes and define
partial-failure semantics; do not add repositories, an outbox or a saga merely
because several promises are involved. Keep raw database/API data behind explicit
validated results, including serialization and error mapping.

## Basis

[Promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises),
[Promise.all](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all),
[await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await),
[DOM cancellation](https://dom.spec.whatwg.org/#aborting-ongoing-activities) and
[async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for-await...of)
explain the mechanisms. Completion ownership and integration boundaries are
project policy; they do not assert structured concurrency as a native JS feature.
