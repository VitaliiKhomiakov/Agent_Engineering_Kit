# Angular change detection and performance

Use the [entry](../angular.md). Optimize measured bottlenecks while preserving
correct updates, focus and component identity.

## OnPush is a notification contract

Prefer OnPush for new application components. In versions before Angular 22,
declare `changeDetection: ChangeDetectionStrategy.OnPush`; current v22 docs make
it the default. An explicit setting remains useful in compatible shared examples.
Changing an existing subtree requires checking how its views receive updates.

An OnPush view can be checked after bound inputs change, Angular handles an event
in its subtree, or it is marked for checking. A changed signal read by the
template marks its consumer; `AsyncPipe` marks on emissions. OnPush does not mean
"inputs only", "render once", or "every Observable emission updates any field".

Replace changed input/state references. Mutating an object while preserving its
reference can bypass input/equality checks and selector memoization. An event
that happens to refresh the view does not make such mutation reliable. Setting
an input through an arbitrary child property assignment differs from Angular's
input binding/`ComponentRef.setInput` machinery.

Manual subscription callbacks that assign plain fields need an actual notification
path. Prefer a template-read signal or `AsyncPipe`; use `markForCheck` at an
imperative integration boundary when appropriate. `detectChanges`, detaching views
and blanket eager/default change detection are not routine fixes for stale state.

## Zoneless and ZoneJS

Zoneless scheduling and OnPush subtree checking are separate decisions. Angular
21+ defaults to zoneless; older projects may explicitly use ZoneJS. Verify bootstrap
providers, polyfills and third-party integrations rather than inferring mode from
the package version alone. OnPush is recommended but not a prerequisite for
zoneless correctness; views still need supported change notifications.

Do not rely on arbitrary timers, promises or third-party callbacks causing
zoneless rendering. Route their results into signals/AsyncPipe or mark the view.
Programmatic Reactive Forms updates need that bridge too; see the
[forms notification contract](boundaries.md#forms-and-component-contracts).
For SSR async work outside tracked framework APIs, use the version's pending-task
contract so serialization waits for required work. In ZoneJS applications, isolate
measured high-frequency external work with `runOutsideAngular` where appropriate,
then re-enter/notify when UI state changes. Do not add NgZone workarounds to a
zoneless application without a concrete requirement.

## Reduce work and preserve identity

- Move expensive filtering/sorting to memoized selectors or `computed`; keep
  cheap template expressions simple. Do not call HTTP, dispatch or construct
  subscriptions in getters/templates. Signal getter calls are normal.
- Use `@for (...; track item.id)` in compatible versions, or `trackBy` with older
  `*ngFor`. Use a stable unique business ID; indexes suit only truly static lists.
  Tracking limits DOM churn but does not virtualize a long collection.
- Use lazy routes and `@defer` for suitable noncritical content. Confirm actual
  chunking/dependency restrictions and accessible placeholders/error states.
  Avoid delaying primary content or loading it twice via competing triggers.
- For very large lists, choose pagination or virtualization based on measured
  DOM/memory cost. Preserve keyboard navigation, scrolling and identity.
- Measure initial bundle/load separately from interaction/rendering time. Use
  Angular DevTools/browser profiles and actual build budgets; OnPush alone does
  not fix expensive algorithms, too many DOM nodes or duplicate HTTP requests.

Basis: [OnPush](https://angular.dev/best-practices/skipping-subtrees),
[zoneless provider contract](https://angular.dev/api/core/provideZonelessChangeDetection),
[signals](https://angular.dev/guide/signals),
[AsyncPipe](https://angular.dev/api/common/AsyncPipe),
[control flow](https://angular.dev/guide/templates/control-flow),
[deferred loading](https://angular.dev/guide/templates/defer) and
[performance](https://angular.dev/best-practices/performance).
