import pytest
from lib import part1, part2


def test_part1():
    assert part1(data) == 10


def test_part2():
    assert part2(data) == 36


def test_part2_simple():
    assert part2(simple) == 3


data = [
    "start-A",
    "start-b",
    "A-c",
    "A-b",
    "b-d",
    "A-end",
    "b-end"
]

# start,A,end
# start,A,b,A,end
# start,A,b,A,b,A,end
simple = [
    "start-A",
    "A-b",
    "A-end"
]
