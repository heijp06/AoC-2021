import pytest
from display import Display


def test_init():
    display = Display(2, 5)
    assert display.width == 2
    assert display.height == 5


def test_width_positive():
    with pytest.raises(ValueError):
        display = Display(0, 5)


def test_height_positive():
    with pytest.raises(ValueError):
        display = Display(2, 0)


def test_clear():
    display = Display(2, 3)
    assert display.lines == [[" ", " "], [" ", " "], [" ", " "]]
    display.clear("*")
    assert display.lines == [["*", "*"], ["*", "*"], ["*", "*"]]


def test_set_item():
    display = Display(2, 3)
    display[0, 1] = "+"
    display[1, 0] = "-"
    display[1, 1] = "#"
    display[1, 1] = "="
    assert display.lines == [[" ", "-"], ["+", "="], [" ", " "]]


def test_get_item():
    display = Display(2, 3)
    display[0, 1] = "+"
    display[1, 0] = "-"
    display[1, 1] = "#"
    display[1, 1] = "="
    assert display[0, 0] == " "
    assert display[0, 1] == "+"
    assert display[0, 2] == " "
    assert display[1, 0] == "-"
    assert display[1, 1] == "="
    assert display[1, 2] == " "
