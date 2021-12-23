from __future__ import annotations
from typing import Collection

import burrow as b


def get_step(start: int, end: int) -> int:
    return 1 if start < end else -1


class Amphipod:
    kinds = {
        "A": (3, 1),
        "B": (5, 10),
        "C": (7, 100),
        "D": (9, 1000),
    }

    def __init__(self, position: tuple[int, int], kind: str) -> None:
        self.position = position
        self.kind = kind
        self.destination, self.energy = Amphipod.kinds[kind]

    def __key(self) -> tuple[tuple[int, int], str]:
        return self.position, self.kind

    def __hash__(self) -> int:
        return hash(self.__key())

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Amphipod) and self.__key() == other.__key()

    def __repr__(self) -> str:
        return repr(self.__key())

    def final(self, burrow: b.Burrow) -> bool:
        if self.position == (3, self.destination):
            return True
        if self.position != (2, self.destination):
            return False
        amphipod = burrow[3, self.destination]
        return amphipod and amphipod.kind == self.kind

    def move(self, burrow: b.Burrow) -> list[b.Burrow]:
        if self.final(burrow) or self.position[0] == 1:
            return []
        burrows = []
        for column in [1, 2, 4, 6, 8, 10, 11]:
            route = self.get_route((1, column))
            if self.can_reach(burrow, route):
                burrows.append(self.create_burrow(burrow, route))
        return burrows

    def move_home(self, burrow: b.Burrow) -> b.Burrow | None:
        if self.final(burrow):
            return None
        home = (3, self.destination)
        other = burrow[home]
        if other:
            if other.kind != self.kind:
                return None
            else:
                home = (2, self.destination)
        route_home = self.get_route(home)
        if not self.can_reach(burrow, route_home):
            return None
        return self.create_burrow(burrow, route_home)

    def create_burrow(self, burrow: b.Burrow, route: list[tuple[int, int]]) -> b.Burrow:
        new_cost = burrow.cost + len(route) * self.energy
        new_amphipod = Amphipod(route[-1], self.kind)
        others = [
            amphipod for amphipod in burrow.amphipods if amphipod != self
        ]
        return b.Burrow(others + [new_amphipod], new_cost)

    def get_route(self, destination: tuple[int, int]) -> list[tuple[int, int]]:
        row_start, column_start = self.position
        row_end, column_end = destination
        step = get_step(column_start, column_end)

        up = [(row, column_start) for row in range(row_start - 1, 0, -1)]
        sideways = [(1, column) for column in range(
            column_start + step, column_end + step, step)]
        down = [(row, column_end) for row in range(2, row_end + 1)]

        return up + sideways + down

    def can_reach(self, burrow: b.Burrow, route: list[tuple[int, int]]) -> bool:
        return not any(burrow[position] for position in route)
