import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
           "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
           "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

letters_num = int(input("How many letters do you want in your password? "))

symbols_num = int(input("How many symbols do you want in your password? "))

numbers_num = int(input("How many numbers do you want in your password? "))

password = "".join(map(lambda _: random.choice(letters), range(letters_num)))

password += "".join(
    map(lambda _: random.choice(symbols), range(symbols_num)))

password += "".join(
    map(lambda _: random.choice(numbers), range(numbers_num)))

password_as_list = list(password)

random.shuffle(password_as_list)

password = "".join(password_as_list)

print(password)
