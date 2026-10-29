# Angular styles and presentation boundaries

Use the [entry](../angular.md). SCSS and nested style authoring below are binding
library policy for Angular work, subject to explicitly accepted project
exceptions. Angular supports several stylesheet languages; it does not mandate
this choice. Retain the selected component library and its supported integration.

## SCSS source and Angular setup

- Use SCSS for application-authored component and global styles. Colocate a
  component's `.scss` file with its TypeScript and template, using matching base
  names and the supported `styleUrl`/`styleUrls` reference. Keep shared global
  source in an owned SCSS entry such as `src/styles.scss`.
- Apply this to new styles and styles whose authoring changes in scope. Convert
  the affected owned stylesheet and its references together; do not convert
  unrelated legacy files or rewrite vendor/generated CSS. A real builder or
  integration incompatibility needs an explicit project decision, not a silent
  fallback to CSS/Less. SCSS selection does not authorize a dependency upgrade.
- For a new CLI application, select `ng new <name> --style=scss`. In an existing
  workspace, set the effective `@schematics/angular:component` default to
  `"style": "scss"`, reconciling workspace and project overrides. Generation
  defaults neither rename existing files nor change their references.
- Keep the actual global SCSS path in the selected build target's `styles`
  configuration. Prefer external component files; if small inline styles are
  retained, verify SCSS preprocessing in that builder (the application builder
  uses `inlineStyleLanguage: "scss"`). Check test/library builders separately;
  an application option is not proof of support in every builder.
- Use the project's supported Dart Sass/build integration. Prefer relative module
  paths; configure `stylePreprocessorOptions.includePaths` only for an actual
  shared path and in each target that needs it. Do not add another Sass pipeline
  or install tooling at the instruction library's root.

For example, merge this generator-default fragment into the appropriate existing
workspace or project configuration; it is not a complete `angular.json`:

```json
{
  "schematics": {
    "@schematics/angular:component": {
      "style": "scss"
    }
  }
}
```

## Nested style authoring

- Write related styles as a shallow tree under their owning component/block.
  Nest owned child elements, states, variants and local responsive rules there
  instead of maintaining a flat list that repeatedly spells the same owner.
  Merely changing a file extension to `.scss` does not satisfy this requirement.
- Use `&` for the current selector's pseudo-classes, pseudo-elements, attributes
  and same-element modifier classes, such as `&:focus-visible`, `&::before` or
  `&.is-selected`. A nested child selector denotes a descendant; use it only for
  a real relationship in the template. A child combinator requires a real direct
  child. Preserve the selector's meaning when converting existing CSS.
- Keep the source tree and emitted selectors shallow. Group by visual ownership,
  not every DOM wrapper; do not reproduce the full template hierarchy, multiply
  selector lists, or increase specificity merely to make a tree. When existing
  BEM names are used, `&__element` can group them in source while emitting a flat
  class selector; it does not imply a descendant selector or require BEM adoption.
- Keep independent owners and `:host` rules at the top level when appropriate.
  A single simple rule needs no artificial wrapper or nesting. Put an owner's
  `@media` rules with that owner; shared tokens, module directives, keyframes and
  genuinely global rules retain their appropriate scope.
- Keep declarations before nested rules within a block for a predictable reading
  order. Separate sibling blocks visibly and follow the project's formatter.
  Formatting or successful Sass compilation alone does not prove this grouping;
  apply the [style acceptance check](verification.md#scss-and-style-acceptance).

This complete `order-card.scss` example assumes a template with an `.order-card`
wrapper containing `.order-card__title` and `.order-card__action`. The action is
a button; `is-selected` belongs on the wrapper itself. Bind real UI state through
the component's existing presentation contracts.

```scss
:host {
  display: block;
}

.order-card {
  display: grid;
  gap: var(--space-3, 1rem);
  padding: var(--space-3, 1rem);
  border: 1px solid var(--border-color, #d0d7de);

  &.is-selected {
    border-color: var(--accent-color, #075fcd);
  }

  .order-card__title {
    margin: 0;
  }

  .order-card__action {
    justify-self: start;

    &:focus-visible {
      outline: 2px solid currentColor;
      outline-offset: 2px;
    }

    &:disabled {
      opacity: 0.6;
      cursor: not-allowed;
    }
  }

  @media (min-width: 48rem) {
    grid-template-columns: 1fr auto;
    align-items: center;
  }
}
```

Before Angular's encapsulation transform, the relevant emitted selectors are
`.order-card.is-selected`, `.order-card .order-card__title`, and
`.order-card .order-card__action:focus-visible`. Writing `.is-selected` without
`&` inside the owner would target a descendant and change the contract. Sass
compilation checks those expansions, not Angular scoping or browser rendering.

## Shared Sass and presentation boundaries

- Use namespaced `@use` for new Sass module dependencies and `@forward` only for
  an intentional shared API. Keep those directives at their supported module
  scope, not inside the selector tree. Avoid new Sass `@import` and deprecated
  global built-in calls; use supported `sass:` modules. Plain CSS imports and
  dependency-distributed styles are a different contract, not a reason to rewrite
  vendor files.
- Use default emulated encapsulation unless a concrete integration requires
  otherwise. Global rules can still affect an emulated component; encapsulation
  is neither a complete CSS firewall nor a security boundary.
- Keep global files for reset/base typography, design tokens/themes and deliberately
  shared primitives. Prefer CSS custom properties for runtime theme values and
  documented library theming APIs for Material/CDK or another component kit.
- Do not introduce `::ng-deep` for new code. Avoid disabling encapsulation to
  solve a local selector problem. Prefer a documented input, CSS variable,
  supported theme API or a narrowly namespaced global override with an owner.
  Existing compatibility overrides should state their scope and removal condition.
- Do not style another feature's private DOM or generated Angular attributes.
  Overlay content may render outside the component subtree; use the library's
  supported overlay class/theme hooks rather than assuming ancestry.
- Keep selectors shallow, specificity predictable and tokens reusable. Do not
  solve ordering problems by accumulating `!important` or deeply nested SCSS.
  Emit shared theme CSS once; importing a CSS-generating theme in every component
  can multiply the output. `@use` loads a module once per Sass compilation, not
  once across every independently compiled component. Reuse non-emitting
  tokens/functions/mixins in components and emit global theme styles at their owner.
- Prefer simple class/style bindings for dynamic presentation. State chooses a
  semantic variant; styles own its appearance. Do not store CSS class strings or
  DOM elements as domain state.
- Preserve visible focus, contrast, reduced-motion preferences and usable layouts
  across the supported viewports. CSS hiding does not replace accessible labeling
  or authorization. Check affected states, not just the ideal populated screen.

Shadow DOM changes integration and event/style behavior; choose it deliberately
and verify the component library, overlays and theming. Do not adopt an experimental
encapsulation mode from a newer manual without checking the installed release.

Basis: [component styling](https://angular.dev/guide/components/styling),
[workspace configuration](https://angular.dev/reference/configs/workspace-config),
[Sass nesting](https://sass-lang.com/documentation/style-rules/#nesting),
[parent selectors](https://sass-lang.com/documentation/style-rules/parent-selector/),
[Sass modules](https://sass-lang.com/documentation/at-rules/use/) and
[accessibility](https://angular.dev/best-practices/a11y).
The [dated SCSS evidence](../../docs/research/2026-10-29-angular-scss.md) separates
source review, executed compilation and integration limits. Mandatory SCSS,
tree-shaped authoring, token organization and override ownership are library policy.
