from __future__ import annotations


def parse(input: str) -> Packet:
    bits = convert_hex(input)
    version, bits = get_int(bits, 3)
    type_id, bits = get_int(bits, 3)

    match type_id:
        case 4:
            return parse_literal(version, type_id, bits)
        case 6:
            return parse_operator(version, type_id, bits)


def convert_hex(input: str) -> str:
    return "".join(
        "{0:04b}".format(int(hex_digit, base=16)) for hex_digit in input
    )


def parse_literal(version: int, type_id: int, bits: int) -> LiteralPacket:
    parsing = 1
    binary = ""
    while parsing:
        parsing, bits = get_int(bits, 1)
        nybble, bits = split_at(bits, 4)
        binary += nybble
    value = int(binary, base=2)
    return LiteralPacket(version, type_id, value)


def parse_operator(version: int, type_id: int, bits: int) -> OperatorPacket:
    length_type_id, bits = get_int(bits, 1)
    if length_type_id:
        packets = fixed_number_of_packets(bits)
    else:
        packets = fixed_length_packets(bits)
    return OperatorPacket(version, type_id, packets)

def fixed_number_of_packets(bits: str) -> list[Packet]:
    pass

def fixed_length_packets(bits: str) -> list[Packet]:
    length, bits = get_int(bits, 15)
    data, bits = split_at(bits, length)
    packets = []
    # while data:
    #     packet, data = parse

def get_int(bits: str, index: int) -> tuple[int, str]:
    field, bits = split_at(bits, index)
    return int(field, base=2), bits


def split_at(bits: str, index: int) -> tuple[str, str]:
    return bits[:index], bits[index:]


class Packet():
    def __init__(self, version: int, type_id: int) -> None:
        self.version = version
        self.type_id = type_id


class LiteralPacket(Packet):
    def __init__(self, version: int, type_id: int, value: int) -> None:
        super().__init__(version, type_id)
        self.value = value


class OperatorPacket(Packet):
    def __init__(self, version: int, type_id: int, packets: list[Packet]) -> None:
        super().__init__(version, type_id)
