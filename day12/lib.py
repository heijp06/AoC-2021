from collections import defaultdict

def part1(rows: list[str]) -> int:
    connections = defaultdict(list)
    for row in rows:
        cave1, cave2 = row.split("-")
        connections[cave1].append(cave2)
        connections[cave2].append(cave1)
    routes = [("start", {"start"})]
    count = 0
    while routes:
        new_routes = []
        for (current, visited) in routes:
            for cave in connections[current]:
                if cave == "end":
                    count += 1
                elif cave.isupper():
                    new_routes.append((cave, visited.copy()))
                elif cave not in visited:
                    new_visited = visited.copy()
                    new_visited.add(cave)
                    new_routes.append((cave, new_visited))
        routes = new_routes
    return count
                


def part2(rows):
    pass
