import enum

from . import meta

class Enum(enum.Enum, metaclass = meta.EnumMeta): pass

class StrEnum(str, Enum):
    def __str__(self) -> str:
        return super().__str__()

class IntEnum(int, Enum):
    def __str__(self) -> str:
        # NOTE: This applies to all, including `StrEnum`. Turn into mixin class?
        return self.value.__str__()
