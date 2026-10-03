# Pydantic example: a booking input boundary

Read when strict parsing, presence, cross-field consistency, or safe validation
errors need a concrete example. Return to [validation](../validation.md).
Requires Python 3.11+ and Pydantic **2.13.4** (pydantic-core **2.46.4**), the
executed baseline. Use the project's existing environment; these versions do
not authorize upgrading a target project. No email/HTTP/ORM dependency is needed.

The sample API accepts JSON dates, an integer guest count from 1 to 12, and a
required note that may be null. A stay's end must follow its start. This is input
consistency, not proof of availability, payment, permission, or a valid booking
state transition. Those remain application/domain checks before effects.

Save as `booking_input.py`:

```python
from datetime import date
from typing import Annotated, Self

from pydantic import BaseModel, ConfigDict, Field, ValidationError, model_validator


class BookingInput(BaseModel):
    model_config = ConfigDict(
        strict=True, extra="forbid", frozen=True, hide_input_in_errors=True
    )

    starts_on: date
    ends_on: date
    guests: Annotated[int, Field(ge=1, le=12)]
    note: Annotated[str, Field(max_length=200)] | None

    @model_validator(mode="after")
    def check_window(self) -> Self:
        if self.ends_on <= self.starts_on:
            raise ValueError("end must follow start")
        return self


class InvalidBookingInput(ValueError):
    pass


def parse_booking(body: bytes) -> BookingInput:
    try:
        return BookingInput.model_validate_json(body)
    except ValidationError as error:
        raise InvalidBookingInput("invalid booking request") from error
```

Strict JSON validation intentionally accepts ISO date strings. Passing the same
strings through strict Python-object validation has a different contract.
`note` has no default: null is valid, omission is not. A normal typed constructor
can receive actual `date` objects. The adapter returns one named type; an
independent use case should receive its owned command/values when transport
coupling would otherwise cross the boundary.

The public error has fixed text and preserves an internal cause. Do not return
or log that cause's raw structured details; `hide_input_in_errors` is not universal
redaction. Unexpected programming errors are not caught as invalid input. A real
transport still owns body limits, authentication, error status/code, and dispatch.

Save as `test_booking_input.py` beside the module:

```python
from datetime import date
import json
import unittest

from pydantic import ValidationError

from booking_input import BookingInput, InvalidBookingInput, parse_booking


def valid_payload() -> dict[str, object]:
    return {
        "starts_on": "2026-10-01",
        "ends_on": "2026-10-03",
        "guests": 2,
        "note": None,
    }


def encode(payload: dict[str, object]) -> bytes:
    return json.dumps(payload).encode()


class BookingInputTests(unittest.TestCase):
    def test_strict_json_accepts_dates_and_explicit_null(self) -> None:
        result = parse_booking(encode(valid_payload()))
        self.assertEqual(result.starts_on, date(2026, 10, 1))
        self.assertEqual(result.ends_on, date(2026, 10, 3))
        self.assertEqual(result.guests, 2)
        self.assertIsNone(result.note)

    def test_python_input_requires_date_objects(self) -> None:
        with self.assertRaises(ValidationError):
            BookingInput.model_validate(valid_payload())
        result = BookingInput(
            starts_on=date(2026, 10, 1), ends_on=date(2026, 10, 3),
            guests=2, note=None,
        )
        self.assertEqual(result, parse_booking(encode(valid_payload())))

    def test_missing_note_and_extra_fields_are_rejected(self) -> None:
        missing = valid_payload()
        del missing["note"]
        for payload in (missing, {**valid_payload(), "paid": True}):
            with self.subTest(payload=payload), self.assertRaises(InvalidBookingInput):
                parse_booking(encode(payload))

    def test_guest_contract_rejects_coercions_and_out_of_range(self) -> None:
        invalid: tuple[object, ...] = (True, "2", 2.0, 0, 13, None)
        for value in invalid:
            with self.subTest(value=value), self.assertRaises(InvalidBookingInput):
                parse_booking(encode({**valid_payload(), "guests": value}))

    def test_invalid_windows_and_malformed_json_are_rejected(self) -> None:
        for end in ("2026-09-30", "2026-10-01", "not-a-date"):
            with self.subTest(end=end), self.assertRaises(InvalidBookingInput):
                parse_booking(encode({**valid_payload(), "ends_on": end}))
        with self.assertRaises(InvalidBookingInput):
            parse_booking(b"{")

    def test_public_error_does_not_echo_rejected_note(self) -> None:
        with self.assertRaises(InvalidBookingInput) as failure:
            parse_booking(encode({**valid_payload(), "note": "private" * 40}))
        self.assertEqual(str(failure.exception), "invalid booking request")

    def test_published_schema_keeps_note_required_and_nullable(self) -> None:
        schema = BookingInput.model_json_schema(mode="validation")
        self.assertIn("note", schema["required"])
        self.assertIn({"type": "null"}, schema["properties"]["note"]["anyOf"])
        self.assertEqual(schema["properties"]["guests"]["minimum"], 1)
        self.assertEqual(schema["properties"]["guests"]["maximum"], 12)
        self.assertFalse(schema["additionalProperties"])
```

Run `python -W error -m unittest -v test_booking_input`. Check the module and tests
with the pinned mypy/Pydantic plugin configuration described in
[verification](../verification.md). Schema assertions stay at the schema boundary;
their dynamic library representation is not an application result contract.
The test does not claim that JSON Schema encodes the end-after-start validator.

For a state-dependent rule, compare the existing
[Python publication example](../../python/examples/domain.md); do not duplicate
that rule in input validators. Actual execution evidence is in the
[practice plan](../../../docs/plans/2026-09-21-engineering-practices.md).
