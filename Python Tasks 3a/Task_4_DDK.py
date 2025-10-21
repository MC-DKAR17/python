# Factorials Calculator

# setting up a number that the user would like to use
user_num = int(input("Choose a number, so long it's not a negative: "))

# integer variable used for the for loop
product = 1

# for loop that follows the range of the user_num + one.

# basically, this for loop is just calculating the factorial of the user's number
for i in range(1, user_num+1):
    product = product * i

# finally, printing the end value after all the calculations
print(f"The factorial of {user_num} is {product}")
