from __future__ import annotations
from typing import FrozenSet

import amphipod as a
from routes import Position, Route, Routes


def parse(rows: list[str]) -> Burrow:
    amphipods = [
        a.Amphipod((row, column), rows[row][column])
        for row in range(len(rows))
        for column in range(len(rows[row]))
        if rows[row][column] in "ABCD"
    ]

    height = len(rows)
    return Burrow(amphipods, height, Routes(height))


class Burrow:
    def __init__(self, amphipods: list[a.Amphipod], height: int, routes: Routes) -> None:
        self.amphipods = frozenset(amphipods)
        self.height = height
        self._amphipods_by_position = {
            amphipod.position: amphipod for amphipod in self.amphipods
        }
        self.routes = routes

    def __key(self) -> FrozenSet[a.Amphipod]:
        return self.amphipods

    def __hash__(self) -> int:
        return hash(self.__key())

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Burrow) and self.__key() == other.__key()

    def __repr__(self) -> str:
        return repr(self.__key())

    def __getitem__(self, position: tuple[int, int]) -> a.Amphipod | None:
        return self._amphipods_by_position.get(position)

    def get_route(self, start_point: Position, end_point: Position) -> Route:
        return self.routes[start_point, end_point]

    def final(self) -> bool:
        return all(amphipod.final(self) for amphipod in self.amphipods)

    def can_travel(self, route: list[Position]) -> bool:
        return all(position not in self._amphipods_by_position for position in route)
