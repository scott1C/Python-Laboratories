import random


res = 0
sim = int(input("Enter number of simulation: "))

for i in range(sim):
    occuped = []
    places = list(range(100))
    que = list(range(100))
    random.shuffle(que)
    mapping = {i: que.pop() for i in range(100)}
    mapping[0] = random.randint(0, 99)

    for i in range(100):
        if mapping[i] in occuped:
            a = random.choice(places)
            places.remove(a)
            occuped.append(a)
        else:
            occuped.append(mapping[i])
            places.remove(mapping[i])

    if (occuped[len(occuped) - 1]) == mapping[99]:
        res += 1

print(f"The probability is {res/sim}")
