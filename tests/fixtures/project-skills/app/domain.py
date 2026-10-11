"""Static starting input for a design observation, not an executed API fixture."""

from dataclasses import dataclass
from threading import Lock
from typing import Literal
from uuid import uuid4


@dataclass(frozen=True)
class Reservation:
    id: str
    quantity: int
    state: Literal["active", "cancelled"] = "active"


class Inventory:
    def __init__(self, stock: int) -> None:
        self._stock = stock
        self._reservations: dict[str, Reservation] = {}
        self._lock = Lock()

    def reserve(self, quantity: int) -> Reservation:
        with self._lock:
            if quantity <= 0 or quantity > self._stock:
                raise ValueError("invalid_quantity")
            result = Reservation(str(uuid4()), quantity)
            self._reservations[result.id] = result
            self._stock -= quantity
            return result

    def get(self, reservation_id: str) -> Reservation:
        with self._lock:
            return self._reservations[reservation_id]
