from burrow import Burrow, parse
from sortedcontainers import SortedDict


def part1(rows: tuple[str]) -> int:
    return go(rows)


def part2(rows: tuple[str]) -> int:
    new_rows = list(rows[:3]) + [
        "  #D#C#B#A#",
        "  #D#B#A#C#",
    ] + list(rows[3:])
    return go(new_rows)


def go(rows: list[str]) -> int:
    groups = SortedDict()
    burrows = {parse(rows)}
    min_cost = None
    cost = 0
    while not min_cost or cost < min_cost:
        for burrow in burrows:
            for new_burrow in burrow.move():
                if not min_cost or new_burrow.cost < min_cost:
                    if new_burrow.final():
                        min_cost = new_burrow.cost
                    elif new_burrow.cost in groups:
                        groups[new_burrow.cost].add(new_burrow)
                    else:
                        groups[new_burrow.cost] = {new_burrow}
        if not groups:
            break
        cost, burrows = groups.popitem(index=0)
    return min_cost


def dump(burrow: Burrow) -> None:
    for row in range(burrow.height):
        for column in range(13 if row < 3 else 11):
            amphipod = burrow[row, column]
            if amphipod:
                print(amphipod.kind, end='')
                continue
            if (
                row == 0 or
                column in (0, 12) and row == 1 or
                column in (0, 1, 2, 4, 6, 8, 10, 11, 12) and row == 2 or
                column in (2, 4, 6, 8, 10) and 2 < row < burrow.height - 1 or
                column in (2, 3, 4, 5, 6, 7, 8, 9,
                           10) and row == burrow.height - 1
            ):
                print('#', end='')
                continue
            if row > 2 and (column < 2 or column > 10):
                print(' ', end='')
                continue
            print('.', end='')
        print()
