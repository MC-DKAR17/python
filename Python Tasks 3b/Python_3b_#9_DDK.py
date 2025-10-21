# Task 9: Average Calculator

# Starting with a number chosen by the user.
count = int(input("How many numbers?: "))

# empty array to store values
storage = []

# for loop that uses the count chosen by the user

# then, every new iteration, it asks the user for a number to put into the array.

# once the for loop has finished it's calculations, then we move on to the next step.
for i in range(1, count + 1):
    calculations = int(input(f"Enter number {i}: "))
    storage.append(calculations)

# the next step is summing up everything inside the array, and then dividing it by the user count.
total = sum(storage) / count

# and now, we have the total completely averaged out.
print(f"The average is {total}")