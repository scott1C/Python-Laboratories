import json
import nltk
import os

nltk.download("punkt")
nltk.download("stopwords")

file_path = os.path.join(os.path.dirname(__file__), "tweets.json")


def remove_punctuation(words):
    return [word for word in words if word.isalnum()]


def t9(word, text):
    indices = [i + 1 for i, w in enumerate(text) if w == word and i + 1 < len(text)]
    words_after = [text[i] for i in indices]

    words_after = remove_punctuation(words_after)

    fdist = nltk.FreqDist(words_after)
    most_common_words_after = fdist.most_common(3)

    return most_common_words_after


s = []
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)
for i in range(len(data)):
    s.append(data[i]["text"])
my_s = " ".join(s)
my_s = my_s.lower()

words = nltk.word_tokenize(my_s)

word = input("Enter your word: ")

most_common_words_after = t9(word, words)

print(f"The top 3 most common words after '{word}':")
for word, count in most_common_words_after:
    print(f"{word}: {count}")
