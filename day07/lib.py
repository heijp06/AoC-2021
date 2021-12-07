from collections import Counter


def part1(data):
    end = max(data)
    crabs = [0] * (end + 1)
    cost = 0
    for crab in data:
        crabs[crab] += 1
        cost += crab
    min_cost = cost
    crabs_left = 0
    crabs_right = sum(crabs) - crabs[0]
    for pos in range(1, end + 1):
        cost += crabs_left + crabs[pos - 1] - crabs_right
        if cost < min_cost:
            min_cost = cost
        crabs_left += crabs[pos - 1]
        crabs_right -= crabs[pos]
    return min_cost


def part2(data):
    counts = dict(Counter(data))
    end = max(data)
    min_cost = None
    for pos in range(end + 1):
        cost = 0
        for crab_pos, count in counts.items():
            distance = abs(crab_pos - pos)
            cost += count * distance * (distance + 1) // 2
        if min_cost is None or cost < min_cost:
            min_cost = cost
    return min_cost
