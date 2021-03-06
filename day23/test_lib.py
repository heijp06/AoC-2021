import pytest
from lib import move, part1, part2
from amphipod import Amphipod
from burrow import Burrow, parse
from routes import Routes

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

cost_8 = [
    "#############",
    "#.........A.#",
    "###.#B#C#D###",
    "  #A#B#C#D#",
    "  #########",
]


@pytest.mark.parametrize(["grid", "expected"], [
    (final, 0),
    (cost_8, 8),
    (data, 12521)
])
def test_part1(grid, expected):
    assert part1(grid) == expected


@pytest.mark.parametrize(["grid", "expected"], [
    (final, 0),
    (cost_8, 8),
    (data, 12499)
])
def test_min_cost_to_end(grid, expected):
    burrow = parse(grid)
    assert burrow.min_cost_to_solution() == expected


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
    height = len(data)
    expected = Burrow(amphipods, height, Routes(height))
    actual = parse(data)

    assert actual == expected


@pytest.mark.parametrize(["grid", "is_final"], [
    (data, False),
    (final, True)
])
def test_final(grid, is_final):
    burrow = parse(grid)
    assert burrow.final() == is_final
