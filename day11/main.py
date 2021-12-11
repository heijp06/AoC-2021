import csv
import pyperclip
from lib import part1, part2


def read_rows(**kwargs):
    with open('data.txt', newline='') as csv_file:
        # return list(csv.reader(csv_file, **kwargs))
        # return csv_file.read().strip()
        return csv_file.read().splitlines()


def clip(x):
    if not x:
        return
    pyperclip.copy(x)


rows = tuple(read_rows())
x = part1(rows)
print(f"Part 1: {x}")
clip(x)

x = part2(rows)
print(f"Part 2: {x}")
clip(x)

# data = [
#     "5483143223",
#     "2745854711",
#     "5264556173",
#     "6141336146",
#     "6357385478",
#     "4167524645",
#     "2176841721",
#     "6882881134",
#     "4846848554",
#     "5283751526"
# ]


# part1(data, 2)