import cassidy

from . import bases
from . import generators
from . import utils


class Name(bases.StrEnum):
    pass


class Index(bases.IntEnum):
    pass


class Integer(bases.IntEnum):
    _generate_next_value_ = utils.compose(generators.count, lambda count: count + 1)


class NoValue(bases.Enum):
    def __repr__(self) -> str:
        return f"<{type(self).__name__}.{self.name}>"

    @property
    def value(self) -> None:
        raise AttributeError(f"{type(self).__name__!r} object has no attribute 'value'")


class Lower(bases.StrEnum):
    _generate_next_value_ = utils.compose(generators.name, cassidy.lower)


class Upper(bases.StrEnum):
    _generate_next_value_ = utils.compose(generators.name, cassidy.upper)


class Title(bases.StrEnum):
    _generate_next_value_ = utils.compose(generators.name, cassidy.title)


class Sentence(bases.StrEnum):
    _generate_next_value_ = utils.compose(generators.name, cassidy.sentence)


class Snake(bases.StrEnum):
    _generate_next_value_ = utils.compose(generators.name, cassidy.snake)


class Helter(bases.StrEnum):
    _generate_next_value_ = utils.compose(generators.name, cassidy.helter)


class Macro(bases.StrEnum):
    _generate_next_value_ = utils.compose(generators.name, cassidy.macro)


class Flat(bases.StrEnum):
    _generate_next_value_ = utils.compose(generators.name, cassidy.flat)


class Flush(bases.StrEnum):
    _generate_next_value_ = utils.compose(generators.name, cassidy.flush)


class Camel(bases.StrEnum):
    _generate_next_value_ = utils.compose(generators.name, cassidy.camel)


class Pascal(bases.StrEnum):
    _generate_next_value_ = utils.compose(generators.name, cassidy.pascal)


class Kebab(bases.StrEnum):
    _generate_next_value_ = utils.compose(generators.name, cassidy.kebab)


class Train(bases.StrEnum):
    _generate_next_value_ = utils.compose(generators.name, cassidy.train)


class Cobol(bases.StrEnum):
    _generate_next_value_ = utils.compose(generators.name, cassidy.cobol)


class Dot(bases.StrEnum):
    _generate_next_value_ = utils.compose(generators.name, cassidy.dot)


class Path(bases.StrEnum):
    _generate_next_value_ = utils.compose(generators.name, cassidy.path)
