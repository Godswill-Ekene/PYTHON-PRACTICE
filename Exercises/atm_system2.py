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
        print("Welcome to the ATM!")
        print("Choose an option (1, 2, 3, 4, 5):")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Balance Inquiry")
        print("4. Exit")
        print("5. Transaction History")
        return (input("Enter your choice: "))

def reduce_attempts(attempts):
    attempts -= 1
    print(f"Attempts left: {attempts}")

    if attempts == 1:
        print("Last attempt remaining. Please try again.")
            #if i use return "Account locked!" here, it will end the program immediately after the last attempt, which is not what I want. I want the user to have one last chance to enter the correct pin before the account is locked.
    return attempts

def validate_pin():
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
            return True
    return "Account locked!" 

def transaction_history():
    if len(transactions) == 0:
        print("No transactions yet.")
    else:
        for transaction in transactions:
            print(transaction)
    return        

from datetime import datetime

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

        elif amount <= 0:
            print("Enter a valid withdrawal amount!")
            continue
        
        else:
            validate = validate_pin()
            if validate == "Account locked!":
                return "Failed attempts!"
            else:
                balance -= amount
                timestamp = datetime.now().strftime("%Y-%m-%d | %H:%M:%S")
                print(f"Withdrawal successful! Your new balance is: {balance}")
                transactions.append(f"{timestamp} - Withdraw: {amount} | Balance: {balance}")
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
                    
        if amount <= 0:
            print("Enter a valid deposit amount!")
            continue

        validate = validate_pin()
        if validate == "Account locked!":
            return "Failed attempts!"
        else:
            balance += amount
            timestamp = datetime.now().strftime("%Y-%m-%d | %H:%M:%S")
            print(f"Deposit successful! Your new balance is: {balance}")
            transactions.append(f"{timestamp} - Deposit: {amount} | Balance: {balance}")
            return 
            
def balance_enquiry():
    # Global balance variable
    global balance
    while True:
        validate = validate_pin()
        if validate == "Account locked!":
            return "Failed attempts!"
        else:
            print(f"Balance enquiry successful! Your balance is: {balance}")
            return 

def ATM():
    result = login()
    if result == "Account locked!":
        print("Account locked! Too many failed attempts.")
        return
    while True:
        choice = menu()
        if choice == "1":
            result = withdraw()
            if result:
                print(result)

        elif choice == "2":
            result = deposit()
            if result:
                print(result)

        elif choice == "3":
            result = balance_enquiry()
            if result:
                print(result)

        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break

        elif choice == "5":
            transaction_history()

        else:
            print("Invalid! Please try again.")

def login():
    validate = validate_pin()
    if validate == "Account locked!":
        return "Account locked!"
    
    return validate

ATM()