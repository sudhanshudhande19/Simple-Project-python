# ---------------- ATM Simulation Project ----------------

# Display ATM Heading
print("========== ATM ==========")

# Take PIN input from the user
pin = int(input("Enter Your 4-Digit PIN = "))
print()

# Check whether the PIN is a valid 4-digit number
if 1000 <= pin <= 9999:

    # Set the initial account balance
    Current_Balance = 50000

    # Display ATM Menu
    print("========= ATM MENU =========")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    print()

    # Take option from the user
    option = int(input("Select an Option (1-4) = "))
    print()

    # Option 1: Check Current Balance
    if option == 1:
        print("Current Balance =", Current_Balance)
        print()

    # Option 2: Deposit Money
    elif option == 2:

        # Take deposit amount
        deposit = int(input("Enter Deposit Amount = "))

        # Check if deposit amount is valid
        if deposit > 0:
            print("Current Balance =", Current_Balance + deposit)
            print("Deposit Successful")
            print()
        else:
            print("Invalid Deposit Amount")
            print()

    # Option 3: Withdraw Money
    elif option == 3:

        # Take withdraw amount
        Withdraw_Money = int(input("Enter Withdraw Amount = "))

        # Check if sufficient balance is available
        if Withdraw_Money <= Current_Balance:
            print("Current Balance =", Current_Balance - Withdraw_Money)
            print("Withdraw Successful")
            print()
        else:
            print("Insufficient Balance")
            print()

    # Option 4: Exit
    elif option == 4:
        print("Thank You For Using ATM")
        print("Visit Again")
        print()

    # Invalid menu option
    else:
        print("Invalid Option Selected")
        print()

# Invalid PIN
else:
    print("Invalid PIN")
    print("Thank You For Using ATM")
    print("Visit Again")