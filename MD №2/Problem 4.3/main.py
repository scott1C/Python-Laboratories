import os
import json
import nltk
from nltk.tokenize import word_tokenize

nltk.download("punkt")

file_path_tweets = os.path.join(os.path.dirname(__file__), "tweets.json")
file_path_afinn = os.path.join(os.path.dirname(__file__), "AFINN-111.txt")


def load_afinn_dictionary():
    afinn_dict = {}
    with open(file_path_afinn, "r") as afinn_file:
        for line in afinn_file:
            word, score = line.strip().split("\t")
            afinn_dict[word] = int(score)
    return afinn_dict


def compute_emotional_value(text, afinn_dict):
    words = word_tokenize(text.lower())
    emotional_value = sum(afinn_dict.get(word, 0) for word in words)
    return emotional_value


afinn_dict = load_afinn_dictionary()

with open(file_path_tweets, "r", encoding="utf-8") as file:
    tweets = json.load(file)

tweet_emotional_values = [
    (tweet["id"], compute_emotional_value(tweet["text"], afinn_dict))
    for tweet in tweets
]

sorted_tweets = sorted(tweet_emotional_values, key=lambda x: x[1])

print("10 Most Positive Tweets:")
for tweet_id, emotional_value in sorted_tweets[-10:]:
    print(f"{tweet_id}: {emotional_value}")

print("\n10 Most Negative Tweets:")
for tweet_id, emotional_value in sorted_tweets[:10]:
    print(f"{tweet_id}: {emotional_value}")
