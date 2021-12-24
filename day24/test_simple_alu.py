import pytest
from simple_alu import SimpleAlu
from lib import part1, part2
from itertools import product


@pytest.mark.parametrize(["register"], "wxyz")
def test_input(register):
    alu = SimpleAlu([f"inp {register}"])
    alu.run([42])

    assert alu.get(register) == 42
    assert_others_zero(register)


@pytest.mark.parametrize(["register1", "register2"], product("wxyz", repeat=2))
def test_add(register1, register2):
    alu = SimpleAlu([
        f"inp {register1}",
        f"inp {register2}",
        f"add {register1} {register2}"
    ])
    alu.run([1, 2])

    assert alu.get(register1) == (4 if register1 == register2 else 3)
    assert alu.get(register2) == (4 if register1 == register2 else 2)
    assert_others_zero(register1, register2)


@pytest.mark.parametrize(["register1", "register2"], product("wxyz", repeat=2))
def test_mul(register1, register2):
    alu = SimpleAlu([
        f"inp {register1}",
        f"inp {register2}",
        f"mul {register1} {register2}"
    ])
    alu.run([2, 3])

    assert alu.get(register1) == (9 if register1 == register2 else 6)
    assert alu.get(register2) == (9 if register1 == register2 else 3)
    assert_others_zero(register1, register2)


@pytest.mark.parametrize(["register1", "register2"], product("wxyz", repeat=2))
def test_div(register1, register2):
    alu = SimpleAlu([
        f"inp {register1}",
        f"inp {register2}",
        f"div {register1} {register2}"
    ])
    alu.run([-3, 2])

    assert alu.get(register1) == (1 if register1 == register2 else -1)
    assert alu.get(register2) == (1 if register1 == register2 else 2)
    assert_others_zero(register1, register2)


@pytest.mark.parametrize(["register1", "register2"], product("wxyz", repeat=2))
def test_mod(register1, register2):
    alu = SimpleAlu([
        f"inp {register1}",
        f"inp {register2}",
        f"mod {register1} {register2}"
    ])
    alu.run([16, 7])

    assert alu.get(register1) == (0 if register1 == register2 else 2)
    assert alu.get(register2) == (0 if register1 == register2 else 7)
    assert_others_zero(register1, register2)


@pytest.mark.parametrize(["register1", "register2"], product("wxyz", repeat=2))
def test_eql(register1, register2):
    alu = SimpleAlu([
        f"inp {register1}",
        f"inp {register2}",
        f"eql {register1} {register2}"
    ])
    alu.run([1, 2])

    assert alu.get(register1) == (1 if register1 == register2 else 0)
    assert alu.get(register2) == (1 if register1 == register2 else 2)
    assert_others_zero(register1, register2)


def assert_others_zero(alu: SimpleAlu, *registers: str) -> None:
    for register in registers:
        if register not in registers:
            assert register == 0
