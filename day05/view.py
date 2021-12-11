from abc import ABC, abstractmethod
from PIL import Image  # type: ignore


class View(ABC):
    @property
    @abstractmethod
    def width(self) -> int:
        raise NotImplementedError()

    @property
    @abstractmethod
    def height(self) -> int:
        raise NotImplementedError()

    def paint(self, image: Image) -> None:
        raise NotImplementedError()
