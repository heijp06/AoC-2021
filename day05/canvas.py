from view import View
from PIL import Image  # type: ignore


class Canvas:
    def __init__(self, view: View) -> None:
        self.view = view
        self.image_number = 0

    def paint(self) -> Image:
        image = Image.new("RGB", (self.view.width, self.view.height))
        self.view.paint(image)
        return image

    def save(self) -> None:
        image = self.paint()
        image.save(f"img/img{self.image_number:08d}.jpg")
        self.image_number += 1
