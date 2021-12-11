from lib import part2
from text_grid_view import TextGridView
from canvas import Canvas
from border import Border
from PIL import ImageFont

font = ImageFont.truetype(r"C:\Windows\Fonts\consola.ttf", 24)

grid = TextGridView(10, 10, font)
grid.clear(".")

border = Border(20, grid)

canvas = Canvas(border)
canvas.save()

def item_set(item, value):
    if not value:
        return
    grid[item] = str(value)
    canvas.save()


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
