# Task 5: Multiplication Table

starting_value = int(input("Enter a number: "))

for i in range(1, 11):
    calculation = starting_value * i
    print(f"{starting_value} x {i} = {calculation}")