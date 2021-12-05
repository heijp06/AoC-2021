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
#     "0,9 -> 5,9",
#     "8,0 -> 0,8",
#     "9,4 -> 3,4",
#     "2,2 -> 2,1",
#     "7,0 -> 7,4",
#     "6,4 -> 2,0",
#     "0,9 -> 2,9",
#     "3,4 -> 1,4",
#     "0,0 -> 8,8",
#     "5,5 -> 8,2",
# ]

# part2(data)