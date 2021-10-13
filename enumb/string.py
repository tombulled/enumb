# TODO: Add as sibling dependency
import case

from . import bases
from . import generators
from . import utils

@generators.name(utils.identity)
class Name(bases.StrEnum): ...

@generators.name(case.lower)
class Lower(bases.StrEnum): ...

@generators.name(case.upper)
class Upper(bases.StrEnum): ...

@generators.name(case.title)
class Title(bases.StrEnum): ...

@generators.name(case.sentence)
class Sentence(bases.StrEnum): ...

@generators.name(case.snake)
class Snake(bases.StrEnum): ...

@generators.name(case.helter)
class Helter(bases.StrEnum): ...

@generators.name(case.macro)
class Macro(bases.StrEnum): ...

@generators.name(case.flat)
class Flat(bases.StrEnum): ...

@generators.name(case.flush)
class Flush(bases.StrEnum): ...

@generators.name(case.camel)
class Camel(bases.StrEnum): ...

@generators.name(case.pascal)
class Pascal(bases.StrEnum): ...

@generators.name(case.kebab)
class Kebab(bases.StrEnum): ...

@generators.name(case.train)
class Train(bases.StrEnum): ...

@generators.name(case.cobol)
class Cobol(bases.StrEnum): ...

@generators.name(case.dot)
class Dot(bases.StrEnum): ...

@generators.name(case.path)
class Path(bases.StrEnum): ...
