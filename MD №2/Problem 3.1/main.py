import os

file_path = os.path.join(os.path.dirname(__file__), "matrix.txt")


def find_person_with_most_friends(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    names = [name.strip() for name in lines[0].split("|")]
    matrix = [
        [int(value) if value.strip().isdigit() else 0 for value in row.split()[2:]]
        for row in lines[1:]
    ]

    friend_sums = [sum(row) for row in matrix]

    max_friends_index = friend_sums.index(max(friend_sums))
    person_with_most_friends = names[max_friends_index]

    return person_with_most_friends


result = find_person_with_most_friends(file_path)
print(f"The person with the most friends is: {result}")
