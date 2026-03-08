from collections import deque

def bfs_shortest_path(graph, start, goal):
    visited = set()
    queue = deque([start])
    parent = {start: None}

    while queue:
        node = queue.popleft()

        if node == goal:
            break

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                queue.append(neighbor)

    # Reconstruct path
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent.get(current)

    path.reverse()

    if path[0] == start:
        return path
    else:
        return None


# Graph creation
graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node: ")
    neighbors = input("Enter neighbors separated by space: ").split()
    graph[node] = neighbors

start = input("Enter start node: ")
goal = input("Enter goal node: ")

path = bfs_shortest_path(graph, start, goal)

if path:
    print("\nShortest Path:", " -> ".join(path))
    print("Distance:", len(path) - 1)
else:
    print("No path found")
