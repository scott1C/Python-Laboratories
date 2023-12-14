import networkx as nx
import os

file_path_interests = os.path.join(os.path.dirname(__file__), "interests.txt")
file_path_people_interests = os.path.join(
    os.path.dirname(__file__), "people_interests.txt"
)


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


import networkx as nx

with open(file_path_interests, "r") as file:
    interests = file.read().splitlines()

with open(file_path_people_interests, "r") as file:
    people_data = file.read().splitlines()

people_interests = [line.split(" : ")[1].split() for line in people_data]

matrix = [
    [1 if interest in person_interests else 0 for interest in interests]
    for person_interests in people_interests
]

ratings = compute_rating(matrix)

final_scores = [
    (people_data[i].split(" : ")[0], ratings[i] * 0.2 * sum(matrix[i]))
    for i in range(len(people_data))
]

final_scores.sort(key=lambda x: x[1], reverse=True)

top_5_people = final_scores[:5]
for name, score in top_5_people:
    print(f"{name}: {score}")
