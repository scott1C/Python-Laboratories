import random
import matplotlib.pyplot as plt


def three_dice_rolls():
    return random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)


def rolls_simulation(num_of_simulations):
    count_nines = 0
    count_tens = 0
    for _ in range(num_of_simulations):
        result = three_dice_rolls()
        if result == 9:
            count_nines += 1
        elif result == 10:
            count_tens += 1

    return count_nines, count_tens


num_of_simulations = int(input("Enter the wanted number of simulations: "))
count_nines, count_tens = rolls_simulation(num_of_simulations)
labels = ["Num of 9", "Num of 10"]
counts = [count_nines, count_tens]

plt.bar(labels, counts, color=["black", "red"])
plt.title("Occurrences of Sum 9 and Sum 10 in Three Dice Rolls")
plt.xlabel(f"From {num_of_simulations}")
plt.ylabel("Number of Occurrences")
plt.show()
