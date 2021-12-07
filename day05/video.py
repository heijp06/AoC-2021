from lib import part2
from display import Display

display = Display(10, 10)
display.clear(".")
display.write_image()


def item_set(item, value):
    if not value:
        return
    display[item] = str(value)
    display.write_image()


data = [
    "0,9 -> 5,9",
    "8,0 -> 0,8",
    "9,4 -> 3,4",
    "2,2 -> 2,1",
    "7,0 -> 7,4",
    "6,4 -> 2,0",
    "0,9 -> 2,9",
    "3,4 -> 1,4",
    "0,0 -> 8,8",
    "5,5 -> 8,2",
]

x = part2(data, observer=item_set)
