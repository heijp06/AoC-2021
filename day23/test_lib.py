import pytest
from lib import part1, part2
from amphipod import Amphipod
from burrow import Burrow, parse

data = [
    "#############",
    "#...........#",
    "###B#C#B#D###",
    "  #A#D#C#A#",
    "  #########",
]

final = [
    "#############",
    "#...........#",
    "###A#B#C#D###",
    "  #A#B#C#D#",
    "  #########",
]


@pytest.mark.skip()
def test_part1():
    assert part1(data) == 12521


def test_parse():
    amphipods = [
        Amphipod(*amphipod) for amphipod in
        [
            ((2, 3), "B"),
            ((3, 3), "A"),
            ((2, 5), "C"),
            ((3, 5), "D"),
            ((2, 7), "B"),
            ((3, 7), "C"),
            ((2, 9), "D"),
            ((3, 9), "A"),
        ]
    ]
    expected = Burrow(amphipods, 0)
    actual = parse(data)

    assert actual == expected


@pytest.mark.parametrize(["grid", "number"], [
    (data, 28),
    (final, 0)
])
def test_move(grid, number):
    burrow = parse(grid)
    burrows = burrow.move()

    assert len(burrows) == number


@pytest.mark.parametrize(["grid", "is_final"], [
    (data, False),
    (final, True)
])
def test_final(grid, is_final):
    burrow = parse(grid)
    assert burrow.final() == is_final
