from lib import part2
from text_grid_view import TextGridView
from canvas import Canvas
from border import Border
from stack_layout import StackLayout
from label import Label
from snow import Snow
from PIL import ImageFont

font = ImageFont.truetype(r"C:\Windows\Fonts\consola.ttf", 24)

grid = TextGridView(10, 10, font)
grid.clear(".")

grid_border = Border([0, 0, 0, 20], grid)

label_part2 = Label("Part 2: ", font=font)
label_count = Label("0 ", font=font)
hlayout = StackLayout(StackLayout.HORIZONTAL, label_part2, label_count)

vlayout = StackLayout(StackLayout.VERTICAL, grid_border, hlayout)

border = Border(20, vlayout)

snow = Snow(border, font=font)

canvas = Canvas(snow)
canvas.save(10)

count = 0

def item_set(item, value):
    global count
    if not value:
        return
    grid[item] = str(value)
    if value == 2:
        count += 1
    label_count.text = str(count)
    canvas.save(10)


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
