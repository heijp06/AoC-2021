from block import Block
import re


def part1(rows: list[str]) -> int:
    return go(rows, 1)


def part2(rows):
    return go(rows, 2)


def go(rows: list[str], part: int):
    blocks = []
    for row in rows:
        action, (x0, x1), (y0, y1), (z0, z1) = parse(row)
        if part == 1 and (x0 < -50 or x0 > 50):
            break
        block = Block((x0, x1), (y0, y1), (z0, z1))
        blocks = [
            rest
            for existing in blocks
            for rest in existing - block
        ]
        if action == "on":
            blocks.append(block)
    return sum(block.size() for block in blocks)


def parse(row: str) -> int:
    match = re.match(
        r"(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)", row)
    action, x0, x1, y0, y1, z0, z1 = match.groups()
    return action, (int(x0), int(x1)), (int(y0), int(y1)), (int(z0), int(z1))
