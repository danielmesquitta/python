import random


def play_game():
    print("Welcome to the Number Guessing Game!")

    numbers = range(1, 101)

    selected_number = random.choice(numbers)

    print("I'm thinking of a number between 1 and 100.")

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == "easy":
        guesses = 10
    else:
        guesses = 5

    while (guesses > 0):
        print(f"You have {guesses} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))

        if guess == selected_number:
            print(f"You got it! The answer was {selected_number}.")
            return

        if guess > selected_number:
            print("Too high.")
        else:
            print("Too low.")

        guesses -= 1

    print(
        f"You've run out of guesses, you lose. The answer was {selected_number}.")


while (True):
    play_game()

    play_again = input("Play again? (y/n) ").lower()

    if play_again != "y":
        break
