def part1(rows):
    total = 0
    for row in rows:
        total += score(row)
    return total


def score(row: str) -> int:
    stack = []
    for char in row:
        if char in "([{<":
            stack.append(char)
            continue
        if not stack:
            return 0
        open = stack.pop()
        if char == ")" and open != "(":
            return 3
        if char == "]" and open != "[":
            return 57
        if char == "}" and open != "{":
            return 1197
        if char == ">" and open != "<":
            return 25137
    return 0
        


def part2(rows):
    pass
