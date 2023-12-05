import random


def experiment_simulation(num_simulations):
    successful_trials = 0
    for _ in range(num_simulations):
        # We break the stick into two parts
        break1 = random.random()
        piece1 = min(break1, 1 - break1)
        piece2 = 1 - piece1
        # We break the longer part into two parts at one random point
        break2 = piece2 * random.random()
        piece3 = min(break2, 1 - break2)
        piece4 = 1 - piece3

        if (
            piece1 + piece3 > piece4
            and piece3 + piece4 > piece1
            and piece1 + piece4 > piece3
        ):
            successful_trials += 1

    return successful_trials


trials = int(input("Enter the total num of simulations: "))
print(
    f"The probability to that the three pieces can be used to form a triangle is: {experiment_simulation(trials) / trials}"
)
