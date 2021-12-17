import pyperclip
from lib import part1, part2


def read_rows(**kwargs):
    with open('data.txt', newline='') as csv_file:
        return csv_file.read().strip()


def clip(x):
    if not x:
        return
    pyperclip.copy(x)


rows = read_rows()
x = part1(rows)
print(f"Part 1: {x}")
clip(x)

x = part2(rows)
print(f"Part 2: {x}")
clip(x)
