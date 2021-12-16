import pytest
from lib import part1, part2
from packet import parse


def test_parse_1():
    data = "D2FE28"
    packet = parse(data)

    assert packet.version == 6
    assert packet.type_id == 4
    assert packet.value == 2021
    assert len(packet.packets) == 0

def test_parse_operator_1():
    data = "38006F45291200"
    packet = parse(data)

    assert packet.version == 1
    assert packet.type_id == 6
    assert len(packet.packets) == 2
    assert packet.packets[0].value == 10
    assert packet.packets[1].value == 20

def test_parse_operator_2():
    data = "EE00D40C823060"
    packet = parse(data)

    assert packet.version == 7
    assert packet.type_id == 3
    assert len(packet.packets) == 3
    assert packet.packets[0].value == 1
    assert packet.packets[1].value == 2
    assert packet.packets[2].value == 3