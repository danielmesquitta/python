import random
random_index = random.randint(0, 2)

options = [
    """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
]

selected_index = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

if (selected_index > 2 or selected_index < 0):
    print("You typed an invalid number, you lose!")
    exit()

print(options[selected_index])

print("Computer chose:")

print(options[random_index])

if (selected_index == 0 and random_index == 1):
    print("You lose!")
elif (selected_index == 0 and random_index == 2):
    print("You win!")
elif (selected_index == 1 and random_index == 0):
    print("You win!")
elif (selected_index == 1 and random_index == 2):
    print("You lose!")
elif (selected_index == 2 and random_index == 0):
    print("You lose!")
elif (selected_index == 2 and random_index == 1):
    print("You win!")
elif (selected_index == random_index):
    print("It's a draw!")
