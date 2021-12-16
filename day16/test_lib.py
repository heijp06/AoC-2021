import pytest
from lib import part1, part2
from packet import parse

@pytest.mark.parametrize(["data", "expected"], (
    ("8A004A801A8002F478", 16),
    ("620080001611562C8802118E34", 12),
    ("C0015000016115A2E0802F182340", 23),
    ("A0016C880162017C3686B18A3D4780", 31)
))
def test_part1(data, expected):
    assert part1(data) == expected

@pytest.mark.parametrize(["data", "expected"], (
    ("C200B40A82", 3),
    ("04005AC33890", 54),
    ("880086C3E88112", 7),
    ("CE00C43D881120", 9),
    ("D8005AC2A8F0", 1),
    ("F600BC2D8F", 0),
    ("9C005AC2F8F0", 0),
    ("9C0141080250320F1802104A08", 1),
))
def test_part2(data, expected):
    assert part2(data) == expected

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