import re
from collections import defaultdict


def part1(rows):
    return count_overlap(rows, diagonals=False)


def part2(rows, observer=None):
    return count_overlap(rows, diagonals=True, observer=observer)


def count_overlap(rows, diagonals, observer=None):
    if not observer:
        def observer(item, value):
            pass
    points = ObservableDefaultDict(observer, int)
    for row in rows:
        a, b, u, v = re.split(r" -> |,", row)
        x1, y1, x2, y2 = int(a), int(b), int(u), int(v)
        if not diagonals and x1 != x2 and y1 != y2:
            continue
        steps = max(abs(x1 - x2), abs(y1 - y2)) + 1
        dx, dy = get_delta(x1, x2), get_delta(y1, y2)
        x, y = x1, y1
        for _ in range(steps):
            points[x, y] += 1
            x, y = x + dx, y + dy
    return sum(value > 1 for value in points.values())


def get_delta(u1, u2):
    if u1 == u2:
        return 0
    else:
        return 1 if u2 > u1 else -1


class ObservableDefaultDict(defaultdict):
    def __init__(self, observer, default_factory=None):
        self.observer = observer
        super().__init__(default_factory)

    def __setitem__(self, item, value):
        self.observer(item, value)
        super().__setitem__(item, value)
