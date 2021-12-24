from abc import ABC, abstractmethod


class Expression(ABC):
    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def __eq__(self, __o: object) -> bool:
        pass


class ValueExpression(Expression):
    def __init__(self, value: int) -> None:
        super().__init__()
        self.value = value

    def __repr__(self) -> str:
        return str(self.value)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, ValueExpression) and self.value == other.value


class InputExpression(Expression):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name

    def __repr__(self) -> str:
        return self.name

    def __eq__(self, other: object) -> bool:
        return isinstance(other, InputExpression) and self.name == other.name


class BinaryExpression(Expression):
    def __init__(self, symbol: str, left: Expression, right: Expression) -> None:
        super().__init__()
        self.symbol = symbol
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"({self.left} {self.symbol} {self.right})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BinaryExpression):
            return False
        return self.left == other.left and self.right == other.right
