from simple_alu import SimpleAlu


def part1(rows):
    alu = SimpleAlu(list(rows))
    number = int("9" * 14)
    while not valid(alu, number):
        if number % 1000 == 999:
            print(number)
        number -= 1
        while "0" in str(number):
            number -= 1
    return number


def part2(rows):
    pass


def valid(alu: SimpleAlu, number: int) -> bool:
    digits = [int(digit) for digit in str(number)]
    alu.run(digits)
    return alu.get("z") == 0
