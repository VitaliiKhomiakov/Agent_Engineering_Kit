# Typed query with separate identifier and value binding

Read when a small SQL adapter needs named output and a restricted choice of tables.
This is a short synchronous one-shot operation, not a service or a pool recipe.

The assumed application schema has `app.report` and `app.report_archive`, each with
an integer primary key `id` and required text `title`. The caller has already checked
operation permission and parsed the table choice into ReportTable. Quoting an arbitrary
user-selected table would not establish permission. class_row constructs the result;
it does not validate annotations against the live schema.

### `typed_query.py`

```python
from dataclasses import dataclass
from enum import Enum

import psycopg
from psycopg import sql
from psycopg.rows import class_row


@dataclass(frozen=True)
class Report:
    id: int
    title: str


class ReportTable(Enum):
    CURRENT = 'report'
    ARCHIVE = 'report_archive'


def report_query(table: ReportTable) -> sql.Composed:
    return sql.SQL('SELECT id, title FROM {} WHERE id = %s').format(
        sql.Identifier('app', table.value)
    )


def find_report(dsn: str, table: ReportTable, report_id: int) -> Report | None:
    # One-shot connection owner; repeated service calls can borrow from a pool.
    with psycopg.connect(dsn, autocommit=True, row_factory=class_row(Report)) as conn:
        with conn.cursor() as cursor:
            cursor.execute(report_query(table), (report_id,))
            return cursor.fetchone()
```

The enum selects an allowed object; Identifier quotes its schema and table separately.
The id stays a value parameter, including a one-element tuple. Explicit columns match
Report; no row returns None. Autocommit avoids retaining a transaction around this
independent read. Repeated service operations should use the project's connection
owner/pool instead of copying a new connection per request as a universal default.

Checks: Python 3.12.3 syntax and strict mypy 2.1.0 with psycopg/binary 3.3.6; offline
SQL rendering confirmed the selected identifiers and untouched `%s` placeholder,
including a separate identifier-escaping probe. No database query or row decoding was
executed. Verify the stated schema and adaptation in the consuming application.
