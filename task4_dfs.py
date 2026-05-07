graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

visited = []

def dfs(node, goal, path):
    path.append(node)
    visited.append(node)

    if node == goal:
        print("DFS Path:", path)
        return True

    for neighbour in graph[node]:
        if neighbour not in visited:
            if dfs(neighbour, goal, path):
                return True

    return False

dfs('A', 'F', [])