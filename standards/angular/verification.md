# Angular verification and compatibility

Apply [proportionate verification](../verification.md) to the affected behavior.
Do not install a new runner, migrate the application or create an E2E suite for
an ordinary local change.

## Version and build contract

Record resolved Angular/CLI/compiler/build, TypeScript, RxJS, Node and used NgRx
versions; consult peer dependencies and Angular's compatibility table. A moving
manual is not a lockfile. Preserve the actual standalone/NgModule and ZoneJS/
zoneless setup. Verify newer inputs, resources, forms and testing APIs before use.

Use `strict: true` and `angularCompilerOptions.strictTemplates: true` for checked
code. Do not silence errors with `any`, `$any`, blanket schemas or disabled template
checks. Use the project's build/lint/test commands and affected configuration;
plain `tsc` does not prove template compilation or lazy route/provider integration.

## Choose evidence by the changed contract

| Change | Relevant checks |
| --- | --- |
| Pure calculation or validation | Focused unit cases for meaningful inputs/errors |
| OnPush/signal/Observable UI | Real component/template update after the actual trigger; empty/error/pending states |
| DI/provider scope | Actual injector resolution, intended sharing/isolation and destruction |
| Route-driven data | Parameter change on reused component, nested IDs, back/forward and stale response handling |
| Form command | Invalid/disabled values, reset semantics, duplicate submit and preserved edits on failure |
| HTTP adapter | URL/body mapping, decoded response/error and cancellation using existing HTTP test tools |
| Styles/accessibility | Affected viewports, focus/keyboard, overlays and supported theme states |
| Bundle/lazy boundary | Production build and relevant size/loading evidence |

Assert observable UI behavior. Do not make a broken notification path pass by
manually calling `detectChanges` after every asynchronous update if production
has no equivalent notification. Test under the configured scheduling mode and
use the runner's supported async stabilization. Read NgRx's
[verification section](../ngrx/verification.md) only when those packages are used.

For affected zoneless Reactive Forms, hydrate/reset programmatically and change a
FormArray or complete async validation. After supported stabilization, assert the
bound values, errors/validity and repeated controls reflect the update through
the production notification path. Include deliberately suppressed form events
when used, and verify an owned notification subscription stops after destruction.

## SSR and hydration, when present

Keep browser-only APIs behind the actual browser/render lifecycle. Server and
client must agree on initial DOM and state; avoid nondeterministic rendering and
untracked direct DOM manipulation before hydration. Stores, transfer data and
HTTP caches containing user data must be scoped per request/application instance,
never process-wide mutable module singletons. Clear account-specific state on
identity changes and avoid serializing secrets into the HTML.

Check request isolation and the affected hydrated interaction, including duplicate
fetching and pending-task completion. Do not infer SSR safety from a passing CSR
unit test. Hydration and persistence require a versioned, validated state contract.

For performance claims, record the scenario, production-like mode and measured
baseline/change. OnPush, computed values and memoization are mechanisms, not
evidence of a universal speedup.

Basis: [compatibility](https://angular.dev/reference/versions),
[template checking](https://angular.dev/tools/cli/template-typecheck),
[testing](https://angular.dev/guide/testing),
[SSR](https://angular.dev/guide/ssr) and
[hydration](https://angular.dev/guide/hydration).
