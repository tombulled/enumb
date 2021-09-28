from . import string

# NOTE: Rename? (NoValue, Null, ...?)
class Empty(string.Name):
    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}.{self.name}>'
