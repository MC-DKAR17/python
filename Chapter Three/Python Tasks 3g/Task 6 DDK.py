
# this loop will keep running forever, until the number that the user inputs is between the values of 0 and 100.
while True:
    user_input = int(input("Enter a grade (0-100): "))
    if user_input >= 100 or user_input <= 0:
        print("Invalid! Must be between 0 and 100")
    else:
        print(f"Valid grade accepted: {user_input}")
        # without this break, we would be getting an infinite loop
        break