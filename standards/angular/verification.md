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
| Styles/accessibility | [SCSS/style acceptance](#scss-and-style-acceptance), affected viewports, focus/keyboard, overlays and supported theme states |
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

## SCSS and style acceptance

Apply the [style owner's requirements](styles.md) to changed component/global
styles within the shared [readability acceptance](../verification.md#readability-acceptance).
Check SCSS authoring and file references, effective generator defaults when changed,
and the selected builder's global/inline preprocessing options when used. Run the
affected Angular build for changed style wiring or preprocessing; plain `tsc` or
a standalone Sass run does not establish that Angular loads the stylesheet.

Inspect the final source tree and representative emitted selectors. Confirm that
related child/state/responsive rules are grouped under their owner, `&` preserves
same-element states, descendant selectors match the actual template, and nesting
does not create excessive specificity or cross-component dependencies. Check
shared module/theme emission when imports change. A formatter, extension check
or clean Sass compile alone does not establish compliance.

For visual changes, check the affected layout, focus/keyboard, disabled/error and
theme states at relevant viewports, plus overlays/encapsulation when affected.
Record a concise scoped result and resolve in-scope violations before acceptance;
reuse valid evidence and the existing review rather than adding a separate style
review cycle or installing a new test/formatting framework by default.

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
