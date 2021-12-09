def part1(rows):
    data = get_data(rows)
    total = 0
    for y in range(len(data)):
        for x in range(len(data[0])):
            val = get_val(data, y, x)
            if (
                val < get_val(data, y-1, x) and
                val < get_val(data, y+1, x) and
                val < get_val(data, y, x-1) and
                val < get_val(data, y, x+1)
            ):
                total += val + 1
    return total


def part2(rows):
    data = get_data(rows)
    basins = []
    for y in range(len(data)):
        for x in range(len(data[0])):
            if get_val(data, y, x) >= 9 or any((x, y) in basin for basin in basins):
                continue
            basin = set()
            basins.append(basin)
            grow_basin(basin, data, x, y)
    lens = [len(basin) for basin in basins]
    lens.sort(reverse=True)
    return lens[0] * lens[1] * lens[2]


def get_data(rows):
    return [
        [int(char) for char in row]
        for row in rows
    ]


def get_val(data, y, x):
    if not in_range(data, x, y):
        return 10
    return data[y][x]


def grow_basin(basin, data, x, y):
    if (x, y) in basin or not in_range(data, x, y) or data[y][x] > 8:
        return
    basin.add((x, y))
    grow_basin(basin, data, x + 1, y)
    grow_basin(basin, data, x - 1, y)
    grow_basin(basin, data, x, y + 1)
    grow_basin(basin, data, x, y - 1)


def in_range(data, x, y):
    return x >= 0 and y >= 0 and x < len(data[0]) and y < len(data)
