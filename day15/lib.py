import copy


def part1(rows: list[str]) -> int:
    data = get_data(rows, 1)
    return go(data)


def part2(rows: list[str]) -> int:
    data = get_data(rows, 5)
    return go(data)


def go(data: list[list[int]]) -> int:
    risk = max_bottom_right(data)
    path_finders = [((0, 0), 0, set())]
    size = len(data)
    risks = [
        [risk for _ in range(size)]
        for _ in range(size)
    ]
    counter = 0
    while path_finders:
        print(counter, len(path_finders), risk)
        counter += 1
        new_path_finders = {}
        for (x0, y0), risk0, seen in path_finders:
            for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dx, dy = direction
                x1, y1 = x0 + dx, y0 + dy
                if (x1, y1) in seen or x1 < 0 or y1 < 0 or x1 >= size or y1 >= size:
                    continue
                new_risk = risk0 + data[y1][x1]
                line = risks[y1]
                if new_risk >= line[x1]:
                    continue
                if new_risk + size - 1 - x1 + size - 1 - y1 >= risk:
                    continue
                if x1 == size - 1 and y1 == size - 1:
                    risk = min(risk, new_risk)
                    continue
                line[x1] = new_risk
                new_seen = seen.copy()
                new_seen.add((x0, y0))
                new_path_finders[(x1, y1)] = (((x1, y1), new_risk, new_seen))
        path_finders = list(new_path_finders.values())
    return risk


def get_data(rows: list[str], repeat: int) -> list[list[int]]:
    top_left = [
        [int(level) for level in row]
        for row in rows
    ]
    size = len(top_left)
    data = []
    for row in range(repeat * size):
        r, y = divmod(row, size)
        line = []
        for column in range(repeat * size):
            c, x = divmod(column, size)
            value = top_left[y][x] + r + c
            if value > 9:
                value -= 9
            line.append(value)
        data.append(line)
    return data


def max_bottom_right(grid: list[list[int]]) -> int:
    data = copy.deepcopy(grid)
    size = len(data)
    for diagonal in range(1, 2 * size):
        for x in range(size):
            y = diagonal - x
            if y >= 0 and y < size:
                if y == 0:
                    data[y][x] += data[y][x - 1]
                elif x == 0:
                    data[y][x] += data[y - 1][x]
                else:
                    data[y][x] += min(data[y - 1][x], data[y][x - 1])
    return data[size - 1][size - 1] - data[0][0]
