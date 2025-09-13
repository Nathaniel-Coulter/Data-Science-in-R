# Data Science Quiz 3: Question 1 (a)
# Nathaniel Coulter 

import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

nodes = ['v1', 'v2', 'v3', 'v4', 'v5']
G.add_nodes_from(nodes)

adj_matrix = [
    [0, 0, 0, 1, 0],  # v1
    [0, 0, 0, 1, 1],  # v2
    [0, 0, 0, 0, 1],  # v3
    [1, 1, 0, 0, 1],  # v4
    [0, 1, 1, 1, 0]   # v5
]

for i in range(5):
    for j in range(5):
        if adj_matrix[i][j] == 1:
            G.add_edge(nodes[i], nodes[j])

pos = nx.spring_layout(G, seed=42)  
nx.draw(G, pos, with_labels=True, node_color='lightblue', arrows=True, node_size=2000, font_size=14, arrowstyle='-|>')
nx.draw_networkx_edges(G, pos, arrows=True)
plt.title("Directed Graph from Adjacency Matrix")
plt.show()
