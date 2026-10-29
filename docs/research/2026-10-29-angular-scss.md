# Angular SCSS and nested styling: dated evidence

Researched and checked on **2026-10-29** for the user's requested SCSS and nested
style-authoring policy. [Styles](../../standards/angular/styles.md) owns the rules;
the [task](../plans/2026-10-29-angular-scss.md) owns progress and acceptance.
This record supplements the
[earlier Angular evidence](2026-09-29-angular-ngrx-engineering-practices.md)
without changing its executed versions or results.

## Primary sources and policy boundary

| Source reviewed | Conclusion used |
| --- | --- |
| [Angular component styling](https://angular.dev/guide/components/styling) | External component styles and CSS-producing preprocessors are supported. Encapsulation remains a separate Angular concern. Angular does not require SCSS. |
| [Angular CLI new](https://angular.dev/cli/new), [component generation](https://angular.dev/cli/generate/component) and [workspace configuration](https://angular.dev/reference/configs/workspace-config) | Select the stylesheet language for generation; reconcile workspace/project schematic defaults and actual builder options. Defaults do not convert existing files. |
| [Angular CLI 20.3.0 component schema](https://github.com/angular/angular-cli/blob/20.3.0/packages/schematics/angular/component/schema.json) | The component `style` option accepts `scss`; the schema's default is `css`. |
| [Angular application builder 20.3.0 schema](https://github.com/angular/angular-cli/blob/20.3.0/packages/angular/build/src/builders/application/schema.json) | Global style inputs accept SCSS; application inline styles use `inlineStyleLanguage`; Sass include paths are workspace-relative under `stylePreprocessorOptions`. Other builders need their own supported contract. |
| [Angular build 20.3.0 manifest](https://github.com/angular/angular-cli/blob/20.3.0/packages/angular/build/package.json) | The build package pins Sass 1.90.0, used below to align with the earlier Angular example baseline rather than selecting an arbitrary latest compiler. |
| [Sass nesting](https://sass-lang.com/documentation/style-rules/#nesting) | Nested rules combine selectors. Sass recommends keeping selectors shallow and explains selector-list expansion. A source tree need not reproduce every DOM ancestor. |
| [Sass parent selector](https://sass-lang.com/documentation/style-rules/parent-selector/) | `&` denotes the outer selector, including pseudo-classes and same-element variants; suffixes such as BEM elements generate a different selector shape from descendants. |
| [Sass modules](https://sass-lang.com/documentation/at-rules/use/) and [import deprecation](https://sass-lang.com/documentation/breaking-changes/import/) | Prefer the module system for new dependencies. Sass `@import` and global built-ins are deprecated from Dart Sass 1.80.0. Module CSS emission is bounded by the compilation, not every separately compiled component. |

The workspace guide still contains legacy Sass `@import` illustrations. Their
path-resolution examples are not used to override Sass's current module guidance.
Plain CSS imports and dependency-distributed CSS are separate contracts.

Mandatory SCSS, related-rule grouping, declaration ordering and acceptance review
are explicit library policy requested by the user. They are not vendor mandates,
a numeric nesting-depth limit, or permission for a whole-project migration.
Current manuals were consulted as guidance; version-specific field claims above
are bounded to the inspected 20.3.0 schemas. A requested 22.2.0 raw-schema URL
returned 404 and was not treated as verified evidence for that release.

## Executed checks

Environment: Linux, Node **24.13.0**, npm **11.6.2**, Dart Sass **1.90.0**
(`sass.info` reports dart2js 3.8.3). The compiler was installed with an exact
version and lifecycle scripts disabled under
`/tmp/aek-angular-scss-t05l3ced/runtime/`; no repository dependency was added.
The initial sandbox registry DNS failure was not a successful install; the same
temporary installation then succeeded with permitted network access.

The complete SCSS block in the style owner was extracted unchanged as
`order-card.scss`. The JSON fragment was parsed and its SCSS value checked against
the versioned component schema. The inspected application schema contains the
documented inline-language and include-path fields, and the build manifest's
Sass pin matches the tested compiler. This is field-contract inspection, not a
complete Angular workspace validation or a CLI generation run.

`node /tmp/aek-angular-scss-t05l3ced/runtime/check-scss.mjs` executed these checks:

| Scenario | Observed result |
| --- | --- |
| Exact owner example via `sass.compile`, expanded output, source maps disabled | Exit 0 with no warnings; input remained unchanged. |
| Host, owner, child, selected-state, focus and disabled selectors | Expected selectors emitted, including same-element `.order-card.is-selected` and descendant `.order-card .order-card__action:focus-visible`; the focus declaration remained present. |
| Nested media rule | Emitted `@media (min-width: 48rem)` contains the owner's responsive grid declarations. |
| Remove `&` before `.is-selected` in a temporary variant | The compiler emitted `.order-card .is-selected` instead, confirming the semantic difference; compilation alone does not catch an unintended descendant. |
| Load one CSS-emitting module twice under different namespaces in one entry | Shared CSS emitted once in that compilation. |
| Compile a second entry loading the same module | Shared CSS emitted again in the second output, confirming the cross-entry duplication concern. |

To reproduce basic compilation, save the owner's SCSS block in an empty temporary
directory, install `sass@1.90.0` there with `--ignore-scripts`, and run:

```sh
./node_modules/.bin/sass --no-source-map --style=expanded order-card.scss order-card.css
```

The JavaScript harness used the compiler API for assertions and preserved its
generated CSS for inspection. The scoped baseline and evidence copies remain in
`/tmp/aek-angular-scss-t05l3ced/` through handoff; temporary dependencies and caches
are removed after recording results. Library artifact checks and scoped review
are recorded in the canonical task.

## Limits

No Angular application build, generator execution, encapsulation transform,
library/test builder, browser layout, accessibility interaction, SSR or hydration
was exercised. The example is a Sass compilation/selector check, not evidence of
those integrations. Existing Angular/NgRx fixture versions were not changed.
Consumers must use their own supported builder/compiler and execute the affected
integration and visual checks. A formatter or successful compiler cannot certify
the required source grouping; the scoped style review remains binding.
