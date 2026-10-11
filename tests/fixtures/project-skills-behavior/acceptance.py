"""Domain behavior oracle for a generated cancellation implementation."""

from concurrent.futures import ThreadPoolExecutor
from dataclasses import FrozenInstanceError
import unittest

from app.domain import Inventory


class CancellationAcceptance(unittest.TestCase):
    def test_transition_identity_and_single_stock_return(self) -> None:
        inventory = Inventory(10)
        original = inventory.reserve(4)
        cancelled = inventory.cancel(original.id)
        self.assertEqual((cancelled.id, cancelled.quantity, cancelled.state), (original.id, 4, "cancelled"))
        self.assertEqual(original.state, "active")
        self.assertEqual(inventory.get(original.id), cancelled)
        self.assertEqual(inventory.cancel(original.id), cancelled)
        inventory.reserve(10)
        with self.assertRaisesRegex(ValueError, "invalid_quantity"):
            inventory.reserve(1)
        with self.assertRaises(FrozenInstanceError):
            setattr(cancelled, "quantity", 9)

    def test_missing_id_preserves_existing_state_and_capacity(self) -> None:
        inventory = Inventory(10)
        reservation = inventory.reserve(4)
        with self.assertRaises(KeyError):
            inventory.cancel("missing")
        self.assertEqual(inventory.get(reservation.id), reservation)
        inventory.reserve(6)
        with self.assertRaises(ValueError):
            inventory.reserve(1)

    def test_concurrent_cancel_returns_stock_once(self) -> None:
        inventory = Inventory(10)
        reservation = inventory.reserve(10)
        with ThreadPoolExecutor(max_workers=8) as pool:
            results = list(pool.map(inventory.cancel, [reservation.id] * 32))
        self.assertTrue(all(item == results[0] and item.state == "cancelled" for item in results))
        inventory.reserve(10)
        with self.assertRaises(ValueError):
            inventory.reserve(1)


if __name__ == "__main__":
    unittest.main()
