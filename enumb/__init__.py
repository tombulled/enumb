import humps
import slugify

import enum

class NoValue(AutoName):
    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}.{self.name}>'

class StrEnum(str, enum.Enum): pass

class AutoName(StrEnum):
    _generate_next_value_ = lambda name, *_: name

class AutoNameLower(StrEnum):
    _generate_next_value_ = lambda name, *_: name.lower()

class AutoNameUpper(StrEnum):
    _generate_next_value_ = lambda name, *_: name.upper()

class AutoNameTitle(StrEnum):
    _generate_next_value_ = lambda name, *_: name.title()

class AutoNamePascal(StrEnum):
    _generate_next_value_ = lambda name, *_: humps.pascalize(name.lower())

class AutoNameCamel(StrEnum):
    _generate_next_value_ = lambda name, *_: humps.camelize(name.lower())

class AutoNameSlug(StrEnum):
    _generate_next_value_ = lambda name, *_: slugify.slugify(name)

class AutoNameSlugUpper(StrEnum):
    _generate_next_value_ = lambda name, *_: slugify.slugify(name).upper()

class AutoNameSlugTitle(StrEnum):
    _generate_next_value_ = lambda name, *_: slugify.slugify(name).title()
