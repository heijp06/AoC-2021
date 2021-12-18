import pytest
from lib import part1, part2
from snailfish import Parser, RootSnailFish, Snailfish, parse


@pytest.mark.parametrize(["row", "expected"], (
    ("1", 1),
    ("[1,2]", 7),
    ("[[1,2],[[3,4],5]]", 143),
    ("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]", 1384),
    ("[[[[1,1],[2,2]],[3,3]],[4,4]]", 445),
    ("[[[[3,0],[5,3]],[4,4]],[5,5]]", 791),
    ("[[[[5,0],[7,4]],[5,5]],[6,6]]", 1137),
    ("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]", 3488),
))
def test_magnitude(row, expected):
    snailfish = parse(row)
    assert snailfish.magnitude() == expected


@pytest.mark.parametrize(["row", "result", "expected"], (
    ("1", False, "1"),
    ("[1,2]", False, "[1,2]"),
    ("[[[[[9,8],1],2],3],4]", True, "[[[[0,9],2],3],4]"),
    ("[7,[6,[5,[4,[3,2]]]]]", True, "[7,[6,[5,[7,0]]]]"),
    ("[[6,[5,[4,[3,2]]]],1]", True, "[[6,[5,[7,0]]],3]"),
    ("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]",
     True, "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"),
    ("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]", True, "[[3,[2,[8,0]]],[9,[5,[7,0]]]]"),
))
def test_explode(row, result, expected):
    snailfish = parse(row)
    changed = snailfish.explode()

    assert changed == result
    assert str(snailfish) == expected


@pytest.mark.parametrize(["row", "first_left", "first_right"], (
    ("[1,2]", "1", "2"),
    ("[1,[2,3]]", "1", "2"),
    ("[[1,2],3]", "2", "3"),
    ("[[[[1,2],3],4],5]", "4", "5"),
    ("[1,[2,[3,[4,5]]]]", "1", "2"),
    ("[[1,[2,[3,4]]],5]", "4", "5"),
    ("[1,[[[2,3],4],5]]", "1", "2"),
))
def test_first_left_and_first_right(row, first_left, first_right):
    snailfish = parse(row).child

    assert str(snailfish.left.first_right()) == first_right
    assert str(snailfish.left.first_left()) == "None"
    assert str(snailfish.right.first_right()) == "None"
    assert str(snailfish.right.first_left()) == first_left


def test_parent():
    snailfish = parse("1")
    assert snailfish.parent is None

    snailfish = parse("[1,2]")
    assert snailfish.parent is None
    assert snailfish.child.left.parent == snailfish.child
    assert snailfish.child.right.parent == snailfish.child


@pytest.mark.parametrize(["row", "expected"], (
    ("10", "[5,5]"),
    ("11", "[5,6]"),
    ("12", "[6,6]"),
    ("[[[[0,7],4],[15,[0,13]]],[1,1]]", "[[[[0,7],4],[[7,8],[0,13]]],[1,1]]"),
    ("[[[[0,7],4],[[7,8],[0,13]]],[1,1]]",
     "[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]"),
))
def test_split(row, expected):
    snailfish = parse(row)

    assert snailfish.split()
    assert str(snailfish) == expected
