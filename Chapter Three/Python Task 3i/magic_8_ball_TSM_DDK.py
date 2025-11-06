# Danielius Karalius
# Tristan Michalek
# fun choice: 8-ball
# Tristan came up with the possible answers, along with some small touch ups in the logic.
# I was figuring out the random aspect of the game, along with setting up the while loop
# In my opinion, the hardest part was coming up with creative random responses for the 8-ball to work with. The rest wasn't that hard


import random

def display_welcome():
    """Display a welcome banner for the Magic 8-Ball."""
    print("═══════════════════════════\nMAGIC 8-BALL FORTUNE TELLER\n═══════════════════════════")

def get_question():
    """Get a question from the user. Return the question."""
    user_qhar = input("Ask a yes/no qhar (plz): ")
    return user_qhar

def get_fortune():
    """Return a random fortune from a list of possible answers."""
    # Hint: Create a list of at least 10 different answers
    # Use random.choice() or random.randint()
    fortune = ["Yeah, sure, whatever.",
        "That doesn't quite match my guide lines, bud.",
        "Hey champ, that's really interesting, next time keep it to yourself.",
        "chair",
        "I say, I say boy, that's a gosh darn tarnation WONDERFUL IDEA!",
        "I NEED <YOU TO KINDLY1 [[Vacation To A Far Away Place!]]1!!",
        "'Ey, Fogetabouit!",
        "i don't think that's plausible :U",
        "I'm a friggin' ball, not a therapist.",
        "No thanks, but maybe some other day I'll change my mind."]
    return fortune[random.randint(0,9)]


def display_fortune(fortune):
    """Display the fortune in a fancy way."""
    print("The Magic 8-ball has decided...")
    print("👀")
    print(fortune)

def play_again():
    """Ask user if they want to ask another question. Return True or False."""
    user_input = input("\n Ask another qhar? (y/n): ")
    return user_input

# Main program
display_welcome()
question_count = 0

# YOUR CODE HERE - Write the main game loop
# Use the functions above to create the complete program

print("\n")

while True:
        get_question()
        new_fortune = get_fortune()
        display_fortune(new_fortune)
        question_count += 1
        if play_again() == "n":
             print(f"You asked {question_count} question(s). Thanks for playing!!!!!!!!!!!!!!!!1111!")
             break
        
