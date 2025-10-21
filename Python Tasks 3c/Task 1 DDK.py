
# takes a user input, could be any word that they want
user_input = input("Enter a word: ")

# for every letter in the word that the user wrote, it will print out that specific letter until it reaches the entire word.

# example, someone chooses the word: "Python"

# what will be printed:
# p
# y
# t
# h
# o
# n

for char in user_input:
    print(char)