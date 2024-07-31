import abc

from src.orders.domain import Order


class IOrderRepository(abc.ABC):
    @abc.abstractmethod
    def get(self, order_id: str) -> Order:
        """Retrieves a Order given the order id."""
