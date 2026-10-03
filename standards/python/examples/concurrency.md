# Python example: two required results with one lifetime

Read when related async operations must succeed together and finish cleanup
before their caller continues. Return to [execution and resources](../execution-resources.md).
Requires Python 3.11+ for `TaskGroup`, `asyncio.timeout`, and `except*`; only the
standard library is used.

Save as `source_pair.py`:

```python
import asyncio
from dataclasses import dataclass
from typing import Protocol


class TextSource(Protocol):
    async def read(self) -> str: ...


@dataclass(frozen=True)
class SourceTexts:
    primary: str
    secondary: str


async def read_pair(
    primary: TextSource,
    secondary: TextSource,
    *,
    timeout_seconds: float,
) -> SourceTexts:
    async with asyncio.timeout(timeout_seconds):
        async with asyncio.TaskGroup() as group:
            first = group.create_task(primary.read())
            second = group.create_task(secondary.read())
        return SourceTexts(primary=first.result(), secondary=second.result())
```

The consumer owns a narrow structural port and receives already assembled
implementations. Two tasks give fixed fan-out, and fields keep input/result
identity independent of completion order. The group joins its children before
returning; an ordinary child failure cancels its sibling and raises an exception
group. The timeout becomes `TimeoutError` outside its context; caller cancellation
remains cancellation. These choices are part of the function's contract.

Sequential calls are simpler if the operations depend on each other or overlap
has no value. This example provides no atomicity for external writes, durable
work, thread termination, or hard wall-clock deadline. Adapters must cooperate
with cancellation and own their resources; a blocking call can prevent timeout
delivery. A large collection needs separate backpressure, not one task per item.

Save as `test_source_pair.py` beside the module:

```python
import asyncio
import unittest

from source_pair import SourceTexts, read_pair


class ControlledSource:
    def __init__(self, text: str) -> None:
        self.text: str = text
        self.started: asyncio.Event = asyncio.Event()
        self.release: asyncio.Event = asyncio.Event()
        self.cleaned: asyncio.Event = asyncio.Event()

    async def read(self) -> str:
        self.started.set()
        try:
            await self.release.wait()
            return self.text
        finally:
            self.cleaned.set()


class FailingSource:
    def __init__(self, peer_started: asyncio.Event) -> None:
        self.peer_started: asyncio.Event = peer_started

    async def read(self) -> str:
        await self.peer_started.wait()
        raise LookupError("source unavailable")


class SourcePairTests(unittest.IsolatedAsyncioTestCase):
    async def test_success_preserves_source_order_and_joins(self) -> None:
        first, second = ControlledSource("one"), ControlledSource("two")
        async with asyncio.timeout(2):
            operation = asyncio.create_task(read_pair(first, second, timeout_seconds=1))
            await first.started.wait()
            await second.started.wait()
            second.release.set()
            await second.cleaned.wait()
            self.assertFalse(operation.done())
            first.release.set()
            self.assertEqual(await operation, SourceTexts(primary="one", secondary="two"))
        self.assertTrue(first.cleaned.is_set())
        self.assertTrue(second.cleaned.is_set())

    async def test_failure_cancels_and_joins_peer(self) -> None:
        first = ControlledSource("one")
        observed = False
        try:
            await read_pair(first, FailingSource(first.started), timeout_seconds=1)
        except* LookupError as errors:
            self.assertEqual(len(errors.exceptions), 1)
            observed = True
        self.assertTrue(observed)
        self.assertTrue(first.cleaned.is_set())

    async def test_timeout_cleans_up_both_children(self) -> None:
        first, second = ControlledSource("one"), ControlledSource("two")
        with self.assertRaises(TimeoutError):
            await read_pair(first, second, timeout_seconds=0.05)
        self.assertTrue(first.started.is_set())
        self.assertTrue(second.started.is_set())
        self.assertTrue(first.cleaned.is_set())
        self.assertTrue(second.cleaned.is_set())

    async def test_caller_cancellation_cleans_up_both_children(self) -> None:
        first, second = ControlledSource("one"), ControlledSource("two")
        async with asyncio.timeout(2):
            operation = asyncio.create_task(read_pair(first, second, timeout_seconds=10))
            await first.started.wait()
            await second.started.wait()
            operation.cancel()
            with self.assertRaises(asyncio.CancelledError):
                await operation
        self.assertTrue(first.cleaned.is_set())
        self.assertTrue(second.cleaned.is_set())
```

Run `python -W error -m unittest -v test_source_pair` in that directory. Events
coordinate execution; the short timeout exercises a deadline rather than using
a sleep to guess ordering. The default isolated async test loop runs in debug
mode. Run the project's pinned analyzer on the module and tests with `--strict
--disallow-any-explicit --disallow-any-unimported`; the module also passes
`--disallow-any-expr`. Real adapter cleanup, repeated cancellation during async
cleanup, and thread/process behavior need their own checks when affected.

Execution evidence and interpreter/checker versions are recorded in the
[practice plan](../../../docs/plans/2026-09-21-engineering-practices.md).
