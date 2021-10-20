import typing
import functools

import export # TODO: Add as sibling dependency

from . import models
from . import types

@export
def generate_next_value(func: typing.Callable[[models.Arguments], typing.Any]) -> types.EnumValueGenerator:
    @functools.wraps(func) # Note: Will this add the wrong function signature. Just update __name__ ?
    def wrapper(name: str, start: int, count: int, last_values: typing.List[typing.Any]):
        return func \
        (
            models.Arguments \
            (
                name        = name,
                start       = start,
                count       = count,
                last_values = last_values,
            ),
        )

    return wrapper

# def generate(func):
#     def wrapper(cls):
#         @functools.wraps(cls, updated = ())
#         class Wrapped(cls):
#             _generate_next_value_: types.EnumValueGenerator = func
#
#         return Wrapped
#
#     return wrapper

# @export
# def generate_name(func: typing.Callable[[str], typing.Any]):
#     return generate_next_value(lambda args: func(args.name))
#
# @export
# def generate_count(func: typing.Callable[[int], typing.Any]):
#     return generate_next_value(lambda args: func(args.count))

@export
@generate_next_value
def name(arguments: models.Arguments) -> str:
    return arguments.name

@export
@generate_next_value
def count(arguments: models.Arguments) -> int:
    return arguments.count
