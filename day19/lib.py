from scanner import parse


def part1(data: list[str]) -> int:
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
    return len({
        beacon
        for scanner in scanners
        for beacon in scanner.beacons
    })


def part2(data: list[str]) -> int:
    pass
