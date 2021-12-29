Position = tuple[int, int]


def get_step(start: int, end: int) -> int:
    return 1 if start < end else -1


class Routes:
    def __init__(self) -> None:
        self._routes = {}

    def get_route(self, start_point: Position, end_point: Position) -> list[Position]:
        if not (route := self._routes.get((start_point, end_point))):
            route = self._build_route(start_point, end_point)
            self._routes[start_point, end_point] = route
        return route

    def _build_route(self, start_point: Position, end_point: Position) -> list[Position]:
        row_start, column_start = start_point
        row_end, column_end = end_point
        step = get_step(column_start, column_end)

        up = [(row, column_start) for row in range(row_start - 1, 0, -1)]
        sideways = [(1, column) for column in range(
            column_start + step, column_end + step, step)]
        down = [(row, column_end) for row in range(2, row_end + 1)]

        return up + sideways + down
