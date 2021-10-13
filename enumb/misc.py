from . import string

class NoValue(string.Name):
    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}.{self.name}>'
