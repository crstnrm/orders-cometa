from fastapi import APIRouter, status

from src.orders.use_cases import OrdersUseCase
from web.bootstrap import inject
from web.orders.serializers import Order as OrderResponse

router = APIRouter()


@router.get(
    "/orders/{order_id}", status_code=status.HTTP_200_OK, response_model=OrderResponse
)
def get_columns(order_id: str):
    orders_use_case: OrdersUseCase = inject(OrdersUseCase)

    return orders_use_case.get_order(order_id=order_id)
