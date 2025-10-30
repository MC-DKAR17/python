
import random

# starting with an empty list
lottery_numbers = []


# this iterates through six times, and each time it iterates through, a new random value is generated, and the if statement inside the loop
# checks for if the newly generated value is not in the list already, and if that's the case, then it adds the new value into the list
for i in range(6):
    lottery_value = random.randint(1,49)
    if lottery_value not in lottery_numbers:
        lottery_numbers.append(lottery_value)

# printing out all the lottery numbers
print(f"Your lottery numbers: {lottery_numbers}")