from typing import Any, Callable, List

EnumValueGenerator = Callable[
    [str, int, int, List[Any]],  # name, start, count, last_values
    Any,
]
