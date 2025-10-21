# Task 7: Odd Sum

# asking the user for a starting value again
starting_value = int(input("Enter a number: "))

# empty total variable for later
total = 0

# for loop that counts by odds, so whenever "total" is adding i to itself, it is adding only odd numbers instead of every number.
for i in range(1, starting_value + 1, 2):
    total += i

# finally, print out the total
print(f"The sum of odd numbers from 1 to {starting_value} is {total}")

