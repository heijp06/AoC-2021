from view import View
from PIL import Image, ImageDraw, ImageFont  # type: ignore


class TextGridView(View):
    def __init__(self, rows: int, columns: int, font: ImageFont = None) -> None:
        self.rows = rows
        self.columns = columns
        self.font = font or ImageFont.load_default()
        self.char_width, self.char_height = self.font.getsize("X")
        self.lines = [list(" " * columns) for _ in range(rows)]

    @property
    def width(self) -> int:
        return self.columns * self.char_width

    @property
    def height(self) -> int:
        return self.rows * self.char_height

    def paint(self, image: Image) -> None:
        draw = ImageDraw.Draw(image)
        color_table = {".": 0xff0000, "1": 0xff5555,
                       "2": 0xffaaaa, "3": 0xffffff}
        for y in range(self.rows):
            for x in range(self.columns):
                char = self.lines[y][x]
                color = color_table[char]
                draw.text((self.char_width * x, self.char_height * y),
                          self.lines[y][x], fill=color, font=self.font)

    def __setitem__(self, index: tuple[int, int], char: str) -> None:
        if not isinstance(char, str) or len(char) != 1:
            raise ValueError("char should be string of length 1.")
        x, y = index
        self.lines[y][x] = char

    def __getitem__(self, index: tuple[int, int]) -> str:
        x, y = index
        return self.lines[y][x]

    def clear(self, char: str) -> None:
        if not isinstance(char, str) or len(char) != 1:
            raise ValueError("char should be of length 1.")
        for line in self.lines:
            line[:] = list(char * self.width)
