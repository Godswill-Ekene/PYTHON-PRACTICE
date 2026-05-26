
balance = 5000

from history import transactions
from datetime import datetime
from authe import validate_pin

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