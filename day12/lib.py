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


def part2(rows: list[str]) -> int:
    connections = defaultdict(list)
    for row in rows:
        cave1, cave2 = row.split("-")
        connections[cave1].append(cave2)
        connections[cave2].append(cave1)
    routes = []
    for small in (cave for cave in connections.keys() if cave.islower() and cave not in ["start", "end"]):
        routes.append(("start", {"start"}, small, []))
    count = 0
    known_routes = set()
    while routes:
        new_routes = []
        for (current, visited, twice, route) in routes:
            for cave in connections[current]:
                new_route = route.copy()
                new_route.append(current)
                if cave == "end":
                    path = ",".join(new_route)
                    if path not in known_routes:
                        known_routes.add(path)
                        # print(path, ",end", sep="")
                        count += 1
                elif cave.isupper():
                    new_routes.append((cave, visited.copy(), twice, new_route))
                elif cave not in visited:
                    new_visited = visited.copy()
                    if cave == twice:
                        new_routes.append((cave, new_visited, "", new_route))
                    else:
                        new_visited.add(cave)
                        new_routes.append((cave, new_visited, twice, new_route))
        routes = new_routes
    return count
