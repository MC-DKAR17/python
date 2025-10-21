# Task 5: Free Throw Tracker

# asking the user for how many free throws they want to shoot
free_throw_count = int(input("How many free throws will you attempt?: "))

# setting up a blank score variable for later
score = 0

# looping through the different attempts, and each time "y" is selected, one is
# added to the score.
# Also, each time the question is answered, it gives a current update on the
# score.
for i in range(free_throw_count):
    question = input(f"Shot {i+1} (y/n): ")
    if question == "y":
        score = score + 1
    print(f"Current score: {score}")

# Finally, printing the final score.
print(f"Final score: {score} out of {free_throw_count}")
