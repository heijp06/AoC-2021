from typing import Sequence
from PIL import Image  # type: ignore
from view import View
from typing import Union


class Border(View):
    def __init__(self, thickness: Union[int, list[int]], child: View) -> None:
        self.child = child
        match thickness:
            case int(_):
                self.left = thickness
                self.upper = thickness
                self.right = thickness
                self.lower = thickness
            case [int(horizontal), int(vertical)]:
                self.left = horizontal
                self.upper = vertical
                self.right = horizontal
                self.lower = vertical
            case [int(left), int(upper), int(right), int(lower)]:
                self.left = left
                self.upper = upper
                self.right = right
                self.lower = lower
            case _:
                raise ValueError(
                    f"Unexpected value for thickness: {thickness}")

    @property
    def width(self) -> int:
        return self.left + self.child.width + self.right

    @property
    def height(self) -> int:
        return self.upper + self.child.height + self.lower

    def paint(self, image: Image) -> None:
        left = self.left
        upper = self.upper
        right = self.right + self.child.width
        lower = self.lower + self.child.height
        inner = image.crop((left, upper, right, lower))
        self.child.paint(inner)
        image.paste(inner, (left, upper))
