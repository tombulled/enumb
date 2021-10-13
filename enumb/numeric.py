from . import bases
from . import generators
from . import utils

@generators.count(lambda count: count - 1)
class Index(bases.IntEnum): ...

@generators.count(utils.identity)
class Integer(bases.IntEnum): ...
