import json
import nltk
import os

nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")

file_path = os.path.join(os.path.dirname(__file__), "tweets.json")

s = []
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)
for i in range(len(data)):
    s.append(data[i]["text"])
my_s = " ".join(s)
my_s = my_s.lower()
words = nltk.word_tokenize(my_s)
pos_tags = nltk.pos_tag(words)
nouns = [
    word
    for word, pos_tag in pos_tags
    if pos_tag == "NNP" and word.isalnum() and word != "https"
]

fdist = nltk.FreqDist(nouns)

word_counts = fdist.most_common(10)

for word, count in word_counts:
    print(f"{word} {count}")
