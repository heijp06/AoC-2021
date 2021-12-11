from PIL import Image, ImageDraw, ImageFont  # type: ignore
from view import View


class Label(View):
    def __init__(self, text: str, width: int = None, color: int = 0xffffff, font: ImageFont = None) -> None:
        self.text = text
        self.color = color
        self.font = font or ImageFont.load_default()
        char_width, self._height = self.font.getsize("X")
        self._width = width or char_width * len(text)

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    def paint(self, image: Image) -> None:
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), self.text, fill=self.color, font=self.font)
