# First off, we start with 1000 dollars

atm_balance = 1000

# and now, we have this behemoth of a while loop
while True:
    # this first part is just showing the user what options they have, while also including \n as a line break in-between choices.
    print("\n ATM Menu: ")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    user_input = int(input("Choice: "))
    
    # if the user inputs 1, then it will show the current balance
    if user_input == 1:
        print(f"Your balance: ${atm_balance}")
    
    # next, we have the deposit, which is just adding whatever amount the user likes to the atm balance, and prints out the new balance
    elif user_input == 2:
        deposit_amt = float(input("Deposit amount: $"))
        atm_balance += deposit_amt
        print(f"New balance: ${atm_balance}")
    # this is the opposite from the last, instead subtracting from the balance and then printing out the new value
    elif user_input == 3:
        withdraw_amt = float(input("Withdraw amount: $"))
        atm_balance -= withdraw_amt
        print(f"New balance: ${atm_balance}")
    
    # and then, this is just to make sure the loop isn't infinite, and the user can exit out of the atm
    elif user_input == 4:
        print("Thank you for using our ATM!")
        break
    