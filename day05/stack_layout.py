from view import View
from PIL import Image  # type: ignore


class StackLayout(View):
    HORIZONTAL = 0
    VERTICAL = 1

    def __init__(self, orientation: int, *children: View) -> None:
        self.orientation = orientation
        self.children = children

    @property
    def width(self) -> int:
        widths = (child.width for child in self.children)
        if self.orientation == StackLayout.HORIZONTAL:
            return sum(widths)
        return max(widths)

    @property
    def height(self) -> int:
        heights = (child.height for child in self.children)
        if self.orientation == StackLayout.VERTICAL:
            return sum(heights)
        return max(heights)

    def paint(self, image: Image) -> None:
        left = 0
        upper = 0
        for child in self.children:
            right = left + child.width
            lower = upper + child.height
            inner = image.crop((left, upper, right, lower))
            child.paint(inner)
            image.paste(inner, (left, upper))
            if self.orientation == StackLayout.HORIZONTAL:
                left += child.width
            else:
                upper += child.height
