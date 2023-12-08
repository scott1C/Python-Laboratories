import random


def child_choice():
    return random.choice(["boy", "girl"])


def simulate_until_boy():
    num_children = 0
    while True:
        num_children += 1
        if child_choice() == "boy":
            break

    return num_children


def simulate_until_boy_and_girl():
    num_children = 0
    was_boy = False
    was_girl = False
    while True:
        num_children += 1
        if child_choice() == "boy":
            was_boy = True
        else:
            was_girl = True
        if was_boy and was_girl:
            break

    return num_children


num_trials = 100000
children_until_boy = sum(simulate_until_boy() for _ in range(num_trials))
children_until_boy_and_girl = sum(
    simulate_until_boy_and_girl() for _ in range(num_trials)
)
print(
    f"The average number of children to achive one boy is: {children_until_boy / num_trials}"
)
print(
    f"The average number of children to achieve at least one boy and at least one girl is: {children_until_boy_and_girl / num_trials}"
)
print(
    f"We have with {(children_until_boy_and_girl - children_until_boy) / num_trials} more children in average in the second case than in the first one"
)
