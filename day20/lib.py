def part1(data: list[str]) -> int:
    return go(data, 2)


def part2(data: list[str]) -> int:
    return go(data, 50)


def go(data: list[str], steps: int) -> int:
    key = data[0]
    inverting = False
    if key[0] == '#':
        if key[-1] == '#':
            raise NotImplementedError()
        inverting = True
    grid = get_grid(data[2:])
    active_region = set()
    for step in range(steps):
        new_grid = set()
        old_active_region = active_region
        active_region = get_active_region(get_active_region(grid))
        for (x, y) in active_region:
            index = get_index(
                grid, x, y, inverting and step % 2, old_active_region)
            if key[index] == '#':
                new_grid.add((x, y))
        grid = new_grid
    return len(grid)


def get_grid(rows: list[str]) -> set[tuple[int, int]]:
    grid = set()
    for y in range(len(rows)):
        for x in range(len(rows[0])):
            if rows[y][x] == '#':
                grid.add((x, y))
    return grid


def get_active_region(grid: set[tuple[int, int]]) -> set[tuple[int, int]]:
    return {
        (x + dx, y + dy)
        for (x, y) in grid
        for dx in [-1, 0, 1]
        for dy in [-1, 0, 1]
    }


def get_index(grid: set[tuple[int, int]], x: int, y: int, inverting: bool, old_active_region: set[tuple[int, int]]) -> int:
    index = 511 if inverting else 0
    bit = 256
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            pos = (x + dx, y + dy)
            if inverting:
                if pos in old_active_region and pos not in grid:
                    index -= bit
            elif pos in grid:
                index += bit
            bit //= 2
    return index
