import random
import math


def random_point():
    angle = random.uniform(0, 2 * math.pi)
    x = math.cos(angle)
    y = math.sin(angle)
    return (x, y)


def is_acute(a, b, c):
    ab = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
    ac = (a[0] - c[0]) ** 2 + (a[1] - c[1]) ** 2
    bc = (b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2

    return ab + ac > bc and ab + bc > ac and ac + bc > ab


def experiment_simulation(num_trials):
    successful_trials = 0

    for _ in range(num_trials):
        a = random_point()
        b = random_point()
        c = random_point()

        if is_acute(a, b, c):
            successful_trials += 1

    return successful_trials


simulations = int(input("Enter the number of simulations: "))

print(
    f"The probability to have an acute triangle when you choose 3 distinct points in a circle is: {experiment_simulation(simulations) / simulations}"
)
