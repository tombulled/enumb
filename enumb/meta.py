import enum
import typing

import addict

class AutoEnumMeta(enum.EnumMeta):
    def __new__ \
            (
                metacls:   type,
                cls:       str,
                bases:     typing.Tuple[type],
                classdict: typing.Dict[str, typing.Any],
            ):
        attrs: addict.Dict = addict.Dict(classdict)

        namespace: enum._EnumDict = metacls.__prepare__(cls, bases)

        for key, value in classdict.items():
            namespace.__setitem__(key, value)

        values: list = []

        for index, (member, annotation) in enumerate(attrs.__annotations__.items()):
            value = attrs.get \
            (
                member,
                attrs._generate_next_value_(member, 1, index, values),
            )

            if member not in classdict:
                namespace.__setitem__(member, value)

            values.append(value)

        return super().__new__(metacls, cls, bases, namespace)
