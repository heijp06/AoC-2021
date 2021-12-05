import re
from collections import defaultdict


def part1(rows):
    points = defaultdict(int)
    for row in rows:
        a, b, u, v = re.split(r" -> |,", row)
        x1, y1, x2, y2 = int(a), int(b), int(u), int(v)
        if x1 == x2:
            x = x1
            start = min(y1, y2)
            end = max(y1, y2)
            for y in range(start, end + 1):
                points[x, y] += 1
        elif y1 == y2:
            y = y1
            start = min(x1, x2)
            end = max(x1, x2)
            for x in range(start, end + 1):
                points[x, y] += 1
    return sum(value > 1 for value in points.values())


def part2(rows):
    points = defaultdict(int)
    for row in rows:
        a, b, u, v = re.split(r" -> |,", row)
        x1, y1, x2, y2 = int(a), int(b), int(u), int(v)
        if x1 == x2:
            x = x1
            start = min(y1, y2)
            end = max(y1, y2)
            for y in range(start, end + 1):
                points[x, y] += 1
        elif y1 == y2:
            y = y1
            start = min(x1, x2)
            end = max(x1, x2)
            for x in range(start, end + 1):
                points[x, y] += 1
        else:
            steps = abs(x1 - x2) + 1
            dx = 1 if x2 > x1 else -1
            dy = 1 if y2 > y1 else -1
            x = x1
            y = y1
            for _ in range(steps):
                points[x, y] += 1
                x += dx
                y += dy
    output(points)
    return sum(value > 1 for value in points.values())

def output(points):
    for y in range(10):
        for x in range(10):
            if (x, y) in points:
                print(points[x, y], end="")
            else:
                print(".", end="")
        print()