import numpy as np


def game_simulation():
    X = np.random.uniform(0, 1)
    i = 0
    while True:
        Y = np.random.uniform(0, 1)
        if Y > X:
            return i
        i += 1


num_trials = int(input("Enter the num of simulations: "))
results = [game_simulation() for _ in range(num_trials)]
print(f"The average fee is: {np.mean(results):.3f}")
