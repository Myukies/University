from sys import maxsize
from itertools import permutations

def travelling_sales_person(graph, start_vertex):
    num_vertices = len(graph)
    vertex = [i for i in range(num_vertices) if i != start_vertex]
    min_path = maxsize
    next_permutations = permutations(vertex)

    for permutation in next_permutations:
        current_path_weight = 0
        current_vertex = start_vertex

        for next_vertex in permutation:
            current_path_weight += graph[current_vertex][next_vertex]
            current_vertex = next_vertex

        current_path_weight += graph[current_vertex][start_vertex]
        min_path = min(min_path, current_path_weight)

    return min_path

if __name__ == "__main__":
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    start_vertex = 0

    print(travelling_sales_person(graph, start_vertex))