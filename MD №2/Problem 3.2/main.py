import os

file_path = os.path.join(os.path.dirname(__file__), "matrix.txt")


def sort_people_by_friends(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    names = [name.strip() for name in lines[0].split("|")]
    matrix = [
        [int(value) if value.strip().isdigit() else 0 for value in row.split()[1:]]
        for row in lines[1:]
    ]

    friend_sums = [sum(row) for row in matrix]

    people_and_friends = list(zip(names, friend_sums))

    sorted_people = sorted(people_and_friends, key=lambda x: x[1], reverse=True)

    return sorted_people


sorted_people = sort_people_by_friends(file_path)

for person, friend_count in sorted_people:
    print(f"{person}: {friend_count} friends")
