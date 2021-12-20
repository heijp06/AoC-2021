def part1(data: list[str]) -> int:
    key = data[0]
    grid = get_grid(data[2:])
    dump(grid)
    for _ in range(2):
        new_grid = set()
        active_region = get_active_region(grid)
        for (x, y) in active_region:
            index = get_index(grid, x, y)
            if key[index] == '#':
                new_grid.add((x, y))
        grid = new_grid
        dump(grid)
    return len(grid)


def part2(data: list[str]) -> int:
    pass


def dump(grid: set[tuple[int, int]]) -> None:
    min_x = min(x for x, _ in grid)
    min_y = min(y for _, y in grid)
    max_x = max(x for x, _ in grid)
    max_y = max(y for _, y in grid)
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            print('#' if (x, y) in grid else '.', end='')
        print()
    print()


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


def get_index(grid: set[tuple[int, int]], x: int, y: int) -> int:
    index = 0
    bit = 256
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if (x + dx, y + dy) in grid:
                index += bit
            bit //= 2
    return index
