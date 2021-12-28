from typing import Any
from simple_alu import SimpleAlu

REPEATED_CODE_LENGTH = 18


def part1(rows: list[str]) -> str:
    return go(rows, lambda b, c: min(9, 9 - b - c))


def part2(rows):
    return go(rows, lambda b, c: max(1, 1 - b - c))


# For the reasons behind the code here, see analysis.txt in the same folder as this file.
def go(rows: list[str], func: Any) -> str:  # sourcery skip: move-assign
    cs = []
    digits = []
    for index in range(0, len(rows), REPEATED_CODE_LENGTH):
        a = get_value(rows[index + 4])
        b = get_value(rows[index + 5])
        c = get_value(rows[index + 15])
        if a == 1:
            cs.append((index // REPEATED_CODE_LENGTH, c))
            digits.append('*')
        else:
            old_index, old_c = cs.pop()
            # old_digit = min(9, 9 - old_c - b)
            old_digit = func(b, old_c)
            digits[old_index] = old_digit
            digit = old_digit + old_c + b
            digits.append(digit)
    return "".join(str(digit) for digit in digits)


def get_value(row: str) -> int:
    return int(row.split()[-1])
