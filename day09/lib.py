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
    basins = []
    for y in range(len(rows)):
        for x in range(len(rows[0])):
            if get_val(rows, y, x) >= 9 or any((x, y) in basin for basin in basins):
                continue
            n = set()
            basins.append(n)
            new_basin(n, rows, x, y)
    lens = [len(basin) for basin in basins]
    lens.sort(reverse = True)
    return lens[0] * lens[1] * lens[2]

def new_basin(basin, rows, x, y):
    if (x, y) in basin:
        return
    if x < 0 or x >= len(rows[0]) or y < 0 or y >= len(rows) or int(rows[y][x]) > 8:
        return
    basin.add((x, y))
    new_basin(basin, rows, x + 1, y)
    new_basin(basin, rows, x - 1, y)
    new_basin(basin, rows, x, y + 1)
    new_basin(basin, rows, x, y - 1)
