import json
import nltk
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download("punkt")
nltk.download("stopwords")

file_path_tweets = os.path.join(os.path.dirname(__file__), "tweets.json")
file_path_afinn = os.path.join(os.path.dirname(__file__), "AFINN-111.txt")
file_path_values = os.path.join(os.path.dirname(__file__), "emotional-values.txt")


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

with open(file_path_values, "w", encoding="utf-8") as result_file:
    for tweet in tweets:
        tweet_id = tweet["id"]
        tweet_text = tweet["text"]

        emotional_value = compute_emotional_value(tweet_text, afinn_dict)
        result_file.write(f"{tweet_id}\t{emotional_value}\n")
