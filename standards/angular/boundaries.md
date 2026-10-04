# Angular routes, forms and external boundaries

Use the [entry](../angular.md) and the selected state owner's rules.

## Routing

Keep shareable search/filter/sort/page/selection state in the URL when it defines
navigation. Parse route values at the boundary, including missing/invalid IDs;
do not assume all parameters belong to the leaf route. Decide query defaults,
history replacement versus push and back/forward behavior.

Use reactive route reads or supported component input binding when a component
can survive parameter changes; a one-time snapshot is only correct for a
one-time contract. Choose one load trigger (route owner, resolver, or store
workflow) to avoid duplicate fetching. With classic NgRx and route-dependent
state, use [Router Store](../ngrx/entity-router.md) where justified; plain Angular
or SignalStore does not require installing Router Store.

Resolvers that block navigation must have intentional loading/error behavior.
Guards improve navigation UX but cannot secure an API. Lazy loading affects code
delivery, not authorization. Keep sensitive server decisions server-side.

## Forms and component contracts

Use the project's form model. Typed Reactive Forms are a compatible baseline for
complex existing forms. Treat `nonNullable` as reset behavior as well as typing;
disabled controls can be omitted from `.value`, while `getRawValue()` includes them.
Choose intentionally before creating a command. Signal Forms are a separate API;
check the installed version's stability and migration cost before selecting them.

Draft fields, dirty/touched state and intermediate invalid input normally belong
to the form/component, not the global store. Persist a draft only when resumption
or cross-page sharing requires it. Map valid submission into a named typed command;
do not patch every form keystroke into a canonical server entity. Avoid feedback
loops between store hydration and `valueChanges`; distinguish accepted server
state from unsaved edits and define when a new record resets the form.

In zoneless Reactive Forms, programmatic `setValue`, `patchValue`, reset or
`FormArray` changes do not themselves schedule component rendering. When the
template reads form values, validity/errors or array structure, connect the
relevant form events to a template-consumed signal, `AsyncPipe`, or an owned
subscription calling `markForCheck`. Include status changes for async validation;
`emitEvent: false` needs a separate notification path. Bind subscription lifetime
to the component as in [reactivity](reactivity.md); keep the existing forms API.

Inputs are data contracts; outputs express user intent. Use typed `input`/`output`
APIs where supported, while preserving decorator-based components in older code.
Use `model` only for an intentional two-way control contract, not to expose store
mutation to children. Required inputs still need meaningful valid runtime values.

Connect labels, validation messages, pending state and focus management. Suppress
duplicate submit according to the command's concurrency rule, display server
validation/conflict errors, and preserve edits on failure.

## Transport and trust

`HttpClient.get<T>` describes a type; it does not validate JSON. Validate untrusted
responses at the adapter with the project's schema/decoder and map into named
contracts. Return Observable results; state/effects own subscription and outcomes.
Interceptors handle cross-cutting transport work, not feature state transitions.
Do not attach credentials to arbitrary third-party hosts or retry every mutation.

For cookie-authenticated mutations, verify both halves of
[HttpClient XSRF protection](https://angular.dev/best-practices/security#httpclient-xsrfcsrf-security):
the backend provisions a JavaScript-readable XSRF token cookie and validates the
token on protected requests; Angular supplies the corresponding request header.
Keep the authentication cookie's protection separate from the readable token.
Align configured cookie/header names and check the installed version's request
method and URL/origin eligibility. Current documentation (checked 2026-10-04)
includes relative and same-origin mutation URLs, excluding GET/HEAD; do not assume
absolute same-origin support on older versions. Keep read methods free of mutations.
Verify eligible requests carry the token, the server rejects missing/invalid tokens,
and unrelated origins receive neither leaked tokens nor application credentials.
Do not disable protection merely to silence integration failures. Public reads and
explicit bearer-only APIs do not acquire a cookie mechanism from this guidance.

Never use `bypassSecurityTrust*` as a general solution for user HTML/URLs. Prefer
Angular bindings and avoid unsanitized direct DOM insertion. Client bundles and
environment files are public; do not place server secrets there. API authorization
must recheck the current user, resource and operation independently of UI state.

Basis: [route state](https://angular.dev/guide/routing/read-route-state),
[guards](https://angular.dev/guide/routing/route-guards),
[typed forms](https://angular.dev/guide/forms/typed-forms),
[zoneless forms](https://angular.dev/guide/zoneless#reactive-forms-in-zoneless-applications),
[Signal Forms](https://angular.dev/guide/forms/signals/overview),
[HTTP](https://angular.dev/guide/http/making-requests) and
[security](https://angular.dev/best-practices/security).
