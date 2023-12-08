import random


def experiment_simulation(num_trials):
    d = 1
    s = 2 * d
    wins = 0

    for _ in range(num_trials):
        x = random.uniform(0, s)
        y = random.uniform(0, s)
        if d / 2 <= x <= s - d / 2 and d / 2 <= y <= s - d / 2:
            wins += 1

    return wins / num_trials


trials = int(input("Enter the num of tossing the coin: "))

print(
    f"This game is fair, because the probability to win is: {experiment_simulation(trials)}"
)
