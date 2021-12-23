from burrow import parse


def part1(rows: tuple[str]) -> int:
    return go(rows)


def part2(rows: tuple[str]) -> int:
    new_rows = list(rows[:3]) + [
        "  #D#C#B#A#",
        "  #D#B#A#C#",
    ] + list(rows[3:])
    return go(new_rows)


def go(rows: list[str]) -> int:
    burrows = {parse(rows)}
    min_cost = None
    while burrows:
        print(len(burrows), min_cost)
        new_burrows = set()
        for burrow in burrows:
            for new_burrow in burrow.move():
                if not min_cost or new_burrow.cost < min_cost:
                    if new_burrow.final():
                        min_cost = new_burrow.cost
                    else:
                        new_burrows.add(new_burrow)
        burrows = new_burrows
    return min_cost
