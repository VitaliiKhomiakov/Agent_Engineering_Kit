# React state, identity and ownership

Read when changing state, list identity, reset behavior or cross-component sharing.

## Choose an owner and a representation

- Keep local UI state close to its owner. Relate parameters that must survive
  navigation and be shareable by link to the URL. Server data must have a clear
  owner for loading and caching.
- Do not copy the same server data into multiple stores or persist derived values
  separately without a need. Use the accepted client query library for its purpose;
  do not add it to every server read.

Derive totals, filtered lists and validity from current inputs during rendering
unless their independent lifetime is required. A draft copied from server data
needs an explicit initial value, dirty/conflict policy and reset rule. Do not keep
resynchronizing a draft from props while the user edits it. Choose discriminated
states for mutually exclusive outcomes instead of combinations such as success
and failure both being true. A reducer helps coordinate related transitions; small
independent state values need no reducer. Reducers remain pure.

Lift shared state only to the nearest real common owner. Context carries values;
it does not selectively subscribe consumers by itself. Split ownership when
unrelated high-frequency updates demonstrably cause work. For an existing external
store, prefer its maintained React integration or `useSyncExternalStore` with an
unsubscribe, stable cached snapshots and matching server snapshot where SSR applies.
Do not build a second store by mirroring it into each subscriber's Effect/state.

## Identity, snapshots and resets

State follows the component's type, position and key. Use stable domain IDs for
reorderable lists; indices fit only genuinely fixed identity, and random keys
remount on every render. Define component functions outside other components to
avoid accidental new types. `useId` connects labels/descriptions; it is not a list
key or persisted business ID.

Reset a complete editing session with a deliberate key when the entity changes;
this also discards descendant state and focus. If a draft must survive switching,
retain it under its actual owner instead. Explain preservation/reset expectations
for navigation and use the router's supported URL API rather than mirrored state.

An event handler sees its render's snapshot. Use functional updates when the next
state depends on queued previous state, and immutable replacements for changed
objects/arrays. Refs keep non-rendered handles; changing a ref does not refresh UI.
Do not use a ref to conceal reactive state or read/write it during rendering except
for documented initialization patterns. Batching is not an atomic server transaction.

## Basis

[State structure](https://react.dev/learn/choosing-the-state-structure),
[sharing state](https://react.dev/learn/sharing-state-between-components),
[identity/reset](https://react.dev/learn/preserving-and-resetting-state),
[queued updates](https://react.dev/learn/queueing-a-series-of-state-updates),
[external stores](https://react.dev/reference/react/useSyncExternalStore) and
[`useId`](https://react.dev/reference/react/useId) support these choices.
