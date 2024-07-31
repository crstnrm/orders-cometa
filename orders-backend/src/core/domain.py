from dataclasses import fields
from typing import Any, TypeVar, Optional

_T = TypeVar("_T", bound="Base")


class Base:
    @classmethod
    def parse(cls: type[_T], __value: dict[str, Any]) -> _T:
        """Recursively creates an instance of `cls` from a dictionary."""

        field_types = {field.name: field.type for field in fields(cls)}  # type: ignore

        init_kwargs = {}

        for field_name, field_type in field_types.items():
            if field_name in __value:
                value = __value[field_name]

                if hasattr(field_type, "__origin__") and issubclass(
                    field_type.__origin__, list
                ):
                    # Handle list of nested dataclasses.
                    nested_cls = field_type.__args__[0]
                    init_kwargs[field_name] = [nested_cls.parse(item) for item in value]
                elif hasattr(field_type, "__args__") and hasattr(
                    nested_cls := field_type.__args__[0], "__dataclass_fields__"
                ):
                    # Handle Optional types
                    init_kwargs[field_name] = (
                        nested_cls.parse(value) if value is not None else None
                    )
                elif hasattr(field_type, "__dataclass_fields__"):
                    # Handle nested dataclass.
                    init_kwargs[field_name] = field_type.parse(value)
                else:
                    init_kwargs[field_name] = value

        return cls(**init_kwargs)
