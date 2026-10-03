# React engineering practices: evidence and adoption

Research date: **2026-09-21**. Scope: K13 of the [approved plan](../plans/2026-09-21-engineering-practices.md).
This optional research is separate from the [combined entry](../../standards/nextjs.md).
K14 owns Next.js-specific research. Existing Next.js obligations are preserved;
React adoption neither requires Next.js nor starts its migration/adoption stage.

## Versions, scope and strength

The official [19.3 release](https://react.dev/blog/2026/09/09/react-19-3) and public
npm metadata agree on **React/React DOM 19.3.0**. These are the executed versions,
with **@types/react and @types/react-dom 19.3.0**. The current documentation tracks
the latest version, as explained by [React versions](https://react.dev/versions).
Do not infer existing-project API availability from unversioned documentation.

The isolated example project uses existing **Node 24.13.0**, native **TypeScript
7.0.2**, compatibility TS package **6.0.2** reporting compiler/API **6.0.3**,
**ESLint 10.11.0**, **typescript-eslint 8.70.0**, **eslint-plugin-react-hooks 7.1.1**,
**Testing Library React 16.3.3**, **jsdom 30.1.0**, **@types/jsdom 30.0.0** and
**@types/node 24.13.6**. Direct dependencies are pinned; the resolved lock and
verification logs are retained in `/tmp/af-k13-react-pd1657bx`. Manifest-only
reinstallation can change transitive resolution. No workspace/global dependencies
were changed. The installed Node patch is execution evidence, not deployment advice.

All linked primary sources were checked on the research date. Recommendations use:

- **R — framework requirement:** an existing user policy or necessary correctness,
  ownership, trust-boundary or truthful-verification contract, with its reason stated.
- **D — recommended default:** a useful starting choice under a stated condition.
- **O — optional technique:** adopt only for an actual problem and acknowledge costs.

React's API contracts and Agent_Engineering_Kit policy are distinct. Capability-oriented
modules, named interfaces and check proportionality are project choices; React does
not prescribe a business-layer stack, FSD, an ORM, a query cache or a DI container.
Web React DOM is the execution target; React Native rendering/platform behavior is
outside these examples. General purity and ownership guidance still applies where
that renderer supports the relevant APIs.

## Coverage and adopted owners

| Research area | Decision and owner |
| --- | --- |
| 1. Architecture and dependencies | R: cohesive owners and pure rendering; [components](../../standards/react/components-boundaries.md) |
| 2. Idioms, construction and alternatives | D: composition, explicit props and ordinary functions; O: custom Hooks/context for actual reuse/lifetime; components |
| 3. Contracts, validation and errors | R: distinguish text, typed command and authoritative operation; [forms](../../standards/react/forms-contracts.md) |
| 4. State, concurrency and resources | R: identity, cleanup and current-result publication; [state](../../standards/react/state-identity.md) and [effects](../../standards/react/effects-integrations.md) |
| 5. Persistence and integration | R: server/cache ownership and mutation reconciliation; forms/effects; database transaction implementation is outside the client renderer |
| 6. Tests and review | R: evidence at the changed boundary, not private Hook implementation; [verification](../../standards/react/verification-compatibility.md) |
| 7. Security, operations and performance | R: host/trust-aware integration; O: measured memoization/Compiler/code splitting; verification |
| 8. Versions and migration | R: actual renderer/build/library compatibility and authorized migration; entry/verification |

## Components, modules and construction

**Problem:** a screen can collect unrelated transformations, requests and state, or
split into many arbitrary layers without clarifying ownership. [Thinking in React](https://react.dev/learn/thinking-in-react)
provides a UI decomposition and data-flow method. **D:** group cohesive product
capabilities and small private components; use explicit props/children to compose
variation. **R:** preserve the existing project rule to reconsider a component at
roughly 250 lines, as a cohesion signal rather than a React limit. Shared size and
business-boundary rules keep their existing owners.

**Alternative/cost:** a route-local component or ordinary helper is sufficient for
a small interaction; extracting an independent capability improves ownership but
adds imports/contracts. A blanket presentational/container split, mandatory FSD,
base-component inheritance or Repository around every fetch is rejected. The
Next.js feature-structure reference remains conditional; its directory names are
not imposed on a React-only application.

[Custom Hooks](https://react.dev/learn/reusing-logic-with-custom-hooks) reuse React
logic, not the state of separate calls. **D:** extract a Hook for one synchronization
or state responsibility. **O:** context for distant consumers of the same tree-owned
capability; a small prop/callback is simpler for nearby consumers. **Cost:** context
broadens update reach and hidden dependency risk; Hook wrappers can obscure actual
reactive inputs. Construct stable services under the actual lifetime owner, without
introducing a generic frontend container.

[Purity](https://react.dev/reference/rules/components-and-hooks-must-be-pure) and
[Hook rules](https://react.dev/reference/rules/rules-of-hooks) are API constraints.
**R:** keep rendering/updaters repeatable because React may restart work; preserve
immutable input snapshots and place external writes in events or synchronization.
Local construction may mutate its fresh object. **R:** ordinary Hooks keep stable
call order. [`use`](https://react.dev/reference/react/use) has its own conditional
call rules in React 19; do not generalize those to other Hooks or hide suspension
inside try/catch. Existing class components need no unrelated rewrite.

## State, identity and sharing

**Problem:** duplicated/contradictory state diverges from current inputs.
[State structure](https://react.dev/learn/choosing-the-state-structure) and
[sharing](https://react.dev/learn/sharing-state-between-components) support **D:**
minimal source state, derived render values, and the nearest meaningful owner.
**R:** one clear owner per datum prevents conflicting caches and misleading feedback.
URL-owned shareable state uses the selected router contract. A server cache and an
editable draft have different lifetimes; copying a draft is valid only with explicit
initialization, dirty/conflict and reset behavior.

**O:** reducers for related transitions, unions for mutually exclusive outcomes,
context for tree sharing, and an established external store for real cross-tree
needs. **Alternatives/costs:** a pair of local values is simpler for independent
controls; reducers add ceremony, and context alone offers no selector subscription.
[`useSyncExternalStore`](https://react.dev/reference/react/useSyncExternalStore)
supports coherent external snapshots; use the maintained integration when available.
Its unsubscribe, cached snapshot identity and SSR snapshot contract remain necessary.

**Problem:** a list reorder or entity switch gives another item the old draft.
[Preservation/reset](https://react.dev/learn/preserving-and-resetting-state) explains
identity by type/position/key. **R:** use stable data identity for changing lists and
avoid nested component definitions that remount accidentally. **O:** keyed session
reset when all descendant state should be discarded. **Cost:** reset can discard
focus/drafts too. [`useId`](https://react.dev/reference/react/useId) links accessible
elements rather than defining persisted identity.

[Queued updates](https://react.dev/learn/queueing-a-series-of-state-updates) explain
snapshots and functional updates. **D:** derive a next state from the queued previous
value when needed; do not treat a captured event value as magically refreshed.
Refs fit non-rendered handles, not hidden UI state. Batching does not implement a
backend transaction. These decisions apply to supported modern React, not only 19.3.

## Effects, data loading and lifetime

**Problem:** command Effects, leaked subscriptions and older responses produce
surprising duplicates or stale output. [Unnecessary Effects](https://react.dev/learn/you-might-not-need-an-effect)
and [synchronization](https://react.dev/learn/synchronizing-with-effects) support
**D:** compute derived UI during render, perform user commands in handlers/Actions,
and use Effects for external synchronization. **R:** setup owns teardown and reactive
inputs under [`useEffect`](https://react.dev/reference/react/useEffect); ignoring
dependencies conceals lifetime changes. A promise is not an Effect cleanup function.

**D:** existing loader/query ownership before a new fetch Effect. **Alternative:**
a small client-only integration can own its Effect, but then owns pending/error state
and stale settlement itself. **Cost:** raw Effects offer no built-in SSR loading,
cache, deduplication or waterfall prevention. **R:** cancellation and publication
are separate contracts; aborting an old request does not prove it cannot settle.
Both old success and old failure must lose permission to change current output.
This is an application consistency policy, not a claim that React cancels requests.

[Strict Mode](https://react.dev/reference/react/StrictMode) deliberately stresses
purity/lifetime in development. **D:** use those diagnostics and repair cleanup;
reject a `hasRun` flag used to hide the probe. Root/subtree conditions differ, so a
fixed number of requests is not an acceptance contract for arbitrary apps.
[`useEffectEvent`](https://react.dev/reference/react/useEffectEvent) is **O**, available
from 19.2, for non-reactive logic within Effects that reads current committed values.
It adds call-site/lint constraints and cannot replace a needed dependency.

[Suspense](https://react.dev/reference/react/Suspense) handles supported suspending
sources; it does not intercept ordinary Effect fetches. **O:** choose boundaries for
independently useful loading regions using the host/library's integration. **Cost:**
unsupported promise creation can restart work or produce incorrect fallback behavior.
[Transitions](https://react.dev/reference/react/useTransition) and
[deferred values](https://react.dev/reference/react/useDeferredValue) are **O** for
responsiveness. They neither order remote responses nor reduce network/CPU work by
themselves; controlled text updates stay urgent. Check async post-await rules in
the installed version. [Error boundaries](https://react.dev/reference/react/Component#catching-rendering-errors-with-an-error-boundary)
protect rendering regions; ordinary event/async failures require their own owner.

## Forms, validation, mutation and persistence

**Problem:** a valid-looking client form is mistaken for an authorized, still-valid
operation. **R:** retain distinct input representation, typed command and current
state checks. This is inherited core/TypeScript policy. The parser example rejects
ambiguous numeric forms; that strict textual grammar is a declared example choice,
not a universal React requirement. Server operations own authoritative eligibility,
transaction/constraint enforcement and durable effects; React renders their outcomes.
Browser storage may persist a draft but cannot establish a trusted balance or secret.

[Inputs](https://react.dev/reference/react-dom/components/input) support **D:** choose
controlled values for live draft-dependent UI, or uncontrolled FormData for simpler
submit-only needs. **Cost:** a controlled draft requires correct synchronous updates;
changing control mode accidentally produces inconsistent ownership. **R:** retain
labels, error association and meaningful outcome feedback for usable interaction.
Native controls are simpler than recreating keyboard behavior in clickable divs.
Form/query libraries remain the project's choice.

[Forms](https://react.dev/reference/react-dom/components/form) and
[`useActionState`](https://react.dev/reference/react/useActionState) support **O:**
React 19 Actions when they clarify pending/result ownership. Previous state precedes
payload; use an Action prop or Transition dispatch. **Alternative/cost:** an explicit
submit handler remains valid on React 18 and can be simpler. Action queuing/reset
semantics need deliberate handling; uncontrolled fields can reset after an Action
returns validation failure as state. The example uses a controlled draft to retain it.
Known refusals are rendered as outcomes; uncertain integration failure is not success.

[`useOptimistic`](https://react.dev/reference/react/useOptimistic) is **O** for easily
reconciled feedback. **Cost:** rollback, concurrent responses and user expectations
must remain intelligible. Reject automatic optimism for every mutation and treating
pending/disabled UI as idempotency. **R:** backend authorization, status/data validation,
retry semantics and authoritative cache reconciliation have explicit owners.
The client renderer does not supply SQL transactions, an HTTP adapter or a global
invalidation scheme; these are integration requirements, not missing React APIs.

## Verification, security, performance and migration

**Problem:** component-internal snapshots pass while user interaction fails.
[Testing Library](https://testing-library.com/docs/react-testing-library/intro/)
supports outcome/DOM-oriented checks; **D:** use relevant roles, labels and displayed
states. [`act`](https://react.dev/reference/react/act) flushes owned React work for
assertions. **R:** match evidence to the affected boundary under shared verification.
Pure domain checks, renderer interaction and real-browser verification answer
different questions. No mandatory E2E or new runner is imposed for every small edit.

**R:** report DOM-emulator limits: it does not establish visual layout, assistive
technology behavior, real keyboard navigation or network/SSR correctness. **D:**
strict TS plus applicable [Hooks lint](https://react.dev/reference/eslint-plugin-react-hooks)
catch misuse that types alone miss. **Cost:** JSX/toolchain and type-library versions
must agree. A whole-tree snapshot or repeated fresh test campaign is rejected when
existing evidence already covers the changed contract.

**Problem:** browser/server environment differences and untrusted sinks bypass
assumptions. [Hydration](https://react.dev/reference/react-dom/client/hydrateRoot)
requires matching initial output; **R:** diagnose mismatches rather than hiding them.
[Raw HTML](https://react.dev/reference/react-dom/components/common#dangerously-setting-the-inner-html)
requires trust/sanitization decisions; JSX text escaping is not general security.
**R:** protect privileged operations outside the browser and assess advisories for
actual RSC/framework dependencies. The [RSC advisory](https://react.dev/blog/2025/12/03/critical-security-vulnerability-in-react-server-components)
shows why a client-only package assumption cannot describe all server deployments.
This note provides no forever-safe patch list; upgrades recheck current advisories.

**D:** measure render, network and bundle cost before adding optimization.
[`memo`](https://react.dev/reference/react/memo) and related caching are **O**;
correctness must not depend on retained caches. [Compiler](https://react.dev/learn/react-compiler/introduction)
is **O** with explicit build integration, compatibility and rollout costs. React 19
alone does not enable it. Simpler state placement/fewer unnecessary Effects precede
blanket memoization. Code splitting, virtualization and workers need a concrete
cost/benefit and preserved accessibility/loading behavior; no benchmark was executed.

The [19 upgrade guide](https://react.dev/blog/2024/04/25/react-19-upgrade-guide)
records testing/ref/toolchain changes. **R:** preserve supported legacy behavior and
upgrade only with authorization. React 18 does not provide React 19 Action APIs;
Effect Events need 19.2+. React 19.3's stable View Transitions/Fragment refs are
optional, not required modernization. Ref-as-prop/ref cleanup and JSX/type packages
need explicit compatibility review. [Server Components](https://react.dev/reference/rsc/server-components)
have framework/bundler-specific integration constraints; client rendering, SSR and
RSC are not interchangeable. Next.js routing/caching/runtime research remains K14.

## Reconciliation and adoption

Five task-conditioned React sections and two optional examples are registered as
resources of the existing `nextjs` profile. The entry remains short and explicitly
limits Next.js instructions to Next.js projects. Original feature/UI obligations
are relocated to their cohesive owners; original Next.js boundaries and mutation
revalidation obligation are retained. The Next.js feature-structure file is unchanged.

Metadata already recognizes `react`; the catalog now includes that technology in
the combined profile. The separate feature-structure profile still matches Next.js
only. All 17 profile IDs, dependencies and globs remain. TypeScript remains a
mandatory dependency under existing policy; no JS-to-TS migration is implied.
Shared JavaScript, TypeScript, Node and process policies retain their owners.
Resources are copied for independent repositories but do not become automatic
reading routes. Research is not injected into the installed instruction context.

## Executed evidence and limits

The [form example](../../standards/react/examples/reservation-form.md) checks actual
React DOM Action submission, malformed input without stock mutation, independent
state refusal, controlled draft retention and pending/safe failure feedback. Its
operation fixture is not a real backend. The [latest-result example](../../standards/react/examples/latest-result.md)
checks input reset, obsolete success/error, same-input Strict Mode cleanup, unmount
and replacement of the service owner. A focused regression reproduced old-owner
output before the identity guard and passed afterward.

The [plan's K13 record](../plans/2026-09-21-engineering-practices.md#k13-result-and-verification)
owns exact commands, counts and delivery checks. Examples execute only the pinned
19.3 stack. React 18 metadata selection is not a runtime compatibility test. No
browser visual/E2E, screen reader, real API/database, SSR/hydration/RSC, Compiler,
optimistic mutation, external-store runtime or performance benchmark was run.
Synthetic client bundles establish portable routes, not actual agent reading
compliance or token savings. P3–P7 remain planned; stop for user review before K14.
