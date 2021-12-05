import pytest
from lib import part1, part2


def test_part2():
    assert part2(data) == 12

def test_diagonal_topleft_bottomright():
    assert part2([
        "0,0 -> 2,2",
        "0,1 -> 2,1"
    ]) == 1

def test_diagonal():
    assert part2([
        "2,2 -> 0,0",
        "0,1 -> 2,1"
    ]) == 1


data = [
    "0,9 -> 5,9",
    "8,0 -> 0,8",
    "9,4 -> 3,4",
    "2,2 -> 2,1",
    "7,0 -> 7,4",
    "6,4 -> 2,0",
    "0,9 -> 2,9",
    "3,4 -> 1,4",
    "0,0 -> 8,8",
    "5,5 -> 8,2",
]