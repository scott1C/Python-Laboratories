import random

MAX_ATTEMPTS = 10

colors = [
    "red",
    "blue",
    "green",
    "yellow",
    "black",
    "white",
]


def colors_randomizer():
    length = int(input("Enter your desired length: "))
    if length > len(colors):
        print(f"Enter a length which is less or equal to {len(colors)}")
        return colors_randomizer()
    return random.sample(colors, length)


def mastermind_simulation(colors, tries=0):
    while tries <= MAX_ATTEMPTS:
        corectGuesses = 0
        correctPositions = 0

        guess_input = input("Enter your guess (space-separated colors): ").lower()
        guess = guess_input.split()
        if len(guess) != len(colors):
            print(
                f"You should enter a fixed number of colors, in this case it is: {len(colors)}!"
            )
            return mastermind_simulation(colors, tries)

        tries += 1
        for i in range(len(colors)):
            if guess[i] in colors:
                corectGuesses += 1
            if guess[i] == colors[i]:
                correctPositions += 1

        if correctPositions == len(colors):
            print(f"You have won after the {tries} attempts!")
            break
        else:
            print(
                f"You have guesed {corectGuesses} correct colors and {correctPositions} correct positions. Try again!"
            )
    else:
        print(f"You have exceeded the limit of the maximum attempts: {MAX_ATTEMPTS}!")


random_colors = colors_randomizer()
mastermind_simulation(random_colors)
