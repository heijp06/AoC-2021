import pytest
from lib import flashing_neighbours, part1, part2


def test_part1():
    assert part1(data) == 1656


def test_part2():
    assert part2(data) == 195


@pytest.mark.parametrize("steps", range(1, 3))
def test_part1_small(steps):
    assert part1(small, steps=1) == 9


@pytest.mark.parametrize(("grid", "expected"), ((["98"], 2), (["988", 3])))
def test_part1_ripple(grid, expected):
    assert part1(grid, 1) == expected


def test_octopus_only_flashes_once():
    assert part1(["96", "08"], 1) == 2


def test_flashing_neighbours():
    assert flashing_neighbours([[10, 9]], 0, 1) == 1


small = [
    "11111",
    "19991",
    "19191",
    "19991",
    "11111"
]

data = [
    "5483143223",
    "2745854711",
    "5264556173",
    "6141336146",
    "6357385478",
    "4167524645",
    "2176841721",
    "6882881134",
    "4846848554",
    "5283751526"
]
