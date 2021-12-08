def part1(rows: list[str]):
    total = 0
    for row in rows:
        _, output = row.split(" | ")
        total += sum(
            len(number) in (2, 3, 4, 7)
            for number
            in output.split(" ")
        )
    return total


def part2(rows):
    pass
