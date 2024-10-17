import networkx as nx        
import matplotlib.pyplot as plt
from collections import deque
import time

# Define the graph
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
    nodes_explored = 0  # Count of nodes explored

    while queue:
        path = queue.popleft()  # Get the first path from the queue
        current = path[-1]  # Get the last node in the current path

        nodes_explored += 1  # Increment the explored nodes count

        if current == goal:
            return path, nodes_explored  # Return the path and the nodes explored

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)  # Mark the neighbor as visited
                new_path = path + [neighbor]  # Create a new path
                queue.append(new_path)  # Add the new path to the queue

    return None, nodes_explored  # Return None if no path is found

# DFS function to find the path from source to destination
def depth_first_search(graph, source, destination):
    stack = [(source, [source])]
    visited = set()  # Track visited nodes
    nodes_explored = 0  # Count of nodes explored

    while stack:
        (node, path) = stack.pop()  # Get the current node and path
        if node in visited:
            continue  # Skip already visited nodes
        visited.add(node)
        nodes_explored += 1  # Increment the explored nodes count
        if node == destination:
            return path, nodes_explored  # Return the path and the nodes explored
        for neighbor in graph[node]:
            stack.append((neighbor, path + [neighbor]))  # Add new path to the stack
    return None, nodes_explored  # Return None if no path is found

# Run BFS and measure time
start_time_bfs = time.time()
bfs_path, bfs_explored = breadth_first_search(graph, "Mahavir Nagar", "MVLU")
bfs_time = time.time() - start_time_bfs

# Run DFS and measure time
start_time_dfs = time.time()
dfs_path, dfs_explored = depth_first_search(graph, "Mahavir Nagar", "MVLU")
dfs_time = time.time() - start_time_dfs

# Output results
print("BFS Path:", bfs_path)
print("BFS Time:", bfs_time, "seconds")
print("BFS Nodes Explored:", bfs_explored)

print("\nDFS Path:", dfs_path)
print("DFS Time:", dfs_time, "seconds")
print("DFS Nodes Explored:", dfs_explored)

# Create and draw the graph
G = nx.DiGraph(graph)  # Create a directed graph
pos = nx.spring_layout(G, seed=75)  # Position the nodes using a spring layout

# Draw BFS path if found
if bfs_path:
    path_edges_bfs = list(zip(bfs_path, bfs_path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges_bfs, edge_color='red', width=2)  # Highlight BFS path

# Draw DFS path if found
if dfs_path:
    path_edges_dfs = list(zip(dfs_path, dfs_path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges_dfs, edge_color='blue', width=2)  # Highlight DFS path

# Draw all nodes and edges in the graph
nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue',
        font_size=10, font_weight='bold', edge_color='gray')

# Create a legend for the graph
plt.legend(handles=[
    plt.Line2D([0], [0], color='gray', label='Normal Path'),
    plt.Line2D([0], [0], color='red', label='BFS Path'),
    plt.Line2D([0], [0], color='blue', label='DFS Path')
], loc='upper right')

# Show the plot
plt.show()
