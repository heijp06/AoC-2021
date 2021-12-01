def part1(rows):
    return sum(a < b for a, b in zip(rows, rows[1:]))


def part2(rows):
    return sum(a < b for a, b in zip(rows, rows[3:]))
