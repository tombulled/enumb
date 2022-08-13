import enum

from . import generators
from . import meta


class Enum(enum.Enum, metaclass=meta.EnumMeta):
    pass


class BaseTypeEnum(Enum):
    def __str__(self) -> str:
        return str(self.value)


class IntEnum(int, BaseTypeEnum):
    _generate_next_value_ = generators.count


class StrEnum(str, BaseTypeEnum):
    _generate_next_value_ = generators.name
