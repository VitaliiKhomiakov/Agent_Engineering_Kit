# Next.js server/client and trust boundaries

Read for RSC/client imports, public data, sessions, Server Actions or privileged work.
[Core](../core.md) owns shared invariants; [TypeScript](../typescript.md) owns
static typing requirements only when TypeScript is used.

## Execution and data exposure

- In the App Router, preserve server execution where browser capabilities are not
  needed. Put `'use client'` at the required interactive boundary, rather than on
  the whole tree for one event handler.
- Separate server and client imports. Use a supported guard against client imports
  for server-only modules. A `.server.ts` suffix alone is not such a guard.
- Do not export server database/secret access and client hooks through one shared
  entry point imported by the browser. Separate entry points when both environments
  exist; do not create them preemptively for a client-only component.
- Across a Server → Client boundary, pass client-facing data that React can
  serialize. Domain instances with methods and ORM objects are unsuitable
  transport contracts.
- Route Handlers and Server Actions are thin server entry points. Every externally
  accessible entry point validates data and authorization, then invokes the
  required operation. A UI or layout check does not replace operation authorization.

`'use client'` declares a module dependency boundary, not "render only in a browser".
Client Components can be prerendered on the server and then hydrated. Do not access
browser globals at module initialization or assume their initial HTML differs safely.
Server-rendered children may be passed through a client wrapper; importing a server
implementation into its client dependency graph is a different operation.

Use explicit public projections. React's serialization contract is broader than
JSON, but serializability never establishes permission to expose a field. Ordinary
functions cannot cross as arbitrary callbacks; supported Server Function references
are an explicit framework mechanism. Do not ship tokens, ORM records or private
fields just because the component only displays one property. Use `server-only`
where server dependencies must fail a client import; naming alone cannot enforce it.

## Authority at the operation

Obtain identity from the established server session/auth provider, then check role,
tenant and resource ownership near the protected operation. Keep session verification
and minimal DTO projection under a coherent server owner; an existing API may own
that instead. Avoid building a new authentication system as routine frontend work.
A layout check, hidden button or Proxy redirect only improves navigation behavior.
Public actions, API routes and direct operation callers retain their own authority.

Treat Server Actions as callable endpoints: validate arguments/FormData, recompute
eligibility from current state and constrain output. An action ID, encrypted closure,
bound argument or TypeScript signature is not authorization. Extract named input
fields; FormData may include React's `$ACTION_` fields, so do not blindly persist
`Object.fromEntries(formData)`. Expected refusal belongs in the UI's typed result;
unexpected failures need safe reporting. Keep redirect/notFound control flow out of
broad catches that would turn it into an ordinary failure.

Next.js Action origin checks are useful defenses, not a general CSRF policy for all
Route Handlers. Cookie-authenticated custom mutations need the project's CSRF/origin
controls; explicit bearer APIs have a different credential model. Configure trusted
proxy/origin behavior narrowly and inspect actual forwarded headers. Validate
webhooks and external APIs at their own boundary. Apply body/time/rate budgets at
the responsible app/ingress layers; a client-side limit is insufficient.

Read request-scoped credentials per request; do not cache a user's identity in a
process-global object or public persistent cache. Server-only code can still return
sensitive data, so guard imports and output separately. Taint APIs are optional
additional diagnostics, not a replacement for projection and authorization.

The optional [authorized-command example](examples/authorized-command.md) exercises
a real HTTP entry and independent operation. Its token map and local stock are
explicit verification fixtures, not production authentication or persistence.

## Basis

[Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components),
[data security](https://nextjs.org/docs/app/guides/data-security),
[authentication](https://nextjs.org/docs/app/guides/authentication),
[Server Actions](https://nextjs.org/docs/app/getting-started/updating-data),
[cookies](https://nextjs.org/docs/app/api-reference/functions/cookies) and
[Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy).
