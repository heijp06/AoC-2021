def part1(rows):
    total = 0
    for y in range(len(rows)):
        for x in range(len(rows[0])):
            val = get_val(rows, y, x)
            if (val < get_val(rows, y-1, x) and val < get_val(rows, y+1, x) and val < get_val(rows, y, x-1) and val < get_val(rows, y, x+1)
            ):
                total += val + 1
    return total


def get_val(rows, y, x):
    if x < 0 or y < 0 or x >= len(rows[0]) or y >= len(rows):
        return 10
    return int(rows[y][x])


def part2(rows):
    pass
