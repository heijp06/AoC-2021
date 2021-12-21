import pytest
from lib import part1, part2


def test_part1():
    assert part1(data) == 739785


def test_part2():
    assert part2(data) == 444356092776315


data = [
    "Player 1 starting position: 4",
    "Player 2 starting position: 8"
]
