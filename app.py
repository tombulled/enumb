import enum
import typing


def enumeration(cls: type, /) -> enum.Enum:
    classdict: enum._EnumDict = enum._EnumDict()

    classdict.update(cls.__dict__)

    bases: typing.Tuple[type] = (*cls.mro()[1:-1], enum.Enum)

    classdict["_generate_next_value_"] = enum.Enum._generate_next_value_

    annotations: typing.Dict[str, type] = typing.get_type_hints(cls)

    member: str
    for member in annotations:
        if member not in classdict:
            classdict[member]: enum.auto = enum.auto()

    return enum.EnumMeta.__new__(enum.EnumMeta, cls.__name__, bases, classdict)


@enumeration
class Foo(str):
    BAR: str
