graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 6)],
    'C': [('F', 2)],
    'D': [],
    'E': [('G', 1)],
    'F': [('G', 4)],
    'G': []
}
heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 5,
    'E': 1,
    'F': 2,
    'G': 0
}

def a_star(start, goal):
    open_list = [start]
    closed_list = []
    g_cost = {start: 0}
    parent = {start: start}

    while open_list:
        current = open_list[0]

        for node in open_list:
            if g_cost[node] + heuristic[node] < g_cost[current] + heuristic[current]:
                current = node

        if current == goal:
            path = []
            while parent[current] != current:
                path.append(current)
                current = parent[current]

            path.append(start)
            path.reverse()
            print("Shortest path:", path)
            return

        open_list.remove(current)
        closed_list.append(current)

        for neighbor, cost in graph[current]:
            if neighbor in closed_list:
                continue

            new_cost = g_cost[current] + cost

            if neighbor not in open_list:
                open_list.append(neighbor)

            g_cost[neighbor] = new_cost
            parent[neighbor] = current

a_star('A', 'G')
