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


rows = tuple(row for row in read_rows())
x = part1(rows)
print(f"Part 1: {x}")
clip(x)

x = part2(rows)
print(f"Part 2: {x}")
clip(x)

# data = [
#     "1163751742",
#     "1381373672",
#     "2136511328",
#     "3694931569",
#     "7463417111",
#     "1319128137",
#     "1359912421",
#     "3125421639",
#     "1293138521",
#     "2311944581"
# ]

# print(part1(data))
