from __future__ import annotations
from functools import total_ordering

import burrow as b


@total_ordering
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

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Amphipod):
            return NotImplemented
        return self.__key() < other.__key()

    def __repr__(self) -> str:
        return repr(self.__key())

    def final(self, burrow: b.Burrow) -> bool:
        row = burrow.height - 2
        if self.position == (row, self.destination):
            return True
        while row > 2:
            amphipod = burrow[row, self.destination]
            if not amphipod or amphipod.kind != self.kind:
                return False
            row -= 1
            if self.position == (row, self.destination):
                return True

    def move(self, burrow: b.Burrow) -> list[b.Burrow]:
        if self.final(burrow) or self.position[0] == 1:
            return []
        burrows = []
        for column in [1, 2, 4, 6, 8, 10, 11]:
            route = burrow.get_route(self.position, (1, column))
            if self.can_reach(burrow, route):
                burrows.append(self.create_burrow(burrow, route))
        return burrows

    def move_home(self, burrow: b.Burrow) -> b.Burrow | None:
        if self.final(burrow):
            return None
        row = burrow.height - 2
        home = (row, self.destination)
        while row > 2:
            other = burrow[home]
            if not other:
                break
            if other.kind != self.kind:
                return None
            row -= 1
            home = (row, self.destination)
        route_home = burrow.get_route(self.position, home)
        if not self.can_reach(burrow, route_home):
            return None
        return self.create_burrow(burrow, route_home)

    def create_burrow(self, burrow: b.Burrow, route: list[tuple[int, int]]) -> b.Burrow:
        new_cost = burrow.cost + len(route) * self.energy
        new_amphipod = Amphipod(route[-1], self.kind)
        others = [
            amphipod for amphipod in burrow.amphipods if amphipod != self
        ]
        return b.Burrow(others + [new_amphipod], new_cost, burrow.height, burrow.routes)

    def can_reach(self, burrow: b.Burrow, route: list[tuple[int, int]]) -> bool:
        return not any(burrow[position] for position in route)
