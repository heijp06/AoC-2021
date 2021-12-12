import pytest
from lib import part1, part2


def test_part1():
    assert part1(data) == 10


data = [
    "start-A",
    "start-b",
    "A-c",
    "A-b",
    "b-d",
    "A-end",
    "b-end"
]
