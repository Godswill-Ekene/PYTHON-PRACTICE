#ATM SYSTEM
#MENU
#WITHDRAWAL VALIDATION
#DEPOSIT VALIDATION
#BALANCE INQUIRY
#TRANSACTION HISTORY

# Global balance variable, this will be used across all functions to keep track of the user's balance.
balance = 5000
transactions = []

def menu():
    while True:
        try:
            print("Welcome to the ATM!")
            print("Choose an option (1, 2, 3, 4):")
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Balance Inquiry")
            print("4. Exit")
            print("5. Transaction History")
            return input("Enter your choice: ")
        except ValueError:
            print("Invalid option! Please try again.")
        continue

def reduce_attempts(attempts):
    attempts -= 1
    print(f"Attempts left: {attempts}")

    if attempts == 1:
        print("Last attempt remaining. Please try again.")
            #if i use return "Account locked!" here, it will end the program immediately after the last attempt, which is not what I want. I want the user to have one last chance to enter the correct pin before the account is locked.
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
            return #if don't return here it will keep asking for pin even after putting the correct one 
    return "Account locked!" 

def transaction_history():
    if len(transactions) == 0:
        print("No transactions yet.")
    else:
        for transaction in transactions:
            print(transaction)
            return        

def withdraw():
    # Global balance variable
    global balance
    while balance > 0:
        try:
            amount = int(input("Enter an amount to withdraw: "))
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
            continue

        if amount > balance:
            print("Insufficient funds!")
            continue
            
        else:
            validate = validate_pin(1234)
            if validate == "Account locked!":
                return "Account locked!"
            else:
                balance -= amount
                print(f"Withdrawal successful! Your new balance is: {balance}")
                transactions.append(f"Withdraw: {amount} | Balance: {balance}")
                return 

def deposit():
    # Global balance variable
    global balance
    while True:
        try:
            amount = int(input("Enter an amount to deposit: "))
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
            continue
                    
        validate = validate_pin(1234)
        if validate == "Account locked!":
            return "Account locked!"
        else:
            balance += amount
            print(f"Deposit successful! Your new balance is: {balance}")
            transactions.append(f"Deposit: {amount} | Balance: {balance}")
            return 
    
def balance_enquiry():
    # Global balance variable
    global balance
    while True:
        validate = validate_pin(1234)
        if validate == "Account locked!":
            return "Account locked!"

        else:
            print(f"Balance enquiry successful! Your balance is: {balance}")
            return 

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

            elif choice == "5":
                result = transaction_history()
                print(result)

            else:
                print("Invalid! Please try again.")

def login():
    validate = validate_pin(1234)
    if validate == "Account locked!":
        return "Account locked!"
    
    else:
        return ATM()
    

login()


