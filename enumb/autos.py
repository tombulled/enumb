import addict
import humps
import slugify

import enum
import typing

from . import meta
from . import bases

class AutoEnum(enum.Enum, metaclass = meta.AutoEnumMeta): pass

class AutoStrEnum(AutoEnum, bases.StrEnum): pass
class AutoIntEnum(AutoEnum, bases.IntEnum): pass

class AutoName(AutoStrEnum):
    _generate_next_value_ = lambda name, *_: name

class AutoNameLower(AutoStrEnum):
    _generate_next_value_ = lambda name, *_: name.lower()

class AutoNameUpper(AutoStrEnum):
    _generate_next_value_ = lambda name, *_: name.upper()

class AutoNameTitle(AutoStrEnum):
    _generate_next_value_ = lambda name, *_: name.title()

class AutoNamePascal(AutoStrEnum):
    _generate_next_value_ = lambda name, *_: humps.pascalize(name.lower())

class AutoNameCamel(AutoStrEnum):
    _generate_next_value_ = lambda name, *_: humps.camelize(name.lower())

class AutoNameSlug(AutoStrEnum):
    _generate_next_value_ = lambda name, *_: slugify.slugify(name)

class AutoNameSlugUpper(AutoStrEnum):
    _generate_next_value_ = lambda name, *_: slugify.slugify(name).upper()

class AutoNameSlugTitle(AutoStrEnum):
    _generate_next_value_ = lambda name, *_: slugify.slugify(name).title()

class NoValue(AutoName):
    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}.{self.name}>'
