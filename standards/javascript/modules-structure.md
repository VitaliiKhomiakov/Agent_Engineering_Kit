# JavaScript modules and structure

Read when changing imports/exports, file placement, construction, dependencies or
callback ownership. Apply the [entry](../javascript.md) and [common
responsibility rules](../core.md); the project chooses its actual module tree.

## Cohesion and boundaries

- Group files by domain capability or use case. Within that grouping, separate
  HTTP/queue transport, application operations, rules, and adapters according to
  their actual responsibilities.
- A file may contain a related function or class, local types, a schema, and small
  helpers from one layer. Independent services and external adapters belong in
  separate modules; a shared suffix does not make them cohesive.
- Export the module's smallest useful contract. Do not use a general barrel to
  bypass boundaries or conceal cyclic dependencies with re-exports.
- Apply the common size thresholds. A function does not require a class merely to
  carry a `Service` name; use a class when behavior, state, or dependencies warrant it.

The transport/layer vocabulary above describes server responsibilities when
present. Browser features need cohesive view, interaction, state and I/O ownership,
not empty backend directories. Pure language/domain operations should not import
DOM, HTTP or database machinery merely to obtain configuration or a shared type.
Do not introduce a package boundary where a local module makes the relationship
clear. Existing framework structure still applies to framework work.

## Construction that carries its cost

Use a function for a stateless operation; pass a dependency as a function or small
named object when that expresses the required capability. A closure can bind
configuration/private state; a class can own lifecycle or enforce state transitions.
Neither requires a DI container, base class or method for every property.

Create plain data with a literal or the accepted schema parser. A separate factory
is useful when creation selects a concrete implementation, acquires resources or
enforces a nontrivial creation protocol. Centralize that protocol; do not add
factories that merely repeat a constructor or assemble each DTO twice. Constructor
or intent-method guards still protect invariants for all callers.

Choose an injected callback/strategy for an actual replaceable decision and a
small adapter/facade for a meaningful external boundary. A local conditional is
often sufficient. Inheritance must preserve the parent's behavioral contract;
sharing a few implementation lines is insufficient justification. Language
prototypes do not require an inheritance architecture.

Preserve the receiver when passing a method as a callback. An extracted regular
method is not automatically bound; call it through its object, wrap it or bind it
at the ownership boundary. Arrow functions capture lexical `this`. Retain the
callback identity when a listener must later be removed. Do not change every
method to an arrow field to address one binding problem.

## Module evaluation and actual hosts

Keep the existing ESM/CommonJS choice for ordinary work. ESM imports are live
bindings, not snapshots; an imported object can still be mutated. Cycles can fail
when initialization reads a binding too early. Remove an inappropriate dependency
or separate the shared contract instead of concealing a cycle behind re-exports.

ES modules use strict mode. Resolution of a specifier belongs to the host/toolchain:
a browser URL, an import map, Node resolution and a bundler alias are distinct.
Verify case, extensions, public exports and runtime paths after file moves using
the actual loader/build. An editor resolving an alias does not prove deployment
can load it. Do not publish a new package entry without checking its consumers.

Keep import-time effects intentional. Top-level `await` can delay dependent module
evaluation; startup configuration and resource acquisition need an explicit owner
and failure path. Avoid starting long-lived work or request-specific state merely
by importing a reusable module. An explicit initialization operation is a simpler
choice when it makes lifetime visible; no initialization framework is required.

## Basis

[MDN modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
and [method receivers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)
explain language behavior. Grouping, dependency direction and conditional pattern
adoption are project policy, not ECMAScript-mandated architecture. See the
[research](../../docs/research/2026-09-21-javascript-engineering-practices.md) for
alternatives and compatibility limits.
