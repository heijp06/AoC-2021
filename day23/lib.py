from queue import PriorityQueue
from burrow import Burrow, parse


def part1(rows: list[str]) -> int | None:
    return go(rows)


def part2(rows: list[str]) -> int | None:
    new_rows = list(rows[:3]) + [
        "  #D#C#B#A#",
        "  #D#B#A#C#",
    ] + list(rows[3:])
    return go(new_rows)


def go(rows: list[str]) -> int | None:
    burrow = parse(rows)
    burrows: PriorityQueue = PriorityQueue()
    burrows.put((burrow.min_cost_to_solution(), burrow))
    seen = {burrow: 0}
    min_cost = 0 if burrow.final() else None
    while burrows.qsize():
        min_cost_to_solution, burrow = burrows.get()
        if min_cost and min_cost <= min_cost_to_solution:
            break
        old_cost = seen[burrow]
        for extra_cost, new_burrow in move(burrow):
            new_cost = old_cost + extra_cost
            if (
                (not min_cost or new_cost < min_cost)
                and (new_burrow not in seen or new_cost < seen[new_burrow])
            ):
                seen[new_burrow] = new_cost
                if new_burrow.final():
                    min_cost = new_cost
                else:
                    burrows.put((new_cost + new_burrow.min_cost_to_solution(), new_burrow))
    return min_cost


def move(burrow: Burrow) -> list[tuple[int, Burrow]]:
    for amphipod in burrow.amphipods:
        new_burrow = amphipod.move_home(burrow)
        if new_burrow:
            return [new_burrow]

    return [
        new_burrow
        for amphipod in burrow.amphipods
        for new_burrow in amphipod.move_hallway(burrow)
    ]


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
