import re
from math import sqrt


def part1(data):
    _, (y_min, _) = get_positions(data)
    speed = abs(y_min) - 1
    return speed * (speed + 1) // 2


def part2(data):  # sourcery skip: use-assigned-variable
    (x_min, x_max), (y_min, y_max) = get_positions(data)
    vx_min = int(sqrt(2 * x_min))
    vx_max = x_max
    vy_min = y_min
    vy_max = abs(y_min) - 1
    initial_velocities = set()
    for vx0 in range(vx_min, vx_max + 1):
        for vy0 in range(vy_min, vy_max + 1):
            vx = vx0
            vy = vy0
            x, y = 0, 0
            while x <= x_max and y >= y_min:
                if x >= x_min and y <= y_max:
                    initial_velocities.add((vx0, vy0))
                x += vx
                y += vy
                vx = max(0, vx - 1)
                vy -= 1
    return len(initial_velocities)


def get_positions(data):
    match = re.match(r"target area: x=(\d+)..(\d+), y=-(\d+)..-(\d+)", data)
    x0, x1, y0, y1 = match.groups()
    x_min = int(x0)
    x_max = int(x1)
    y_min = -int(y0)
    y_max = -int(y1)
    return (x_min, x_max), (y_min, y_max)
