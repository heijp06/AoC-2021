import pyperclip    # type: ignore
from lib import part1, part2
from datetime import datetime


def read_rows(**kwargs):
    with open('data.txt', newline='') as csv_file:
        return csv_file.read().splitlines()


def clip(x):
    if not x:
        return
    pyperclip.copy(x)

t0 = datetime.now()

rows = read_rows()
x = part1(rows)
print(f"Part 1: {x}")
clip(x)

x = part2(rows)
print(f"Part 2: {x}")
clip(x)

t1 = datetime.now()

print(t1 - t0)