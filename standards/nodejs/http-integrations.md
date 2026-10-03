# Node.js HTTP and integrations

Read for HTTP servers/clients, body limits, deadlines, persistence or external
effects in Node. Use the selected framework's transport facilities where present;
this is not a requirement to replace them with `node:http`. Shared validation and
domain-state rules remain in [values/state](../javascript/values-state.md).

## Incoming boundaries

HTTP parsing does not validate an application DTO, authenticate a caller or enforce
domain invariants. Apply the accepted parser/schema, then invoke an explicit use
case; map expected outcomes at the boundary and report unexpected failures without
exposing stack traces, credentials or raw upstream bodies. Enforce method/media-type
and size contracts before expensive work. A declared `Content-Length` is not enough:
account for actual received bytes, chunked input and decoded/decompressed sizes.

Distinguish header receipt, whole-request receipt, socket inactivity, keep-alive and
application/dependency deadlines. Node's `requestTimeout` governs receiving the
request; it does not cap the time a use case may spend on a database or API. A
`setTimeout`/`timeout` notification does not itself implement operation cancellation.
Choose compatible proxy/server limits and an explicit abort/destroy response to
expiration; do not blindly copy timeout numbers or disable protection to mask load.

Translate an actual client disconnect into cancellation only where it matches the
operation contract. Inspect the relevant request/response completion state: a
request `close` event alone is not evidence of an interrupted response. A completed
write or durable handoff may need to finish despite losing the client. Track that
work through its actual owner and define what can be retried.

## Outbound boundaries

Use the existing configured client/dispatcher and application-owned lifetime.
Set a real overall budget, propagate cancellation, and include body reading and
decoding in that budget. Successful `fetch` fulfillment is not successful HTTP
status: inspect status, then validate bounded external data as `unknown` at the
adapter. `response.json()` alone neither enforces a size limit nor proves the
domain contract. Consume or cancel response bodies on rejected-status and early
return paths so connection resources do not wait for garbage collection.

Do not inherit browser assumptions: Node fetch does not enforce browser CORS as an
application authorization boundary. For caller-controlled URLs, constrain scheme,
destination and redirects according to the trust boundary, including the network's
DNS/address policy. Preserve TLS verification. Do not forward credentials to an
unvalidated redirect target or log authorization headers.

Retry only failures and methods covered by the actual idempotency contract. Bound
attempts and backoff within the same budget; cancellation and expired deadlines
are not automatic retry triggers. A timeout/reset during a write can leave its
remote result unknown. Preserve causes/codes for internal diagnosis and map only
documented outcomes; avoid text matching an error message or returning empty data
as invented success.

## Persistence and external consistency

Reuse configured pools, acquire per-operation leases with guaranteed release,
and keep transaction work on the driver's required connection/session. Check
whether that client permits concurrent commands; `Promise.all` neither supplies
independent connections nor creates an atomic transaction. Avoid holding a scarce
database connection while awaiting unrelated slow network work unless the use case
requires it. Pool-wait time is part of resource/deadline planning.

Use parameterized driver APIs, explicit result mapping and storage constraints
for contested invariants. Keep transaction/commit/retry ownership with the use case
and adapter. A process-local lock cannot protect state across worker threads,
process replicas or other clients. Database-specific isolation and ORM practices
belong to their profiles, not a generic Node repository hierarchy.

Await required commit or durable handoff before reporting that effect as complete.
Multiple services do not share a transaction because they share a promise chain.
Use the project's idempotency/outbox/reconciliation mechanism when the consistency
requirement warrants it; retain the simpler single-operation path otherwise.

## Basis

[HTTP API](https://nodejs.org/download/release/v24.13.0/docs/api/http.html),
[fetch and abort globals](https://nodejs.org/download/release/v24.13.0/docs/api/globals.html)
and [Undici's fetch notes](https://github.com/nodejs/undici#specification-compliance)
explain transport behavior. Validation, transaction ownership and retry policy are
project requirements, not guarantees supplied by the Node runtime.
