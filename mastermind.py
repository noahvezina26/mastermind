import random

def main_loop(sequence):

    guess_count = 1

    while guess_count <= 12:

        guess = input("Please guess a sequence of colours (ex. 'RGBY'): ")

        correct_exact = check_exact(guess)
        correct_colours = check_colours(guess)

        if correct_exact == 4:
            print("You win - you guessed the sequence!")
            break

        print(f"Guess {guess_count}:")
        print(f"{correct_exact} of your colours are correct and in the right position.")
        print(f"{correct_colours} of your colours are correct but in the wrong position.\n")

        guess_count += 1

    if guess_count > 12:
        print(f"You lose - you didn't guess the sequence! It was {sequence}.")


def check_exact():
    pass


def check_colours():
    pass

    
colours = ["R", "G", "B", "Y", "O", "P"]

sequence = ""
for _ in range(4):
    sequence += random.choice(colours)

main_loop(sequence)