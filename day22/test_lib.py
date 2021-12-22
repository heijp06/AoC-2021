import pytest
from lib import part1, part2
from block import Block, merge


data1 = [
    "on x=10..12,y=10..12,z=10..12",
    "on x=11..13,y=11..13,z=11..13",
    "off x=9..11,y=9..11,z=9..11",
    "on x=10..10,y=10..10,z=10..10",
]

data2 = [
    "on x=-20..26,y=-36..17,z=-47..7",
    "on x=-20..33,y=-21..23,z=-26..28",
    "on x=-22..28,y=-29..23,z=-38..16",
    "on x=-46..7,y=-6..46,z=-50..-1",
    "on x=-49..1,y=-3..46,z=-24..28",
    "on x=2..47,y=-22..22,z=-23..27",
    "on x=-27..23,y=-28..26,z=-21..29",
    "on x=-39..5,y=-6..47,z=-3..44",
    "on x=-30..21,y=-8..43,z=-13..34",
    "on x=-22..26,y=-27..20,z=-29..19",
    "off x=-48..-32,y=26..41,z=-47..-37",
    "on x=-12..35,y=6..50,z=-50..-2",
    "off x=-48..-32,y=-32..-16,z=-15..-5",
    "on x=-18..26,y=-33..15,z=-7..46",
    "off x=-40..-22,y=-38..-28,z=23..41",
    "on x=-16..35,y=-41..10,z=-47..6",
    "off x=-32..-23,y=11..30,z=-14..3",
    "on x=-49..-5,y=-3..45,z=-29..18",
    "off x=18..30,y=-20..-8,z=-3..13",
    "on x=-41..9,y=-7..43,z=-33..15",
    "on x=-54112..-39298,y=-85059..-49293,z=-27449..7877",
    "on x=967..23432,y=45373..81175,z=27513..53682",
]


@pytest.mark.parametrize(["data", "expected"], [
    (data1, 39),
    (data2, 590784)
])
def test_part1(data, expected):
    assert part1(data) == expected


def test_subtract():
    big = Block((1, 3), (1, 3), (1, 3))
    small = Block((2, 2), (2, 2), (2, 2))

    rest = big - small

    assert sum(block.size() for block in rest) == 26

    assert all(block in big for block in rest)
    assert all(small not in block for block in rest)
    assert all(
        any(Block((x, x), (y, y), (z, z)) in block for block in rest)
        for x in range(1, 4)
        for y in range(1, 4)
        for z in range(1, 4)
        if x != 2 or y != 2 or z != 2
    )


def test_add():
    block1 = Block((1, 2), (1, 2), (1, 2))
    block2 = Block((2, 3), (2, 3), (2, 3))

    total = block1 + block2

    assert sum(block.size() for block in total) == 15

    assert all(
        any(block in part for part in total)
        for x in range(1, 4)
        for y in range(1, 4)
        for z in range(1, 4)
        if (block := Block((x, x), (y, y), (z, z)))
        and block in block1
        and block in block2
    )
    assert all(
        all(block not in part for part in total)
        for x in range(1, 4)
        for y in range(1, 4)
        for z in range(1, 4)
        if (block := Block((x, x), (y, y), (z, z)))
        and block not in block1
        and block not in block2
    )


def test_size():
    block = Block((1, 2), (1, 3), (1, 5))

    assert block.size() == 30


@pytest.mark.parametrize(["block1", "block2", "expected"], [
    (((0, 0), (0, 0), (0, 0)), ((1, 1), (0, 0), (0, 0)), ((0, 1), (0, 0), (0, 0))),
    (((1, 1), (0, 0), (0, 0)), ((0, 0), (0, 0), (0, 0)), ((0, 1), (0, 0), (0, 0))),
    (((0, 0), (0, 0), (0, 0)), ((0, 0), (1, 1), (0, 0)), ((0, 0), (0, 1), (0, 0))),
    (((0, 0), (1, 1), (0, 0)), ((0, 0), (0, 0), (0, 0)), ((0, 0), (0, 1), (0, 0))),
    (((0, 0), (0, 0), (0, 0)), ((0, 0), (0, 0), (1, 1)), ((0, 0), (0, 0), (0, 1))),
    (((0, 0), (0, 0), (1, 1)), ((0, 0), (0, 0), (0, 0)), ((0, 0), (0, 0), (0, 1))),
    (((0, 0), (0, 0), (0, 0)), ((2, 2), (0, 0), (0, 0)), None),
    (((0, 0), (0, 0), (0, 0)), ((0, 0), (2, 2), (0, 0)), None),
    (((0, 0), (0, 0), (0, 0)), ((0, 0), (0, 0), (2, 2)), None),
])
def test_glue(block1, block2, expected):
    assert Block(*block1).glue(Block(*block2)
                               ) == (expected and Block(*expected))


def test_merge():
    assert merge([]) == []

    block = Block((0, 0), (0, 0), (0, 0))
    assert merge([block]) == [block]

    blocks = [
        Block((x, x), (y, y), (z, z))
        for x in range(2)
        for y in range(2)
        for z in range(2)
    ]

    merged = merge(blocks)

    assert len(merged) <= 5
    assert all(block in merged for block in blocks)


@pytest.mark.parametrize(["split_at", "sides"], [
    ((-6, -4), [(-3, 3)]),
    ((-5, -3), [(-3, -3), (-2, 3)]),
    ((-4, -2), [(-3, -2), (-1, 3)]),
    ((-3, -1), [(-3, -1), (0, 3)]),
    ((-2, 0), [(-3, -3), (-2, 0), (1, 3)]),
    ((-1, 1), [(-3, -2), (-1, 1), (2, 3)]),
    ((0, 2), [(-3, -1), (0, 2), (3, 3)]),
    ((1, 3), [(-3, 0), (1, 3)]),
    ((2, 4), [(-3, 1), (2, 3)]),
    ((3, 5), [(-3, 2), (3, 3)]),
    ((4, 6), [(-3, 3)]),
    ((-4, 4), [(-3, 3)])
])
def test_split_x(split_at, sides):
    block = Block((-3, 3), (-10, 10), (-20, 20))

    assert set(block.split_x(split_at)) == {
        Block(side, (-10, 10), (-20, 20)) for side in sides
    }


@pytest.mark.parametrize(["split_at", "sides"], [
    ((-6, -4), [(-3, 3)]),
    ((-5, -3), [(-3, -3), (-2, 3)]),
    ((-4, -2), [(-3, -2), (-1, 3)]),
    ((-3, -1), [(-3, -1), (0, 3)]),
    ((-2, 0), [(-3, -3), (-2, 0), (1, 3)]),
    ((-1, 1), [(-3, -2), (-1, 1), (2, 3)]),
    ((0, 2), [(-3, -1), (0, 2), (3, 3)]),
    ((1, 3), [(-3, 0), (1, 3)]),
    ((2, 4), [(-3, 1), (2, 3)]),
    ((3, 5), [(-3, 2), (3, 3)]),
    ((4, 6), [(-3, 3)]),
    ((-4, 4), [(-3, 3)])
])
def test_split_y(split_at, sides):
    block = Block((-10, 10), (-3, 3), (-20, 20))

    assert set(block.split_y(split_at)) == {
        Block((-10, 10), side, (-20, 20)) for side in sides
    }


@pytest.mark.parametrize(["split_at", "sides"], [
    ((-6, -4), [(-3, 3)]),
    ((-5, -3), [(-3, -3), (-2, 3)]),
    ((-4, -2), [(-3, -2), (-1, 3)]),
    ((-3, -1), [(-3, -1), (0, 3)]),
    ((-2, 0), [(-3, -3), (-2, 0), (1, 3)]),
    ((-1, 1), [(-3, -2), (-1, 1), (2, 3)]),
    ((0, 2), [(-3, -1), (0, 2), (3, 3)]),
    ((1, 3), [(-3, 0), (1, 3)]),
    ((2, 4), [(-3, 1), (2, 3)]),
    ((3, 5), [(-3, 2), (3, 3)]),
    ((4, 6), [(-3, 3)]),
    ((-4, 4), [(-3, 3)])
])
def test_split_z(split_at, sides):
    block = Block((-10, 10), (-20, 20), (-3, 3))

    assert set(block.split_z(split_at)) == {
        Block((-10, 10), (-20, 20), side) for side in sides
    }
