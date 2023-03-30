import random

words = ["apple", "banana", "cherry", "dragonfruit",
         "elderberry", "fig", "grape", "honeydew"]

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''',]


def select_word(words):
    word = random.choice(words)
    return word


def display_word(word, guesses):
    displayed_word = ""
    for letter in word:
        if letter in guesses:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word


def play_game():
    print("Welcome to Hangman!")

    word = select_word(words)

    guesses = set()

    num_guesses = 0

    max_guesses = 6

    while True:
        print(stages[num_guesses])

        print("Letters you have guessed:", guesses)

        print("Guess the word: ", display_word(word, guesses))

        guess = input("Enter a letter: ")

        if guess in guesses:
            print("You already guessed that letter. Try again!")

        else:
            guesses.add(guess)

            if guess in word:
                print("Good guess!")

            else:
                num_guesses += 1
                print("Sorry, that letter is not in the word.")

            if num_guesses >= max_guesses:
                print(stages[num_guesses])

                print("You lose! The word was", word)
                break

            elif set(word) <= guesses:
                print("Congratulations, you won!")
                break


play_game()
