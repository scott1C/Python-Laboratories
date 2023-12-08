import random


def experiment_simulation(num_trials):
    outcomes = ["taxatoare", "controlor", "nothing"]
    probabilites = [0.02, 0.05, 0.93]
    total_money = 0
    cost_per_ride = 6
    first_fine = 50
    second_fine = 200
    subsequent_fine = 300

    for _ in range(num_trials):
        sample = random.choices(outcomes, weights=probabilites, k=730)
        caught_by_controlor = sample.count("controlor")
        caught_by_taxatoare = sample.count("taxatoare")

        if caught_by_controlor == 1:
            total_money += 50
        elif caught_by_controlor == 2:
            total_money += 250
        elif caught_by_controlor >= 3:
            total_money += (
                (caught_by_controlor - 2) * subsequent_fine + second_fine + first_fine
            )
        total_money += caught_by_taxatoare * cost_per_ride

    return round(total_money / num_trials)


num_trials = int(input("Enter the number of simulations: "))
result = experiment_simulation(num_trials)
print(
    f"Total cost for Jora is: {result} lei, while for law-abiding students is: {730 * 6} lei"
)
