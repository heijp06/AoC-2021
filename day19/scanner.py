from __future__ import annotations
import numpy as np
from itertools import combinations

COMMON_BEACONS = 12


def parse(rows: list[str]) -> list[Scanner]:
    scanners = []
    beacons = []
    name = ""
    for row in rows:
        match row.split(","):
            case [x, y, z]:
                beacons.append((int(x), int(y), int(z)))
            case [""]:
                scanners.append(Scanner(name, beacons))
                beacons = []
            case [header]:
                name = header[4:-4]
    scanners.append(Scanner(name, beacons))
    return scanners


def get_rotations() -> list[np.array]:
    identity = np.identity(3, dtype=int)    # z' = z
    rot_x = np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]], dtype=int)  # z' = y
    rot_y = np.array([[0, 0, 1], [0, 1, 0], [-1, 0, 0]], dtype=int)  # z' = -x
    inv_rot_x = np.linalg.matrix_power(rot_x, 3)    # z' = -y
    inv_rot_y = np.linalg.matrix_power(rot_y, 3)    # z' = x
    rot_x_2 = np.linalg.matrix_power(rot_x, 2)  # z' = z

    rot_z = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]],
                     dtype=int)  # rotate around z

    return [
        np.linalg.matrix_power(rot_z, i).dot(m)
        # choose z'
        for m in [identity, rot_x, rot_y, rot_x_2, inv_rot_x, inv_rot_y]
        for i in range(4)   # rotate around z'
    ]


class Scanner:
    def __init__(self, name: str, beacons: list[tuple[int, int, int]]):
        self.name = name
        self.beacons = beacons
        self.position = (0, 0, 0)
    
    def __repr__(self) -> str:
        return self.name

    def set_orientation(self, reference: Scanner) -> bool:
        reference_deltas = set(reference.get_deltas())
        for rotation in get_rotations():
            beacons = [
                tuple(rotation.dot(np.array(beacon)))
                for beacon in self.beacons
            ]
            deltas = self.get_deltas(beacons)
            count = sum(delta in reference_deltas for delta in deltas)
            if count >= COMMON_BEACONS * (COMMON_BEACONS - 1) // 2:
                self.beacons = beacons
                return True
        return False

    def set_position(self, reference: Scanner) -> bool:
        reference_positions = set(reference.beacons)
        for beacon in self.beacons:
            for position in reference_positions:
                delta = np.array(position) - np.array(beacon)
                beacons = [tuple(np.array(b) + delta)
                           for b in self.beacons]
                count = sum(
                    b in reference_positions for b in beacons)
                if count >= COMMON_BEACONS:
                    self.beacons = beacons
                    self.position = tuple(delta)
                    return True
        return False

    def get_deltas(self, beacons=None) -> list[tuple[int, int, int]]:
        beacons = beacons or self.beacons
        return [
            (x1 - x0, y1 - y0, z1 - z0)
            for (x0, y0, z0), (x1, y1, z1)
            in combinations(sorted(beacons), 2)
        ]
