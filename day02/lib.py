def part1(rows):
    return go(rows, 1)


def part2(rows):
    return go(rows, 2)


def go(rows, part):
    position = 0
    depth = 0
    aim = 0
    for row in rows:
        command, arg = row.split()
        value = int(arg)
        if command == "forward":
            position += value
            depth += aim * value
        else:
            aim += value if command == "down" else -value
    return aim * position if part == 1 else depth * position
