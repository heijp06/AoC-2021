from functools import reduce
from itertools import product
from snailfish import Snailfish, parse


def part1(rows: list[str]) -> int:
    snailfish = sum_list(rows)
    return snailfish.magnitude()


def part2(rows: list[str]) -> int:
    return max(
        (parse(a) + parse(b)).magnitude()
        for a, b in product(rows, repeat=2)
    )


def sum_list(rows: list[str]) -> Snailfish:
    return reduce(lambda x, y: x + y, (parse(row) for row in rows))
