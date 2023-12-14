import networkx as nx
import os

file_path = os.path.join(os.path.dirname(__file__), "matrix.txt")


def read_matrix_from_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    names = [name.strip() for name in lines[0].split("|")]
    matrix = [
        [int(value) if value.strip().isdigit() else 0 for value in row.split()[1:]]
        for row in lines[1:]
    ]

    return names, matrix


def compute_rating(matrix):
    graph = nx.Graph()

    for i, row in enumerate(matrix):
        graph.add_node(i)

    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix[i])):
            if matrix[i][j] == 1:
                graph.add_edge(i, j)

    ratings = {}

    for node in graph.nodes():
        total_points = 0

        shortest_paths = nx.single_source_dijkstra_path_length(graph, node)

        for other_node, distance in shortest_paths.items():
            if other_node != node:
                points_contributed = len(graph.nodes) - distance - 1
                total_points += points_contributed

        ratings[node] = total_points

    return ratings


names, matrix = read_matrix_from_file(file_path)

ratings = compute_rating(matrix)

for person, rating in zip(names, ratings.values()):
    print(f"{person}: Rating = {rating}")
