#PIN SYSTEM
#MENU
#WITHDRAWAL VALIDATION
#DEPOSIT VALIDATION
#BALANCE INQUIRY

def menu():
    while True:
        try:
            print("Welcome to the ATM!")
            print("Choose an option (1, 2, 3, 4):")
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Balance Inquiry")
            print("4. Exit")
            return input("Enter your choice:\n ")
        except ValueError:
            print("Invalid option! Please try again.")
        continue

def validate_pin(pin):
    attempts = 3
    while attempts > 0:
        try:
            pin = int(input("Enter 4-digit pin:\n "))
        except ValueError:
            print("Invalid input. Please enter a 4-digit number.")
            attempts = reduce_attempts(attempts)
            continue

        if pin != 1234:
            print("Access denied.")
            attempts = reduce_attempts(attempts)
            continue

        else:
            print("Access granted.")
            break
    return "Account locked!"   

def withdraw():
    balance = 5000
    while balance > 0:
        try:
            withdraw = int(input("Enter an amount to withdraw: \n"))
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
            continue

        if withdraw >= 5000:
            print("Insufficient funds!")
            continue
            
        else:
            balance -= withdraw
            validate = validate_pin(1234)
            if validate == "Account locked!":
                return validate
            else:
                print(f"Withdrawal successful! Your new balance is: {balance}")
            return balance
        
    return "Account locked!"

def reduce_attempts(attempts):
    attempts -= 1
    print(f"Attempts left: {attempts}")

    if attempts == 1:
        print("Last attempt remaining. Please try again.")

    return attempts

def ATM():
        list = menu()
        print(list)
        if list == "1":
            result = withdraw()
            print(result)

        else:
            print("Thank you for using the ATM. Goodbye!")

ATM()


