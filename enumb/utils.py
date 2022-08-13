from typing import Any, Callable


def compose(*functions: Callable) -> Callable:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        response: Any = None

        index: int
        function: Callable
        for index, function in enumerate(functions):
            response = function(*args, **kwargs) if not index else function(response)

        return response

    return wrapper
