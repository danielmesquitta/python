import random

string = input(
    "Type a list of names, separated by commas like \"Pedro, João, Maria\": ")

names = string.split(',')

names = list(map(lambda word: word.strip(), names))

max_index = len(names) - 1

random_index = random.randint(0, max_index)

print(names[random_index])
