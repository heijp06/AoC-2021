from __future__ import annotations
from itertools import combinations


def merge(blocks: list[Block]) -> list[Block]:
    changed = True
    while changed:
        changed = False
        for index1, index2 in combinations(range(len(blocks)), 2):
            block = blocks[index1].glue(blocks[index2])
            if block:
                blocks.pop(index2)
                blocks.pop(index1)
                blocks.append(block)
                changed = True
                break
    return blocks


def split(start1: int, end1: int, start2: int, end2: int) -> list[tuple[int, int]]:
    if start1 > end2 or end1 < start2 or (start1 >= start2 and end1 <= end2):
        return [(start1, end1)]
    if start2 <= start1:
        return [(start1, end2), (end2 + 1, end1)]
    if end2 >= end1:
        return [(start1, start2 - 1), (start2, end1)]
    return [
        (start1, start2 - 1),
        (start2, end2),
        (end2 + 1, end1)
    ]


class Block:
    def __init__(self, side_x: tuple[int, int], side_y: tuple[int, int], side_z: tuple[int, int]) -> None:
        self.side_x = side_x
        self.x0, self.x1 = side_x
        self.side_y = side_y
        self.y0, self.y1 = side_y
        self.side_z = side_z
        self.z0, self.z1 = side_z

    def __key(self) -> tuple[tuple[int, int], tuple[int, int], tuple[int, int]]:
        return (self.side_x, self.side_y, self.side_z)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Block) and self.__key() == other.__key()

    def __hash__(self) -> int:
        return hash(self.__key())

    def __repr__(self) -> str:
        return f"Block({self.__key()})"

    def __add__(self, other: Block) -> list[Block]:
        return merge(self - other + [other])

    def __sub__(self, other: Block) -> list[Block]:
        return merge([
            block
            for (x0, x1) in split(self.x0, self.x1, other.x0, other.x1)
            for (y0, y1) in split(self.y0, self.y1, other.y0, other.y1)
            for (z0, z1) in split(self.z0, self.z1, other.z0, other.z1)
            if (block := Block((x0, x1), (y0, y1), (z0, z1))) and block not in other
        ])

    def __contains__(self, other: Block) -> bool:
        return (
            self.x0 <= other.x0 and self.x1 >= other.x1 and
            self.y0 <= other.y0 and self.y1 >= other.y1 and
            self.z0 <= other.z0 and self.z1 >= other.z1
        )

    def size(self) -> int:
        return (self.x1 - self.x0 + 1) * (self.y1 - self.y0 + 1) * (self.z1 - self.z0 + 1)

    def glue(self, other: Block) -> Block | None:
        if self.side_y == other.side_y and self.side_z == other.side_z:
            if self.x1 + 1 == other.x0:
                return Block((self.x0, other.x1), self.side_y, self.side_z)
            if other.x1 + 1 == self.x0:
                return Block((other.x0, self.x1), self.side_y, self.side_z)
        if self.side_z == other.side_z and self.side_x == other.side_x:
            if self.y1 + 1 == other.y0:
                return Block(self.side_x, (self.y0, other.y1), self.side_z)
            if other.y1 + 1 == self.y0:
                return Block(self.side_x, (other.y0, self.y1), self.side_z)
        if self.side_x == other.side_x and self.side_y == other.side_y:
            if self.z1 + 1 == other.z0:
                return Block(self.side_x, self.side_y, (self.z0, other.z1))
            if other.z1 + 1 == self.z0:
                return Block(self.side_x, self.side_y, (other.z0, self.z1))
        return None
