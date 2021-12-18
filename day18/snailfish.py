from __future__ import annotations
from abc import ABC, abstractmethod
import re


class Parser():
    def __init__(self, row: str) -> None:
        self.row = row
        self.index = 0

    def parse(self) -> Snailfish:
        match self.match(r"\[|\d+"):
            case "[":
                self.index -= 1
                return self.parse_pair()
            case number:
                return ValueSnailfish(int(number))

    def parse_pair(self) -> PairSnailfish:
        self.index += 1
        left = self.parse()
        self.index += 1
        right = self.parse()
        self.index += 1
        return PairSnailfish(left, right)

    def match(self, pattern: str) -> str:
        result = re.match(pattern, self.row[self.index:])[0]
        if not result:
            raise ValueError(
                f"Cannot match '{pattern}' at index {self.index}.")
        self.index += len(result)
        return result


class Snailfish(ABC):
    @abstractmethod
    def magnitude(self) -> int:
        pass


class ValueSnailfish(Snailfish):
    def __init__(self, number: int) -> None:
        super().__init__()
        self.number = number

    def __repr__(self) -> str:
        return str(self.number)

    def magnitude(self) -> int:
        return self.number


class PairSnailfish(Snailfish):
    def __init__(self, left: Snailfish, right: Snailfish) -> None:
        super().__init__()
        self.left = left
        self.right = right
    
    def __repr__(self) -> str:
        return f'[{self.left},{self.right}]'
    
    def magnitude(self) -> int:
        return 3 * self.left.magnitude() + 2 * self.right.magnitude()
