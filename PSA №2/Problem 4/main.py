import json
import nltk
import os
from nltk.corpus import stopwords

nltk.download("punkt")
nltk.download("stopwords")

file_path = os.path.join(os.path.dirname(__file__), "tweets.json")


def t9(word, text):
    indices = [i + 1 for i, w in enumerate(text) if w == word and i + 1 < len(text)]
    words_after = [text[i] for i in indices]
    fdist = nltk.FreqDist(words_after)
    most_common_word_after = fdist.max()

    return most_common_word_after


s = []
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)
for i in range(len(data)):
    s.append(data[i]["text"])
my_s = " ".join(s)
my_s = my_s.lower()

words = nltk.word_tokenize(my_s)

words_for_t9 = words[:]

stop_words = set(stopwords.words("english"))
words = [
    word
    for word in words
    if word.isalnum() and word not in stop_words and word != "https"
]

fdist = nltk.FreqDist(words)

print(fdist.most_common(100))

word = input("Enter your word: ")

print(f"The most common words after it: {t9(word, words_for_t9)}")
