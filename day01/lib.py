def part1(rows):
    return scan(rows, 1)


def part2(rows):
    return scan(rows, 3)


def scan(rows, size):
    return sum(a < b for a, b in zip(rows, rows[size:]))