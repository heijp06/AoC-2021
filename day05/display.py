import sys
from PIL import Image, ImageDraw, ImageFont


class Display:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("width and height should be positive.")
        self.width = width
        self.height = height
        self.lines = [list(" " * self.width) for _ in range(self.height)]
        self.image_number = 0

    def __setitem__(self, index, char):
        if not isinstance(char, str) or len(char) != 1:
            raise ValueError("char should be string of length 1.")
        x, y = index
        self.lines[y][x] = char

    def __getitem__(self, index):
        x, y = index
        return self.lines[y][x]

    def clear(self, char):
        if not isinstance(char, str) or len(char) != 1:
            raise ValueError("char should be of length 1.")
        for line in self.lines:
            line[:] = list(char * self.width)

    def show(self):
        for line in self.lines:
            print("".join(line))

    def write_image(self):
        font = ImageFont.truetype(r"C:\Windows\Fonts\consola.ttf", 24)
        (width, height) = font.getsize("X")
        margin = 10
        image = Image.new("RGB", (margin * 2 + self.width * width, margin * 2 + self.height * height))
        draw = ImageDraw.Draw(image)
        color_table = { ".": 0xff0000, "1": 0xff5555, "2": 0xffaaaa, "3": 0xffffff}
        for y in range(self.height):
            for x in range(self.width):
                char = self.lines[y][x]
                color = color_table[char]
                draw.text((margin + width * x, margin + height * y), self.lines[y][x], fill=color, font=font)
        image.save(f"img/img{self.image_number:08d}.png")
        self.image_number += 1