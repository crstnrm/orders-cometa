import inspect
from typing import Any, TypeVar
from db.repositories import OrderRepository
from src.orders.use_cases import OrdersUseCase

_T = TypeVar("_T")


def __inject_dependencies(handler: type[_T], dependencies: dict[str, Any]) -> _T:
    params = inspect.signature(handler).parameters
    handler_dependencies = {
        name: dependency for name, dependency in dependencies.items() if name in params
    }
    return handler(**handler_dependencies)


def inject(handler: type[_T], **dependencies) -> _T:
    dependencies.setdefault("order_repository", OrderRepository())
    handlers_mapping = {
        OrdersUseCase: __inject_dependencies(OrdersUseCase, dependencies),
    }
    return handlers_mapping[handler]  # type: ignore
