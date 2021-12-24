from alu import Alu
from expressions import InputExpression

def test_input():
    alu = Alu()

    alu.parse(["inp w", "add y w"])

    assert alu.w.values == set(range(1, 10))
    assert alu.w.expression == InputExpression('A')
    assert alu.w == alu.y
