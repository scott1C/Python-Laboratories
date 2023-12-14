import random
import math

num_darts = int(input("Enter the num of darts: "))

right_half = 0
less_than_five = 0
greater_than_five = 0
within_five_of_point = 0

for _ in range(num_darts):
    x = random.uniform(-10, 10)
    y = random.uniform(0, 10)

    if x > 0:
        right_half += 1

    distance = math.sqrt(x**2 + y**2)
    if distance < 5:
        less_than_five += 1
    elif distance > 5:
        greater_than_five += 1

    distance_from_point = math.sqrt(x**2 + (y - 5) ** 2)
    if distance_from_point < 5:
        within_five_of_point += 1

prob_right_half = right_half / num_darts
prob_less_than_five = less_than_five / num_darts
prob_greater_than_five = greater_than_five / num_darts
prob_within_five_of_point = within_five_of_point / num_darts

print("Probability it lands in the right half of the target: ", prob_right_half)
print(
    "Probability its distance from the centre is less than 5 inches: ",
    prob_less_than_five,
)
print(
    "Probability its distance from the centre is greater than 5 inches: ",
    prob_greater_than_five,
)
print(
    "Probability it lands within 5 inches of the point (0, 5): ",
    prob_within_five_of_point,
)
