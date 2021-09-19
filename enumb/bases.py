import enum

class StrEnum(str, enum.Enum):
    def __str__(self) -> str:
        return super().__str__()

class IntEnum(int, enum.Enum):
    def __str__(self) -> str:
        return self.value.__str__()
