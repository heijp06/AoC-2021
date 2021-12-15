from __future__ import annotations
import copy


class PathFinder:
    def __init__(self, grid: list[list[int]]) -> None:
        self.grid = grid
        self.grid_size = len(grid)
        self.position = (0, 0)
        self.risk = 0
        self.seen: frozenset[tuple[int, int]] = frozenset()
    
    def __repr__(self) -> str:
        return f"{self.position}: {self.risk}"

    def minimum_risk(self) -> int:
        return self.risk + self.manhattan_distance_to_end()

    def manhattan_distance_to_end(self) -> int:
        x, y = self.position
        return self.grid_size - 1 - x + self.grid_size - 1 - y

    def move(self, direction: tuple[int, int]) -> PathFinder:
        # self.seen.add(self.position)
        self.seen = self.seen.union(frozenset([self.position]))
        x, y = self.position
        dx, dy = direction
        path_finder = PathFinder(self.grid)
        path_finder.position = (x + dx, y + dy)
        path_finder.risk = self.risk
        path_finder.seen = self.seen.copy()
        if path_finder.valid():
            path_finder.risk += self.grid[y + dy][x + dx]
        return path_finder

    def valid(self) -> bool:
        return self.on_grid() and self.position not in self.seen

    def on_grid(self) -> bool:
        x, y = self.position
        return x >= 0 and y >= 0 and x < self.grid_size and y < self.grid_size

    def at_end(self) -> bool:
        x, y = self.position
        return x == self.grid_size - 1 and y == self.grid_size - 1
