from packet import Packet, parse


def part1(data: str) -> int:
    packet = parse(data)
    return sum_of_versions(packet)


def part2(data):
    pass


def sum_of_versions(packet: Packet):
    return packet.version + sum(
        sum_of_versions(inner)
        for inner
        in packet.packets
    )
