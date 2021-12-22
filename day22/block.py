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
            block_xyz
            for block_x in self.split_x(other.side_x)
            for block_xy in block_x.split_y(other.side_y)
            for block_xyz in block_xy.split_z(other.side_z)
            if block_xyz not in other
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

    def split_x(self, other_side_x: int) -> list[Block]:
        def block(start, end):
            return Block((start, end), self.side_y, self.side_z)

        x0, x1 = self.side_x
        other_x0, other_x1 = other_side_x

        if x0 > other_x1 or x1 < other_x0 or (x0 >= other_x0 and x1 <= other_x1):
            return [self]
        if other_x0 <= x0:
            return [block(x0, other_x1), block(other_x1 + 1, x1)]
        if other_x1 >= x1:
            return [block(x0, other_x0 - 1), block(other_x0, x1)]
        return [
            block(x0, other_x0 - 1),
            block(other_x0, other_x1),
            block(other_x1 + 1, x1)
        ]

    def split_y(self, other_side_y: int) -> list[Block]:
        def block(start, end):
            return Block(self.side_x, (start, end), self.side_z)

        y0, y1 = self.side_y
        other_y0, other_y1 = other_side_y

        if y0 > other_y1 or y1 < other_y0 or (y0 >= other_y0 and y1 <= other_y1):
            return [self]
        if other_y0 <= y0:
            return [block(y0, other_y1), block(other_y1 + 1, y1)]
        if other_y1 >= y1:
            return [block(y0, other_y0 - 1), block(other_y0, y1)]
        return [
            block(y0, other_y0 - 1),
            block(other_y0, other_y1),
            block(other_y1 + 1, y1)
        ]

    def split_z(self, other_side_z: int) -> list[Block]:
        def block(start, end):
            return Block(self.side_x, self.side_y, (start, end))

        z0, z1 = self.side_z
        other_z0, other_z1 = other_side_z

        if z0 > other_z1 or z1 < other_z0 or (z0 >= other_z0 and z1 <= other_z1):
            return [self]
        if other_z0 <= z0:
            return [block(z0, other_z1), block(other_z1 + 1, z1)]
        if other_z1 >= z1:
            return [block(z0, other_z0 - 1), block(other_z0, z1)]
        return [
            block(z0, other_z0 - 1),
            block(other_z0, other_z1),
            block(other_z1 + 1, z1)
        ]
