import networkx as nx
import matplotlib.pyplot as plt
#SIDDHANT ATHAWALE T071
# Define the graph nodes with weights
Graph_nodes = {
    "Mahavir Nagar": [("satya Nagar Rd", 6), ("Boraspada Road", 3)],
    "satya Nagar Rd": [("RM Bhattad Rd", 3)],
    "RM Bhattad Rd": [("Dattapada Road", 1)],
    "Dattapada Road": [("Western Express Hwy", 7)],
    "Western Express Hwy": [("jijamata Rd", 1)],
    "jijamata Rd": [("Nicolas Wadi Rd", 1)],
    "Nicolas Wadi Rd": [("Old Nagardas Road", 1)],
    "Old Nagardas Road": [("MVLU", 1)],
    "MVLU": [],
    "Boraspada Road": [("New Link Road", 8)],
    "New Link Road": [("Malad Marve Road", 4)],
    "Malad Marve Road": [("Father Justin Dsouza Rd", 6)],
    "Father Justin Dsouza Rd": [("Datta Mandir Road", 9)],
    "Datta Mandir Road": [("Western Express Hwy", 7)]
}

# Function to get neighbors with weights
def get_neighbors(v):
    """Return the neighbors of the given node with weights."""
    return Graph_nodes.get(v, [])

# Heuristic function
def h(n):
    """Return the heuristic distance to the goal for the given node."""
    H_dist = {
        'Mahavir Nagar': 10,
        'satya Nagar Rd': 8,
        'RM Bhattad Rd': 5,
        'Dattapada Road': 3,
        'Western Express Hwy': 6,
        'jijamata Rd': 5,
        'Nicolas Wadi Rd': 1,
        'Old Nagardas Road': 2,
        'MVLU': 0,
        'Boraspada Road': 7,
        'New Link Road': 4,
        'Malad Marve Road': 2,
        'Father Justin Dsouza Rd': 1,
        'Datta Mandir Road': 3
    }
    return H_dist.get(n, float('inf'))  # Return infinity if node not found

# A* algorithm implementation
def aStarAlgo(start_node, stop_node):
    """Perform the A* search algorithm."""
    open_set = {start_node}
    closed_set = set()
    g = {start_node: 0}
    parents = {start_node: start_node}

    while len(open_set) > 0:
        n = None
        for v in open_set:
            if n is None or g[v] + h(v) < g[n] + h(n):
                n = v
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            # Create a list of edges in the path
            path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
            print('Path found: {}'.format(path))
            print('Path edges: {}'.format(path_edges))  # Print the edges in the path
            return path

        open_set.remove(n)
        closed_set.add(n)

        for (m, weight) in get_neighbors(n):
            if m not in open_set and m not in closed_set:
                open_set.add(m)
                parents[m] = n
                g[m] = g[n] + weight  # Use the actual weight of the edge
            else:
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n
                    if m in closed_set:
                        closed_set.remove(m)
                        open_set.add(m)

    print('Path does not exist!')
    return None

# Run A* Search
path = aStarAlgo('Mahavir Nagar', 'MVLU')

# Create a directed graph
G = nx.DiGraph()

# Add nodes to the graph
for node in Graph_nodes:
    G.add_node(node)

# Add edges to the graph with weights
for node, neighbors in Graph_nodes.items():
    for neighbor, weight in neighbors:
        G.add_edge(node, neighbor, weight=weight)

# Use spring layout for better positioning
pos = nx.spring_layout(G, seed=75)  # Adjust k for better spacing
# Draw the graph without node labels
plt.figure(figsize=(12, 12))  # Increase figure size for clarity
nx.draw(G, pos, with_labels=False, node_color='lightblue', edge_color='gray', font_size=10)
# Highlight the path in red
if path:
    # Highlight nodes in the path
    red_nodes = nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='red', node_size=500)
    # Highlight edges in the path
    path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
    red_edges = nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)

    # Draw edge weights with smaller font size
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)  # Smaller font size
   
    # Add heuristic values as labels in the format 'Node_Name': Heuristic_Value
    heuristic_labels = {node: f"{node}: {h(node)}" for node in Graph_nodes}
    nx.draw_networkx_labels(G, pos, labels=heuristic_labels, font_color='black', verticalalignment='bottom', font_size=8)  # Smaller font size
# Set title and display the graph
plt.title('Graph Representation with A* Path Highlighted')
plt.axis('off')
plt.show()
