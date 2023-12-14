import os

file_path = os.path.join(os.path.dirname(__file__), "interests.txt")


def analyze_interests(title, interests_file):
    with open(interests_file, "r") as file:
        interests = [line.strip() for line in file]

    title_words = title.lower().split()

    matching_interests = set()
    for interest in interests:
        for word in title_words:
            if word in interest.lower():
                matching_interests.add(interest)

    return matching_interests


book_title = "From T-Rex to Multi Universes: How the Internet has Changed Politics, Art and Cute Cats."
result = analyze_interests(book_title, file_path)

print("The book is marketable to the following interests:")
for interest in result:
    print(interest)
