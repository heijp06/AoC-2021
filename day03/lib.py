def part1(rows):
    length = len(rows)
    binary = ""
    for column in zip(*rows):
        bits_set = sum(int(bit) for bit in column)
        binary += "1" if bits_set > length // 2 else "0"
    epsilon = int(binary, base=2)
    gamma = (1 << len(binary)) - epsilon - 1

    return epsilon * gamma


def part2(rows):
    pass
