# Symfony runtime, external effects, and workers

Read for HttpClient, Messenger, kernel events, persistent workers, transactions,
streaming, caches, or shutdown behavior. Apply [PHP ownership](../php/state-effects.md)
and the actual configured transport/runtime; installing a component is not a
requirement to use it for every operation.

## HTTP clients and lazy work

Inject the existing HttpClientInterface or a small integration adapter, with
service-specific base URI, credentials and budgets configured at composition.
Keep user-supplied destinations constrained; a scoped client is not a complete
SSRF policy. Review redirects, credentials and network restrictions when fetching
untrusted URLs; the supported NoPrivateNetworkHttpClient is one relevant control.
[HTTP client](https://symfony.com/doc/7.4/http_client.html).

Responses are lazy. Creating a response is not evidence that status/body handling
succeeded, and dropping it is not reliable fire-and-forget delivery. Failures can
surface during status access, body consumption or destruction. Handle transport,
HTTP-status and decoding failures according to the integration contract; retain
causes without returning upstream internals to callers. Calling getStatusCode()
opts out of the destructor's HTTP-status exception fallback, so inspect that code.

Set idle timeout and overall `max_duration` deliberately. A continuously active
transfer can outlast an idle timeout. For large/untrusted responses, disable
unnecessary buffering, stream bounded data and cancel remaining work on early
return or rejection. Chunk streaming does not itself limit total bytes, decoded
structure, number of requests or process memory. A retry consumes additional
time and needs its own operation budget and an idempotency policy.
The optional [client example](examples/http-client.md) distinguishes 404 absence,
upstream failure, invalid data, timeout and oversized output before returning a
named result, with an owned response cancellation path.

Dispatch concurrent requests only when the workload benefits, and cap fan-out.
Reuse the supported client/runtime; laziness does not make CPU work parallel.
Mocks can verify consumption/errors/options, but do not establish real-network
timing, DNS, TLS, buffering/backpressure or disconnect behavior.

## Messenger delivery and process lifetime

A bus dispatch is synchronous unless configured routing/middleware sends it to a
transport. Make that distinction explicit in the operation's success contract.
Do not queue a local call merely to add a handler abstraction. For asynchronous
work, send a serializable message with stable IDs/data and an intentional schema;
do not send Request, a service, an ORM proxy or an open connection.
[Messenger](https://symfony.com/doc/7.4/messenger.html).

Normal transport delivery can repeat after a worker succeeds but fails before
acknowledgement. Use a stable business idempotency key or an inherently idempotent
operation; a read-before-write check alone is not concurrency protection. Bound
retries/backoff, distinguish permanent failure from transient failure, and define
failure-transport ownership, monitoring and replay procedures. A successful enqueue
does not mean a consumer completed the business effect.

For a database write plus publish, define the transaction/handoff boundary that
actually guarantees the requirement. A database transaction does not atomically
commit an external broker/HTTP call. An outbox or existing durable handoff can be
appropriate when that guarantee is required; do not add it to a read-only or purely
local operation. Doctrine middleware/flush details remain the later ORM topic.

Persistent workers reuse the service graph. Keep services stateless where possible;
reset per-message state with the configured ResetInterface/container mechanism,
including error paths, and avoid disabling reset casually. Separate actor/tenant
context from process configuration. Graceful stop/restart, memory/time limits and
supported signal handling belong to deployment; a handler returning does not reset
every captured object or prove every connection was released.

## Kernel lifecycle and persistence

Understand the affected kernel event and its priority, main-request/subrequest
scope, and exception behavior before adding a listener. A subscriber is useful
for a real cross-cutting framework concern; hidden business orchestration in an
event makes ordering and failure harder to reason about than a direct use case.
[HttpKernel](https://symfony.com/doc/7.4/components/http_kernel.html).

Complete success-critical writes/commits before returning success. Depending on
SAPI and mode, `kernel.terminate` can run after the response is already sent;
it cannot reliably revise that response or guarantee durable background delivery.
Do not move required persistence or enqueue work there to improve apparent latency.
Streaming responses likewise need an explicit point after which status/headers
cannot be changed, plus ownership through actual consumption and disconnect.

Keep cache keys, privacy, invalidation, and tenant boundaries explicit. Symfony
cache, Lock, or RateLimiter components can implement an actual policy, but process
configuration and storage determine their scope; a local cache/lock is not a
distributed invariant. Profile concrete latency, memory and query/HTTP counts
before adding caches, workers or additional layers.
