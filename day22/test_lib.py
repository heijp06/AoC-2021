import pytest
from lib import part1, part2
from block import Block, merge


def test_part1():
    assert part1(data) == 39


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


data = [
    "on x=10..12,y=10..12,z=10..12",
    "on x=11..13,y=11..13,z=11..13",
    "off x=9..11,y=9..11,z=9..11",
    "on x=10..10,y=10..10,z=10..10",
]
