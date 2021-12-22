from block import Block
import re

def part1(rows: list[str]) -> int:
    # cubes = set()
    # for row in rows:
    #     state, (x0, x1), (y0, y1), (z0, z1) = parse(row)
    #     for x in range(x0, x1 + 1):
    #         for y in range(y0, y1 + 1):
    #             for z in range(z0, z1 + 1):
    #                 if state == "on":
    #                     cubes.add((x, y, z))
    #                 elif (x, y, z) in cubes:
    #                     cubes.remove((x, y, z))
    # return len(cubes)
    blocks = []
    for count, row in enumerate(rows):
        print(count, len(blocks))
        action, (x0, x1), (y0, y1), (z0, z1) = parse(row)
        block = Block((x0, x1), (y0, y1), (z0, z1))
        blocks = [
            rest
            for existing in blocks
            for rest in existing - block
        ]
        if action == "on":
            blocks.append(block)
    return sum(block.size() for block in blocks)
                

                

def part2(rows):
    pass

def parse(row: str) -> int:
    match = re.match(r"(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)", row)
    action, x0, x1, y0, y1, z0, z1 = match.groups()
    return action, (int(x0), int(x1)), (int(y0), int(y1)), (int(z0), int(z1))