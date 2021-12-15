import pytest
from lib import max_bottom_right, part1, part2
from path_finder import PathFinder


data = [
    "1163751742",
    "1381373672",
    "2136511328",
    "3694931569",
    "7463417111",
    "1319128137",
    "1359912421",
    "3125421639",
    "1293138521",
    "2311944581"
]

other = [
    "19999",
    "19111",
    "19191",
    "19191",
    "11191"
]


@pytest.mark.parametrize(["grid", "expected"], ((data, 40), (other, 14)))
def test_part1(grid, expected):
    assert part1(grid) == expected


@pytest.mark.parametrize(["grid", "expected"], ((data, 40), (other, 16)))
def test_max_bottom_right(grid, expected):
    assert max_bottom_right(grid) == expected


def test_manhattan_distance():
    path_finder = PathFinder([[1, 1], [1, 1]])
    assert path_finder.manhattan_distance_to_end() == 2
