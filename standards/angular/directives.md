# Angular behavioral directives

Use the [Angular entry](../angular.md) and
[component contracts](components.md) for the installed API and host semantics.
Use a directive for behavior that augments an existing element without owning a
separate view. Give it a narrow input/output contract; component structure,
business workflows and feature state retain their existing owners.

## Composition and public API

Use `host` metadata for ordinary host bindings and listeners in new compatible
code. Preserve functioning decorator bindings in existing code. Keep attributes,
classes and native behavior consistent with the host; a directive should not
silently replace the consumer's role, accessible name or disabled contract.

`hostDirectives` composes behavior statically; it is not a runtime plugin list and
does not use the composed directive's selector to decide whether to apply it.
The composed directive must satisfy the installed API's standalone requirement.
Its inputs/outputs are not automatically part of the enclosing public API:
expose only the intended members and aliases in the composition declaration.
Keep the internal behavior name and external component contract distinguishable.

The host directive initializes before its enclosing component/directive. Do not
depend on consumer inputs being ready in its constructor, or use hook ordering
to synchronize duplicate state. Define one owner when composed behaviors write
the same host property or respond to the same event. Shared behavior need not
become a base component class or require inheritance across unrelated features.

## Lifetime and browser effects

Prefer Angular bindings to imperative DOM mutation. When a browser adapter needs
an owned listener, observer or timer, create it at the appropriate lifecycle point
and release it with the directive's destruction, including partial/late setup.
Angular-managed host listeners need no second manual removal mechanism. Follow
[reactivity](reactivity.md) for subscription/effect ownership instead of adding a
second subscription policy here.

Browser work that needs rendered DOM belongs in a supported render callback such
as `afterNextRender`, using an injection context or the installed API's explicit
injector option. These callbacks do not execute during server rendering. A
callback's automatic destruction handling does not release resources already
created by that callback: register their cleanup with the owning `DestroyRef` or
equivalent adapter contract. Guard asynchronous setup against a destroyed owner.

Keep event handling bounded to the intended element/interaction. Read current
input state in a long-lived callback rather than capture its initial value.
Honor an event already handled by a nested control where the interaction contract
requires it; avoid consuming unrelated keys or installing multiple competing
global handlers. Browser guards alone do not establish hydration correctness;
use [SSR/hydration verification](verification.md#ssr-and-hydration-when-present)
when those modes are in scope.

## Verify the exposed behavior

Exercise the directive through the actual host and consumer bindings, including
changed inputs, emitted intent and destruction. Verify only the intended aliases
are public when that boundary matters. For manual listeners, a stopped output
subscription alone does not prove removal: observe an independently detectable
event side effect on a retained host after destruction, or use the adapter's
observable resource contract. Use the existing runner and real notification path.

Optional example: [composed dismissal and cleanup](examples/component-contracts.md).
Basis: Angular 20 [composition](https://v20.angular.dev/guide/directives/directive-composition-api),
[DOM lifecycle](https://v20.angular.dev/guide/components/dom-apis),
[afterNextRender](https://v20.angular.dev/api/core/afterNextRender) and
[DestroyRef](https://v20.angular.dev/api/core/DestroyRef).
