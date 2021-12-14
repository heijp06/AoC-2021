import pytest
from lib import go, part1, part2


def test_part1():
    assert part1(data) == 1588


def test_part2():
    assert part2(data) == 2188189693529


@pytest.mark.parametrize(["times", "expected"], [(0, 1), (1, 1), (10, 1588), (40, 2188189693529)])
def test_go(times, expected):
    assert go(data, times) == expected


data = [
    "NNCB",
    "",
    "CH -> B",
    "HH -> N",
    "CB -> H",
    "NH -> C",
    "HB -> C",
    "HC -> B",
    "HN -> C",
    "NN -> C",
    "BH -> H",
    "NC -> B",
    "NB -> B",
    "BN -> B",
    "BB -> N",
    "BC -> B",
    "CC -> N",
    "CN -> C"
]
