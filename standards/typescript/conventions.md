# TypeScript conventions and scoped framework rules

Read for TypeScript naming/layout or a conflict between style guides and framework
requirements. Apply [JavaScript conventions](../javascript/conventions.md), then
[shared resolution](../core.md#language-and-framework-conventions). The
[TypeScript entry](../typescript.md) continues to own strict typing and named
contracts; style selection does not weaken those requirements.

## Choose a guide for the actual project

Establish `tsconfig`, the effective formatter/linter settings and framework/code
generation for the affected package. Use the selected compiler's supported
language contract. TypeScript syntax and static analysis do not prescribe a
universal source-layout preset.

Microsoft's [TypeScript contributor guidelines](https://github.com/microsoft/TypeScript/wiki/Coding-guidelines)
explicitly target the compiler repository. Its restrictions on shared type files,
classes or null values are not application-wide rules. Google's
[TS/JS guide](https://google.github.io/styleguide/tsguide.html) is another scoped
guide, with its own environment assumptions. Apply an adopted guide's compatible
recommendations; do not import either repository's architecture or toolchain.

For new code without a project convention, this library uses `PascalCase` for
types/interfaces/classes and `camelCase` for functions, members and local values,
with the shared JavaScript layout baseline. Do not add an `I` prefix to every
new interface; preserve an established public/project convention. These naming
defaults are AEK policy, not compiler restrictions. Public/wire/schema names
retain their compatibility contract.

## Framework refinements are conditional

Use the selected framework's owner for file names, recognized exports, decorators,
component/Hook names and generated contracts. Angular's style guide does not apply
to a Nest service merely because both use TypeScript. Nest's runtime injection
tokens/classes do not eliminate the TypeScript interface boundary, and framework
DTO or reflected entity requirements do not require classes for every plain object.
Next.js route exports retain their router contract; JSX follows the actual UI
framework and the project's `.tsx`/compiler configuration.

Choose file-level/package-level formatting overrides when different owned formats
actually require them, preserving existing config. A guide recommending an import
style or erased type does not establish its compatibility with emitted decorator
metadata, runtime tokens or the selected module loader. Use
[toolchain verification](toolchain-verification.md) for those changes, plus shared
readability acceptance for final layout. No new formatter, analyzer or framework
is selected by this topic.

[Dated evidence](../../docs/research/2026-11-06-language-and-framework-conventions.md)
records the sources and their limits; reading a guide does not verify application behavior.
