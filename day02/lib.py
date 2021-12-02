def part1(rows):
    return go(rows, 1)


def part2(rows):
    return go(rows, 2)


def go(rows, part):
    position = 0
    depth = 0
    aim = 0
    for row in rows:
        match row.split():
            case "forward", arg:
                value = int(arg)
                position += value
                depth += aim * value
            case "down", arg:
                aim += int(arg)
            case "up", arg:
                aim -= int(arg)
    return aim * position if part == 1 else depth * position
