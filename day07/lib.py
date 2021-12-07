from collections import Counter


def part1(data):
    return go(data, lambda distance: distance)


def part2(data):
    return go(data, lambda distance: distance * (distance + 1) // 2)


def go(data, cost_func):
    counts = Counter(data)
    end = max(data)
    min_cost = None
    for pos in range(end + 1):
        cost = 0
        for crab_pos, count in counts.items():
            distance = abs(crab_pos - pos)
            cost += count * cost_func(distance)
        if min_cost is None or cost < min_cost:
            min_cost = cost
    return min_cost
