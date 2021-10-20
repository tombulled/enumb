import dataclasses
import typing

import export # TODO: Add as sibling dependency

@export
@dataclasses.dataclass(frozen = True)
class Arguments:
    name:        str
    start:       int
    count:       int
    last_values: typing.List[str]
