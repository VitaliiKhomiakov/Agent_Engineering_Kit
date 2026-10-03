# Angular styles and presentation boundaries

Use the [entry](../angular.md); retain the project's CSS/SCSS/utility or component
library choice unless replacing it is the task.

- Colocate component styles with the component and template. Prefer external
  files for substantial styles; small inline styles are valid. Use matching base
  names and keep style rules focused on that component's visual responsibility.
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
  can multiply the output.
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
[style guide](https://angular.dev/style-guide) and
[accessibility](https://angular.dev/best-practices/a11y).
Token organization and override ownership are this framework's conventions.
