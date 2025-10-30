import random

# starting with no wins or losses
wins = 0

losses = 0


# this is gonna be a lot, so bear with me:
while True:

    # this is setting up the first random value that the computer thought of, which will be compared with the new random value later
    computer_num = random.randint(1,100)
    print(f"Current number: {computer_num}")
    user_guess = input("Will the next number be (h)igher or (l)ower? ")

    # this is that said new random value, which will be compared based on the user inputs.
    new_value = random.randint(1,100)

    # the "h" section consists of whether the number guessed was actually higher, or it was lower. if it was lower, then we add a loss and the loop breaks

    # if not, then... the game continues on
    if user_guess == "h" and (new_value > computer_num):
        print(f"Next number: {new_value}")
        print("You win!")
        wins += 1
    elif user_guess == "h" and (new_value < computer_num):
        print(f"Next number: {new_value}")
        print("You lose!")
        losses += 1
        break
    
    # this is the same as earlier, only its with lower instead of higher values
    if user_guess == "l" and (new_value < computer_num):
        print(f"Next number: {new_value}")
        print("You win!")
        wins += 1
    elif user_guess == "l" and (new_value > computer_num):
        print(f"Next number: {new_value}")
        print("You lose!")
        losses += 1
        break

# printing out the score once you lose!
print(f"Score: {wins} wins, {losses}, losses")