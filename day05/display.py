import sys


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
        stdout = sys.stdout
        with open(f"img/img{self.image_number:08d}.txt", "w") as f:
            sys.stdout = f
            self.show()
        sys.stdout = stdout
        self.image_number += 1
