import pytest
from lib import part1, part2
from packet import parse


def test_parse_1():
    input = "D2FE28"
    packet = parse(input)

    assert packet.version == 6
    assert packet.type_id == 4
    assert packet.value == 2021

def test_parse_operator_1():
    input = "38006F45291200"
    packet = parse(input)

    assert packet.version == 1
    assert packet.type_id == 6
    # assert packet.packets[0].value == 10
    # assert packet.packets[1].value == 20