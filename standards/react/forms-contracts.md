# React forms, commands and user-visible contracts

Read for form ownership, external data, mutation outcomes or accessible interaction.
Shared [TypeScript](../typescript.md) and [core](../core.md) rules own runtime
validation and independent business invariants.

- Client-side form validation helps the user; the server validates the contract
  and operation eligibility again. A TypeScript `type`/`interface` or `as`
  assertion does not validate received JSON.
- Define relevant loading, error, empty, and success states. Preserve element
  accessibility, focus behavior, and keyboard interaction.


## Representation is not eligibility

Keep editable input text distinct from a parsed command. Decide trimming, empty,
null, numeric syntax and range intentionally; `Number('')` and a cast are not a
validation policy. A schema library is optional when a small demonstrable parser
is sufficient. API adapters validate unknown responses, status semantics and
public error contracts before exposing typed values to UI.

State-dependent eligibility belongs to the operation using authoritative state.
Disabling a button and parsing a positive quantity cannot reserve inventory or
prevent conflicting writes. The backend owns authorization, transaction/concurrency
control and durable idempotency. Browser storage is a user-controlled convenience,
not a secret store or authoritative ledger; scope and validate persisted drafts.

Use expected business outcomes for actionable refusal; map transport failure to
safe feedback and retain appropriate diagnostics at the integration owner. Avoid
showing raw exception bodies or claiming success when the response is uncertain.
After mutation, reconcile authoritative results with the chosen cache/loader;
React itself defines no general cache invalidation protocol.

## Form state and interaction

Choose controlled inputs when rendering/validation needs the current draft;
uncontrolled inputs with FormData suit a simpler submit-only form. Do not switch
between controlled and uncontrolled modes accidentally. Provide defined string
values/Boolean checked values and synchronous updates for controlled inputs.
A form library is justified by actual complexity and the project's choice.

Use native labels, buttons and form submission where possible. Connect errors and
instructions to the input, announce meaningful outcomes, preserve user input after
failure, and choose focus movement deliberately. Mark pending work and define what
happens to repeated submission; a disabled control alone is not server idempotency.
Do not hide essential errors behind color or remove keyboard operability.

React 19 form Actions and `useActionState` are optional for owned async submission.
Pass the dispatcher through an Action prop or a Transition; the Action receives
previous state before its payload. Sequential dispatch is not a backend transaction.
Known refusals can be returned as state; unexpected thrown failures require the
supported error boundary path. Successful form Actions reset uncontrolled fields;
account for that behavior when returning validation failures as ordinary state.
An explicit onSubmit handler remains valid, particularly on React 18.

Optimistic feedback is optional when reversal/reconciliation is understandable.
Define failure rollback and out-of-order response behavior; `useOptimistic` does
not persist data or prove permission. Avoid optimistic confirmation of an operation
whose actual refusal would mislead the user.

The [reservation form example](examples/reservation-form.md) separates text parsing,
UI outcomes and an independent stateful operation. Its in-memory service is a test
fixture for that boundary, not a browser implementation of trusted inventory.

## Basis

[Inputs](https://react.dev/reference/react-dom/components/input),
[forms](https://react.dev/reference/react-dom/components/form),
[Action state](https://react.dev/reference/react/useActionState),
[optimistic state](https://react.dev/reference/react/useOptimistic). Server trust,
stateful operation ownership and proportionate validation are project policy.
