
# starting with a word the user would like to reverse
user_input = input("Enter a word: ")

# empty variable for the reversed word later
reversed_str = ""

# for every letter in the user input, that character is added to the reversed string, in reverse order. Kind of confusing, but low amount of code
for char in user_input:
    reversed_str = char + reversed_str

# printing out the final result of the reversed string.
print(reversed_str)