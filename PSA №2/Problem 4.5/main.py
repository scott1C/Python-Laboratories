import json
import nltk
from nltk.corpus import stopwords
from collections import defaultdict
import os

nltk.download("stopwords")
nltk.download("punkt")

file_path = os.path.join(os.path.dirname(__file__), "tweets.json")


def check_the_popularity(word, tweets):
    appears = 0
    likes = 0
    reposts = 0

    for key in tweets.keys():
        if word in key.lower().split():
            appears += 1
            likes += int(tweets[key][0])
            reposts += int(tweets[key][1])

    if appears != 0:
        popularity = appears * (1.4 + reposts / appears) * (1.2 + likes / appears)
        return popularity
    else:
        return 0


wordss = defaultdict(int)
s = []

with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

tweets = dict()

for i in range(len(data)):
    tweets[data[i]["text"]] = [data[i]["likes"], data[i]["retweets"]]
    s.append(data[i]["text"])

my_s = " ".join(s)
my_s = my_s.lower()
words = nltk.word_tokenize(my_s)
stop_words = set(stopwords.words("english"))
words = [
    word
    for word in words
    if word.isalnum() and word not in stop_words and word != "https"
]

for word in words:
    wordss[word] += int(check_the_popularity(word, tweets))

sorted_wordss = dict(sorted(wordss.items(), key=lambda item: item[1], reverse=True))

top_10_words = list(sorted_wordss.keys())[:10]

print("Top 10 Most Popular Words:")
for word in top_10_words:
    print(f"{word}: {wordss[word]}")
