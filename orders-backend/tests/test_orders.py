from decimal import Decimal
from src.orders.domain import Order, OrderDiscountType, OrderItem, OrderDiscount
from src.orders.repositories import IOrderRepository
from src.orders.use_cases import OrdersUseCase
from fastapi import status


class TestOrdersAPI:
    def test_get_orders(self, client):
        response = client.get("/orders/1")
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {
            "id": "1",
            "status": "OPENED",
            "items": [
                {"name": "Corona", "quantity": 3, "unit_price": "10000"},
                {"name": "Club Colombia", "quantity": 2, "unit_price": "11900"},
                {"name": "Quilmes", "quantity": 2, "unit_price": "8900"},
            ],
            "rounds": [
                {
                    "created_at": "2024-09-10T12:00:30",
                    "items": [
                        {"name": "Corona", "quantity": 3},
                        {"name": "Club Colombia", "quantity": 1},
                    ],
                },
                {
                    "created_at": "2024-09-10T12:20:31",
                    "items": [
                        {"name": "Club Colombia", "quantity": 1},
                        {"name": "Quilmes", "quantity": 2},
                    ],
                },
                {
                    "created_at": "2024-09-10T12:43:21",
                    "items": [{"name": "Quilmes", "quantity": 3}],
                },
            ],
            "created_at": "2024-09-10T12:00:00",
            "is_paid": False,
            "subtotal": "71600",
            "discounts": "7160",
            "total": "64440",
        }


class DummyOrderRepository(IOrderRepository):
    def get(self, order_id: str) -> Order:
        return Order(
            id=order_id,
            items=[
                OrderItem(
                    name="Club Colombia", quantity=10, unit_price=Decimal(1_000.0)
                ),
                OrderItem(name="Poker", quantity=5, unit_price=Decimal(2_000.0)),
                OrderItem(name="Quilmes", quantity=4, unit_price=Decimal(3_000.0)),
            ],
        )


class TestOrders:
    def test_validate_order_totals(self):
        orders_use_case = OrdersUseCase(order_repository=DummyOrderRepository())

        order = orders_use_case.get_order("1")

        assert order.subtotal == order.total == Decimal(32_000.0)

    def test_validate_order_totals_with_discount(self):
        orders_use_case = OrdersUseCase(order_repository=DummyOrderRepository())

        order = orders_use_case.get_order("1")

        order.discount = OrderDiscount(value=40, type=OrderDiscountType.PERCENTAGE)

        assert order.discounts == Decimal(12_800.0)

        assert order.total == Decimal(19_200.0)
