from itertools import groupby
from collections import defaultdict


def part1(rows):
    template = rows[0]
    rules = {}
    for row in rows[2:]:
        fields = row.split()
        rules[fields[0]] = fields[2]
    for _ in range(10):
        new_template = []
        for a, b in zip(template, template[1:]):
            if a + b in rules:
                c = rules[a + b]
                new_template.extend([a, c])
            else:
                raise ValueError()
        new_template.append(template[-1])
        template = new_template
    bla = sorted(template)
    minimum = min(len(list(x)) for _, x in groupby(bla))
    maximum = max(len(list(x)) for _, x in groupby(bla))
    return maximum - minimum


def part2(rows, times=40):
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
