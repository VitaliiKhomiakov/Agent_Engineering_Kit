# NgRx Effects and async workflows

Use the [entry](../ngrx.md) for classic `@ngrx/effects`. Angular `effect`, NgRx
`createEffect`, ComponentStore effects and SignalStore `rxMethod` are different
APIs with different ownership; do not use their names interchangeably.

## Work ownership

Components dispatch intent and select state. Effects coordinate external work
through typed adapter services and emit outcome actions. Register functional or
class effects with the installed supported API; construction alone does not run
an effect. Inject dependencies synchronously; prefer functional arguments where
that makes isolated tests simpler.

Use `ofType` and a flattening operator chosen from
[Angular's concurrency table](../angular/reactivity.md). `switchMap` is suitable
for replaceable reads, not a default for essential writes. `exhaustMap` suppresses
all new inputs in that stream while busy; it is not per-entity deduplication.
`concatMap` queues work and `mergeMap` allows out-of-order outcomes. Define keys,
request IDs, queue limits or partitioning when required by the operation.

Catch expected failures inside the inner request and return a failure action.
Do not complete the whole effect on the first error or silently return `EMPTY`
while leaving the UI pending. Map `unknown`/HTTP errors into safe serializable
outcomes. Keep retry bounded and appropriate to the operation; a failed response
does not prove a write was not committed.

Cancellation, logout and replacement must not let old outcomes overwrite a new
context. Explicitly cancel long-running subscriptions or reject stale correlation
IDs in the state transition. Model loading per operation where work overlaps.
If using `finalize`, its cancellation callback must not clear a newer request's
pending state. Optimistic updates require reconciliation/rollback that respects
newer edits, not restoration of an obsolete full-state snapshot.

## Read state and emit outcomes

Use `concatLatestFrom` from the installed package's supported import path (current
`@ngrx/operators`) to sample Store selectors lazily after a relevant action.
The joined selector must have a current value; do not use it as a waiting operator
for a cold HTTP request. Use an explicit flattening/composition step for that work.

Effects observe actions after reducers have processed them. A selector sampled
therefore may contain the state changed by that action. Check this when a reducer
sets `loading` and an effect filters on `!loading`; that filter can suppress the
very request being started. Put deduplication in a coherent owner and test it.

Return an outcome action from the effect stream instead of manually subscribing
or dispatching from `tap`. Prefer one meaningful outcome that interested reducers
can handle; avoid an array of setter actions representing one transition. For
navigation/logging that emits no action, use `{ dispatch: false }`, handle errors
and prevent feedback loops. Do not have an effect redispatch its own trigger
without a bounded, explicit protocol.

For polling/websocket work, specify start/stop, reconnect/backoff and identity
scope. Root Effects do not automatically end when a page disappears. Do not make
route destruction your implicit cancellation contract.

Basis: [Effects](https://ngrx.io/guide/effects),
[operators](https://ngrx.io/guide/operators),
[concatLatestFrom implementation](https://github.com/ngrx/platform/blob/main/modules/operators/src/concat_latest_from.ts),
and [RxJS operators](https://rxjs.dev/guide/operators).
Correlation, idempotency and reconciliation are application contracts.
