from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from enum import StrEnum

from src.core.domain import Base


@dataclass
class OrderRoundItem(Base):
    name: str
    quantity: int


@dataclass
class OrderRound(Base):
    created_at: datetime
    items: list[OrderRoundItem]


class OrderStatus(StrEnum):
    OPENED = "OPENED"
    PAID = "PAID"


@dataclass
class OrderItem(Base):
    name: str
    quantity: int
    unit_price: Decimal

    @property
    def total(self) -> Decimal:
        return Decimal(self.quantity * self.unit_price)


class OrderDiscountType(StrEnum):
    AMOUNT = "AMOUNT"
    PERCENTAGE = "PERCENTAGE"


@dataclass
class OrderDiscount(Base):
    value: Decimal
    type: OrderDiscountType


@dataclass
class Order(Base):
    id: str
    status: OrderStatus = OrderStatus.OPENED
    items: list[OrderItem] = field(default_factory=list)
    rounds: list[OrderRound] = field(default_factory=list)
    discount: OrderDiscount | None = None
    created_at: datetime = field(default_factory=datetime.now)

    @property
    def is_paid(self) -> bool:
        return self.status == OrderStatus.PAID

    @property
    def subtotal(self) -> Decimal:
        if not self.items:
            # Making sure the return value is always a Decimal instance.
            return Decimal(0)

        return sum(item.total for item in self.items)  # type: ignore

    @property
    def discounts(self) -> Decimal:
        if not self.discount:
            return Decimal(0)

        if self.discount.type == OrderDiscountType.AMOUNT:
            return self.subtotal - self.discount.value

        if self.discount.type == OrderDiscountType.PERCENTAGE:
            return self.subtotal * self.discount.value / 100

        return Decimal(0)

    @property
    def total(self) -> Decimal:
        return self.subtotal - self.discounts
