from __future__ import annotations

import amphipod as a


def parse(rows: list[str]) -> Burrow:
    amphipods = [
        a.Amphipod((row, column), rows[row][column])
        for row in range(len(rows))
        for column in range(len(rows[row]))
        if rows[row][column] in "ABCD"
    ]

    return Burrow(amphipods, 0)


class Burrow:
    def __init__(self, amphipods: list[a.Amphipod], cost: int, height: int = 5) -> None:
        self.amphipods = tuple(sorted(amphipods))
        self.cost = cost
        self.height = height

    def __key(self) -> tuple[tuple[a.Amphipod], int]:
        return self.amphipods, self.cost

    def __hash__(self) -> int:
        return hash(self.__key())

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Burrow) and self.__key() == other.__key()

    def __repr__(self) -> str:
        return repr(self.__key())

    def __getitem__(self, position: tuple[int, int]) -> a.Amphipod | None:
        amphipods = [
            amphipod for amphipod in self.amphipods
            if amphipod.position == position
        ]
        return amphipods and amphipods[0]

    def move(self) -> list[Burrow]:
        for amphipod in self.amphipods:
            burrow = amphipod.move_home(self)
            if burrow:
                return [burrow]

        return [
            burrow
            for amphipod in self.amphipods
            for burrow in amphipod.move(self)
        ]

    def final(self) -> bool:
        return all(amphipod.final(self) for amphipod in self.amphipods)
