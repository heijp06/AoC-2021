from __future__ import annotations
from functools import total_ordering

import burrow as b
from routes import Route


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
        row, column = self.position
        if column != self.destination:
            return False
        for r in range(burrow.height - 2, row, -1):
            amphipod = burrow[r, column]
            if not amphipod or amphipod.kind != self.kind:
                return False
        return True

    def move_hallway(self, burrow: b.Burrow) -> list[tuple[int, b.Burrow]]:
        if self.final(burrow):
            return []
        row, column = self.position
        if row == 1:
            return []
        for r in range(2, row):
            if burrow[2, r]:
                return []
        burrows = []
        left = [c for c in [8, 6, 4, 2, 1] if c < column]
        right = [c for c in [4, 6, 8, 10, 11] if c > column]
        for c in left:
            route = burrow.get_route(self.position, (1, c))
            if not burrow.can_travel(route.positions):
                break
            burrows.append(self.create_burrow(burrow, route))
        for c in right:
            route = burrow.get_route(self.position, (1, c))
            if not burrow.can_travel(route.positions):
                break
            burrows.append(self.create_burrow(burrow, route))
        return burrows

    def move_home(self, burrow: b.Burrow) -> tuple[int, b.Burrow] | None:
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
        if not burrow.can_travel(route_home.positions):
            return None
        return self.create_burrow(burrow, route_home)

    def create_burrow(self, burrow: b.Burrow, route: Route) -> tuple[int, b.Burrow]:
        extra_cost = route.length * self.energy
        new_amphipod = Amphipod(route.positions[-1], self.kind)
        others = [
            amphipod for amphipod in burrow.amphipods if amphipod != self
        ]
        return extra_cost, b.Burrow(others + [new_amphipod], burrow.height, burrow.routes)

    def min_cost_to_column(self, burrow: b.Burrow) -> int:
        if self.final(burrow):
            return 0
        row, column = self.position
        distance = row + 1 if column == self.destination else row - \
            1 + abs(column - self.destination)
        return distance * self.energy
