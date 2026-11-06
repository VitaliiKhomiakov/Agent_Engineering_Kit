# Python standards and conventions

Read for Python layout, naming, documentation or standards selection. Apply
[convention resolution](../core.md#language-and-framework-conventions) and
[readable layout](../core.md#readable-code-layout); keep supported versions and
existing formatter/analyzer settings. Return to the [Python entry](../python.md).

## Style and documentation baseline

Use [PEP 8](https://peps.python.org/pep-0008/) as the fallback style when the
project has no established convention. It explicitly allows project-specific
guidance and prioritizes compatibility. Existing formatter widths, quote choices
and import tooling remain project decisions; adopting PEP 8 does not authorize
replacing them or installing a new formatter.

- Use four spaces for indentation; keep imports ordered into standard-library,
  third-party and local groups. Preserve required import order and side effects.
- Use `snake_case` for functions, methods, variables and modules; `PascalCase`
  for classes; and `UPPER_CASE` for constants. Preserve existing public names,
  library overrides and protocol-required special names.
- Keep declarations and logical sections visibly separated. PEP 8's default
  widths are 79 for code and 72 for comments/docstrings; preserve an explicitly
  chosen project width rather than adding a conflicting second length gate.
- Use [PEP 257](https://peps.python.org/pep-0257/) for docstring structure: a
  meaningful summary and, when needed, a blank line before further explanation.
  It does not choose Google/NumPy/reStructuredText markup. Retain the project's
  documentation syntax and the shared [contract/comment policy](../core.md#public-contracts-and-explanatory-comments),
  without adding empty documentation to every private helper.

## Select other specifications only for the affected contract

| Task | Primary reference | Existing owner / limit |
| --- | --- | --- |
| Type annotations or checker behavior | [Typing specification](https://typing.python.org/en/latest/spec/) | [Typing contracts](typing-contracts.md) own AEK's stricter authored-code policy; gradual typing in the language does not waive it. Check actual interpreter/analyzer support. |
| Build metadata or distribution interoperability | [PyPA specifications](https://packaging.python.org/en/latest/specifications/) | [Packaging and versions](structure.md#imports-packaging-and-versions); preserve the selected build backend and dependency workflow. No package-manager migration follows from reading a specification. |
| A DB-API driver boundary | [PEP 249](https://peps.python.org/pep-0249/) | [Resource and effect contracts](execution-resources.md); preserve the driver's parameter, transaction and error semantics. A different async/ORM interface is not automatically DB-API-compatible. |
| ASGI application/server or middleware integration | [ASGI 3.0](https://asgi.readthedocs.io/en/stable/specs/main.html) | Use the selected framework/host's protocol and lifecycle rules. ASGI and WSGI are different interfaces; do not change a FastAPI handler into a protocol adapter merely to claim compliance. |

## Framework and external names

Keep Python symbols idiomatic while preserving externally defined field names,
routes and schemas. For example, an internal `user_id` may map to a required
`userId` payload key through the existing serializer. When Pydantic is selected,
its validation/output alias policy owns that mapping; a style edit does not
change either direction's accepted contract. ORM table/column mappings have the
same compatibility boundary. Follow a required override/callback signature
instead of renaming it to satisfy a general preference.

Framework integration and application layout still belong to their selected
profiles. FastAPI, Pydantic, SQLAlchemy or an AI library does not automatically
select every Python interface specification above. Their contributor-only style
requirements apply to work in those repositories or deliberate project adoption.

Use [Python verification](verification.md) and shared readability acceptance for
changed source. The [dated comparison](../../docs/research/2026-11-06-language-and-framework-conventions.md)
separates source review from executed checks; no formatter is installed by this topic.
