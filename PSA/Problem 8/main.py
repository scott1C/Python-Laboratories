import random


def simulate_experiment(num_people, num_trials):
    successes = 0
    for _ in range(num_trials):
        dinner = list(range(num_people))
        lunch = list(range(num_people))
        random.shuffle(dinner)
        random.shuffle(lunch)

        for i in range(num_people):
            if (
                dinner[(i - 1) % num_people] == lunch[(i - 1) % num_people]
                or dinner[(i + 1) % num_people] == lunch[(i + 1) % num_people]
                or dinner[(i + 1) % num_people] == lunch[(i - 1) % num_people]
                or dinner[(i - 1) % num_people] == lunch[(i + 1) % num_people]
            ):
                break
        else:
            successes += 1

    print(successes)
    return successes / num_trials


print(
    f"The probability that no two people sit next to each other at both lunch and dinner is: {simulate_experiment(100, 10000)}"
)