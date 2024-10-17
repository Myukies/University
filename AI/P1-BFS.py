import networkx as nx        
import matplotlib.pyplot as plt
from collections import deque
#SIDDHANT ATHAWALE T071
graph = {
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

# BFS function to find the shortest path from source to goal
def breadth_first_search(graph, source, goal):
    queue = deque([[source]])  # Initialize the queue with the source path
    visited = {source}  # Track visited nodes

    while queue:
        path = queue.popleft()  # Get the first path from the queue
        current = path[-1]  # Get the last node in the current path

        if current == goal:
            return path  # Return the path if the goal is reached

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)  # Mark the neighbor as visited
                new_path = path + [neighbor]  # Create a new path
                queue.append(new_path)  # Add the new path to the queue
            else:
                print("visited:", new_path)  # Print visited paths (for debugging)

    return None  # Return None if no path is found

# Run BFS to get the shortest path from "Mahavir Nagar" to "MVLU"
bfs_path = breadth_first_search(graph, "Mahavir Nagar", "MVLU")

# Create and draw the graph
G = nx.DiGraph(graph)  # Create a directed graph
pos = nx.spring_layout(G, seed=75)  # Position the nodes using a spring layout
nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue',
        font_size=10, font_weight='bold', edge_color='gray')

# Highlight the BFS path on the graph
if bfs_path:
    path_edges = list(zip(bfs_path, bfs_path[1:]))  # Create a list of edges in the path
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)  # Highlight the path edges in red
    nx.draw_networkx_nodes(G, pos, nodelist=bfs_path, node_color='red', node_size=500)  # Highlight the path nodes in red

# Create a legend for the graph
plt.legend(handles=[
    plt.Line2D([0], [0], color='gray', label='Normal Path'),
    plt.Line2D([0], [0], color='red', label='BFS Path')
], loc='upper right')

# Show the plot
plt.show()
