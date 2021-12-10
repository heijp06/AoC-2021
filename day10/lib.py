def part1(rows):
    return sum(score1(row) for row in rows)


def score1(row: str) -> int:
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
    scores = []
    for row in rows:
        if part1(row):
            continue
        result = ""
        char = completion(row)
        while char:
            result += char
            row += char
            char = completion(row)
        score = score2(result)
        if score:
            scores.append(score)
    scores.sort()
    return scores[len(scores) // 2]


def completion(row):
    stack = []
    for char in row:
        if char in "([{<":
            stack.append(char)
            continue
        if not stack:
            return ""
        open = stack.pop()
        if (
            char == ")" and open != "(" or
            char == "]" and open != "[" or
            char == "}" and open != "{" or
            char == ">" and open != "<"
        ):
            return ""
    if stack:
        char = stack.pop()
        match char:
            case "(":
                return ")"
            case "[":
                return "]"
            case "{":
                return "}"
            case "<":
                return ">"
    else:
        return ""


def score2(result):
    total = 0
    for char in result:
        total *= 5
        match char:
            case ")":
                total += 1
            case "]":
                total += 2
            case "}":
                total += 3
            case ">":
                total += 4
    return total
