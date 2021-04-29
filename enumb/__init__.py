import addict
import humps
import slugify

import enum
import typing

class StrEnum(str, enum.Enum):
    def __str__(self) -> str:
        return super().__str__()

class IntEnum(int, enum.Enum):
    def __str__(self) -> str:
        return str(int(self))

class AutoEnumMeta(enum.EnumMeta):
    def __new__(metacls: type, cls: str, bases: typing.Tuple[type], classdict: typing.Dict[str, typing.Any]):
        attrs = addict.Dict(classdict)

        namespace = metacls.__prepare__(cls, bases)

        for key, value in classdict.items():
            namespace[key] = value

        values = []

        for index, (member, annotation) in enumerate(attrs.__annotations__.items()):
            value = attrs.get \
            (
                member,
                attrs._generate_next_value_(member, 1, index, values),
            )

            if member not in classdict:
                namespace[member] = value

            values.append(value)

        return super().__new__(metacls, cls, bases, namespace)

class AutoEnum(enum.Enum, metaclass = AutoEnumMeta): pass

class AutoStrEnum(AutoEnum, StrEnum): pass

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
