#ATM SYSTEM
#MENU
#WITHDRAWAL VALIDATION
#DEPOSIT VALIDATION
#BALANCE INQUIRY

# Global balance variable, this will be used across all functions to keep track of the user's balance.
balance = 5000

def menu():
    while True:
        try:
            print("Welcome to the ATM!")
            print("Choose an option (1, 2, 3, 4):")
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Balance Inquiry")
            print("4. Exit")
            return input("Enter your choice: ")
        except ValueError:
            print("Invalid option! Please try again.")
        continue

def reduce_attempts(attempts):
    attempts -= 1
    print(f"Attempts left: {attempts}")

    if attempts == 1:
        print("Last attempt remaining. Please try again.")

    return attempts

def validate_pin(pin):
    attempts = 3
    while attempts > 0:
        try:
            pin = int(input("Enter 4-digit pin: "))
        except ValueError:
            print("Invalid input. Please enter a 4-digit number.")
            attempts = reduce_attempts(attempts)
            continue

        if pin != 1234:
            print("Wrong PIN!.")
            attempts = reduce_attempts(attempts)
            continue

        else:
            print("Correct!.")
    return "Account locked!" #i think i need to add another function here to continue the withdrawal process after the pin is correct.   

def withdraw():
    # Global balance variable
    global balance
    while balance > 0:
        try:
            withdraw = int(input("Enter an amount to withdraw: "))
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
            continue

        if withdraw >= 5000:
            print("Insufficient funds!")
            continue
            
        else:
            validate = validate_pin(1234)
            if validate == "Account locked!":
                return "Account locked!"
            else:
                balance -= withdraw
                print(f"Withdrawal successful! Your new balance is: {balance}")
                return ATM()

def deposit():
    # Global balance variable
    global balance
    while True:
        try:
            deposit = int(input("Enter an amount to deposit: "))
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
            continue
                    
        validate = validate_pin(1234)
        if validate == "Account locked!":
            return "Account locked!"
        else:
            balance += deposit
            print(f"Deposit successful! Your new balance is: {balance}")
            return ATM()

def balance_enquiry():
    # Global balance variable
    global balance
    while True:
        validate = validate_pin(1234)
        if validate == "Account locked!":
            return "Account locked!"

        else:
            print(f"Balance enquiry successful! Your balance is: {balance}")
        return ATM()

def ATM():
        while True:
            choice = menu()
            print(choice)
            if choice == "1":
                result = withdraw()
                print(result)

            elif choice == "2":
                result = deposit()
                print(result)

            elif choice == "3":
                result = balance_enquiry()
                print(result)

            elif choice == "4":
                result = "Thank you for using the ATM. Goodbye!"
                print(result)
                break

            else:
                print("Invalid! Please try again.")

ATM()


