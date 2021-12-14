from itertools import groupby


def part1(rows):
    template = list(rows[0])
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


def part2(rows):
    pass
