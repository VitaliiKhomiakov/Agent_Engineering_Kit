# Angular component and directive contracts: 2026-11-06

This record supports [component contracts](../../standards/angular/components.md),
[behavioral directives](../../standards/angular/directives.md) and the optional
[executable fixture](../../standards/angular/examples/component-contracts.md).
It is new evidence for this content, not a replacement for the
[2026-09-29 Angular/NgRx record](2026-09-29-angular-ngrx-engineering-practices.md).
The [task plan](../plans/2026-11-06-guidance-quality-and-skill-delivery.md) owns progress
and instruction-artifact checks.

## Versioned sources and local decisions

Reviewed on 2026-11-06:

| Primary source | Relevant contract and evidence boundary |
| --- | --- |
| Angular 20 [input](https://v20.angular.dev/api/core/input) and [output](https://v20.angular.dev/api/core/output) APIs; installed `@angular/core@20.3.0` declarations/runtime | Input/output types and lifecycle; the fixture checks a required binding and intentional output exposure |
| [Queries](https://v20.angular.dev/guide/components/queries) and installed 20.3.0 query contracts | Own-view versus projected-content queries, optional absence and required-match errors; `contentChild` defaults to descendants, `contentChildren` to direct children |
| [Projection](https://v20.angular.dev/guide/components/content-projection) | Static slots do not control creation of projected views; consumer conditionals or an explicit template-fragment API own creation |
| [Directive composition](https://v20.angular.dev/guide/directives/directive-composition-api) | Static host composition, standalone requirement and deliberately exposed inputs/outputs |
| [DOM lifecycle](https://v20.angular.dev/guide/components/dom-apis), [afterNextRender](https://v20.angular.dev/api/core/afterNextRender) and [DestroyRef](https://v20.angular.dev/api/core/DestroyRef) | Render timing and resource cleanup are distinct; browser callback behavior is source-reviewed, not an executed SSR claim |
| [Host elements](https://v20.angular.dev/guide/components/host-elements) and [accessibility](https://v20.angular.dev/best-practices/a11y) | Host binding semantics, native controls and focus responsibilities; no claim of a complete accessibility audit |
| [Zoneless testing](https://v20.angular.dev/guide/zoneless) and [compatibility](https://v20.angular.dev/reference/versions) | Explicit Angular 20 zoneless provider, supported stabilization and the Node/TypeScript/RxJS compatibility ranges |
| [esbuild installation](https://esbuild.github.io/getting-started/#additional-npm-flags) | Disabled lifecycle scripts still require the optional platform binary; the recorded install/build verified this setup locally |

The query guide contains an overbroad direct-child statement before its more
specific descendant-scope section. The specific section and installed 20.3.0
contracts agree on the distinct singular/plural defaults recorded above. The
inputs/outputs guide pages were unavailable through the research browser; API
references, installed contracts and actual compiler/runtime checks supplied the
bounded evidence instead. Moving documentation does not authorize upgrading a
consumer or the earlier Angular/NgRx fixtures.

Keeping one state/host-property owner, preserving existing decorator/NgModule and
ZoneJS choices, limiting aliases, preferring native controls, and choosing
proportionate verification are AEK engineering policies. The fixture demonstrates
their application; it does not require its component shape, styling, runner or
manual-listener implementation in every project. Ordinary host event bindings
remain the simpler default when no adapter lifecycle is needed.

## Executed environment

| Tool/package | Resolved version |
| --- | --- |
| Node / npm | 24.13.0 / 11.6.2 |
| Angular core, common, compiler, compiler-cli, platform-browser | 20.3.0 |
| TypeScript / RxJS / tslib | 5.9.3 / 7.8.2 / 2.8.1 |
| jsdom / its type declarations | 26.1.0 / 21.1.7 |
| Node type declarations / esbuild | 24.13.6 / 0.25.10 |

The temporary environment was `/tmp/aek-s2-2026-11-06-4z80x24i/runtime`.
Its manifest was installed with lifecycle scripts disabled and engine checks
enforced. An initial jsdom 30.1.0 selection required a newer Node version; it was
replaced before acceptance, preserving the selected Angular/Node baseline.
The compatible resolution emitted a transitive `whatwg-encoding` deprecation
notice; this was not a compiler/test failure. No audit or security-assessment
claim follows from the install.

The eight named Markdown blocks are the fixture source of truth. Extraction
confirmed exact equality with the checked files. The generated lockfile and
resolved dependency list are retained under the adjacent `evidence/` directory;
the lockfile SHA-256 is
`ff3c574636356acd7f423adee2f1619576b0f87935c999ac1ac676387dc063e0`.
The source hash map, commands and logs accompany them. A new install from direct
pins alone need not reproduce this transitive resolution; the local evidence
archive is not a portable dependency of an adopted bundle.
After recording results, the runtime, extracted source copy and task npm cache
were removed. Baseline copies and the bounded evidence archive remain available.

## Executed checks and limits

- `npm run build`: Angular `ngc` strict TypeScript/templates followed by esbuild
  bundling of emitted local test modules passed. Plain Node initially rejected a
  generated extensionless import; bundling resolved it without changing compiler
  output by hand. Package imports and the separately preloaded DOM setup remain
  external. This does not establish an Angular CLI application/package build.
- `npm test`: six cases passed, zero failures/skips. They cover optional view
  absence/recreation, consumer-owned projected action changes, host-directive
  aliases, closing intent, focus transfer/return, ignored/handled keys and listener
  destruction. Updates use actual signals/events/render callbacks and
  `whenStable()`, without forced `detectChanges()` or timed waits.
- The default isolated Node reporter exposed only a file-level outcome in this
  environment. A minimal intentional-failure probe confirmed failure propagation;
  the selected single-process command reported all six named scenarios. This is
  an observed harness limit, not a diagnosed Node product defect.
- An isolated invalid consumer failed compilation with both expected diagnostics:
  NG8002 for the unexposed `enabled` input and NG8008 for missing required `title`.
  No schema bypass or type suppression was introduced to silence those errors.
- A temporary omission of `removeEventListener` made the destruction test fail
  on the retained host's `defaultPrevented` assertion, independently of automatic
  output cleanup. The mutation was removed and the complete valid fixture passed
  afterward. The invalid consumer and mutation are not shipped as normal source.
- `npm ls --all --json` passed and records the resolved tree. Strict compilation
  and scoped source review cover the authored TypeScript; a type-aware ESLint
  configuration was not installed or claimed.

This is DOM emulation with synthetic events and focus bookkeeping. It does not
test browser keyboard defaults, layout, screen readers, visual thresholds,
SSR/hydration, forms, NgRx, router integration or native skill activation. Existing
application-specific runners and required gates remain authoritative in consumers.
