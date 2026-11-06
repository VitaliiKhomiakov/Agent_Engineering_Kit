# PostgreSQL SQL conventions and dialect contracts

Read for authored SQL/PL/pgSQL layout, names or standard-versus-dialect decisions.
Use [shared convention resolution](../core.md#language-and-framework-conventions)
and the [PostgreSQL entry](../postgresql.md). A driver or ORM does not establish
the server version or make its generated naming conventions universal SQL rules.

## Standard and supported dialect

ISO/IEC 9075 defines SQL. PostgreSQL documents its supported and unsupported
features in the [16](https://www.postgresql.org/docs/16/features.html) and
[18](https://www.postgresql.org/docs/18/features.html) conformance appendices.
Use the actual server's contract; neither a standard edition nor a successful ORM
type check proves that a particular query/DDL feature is available. PL/pgSQL is
a PostgreSQL procedural language, not portable SQL by assumption.

The SQL standard is not a universal application naming or formatting preset.
Keep the project's formatter, migration style and established schema conventions.
For new owned SQL without such conventions, AEK uses uppercase keywords,
lowercase `snake_case` identifiers and consistent indentation, with major clauses,
CTEs, joins and long predicates split into readable groups. Keep a simple query
compact when clear; keyword case and this layout are local policy.

## Names and generated SQL are contracts

PostgreSQL folds unquoted identifiers to lowercase; quoted names are case
sensitive. This differs from the standard's uppercase folding. Preserve quoting
and spelling deliberately: changing `"UserId"` to `user_id` is not formatting.
[Lexical structure](https://www.postgresql.org/docs/18/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIERS).

Distinguish a model/property name, physical table/column name and result alias.
Follow the installed ORM's explicit mapping/naming strategy and existing schema;
do not rename columns to match the application language or normalize generated
migrations by hand. A necessary identifier change follows the
[migration contract](migrations-verification.md), including affected callers.
Preserve parameter placeholders and literal contents while formatting; never
rewrite bound values into interpolated SQL for visual consistency.

For [PL/pgSQL](https://www.postgresql.org/docs/18/plpgsql-structure.html), keep
declarations, nested blocks and statement terminators clear and respect the
function body's quoting. Use the project's established variable/parameter naming
and qualify ambiguous references; formatting must not change name resolution.

Apply shared readability acceptance and [PostgreSQL verification](migrations-verification.md).
A formatter does not validate schema resolution, dialect support or query behavior.
The [dated comparison](../../docs/research/2026-11-06-language-and-framework-conventions.md)
records source review only; unchanged examples keep their earlier runtime evidence.
