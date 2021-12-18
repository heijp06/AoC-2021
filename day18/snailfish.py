from __future__ import annotations
from abc import ABC, abstractmethod
import re


def parse(row: str) -> RootSnailfish:
    parser = Parser(row)
    return RootSnailFish(parser.parse())


class Parser():
    def __init__(self, row: str) -> None:
        self.row = row
        self.index = 0

    def parse(self) -> Snailfish:
        match self.match(r"\[|\d+"):
            case "[":
                left = self.parse()
                self.index += 1
                right = self.parse()
                self.index += 1
                return PairSnailfish(left, right)
            case number:
                return ValueSnailfish(int(number))

    def match(self, pattern: str) -> str:
        result = re.match(pattern, self.row[self.index:])[0]
        if not result:
            raise ValueError(
                f"Cannot match '{pattern}' at index {self.index}.")
        self.index += len(result)
        return result


class Snailfish(ABC):
    def __init__(self) -> None:
        super().__init__()
        self._parent = None

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def magnitude(self) -> int:
        pass

    @abstractmethod
    def explode(self, depth=0) -> bool:
        pass

    @abstractmethod
    def split(self) -> bool:
        pass

    @abstractmethod
    def replace(self, child: Snailfish, replacement: Snailfish) -> None:
        pass

    @property
    def parent(self) -> Snailfish:
        return self._parent

    def first_left(self) -> ValueSnailfish:
        current = self
        if not current.parent or isinstance(current.parent, RootSnailFish):
            return None
        while current == current.parent.left:
            current = current.parent
            if not current.parent or isinstance(current.parent, RootSnailFish):
                return None
        current = current.parent.left
        while not isinstance(current, ValueSnailfish):
            current = current.right
        return current

    def first_right(self) -> ValueSnailfish:
        current = self
        if not current.parent or isinstance(current.parent, RootSnailFish):
            return None
        while current == current.parent.right:
            current = current.parent
            if not current.parent or isinstance(current.parent, RootSnailFish):
                return None
        current = current.parent.right
        while not isinstance(current, ValueSnailfish):
            current = current.left
        return current


class ValueSnailfish(Snailfish):
    def __init__(self, number: int) -> None:
        super().__init__()
        self.number = number

    def __repr__(self) -> str:
        return str(self.number)

    def magnitude(self) -> int:
        return self.number

    def explode(self, _=0) -> bool:
        return False

    def split(self) -> bool:
        if self.number < 10:
            return False
        half, remainder = divmod(self.number, 2)
        replacement = PairSnailfish(ValueSnailfish(
            half), ValueSnailfish(half + remainder))
        self.parent.replace(self, replacement)
        return True

    def replace(self, child: Snailfish, replacement: Snailfish) -> None:
        raise ValueError("Cannot replace child of value.")


class PairSnailfish(Snailfish):
    def __init__(self, left: Snailfish, right: Snailfish) -> None:
        super().__init__()
        self.left = left
        self.right = right
        left._parent = self
        right._parent = self

    def __repr__(self) -> str:
        return f'[{self.left},{self.right}]'

    def magnitude(self) -> int:
        return 3 * self.left.magnitude() + 2 * self.right.magnitude()

    def explode(self, depth=0) -> bool:
        if depth < 4:
            return self.left.explode(depth + 1) or self.right.explode(depth + 1)
        first_left = self.first_left()
        if first_left:
            first_left.number += self.left.number
        first_right = self.first_right()
        if first_right:
            first_right.number += self.right.number
        self.parent.replace(self, ValueSnailfish(0))
        return True

    def split(self):
        return self.left.split() or self.right.split()

    def replace(self, child: Snailfish, replacement: Snailfish) -> None:
        replacement._parent = self
        if child == self.left:
            self.left = replacement
        else:
            self.right = replacement


class RootSnailFish(Snailfish):
    def __init__(self, child: Snailfish) -> None:
        super().__init__()
        self.child = child
        child._parent = self

    def __repr__(self) -> str:
        return repr(self.child)
    
    def __add__(self, other: RootSnailFish) -> RootSnailFish:
        left = self.child
        right = other.child
        result = RootSnailFish(PairSnailfish(left, right))
        result.reduce()
        return result

    def magnitude(self) -> int:
        return self.child.magnitude()

    def explode(self, depth=0) -> bool:
        return self.child.explode()

    def split(self) -> bool:
        return self.child.split()

    def replace(self, child: Snailfish, replacement: Snailfish) -> None:
        replacement._parent = self
        self.child = replacement

    def reduce(self) -> None:
        changed = True
        while changed:
            while self.explode():
                pass
            changed = self.split()
