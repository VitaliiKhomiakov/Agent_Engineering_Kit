# React verification, compatibility and performance

Read for changed interaction/rendering, tooling, security or migration decisions.
The [shared verification policy](../verification.md) owns check depth and review.

## Evidence at the affected boundary

For a UI change, verify the changed behavior and an appropriate visual rendering.
For a form change, check material input and error paths; for a routing or
Server/Client boundary change, check the relevant build and navigation. Browser
E2E is required for an affected critical use case or mandatory gate, not for every
component or spacing change.


Prefer role/label/text queries and user-visible outcomes over component internals,
private state, full-tree snapshots or render-count quotas. Check relevant stale
success/error, unmount, retry, pending and business-refusal paths. Exercise the real
DOM renderer when the contract depends on Effects, events or accessible markup;
pure functions can use cheaper direct tests. React Testing Library supports that
style; it is not mandatory when the project already has suitable tooling.

DOM emulation checks semantic structure and interactions, not layout, real keyboard
navigation, screen readers, focus rendering or browser networking. Use actual
browser/visual verification for affected presentation or critical journeys. Keep
JSX/build resolution, strict type checks and applicable Hooks lint in the evidence.
Use `act` through supported testing helpers for pending UI updates. React 19
deprecates react-test-renderer and moves `act` to React; do not adopt a new test
suite that depends on unsupported internals.

## Host and security

Server rendering, hydration and Server Components are different mechanisms.
Hydration must start with matching server/client output; avoid time/random/browser
branches that change initial markup. Use the framework's supported client boundary
and data transfer contract; an Effect cannot retroactively fix the initial server
contract. Treat recoverable hydration errors as defects to investigate, not reasons
to blanket-suppress warnings. No universal Next.js route/cache rules apply to React.

Ordinary text interpolation avoids interpreting data as HTML. Raw HTML, URL sinks
and third-party widgets need an explicit trust policy and appropriate sanitization;
JSX is not a general XSS or URL-policy guarantee. Keep credentials and privileged
operations server-side. Review current advisories for the actual renderer/RSC
packages and framework; client-only React and RSC deployments have different
exposure. Do not pin a historical security patch from a research note forever.

## Performance and versions

Measure the affected interaction, network, bundle and render cost before adding
memoization. `memo`, `useMemo` and `useCallback` are optimizations, not correctness
or permanent identity guarantees. Prefer clear state ownership and fewer unnecessary
Effects first. Code splitting, list virtualization and workers have real loading,
accessibility and integration costs; use them for observed needs.

React Compiler is an optional build integration with compatibility and rollout
costs. Verify the actual compiler target/plugin/toolchain before relying on its
memoization; React 19 alone does not mean the Compiler ran. Keep required lint
checks even when compilation is not enabled.

Research checked React 19.3 on 2026-09-21. Preserve supported existing projects:
React 18 has no 19 form Actions/useActionState/useOptimistic; Effect Events require
19.2+. React 19.3 adds stable View Transitions and Fragment refs; these are optional,
not baseline requirements. Ref-as-prop and ref cleanup support are version-sensitive;
preserve legacy forwardRef contracts until an authorized migration verifies callers.
Check matching React/renderer, type packages, JSX transform, libraries and host.
RSC framework/bundler APIs have separate compatibility constraints; do not assemble
an ad hoc server transport from a client example. When Next.js is used, its
[verification and migration section](../nextjs/verification-migration.md) owns
framework build, generated-type and router compatibility checks.

## Basis

[Testing Library](https://testing-library.com/docs/react-testing-library/intro/),
[React 19 upgrade](https://react.dev/blog/2024/04/25/react-19-upgrade-guide),
[Hooks lint](https://react.dev/reference/eslint-plugin-react-hooks),
[hydration](https://react.dev/reference/react-dom/client/hydrateRoot),
[HTML sink](https://react.dev/reference/react-dom/components/common#dangerously-setting-the-inner-html),
[RSC advisory](https://react.dev/blog/2025/12/03/critical-security-vulnerability-in-react-server-components),
[memo](https://react.dev/reference/react/memo),
[Compiler](https://react.dev/learn/react-compiler/introduction),
[React 19.3](https://react.dev/blog/2026/09/09/react-19-3) and
[Server Components](https://react.dev/reference/rsc/server-components).
