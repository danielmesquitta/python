row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input(
    "Where do you want to put the treasure (use two numbers to define x and y from 1 to 3, ex.: 12)? ")

x = int(position[0])
y = int(position[1])

selected_row = map[y - 1]
selected_row[x - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")
