# JavaScript verification and compatibility

Read for tests, static checking, changed module paths, security, performance or
version changes. The [shared verification policy](../verification.md) owns check
selection and proportionality; use current project tools before adding new ones.

## Verify the boundary that changed

Check observable outcomes and relevant failure paths. Input parsing may need
malformed data, omission versus null, coercion, numeric limits and safe output
projection checks. An invariant change needs refusal without invalid mutation,
not just successful DTO creation. Use existing focused tests or a temporary probe
where sufficient; do not add a permanent test for every helper.

For async ownership, verify completion, rejection, pre-abort, cancellation during
work and required cleanup. Use controlled promises/fakes to order transitions;
avoid arbitrary sleeps and tests that merely count private helper calls. A fake
can establish orchestration but cannot prove real network cancellation, transaction
isolation or browser scheduling. Use an actual adapter/host integration check when
that behavior changes. Tests must await assertions and fail for rejection/leaked
work that violates their contract; do not suppress failures globally.

JSDoc with `allowJs`/`checkJs` can check JavaScript contracts without emitting code
or converting files to TypeScript. Reuse it where already enabled or where the
boundary warrants it. A `jsconfig.json` alone is not proof that CI runs the checker;
verify the command, included files and diagnostics. Keep external values unknown
until narrowed, and do not silence errors with `any`, unchecked casts or blanket
suppression. Static types do not execute a runtime validator.

When exports, package paths or build configuration change, run the actual relevant
loader/build. A syntax check does not execute imports, and a checker resolving a
path does not establish runtime resolution. Browser behavior requires a browser
check for the affected DOM, loader or API boundary; a Node test alone is insufficient.
No new E2E suite or alternate test framework is required for a local language edit.

## Compatibility follows the supported project

Record the engine/host versions, module format, package manager/lock and build
targets that actually matter. ECMAScript specifies language semantics; DOM,
`fetch`, timers, Node built-ins and available globals come from hosts. Browser,
worker and server contexts differ. A dependency using browser globals cannot be
assumed to load during server rendering merely because both use JavaScript.

Check syntax support, library/host API support and loader behavior separately.
Transpiling syntax does not supply missing APIs or establish a server/browser
security model. Polyfills and compiler `lib` declarations have different effects.
Use per-feature compatibility evidence for supported targets, not a universal
"modern JavaScript" minimum inferred from one successful local run.

Preserve the declared support range and lockfile workflow. Package upgrades,
CommonJS-to-ESM conversion, JS-to-TS migration and new bundlers need task scope
and consumer checks. Current specification examples or documentation versions do
not authorize those migrations. New facilities such as disposal syntax are
optional after checking the actual runtime/toolchain and resource API.

## Security, load and operations when relevant

Validate and project external fields before using them as owned state. Do not
merge untrusted dynamic keys into ordinary objects: prototype pollution can
change unrelated lookups. A known result should have named fields; real dynamic
dictionaries can use `Map` or a null-prototype object with an explicit contract.
Parsing JSON is neither authorization nor safe handling at a later output sink.

Avoid interpreting data as code through `eval` or a dynamic Function constructor.
At DOM/SQL/URL boundaries, use that platform's safe data APIs and contextual
validation/encoding. Client checks cannot establish server authorization. Do not
expose credentials, raw request bodies or internal errors through public results
and logs. Apply these controls at the actual boundary; a language-only utility
does not require a new security framework.

Bound external sizes and fan-out according to resources. Large parsing, regular
expressions, synchronous loops and repeated copying can block useful work despite
an `async` signature. Measure the actual slow operation before selecting a worker,
cache, streaming parser or memoization policy. Give caches a scope, invalidation
and size owner; no performance pattern is universally free. Record which workload
and host a measurement covers rather than presenting a microbenchmark as a rule.

## Basis

[ECMAScript's host boundary](https://tc39.es/ecma262/2026/multipage/overview.html),
[checkJs](https://www.typescriptlang.org/tsconfig/checkJs.html),
[JSDoc](https://www.typescriptlang.org/docs/handbook/jsdoc-supported-types.html),
[prototype pollution](https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/Prototype_pollution)
and [Node's blocking-work guidance](https://nodejs.org/en/learn/asynchronous-work/dont-block-the-event-loop)
support these limits. See [research and executed scope](../../docs/research/2026-09-21-javascript-engineering-practices.md)
for the single-runtime examples and unexecuted host checks.
