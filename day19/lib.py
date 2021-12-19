from itertools import combinations
from scanner import Scanner, parse


def part1(data: list[str]) -> int:
    beacons = {
        beacon
        for scanner in go(data)
        for beacon in scanner.beacons
    }
    return len(beacons)


def part2(data: list[str]) -> int:
    return int(max(
        abs(x1 - x0) + abs(y1 - y0) + abs(z1 - z0)
        for (x0, y0, z0), (x1, y1, z1)
        in combinations((scanner.position for scanner in go(data)), 2)
    ))


def go(data: list[str]) -> list[Scanner]:
    scanners = parse(data)
    oriented = [scanners[0]]
    to_orient = scanners[1:]
    while to_orient:
        new_oriented = []
        new_to_orient = []
        for scanner in to_orient:
            if any(
                scanner.set_orientation(reference)
                and scanner.set_position(reference)
                for reference in oriented
            ):
                new_oriented.append(scanner)
            else:
                new_to_orient.append(scanner)
        oriented = new_oriented
        to_orient = new_to_orient
    return scanners
