# Atomic reservation without a read-before-write race

Read when a single-row stock bound and its receipt must change together. This is a
small PostgreSQL adapter example for [transactions](../transactions-concurrency.md),
not a complete inventory, authorization or idempotency service.

## Contract and setup

Use a disposable database on PostgreSQL 16 or 18 and `psql -X -v ON_ERROR_STOP=1`.
Save the three SQL blocks below as named files. Apply `schema.sql` once, then load
`reserve.sql` and `call.sql` in the **same psql session**, for example:

```sh
psql -X -v ON_ERROR_STOP=1 -f schema.sql -f reserve.sql -f call.sql
```

Connection parameters come from your isolated test environment. The fixture owns
its new `reservation_demo` schema; do not run it in an existing application database.
PREPARE is session-local. Production code should use the established driver's bound
parameters and transaction owner, with trusted tenant identity and operation
permission checked before dispatch. No role or RLS policy is installed here.

A submitted quantity must parse to the transport's integer representation. The
operation separately requires a positive quantity and enough **current** stock.
UUID/text/integer SQL parameter types do not validate an HTTP DTO. Zero returned
rows mean the operation did not reserve (including invalid quantity or unavailable
item); the adapter chooses a permitted public refusal without exposing other tenants.

### `schema.sql`

```sql
CREATE SCHEMA reservation_demo;
CREATE TABLE reservation_demo.stock (
    tenant_id uuid NOT NULL,
    sku text NOT NULL,
    remaining integer NOT NULL CHECK (remaining >= 0),
    PRIMARY KEY (tenant_id, sku)
);
CREATE TABLE reservation_demo.reservation (
    tenant_id uuid NOT NULL,
    request_id uuid NOT NULL,
    sku text NOT NULL,
    quantity integer NOT NULL CHECK (quantity > 0),
    PRIMARY KEY (tenant_id, request_id),
    FOREIGN KEY (tenant_id, sku)
        REFERENCES reservation_demo.stock (tenant_id, sku)
);
INSERT INTO reservation_demo.stock VALUES
    ('00000000-0000-0000-0000-000000000001', 'book', 3),
    ('00000000-0000-0000-0000-000000000002', 'book', 7);
```

### `reserve.sql`

```sql
PREPARE reserve (uuid, uuid, text, integer) AS
WITH spent AS (
    UPDATE reservation_demo.stock
    SET remaining = remaining - $4
    WHERE tenant_id = $1 AND sku = $3
      AND $4 > 0 AND remaining >= $4
    RETURNING tenant_id, sku
)
INSERT INTO reservation_demo.reservation (tenant_id, request_id, sku, quantity)
SELECT tenant_id, $2, sku, $4 FROM spent
RETURNING request_id, quantity;
```

### `call.sql`

```sql
BEGIN;
SET LOCAL lock_timeout = '1s';
SET LOCAL statement_timeout = '3s';
EXECUTE reserve(
    '00000000-0000-0000-0000-000000000001',
    '10000000-0000-0000-0000-000000000001',
    'book', 2
);
COMMIT;
```

## Why this statement has the needed boundary

The UPDATE condition and decrement are one write. Its RETURNING relation supplies
only successful changes to the receipt INSERT. An insertion error rolls back the
whole statement, including the decrement; a later transaction failure rolls back
both. A returned receipt becomes committed success only after COMMIT.

The request key is tenant-scoped. Reusing it can raise `23505` and must not decrement
again. This example intentionally does **not** return a stored success on replay:
a real idempotency contract must compare payload and retain the outcome, including
reconciliation after uncertain COMMIT. If stock is already insufficient, the same
replay can return zero rows before attempting the conflicting insert. Do not attach
`ON CONFLICT DO NOTHING` to this INSERT: that can consume stock without a new receipt.

The composite foreign key prevents a receipt for a nonexistent tenant/item pair;
it does not authorize access. The stock CHECK is a last integrity boundary. The
statement guards the business decision even when called by a CLI or worker without
an HTTP validator. Separate constraints on receipt quantity protect direct writes.
This does not make arbitrary table writes preserve the full inventory ledger.

## Check competing requests and failure paths

For a clean fixture, open two separate connections and load `reserve.sql` in each.
In A, BEGIN and execute a quantity of 2 with a fresh request UUID; leave it uncommitted.
In B, BEGIN and execute quantity 2 for the same tenant/item with a different UUID.
Observe B's lock wait in `pg_stat_activity`, then COMMIT A. Under Read Committed, B
returns zero rows; commit B. Verify stock is 1 and exactly one receipt exists.
Reset only the disposable fixture before another scenario. Do not use a fixed sleep
as evidence that the transactions actually overlapped.

The K15 harness executed on **16.15 and 18.4**:

- Invalid text (`22P02`), zero/negative/NULL/excess quantity and missing item;
  refusals leave stock unchanged.
- Required/nonnegative/reference constraints, successful receipt, tenant targeting,
  and duplicate receipt (`23505`) rolling back the provisional debit.
- The observed two-connection wait above, plus bounded `55P03` lock refusal.
- Two Serializable transactions reading the same stock: the second writer receives
  `40001`; restarting the whole operation in a new transaction sees current stock
  and refuses the now-unavailable quantity. This is evidence for retry scope, not
  a production retry scheduler or an idempotency implementation.

Timeouts here are fixture budgets, not universal defaults. The harness uses psql
sessions, not a selected ORM/driver. No real auth, RLS, pool, remote effects, load,
durability across server loss or uncertain-COMMIT recovery was tested. The separate
[migration example](online-constraint.md) concerns an existing-data contract.

Basis: [UPDATE](https://www.postgresql.org/docs/18/sql-update.html),
[data-modifying WITH](https://www.postgresql.org/docs/18/queries-with.html), and
[Read Committed](https://www.postgresql.org/docs/16/transaction-iso.html).
