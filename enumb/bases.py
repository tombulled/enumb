import enum

from . import meta

class Enum(enum.Enum, metaclass = meta.EnumMeta): pass

class BaseTypeEnum(Enum):
    def __str__(self) -> str:
        return str(self.value)

class StrEnum  (str,   BaseTypeEnum): pass
class IntEnum  (int,   BaseTypeEnum): pass
class FloatEnum(float, BaseTypeEnum): pass
class BytesEnum(bytes, BaseTypeEnum): pass
