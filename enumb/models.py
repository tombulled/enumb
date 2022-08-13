import dataclasses
from typing import List


@dataclasses.dataclass(frozen=True)
class Arguments:
    name: str
    start: int
    count: int
    last_values: List[str]
