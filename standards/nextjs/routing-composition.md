# Next.js routing and application composition

Read for routes, layouts, parameter contracts, navigation or module ownership.
The [entry](../nextjs.md) selects guidance; [feature structure](../nextjs-feature-structure.md)
owns the project's compact capability organization and import directions.

## Router and version first

Record the versions of Next.js, React, and TypeScript; the App or Pages Router;
the server runtime; and the approaches to styling, forms, and state management.
Do not apply App Router requirements to the Pages Router or upgrade the stack to
match a documentation example. The project selects its state, UI, CSS, and lint libraries.

- Routing files compose the screen, parameters, and framework configuration. A
  server page may load data for composition; it does not become a universal
  business service. Reusable operations belong to their owner.

In App Router, `page` exposes UI, `layout` composes persistent shared UI and `route`
exposes HTTP methods. Do not put a page and Route Handler at the same URL segment.
Private folders/route groups organize code without implying an application layer;
check URL collisions and root-layout transitions. Use parallel/intercepted routes
only for a real navigation experience and account for direct loads and slot defaults.
A filename is a framework adapter, not permission to concentrate all business rules.

Await `params`, `searchParams`, `cookies()` and `headers()` where the installed API
is asynchronous; React/client consumers use the supported unwrapping mechanism.
Typed/generated parameter shapes do not validate a slug's meaning or a query value.
Handle absent, repeated and invalid query fields explicitly. Generated `PageProps`,
`LayoutProps` and `RouteContext` require the matching generation step.

Pages Router retains `pages`, `_app`, `_document`, API Routes and its own data-loading
contracts. Choose `getServerSideProps` for request-time data or static generation/ISR
where appropriate to that router. Returned page props become client-visible, even
when their loader runs only on the server. Do not paste App Router RSC or Route
Handler signatures into Pages APIs. Router migration is a separate authorized task.

## Own the integration once

Server Components can call an authorized server read or existing backend directly.
Avoid fetching the application's own Route Handler merely to reuse server code:
that adds HTTP overhead and may fail at build time when no server is listening.
Expose a Route Handler when browsers, webhooks or external consumers need an HTTP
contract. An existing independent backend remains its own authority; a new BFF
should add an actual aggregation or trust boundary rather than duplicate its rules.

Use thin framework adapters around existing capability contracts. Public HTTP
contracts own status/content type, input/body budgets, authorization, safe error
projection, rate limits and cancellation/deadlines as required. Webhooks verify
authenticity using the exact required raw bytes before parsing; avoid an open proxy
that forwards arbitrary client URLs or credentials. No generic controller/repository
hierarchy is required for one endpoint.

Prefer the router's Link/navigation APIs for local navigation. Treat user-supplied
redirect/href targets as untrusted. Test reload/back/forward and deep links when
routing changes. Layout persistence, template remounting and Cache Components'
retained UI state affect reset/focus expectations; React owns the general state rules.

## Basis

[Project structure](https://nextjs.org/docs/app/getting-started/project-structure),
[layouts/pages](https://nextjs.org/docs/app/getting-started/layouts-and-pages),
[Route Handlers](https://nextjs.org/docs/app/getting-started/route-handlers),
[route API](https://nextjs.org/docs/app/api-reference/file-conventions/route),
[Pages server props](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props)
and [BFF](https://nextjs.org/docs/app/guides/backend-for-frontend). The module layout
is project policy, not a mandated Next.js architecture.
