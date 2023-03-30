total_bill = float(input("What is the total bill? "))

total_percentage = float(
    input("What is the total percentage you want to add? "))

total_tip = total_bill * (1 + total_percentage / 100)

print(f"The total tip is {round(total_tip, 2)}")

people = int(input("How many people are splitting the bill? "))

total_per_person = total_tip / people

print(f"The total per person is {round(total_per_person, 2)}")
