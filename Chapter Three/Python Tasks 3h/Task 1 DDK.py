# for anything random/RNG related, THIS IS A MUST HAVE!!!
import random

# starting print message
print("Rolling a die 10 times:")

# a for loop that calls the random integer method 10 times
for i in range(10):
    # this will roll for a new number between 1 and 6, emulating a dice roll
    rand_int = random.randint(1,6)
    print(rand_int, end=" ")