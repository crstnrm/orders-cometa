from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel


class OrderRoundItem(BaseModel):
    name: str
    quantity: int


class OrderRound(BaseModel):
    created_at: datetime
    items: list[OrderRoundItem]


class OrderItem(BaseModel):
    name: str
    quantity: int
    unit_price: Decimal


class Order(BaseModel):
    id: str
    status: str
    items: list[OrderItem]
    rounds: list[OrderRound]
    created_at: datetime
    is_paid: bool
    subtotal: Decimal
    discounts: Decimal
    total: Decimal
