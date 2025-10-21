# Task 6: Range Calculator

# starting with setting the lower bound of the range
lower_bound = int(input("Enter lower bound: "))

# vice versa, but with the upper bound instead
upper_bound = int(input("Enter upper bound: "))

# empty total variable to store for later
calculations = 0


# for loop that uses a range of the lower bound and upper bound + 1, with the total calculations being added by i.
for i in range(lower_bound, upper_bound + 1):
    calculations += i

# finally, printing out the sum of the numbers in that range.
print(f"The sum of numbers from {lower_bound} to {upper_bound} is {calculations}")