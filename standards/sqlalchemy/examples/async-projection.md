# Async loading into an owned public projection

Read when [query loading](../queries-loading.md) must complete before a session closes.
Use the shared setup/pins in the [transaction example](transactional-command.md).
The two Python files below belong in that same temporary directory; all tests require
its disposable PostgreSQL socket. Run them with the published unittest/mypy commands.

## Load before crossing the boundary

The adapter loads shelves and books with an explicit relationship strategy, then
returns frozen DTOs with immutable tuples. `lazy='raise'` makes accidental relationship
access fail near the query rather than issue hidden SQL. The DTO can be used after
session close, including an empty collection and deterministic book ordering.

This demonstrates a loaded ORM graph; a scalar/column projection may be simpler for
a purely tabular read. The 20-parent limit does not bound child collection sizes.
For a real large catalog, choose child bounds/pagination or an aggregate read contract.
The private note is deliberately omitted from output, although this small example
loads the mapped record; selecting fewer database columns is a separate optimization.

### `projection.py`

```python
from dataclasses import dataclass

from sqlalchemy import ForeignKey, select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedAsDataclass, mapped_column, relationship, selectinload


class ReadBase(MappedAsDataclass, DeclarativeBase):
    pass


class Shelf(ReadBase):
    __tablename__ = 'k16_shelf'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    books: Mapped[list['Book']] = relationship(
        back_populates='shelf', lazy='raise', init=False,
        order_by='Book.id', cascade='save-update, merge',
    )


class Book(ReadBase):
    __tablename__ = 'k16_book'

    id: Mapped[int] = mapped_column(primary_key=True)
    shelf_id: Mapped[int] = mapped_column(ForeignKey('k16_shelf.id'))
    title: Mapped[str]
    internal_note: Mapped[str]
    shelf: Mapped[Shelf] = relationship(back_populates='books', init=False, repr=False)


@dataclass(frozen=True)
class ShelfView:
    id: int
    title: str
    book_titles: tuple[str, ...]


async def list_shelves(factory: async_sessionmaker[AsyncSession]) -> tuple[ShelfView, ...]:
    async with factory() as session:
        statement = (
            select(Shelf)
            .order_by(Shelf.id)
            .limit(20)
            .options(selectinload(Shelf.books))
        )
        shelves = (await session.scalars(statement)).all()
        result = tuple(
            ShelfView(shelf.id, shelf.title, tuple(book.title for book in shelf.books))
            for shelf in shelves
        )
    return result
```

## Executed checks and lifetime

Four tests run on a new event loop/engine per test. Two concurrent list operations
share a factory and own separate AsyncSessions. The test without eager loading proves
the relationship guard refuses unexpected access. The cancellation case flushes a
write, signals that milestone, then cancels the owner while it waits; after cleanup,
a fresh session sees no committed row. All waits have explicit deadlines.

### `test_projection.py`

```python
import asyncio
import os
import unittest
from dataclasses import asdict

from sqlalchemy import URL, select
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine

from projection import Book, ReadBase, Shelf, ShelfView, list_shelves


class ProjectionTests(unittest.IsolatedAsyncioTestCase):
    engine: AsyncEngine
    factory: async_sessionmaker[AsyncSession]

    async def asyncSetUp(self) -> None:
        self.engine = create_async_engine(
            URL.create('postgresql+asyncpg', username='postgres', database='postgres',
                       query={'host': os.environ['K16_PG_SOCKET']}),
            connect_args={'server_settings': {'statement_timeout': '5000'}},
        )
        self.factory = async_sessionmaker(self.engine, expire_on_commit=False)
        async with self.engine.begin() as connection:
            await connection.run_sync(ReadBase.metadata.drop_all)
            await connection.run_sync(ReadBase.metadata.create_all)
        async with self.factory.begin() as session:
            shelf = Shelf(id=1, title='Engineering')
            shelf.books.extend([
                Book(id=2, shelf_id=1, title='Transactions', internal_note='private'),
                Book(id=1, shelf_id=1, title='Boundaries', internal_note='private'),
            ])
            session.add_all([shelf, Shelf(id=2, title='Empty')])

    async def asyncTearDown(self) -> None:
        async with self.engine.begin() as connection:
            await connection.run_sync(ReadBase.metadata.drop_all)
        await self.engine.dispose()

    async def test_detached_public_dto_is_complete_and_ordered(self) -> None:
        result = await list_shelves(self.factory)
        self.assertEqual(result, (
            ShelfView(1, 'Engineering', ('Boundaries', 'Transactions')),
            ShelfView(2, 'Empty', ()),
        ))
        self.assertNotIn('private', repr(asdict(result[0])))
        self.assertNotIn('internal_note', asdict(result[0]))

    async def test_unplanned_relationship_access_fails_at_adapter(self) -> None:
        async with self.factory() as session:
            shelf = (await session.scalars(select(Shelf).where(Shelf.id == 1))).one()
            with self.assertRaises(InvalidRequestError):
                tuple(shelf.books)

    async def test_concurrent_read_operations_use_owned_sessions(self) -> None:
        async with asyncio.timeout(10):
            first, second = await asyncio.gather(
                list_shelves(self.factory), list_shelves(self.factory),
            )
        self.assertEqual(first, second)
        self.assertEqual(len(first), 2)

    async def test_cancelled_owner_rolls_back_flushed_write(self) -> None:
        flushed = asyncio.Event()
        hold = asyncio.Event()

        async def pending_write() -> None:
            async with self.factory.begin() as session:
                session.add(Shelf(id=99, title='Uncommitted'))
                await session.flush()
                flushed.set()
                await hold.wait()

        task = asyncio.create_task(pending_write())
        try:
            async with asyncio.timeout(5):
                await flushed.wait()
            task.cancel()
            with self.assertRaises(asyncio.CancelledError):
                await asyncio.wait_for(task, timeout=5)
            async with self.factory() as session:
                self.assertIsNone(await session.get(Shelf, 99))
        finally:
            if not task.done():
                task.cancel()
                with self.assertRaises(asyncio.CancelledError):
                    await asyncio.wait_for(task, timeout=5)


if __name__ == '__main__':
    unittest.main()
```

These four checks and the five sync checks passed on the versions in the shared
setup; strict typing covers both examples and their tests. Engine disposal is awaited
after fixture cleanup. `run_sync` here adapts metadata DDL; it is not a general way
to run blocking application work on an event loop. Tests use create_all only for
fresh disposable tables.

`expire_on_commit=False` suits this async factory, but does not load missing relations
or establish currentness forever. DTO completeness comes from explicit loading and
projection. `lazy='raise'` is not a guarantee that a flush can never issue a SELECT.
No serializer is allowed to depend on a detached ORM graph here.

Limits: cancellation was delivered after flush while awaiting an application event,
not during a driver call or COMMIT. No query-count/load benchmark, stream interruption,
production connection pooler, real TLS/auth/RLS, cache consistency, migration or
other dialect was exercised. The DTO test proves field selection, not an authorization
system or browser/API serialization contract. Async is not required for every service.
