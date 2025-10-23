# empty variable to store values
total = []

# condition is infinitely true
while True:

    # asks the user for a number, which is later added to the array
    user_num = int(input("Enter a number (0 to stop): "))
    total.append(user_num)

    # when the user inputs 0, it stops the loop and prints out the sum of the array
    if user_num == 0:
        print(sum(total))
        break