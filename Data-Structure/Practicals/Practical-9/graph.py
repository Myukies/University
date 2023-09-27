class Graph:
    def __init__(self):
        self.graph = {}

    def insert_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def insert_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)

    def delete_vertex(self, vertex):
        if vertex in self.graph:
            del self.graph[vertex]
            for v in self.graph:
                self.graph[v] = [vtx for vtx in self.graph[v] if vtx != vertex]

    def delete_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].remove(vertex2)
            self.graph[vertex2].remove(vertex1)

    def traverse(self):
        for vertex, neighbors in self.graph.items():
            print(f"Vertex: {vertex}, Neighbors: {neighbors}")

if __name__ == "__main__":
    graph = Graph()

    while True:
        print("\nGraph Menu:")
        print("1. Insert a vertex")
        print("2. Insert an edge")
        print("3. Delete a vertex")
        print("4. Delete an edge")
        print("5. Traverse the graph")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            vertex = input("Enter the vertex: ")
            graph.insert_vertex(vertex)
            print(f"Vertex {vertex} inserted into the graph.")

        elif choice == "2":
            vertex1 = input("Enter the first vertex: ")
            vertex2 = input("Enter the second vertex: ")
            graph.insert_edge(vertex1, vertex2)
            print(f"Edge between {vertex1} and {vertex2} inserted into the graph.")

        elif choice == "3":
            vertex = input("Enter the vertex to delete: ")
            graph.delete_vertex(vertex)
            print(f"Vertex {vertex} deleted from the graph.")

        elif choice == "4":
            vertex1 = input("Enter the first vertex: ")
            vertex2 = input("Enter the second vertex: ")
            graph.delete_edge(vertex1, vertex2)
            print(f"Edge between {vertex1} and {vertex2} deleted from the graph.")

        elif choice == "5":
            print("\nGraph:")
            graph.traverse()

        elif choice == "6":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please choose a valid option.")
