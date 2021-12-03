def part1(rows):
    binary = ""
    for index in range(len(rows[0])):
        binary += get_bit(rows, index)

    epsilon = int(binary, base=2)
    gamma = (1 << len(binary)) - epsilon - 1

    return epsilon * gamma

def get_bit(rows, index, most_common = True):
    length = len(rows)
    column = list(zip(*rows))[index]
    bits_set = sum(int(bit) for bit in column)
    if most_common:
        return "1" if bits_set * 2 >= length else "0"
    return "0" if bits_set * 2 >= length else "1"


def part2(rows):
    oxygen_rows = list(rows)
    index = 0
    while len(oxygen_rows) > 1:
        bit = get_bit(oxygen_rows, index, True)
        oxygen_rows = [row for row in oxygen_rows if row[index] == bit]
        index += 1
    
    co2_rows = list(rows)
    index = 0
    while len(co2_rows) > 1:
        bit = get_bit(co2_rows, index, False)
        co2_rows = [row for row in co2_rows if row[index] == bit]
        index += 1
    
    oxygen = int(oxygen_rows[0], base=2)
    co2 = int(co2_rows[0], base=2)

    return oxygen * co2
