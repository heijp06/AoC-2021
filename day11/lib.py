import copy


def part1(rows: list[str], steps: int = 100) -> int:
    grid = get_grid(rows)
    show(grid, 0)
    flashes = 0
    for step in range(steps):
        increase(grid)
        show(grid, step + 1)
        new_flashes, grid = ripple(grid)
        show(grid, step + 1)
        while new_flashes:
            flashes += new_flashes
            new_flashes, grid = ripple(grid)
            show(grid, step + 1)
        reset(grid)
        # if step + 1 in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100):
        #     show(grid, step + 1)
    return flashes


def show(grid: list[list[int]], step: int) -> None:
    width, height = size(grid)
    if step:
        print(f"After step {step}:")
    else:
        print("Before any step:")
    for row in range(height):
        for column in range(width):
            val = grid[row][column]
            s = str(val) if val < 10 else chr(ord('A') + val - 10)
            print(s, end="")
        print()
    print()


def get_grid(rows: list[str]) -> list[list[int]]:
    return [
        [int(octopus) for octopus in row]
        for row in rows
    ]


def increase(grid: list[list[int]]) -> int:
    flashes = 0
    width, height = size(grid)
    for row in range(height):
        for column in range(width):
            grid[row][column] += 1
            if grid[row][column] > 9:
                flashes += 1
    return flashes


def ripple(grid: list[list[int]]) -> tuple[int, list[list[int]]]:
    flashes = 0
    width, height = size(grid)
    for row in range(height):
        for column in range(width):
            if grid[row][column] > 9:
                flashes += 1
                grid[row][column] = -1
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        if (dx, dy) != 0 and in_range(grid, row + dy, column + dx) and grid[row + dy][column + dx] > -1:
                            grid[row + dy][column + dx] += 1
    return flashes, grid


def flashing_neighbours(grid: list[list[int]], row: int, column: int) -> int:
    return sum(
        grid[row + dy][column + dx] > 9
        for dx in [-1, 0, 1]
        for dy in [-1, 0, 1]
        if (dx, dy) != (0, 0) and in_range(grid, row + dy, column + dx)
    )


def reset(grid: list[list[int]]) -> None:
    width, height = size(grid)
    for row in range(height):
        for column in range(width):
            grid[row][column] = max(grid[row][column], 0)


def in_range(grid: list[list[int]], row: int, column: int) -> bool:
    width, height = size(grid)
    return row >= 0 and row < height and column >= 0 and column < width


def size(grid: list[list[int]]) -> tuple[int, int]:
    return len(grid[0]), len(grid)


def part2(rows):
    pass
