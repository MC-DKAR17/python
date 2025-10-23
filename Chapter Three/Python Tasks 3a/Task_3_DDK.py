# Task 3: Name Repeater


# first variable that takes a user input, telling us their name
user_name = input("What is your name?: ")

# second variable that takes an integer input, for how many times they would
# like to see their name repeated
user_iteration = int(input("How many times would you like to repeat your name?: "))

# for loop that takes the user iteration as a range, now printing out
# however many times they chose to have their name printed.
for i in range(user_iteration):
    print(user_name, end=" ")
