# An explicit transaction owner and a borrowing helper

Read for the distinction between connection lifetime and an atomic operation.
Use Report from the [typed query](typed-query.md). This assumes `app.report` additionally
has a required boolean `archived`, and `app.report_audit` accepts required report_id
and title fields with the appropriate application constraints. No schema is installed
by this example. Both functions belong to the persistence adapter.

The caller supplies typed inputs and authorization. The helper independently refuses
a blank title; the conditional write checks current archived state. Input parsing
alone cannot decide whether a stored report can still change. An audit insert failure
must unwind the operation rather than leave an unaudited rename.

### `owned_transaction.py`

```python
import psycopg
from psycopg import Connection
from psycopg.rows import class_row

from typed_query import Report


def rename_in_transaction(conn: Connection[Report], report_id: int, title: str) -> bool:
    """Caller owns an active transaction and has authorized this operation."""
    if not title.strip():
        raise ValueError('title must not be blank')
    with conn.cursor() as cursor:
        cursor.execute(
            'UPDATE app.report SET title = %s WHERE id = %s AND NOT archived '
            'RETURNING id, title',
            (title, report_id),
        )
        changed = cursor.fetchone()
        if changed is None:
            return False
        cursor.execute(
            'INSERT INTO app.report_audit (report_id, title) VALUES (%s, %s)',
            (changed.id, changed.title),
        )
    return True


def rename_report(dsn: str, report_id: int, title: str) -> bool:
    with psycopg.connect(dsn, autocommit=True, row_factory=class_row(Report)) as conn:
        with conn.transaction():
            changed = rename_in_transaction(conn, report_id, title)
    return changed
```

The owned connection starts in autocommit, so the explicit transaction block here is
the outer boundary. Its successful exit precedes the return. The helper performs no
commit/rollback and can participate in a caller's larger active transaction. Calling
that helper on an autocommit connection without the promised transaction would break
atomicity; its annotation alone does not enforce the lifetime contract.

On a default non-autocommit connection, a prior SELECT may already have started a
transaction. A later transaction() block can then be a savepoint, not the outer commit.
Do not move this owner's pattern into a borrowed connection without checking ownership.
No catch suppresses database failure inside the transaction. Public error mapping and
uncertain-commit/idempotency recovery remain with the consuming application's owner.

Checks: syntax and strict typing only on Python 3.12.3/psycopg 3.3.6. Transaction
semantics were reviewed against the [official manual](https://www.psycopg.org/psycopg3/docs/basic/transactions.html);
this stage did not execute the SQL, rollback or concurrency. These small snippets
replace a test application; they are not production validation evidence.

To check both saved files with the project's compatible environment:

```sh
python -m compileall -q typed_query.py owned_transaction.py
python -m mypy --strict --disallow-any-explicit --disallow-any-unimported typed_query.py owned_transaction.py
```

Use psycopg 3.3.6 and a supported Python/psycopg implementation for these checks;
no server is needed for importing/type-checking the functions. Do not install or
upgrade dependencies in an existing project merely to run the example.
