from collections import defaultdict


def part1(rows):
    return go(rows, 10)


def part2(rows):
    return go(rows, 40)


def go(rows, times=40):
    rules = {}
    for row in rows[2:]:
        fields = row.split()
        rules[fields[0]] = fields[2]
    polymer = defaultdict(int)
    last = rows[0][-1]
    for a, b in zip(rows[0], rows[0][1:]):
        polymer[a + b] += 1
    for _ in range(times):
        new_polymer = defaultdict(int)
        for pair, count in polymer.items():
            c = rules[pair]
            new_polymer[pair[0] + c] += count
            new_polymer[c + pair[1]] += count
        polymer = new_polymer
    bla = defaultdict(int)
    for pair, count in polymer.items():
        bla[pair[0]] += count
    bla[last] += 1
    minimum = min(bla.values())
    maximum = max(bla.values())
    return maximum - minimum
