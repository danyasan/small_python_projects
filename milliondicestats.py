"""Million Dice Roll Statistics Simulator

A simulation of one million dice rolls.
View this code at https://nostarch.com/big-book-small-python-projects
"""

import random, time
print("""Million Dice Roll Statistics Simulator
By Daniel Young

Enter how many six-sided dice you want to roll:""")
number_of_dice = int(input("> "))

# Set up a dictionary to store the results of each dice roll:
results = {i:0 for i in range(number_of_dice, (number_of_dice * 6) + 1)}

# Simulate dice rolls:
print(f"Simulating 1,000,000 rolls of {number_of_dice} dice...")
last_print_time = time.time()
for i in range(int(1E6)):
    if time.time() > last_print_time + 1:
        print(f"{round(i / 10000, 1)}% done...")
        last_print_time = time.time()

    total = 0
    for j in range(number_of_dice):
        total = total + random.randint(1, 6)
    results[total] = results[total] + 1

# Display results:
print("TOTAL - ROLLS - PERCENTAGE")
for i in range(number_of_dice, (number_of_dice*6) + 1):
    roll = results[i]
    percentage = round(results[i] / 10000, 1) # 1E6 / 1E2 = 1E4
    print(f"{i} - {roll} rolls - {percentage}%")

