# Example: tagged server data and a minimal client projection

Read when cache reuse, invalidation and server/client output need concrete evidence.
This optional example supports [data/cache policy](../data-cache-mutations.md).
Use the shared setup, dependencies and runner from the
[authorized-command example](authorized-command.md#setup-in-a-temporary-directory),
plus the files below. Both scenarios form one small production-build fixture.

`readCatalog` validates local fixture data, projects a public DTO and caches that
result using Cache Components, `cacheLife('hours')` and a fixed public tag. The
catalog is public and shared: this key is deliberately not suitable for tenant- or
session-dependent output. Internal cost is neither cached in the DTO nor passed to
the client. A real read adapter would own storage/network validation and credentials.

`connection()` keeps the HTTP response request-time while the explicit data read
remains cached. Thus an HTTP no-store header does not erase the server data cache.
The protected invalidation endpoint expires only the fixed tag using `{ expire: 0 }`
because the next read must be fresh. It does not accept arbitrary caller-supplied
tags and does not use Server Action-only `updateTag`. The fixture editor capability
represents permission to administer this public catalog; real scopes need their own
policy. A webhook would verify its signature rather than copy this test token map.

The server page passes only `title` into a small Client Component. The `'use client'`
directive allows interaction but does not prevent initial server rendering. The
button is boundary illustration; browser hydration and clicking it were not tested.

## Files

### `features/catalog/read.ts`

```ts
import 'server-only';
import { readFile } from 'node:fs/promises';
import { cacheLife, cacheTag } from 'next/cache';

export interface PublicCatalog { readonly title: string }
export async function readCatalog(): Promise<PublicCatalog> {
  'use cache';
  cacheLife('hours');
  cacheTag('public-catalog');
  const path = process.env.AF_CATALOG_FILE;
  if (!path) throw new Error('Catalog fixture not configured');
  const value: unknown = JSON.parse(await readFile(path, 'utf8'));
  if (typeof value !== 'object' || value === null
    || !('title' in value) || typeof value.title !== 'string') {
    throw new Error('Invalid catalog fixture');
  }
  // Internal fields in the fixture never become part of the public DTO/cache.
  return { title: value.title };
}
```

### `app/api/catalog/route.ts`

```ts
import { connection } from 'next/server';
import { readCatalog } from '../../../features/catalog/read';

export async function GET(): Promise<Response> {
  await connection(); // Keep the HTTP response request-time; cache only the explicit read.
  return Response.json(await readCatalog(), { headers: { 'Cache-Control': 'no-store' } });
}
```

### `app/api/revalidate/route.ts`

```ts
import { revalidateTag } from 'next/cache';
import { authenticate } from '../../../features/reserve/session';

export function POST(request: Request): Response {
  const actor = authenticate(request);
  if (!actor) return new Response(null, { status: 401 });
  if (!actor.canReserve) return new Response(null, { status: 403 });
  // This endpoint requires immediate freshness on the next read, not SWR.
  revalidateTag('public-catalog', { expire: 0 });
  return new Response(null, { status: 204 });
}
```

### `features/catalog/CatalogTitle.tsx`

```tsx
'use client';
import { useState } from 'react';
import type { ReactElement } from 'react';
export interface CatalogTitleProps { readonly title: string }
export function CatalogTitle({ title }: CatalogTitleProps): ReactElement {
  const [expanded, setExpanded] = useState(false);
  return <section>
    <h1>{title}</h1>
    <button type="button" aria-expanded={expanded} onClick={() => setExpanded(value => !value)}>
      Catalog details
    </button>
    {expanded && <p>Public catalog information.</p>}
  </section>;
}
```

### `app/page.tsx`

```tsx
import type { ReactElement } from 'react';
import { readCatalog } from '../features/catalog/read';
import { CatalogTitle } from '../features/catalog/CatalogTitle';

export default async function Page(): Promise<ReactElement> {
  const catalog = await readCatalog();
  return <main><CatalogTitle title={catalog.title} /></main>;
}
```

### `app/layout.tsx`

```tsx
import type { ReactElement, ReactNode } from 'react';
export interface RootLayoutProps { readonly children: ReactNode }
export default function RootLayout({ children }: RootLayoutProps): ReactElement {
  return <html lang="en"><body>{children}</body></html>;
}
```

## Observed evidence and limits

The shared HTTP runner first sees the cached initial title after the backing file
changes, including after denied invalidation requests. Authorized expiration then
makes both the API read and page HTML expose the updated title. No private sentinel
or internal field name appears in the rendered page. This proves the exercised
public projection, not a general secret scan. The build prerenders `/` and retains
three request-time Route Handlers, as shown by its route report.

A separate temporary copy adds `import './read'` to `CatalogTitle.tsx`. Production
compilation rejects that client import of the server-only module. The published
source remains unchanged and has a successful build; the negative probe is not
part of the runnable application.

Executed only Next 16.3.5/Cache Components on a local Node server with webpack and
a controlled file fixture. No Pages Router, previous cache model, SWR timing,
Server Action/updateTag/refresh path, browser router cache, CDN, remote cache handler,
distributed tag propagation, Edge/static-export target or deployment adapter was
executed. The build/runtime fixture environment and single-process cache are not
production durability guarantees. The fixed hours lifetime illustrates a deliberately
stale public read, not a general recommendation for inventory or authorization.
