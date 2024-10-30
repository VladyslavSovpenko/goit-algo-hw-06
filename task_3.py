import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

stations = ["Lepse", "Gavela", "Vidradniy", "Dontsa", "Harmatna", "Shulyavska"]
G.add_nodes_from(stations)

edges = [
    ("Lepse", "Gavela", 5),
    ("Lepse", "Vidradniy", 7),
    ("Gavela", "Dontsa", 3),
    ("Vidradniy", "Dontsa", 2),
    ("Dontsa", "Harmatna", 4),
    ("Harmatna", "Shulyavska", 6),
    ("Vidradniy", "Shulyavska", 5)
]
G.add_weighted_edges_from(edges)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', font_weight='bold')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Транспортна мережа з вагами")
plt.show()

def dijkstra_all_paths(graph, source):
    return nx.single_source_dijkstra_path_length(graph, source)

shortest_paths = {station: dijkstra_all_paths(G, station) for station in stations}

for start, paths in shortest_paths.items():
    print(f"Найкоротші шляхи від станції {start}:")
    for end, distance in paths.items():
        print(f"   до {end}: {distance} одиниць")
