import pytest
from lib import part1, part2


@pytest.mark.parametrize(["instruction", "expected"], (
    ("target area: x=20..30, y=-10..-5", 45),
    ("target area: x=1..1, y=-1..-1", 0)
))
def test_part1(instruction, expected):
    assert part1(instruction) == expected


@pytest.mark.parametrize(["instruction", "expected"], (
    ("target area: x=20..30, y=-10..-5", 112),
    ("target area: x=1..1, y=-1..-1", 2)
))
def test_part2(instruction, expected):
    assert part2(instruction) == expected