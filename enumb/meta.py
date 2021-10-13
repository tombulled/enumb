import enum
import types
import typing

from . import classes

# import inspect

# TODO: Drop dependency on `addict`
import addict

class EnumMeta(enum.EnumMeta):
    def __new__ \
            (
                metacls:   type,
                cls:       str,
                bases:     typing.Tuple[type],
                classdict: typing.Dict[str, typing.Any],
            ):
        # signature = inspect.signature(metacls)
        # print(signature)
        # print(signature.__dict__)
        # attrs: types.SimpleNamespace = types.SimpleNamespace(**classdict)
        attrs = addict.Dict(classdict)
        # attrs = classes.AttrDict(classdict)

        # print(attrs)

        namespace: enum._EnumDict = metacls.__prepare__(cls, bases)

        for key, value in classdict.items():
            namespace.__setitem__(key, value)

        values: list = []

        for index, (member, annotation) in enumerate(attrs.__annotations__.items(), start = 1):
            value = attrs.get \
            (
                member,
                # Note: Can't assume that this exists?
                # Do enums have a default version of this (that uses ints)?
                attrs._generate_next_value_(member, 1, index, values),
            )

            if member not in classdict:
                namespace.__setitem__(member, value)

            values.append(value)

        return super().__new__(metacls, cls, bases, namespace)
