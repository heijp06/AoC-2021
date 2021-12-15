from __future__ import annotations


class PathFinder:
    def __init__(self, grid: list[list[int]]) -> None:
        self.grid = grid
        self.grid_size = len(grid)
        self.position = (0, 0)
        self.risk = 0
        self.seen: set[tuple[int, int]] = set()
    
    def __repr__(self) -> str:
        return f"{self.position}: {self.risk}"

    def minimum_risk(self) -> int:
        return self.risk + self.manhattan_distance_to_end()

    def manhattan_distance_to_end(self) -> int:
        x, y = self.position
        return self.grid_size - 1 - x + self.grid_size - 1 - y

    def move(self, x: int, y: int, new_risk: int) -> PathFinder:
        self.seen.add(self.position)
        path_finder = PathFinder(self.grid)
        path_finder.position = x, y
        path_finder.risk = new_risk
        path_finder.seen = self.seen.copy()
        return path_finder

    def at_end(self) -> bool:
        x, y = self.position
        return x == self.grid_size - 1 and y == self.grid_size - 1
