
# while this loop is true, it will keep going until the user inputs the correct password
while True:
    password = input("Enter password: ")
    print("Incorrect.")
    if password == "password":
        print("Access granted.")
        break
