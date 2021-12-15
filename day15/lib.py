from path_finder import PathFinder

def part1(rows: list[str]) -> int:
    risk = max_bottom_right(rows)
    data = get_data(rows)
    path_finders = [PathFinder(data)]
    risks = {(0, 0): 0}
    while path_finders:
        print(len(path_finders), risk)
        new_path_finders = []
        seen = set()
        for path_finder in path_finders:
            for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_path_finder = path_finder.move(direction)
                if not new_path_finder.valid() or new_path_finder.minimum_risk() >= risk:
                    continue
                if new_path_finder.at_end():
                    risk = min(risk, new_path_finder.risk)
                    continue
                key = (new_path_finder.position, new_path_finder.seen)
                if (new_path_finder.position in risks and
                    new_path_finder.risk >= risks[new_path_finder.position]):
                    continue
                risks[new_path_finder.position] = new_path_finder.risk
                if key not in seen:
                    seen.add(key)
                    new_path_finders.append(new_path_finder)
        path_finders = new_path_finders
    return risk




# def add_path(data, result, paths, pos, seen, total) -> int:
#     x, y = pos
#     if x >= 0 and y >= 0 and x < len(data) and y < len(data) and pos not in seen:
#         new_seen = seen.copy()
#         new_seen.add(pos)
#         new_total = total + data[y][x]
#         if new_total < result:
#             paths.add((pos, result, new_seen, new_total))
            


def part2(rows):
    pass

def get_data(rows: list[str]) -> list[list[int]]:
    return [
        [int(level) for level in row]
        for row in rows
    ]

def max_bottom_right(rows: list[list[int]]) -> int:
    data = get_data(rows)
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
