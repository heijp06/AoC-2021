def part1(rows: list[str]) -> int:
    coordinates = []
    folds = []
    reading_paper = True
    for row in rows:
        if not row:
            reading_paper = False
        elif reading_paper:
            x, y = row.split(",")
            coordinates.append((int(x), int(y)))
        else:
            folds.append(row.split()[2])
    max_x = max(x for x, _ in coordinates)
    max_y = max(y for _, y in coordinates)
    paper = [
        list("." * (max_x + 1))
        for _ in range(max_y + 1)
    ]
    for (x, y) in coordinates:
        paper[y][x] = "#"
    for fold in folds[:1]:
        match fold.split("="):
            case ["y", value]:
                paper = horizontal_fold(paper, int(value))
            case ["x", value]:
                paper = vertical_fold(paper, int(value))
    total = 0
    for row in paper:
        for char in row:
            total += char == "#"
    return total
    
def horizontal_fold(paper, line):
    top = paper[:line]
    bottom = paper[line + 1:]
    print(len(top) == len(bottom))
    new_rows = []
    for line in range(len(top)):
        top_line = top[line]
        bottom_line = bottom[len(bottom) - line - 1]
        new_row = [
            "." if c1 == "." and c2 == "." else "#"
            for c1, c2 in zip(top_line, bottom_line)
        ]
        new_rows.append(new_row)
    return new_rows

def vertical_fold(paper, column):
    paper = list(zip(*paper))
    return horizontal_fold(paper, column)

def part2(rows):
    pass
