import pytest
from alu import Alu

@pytest.mark.parametrize("instructions", [
    ["inp w"],
    ["inp w", "mul w 0"]
])
def test_parse(instructions):
    alu = Alu()

    alu.parse(instructions)