# Next.js rendering, resources and deployment

Read for streaming, error surfaces, metadata/assets, runtime or deployment changes.

## Useful rendering boundaries

Keep related loading/error/empty states near their screen owner. `loading` and
Suspense allow independently useful UI to stream; avoid serializing independent
reads accidentally, but do not parallelize operations with ordering/authorization
dependencies. Handle rejected work and cancellation at its actual integration owner.
A navigation ending does not prove the remote operation stopped.

Under Cache Components, separate reusable output from request-time work and place
meaningful Suspense boundaries for dynamic regions. Check the installed version's
blocking/prerender diagnostics and opt-ins. Next.js 16.3 Instant Navigation tools
are not a universal requirement, and `instant = false` is an explicit acceptance of
blocking, not a fix for every synchronous-I/O/prerender error. Do not suppress a
missing auth/data boundary merely to make the static shell compile.

Route `error` components need the documented client contract; their scope does not
include every ancestor layout. Root failures need the matching global boundary.
Preserve not-found/redirect behavior and safe production errors. Once streaming has
sent headers, later failure cannot simply replace the HTTP status with a new one;
verify the actual response when status/SEO/crawlers matter. Next.js 16.3 custom
`catchError` boundaries are optional; do not paste them into older versions.

Use the framework metadata conventions for title/canonical/robots/Open Graph data
and its image/font/script facilities where they meet the requirement. Validate
remote image sources narrowly and preserve dimensions/alt text. Keep secrets out
of generated metadata, JSON-LD, page props, RSC payloads and public assets. Fonts or
content fetched during build require an intentional reproducible build dependency;
prefer local assets where offline/controlled builds are required.

## Host capabilities and lifetime

Pick the actual Node, Edge, static-export or adapter target before choosing drivers
and runtime APIs. Edge has a narrower API surface and different feature support;
check the specific convention rather than assuming every Proxy uses Edge. Current
16.x Proxy defaults to Node and has its own runtime restrictions. A static export
has no request-time application server for Actions, sessions or mutable endpoints.
Adapter support for streaming, ISR and cache backends requires explicit verification.

Load configuration at the correct time. `NEXT_PUBLIC_` values are bundled for the
browser at build time and are public; they are not runtime secret injection. Server
values can also be consumed during prerendering, so prove runtime behavior before
promoting one built artifact across environments. Validate configuration without
logging secrets. Preserve the framework's generated instruction files as local
project inputs rather than overwriting them blindly during agent adoption.

For self-hosting, own ingress request limits, trusted proxy headers, health/readiness,
stream buffering and graceful shutdown. Reuse clients under their actual server
lifetime and size connection budgets for instance count. Local files or process
memory are not durable shared storage on arbitrary serverless/multiple-instance
hosts. An `after` callback may suit bounded post-response work; critical delivery
needs a durable job/outbox mechanism rather than an unawaited promise.

Identify cache storage per model: legacy incremental cache and `'use cache'` handlers
are different configuration surfaces. Multiple instances need intentional tag/cache
coordination; deployments need compatible build/assets and Action encryption/skew
handling when applicable. Do not assume a one-process test proves those contracts.
Log operational failures and measure actual build/request behavior without exposing
credential or personal payloads.

## Basis

[Caching/rendering](https://nextjs.org/docs/app/getting-started/caching),
[errors](https://nextjs.org/docs/app/getting-started/error-handling),
[metadata](https://nextjs.org/docs/app/getting-started/metadata-and-og-images),
[Edge](https://nextjs.org/docs/app/api-reference/edge),
[Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy),
[static export](https://nextjs.org/docs/app/guides/static-exports),
[environment](https://nextjs.org/docs/app/guides/environment-variables),
[self-hosting](https://nextjs.org/docs/app/guides/self-hosting),
[`after`](https://nextjs.org/docs/app/api-reference/functions/after) and
[16.3 release](https://nextjs.org/blog/next-16-3).
