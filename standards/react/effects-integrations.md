# React effects, reads and integration lifetime

Read for subscriptions, requests, asynchronous UI and resource ownership.

## Synchronization has a lifetime

Prefer an event handler or Action for a user command. Do not trigger a purchase
from an Effect because a Boolean became true. Derive render data without an Effect.
Use an Effect when committed UI must stay synchronized with an external system.
Declare all reactive dependencies; restructure unstable objects/functions at their
owner instead of suppressing exhaustive-deps. Each setup owns its matching cleanup:
unsubscribe listeners, clear timers, disconnect widgets and signal obsolete work.
Do not return an async function or promise as Effect cleanup.

Strict Mode's development setup/cleanup probes reveal lifetime defects. Make them
safe rather than hiding repeated setup with a `hasRun` ref. Exact probes depend on
root/subtree placement and React version; do not make request-count assertions a
universal contract. Effects do not execute during server rendering.

`useEffectEvent` (19.2+) is optional for non-reactive event logic inside Effects
that needs current committed values. Follow its call-site and lint restrictions;
it does not justify omitting values that must resynchronize the Effect. Plain
dependencies or a focused subscription Hook are often sufficient.

## Reads, races and stale UI

Use the framework loader or accepted query cache when it already owns server data.
A hand-written Effect is reasonable for a small client-only integration, but owns
loading/error state, cleanup and races; it does not supply SSR, caching, deduplication
or waterfall prevention. Keep cache keys sensitive to identity/tenant/parameters,
and define freshness, mutation reconciliation and logout invalidation.

For changing inputs, ensure only the current generation can publish success or
failure. Abort cooperative work to save resources and separately ignore stale
settlement: cancellation may be unsupported or arrive too late. Associate rendered
results with their input so an old result is never labelled as the new entity.
Handle rejection even when obsolete. Abort is not server rollback or proof that
remote work stopped. Retry mutations only under the backend's idempotency contract.

The optional [latest-result example](examples/latest-result.md) demonstrates a
small owned Effect with obsolete success/error guards and cleanup; use a maintained
loader/query library when the actual requirements exceed that example's scope.

## Rendering boundaries and responsiveness

Suspense displays a fallback for supported suspending reads/lazy code. Fetching in
an Effect does not become Suspense-aware merely by adding a boundary. Use the
framework or library's supported integration instead of throwing freshly created
promises from arbitrary renders. Choose boundaries by independently useful UI.

Transitions/deferred values can keep urgent interaction responsive; controlled
text input updates remain urgent. They do not speed up computation, debounce a
request, move CPU work to another thread or automatically order network responses.
When using async transitions, check installed-version rules for updates after
`await` and pending/error ownership. Prefer the existing data layer for ordering.
Error boundaries handle descendant rendering failures, not ordinary event-handler
or asynchronous callback errors; own those outcomes at their source. Supported
Actions have their own error propagation rules.

## Basis

[Effects](https://react.dev/reference/react/useEffect),
[unnecessary Effects](https://react.dev/learn/you-might-not-need-an-effect),
[Strict Mode](https://react.dev/reference/react/StrictMode),
[Effect Events](https://react.dev/reference/react/useEffectEvent),
[Suspense](https://react.dev/reference/react/Suspense),
[transitions](https://react.dev/reference/react/useTransition),
[deferred values](https://react.dev/reference/react/useDeferredValue) and
[error boundaries](https://react.dev/reference/react/Component#catching-rendering-errors-with-an-error-boundary).
