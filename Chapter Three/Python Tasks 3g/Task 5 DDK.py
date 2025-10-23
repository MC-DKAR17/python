# importing the random functon
import random

# setting the random value to be a value between 1 and 50
AI_rand = random.randint(1, 50)

# empty variable for later
total = 0

# adding suspense for the viewer :OO
print("I'm thinking of a number between 1 and 50...")

# loop that runs forever until the user guesses the random value, and along the way gives hints depending on the value of the guess
while True:
    guess = int(input("Your guess: "))
    total += 1
    if guess > AI_rand:
        print("Too high")
    elif guess < AI_rand: 
        print("Too low")
    if guess == AI_rand:
        print(f"Correct! You got it in {total} guesses.")
        break