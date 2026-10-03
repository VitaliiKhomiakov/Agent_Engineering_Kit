# Example: HTTP validation and a domain capacity rule

Read when deciding what belongs to an endpoint versus the state owner. The
transport accepts a bounded strict integer, invokes an injected typed function,
maps a capacity conflict, and exposes a public receipt. The domain also checks
its invariant when called without HTTP. No DI container or Repository is needed
for this example. See [transport](../transport.md).

Save the three Python blocks under the indicated names in one temporary folder.
They use Python 3.11 syntax, FastAPI 0.138.0, Pydantic 2.13.4, Starlette 1.3.1,
and HTTPX 0.28.1; the executed interpreter was Python 3.12.3. These are the checked
versions, not an instruction to upgrade a project. The Content-Type expectations
depend on FastAPI 0.132.0+ defaults.

`reservations.py` is independent of HTTP:

```python
from dataclasses import dataclass


class CapacityExceeded(Exception):
    pass


@dataclass(frozen=True)
class Receipt:
    seats: int
    remaining: int
    internal_reference: str


@dataclass
class Event:
    remaining: int
    internal_reference: str

    def reserve(self, seats: int) -> Receipt:
        if seats < 1:
            raise ValueError("seats must be positive")
        if seats > self.remaining:
            raise CapacityExceeded("insufficient capacity")
        self.remaining -= seats
        return Receipt(seats, self.remaining, self.internal_reference)
```

`reservation_http.py` owns parsing, dependency wiring, and public responses:

```python
from collections.abc import Callable
from typing import Annotated

from fastapi import APIRouter, Depends, FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import Response
from pydantic import BaseModel, ConfigDict, Field

from reservations import CapacityExceeded, Receipt


class ReservationInput(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid")
    seats: Annotated[int, Field(ge=1, le=20)]


class PublicReceipt(BaseModel):
    seats: int
    remaining: int


class PublicError(BaseModel):
    detail: str


def create_app(reserve: Callable[[int], Receipt]) -> FastAPI:
    app = FastAPI()
    router = APIRouter()

    async def get_reserve() -> Callable[[int], Receipt]:
        return reserve

    @app.exception_handler(RequestValidationError)
    async def invalid_input(
        request: Request, exc: RequestValidationError
    ) -> Response:
        # Deliberate direct Response: serialize only this owned public contract.
        error = PublicError(detail="Invalid reservation input")
        return Response(
            content=error.model_dump_json(),
            status_code=422,
            media_type="application/json",
        )

    @router.post(
        "/reservations",
        status_code=201,
        responses={422: {"model": PublicError}, 409: {"model": PublicError}},
    )
    async def reserve_seats(
        payload: ReservationInput,
        operation: Annotated[Callable[[int], Receipt], Depends(get_reserve)],
    ) -> PublicReceipt:
        try:
            receipt = operation(payload.seats)
        except CapacityExceeded as exc:
            raise HTTPException(409, "Not enough seats") from exc
        return PublicReceipt(seats=receipt.seats, remaining=receipt.remaining)

    app.include_router(router)
    return app
```

`test_reservation_http.py` checks observable behavior and the affected schemas:

```python
import unittest

from fastapi.testclient import TestClient

from reservation_http import create_app
from reservations import CapacityExceeded, Event, Receipt


class ReservationTests(unittest.TestCase):
    def test_success_has_only_public_fields(self) -> None:
        event = Event(5, "private-reference")
        with TestClient(create_app(event.reserve)) as client:
            response = client.post("/reservations", json={"seats": 2})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {"seats": 2, "remaining": 3})
        self.assertEqual(event.remaining, 3)
        self.assertNotIn("private-reference", response.text)

    def test_domain_conflict_preserves_state(self) -> None:
        event = Event(1, "private-reference")
        with TestClient(create_app(event.reserve)) as client:
            response = client.post("/reservations", json={"seats": 2})
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.json(), {"detail": "Not enough seats"})
        self.assertEqual(event.remaining, 1)

    def test_invalid_bodies_do_not_reserve_or_echo_input(self) -> None:
        event = Event(5, "private-reference")
        bodies = (
            b'{"seats": 0}', b'{"seats": 21}', b'{"seats": true}',
            b'{"seats": "sensitive-value"}', b'{"seats": 2, "admin": true}',
            b'{}', b'{"seats": null}', b'not-json',
        )
        with TestClient(create_app(event.reserve)) as client:
            for body in bodies:
                with self.subTest(body=body):
                    response = client.post(
                        "/reservations", content=body,
                        headers={"Content-Type": "application/json"},
                    )
                    self.assertEqual(response.status_code, 422)
                    self.assertEqual(
                        response.json(), {"detail": "Invalid reservation input"}
                    )
                    self.assertEqual(event.remaining, 5)

    def test_json_requires_appropriate_content_type(self) -> None:
        event = Event(5, "private-reference")
        with TestClient(create_app(event.reserve)) as client:
            for headers in ({}, {"Content-Type": "text/plain"}):
                with self.subTest(headers=headers):
                    response = client.post(
                        "/reservations", content=b'{"seats": 2}', headers=headers
                    )
                    self.assertEqual(response.status_code, 422)
        self.assertEqual(event.remaining, 5)

    def test_domain_checks_without_http(self) -> None:
        event = Event(1, "private-reference")
        with self.assertRaises(ValueError):
            event.reserve(0)
        with self.assertRaises(CapacityExceeded):
            event.reserve(2)
        self.assertEqual(event.remaining, 1)

    def test_unexpected_failure_is_not_reported_as_bad_input(self) -> None:
        def failed_operation(seats: int) -> Receipt:
            raise RuntimeError("private upstream detail")

        with TestClient(
            create_app(failed_operation), raise_server_exceptions=False
        ) as client:
            response = client.post("/reservations", json={"seats": 1})
        self.assertEqual(response.status_code, 500)
        self.assertNotIn("private upstream detail", response.text)

    def test_openapi_matches_owned_response_contracts(self) -> None:
        schema = create_app(Event(5, "private-reference").reserve).openapi()
        operation = schema["paths"]["/reservations"]["post"]
        self.assertEqual(set(operation["responses"]), {"201", "409", "422"})
        models = schema["components"]["schemas"]
        self.assertEqual(set(models["PublicReceipt"]["properties"]), {"seats", "remaining"})
        self.assertEqual(models["ReservationInput"]["required"], ["seats"])
        self.assertFalse(models["ReservationInput"]["additionalProperties"])
        self.assertEqual(
            operation["responses"]["422"]["content"]["application/json"]["schema"],
            {"$ref": "#/components/schemas/PublicError"},
        )
```

Run `python3 -W default -m unittest -v test_reservation_http` and the project's
strict analyzer with its Pydantic plugin over all three modules. The
[practice plan](../../../docs/plans/2026-09-21-engineering-practices.md) records
the executed commands and results. On this stack Starlette warns that its HTTPX
TestClient backend is deprecated in favor of HTTPX2; the warning remains visible.
Treat migration as a versioned dependency change, not an automatic example setup.

This intentionally sequential, in-memory example assumes a valid initial Event.
It does not establish durable reservations, concurrent capacity enforcement,
authentication, idempotency, or database rollback. A real storage operation must
enforce capacity and commit atomically before returning; use its actual blocking
or async contract rather than putting blocking I/O in this short async handler.
The fixed 422 shape is an explicit API choice and omits field-level diagnostics.
