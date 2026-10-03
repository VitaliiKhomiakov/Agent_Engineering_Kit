# NgRx verification and tooling

Apply [Angular verification](../angular/verification.md) and the shared
[proportionate-check policy](../verification.md). Test actual transitions and
integration risks, not every action creator or the internals of NgRx itself.

## Focused evidence

| Changed behavior | Useful evidence |
| --- | --- |
| Reducer/domain transition | Valid and invalid outcomes, original state unchanged, unrelated references preserved |
| Derived view/memoization | Correct projection and stable result identity after an unrelated update; relevant change recomputes |
| Effect/rxMethod | Success/error followed by a successful later trigger; cancellation/ordering/duplicate behavior selected by the operation |
| Concurrent or optimistic writes | Correlated out-of-order responses, conflict/reconciliation and newer edits retained |
| Entity/query state | Partial update semantics, missing selected ID, independent pages retaining shared records |
| Router-driven state | Parent/leaf params, cancelled/reused navigation, back/forward and one load trigger |
| Scoped store | Intended shared versus independent instances, reset/account change and subscription cleanup |
| Component binding | Actual AsyncPipe/signal view updates under OnPush and the configured scheduling mode |

Use reducer/selector functions directly for pure contracts. `provideMockStore`
and overridden selectors are suitable for component isolation, but cannot verify
real reducer registration, selector composition or memoization. Test the full
selector invocation when its caching contract matters, not only `.projector`.

For Effects, use existing `provideMockActions`/functional dependency injection
and RxJS TestScheduler or the runner's supported scheduling tools. Prefer
deterministic time to arbitrary delays. Include actual provider integration when
registration changed; isolated stream tests cannot find missing feature providers.
SignalStore tests should use the intended injector scope and real methods, checking
computed outcomes and destruction. Do not freeze a store so broadly that framework
internals fail instead of detecting the application mutation.

## Runtime checks and diagnostics

Keep Store state/action immutability checks enabled during development. Prefer
serializable state/actions and enable corresponding checks plus action-type
uniqueness in compatible new Store configurations. Record a bounded legacy
exception instead of disabling all checks to hide a mutation. Minimal/custom
serializable Router Store state is compatible; full snapshots are not.

`strictActionWithinNgZone` is specific to ZoneJS applications and is not a blanket
requirement. Do not enable it for zoneless merely because a documentation example
enables every flag; verify actual notification paths instead. Development runtime
checks are not production validation, and classic Store checks do not automatically
apply to SignalStore.

Use Store DevTools deliberately: bound retained history and restrict/sanitize
sensitive payloads; choose production enablement explicitly. Never persist or
export credentials as ordinary diagnostic state. Persist only necessary validated,
versioned data with identity scoping and reset/migration behavior. Action replay
is not a guarantee that an external side effect is safe to execute again.

Before adopting an NgRx API, check the actual package export and peer versions.
Do not assume moving docs, an older code sample and an installed major describe
the same API. Preserve ComponentStore and class Effects where valid; migration
needs an explicit benefit and affected behavior evidence.

Basis: [Store testing](https://ngrx.io/guide/store/testing),
[Effects testing](https://ngrx.io/guide/effects/testing),
[SignalStore testing](https://ngrx.io/guide/signals/signal-store/testing),
[runtime checks](https://ngrx.io/guide/store/configuration/runtime-checks) and
[Store DevTools](https://ngrx.io/guide/store-devtools).
