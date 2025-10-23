# every value goes in here
total = []

# while this is true, it will keep adding numbers to the array until the user inputs -1
while True:
    number = int(input("Enter a number (-1 to finish): "))
    # when the user does input -1, all the values are added together, and then divided by how many there are in the array, and then printed out.
    if number == -1:
        print(f"Average: {sum(total) / len(total)}")
        break
    total.append(number)
