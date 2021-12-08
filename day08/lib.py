from itertools import permutations


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
        mapping = get_mapping(inputs + outputs)
        value = 0
        for digit in outputs:
            index = mapping.index(set(digit))
            value *= 10
            value += index
        total += value
    return total


def get_mapping(digits: list[str]) -> list[set[str]]:
    for permutation in [list(p) for p in permutations("abcdefg")]:
        zero = {permutation[i] for i in [0, 1, 2, 4, 5, 6]}
        one = {permutation[i] for i in [2, 5]}
        two = {permutation[i] for i in [0, 2, 3, 4, 6]}
        three = {permutation[i] for i in [0, 2, 3, 5, 6]}
        four = {permutation[i] for i in [1, 2, 3, 5]}
        five = {permutation[i] for i in [0, 1, 3, 5, 6]}
        six = {permutation[i] for i in [0, 1, 3, 4, 5, 6]}
        seven = {permutation[i] for i in [0, 2, 5]}
        eight = {permutation[i] for i in [0, 1, 2, 3, 4, 5, 6]}
        nine = {permutation[i] for i in [0, 1, 2, 3, 5, 6]}
        mapping = [zero, one, two, three, four, five, six, seven, eight, nine]
        # if all({digit} in mapping for digit in digits):
        #     return mapping
        found = True
        for digit in digits:
            if not set(digit) in mapping:
                found = False
                break
        if found:
            return mapping
    raise ValueError("Not found.")
