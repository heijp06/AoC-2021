import pytest
from lib import get_data, max_bottom_right, part1, part2
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


def test_part2():
    assert part2(data) == 315


def test_get_data():
    assert get_data(["8"], 5) == [
        [8, 9, 1, 2, 3],
        [9, 1, 2, 3, 4],
        [1, 2, 3, 4, 5],
        [2, 3, 4, 5, 6],
        [3, 4, 5, 6, 7]
    ]


@pytest.mark.parametrize(["grid", "expected"], ((data, 40), (other, 16)))
def test_max_bottom_right(grid, expected):
    assert max_bottom_right(get_data(grid, 1)) == expected


def test_manhattan_distance():
    path_finder = PathFinder([[1, 1], [1, 1]])
    assert path_finder.manhattan_distance_to_end() == 2
