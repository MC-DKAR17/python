# Demonstrate task number 5: Boolean Flags

# starting off with defining the boolean we use later in the while loop
logged_in = False

# adding snazzy flair!
print("WELCOME TO TERMINAL 5. PLEASE INPUT CREDENTIALS TO CONTINUE FURTHER.")

# this loops through asking for a password, and it will not stop until Lynyrd Skynyrd is entered into the user input
while logged_in == False:
# user input
    user_guess = input("PASSWORD: ")
# the password the user needs to enter
    if user_guess == "lynyrd-skynyrd":
# this will be displayed when the user input matches the set password
        print("WELCOME USER. ENJOY FREE BIRD.")
        print("If I leave here tomorrow Would you still remember me? For I must be traveling on, now 'Cause there's too many places I've got to see But if I stay here with you, girl Things just couldn't be the same 'Cause I'm as free as a bird now And this bird you cannot change Oh-oh-oh-oh-oh And the bird you cannot change And this bird you cannot change Lord knows I can't change Bye-bye, baby, it's been a sweet love, yeah-yeah Though this feeling I can't change But, please, don't take it so badly 'Cause Lord knows I'm to blame But, if I stay here with you, girl Things just couldn't be the same 'Cause I'm as free as a bird now And this bird you cannot change Oh-oh-oh-oh-oh And the bird you cannot change And this bird you cannot change Lord knows I can't change Lord, help me, I can't change Lord, I can't change Won't you fly high, free bird, yeah")
# This will then break out of the loop, so it doesn't loop infinitely ;)
        break
    else:
# this will be displayed when the user's input doesn't match the password, then it will loop back to asking for an input from the user
        print("INVALID CREDENTIALS. GIvE IT ANOTheer [[SHOT!!!!!]] [[BIG SHOT!!!!!]]")