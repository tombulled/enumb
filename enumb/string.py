import case # TODO: Add as dependency

from . import bases
from . import generators

class Name(bases.StrEnum):
    _generate_next_value_ = generators.generate_name(lambda name: name)

class Lower(bases.StrEnum):
    _generate_next_value_ = generators.generate_name(case.lower)

class Upper(bases.StrEnum):
    _generate_next_value_ = generators.generate_name(case.upper)

class Title(bases.StrEnum):
    _generate_next_value_ = generators.generate_name(case.title)

class Sentence(bases.StrEnum):
    _generate_next_value_ = generators.generate_name(case.sentence)

class Snake(bases.StrEnum):
    _generate_next_value_ = generators.generate_name(case.snake)

class Helter(bases.StrEnum):
    _generate_next_value_ = generators.generate_name(case.helter)

class Macro(bases.StrEnum):
    _generate_next_value_ = generators.generate_name(case.macro)

class Flat(bases.StrEnum):
    _generate_next_value_ = generators.generate_name(case.flat)

class Flush(bases.StrEnum):
    _generate_next_value_ = generators.generate_name(case.flush)

class Camel(bases.StrEnum):
    _generate_next_value_ = generators.generate_name(case.camel)

class Pascal(bases.StrEnum):
    _generate_next_value_ = generators.generate_name(case.pascal)

class Kebab(bases.StrEnum):
    _generate_next_value_ = generators.generate_name(case.kebab)

class Train(bases.StrEnum):
    _generate_next_value_ = generators.generate_name(case.train)

class Cobol(bases.StrEnum):
    _generate_next_value_ = generators.generate_name(case.cobol)

class Dot(bases.StrEnum):
    _generate_next_value_ = generators.generate_name(case.dot)

class Path(bases.StrEnum):
    _generate_next_value_ = generators.generate_name(case.path)
