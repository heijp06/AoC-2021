def part1(rows: list[str]) -> int:
    return go(rows, 1)


def part2(rows):
    return go(rows, 2)


def go(rows: list[str], number: int) -> int:
    coordinates = set()
    folds = []
    reading_coordinates = True
    for row in rows:
        if not row:
            reading_coordinates = False
        elif reading_coordinates:
            x, y = row.split(",")
            coordinates.add((int(x), int(y)))
        else:
            folds.append(row.split()[2])
    for fold in folds:
        match fold.split("="):
            case ["y", value]:
                coordinates = horizontal_fold(coordinates, int(value))
            case ["x", value]:
                coordinates = vertical_fold(coordinates, int(value))
        if number == 1:
            break
    if number == 2:
        max_x = max(x for x, _ in coordinates) + 1
        max_y = max(y for _, y in coordinates) + 1
        paper = [
            ["." for _ in range(max_x)]
            for _ in range(max_y)
        ]
        for x, y in coordinates:
            paper[y][x] = "#"
        for row in paper:
            print("".join(row))
    return len(coordinates)


def horizontal_fold(coordinates: set[tuple[int, int]], fold_y: int) -> set[tuple[int, int]]:
    new_coordinates = set()
    for x, y in coordinates:
        if y < fold_y:
            new_coordinates.add((x, y))
        elif y > fold_y:
            new_coordinates.add((x, fold_y - (y - fold_y)))
    return new_coordinates


def vertical_fold(coordinates: set[tuple[int, int]], fold_x: int) -> set[tuple[int, int]]:
    new_coordinates = set()
    for x, y in coordinates:
        if x < fold_x:
            new_coordinates.add((x, y))
        elif x > fold_x:
            new_coordinates.add((fold_x - (x - fold_x), y))
    return new_coordinates
