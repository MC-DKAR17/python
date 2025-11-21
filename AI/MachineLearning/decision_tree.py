"""
Decision Tree Program: [Weekend Planner]
Team Members: Solo [Danielius]
Date: [11/17/25]
Description: [A small decision tree about getting a weekend plan together, whether it be solo or with friends, and depends on if it is raining or sunny]
"""

print("=" * 60)
print("[Weekend Planner]")
print("=" * 60)
print()

# Gather information (at least 3 inputs)
input1 = input("What is the weather like? (Rainy, or Sunny?): ").lower()
input2 = input("Do you want to have some me time? (Yes or No): ").lower()

def display_reccomend():
    print()  # Blank line for formatting
    print("-" * 60)
    print("RECOMMENDATION:")
    print("-" * 60) 

# Decision tree logic (at least 2 levels of nesting, 4 outcomes)
if input1 == "rainy":
    if input2 =="yes":
        # Outcome 1
        display_reccomend()
        print("Recommendation: You should read a book!")
        print("Reason: It's raining, and you're forced to stay inside. Why not read something that can clear your mind?")
    elif input2 == "no":
        # Outcome 2
        display_reccomend()
        print("Recommendation: You should invite some friends over for video games")
        print("Reason: It doesn't have to be centered around video games, but you could at least have some activities with your friends while indoors!")
    else:
        print("ERrOR in InpUT")
elif input1 == "sunny":
    input3 = input("Is the destination close by, or far away? (Close / Far): ").lower()
    if input2 == "no":
        if input3 == "close":
            # Outcome 3
            display_reccomend()
            print("Recommendation: You should eat out!")
            print("Reason: Eating with friends can help everyone bring themselves together and to have a nice time in general.")
        elif input3=="far":
            # Outcome 4
            display_reccomend()
            print("Recommendation: You should head out to the movies!")
            print("Reason: Watching a good movie with friends can be such a thrill!")
        else:
            print("ERrOR in InpUT")
    elif input2 == "yes":
        # You can add more outcomes here
        if input3 == "close":
            # Outcome 3
            display_reccomend()
            print("Recommendation: You should take a walk!")
            print("Reason: Taking a walk can genuinely help clear the mind and put you in a better state than before.")
        elif input3=="far":
            # Outcome 4
            display_reccomend()
            print("Recommendation: You should take a trip through a park!")
            print("Reason: Seeing all the nature and various creatures that roam about can be super calming for the mind. It doesn't also have to be a park, either. You could go to a forest to immerse yourself in the natural world.")
        else:
            print("ERrOR in InpUT")
    else:
            print("ERrOR in InpUT")
else:
    print("ErRoR iN iNpUt")

print()
print("=" * 60)
print("Thank you for using [Weekend Planner]!")
print("=" * 60)