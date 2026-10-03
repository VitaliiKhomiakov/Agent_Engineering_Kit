# Next.js verification and version migration

Read when selecting checks, changing build/runtime contracts or upgrading Next.js.
The [shared verification policy](../verification.md) owns check proportionality;
[React verification](../react/verification-compatibility.md) owns UI evidence limits.

## Verify the changed contract

Generate framework route types before relying on `tsc` for helpers/contracts. Run
the project's strict type/lint checks and relevant production build after changes
to routes, server/client imports, caching or runtime configuration. A build can
prerender data and use external assets: isolate fixture dependencies intentionally.
Do not hide diagnostics with `ignoreBuildErrors`, casts or disabled lint rules.
Next.js 16 does not make `next build` an ESLint gate; run configured lint separately.

Direct function tests suit pure invariants but cannot establish the actual Next.js
HTTP, RSC, Actions or cache pipeline. Use the real production host for changed
request contracts, status/output projection, cache freshness and denied operations.
Test a meaningful input/state refusal, not only the happy-path shape. For a Server
Action, invoking its function directly is not evidence of dispatcher/origin/form
behavior. Async Server Component test-tool support varies; a supported integration
or browser check may be needed instead of shallow rendering.

Use a real browser for affected critical navigation/hydration/form interactions
and visual verification for presentation. Server HTML does not prove hydration,
client event handling or back/forward behavior. For modified cache behavior, test
cross-request reuse and post-mutation freshness under the chosen model, separating
server results from client router/CDN state. A development hot-reload result is
not evidence of production caching.

For import boundaries, verify the actual build guard or emitted client assets when
the risk warrants it. Searching for a sentinel proves only that fixture's projection;
it is not a security audit of all possible secrets. Native bundles/portable links
are artifact evidence, not a fresh-session model compliance pilot.

## Compatibility is a scoped decision

Record exact Next/React/React DOM/type/TS versions, cache flags, router, bundler and
adapter. Resolve peers rather than forcing an incompatible install. Next 16.3 can
use a local TS CLI; the documented API-checker mode requires a supported compiler
API. Keep lint and framework generation compatible with the chosen setup, and record
which compiler actually ran. Generated helper signatures are version-dependent.

| Existing model | Migration concerns to verify if an upgrade is authorized |
| --- | --- |
| Pages Router | Data loaders, API Routes, `_app`/`_document`, serializable public props and router behavior; no automatic move to App Router |
| App Router 14 → 15 | Async request APIs and changed fetch/GET/client-route cache defaults; remove transitional synchronous access deliberately |
| 15 → 16 | Required async access, runtime/toolchain minimums, Proxy convention, Turbopack/default build changes, removed `next lint`, image/security/config changes |
| Enabling Cache Components | Explicit cache scopes, Node runtime, segment-option migration, dynamic rendering boundaries and retained route state |
| 16.3 optional features | Instant navigation/prefetch tools, new error APIs and Compiler experiments require their own applicability and checks |

Keep a working legacy approach while it is supported and meets requirements.
Migrate one cohesive route/capability with its callers; do not mix recipes from
different models. Consult the installed package's `dist/docs` where present and
current release/advisory/support information. A pinned example patch is execution
evidence, not a forever-safe deployment recommendation.

Measure client bundles, network/navigation, server rendering and data latency before
adopting code splitting, cache widening or compiler options. A framework benchmark
is not the project's measurement. Reduce unnecessary client dependencies and
waterfalls before adding a generic optimization framework.

## Basis

[Testing](https://nextjs.org/docs/app/guides/testing),
[TypeScript](https://nextjs.org/docs/app/api-reference/config/typescript),
[15 upgrade](https://nextjs.org/docs/app/guides/upgrading/version-15),
[16 upgrade](https://nextjs.org/docs/app/guides/upgrading/version-16),
[16.3](https://nextjs.org/blog/next-16-3),
[support policy](https://nextjs.org/support-policy) and
[August 2026 advisory](https://nextjs.org/blog/august-2026-security-release).
