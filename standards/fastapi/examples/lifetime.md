# Example: lifespan client and request-owned upstream stream

Read when a response consumes a resource after the endpoint returns. An app
factory owns one HTTP client through lifespan. A yield dependency opens an
upstream response and checks its status before downstream headers are sent.
The streaming route keeps that response open through consumption; a bounded
snapshot route finishes reading in the handler and can close earlier.
See [dependency lifetime](../dependencies-lifetime.md).

Save the two blocks in the same temporary folder. Checked: Python 3.12.3,
FastAPI 0.138.0, Starlette 1.3.1, HTTPX 0.28.1, and AnyIO 4.14.0. Syntax targets
Python 3.11; explicit dependency scopes require FastAPI 0.121.0+. All requests
in the tests use an in-memory transport, with no DNS or remote service.

`feed_http.py`:

```python
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import Annotated

import anyio
import httpx
from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import PlainTextResponse, StreamingResponse


def create_app(transport: httpx.AsyncBaseTransport) -> FastAPI:
    shared_client: httpx.AsyncClient | None = None

    @asynccontextmanager
    async def lifespan(app: FastAPI) -> AsyncIterator[None]:
        nonlocal shared_client
        async with httpx.AsyncClient(
            base_url="https://feed.example.invalid",
            transport=transport,
            timeout=httpx.Timeout(2.0),
        ) as client:
            shared_client = client
            try:
                yield
            finally:
                shared_client = None

    app = FastAPI(lifespan=lifespan)

    async def open_feed() -> AsyncIterator[httpx.Response]:
        client = shared_client
        if client is None:
            raise RuntimeError("application lifespan is not active")
        try:
            upstream = await client.send(
                client.build_request("GET", "/feed"), stream=True
            )
        except httpx.TimeoutException as exc:
            raise HTTPException(504, "Feed timed out") from exc
        except httpx.RequestError as exc:
            raise HTTPException(502, "Feed unavailable") from exc
        try:
            if upstream.status_code != 200:
                raise HTTPException(502, "Feed unavailable")
            yield upstream
        finally:
            # Allow awaited cleanup under cancellation, with a finite deadline.
            with anyio.fail_after(1.0, shield=True):
                await upstream.aclose()

    @app.get("/feed", response_class=PlainTextResponse)
    async def stream_feed(
        upstream: Annotated[httpx.Response, Depends(open_feed, scope="request")],
    ) -> StreamingResponse:
        return StreamingResponse(upstream.aiter_bytes(), media_type="text/plain")

    @app.get("/snapshot", response_class=PlainTextResponse)
    async def snapshot(
        upstream: Annotated[httpx.Response, Depends(open_feed, scope="function")],
    ) -> PlainTextResponse:
        body = bytearray()
        async for chunk in upstream.aiter_bytes():
            if len(body) + len(chunk) > 1024:
                raise HTTPException(502, "Feed snapshot too large")
            body.extend(chunk)
        return PlainTextResponse(bytes(body))

    return app
```

`test_feed_http.py`:

```python
from collections.abc import AsyncIterator
import unittest

import httpx
from fastapi.testclient import TestClient

from feed_http import create_app


class RecordedStream(httpx.AsyncByteStream):
    def __init__(self, events: list[str], body: bytes, fail: bool) -> None:
        self.events = events
        self.body = body
        self.fail = fail
        self.closed = False

    async def __aiter__(self) -> AsyncIterator[bytes]:
        if self.closed:
            raise RuntimeError("stream used after close")
        self.events.append("read")
        yield self.body
        if self.fail:
            raise httpx.ReadError("private streaming failure")

    async def aclose(self) -> None:
        self.closed = True
        self.events.append("stream-close")


class RecordedTransport(httpx.AsyncBaseTransport):
    def __init__(
        self, status: int = 200, body: bytes = b"one\ntwo\n",
        fail_read: bool = False, timeout: bool = False,
    ) -> None:
        self.events: list[str] = []
        self.status = status
        self.body = body
        self.fail_read = fail_read
        self.timeout = timeout

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        self.events.append("request")
        if self.timeout:
            raise httpx.ReadTimeout("private timeout", request=request)
        return httpx.Response(
            self.status,
            stream=RecordedStream(self.events, self.body, self.fail_read),
        )

    async def aclose(self) -> None:
        self.events.append("client-close")


class FeedTests(unittest.TestCase):
    def test_stream_consumed_before_close_and_client_reused(self) -> None:
        transport = RecordedTransport()
        with TestClient(create_app(transport)) as client:
            for path in ("/feed", "/feed"):
                response = client.get(path)
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.content, b"one\ntwo\n")
            self.assertEqual(
                transport.events, ["request", "read", "stream-close"] * 2
            )
        self.assertEqual(transport.events[-1], "client-close")

    def test_function_scope_is_sufficient_for_consumed_snapshot(self) -> None:
        transport = RecordedTransport()
        with TestClient(create_app(transport)) as client:
            response = client.get("/snapshot")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content, b"one\ntwo\n")
            self.assertEqual(transport.events, ["request", "read", "stream-close"])
        self.assertEqual(transport.events[-1], "client-close")

    def test_upstream_rejection_precedes_success_and_closes(self) -> None:
        transport = RecordedTransport(status=503)
        with TestClient(create_app(transport)) as client:
            response = client.get("/feed")
            self.assertEqual(response.status_code, 502)
            self.assertEqual(response.json(), {"detail": "Feed unavailable"})
            self.assertEqual(transport.events, ["request", "stream-close"])
        self.assertEqual(transport.events[-1], "client-close")

    def test_connection_timeout_is_safe_gateway_error(self) -> None:
        transport = RecordedTransport(timeout=True)
        with TestClient(create_app(transport)) as client:
            response = client.get("/feed")
            self.assertEqual(response.status_code, 504)
            self.assertEqual(response.json(), {"detail": "Feed timed out"})
        self.assertEqual(transport.events, ["request", "client-close"])

    def test_stream_failure_propagates_and_releases_resource(self) -> None:
        transport = RecordedTransport(fail_read=True)
        with TestClient(create_app(transport)) as client:
            with self.assertRaises(httpx.ReadError):
                client.get("/feed")
            self.assertEqual(transport.events, ["request", "read", "stream-close"])
        self.assertEqual(transport.events[-1], "client-close")

    def test_snapshot_bound_rejects_without_leaking_stream(self) -> None:
        transport = RecordedTransport(body=b"x" * 1025)
        with TestClient(create_app(transport)) as client:
            response = client.get("/snapshot")
            self.assertEqual(response.status_code, 502)
            self.assertEqual(response.json(), {"detail": "Feed snapshot too large"})
            self.assertEqual(transport.events, ["request", "read", "stream-close"])
        self.assertEqual(transport.events[-1], "client-close")

    def test_missing_lifespan_does_not_use_uninitialized_client(self) -> None:
        transport = RecordedTransport()
        client = TestClient(create_app(transport))
        try:
            with self.assertRaisesRegex(RuntimeError, "lifespan is not active"):
                client.get("/feed")
        finally:
            client.close()
        self.assertEqual(transport.events, [])
```

Run `python3 -W default -m unittest -v test_feed_http` and the project's strict
analyzer over both modules. Actual results are in the
[practice plan](../../../docs/plans/2026-09-21-engineering-practices.md). The installed
Starlette TestClient supports HTTPX with a visible deprecation warning in favor of
HTTPX2; no dependency migration is implied by this example.

The decorators document `text/plain`; the streaming handler supplies its own
StreamingResponse, so it still owns its actual bytes and headers.
The custom transport supplies deterministic lifecycle evidence. It does not
implement network pooling or timeouts; the timeout test injects the exception.
A real adapter can use `httpx.AsyncHTTPTransport` with its own connection limits
(passing a custom transport means that transport owns pool configuration).
Choose deadlines/limits from the integration contract; the small values here
illustrate separate ownership and budgets.

The snapshot bounds its accumulation after receiving each chunk; it is not a
limit on allocation inside the transport. The streaming route assumes a trusted,
bounded feed and fixed text media type, with no retries or durable effects. A
production stream may need total duration/byte limits and disconnect handling.
These buffered in-process tests establish consumption/cleanup and failure
semantics, not network backpressure, cancellation, or graceful server shutdown.
