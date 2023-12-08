import random
import matplotlib.pyplot as plt


def coin_tosses_simulation(num_tosses=100, num_trials=1000):
    results = []
    for _ in range(num_trials):
        num_heads = sum(random.choice([0, 1]) for _ in range(num_tosses))
        results.append(num_heads)

    return results


def plot_graph(results):
    counts = [results.count(n) for n in range(35, 66)]
    plt.bar(range(35, 66), counts)
    plt.xlabel("Number of heads")
    plt.ylabel("Number of cases")
    plt.title("Distribution of heads in coin tosses experiment")
    plt.show()


results = coin_tosses_simulation()
plot_graph(results)
