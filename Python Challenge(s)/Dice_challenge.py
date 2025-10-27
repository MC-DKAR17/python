import random

# gets a user input for how many times they would like to roll the dice
user_input = int(input("How many times will you throw the dice?: "))

# empty array to store all the die values
total = []

# now, we iterate through 
for i in range(0, user_input):
    die_value = random.randint(1,6)
    print(f"Die {i+1}: {die_value}")
    total.append(die_value)

# takes the values from the array and adds them together, and then divide by
# the user input.
average_total = sum(total) / user_input

# printing out the average total of the dice
print(f"Average roll: {average_total}")
    
