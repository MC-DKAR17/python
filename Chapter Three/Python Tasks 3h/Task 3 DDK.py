import random

print("Think of a number between 1 and 100...")

# starting with 0 guesses
guesses = 0

# starting with a random value at first
computer_guess = random.randint(1,100)

while True:
    user_input = input(f"My guess is {computer_guess}. (higher/lower/correct): ")
    
    # if the user inputs, "higher", then a new random value is assigned, based on the conditions that the previous guess is the minimum value, to 100
    if user_input == "higher":
        guesses += 1
        computer_guess = random.randint(computer_guess, 100)
    
    # this is almost the same as the last one, except this time the conditional value is set to be the maximum value for the random condition (however, it's a bit buggy)
    if user_input == "lower":
        guesses += 1
        computer_guess = random.randint(1, computer_guess)
    
    # and then finally this terminates the loop, and prints out how many guesses it took
    if user_input == "correct":
        guesses += 1
        print(f"I got it in {guesses} guesses!")
        break