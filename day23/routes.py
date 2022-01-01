from __future__ import annotations
from itertools import product

Position = tuple[int, int]


def _get_step(start: int, end: int) -> int:
    return 1 if start < end else -1


def _build_route(start_point: Position, end_point: Position) -> Route:
    row_start, column_start = start_point
    row_end, column_end = end_point
    step = _get_step(column_start, column_end)

    up = [(row, column_start) for row in range(row_start - 1, 0, -1)]
    sideways = [(1, column) for column in range(
        column_start + step, column_end + step, step)]
    down = [(row, column_end) for row in range(2, row_end + 1)]

    return Route(up + sideways + down)


class Routes:
    def __init__(self, height: int) -> None:
        rooms = [
            (row, column)
            for row in range(2, height - 1)
            for column in range(3, 10, 2)
        ]
        hallways = [(1, column) for column in (1, 2, 4, 6, 8, 10, 11)]
        positions = rooms + hallways
        self._routes = {
            (start_point, end_point): _build_route(start_point, end_point)
            for start_point, end_point in product(positions, repeat=2)
        }

    def __getitem__(self, end_points: tuple[Position, Position]) -> Route:
        return self._routes[end_points]

class Route:
    def __init__(self, positions: list[Position]) -> None:
        self.length = len(positions)
        self.positions = [
            (row, column)
            for row, column
            in positions
            if row != 1 or column not in (3, 5, 7, 9)
        ]