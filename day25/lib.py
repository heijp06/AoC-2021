def part1(rows: tuple[str]) -> None:
    width = len(rows[0])
    height = len(rows)
    right = parse('>', rows)
    down = parse('v', rows)
    stop = False
    step = 0
    while not stop:
        stop = True
        new_right = move(right, down, (1, 0), (width, height))
        if right != new_right:
            stop = False
        right = new_right
        new_down = move(down, right, (0, 1), (width, height))
        if down != new_down:
            stop = False
        down = new_down
        step += 1
    return step


def move(
        these: set[tuple[int, int]], others: set[tuple[int, int]],
        direction: tuple[int, int], size: tuple[int, int]) -> set[tuple[int, int]]:
    dx, dy = direction
    width, height = size
    these_moved = set()
    for (x, y) in these:
        pos = ((x + dx) % width, (y + dy) % height)
        if pos not in these and pos not in others:
            these_moved.add(pos)
        else:
            these_moved.add((x, y))
    return these_moved


def part2(rows: tuple[str]) -> None:
    pass


def parse(cucumber: str, rows: tuple[str]) -> set[tuple[int, int]]:
    return {
        (x, y)
        for x in range(len(rows[0]))
        for y in range(len(rows))
        if rows[y][x] == cucumber
    }
