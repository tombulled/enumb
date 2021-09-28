from . import bases
from . import generators

class Index(bases.IntEnum):
    _generate_next_value_ = generators.generate_count(lambda count: count)

class Integer(bases.IntEnum):
    _generate_next_value_ = generators.generate_count(lambda count: count + 1)
