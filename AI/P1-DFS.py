import networkx as nx
import matplotlib.pyplot as plt
#SIDDHANT ATHAWALE T071
# Define the graph
unweighted_graph = {
    "Mahavir Nagar": ["satya Nagar Rd", "Boraspada Road"],
    "satya Nagar Rd": ["RM Bhattad Rd"],
    "RM Bhattad Rd": ["Dattapada Road"],
    "Dattapada Road": ["Western Express Hwy"],
    "Western Express Hwy": ["jijamata Rd"],
    "jijamata Rd": ["Nicolas Wadi Rd"],
    "Nicolas Wadi Rd": ["Old Nagardas Road"],
    "Old Nagardas Road": ["MVLU"],
    "MVLU": [],
    "Boraspada Road": ["New Link Road"],
    "New Link Road": ["Malad Marve Road"],
    "Malad Marve Road": ["Father Justin Dsouza Rd"],
    "Father Justin Dsouza Rd": ["Datta Mandir Road"],
    "Datta Mandir Road": ["Western Express Hwy"]
}

def depth_first_search(graph, source, destination):
    # Initialize stack for DFS
    stack = [(source, [source])]
    visited = set()  # Track visited nodes

    while stack:
        (node, path) = stack.pop()  # Get the current node and path
        if node in visited:
            continue  # Skip already visited nodes
        visited.add(node)
        if node == destination:
            return path  # Return the path if the destination is reached
        for neighbor in graph[node]:
            stack.append((neighbor, path + [neighbor]))  # Add new path to the stack
    return None  # Return None if no path is found

# Example usage: Find the path using DFS
dfs_path = depth_first_search(unweighted_graph, "Mahavir Nagar", "MVLU")

# Create a directed graph
G = nx.DiGraph(unweighted_graph)

# Draw the graph
pos = nx.spring_layout(G, seed=75)  # Position the nodes using a spring layout

# Adjust label positions
label_pos = {k: [v[0], v[1] - 0.06] for k, v in pos.items()}

# Draw all nodes and edges in the graph
nx.draw(G, pos, node_size=300, font_size=10, font_color='black', with_labels=False)
nx.draw_networkx_labels(G, label_pos, font_size=8, font_color='black')

# Highlight the path found by DFS
if dfs_path:
    # Convert the path into a list of edges
    path_edges = list(zip(dfs_path, dfs_path[1:]))

    # Draw the path with a blue color
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='b', width=2)
# Create a legend for the graph
plt.legend(handles=[
    plt.Line2D([0], [0], color='gray', label='Normal Path'),
    plt.Line2D([0], [0], color='blue', label='DFS Path')
], loc='upper right')
# Show the plot
plt.show()
