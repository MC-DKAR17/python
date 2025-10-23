
# takes any text that the user would like to input
user_input = input("Enter some text: ")

# blank total variable to store the value of how many "A"s will be in the text written.
total = 0

# each time this for loop iterates through the text and finds a letter "a", then it will add one to the total variable, and then later on
# will print out the full total of "a"s in the text.
for char in user_input:
    if char =="a":
        total += 1

# This finally prints out the total times the letter "A" appears in the text.
print(f"The letter 'a' appears {total} times")