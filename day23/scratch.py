from burrow import Burrow, parse
from lib import part1, part2


def dump(burrow: Burrow) -> None:
    for row in range(len(data)):
        for column in range(len(data[row])):
            amphipod = burrow[row, column]
            print(amphipod and amphipod.kind or grid[row][column], end='')
        print()
    print()


data = [
    "#############",
    "#...........#",
    "###B#C#B#D###",
    "  #A#D#C#A#",
    "  #########",
]

print(part2(data))

grid = [
    "#############",
    "#...........#",
    "###.#.#.#.###",
    "  #.#.#.#.#",
    "  #########",
]

# burrow = parse(data)

# dump(burrow)
# print("--------------------------------------------------------------------------------")

# for b in burrow.move():
#     dump(b)
