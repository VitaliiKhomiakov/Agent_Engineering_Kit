# Language standards and framework conventions

Reviewed: 2026-11-06. Scope: primary-source review and AEK instruction maintenance.
This record distinguishes language specifications, style guides and integration
contracts. It supplies no new application, engine or formatter execution evidence.
The [canonical plan](../plans/2026-11-06-language-and-framework-conventions.md)
owns implementation progress, executed checks and the review outcome.

## Inventory and existing coverage

At baseline `d63e297adb0cfc380d1e16179ac0f4a69428b1ab`, PHP had a dedicated
[FIG standards owner](../../standards/php/fig-standards.md). Go and GDScript already
had detailed layout rules; Unreal had engine naming/lifetime rules, and Godot had
conditional C#/native integration guidance. Python, JavaScript, TypeScript and
PostgreSQL covered behavior and tooling but lacked a dedicated conventions topic.

The scope is the languages already represented in AEK: Python, Go, JavaScript,
TypeScript, GDScript, C#, C++ and SQL/PL/pgSQL. PHP/Symfony participate only where
their existing guidance composes with the shared rule. C#/C++ remain conditional
engine subjects. HTML/SCSS, configuration formats, shell commands and visual
scripting keep their existing owners; they do not create new language profiles.

The conclusion is not that every ecosystem has a PHP-FIG equivalent. Different
documents govern syntax/semantics, source style, library interoperability and
framework discovery. AEK's [shared resolution rule](../../standards/core.md#language-and-framework-conventions)
keeps those authorities distinct and scopes compatible project/framework choices.

## Language evidence and resulting owners

| Language / primary sources | Authority and reviewed scope | AEK decision |
| --- | --- | --- |
| Python: [PEP 8](https://peps.python.org/pep-0008/), [PEP 257](https://peps.python.org/pep-0257/) | Style and docstring conventions; project consistency and compatibility matter. Docstring structure does not select a documentation markup dialect. | Add [Python conventions](../../standards/python/conventions.md); retain existing formatter choices and stronger typing policy. |
| Python: [typing specification](https://typing.python.org/en/latest/spec/), [PyPA specifications](https://packaging.python.org/en/latest/specifications/), [PEP 249](https://peps.python.org/pep-0249/), [ASGI 3.0](https://asgi.readthedocs.io/en/stable/specs/main.html) | Separate typing, packaging, DB-API 2.0 and application/server interface contracts. | Route to the affected boundary only; an installed framework does not require adopting every specification or replacing existing adapters. |
| Go: [language specification](https://go.dev/ref/spec), [Effective Go](https://go.dev/doc/effective_go#formatting), [Code Review Comments](https://go.dev/wiki/CodeReviewComments), [`http.Handler`](https://pkg.go.dev/net/http#Handler) | Language semantics, official formatting/idiom advice and a concrete standard-library interface have different roles. | Extend [Go style](../../standards/go/style.md) with source scope; preserve its existing formatter/grouping rules, interface signatures and wire tags. |
| JavaScript: [ECMA-262, 17th edition (2026)](https://262.ecma-international.org/17.0/), [MDN example style](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Code_style_guide/JavaScript), [WHATWG Fetch](https://fetch.spec.whatwg.org/) | ECMAScript specifies the language; MDN's guide governs examples; Fetch specifies a host-facing web API. | Add [JavaScript conventions](../../standards/javascript/conventions.md). Mark the layout fallback as AEK policy and preserve actual host/tool support. |
| TypeScript: [compiler contributor guide](https://github.com/microsoft/TypeScript/wiki/Coding-guidelines), [Google TS/JS guide](https://google.github.io/styleguide/tsguide.html) | The compiler guide explicitly limits its audience; Google's guide has environment-specific assumptions. Neither is a universal application formatter/architecture standard. | Add [TypeScript conventions](../../standards/typescript/conventions.md); preserve AEK's existing strictness and interface owners. |
| GDScript: [Godot 4.7 style guide](https://docs.godotengine.org/en/4.7/tutorials/scripting/gdscript/gdscript_styleguide.html) | Engine-language guidance inspired by PEP 8, with its own rules. | Extend the existing [GDScript owner](../../standards/godot/gdscript.md); do not apply Python or C# conventions to `.gd` source. |
| C#: [ECMA-334](https://ecma-international.org/publications-and-standards/standards/ecma-334/), [Microsoft conventions](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions), [Godot 4.7 C# guide](https://docs.godotengine.org/en/4.7/tutorials/scripting/c_sharp/c_sharp_style_guide.html) | A language standard and scoped source-style recommendations are different. Microsoft describes its documentation/example style; Godot's contributor guide also recommends conventions to users. | Add the conditional Godot default in [interop](../../standards/godot/interop.md#c); preserve SDK and engine support rather than adopting every new documentation feature. |
| C++: [ISO/IEC 14882:2024 catalog](https://www.iso.org/standard/83626.html), [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines), [Godot 4.7 binding example](https://docs.godotengine.org/en/4.7/tutorials/scripting/cpp/gdextension_cpp_example.html) | Formal language standard, advisory design/style guidance and binding contracts. The ISO reference was identified through public catalog metadata, not a review of the full standard text. | Extend the existing [Godot native](../../standards/godot/interop.md#gdextension) and [Unreal C++](../../standards/unreal-engine/cpp-lifetime.md) owners; preserve registered/reflected names and engine lifetime rules. |
| SQL/PL/pgSQL: PostgreSQL [16](https://www.postgresql.org/docs/16/features.html) / [18](https://www.postgresql.org/docs/18/features.html) conformance appendices, [lexical rules](https://www.postgresql.org/docs/18/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIERS), [PL/pgSQL structure](https://www.postgresql.org/docs/18/plpgsql-structure.html) | PostgreSQL documents its relationship to ISO/IEC 9075 and its own dialect. The manuals do not establish a universal application style; PL/pgSQL is PostgreSQL-specific. | Add [SQL conventions](../../standards/postgresql/conventions.md), keeping schema spelling, quoting, ORM mappings and migration behavior distinct from formatting. |

## Framework differences that affect the decision

| Primary evidence | Relevant difference | Instruction placement |
| --- | --- | --- |
| [Pydantic aliases](https://pydantic.dev/docs/validation/latest/concepts/alias/) | Internal Python names and accepted/emitted payload names are separate. | Python conventions route to the existing alias owner in [serialization](../../standards/pydantic/serialization.md#names-presence-and-partial-updates); no duplicate alias policy. |
| [Angular 20 style guide](https://v20.angular.dev/style-guide) | Filename and colocation advice is scoped style guidance, distinct from runtime/template contracts. | [Angular architecture](../../standards/angular/architecture.md#naming-and-style-scope); preserve established suffixes and the existing SCSS choice. |
| React [components](https://react.dev/learn/your-first-component) and [custom Hooks](https://react.dev/learn/reusing-logic-with-custom-hooks) | JSX component identifiers and custom Hook names refine ordinary JavaScript naming. | [Component boundaries](../../standards/react/components-boundaries.md#names-and-module-conventions); filenames/exports remain project/framework decisions. |
| Next.js [page](https://nextjs.org/docs/app/api-reference/file-conventions/page) and [route](https://nextjs.org/docs/app/api-reference/file-conventions/route) APIs | Special files and recognized exports participate in routing. | [Routing composition](../../standards/nextjs/routing-composition.md#router-and-version-first); retain default page components and HTTP-method exports in their router scope. |
| Nest official documentation source: [controllers](https://raw.githubusercontent.com/nestjs/docs.nestjs.com/master/content/controllers.md), [Swagger plugin](https://raw.githubusercontent.com/nestjs/docs.nestjs.com/master/content/openapi/cli-plugin.md) | Ordinary artifact suffixes differ from filename patterns consumed by an enabled plugin. Swagger's DTO suffix matching is configurable and opt-in. | [Naming/discovery](../../standards/nestjs/modules-providers.md#naming-and-discovery); inspect effective configuration before a rename. |
| [Godot C# style](https://docs.godotengine.org/en/4.7/tutorials/scripting/c_sharp/c_sharp_style_guide.html), [Epic coding standard](https://dev.epicgames.com/documentation/unreal-engine/epic-cplusplus-coding-standard-for-unreal-engine) | Godot recommends four-space C# indentation; Epic uses tabs, including C#. General C++ naming advice also differs from Unreal conventions. | Keep choices in their engine owners, including Unreal [C# build inputs](../../standards/unreal-engine/build-assets.md#modules-and-build-inputs). |
| Symfony 7.4 [contribution standard](https://symfony.com/doc/7.4/contributing/code/standards.html), [application best practices](https://symfony.com/doc/7.4/best_practices.html) | Contributor style and application guidance have different audiences; Twig names use a different convention from PHP methods/classes. | [Symfony style/template scope](../../standards/symfony/structure-services.md#coding-style-and-template-names); keep PHP-FIG selection with its existing owner. |

The shared precedence is an AEK engineering decision, informed by these concrete
differences. Preserve required language/runtime/integration contracts first;
within them, use explicit project conventions and accepted AEK exceptions, then
the language baseline and applicable framework refinement. A preference alone
does not authorize a public-name migration or toolchain/configuration replacement.

## Versions, access and evidence limits

- Preserve AEK's Angular 20, Godot 4.7, UE 5.8, Symfony 7.4 and PostgreSQL 16/18
  reference boundaries. The new links do not upgrade fixtures or consuming projects.
  Existing example/runtime evidence remains in its original dated records.
- The Go specification page identified `go1.27` at retrieval; ECMAScript was the
  2026 edition, and the ECMA-334 publication page listed the seventh edition
  (December 2023). These references identify source scope, not minimum target versions.
- React's live page identified v19.3 and Next.js v16.4.5. Their narrow naming and
  route findings do not establish that all current APIs work in an older target.
  Typing, PyPA, Fetch, MDN, TypeScript/Google guides and C++ Core Guidelines are
  rolling references; check affected features against the actual selected versions.
- Direct Nest documentation HTML requests timed out. The official documentation
  repository supplied controller and plugin text. The public documentation URLs
  remain the user-facing references in the standard.
- The indexed official Epic page identified UE 5.8 and supplied formatting text.
  Its explicit version-query URL could not be fetched directly. This is a source
  retrieval limit, not evidence from a local Unreal build.
- A fresh Godot 4.7 core C++ contribution-guide page could not be retrieved at the
  attempted versioned paths. No new engine-wide C++ preset is inferred from that
  missing page. Use the extension's actual configuration and the accessible
  versioned binding example; a future core-style change needs its own source check.
- PostgreSQL's manuals provide public SQL-conformance evidence; no full ISO SQL
  text was reviewed. The ISO C++ catalog similarly establishes identity only.
- There is no claim of complete standards conformance, a new formatter/runtime
  run, or measured improvement in agent behavior. Artifact, profile-selection,
  static-analysis and coordinator-review results belong to the canonical plan.

## Integration decisions

Four new topic resources are included in their existing language profiles and
compatibility inventory. No profile dependency or runtime/tool selection is added.
Entry tables route to the new/existing owners; examples and this research remain
conditional references. Shared readable layout continues to own semantic grouping,
and [verification](../../standards/verification.md#readability-acceptance) owns
acceptance. This record does not introduce a second instruction or progress owner.
