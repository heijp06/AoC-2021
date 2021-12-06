from collections import defaultdict, Counter


def part1(input: list[int]) -> int:
    return go(input, 80)


def part2(input):
    return go(input, 256)


def go(input, days):
    fish = dict(Counter(input))
    for _ in range(days):
        new_fish = defaultdict(int)
        for age, number in fish.items():
            if age:
                new_fish[age - 1] += number
            else:
                new_fish[6] += number
                new_fish[8] = number
        fish = new_fish
    return sum(fish.values())
