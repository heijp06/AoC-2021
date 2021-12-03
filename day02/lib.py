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
        match command, int(arg):
            case "forward", value:
                position += value
                depth += aim * value
            case "down", value:
                aim += value
            case "up", value:
                aim -= value
    return aim * position if part == 1 else depth * position
