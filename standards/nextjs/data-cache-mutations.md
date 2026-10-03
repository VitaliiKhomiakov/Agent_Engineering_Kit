# Next.js data, cache ownership and mutations

Read for server reads, caching, persistence or mutation reconciliation. React's
[state](../react/state-identity.md) and [forms](../react/forms-contracts.md) sections
retain client draft/query ownership; do not create a second store here.

- After a mutation, update data through an agreed mechanism. Verify cache and
  revalidation behavior for the project's Next.js version, not from a general assumption.

## Identify the actual cache model

Record router/version, `cacheComponents`, runtime and host before choosing APIs.
Distinguish render/request memoization, stored server data, prerendered output,
client router state and external CDN/browser caches. They have different keys,
lifetimes and invalidation paths. A fresh browser request or router refresh does
not prove the backing data is fresh. React `cache` request memoization is not a
persistent cross-request data cache.

With Cache Components enabled in Next.js 16, use explicit async `'use cache'`
scopes, `cacheLife` and `cacheTag` for data that may be reused. Inputs/captured values
participate in keys. Read request APIs outside a shared scope and pass only the
required validated identity/tenant arguments when safe; key partitioning alone does
not authorize the caller. Prefer uncached private reads when their freshness and
trust requirements are simpler. Private/remote cache variants are optional and
version/host-sensitive, with operational and latency costs.

Without Cache Components, keep the installed fetch/route-segment/`unstable_cache`
model and deliberately declare freshness. Next.js 15 changed defaults for fetch
and GET handlers compared with 14; cached route output can still surprise callers.
Do not copy `dynamic`, `revalidate`, `fetchCache` or experimental PPR settings across
models. Enabling Cache Components is an authorized migration, not a local cache fix.
Node runtime is required by the current Cache Components contract.

Choose cache keys/tags by the data owner, relevant inputs and visibility. Cache a
minimal projection rather than raw credentials or a session-dependent global result.
Cache lifetime must match tolerated staleness, not an arbitrary "performance" default.
Do not cache writes or use a cached stock/permission read to authorize a transaction.

## Mutation and invalidation are separate responsibilities

Complete the authoritative operation first, then reconcile the affected data/UI.
The operation owns transaction/concurrency, durable effects and idempotency; a
Server Action or Route Handler supplies transport, not those guarantees. Reuse the
appropriate backend/ORM connection lifetime rather than acquiring one per component.
A cache invalidation failure after commit does not undo the write; do not retry the
whole command without its idempotency contract.

| API in the verified 16.3 model | Purpose and condition |
| --- | --- |
| `updateTag(tag)` | Server Actions only; expire tagged data for read-your-own-writes |
| `revalidateTag(tag, 'max')` | Server Actions or Route Handlers; tolerate serving stale data while refreshing |
| `revalidateTag(tag, { expire: 0 })` | A Route Handler/webhook needs the next read to wait for fresh data |
| `revalidatePath(path)` | Invalidate the relevant page/layout path; not a universal replacement for shared data tags |
| `refresh()` / client `router.refresh()` | `refresh()` is Server Action-only; client `router.refresh()` refreshes router output; neither is a general server-data invalidation |

Use the supported two-argument `revalidateTag`; the old one-argument behavior is
deprecated. Choose semantics from the user's consistency requirement. Invalidating
a tag affects assigned cached entries; it does not eagerly refetch every consumer,
authorize the mutation, refresh all open browser tabs or synchronize external caches.

The [tagged-read example](examples/tagged-read.md) demonstrates persistent reuse and
immediate authorized expiration through real requests, plus public server/client
projection. It does not establish SWR timing, Server Action dispatch, router refresh
or distributed invalidation guarantees.

## Basis

[Caching](https://nextjs.org/docs/app/getting-started/caching),
[previous model](https://nextjs.org/docs/app/guides/caching-without-cache-components),
[`use cache`](https://nextjs.org/docs/app/api-reference/directives/use-cache),
[cache lifetime](https://nextjs.org/docs/app/api-reference/functions/cacheLife),
[updateTag](https://nextjs.org/docs/app/api-reference/functions/updateTag),
[revalidateTag](https://nextjs.org/docs/app/api-reference/functions/revalidateTag),
[revalidatePath](https://nextjs.org/docs/app/api-reference/functions/revalidatePath),
[refresh](https://nextjs.org/docs/app/api-reference/functions/refresh) and
[cache migration](https://nextjs.org/docs/app/guides/migrating-to-cache-components).
