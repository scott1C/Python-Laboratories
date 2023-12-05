import random

def simulate_election(republican_votes, democratic_votes, sample_size, simulations):
    successful_predictions = 0
    for _ in range(simulations):
        sample = random.choices(['R', 'D'], weights=[republican_votes, democratic_votes], k=sample_size)
        republican_sample_votes = sample.count('R')
        democratic_sample_votes = sample.count('D')
        if (republican_sample_votes > democratic_sample_votes and republican_votes > democratic_votes
                or democratic_sample_votes > republican_sample_votes and democratic_votes > republican_votes):
            successful_predictions += 1
    return successful_predictions


print(f"There are {simulate_election(48, 52, 1000, 100)} correct predictions from {100}. It's 48%/52% split. With a sample of size 1000.")
print(f"There are {simulate_election(49, 51, 1000, 100)} correct predictions from {100}. It's 49%/51% split. With a sample of size 1000.")
print(f"There are {simulate_election(48, 52, 3000, 100)} correct predictions from {100}. It's 48%/52% split. With a sample of size 3000.")
print(f"There are {simulate_election(49, 51, 3000, 100)} correct predictions from {100}. It's 49%/51% split. With a sample of size 3000.")
