from lib import part1, part2


def test_part1():
    assert part1(data) == 17


def test_part2():
    assert part2(data) == 16


def test_unequal_length_horizontal():
    assert part1(["0,3", "", "fold along y=2"]) == 1


def test_unequal_length_vertical():
    assert part1(["3,0", "", "fold along x=2"]) == 1


data = [
    "6,10",
    "0,14",
    "9,10",
    "0,3",
    "10,4",
    "4,11",
    "6,0",
    "6,12",
    "4,1",
    "0,13",
    "10,12",
    "3,4",
    "3,0",
    "8,4",
    "1,10",
    "2,14",
    "8,10",
    "9,0",
    "",
    "fold along y=7",
    "fold along x=5"
]
