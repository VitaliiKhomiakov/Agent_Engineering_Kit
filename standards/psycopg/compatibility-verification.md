# psycopg compatibility and verification

Read for installation, an upgrade, Psycopg 2 migration or relevant verification.
Use the shared [verification policy](../verification.md); instruction maintenance
needs artifact checks, not a new application test project.

## Establish the actual stack

The researched target is Psycopg 3.3.6. The moving online manual currently carries
a 3.3.7.dev1 banner; use release notes and installed capabilities before adopting an
API. Record Python, psycopg implementation, libpq, server and optional psycopg_pool
versions separately. Bundled client libraries can differ from the server major.

Choose binary, locally compiled C or pure-Python installation according to deployment
constraints. Binary wheels simplify setup but carry their own native libraries;
local builds rely on system libraries/toolchains. Pure Python still needs libpq.
Review package and native-library updates together. Do not switch installation mode
or upgrade a project merely to match a documentation example.

Psycopg 3 imports as psycopg, not psycopg2. Its connection-context closure, server-side
binding, row factories, async APIs and adaptation rules require deliberate migration.
Do not rename imports and assume existing transaction behavior survives. SQLAlchemy's
psycopg dialect is distinct from psycopg2; preserve the framework's connection/pool
owner and check its supported integration. This profile does not silently recognize
or migrate psycopg2-only projects.

Newer optional features such as Python template-string queries require the documented
Python/driver versions. Ordinary bound parameters remain a simple compatible default;
f-strings do not become safe SQL because another interpolation API is supported.
Prepared statements through a transaction pooler, pipeline capabilities and cancellation
fixes depend on more than one version. Verify the named combination instead of using
blanket claims that every pooler does or does not support a feature.

## Proportionate evidence

For instructions, verify source applicability, consistency with Python/PostgreSQL,
local links, short-entry conditions and selected bundle delivery. For short snippets,
check syntax and strict types, then run a small targeted check only where it resolves
a concrete uncertainty. Do not build a service, schema suite or broad concurrency
harness merely to publish a driver instruction.

For real application changes, use its existing relevant tests: actual PostgreSQL is
needed when the changed requirement concerns rollback, SQLSTATE, adaptation, locking,
pool reset or cancellation. Compilation and quoting checks alone do not establish
those behaviors. Test only the affected failure/cleanup boundary and record what was
not executed. A row factory's annotation cannot replace a real schema/row contract
check when that contract changes.

K17 snippets were syntax/type checked on Python 3.12.3, psycopg/binary 3.3.6 and
mypy 2.1.0. An offline check exercised identifier escaping and preserved parameter
placeholders. No PostgreSQL connection, pool, migration, async cancellation or
benchmark was run for this stage. Older stage integration evidence is not attributed
to these new snippets. Synthetic policy bundles do not prove native agent compliance.

Basis: [installation](https://www.psycopg.org/psycopg3/docs/basic/install.html),
[release notes](https://www.psycopg.org/psycopg3/docs/news.html),
[Psycopg 2 differences](https://www.psycopg.org/psycopg3/docs/basic/from_pg2.html), and
[prepared capabilities](https://www.psycopg.org/psycopg3/docs/advanced/prepare.html).
