from functools import reduce
from snailfish import Snailfish, parse


def part1(rows: list[str]) -> int:
    snailfish = sum_list(rows)
    return snailfish.magnitude()


def part2(rows: list[str]) -> int:
    pass


def sum_list(rows: list[str]) -> Snailfish:
    return reduce(lambda x, y: x + y, (parse(row) for row in rows))
