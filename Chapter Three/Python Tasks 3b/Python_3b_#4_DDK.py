# Task 4: Sum Calculator

# starting with the total being at 0
total = 0

# starting value (or maximum value technically)
starting_value = int(input("Enter a number: "))

# for loop that starts at 0, and then the maximum spot is starting_value + one.

# the plus one is there so that the calculations won't be inaccurate.
for i in range(0, starting_value + 1):
    total += i

# once all calculations are done, print out the range chosen from 1 to the starting value. then the total is printed.
print(f"The sum of numbers 1 to {starting_value} is {total}")