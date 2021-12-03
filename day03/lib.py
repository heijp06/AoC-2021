def part1(rows):
    binary = "".join(get_bit(rows, index) for index in range(len(rows[0])))
    epsilon = int(binary, base=2)
    gamma = (1 << len(binary)) - epsilon - 1
    return epsilon * gamma


def part2(rows):
    oxygen = select_rating(rows, True)
    co2 = select_rating(rows, False)
    return oxygen * co2


def get_bit(rows, index, most_common=True):
    length = len(rows)
    column = list(zip(*rows))[index]
    bits_set = sum(int(bit) for bit in column)
    if most_common:
        return "1" if bits_set * 2 >= length else "0"
    return "0" if bits_set * 2 >= length else "1"


def select_rating(rows, most_common):
    selected_rows = list(rows)
    index = 0
    while len(selected_rows) > 1:
        bit = get_bit(selected_rows, index, most_common)
        selected_rows = [row for row in selected_rows if row[index] == bit]
        index += 1
    return int(selected_rows[0], base=2)
