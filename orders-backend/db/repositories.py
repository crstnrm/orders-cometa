from typing import Any
from db.fixtures import orders
from src.orders.domain import Order
from src.orders.exceptions import EOrderDoesNotExist
from src.orders.repositories import IOrderRepository


class OrderRepository(IOrderRepository):
    def __init__(self, db: dict[str, Any] | None = None) -> None:
        self._db = db or {"orders": orders}

    def get(self, order_id: str) -> Order:
        """Retrieves an Order given an `order_id`."""

        try:
            raw_order = next(
                order
                for order in self._db.get("orders", [])
                if order.get("id") == order_id
            )
        except StopIteration as err:
            raise EOrderDoesNotExist(
                message=f"The order {order_id} doesn't exist."
            ) from err

        return Order.parse(raw_order)
