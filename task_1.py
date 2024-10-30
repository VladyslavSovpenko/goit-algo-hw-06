import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

nodes = ["Lepse", "Gavela", "Vidradniy", "Dontsa", "Harmatna", "Shulyavska"]
G.add_nodes_from(nodes)

edges = [
    ("Lepse", "Gavela"),
    ("Lepse", "Vidradniy"),
    ("Gavela", "Dontsa"),
    ("Vidradniy", "Dontsa"),
    ("Dontsa", "Harmatna"),
    ("Harmatna", "Shulyavska"),
    ("Vidradniy", "Shulyavska")
]
G.add_edges_from(edges)

plt.figure(figsize=(10, 6))
nx.draw_networkx(G, with_labels=True, node_color='skyblue', edge_color='gray', node_size=2000, font_size=15)
plt.title("Local Network Graph")
plt.show()

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_dict = dict(G.degree())

print(f"Кількість вузлів: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступені вершин:")
for node, degree in degree_dict.items():
    print(f"{node}: {degree}")
