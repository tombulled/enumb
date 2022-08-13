import functools
from typing import Any, Callable, List

from . import models
from . import types


def generate_next_value(
    func: Callable[[models.Arguments], Any]
) -> types.EnumValueGenerator:
    @functools.wraps(func)
    def wrapper(
        name: str, start: int, count: int, last_values: List[Any]
    ) -> Any:
        return func(
            models.Arguments(
                name=name,
                start=start,
                count=count,
                last_values=last_values,
            ),
        )

    return wrapper


@generate_next_value
def name(arguments: models.Arguments) -> str:
    return arguments.name


@generate_next_value
def count(arguments: models.Arguments) -> int:
    return arguments.count
