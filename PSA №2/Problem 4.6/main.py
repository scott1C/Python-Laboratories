import json
import nltk
import os

nltk.download("punkt")

file_path = os.path.join(os.path.dirname(__file__), "tweets.json")


def get_word_suggestions(input_word, words, fdist):
    suggestions = [
        word
        for word, freq in fdist.items()
        if word.startswith(input_word) and word != input_word
    ]
    suggestions = sorted(suggestions, key=lambda x: fdist[x], reverse=True)[:3]
    return suggestions


s = []
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)
for i in range(len(data)):
    s.append(data[i]["text"])
my_s = " ".join(s)
my_s = my_s.lower()
words = nltk.word_tokenize(my_s)
words = [word for word in words if word.isalnum() and word != "https"]

fdist = nltk.FreqDist(words)

input_word = input("Enter an uncompleted word: ")

suggestions = get_word_suggestions(input_word, words, fdist)
print(f"\nWord Suggestions for '{input_word}':")
for suggestion in suggestions:
    print(f"{suggestion}: {fdist[suggestion]}")
