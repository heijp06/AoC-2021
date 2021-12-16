from __future__ import annotations


def parse(data: str) -> Packet:
    parser = Parser(data)
    return parser.parse_packet()


class Parser:
    def __init__(self, data: str) -> None:
        self.set_bits(data)
        self.index = 0

    def parse_packet(self) -> Packet:
        version = self.get_int(3)
        type_id = self.get_int(3)

        if type_id == 4:
            return self.parse_literal(version, type_id)
        else:
            return self.parse_operator(version, type_id)

    def set_bits(self, data: str) -> str:
        self.bits = "".join(
            "{0:04b}".format(int(hex_digit, base=16)) for hex_digit in data
        )

    def get_int(self, length: int) -> int:
        field = self.get_string(length)
        return int(field, base=2)

    def get_string(self, length: int) -> str:
        start = self.index
        end = start + length
        self.index = end
        return self.bits[start:end]

    def parse_literal(self, version: int, type_id: int) -> LiteralPacket:
        parsing = 1
        binary = ""
        while parsing:
            parsing = self.get_int(1)
            nybble = self.get_string(4)
            binary += nybble
        value = int(binary, base=2)
        return LiteralPacket(version, type_id, value)

    def parse_operator(self, version: int, type_id: int) -> OperatorPacket:
        length_type_id = self.get_int(1)
        if length_type_id:
            packets = self.fixed_number_of_packets()
        else:
            packets = self.fixed_length_packets()
        return OperatorPacket(version, type_id, packets)

    def fixed_number_of_packets(self) -> list[Packet]:
        count = self.get_int(11)
        packets = []
        for _ in range(count):
            packet = self.parse_packet()
            packets.append(packet)
        return packets

    def fixed_length_packets(self) -> list[Packet]:
        length = self.get_int(15)
        packets = []
        stop = self.index + length
        while self.index < stop:
            packet = self.parse_packet()
            packets.append(packet)
        return packets

class Packet():
    def __init__(self, version: int, type_id: int) -> None:
        self.version = version
        self.type_id = type_id


class LiteralPacket(Packet):
    def __init__(self, version: int, type_id: int, value: int) -> None:
        super().__init__(version, type_id)
        self.value = value
        self.packets = []


class OperatorPacket(Packet):
    def __init__(self, version: int, type_id: int, packets: list[Packet]) -> None:
        super().__init__(version, type_id)
        self.packets = packets
