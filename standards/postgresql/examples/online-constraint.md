# Add a required value without ignoring historical data

Read for [schema evolution](../migrations-verification.md) where old rows exist and
writers can overlap a deployment. This PostgreSQL 16-compatible sequence also ran
on 18. It is an executable illustration, not an automatically authorized migration.

## Preconditions and phases

Use a disposable database with psql and `ON_ERROR_STOP=1`. Save each block as its
named file and execute the files in the order shown. Each invocation uses the same
test database; the named schemas differ from the reservation example. Do not run
`index.sql` through a wrapper that adds BEGIN or psql's single-transaction option.

Before expand, deployed writers must supply an authoritative amount: CHECK NOT VALID
already rejects new violations, including updates to historical invalid rows. Decide
how those old rows are repaired before introducing the constraint. The fixture has
one approved mapping (`old-1` → 900); inventing zero to satisfy NOT NULL would be a
business-data error. Real backfills need bounded resumable batches and progress.

### `legacy.sql`

```sql
CREATE SCHEMA migration_demo;
CREATE TABLE migration_demo.invoice (
    id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    external_ref text NOT NULL,
    amount_minor bigint
);
INSERT INTO migration_demo.invoice (external_ref, amount_minor)
VALUES ('old-1', NULL), ('old-2', 1200);
```

### `expand.sql`

```sql
BEGIN;
SET LOCAL lock_timeout = '1s';
SET LOCAL statement_timeout = '5s';
ALTER TABLE migration_demo.invoice
    ADD CONSTRAINT invoice_amount_present
    CHECK (amount_minor IS NOT NULL) NOT VALID;
COMMIT;
```

### `backfill.sql`

```sql
BEGIN;
SET LOCAL lock_timeout = '1s';
SET LOCAL statement_timeout = '5s';
-- The fixture's approved historical source gives old-1 an amount of 900.
UPDATE migration_demo.invoice
SET amount_minor = 900
WHERE external_ref = 'old-1' AND amount_minor IS NULL;
COMMIT;
```

### `validate.sql`

```sql
BEGIN;
SET LOCAL lock_timeout = '1s';
SET LOCAL statement_timeout = '5s';
ALTER TABLE migration_demo.invoice
    VALIDATE CONSTRAINT invoice_amount_present;
COMMIT;
```

### `contract.sql`

```sql
BEGIN;
SET LOCAL lock_timeout = '1s';
SET LOCAL statement_timeout = '5s';
ALTER TABLE migration_demo.invoice ALTER COLUMN amount_minor SET NOT NULL;
ALTER TABLE migration_demo.invoice DROP CONSTRAINT invoice_amount_present;
COMMIT;
```

### `index.sql`

```sql
-- Separate runner step: no BEGIN, no automatic migration transaction.
SET lock_timeout = '1s';
SET statement_timeout = '10s';
CREATE UNIQUE INDEX CONCURRENTLY invoice_external_ref_key
    ON migration_demo.invoice (external_ref);
RESET lock_timeout;
RESET statement_timeout;
```

### `attach.sql`

```sql
BEGIN;
SET LOCAL lock_timeout = '1s';
SET LOCAL statement_timeout = '5s';
ALTER TABLE migration_demo.invoice
    ADD CONSTRAINT invoice_external_ref_key
    UNIQUE USING INDEX invoice_external_ref_key;
COMMIT;
```

## Expected behavior and lock boundaries

After expand, the old NULL remains readable but new NULL writes fail with `23514`.
VALIDATE before repair fails and the constraint remains unvalidated. The backfill
corrects only the intended missing value. After validation, SET NOT NULL can use
the valid CHECK as evidence and avoid another full null scan; keep the helper until
that command finishes. The short ALTER still needs its lock. Dropping the helper
in a later command in the same transaction preserves the proof during SET NOT NULL.
After contract, absence fails with `23502` and both historical rows remain.

The separate unique-index step addresses a different requirement: `external_ref`
is unique. CONCURRENTLY can wait and can fail, so inspect `pg_index.indisvalid` and
the actual index definition before claiming success or retrying. A duplicate fixture
row causes `23505` and leaves an invalid index. After a reviewed duplicate repair,
drop/rebuild that failed index deliberately, then attach the eligible B-tree index
as a constraint. Do not blindly use IF NOT EXISTS and assume its name proves success.

The K15 harness exercised old-gap validation failure, denied new NULL, backfill,
validation and NOT NULL conversion on **16.15 and 18.4**. It also injected a duplicate,
observed the failed/invalid concurrent index, repaired the fixture, rebuilt/attached
the index and verified duplicate rejection and final row preservation. These are
small integration fixtures; no production-sized scan, lock-duration benchmark,
rolling application deployment, crash restart or recovery rehearsal was executed.

All timeouts are illustrative local budgets. Production phases need reviewed lock
and statement limits, transaction-mode support and operational retry/recovery rules.
An empty new table may need only the final CREATE TABLE definition. A required field
can make an old application writer incompatible even if the SQL migration succeeds.
This example makes no choice of SQLAlchemy, psycopg or migration framework.

Basis: [16 ALTER TABLE](https://www.postgresql.org/docs/16/sql-altertable.html)
and [concurrent indexes](https://www.postgresql.org/docs/18/sql-createindex.html).
