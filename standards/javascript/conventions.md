# JavaScript standards and conventions

Read for JavaScript layout, names or selection of a language/host/style contract.
Apply [shared convention resolution](../core.md#language-and-framework-conventions)
and [readable layout](../core.md#readable-code-layout). Return to the
[JavaScript entry](../javascript.md); TypeScript and frameworks add scoped rules.

## Language specification versus house style

[ECMA-262](https://262.ecma-international.org/17.0/) specifies ECMAScript syntax
and behavior; it is not a formatter preset. The linked 2026 edition is a reviewed
reference, not an instruction to raise a browser/Node target. Match supported
syntax, module behavior and host APIs through [compatibility](verification-compatibility.md#compatibility-follows-the-supported-project).

Use the project's actual formatter/linter configuration and commands. Where no
style is established, AEK uses readable block layout and conventional naming
consistent with [MDN's JavaScript example guide](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Code_style_guide/JavaScript):
two-space indentation, braces for control-flow bodies, one independent statement
per line, `camelCase` variables/functions/members and `PascalCase` classes.
This is an AEK fallback, not an ECMAScript requirement. Keep quotes, semicolons,
wrapping and trailing commas consistent with the chosen formatter/local style;
preserve automatic-semicolon-insertion behavior when splitting statements.

MDN's guide governs its documentation examples. Its use of a particular formatter
does not require installing that formatter in a consuming project. Reuse suitable
existing tools; do not run competing fixers or copy documentation-only constraints
into application code. [Modules](modules-structure.md), [values](values-state.md)
and [effects](async-effects.md) retain their semantic rules.

## Hosts and framework contracts

Choose interoperability references for the boundary that actually exists. For
example, the [WHATWG Fetch standard](https://fetch.spec.whatwg.org/) defines web
request/response behavior; ECMAScript alone does not provide `fetch`, DOM objects
or Node built-ins. Verify the selected host's implementation and version. A
framework HTTP adapter is not automatically interchangeable with a Fetch API.
An instruction to use a standard does not require a polyfill or host migration.

Framework-specific names and module conventions have their own scope. React JSX
components and custom Hooks, Angular artifacts, Nest providers/plugins and Next.js
route files follow their selected framework owners. Preserve required names,
exports, directives and generated-file patterns; do not rename them to the generic
`camelCase` baseline. Ordinary modules retain their project's normal conventions.

Keep external object keys, route strings and serialized fields stable; use a
deliberate adapter when internal naming differs. Preserve the established module
mode and import/export API. A preference for named exports, for example, must not
remove a framework-required default export.

Use the [existing verification owner](verification-compatibility.md) and shared
readability acceptance. Tool success covers the configured files/rules, not all
ECMAScript or host behavior. [Dated evidence](../../docs/research/2026-11-06-language-and-framework-conventions.md)
records source scope without claiming a new runtime/formatter run.
