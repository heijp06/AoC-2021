from PIL import Image  # type: ignore
from view import View


class Border(View):
    def __init__(self, thickness: int, child: View) -> None:
        self.child = child
        self.thickness = thickness

    @property
    def width(self) -> int:
        return 2 * self.thickness + self.child.width

    @property
    def height(self) -> int:
        return 2 * self.thickness + self.child.height

    def paint(self, image: Image) -> None:
        left = self.thickness
        upper = self.thickness
        right = self.thickness + self.child.width
        lower = self.thickness + self.child.height
        inner = image.crop((left, upper, right, lower))
        self.child.paint(inner)
        image.paste(inner, (left, upper))
