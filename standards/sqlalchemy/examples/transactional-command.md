# An owned transaction around a typed reservation

Read for [write ownership](../sessions-transactions.md). This adapter uses SQLAlchemy
2.0 typed mappings, conditional DML and an ORM receipt flush. It illustrates atomic
persistence without imposing a repository hierarchy or a database on every project.

## Setup and scope

Both SQLAlchemy examples share a temporary Python environment. Save the named file
blocks from this page and the [async example](async-projection.md) in one directory.
Use Python 3.11+ syntax; execution here used **3.12.3**, SQLAlchemy **2.0.54**,
PostgreSQL **16.15**, psycopg **3.3.6**, asyncpg **0.31.0** and mypy **2.1.0**.
The stage retains the full resolved dependency list; these direct pins do not freeze
all transitives. No SQLAlchemy typing plugin or external stubs are needed.

These tests create/drop their `k16_*` tables. Set `K16_PG_SOCKET` to the Unix-socket
directory of a **disposable PostgreSQL database** accessible as postgres, database
postgres. This is local fixture authentication, not production configuration. K16
used a task-owned container with network disabled, database data in tmpfs and only
a task-scoped socket directory mounted to the host. Production uses its own role,
credentials and driver transport; do not repoint this fixture at an application DB.

```sh
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m mypy --config-file mypy.ini
.venv/bin/python -W error -m unittest -v test_command test_projection
```

### `requirements.txt`

```text
SQLAlchemy[asyncio]==2.0.54
psycopg[binary]==3.3.6
asyncpg==0.31.0
mypy==2.1.0
```

### `mypy.ini`

```ini
[mypy]
python_version = 3.11
strict = True
disallow_any_explicit = True
disallow_any_unimported = True
files = command.py, projection.py, test_command.py, test_projection.py
```

## Operation and mapping

`parse_quantity` validates representation (including rejecting bool/string); positive
quantity and sufficient current stock are independent operation rules. The typed
Reserve command assumes the adapter has parsed representation and authorized access.
It is not a public unvalidated DTO. The single-SKU fixture has no tenant/auth model.

`reserve_in_transaction` participates in its caller's transaction and does not commit.
The convenience owner `reserve` commits before returning its result. A zero remaining
value is a successful reservation; None means the conditional write found no eligible
row. The database check protects direct invalid stock writes too.

### `command.py`

```python
from dataclasses import dataclass

from sqlalchemy import CheckConstraint, ForeignKey, update
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedAsDataclass, Session, mapped_column, sessionmaker


class Base(MappedAsDataclass, DeclarativeBase):
    pass


class Stock(Base):
    __tablename__ = 'k16_stock'
    __table_args__ = (CheckConstraint('remaining >= 0', name='k16_stock_nonnegative'),)

    sku: Mapped[str] = mapped_column(primary_key=True)
    remaining: Mapped[int]


class Receipt(Base):
    __tablename__ = 'k16_receipt'
    __table_args__ = (CheckConstraint('quantity > 0', name='k16_receipt_positive'),)

    key: Mapped[str] = mapped_column(primary_key=True)
    sku: Mapped[str] = mapped_column(ForeignKey('k16_stock.sku'))
    quantity: Mapped[int]


@dataclass(frozen=True)
class Reserve:
    key: str
    sku: str
    quantity: int


@dataclass(frozen=True)
class Reserved:
    key: str
    remaining: int


def parse_quantity(value: object) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError('quantity must be an integer')
    return value


def reserve_in_transaction(session: Session, command: Reserve) -> Reserved | None:
    """Persistence operation: caller owns the active transaction and authorization."""
    if command.quantity <= 0:
        raise ValueError('quantity must be positive')
    statement = (
        update(Stock)
        .where(Stock.sku == command.sku, Stock.remaining >= command.quantity)
        .values(remaining=Stock.remaining - command.quantity)
        .returning(Stock.remaining)
    )
    remaining = session.scalar(statement)
    if remaining is None:
        return None
    session.add(Receipt(key=command.key, sku=command.sku, quantity=command.quantity))
    session.flush()
    return Reserved(key=command.key, remaining=remaining)


def reserve(factory: sessionmaker[Session], command: Reserve) -> Reserved | None:
    with factory.begin() as session:
        result = reserve_in_transaction(session, command)
    return result
```

The receipt key is unique, but this is not complete idempotency. A duplicate flush
raises IntegrityError and the owner rolls back the decrement; a real replay protocol
must compare payload and recover a stored result after an uncertain COMMIT. An
insufficient-stock replay can return None before encountering a duplicate key.
Do not swallow an insertion error and commit a debit without its receipt. The
transport adapter maps known failures separately; this example lets database failures
propagate to its owner rather than calling every integrity error a duplicate request.

## Executed checks

Five tests use fresh committed state through real PostgreSQL sessions. They cover
representation versus domain refusal, committed success including exact exhaustion,
duplicate-flush rollback followed by a clean new operation, rollback by a larger
caller, competing per-thread sessions, and a constraint bypassing operation code.
The barrier starts competing attempts together; it does not establish a particular
server lock-wait interleaving or benchmark. Both results and committed state matter.

### `test_command.py`

```python
import os
import unittest
from concurrent.futures import ThreadPoolExecutor
from threading import Barrier

from sqlalchemy import URL, create_engine, func, select
from sqlalchemy.engine import Engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session, sessionmaker

from command import Base, Receipt, Reserve, Stock, parse_quantity, reserve, reserve_in_transaction


class CommandTests(unittest.TestCase):
    engine: Engine
    factory: sessionmaker[Session]

    def setUp(self) -> None:
        self.engine = create_engine(
            URL.create('postgresql+psycopg', username='postgres', database='postgres',
                       query={'host': os.environ['K16_PG_SOCKET']}),
            connect_args={'options': '-c statement_timeout=5000 -c lock_timeout=3000'},
        )
        # Only in the explicitly supplied disposable test database.
        Base.metadata.drop_all(self.engine)
        Base.metadata.create_all(self.engine)
        self.factory = sessionmaker(self.engine)
        with self.factory.begin() as session:
            session.add(Stock(sku='book', remaining=3))

    def tearDown(self) -> None:
        Base.metadata.drop_all(self.engine)
        self.engine.dispose()

    def state(self) -> tuple[int, int]:
        with self.factory() as session:
            return (
                session.scalars(select(Stock.remaining)).one(),
                session.scalars(select(func.count()).select_from(Receipt)).one(),
            )

    def test_representation_and_business_refusals_preserve_stock(self) -> None:
        for value in ('2', True, None):
            with self.assertRaises(ValueError):
                parse_quantity(value)
        self.assertEqual(parse_quantity(-1), -1)
        for quantity in (-1, 0):
            with self.assertRaises(ValueError):
                reserve(self.factory, Reserve('invalid', 'book', quantity))
        self.assertIsNone(reserve(self.factory, Reserve('large', 'book', 4)))
        self.assertIsNone(reserve(self.factory, Reserve('missing', 'absent', 1)))
        self.assertEqual(self.state(), (3, 0))

    def test_committed_success_and_duplicate_flush_rollback(self) -> None:
        first = reserve(self.factory, Reserve('request', 'book', 1))
        self.assertIsNotNone(first)
        self.assertEqual(self.state(), (2, 1))
        with self.assertRaises(IntegrityError):
            reserve(self.factory, Reserve('request', 'book', 1))
        self.assertEqual(self.state(), (2, 1))
        # A new operation can acquire a clean session after the failed flush.
        self.assertIsNotNone(reserve(self.factory, Reserve('next', 'book', 1)))
        self.assertEqual(self.state(), (1, 2))
        final = reserve(self.factory, Reserve('last', 'book', 1))
        if final is None:
            self.fail('Expected reservation of the final item')
        self.assertEqual(final.remaining, 0)
        self.assertEqual(self.state(), (0, 3))

    def test_outer_operation_failure_rolls_back_flushed_changes(self) -> None:
        with self.assertRaisesRegex(RuntimeError, 'abort operation'):
            with self.factory.begin() as session:
                result = reserve_in_transaction(session, Reserve('outer', 'book', 2))
                self.assertIsNotNone(result)
                raise RuntimeError('abort operation')
        self.assertEqual(self.state(), (3, 0))

    def test_separate_sessions_compete_without_overselling(self) -> None:
        ready = Barrier(2, timeout=5)

        def compete(key: str) -> bool:
            with self.factory.begin() as session:
                ready.wait()
                return reserve_in_transaction(session, Reserve(key, 'book', 2)) is not None

        with ThreadPoolExecutor(max_workers=2) as pool:
            futures = [pool.submit(compete, key) for key in ('a', 'b')]
            results = [future.result(timeout=10) for future in futures]
        self.assertEqual(sorted(results), [False, True])
        self.assertEqual(self.state(), (1, 1))

    def test_database_constraint_covers_direct_adapter_write(self) -> None:
        with self.assertRaises(IntegrityError):
            with self.factory.begin() as session:
                session.add(Stock(sku='bad', remaining=-1))
        self.assertEqual(self.state(), (3, 0))


if __name__ == '__main__':
    unittest.main()
```

The complete shared suite passed **9 tests** with warnings treated as errors; strict
mypy passed all four Python files. Context-managed tests use real commits, not an
outer test transaction that hides commit behavior. Fixture DDL uses metadata only
because these are fresh disposable tables, not because create_all migrates schemas.

Limits: no production authorization, idempotency receipt replay, SQLSTATE translation,
deadlock/retry scheduler, real migration, proxy pool, lost connection during COMMIT,
failover or load benchmark. The psycopg dialect is a fixture dependency, not K17
adoption. No SQLAlchemy 1.4/2.1 runtime or alternative database was tested.
