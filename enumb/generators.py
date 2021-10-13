import typing
import functools

from . import models
from . import types

def generator(func):
    def wrapper(name: str, start: int, count: int, last_values: typing.List[typing.Any]):
        return func \
        (
            models.Arguments \
            (
                name        = name,
                start       = start,
                count       = count,
                last_values = last_values,
            )
        )

    return wrapper

def generate(func):
    def wrapper(cls):
        @functools.wraps(cls, updated = ())
        class Wrapped(cls):
            _generate_next_value_: types.EnumValueGenerator = generator(func)

        return Wrapped

    return wrapper

def name(func):
    return generate(lambda args: func(args.name))

def count(func):
    return generate(lambda args: func(args.count))
