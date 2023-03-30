def average(number_list):
    return sum(number_list) / len(number_list)


string = input("Input a list of heights in cm separated by commas: ")

heights = string.split(',')

heights = list(map(lambda word: int(word.strip()), heights))

print(average(heights))
