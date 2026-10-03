# TypeScript toolchain and verification

Read for compiler/lint gates, module emit/resolution, framework generation,
compatibility changes or checker performance. The [shared verification policy](../verification.md)
owns proportionality; use existing meaningful checks rather than adding a test
or tool for every type declaration. The [entry](../typescript.md) owns the target
strict/no-any contract across all TypeScript hosts.

## Enforceability

`strict` and `noImplicitAny` do not prohibit explicitly written `any`. The target
set of checks therefore includes:

- TypeScript `strict: true` and the project's existing type-check command.
- `@typescript-eslint/no-explicit-any: error` when typescript-eslint is in use.
- Type-aware lint checks for unsafe assignment, argument, call, member access,
  and return when that tooling is configured. These detect some `any` leaks from
  dependencies that an annotation-only prohibition misses.

Do not run `tsc` on an individual file outside the required `tsconfig` and
framework type generation. In a monorepo, select the affected package/project and
its actual command; do not add a second analyzer without a need.

Enabling strict mode and resolving existing violations in legacy code is a
separate migration phase. New contracts follow this standard immediately. Do not
fix unrelated old code or add new suppressions for a small task. Explicitly report
unchecked scope and existing violations.

Inspect the effective config and included files when scope/defaults are unclear.
`strict` is a group and can have individual overrides; it does not turn on every
useful safety flag. `exactOptionalPropertyTypes` and `noUncheckedIndexedAccess`
address specific absence contracts. Adopt additional flags deliberately; an
unrelated task does not authorize enabling them across an old monorepo.

Typed lint needs real project type information for the affected files. With a
compatible typescript-eslint version, use the existing project-service/config
workflow and unsafe-operation rules. A lint command that skips a file or cannot
load its project is not successful coverage. Promise/async-callback lint can catch
unowned work, but cannot prove runtime cleanup or transaction completion.

## Check compile-time and runtime contracts separately

For a changed public/generic API, check representative consumers. Negative type
cases are useful when a crucial invalid use would otherwise silently compile;
keep intentional failures isolated from normal source/tests and verify the actual
diagnostic, not any nonzero tool exit. Do not require a type-test framework for
ordinary interface edits or silence a production mismatch with a test directive.

Runtime validation, state-dependent refusal, serialization and effects need the
appropriate behavior check. Use the existing runner; types do not prove hostile
input rejection or database atomicity. A fake demonstrates the contract it actually
implements, not the target host's real I/O. Inspect emitted or bundled code and
run the relevant path when imports/exports or build behavior change.

Use `noEmit` when another tool emits code and a separate checker must validate it.
Where `tsc` owns build output, preserve `noEmitOnError` or an equivalent build gate;
emission and checking are distinct. Babel/SWC/esbuild or runtime type stripping
may execute TS-looking source without a full type check. `isolatedModules`
checks compatibility with certain single-file transforms; it is not that transform
or a substitute for the project's type-check command.

## Match the host, package and generated contract

Choose `module`/`moduleResolution` for the actual runtime or bundler. NodeNext and
bundler modes model different loaders; no single preset fits every server, browser
and published library. `paths` affects TypeScript lookup, not emitted import
specifiers. Confirm package exports, runtime paths, file extensions and declarations
for affected consumers. `target`, `lib` and installed `@types` also differ: a type
declaration does not install a missing global or polyfill an API.

`verbatimModuleSyntax` makes type/value import intent explicit when compatible
with the project's emitter. Preserve required value imports and module side
effects. Check actual decorator/metadata behavior where a framework uses it;
erased interfaces cannot replace runtime registration. JSX generation, framework
type generation and client/server restrictions remain with the framework owner.

For a published package, verify the affected declaration/public export contract
with a representative consumer and actual supported modes. Do not expose internal
path aliases that consumers cannot resolve. Project references/composite builds
are optional for real package/build boundaries; they add config and declaration
coordination and do not justify a monorepo restructure for a local edit.

## Versions, migration and performance

Pin and inspect the actual compiler, editor/framework integration, lint parser,
package manager and lock. Compare installed/CLI/API versions, not just a manifest
label. A compatibility wrapper can resolve a separate compiler dependency.

As researched on 2026-09-21, TypeScript 7.0 is the native compiler release; it
does not ship the previous programmatic compiler API. Tools using that API may
need a compatible 6.x installation/alias alongside it. Verify the specific tool's
support range and commands; do not assume `tsc`, editor and typed lint use the
same compiler. The optional examples exercise this arrangement, not a universal
requirement to install two compilers.

TypeScript 6/7 change defaults and deprecations relative to 5.x. Preserve explicit
strictness, targets, module choices and included ambient types; review the actual
release notes for an authorized upgrade. An article recommending a migration
does not authorize changing a consumer project or weakening this framework's
strict policy. Update lock/config/framework outputs coherently when migration is
in scope; do not paper over diagnostics with a blanket suppression.

Measure checker/build cost before adding project references, parallelism controls
or complex type caching. Deep conditional types and large intersections can cost
more than clear named contracts. Use installed-tool diagnostics/traces for an
observed slowdown; published compiler speedups are not application-runtime
benchmarks. Do not switch off required checks or add `skipLibCheck` merely to
conceal incompatible declarations; report existing unchecked declaration scope.

## Basis

[Strict](https://www.typescriptlang.org/tsconfig/strict.html),
[typed lint](https://typescript-eslint.io/getting-started/typed-linting/),
[tool support](https://typescript-eslint.io/users/dependency-versions/),
[module reference](https://www.typescriptlang.org/docs/handbook/modules/reference.html),
[isolatedModules](https://www.typescriptlang.org/tsconfig/isolatedModules.html),
[project references](https://www.typescriptlang.org/docs/handbook/project-references.html),
[TypeScript 6](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/),
[TypeScript 7](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/)
and the [compiler performance guide](https://github.com/microsoft/TypeScript/wiki/Performance)
support the stated limits. See [research](../../docs/research/2026-09-21-typescript-engineering-practices.md)
for actual versions and executed scope.
