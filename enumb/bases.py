import enum

import export # TODO: Add as sibling dependency

from . import generators
from . import meta

@export
class Enum(enum.Enum, metaclass = meta.EnumMeta): pass

class BaseTypeEnum(Enum):
    def __str__(self) -> str:
        return str(self.value)

@export
class IntEnum(int, BaseTypeEnum):
    _generate_next_value_ = generators.count

@export
class StrEnum(str, BaseTypeEnum):
    _generate_next_value_ = generators.name
