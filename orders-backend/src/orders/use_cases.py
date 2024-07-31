from dataclasses import dataclass
from src.orders.domain import Order
from src.orders.repositories import IOrderRepository


@dataclass
class OrdersUseCase:
    order_repository: IOrderRepository

    def get_order(self, order_id: str) -> Order:
        return self.order_repository.get(order_id=order_id)
