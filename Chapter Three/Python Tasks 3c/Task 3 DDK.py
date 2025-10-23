
# starting off with whatever text the user would like to type out for this to analyze later.
user_input = input("Enter text: ")

# setting two empty variables to use for later.
total_vowels = 0
total_consonants = 0

# this for loop counts each character inside the user_input.
for char in user_input:
    # then, it checks if each character is an actual letter.
    if char.isalpha():
        # if so, then we check if it's a vowel
        if char in "aeiouAEIOU":
            total_vowels += 1
        #if it's not, then it will be considered a consonant.
        else:
            total_consonants += 1

    
# and finally, printing out the total calculated vowels and consonants in the user written text.
print(f"Vowels: {total_vowels}")
print(f"Consonants: {total_consonants}")