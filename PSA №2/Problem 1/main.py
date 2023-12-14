import numpy as np

lambda_ = 1 / 10
num_simulations = 100000

waiting_times = np.random.exponential(scale=1 / lambda_, size=num_simulations)

average_waiting_time = np.mean(waiting_times)

print(f"Average waiting time: {average_waiting_time} minutes")
