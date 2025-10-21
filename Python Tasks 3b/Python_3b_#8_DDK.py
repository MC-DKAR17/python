# Task 8: Number Pattern

# first for loop to print out values from 1 to 10, all on the same line.
for i in range(1, 11):
    print(i, end=" ")

# this is here so that the next for loop runs on a completely new line.
print("\n")

# and now, we run this for loop on the new line, but going backwards from the first for loop.
for i in range(10, 0, -1):
    print(i, end=" ")