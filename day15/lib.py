def part1(rows: list[str]) -> int:
    data = get_data(rows, 1)
    return go(data)


def part2(rows: list[str]) -> int:
    data = get_data(rows, 5)
    return go(data)


def go(data: list[list[int]]) -> int:
    positions = {(0, 0)}
    size = len(data)
    risk = 2 * size * 9
    risks = [[risk] * size for _ in range(size)]
    risks[0][0] = 0
    while positions:
        new_positions = set()
        for x0, y0 in positions:
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x1, y1 = x0 + dx, y0 + dy
                if x1 < 0 or y1 < 0 or x1 >= size or y1 >= size:
                    continue
                new_risk = risks[y0][x0] + data[y1][x1]
                if new_risk >= risks[y1][x1]:
                    continue
                risks[y1][x1] = new_risk
                if x1 != size - 1 or y1 != size - 1:
                    new_positions.add((x1, y1))
        positions = new_positions
    return risks[size - 1][size - 1]


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
