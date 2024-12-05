import random

def main_loop(sequence):

    print(f"The possible colours are {colours}.")

    guess_count = 1

    while guess_count <= 12:

        guess = input("Please guess a sequence of colours (ex. 'RGBY'): ")

        correct_exact = check_exact(guess)
        correct_colours = check_colours(guess) - correct_exact

        if correct_exact == 4:
            print(f"You win - you guessed the sequence! It was {sequence}.")
            break

        print(f"\nGuess {guess_count}:")
        print(f"{correct_exact} of your colours are correct and in the right position.")
        print(f"{correct_colours} of your colours are correct but in the wrong position.\n")

        guess_count += 1

    if guess_count > 12:
        print(f"You lose - you didn't guess the sequence! It was {sequence}.")

def check_exact(guess):
    count = 0
    for i in range(len(guess)):
        if guess[i] == sequence[i]:
            count += 1

    return count

def check_colours(guess):
    count = 0
    counted_colours = []
    for i in range(len(guess)):
        for j in range(len(sequence)):
            if guess[i] == sequence[j] and j not in counted_colours:
                count += 1
                counted_colours.append(j)
                break

    return count

colours = ["R", "G", "B", "Y", "O", "P"]

sequence = ""
for _ in range(4):
    sequence += random.choice(colours)

main_loop(sequence)