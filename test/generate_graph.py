import networkx as nx
import matplotlib.pyplot as plt
import random

# Define node and edge types
node_types = ['x', 'y', 'z']
edge_types = ['a', 'b', 'c']

# Create a directed graph with 25 nodes
G = nx.DiGraph()
num_nodes = 25

# Add nodes with random types
for i in range(num_nodes):
    node_type = random.choice(node_types)
    G.add_node(i, type=node_type)

# Add edges with random types
for i in range(num_nodes):
    for j in range(i + 1, num_nodes):
        if random.random() < 0.1:  # 20% chance to create an edge
            edge_type = random.choice(edge_types)
            G.add_edge(i, j, type=edge_type)

# Visualize the graph
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)

# Draw nodes with colors based on their types
node_colors = [random.choice(['skyblue', 'lightgreen', 'salmon']) for _ in range(num_nodes)]
nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=600, font_size=10, font_color="black")

# Draw edge labels for edge types
edge_labels = nx.get_edge_attributes(G, 'type')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="red")
plt.title("Graph with 25 Nodes and Edge/Node Types")

plt.show()