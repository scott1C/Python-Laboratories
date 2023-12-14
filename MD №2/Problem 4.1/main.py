import json
from collections import Counter
import os

file_path = os.path.join(os.path.dirname(__file__), "tweets.json")


def extract_hashtags(text):
    return [word[1:] for word in text.split() if word.startswith("#")]


with open(file_path, "r", encoding="utf-8") as file:
    tweets = json.load(file)

all_hashtags = [
    hashtag for tweet in tweets for hashtag in extract_hashtags(tweet["text"])
]

hashtag_counts = Counter(all_hashtags)

print("10 Most Popular Hashtags:")
for hashtag, count in hashtag_counts.most_common(10):
    print(f"{hashtag}: {count} occurrences")
