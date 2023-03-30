scores = input("Input a list of scores separated by comma: ").split(',')

scores = list(map(lambda word: float(word.strip()), scores))

highest_score = max(scores)

print("The highest score is:", highest_score)
