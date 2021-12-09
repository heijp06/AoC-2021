from itertools import permutations

segments = [
    [0, 1, 2, 4, 5, 6],
    [2, 5],
    [0, 2, 3, 4, 6],
    [0, 2, 3, 5, 6],
    [1, 2, 3, 5],
    [0, 1, 3, 5, 6],
    [0, 1, 3, 4, 5, 6],
    [0, 2, 5],
    [0, 1, 2, 3, 4, 5, 6],
    [0, 1, 2, 3, 5, 6]
]


def part1(rows: list[str]) -> int:
    total = 0
    for row in rows:
        _, output = row.split(" | ")
        total += sum(
            len(number) in (2, 3, 4, 7)
            for number
            in output.split(" ")
        )
    return total


def part2(rows: list[str]) -> int:
    total = 0
    for row in rows:
        input, output = row.split(" | ")
        inputs = input.split()
        outputs = output.split()
        mapping = get_mapping(inputs)
        value = 0
        for digit in outputs:
            index = mapping.index(set(digit))
            value *= 10
            value += index
        total += value
    return total


def get_mapping(digits: list[str]) -> list[set[str]]:
    for permutation in (list(p) for p in permutations("abcdefg")):
        mapping = [
            {permutation[i] for i in segments[number]}
            for number in range(10)
        ]
        if all(set(digit) in mapping for digit in digits):
            return mapping
    raise ValueError("Not found.")
