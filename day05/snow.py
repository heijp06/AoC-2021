from PIL import Image, ImageDraw, ImageFont  # type: ignore
from view import View
import random


class Snow(View):
    def __init__(self, child: View, font=None) -> None:
        self.child = child
        self.font = font or ImageFont.load_default()
        self.char_width, self.char_height = self.font.getsize("X")
        self.flakes: list[Flake] = []

    @property
    def width(self) -> int:
        return self.child.width

    @property
    def height(self) -> int:
        return self.child.height

    def paint(self, image: Image) -> None:
        self.child.paint(image)
        draw = ImageDraw.Draw(image)
        for flake in self.flakes:
            draw.text(flake.position, "*", fill=0xffffff, font=self.font)
        self.update_flakes()

    def update_flakes(self) -> None:
        self.flakes = [
            flake for flake in self.flakes if flake.position[1] <= self.height]
        x = random.randrange(-self.width, 2 * self.width)
        y = -self.char_height
        dx = random.randrange(-3, 4)
        dy = 4 - abs(dx)
        self.flakes.append(Flake((x, y), (dx, dy)))
        for flake in self.flakes:
            flake.move()


class Flake():
    def __init__(self, position: tuple[int, int], direction: tuple[int, int]) -> None:
        self.position = position
        self.direction = direction
        self.counter = random.randrange(10, 20)

    def move(self) -> None:
        x, y = self.position
        dx, dy = self.direction
        self.position = (x + dx, y + dy)

    def __repr__(self) -> str:
        return f"{self.position}, {self.direction}"
