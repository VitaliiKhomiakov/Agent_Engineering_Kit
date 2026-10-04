# Angular and NgRx engineering practices

Researched **2026-09-29** for the user's requested Angular/NgRx architecture and
coding rules. The [Angular](../../standards/angular.md) and
[NgRx](../../standards/ngrx.md) entries own operational instructions. This note is
optional source evidence, not required reading for every Angular task.
The [plan](../plans/2026-09-29-angular-ngrx-rules.md) owns delivery and checks.

## Scope and choices

The library previously had TypeScript and React/Next.js rules but no Angular or
NgRx profile. This addition follows the existing short-entry/topic-section format.
Angular and NgRx are separate selections; an Angular application may use no NgRx,
only Signals, or classic Store with selected supporting packages.

Three approaches were considered: prescribe Store/Effects everywhere; prescribe
SignalStore everywhere; or route by the state owner's requirements and installed
packages. The third is adopted. It preserves existing applications and recognizes
that event coordination, local UI state and server-cache lifetimes are different
problems. It does not make every state owner a global singleton.

Feature boundaries, one authoritative state owner, named commands, cache/reset
obligations and proportionate verification are framework policy informed by the
mechanisms below. Folder names, a mandatory facade, CQRS, Nx or a universal
Store-to-SignalStore migration are not imposed by Angular/NgRx.

## Versions and source retrieval

Moving Angular pages identified their build as **22.2.0**, and the NgRx site
displayed **v22** during research. These are documentation observations, not a
target application's versions or a recommendation to upgrade it.

Several NgRx web routes exposed only a JavaScript application shell to the web
reader. Their official Markdown sources were read instead, from
[ngrx/platform commit 32c4c74](https://github.com/ngrx/platform/tree/32c4c74bd838cf00f8f318753f44cbd11387754b/projects/www/src/app/pages/guide).
The current path is `projects/www/src/app/pages/guide`; older `projects/ngrx.io`
sources were not used to establish the latest SignalStore contract. A branch
snapshot is not evidence that every API in it exists in an installed release.

Important version distinctions:

- Angular's current OnPush guide says it is the default from v22. The rules retain
  explicit OnPush for earlier versions and examples. Zoneless defaults from v21
  and is a separate scheduling decision; verify actual bootstrap configuration.
- New standalone composition is recommended by Angular, while NgModules remain
  relevant to existing applications. New naming conventions do not make suffix-free
  files invisible to rule selection.
- Resources, Signal Forms, newer SignalStore features and their stability must be
  checked against the installed version. They are alternatives, not required
  replacements for typed Reactive Forms, RxJS or existing stores.
- NgRx recommends Signals for new local state and still supports ComponentStore.
  SignalStore also supports root scope and optional event composition; describing
  it as only a small-component store would be misleading.

## Primary evidence and instruction owners

| Official source | Finding used | Rule owner |
| --- | --- | --- |
| [Angular style guide](https://angular.dev/style-guide) | Feature grouping, cohesive files, presentation boundaries and consistent naming | Angular architecture/styles |
| [Hierarchical injectors](https://angular.dev/guide/di/hierarchical-dependency-injection) | Provider location controls instances; component and environment scopes differ | Architecture/state ownership |
| [NgModules](https://angular.dev/guide/ngmodules/overview) | Standalone preferred for new code; declarations/imports/providers remain distinct | Architecture |
| [OnPush](https://angular.dev/best-practices/skipping-subtrees) | Subtree skipping, event/input triggers and v22 default | Change detection |
| [Zoneless provider](https://angular.dev/api/core/provideZonelessChangeDetection) | v21 default and explicit framework scheduling triggers | Change detection/verification |
| [Signals](https://angular.dev/guide/signals) | Lazy computed values, dynamic synchronous dependencies, equality and template notifications | Reactivity |
| [AsyncPipe](https://angular.dev/api/common/AsyncPipe) | Subscription management and marking the view | Reactivity/change detection |
| [RxJS interop](https://angular.dev/ecosystem/rxjs-interop) | Immediate subscription, initial/error handling and stabilization semantics | Reactivity |
| [takeUntilDestroyed](https://angular.dev/ecosystem/rxjs-interop/take-until-destroyed) | Destruction scope and injection context | Reactivity |
| [Resources](https://angular.dev/guide/signals/resource) | Parameter-driven async reads and abort/error behavior | Reactivity |
| [HTTP requests](https://angular.dev/guide/http/making-requests) | Cold streams, subscription cancellation and generic types without JSON validation | Reactivity/boundaries |
| [Read route state](https://angular.dev/guide/routing/read-route-state) and [guards](https://angular.dev/guide/routing/route-guards) | Reactive params, snapshots and client-authorization limits | Boundaries |
| [Typed forms](https://angular.dev/guide/forms/typed-forms) and [Signal Forms](https://angular.dev/guide/forms/signals/overview) | Reset/nullability, disabled values and version-dependent form choices | Boundaries |
| [Styling](https://angular.dev/guide/components/styling) and [accessibility](https://angular.dev/best-practices/a11y) | Encapsulation limits, avoiding new ng-deep, interaction semantics | Styles |
| [Control flow](https://angular.dev/guide/templates/control-flow), [defer](https://angular.dev/guide/templates/defer) and [performance](https://angular.dev/best-practices/performance) | Stable identity, actual lazy dependencies and profiling | Change detection |
| [Security](https://angular.dev/best-practices/security) | Binding protection and limits of bypass/direct DOM APIs | Boundaries |
| [SSR](https://angular.dev/guide/ssr) and [hydration](https://angular.dev/guide/hydration) | Browser-only behavior, deterministic DOM and per-request state | Verification |
| [Compatibility](https://angular.dev/reference/versions), [template checks](https://angular.dev/tools/cli/template-typecheck) and [testing](https://angular.dev/guide/testing) | Installed toolchain and real template/injector evidence | Verification |
| [Why Store](https://ngrx.io/guide/store/why) and [ComponentStore source](https://github.com/ngrx/platform/blob/32c4c74bd838cf00f8f318753f44cbd11387754b/projects/www/src/app/pages/guide/component-store/index.md) | Shared event-oriented state versus local choices; Signals recommendation without mandatory migration | State architecture |
| [Actions](https://ngrx.io/guide/store/actions), [reducers](https://ngrx.io/guide/store/reducers) and [feature creators](https://ngrx.io/guide/store/feature-creators) | Typed events, pure transitions and feature registration | Store/selectors |
| [Selectors source](https://github.com/ngrx/platform/blob/32c4c74bd838cf00f8f318753f44cbd11387754b/projects/www/src/app/pages/guide/store/selectors.md) and [implementation](https://github.com/ngrx/platform/blob/main/modules/store/src/selector.ts) | Latest-arguments cache, reference comparison, deprecated props and selectSignal | Store/selectors |
| [Effects source](https://github.com/ngrx/platform/blob/32c4c74bd838cf00f8f318753f44cbd11387754b/projects/www/src/app/pages/guide/effects/index.md) and [concatLatestFrom implementation](https://github.com/ngrx/platform/blob/main/modules/operators/src/concat_latest_from.ts) | Effects observe reduced state; inner error recovery; lazy sampling is not waiting for HTTP | Effects |
| [Entity adapter](https://ngrx.io/guide/entity/adapter) | Normalized collections, ID/sort choices and operation semantics | Entity |
| [Router selectors](https://ngrx.io/guide/router-store/selectors) and [configuration](https://ngrx.io/guide/router-store/configuration) | Leaf params, serialization and pre/post-activation timing | Router Store |
| [SignalStore source](https://github.com/ngrx/platform/blob/32c4c74bd838cf00f8f318753f44cbd11387754b/projects/www/src/app/pages/guide/signals/signal-store/index.md) | Injectable scope, ordered composition, protected state and internal updates | SignalStore |
| [rxMethod source](https://github.com/ngrx/platform/blob/32c4c74bd838cf00f8f318753f44cbd11387754b/projects/www/src/app/pages/guide/signals/rxjs-integration.md) | Static/reactive inputs, injector hierarchy and cleanup | SignalStore |
| [Signal entities](https://ngrx.io/guide/signals/signal-store/entity-management) and [events](https://ngrx.io/guide/signals/signal-store/events) | Distinct collection plugin and optional event architecture | SignalStore |
| [Runtime checks](https://ngrx.io/guide/store/configuration/runtime-checks) | Development immutability/serializability; Zone-specific check is not universal | NgRx verification |
| [Store testing](https://ngrx.io/guide/store/testing), [Effects testing](https://ngrx.io/guide/effects/testing), [SignalStore testing](https://ngrx.io/guide/signals/signal-store/testing) and [DevTools](https://ngrx.io/guide/store-devtools) | Mock isolation versus real integration and diagnostics | NgRx verification |
| [RxJS shareReplay 7.8.2](https://github.com/ReactiveX/rxjs/blob/7.8.2/src/internal/operators/shareReplay.ts) | Sharing/replay lifetime is distinct from application freshness | Reactivity |

## Important synthesis and failure scenarios

The framework combines these mechanisms into explicit application contracts:

- An immutable update, a stable selector input and a supported view notification
  serve different purposes. OnPush does not repair stale memoized data, and
  selector memoization does not stop duplicate HTTP requests.
- `switchMap` cancels a subscription, not a committed server mutation. Correlate
  responses and choose command concurrency by semantics. An old finalizer can
  clear a newer request's pending state; the SignalStore example initializes
  loading inside the new branch after previous cancellation.
- Route-scoped injection and lazy state registration do not promise reset on
  every navigation. Specify identity/parameter/logout behavior and verify reuse.
- Entity normalization does not track query membership or freshness. Replacing
  a collection with one page can lose records still needed by another view.
- Store runtime checks, SignalStore protected state, TypeScript readonly and
  backend authorization are distinct protections. None substitutes for the others.
- Read-only records in NgRx do not contradict the library's rich-domain policy:
  state transitions preserve invariants without storing mutable domain objects.

## Executed example checks and limits

The temporary harness is `/tmp/af-angular-ngrx-check`. Dependencies were installed
there with lifecycle scripts disabled; no manifest/runner/runtime dependency was
added to this library. Verified versions: **Node 24.13.0; TypeScript 5.9.3; Angular
core/common/compiler/compiler-cli 20.3.0; NgRx store/signals/operators 20.0.1;
RxJS 7.8.2**. This deliberately tests a compatible older baseline, not all APIs
from the moving v22 manuals.

Six exact TypeScript blocks from the two examples were extracted. `ngc` with
`strict: true`, `strictTemplates: true` and `skipLibCheck: false` passed, including
both component templates. Node execution of four focused cases passed:

1. Selector result identity survives an unrelated root update; filtering returns
   the expected records without mutating frozen source state.
2. A new SignalStore read unsubscribes the old source, ignores stale emissions
   and updates derived count on success.
3. A failure becomes visible state and the same query can succeed on a later call.
4. Separate injectors isolate store instances and destruction cancels pending work.

The runtime harness adds `.js` to one generated relative import for Node ESM;
the documented TypeScript source is unchanged. Tests use a controlled Observable
adapter, not a live API. No browser DOM interaction, full application bootstrap,
ZoneJS/zoneless end-to-end comparison, SSR/hydration, Router Store, Entity or classic
Effects runtime test was executed. These remain target-application checks when
affected; template compilation alone is not evidence of their behavior.

Catalog/resource/link checks and the accountable scoped review are recorded in
the plan. No universal performance improvement is claimed without profiling.

## 2026-10-04 follow-up: ANG-01

The [zoneless forms guidance](https://angular.dev/guide/zoneless#reactive-forms-in-zoneless-applications)
identifies a missing notification boundary for programmatic Reactive Forms updates.
The forms topic now owns that caveat, with a short route from change detection.
[AbstractControl](https://angular.dev/api/forms/AbstractControl) documents form/status
events and emission suppression; owned subscriptions retain the existing reactivity
policy. The verification topic describes hydration/reset, array/validation UI
updates, suppressed events and cleanup through production notification paths.

This is a source/consistency review. No compatible zoneless forms fixture is
present in the library; the historical temporary harness is no longer available
and its recorded cases covered stores, not form DOM updates. No runner, dependency
or forms migration was added. The prescribed future component checks use supported
stabilization without per-update forced change detection. No new Angular rendering,
subscription cleanup or version-matrix execution is claimed.
