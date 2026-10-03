# Organizing a Next.js frontend by features

The chosen standard is compact modules organized by product capability, without
requiring full Feature-Sliced Design. The name `features` does not automatically
introduce Pages, Widgets, or other FSD layers and requirements. Record concrete
paths in the application's architecture.

## Compact product-capability structure

Use this structure when the UI and logic need clear owners with few mandatory
levels. This App Router example does not require creating every shown directory:

```text
src/
  app/
    (shop)/checkout/
      page.tsx                  # Route composition
      _components/              # UI local to this route only
    api/orders/route.ts         # Transport entry point, if needed
  features/
    place-order/
      ui/                       # Form/control for the user action
      model/                    # State, schema, and rules for this action
      api/                      # Backend interaction adapters
      server/                   # Server operation, only when needed
      client.ts                 # Public client entry point, if needed
      server.ts                 # Public server entry point, if needed
  entities/
    order/                      # Shared order model, when it has consumers
  shared/
    ui/                         # Domain-independent UI primitives
    api/                        # Shared transport client
    lib/                        # Small libraries with clear purposes
```

Dependency rules for our variant:

- `app` composes use cases; features do not import app.
- A feature uses its own code plus public contracts from entities and shared.
  Features do not import each other's internals. Compose a shared use case above
  them or give it an explicit contract; cycles and hidden dependencies are forbidden.
- Entities do not depend on features or routes. Shared does not know business modules.
- Create a separate entity only when the model has a real shared owner; do not
  move a type used by one feature there merely to fill a layer.
- Shared `shared/ui` contains no checkout rules. A shared API client does not
  become one file containing every domain endpoint.
- Route-local code may remain beside its route. Extract a feature for an
  independent user action, responsibility, or reuse, not for every function and button.
- A module's public interface must preserve the Server/Client split. A barrel
  `index.ts` is optional and does not permit mixing execution environments.

## Migrating from an existing structure

Existing project directories are not exemplary architecture. First describe the
actual dependencies and target owners of capabilities. Move one cohesive use case
at a time while preserving required routes, public imports, metadata, and user behavior.

If the project already uses FSD, map it to the target compact structure and make
the migration a separate task; an ordinary fix does not authorize mass renaming
of layers. Do not create `src/pages` for an abstract screen layer without accounting
for Next.js use of that name for the Pages Router.

A one-off cohesive UI may belong to a route. Introduce a separate module when it
has a clear responsibility, not to meet a layer count. Verify React Server/Client
boundaries against the [Next.js profile](nextjs.md) regardless of directory structure.

## Router adapters and execution contracts

The tree above illustrates App Router. In Pages Router, keep `pages`, API Routes,
`_app` and `_document` under their actual conventions; a shared feature does not
change the router contract. Do not name an abstract feature layer `pages` inside
a router-scanned location. A mixed-router migration must preserve distinct URLs.

Expose server operations through a server-only entry and minimal public data through
an appropriate client contract. `'use server'` declares callable Server Functions;
it is not a generic marker to put on every server module. Pure rules should not
import `next/headers`, router objects or React just to access a request value.
Adapters resolve the request/session and supply the operation's required contract.
A server read may call an existing backend directly; creating an internal HTTP hop
is not a condition for feature reuse.

When those boundaries change, use [routing/composition](nextjs/routing-composition.md)
and [server/client security](nextjs/server-client-security.md); cache ownership is
in [data and mutations](nextjs/data-cache-mutations.md). Load only the sections
needed for the current structure decision, not every linked resource.

## Architecture decisions to record

- Locations of router files and feature modules.
- Owners of primary capabilities, API contracts, and state.
- Allowed import directions and public module entry points.
- Locations of server-only code, form schemas, styles, and colocated tests.
- The selected form, query, state, and UI tools; directory names do not select them.

## Basis and choice

- [Next.js: Project Structure](https://nextjs.org/docs/app/getting-started/project-structure)
  allows different organization approaches, colocation, private folders, and route
  groups. Next.js does not require FSD; this structure is the chosen user standard.

Do not adopt middleware, caching, or framework-file placement rules from a
third-party example without checking the installed Next.js version's documentation.
