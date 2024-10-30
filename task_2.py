import networkx as nx

G = nx.Graph()
nodes = ["Station A", "Station B", "Station C", "Station D", "Station E", "Station F"]
G.add_nodes_from(nodes)
edges = [
    ("Station A", "Station B"),
    ("Station A", "Station C"),
    ("Station B", "Station D"),
    ("Station C", "Station D"),
    ("Station D", "Station E"),
    ("Station E", "Station F"),
    ("Station C", "Station F")
]
G.add_edges_from(edges)

def dfs_path(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        return path
    for neighbor in graph.neighbors(start):
        if neighbor not in path:
            new_path = dfs_path(graph, neighbor, goal, path + [neighbor])
            if new_path:
                return new_path
    return None

def bfs_path(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for neighbor in graph.neighbors(vertex):
            if neighbor not in path:
                if neighbor == goal:
                    return path + [neighbor]
                else:
                    queue.append((neighbor, path + [neighbor]))
    return None

start = "Station A"
goal = "Station F"

dfs_result = dfs_path(G, start, goal)
bfs_result = bfs_path(G, start, goal)

print("DFS шлях:", dfs_result)
print("BFS шлях:", bfs_result)
