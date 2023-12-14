import json
import nltk
import os
import matplotlib.pyplot as plt

nltk.download("punkt")

file_path = os.path.join(os.path.dirname(__file__), "tweets.json")

with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

tweets = dict()
dates = list()

for i in range(len(data)):
    tweets[data[i]["text"]] = data[i]["created_at"]

word = input("Enter the word: ")
keys = list(tweets.keys())

for key in keys:
    if word in key:
        dates.append(tweets[key])

dates = [dates[i].split("-") for i in range(len(dates))]

months = [(dates[i][0], dates[i][1]) for i in range(len(dates))]

xy = {i: 0 for i in months}

for i in months:
    xy[i] += 1

x_list = [i for i in range(len(list(xy.keys())))]
y_list = list(xy.values())

list_of_months = []
m = list(xy.keys())
for year, month in m:
    list_of_months.append(f"{year}-{month}")

plt.figure(figsize=(10, 6))
plt.title("Word usage per months")
plt.xticks(x_list, list_of_months)
plt.bar(x_list, y_list)
plt.show()
