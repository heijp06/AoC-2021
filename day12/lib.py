from collections import defaultdict


def part1(rows: list[str]) -> int:
    return part(rows, 1)


def part2(rows: list[str]) -> int:
    return part(rows, 2)


def part(rows: list[str], number: int) -> int:
    connections = defaultdict(list)
    for row in rows:
        cave1, cave2 = row.split("-")
        connections[cave1].append(cave2)
        connections[cave2].append(cave1)
    twice = set() if number == 1 else {
        cave
        for cave in connections
        if cave.islower() and cave not in ["start", "end"]
    }
    routes = [
        ("start", {"start"}, twice)
    ]
    count = 0
    while routes:
        new_routes = []
        for current, visited, twice in routes:
            for cave in connections[current]:
                if cave == "end":
                    count += 1
                elif cave.isupper():
                    new_routes.append((cave, visited, twice))
                elif cave in visited:
                    if cave in twice:
                        new_routes.append((cave, visited, set()))
                else:
                    new_visited = visited.copy()
                    new_visited.add(cave)
                    new_routes.append((cave, new_visited, twice))
        routes = new_routes
    return count
