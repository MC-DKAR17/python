# Task 3: Countdown Display

# The starting value that the user gets to choose from an input
starting_value = int(input("Enter starting number: "))

# for loop that takes the user inputted number and starts that off as the starting value

# then, the loop goes down from the starting value until 0 is reached.
for i in range(starting_value, 0, -1):
    print(i)

# once 0 is reached, this will print
print("Liftoff!")