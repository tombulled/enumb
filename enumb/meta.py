import enum
import typing
from typing import Dict, Tuple

class EnumMeta(enum.EnumMeta):
    def __new__(
        metacls: type,
        cls: str,
        bases: Tuple[type],
        classdict: enum._EnumDict,
    ) -> object:
        annotations: Dict[str, type] = typing.get_type_hints(cls)

        member: str
        for member in annotations:
            if member not in classdict:
                classdict[member]: enum.auto = enum.auto()

        return super().__new__(metacls, cls, bases, classdict)
