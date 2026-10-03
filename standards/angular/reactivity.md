# Angular reactivity and state ownership

Use the [entry](../angular.md); for NgRx-specific APIs use its
[state-selection rules](../ngrx/state-architecture.md).

## Signals and derived state

Use a local signal for local synchronous UI state. Expose read-only views and
named commands from shared state owners; `asReadonly()` does not deep-freeze
objects. Replace changed objects/arrays rather than mutating them in place.

Use `computed` for derived values. Its evaluation is lazy and memoized, tracking
the signals actually read synchronously. Keep derivations pure; do not fetch,
subscribe, dispatch or write other state inside them. Preserve one authoritative
value instead of effect-driven copies. Use `linkedSignal` only for genuinely
writable dependent state with an explicit reset rule and supported version.

Angular `effect` synchronizes with an external imperative API, such as a chart,
not with another redundant signal. Own cleanup of listeners/timers and work
started by each run. Reads after an asynchronous boundary are not tracked.
For DOM timing, use the installed render-hook API; do not hide ordering defects
with `setTimeout` or repeated `detectChanges`.

## Observable flow and subscriptions

Observables represent asynchronous sequences, completion, cancellation and
concurrency. Signals represent current state. Retain RxJS for workflows that need
event semantics; neither abstraction replaces the other everywhere.

- Compose one pipeline instead of nested subscriptions. Present a stable
  `vm$` with `AsyncPipe`, or a signal view model; avoid repeated async bindings
  that subscribe independently to a cold HTTP stream.
- Use `takeUntilDestroyed` for owned imperative subscriptions. Pass a captured
  `DestroyRef` outside an injection context. Place teardown so it also disposes
  inner subscriptions; a root service's destruction is not a page lifetime.
- Construct `toSignal` once per owned source in an injection context (or supply
  an injector). It subscribes immediately. Specify initial/undefined handling;
  `requireSync` is only for a source guaranteed to emit synchronously, not HTTP.
- Map expected errors into view state before `toSignal`; an unhandled source
  error throws when the signal is read. Completion retains the last value.
  `toObservable` can coalesce signal writes during stabilization, so it is not
  an audit/event stream that preserves every intermediate transition.

## Requests and cache ownership

Choose flattening operators by behavior, not habit:

| Operator | Suitable intent | Contract to preserve |
| --- | --- | --- |
| `switchMap` | Latest search/route read wins | Prior subscription is cancelled; server writes are not rolled back |
| `concatMap` | Ordered commands | Later work queues; bound backlog and stale inputs |
| `exhaustMap` | Ignore duplicate submit while pending | New inputs are dropped, including different keys unless partitioned |
| `mergeMap` | Independent concurrent work | Bound concurrency and correlate out-of-order responses |

Catch recoverable errors inside the request branch so later commands still work.
Model idle/loading/success/empty/error and retry explicitly. Cancel or disregard
stale reads, including after account changes. Unsubscribing from HTTP does not
prove a mutation was never processed; retries of writes need server idempotency
or reconciliation. `finalize` runs on cancellation too: an old request must not
clear a newer request's loading flag.

`HttpClient` streams are cold: multiple subscriptions can issue multiple requests.
`shareReplay({bufferSize: 1, refCount: true})` can share one owned stream but is not
a freshness policy. A completed result can remain replayable; define keys, TTL
or explicit invalidation and user scope. Do not add competing caches in service,
Store, SignalStore and resource for the same data.

Use `resource`/`httpResource`/`rxResource` only after checking availability and
stability in the installed version. Prefer them for parameter-driven reads with
owned loading/error/cancellation semantics, not essential writes that must survive
parameter changes. Handle unavailable/error values and abort behavior explicitly.

Basis: [signals](https://angular.dev/guide/signals),
[RxJS interop](https://angular.dev/ecosystem/rxjs-interop),
[subscription cleanup](https://angular.dev/ecosystem/rxjs-interop/take-until-destroyed),
[HTTP requests](https://angular.dev/guide/http/making-requests),
[resources](https://angular.dev/guide/signals/resource), and
[RxJS shareReplay implementation](https://github.com/ReactiveX/rxjs/blob/7.8.2/src/internal/operators/shareReplay.ts).
