#OOP approach to ATM system
#This program demonstrates object-oriented programming principles in a simple ATM simulation
#
transactions = []
from datetime import datetime
class Bankaccount:
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def transaction_history(self):
        
        if len(transactions) == 0:
            print("No transactions yet.")
        else:
            for transaction in transactions:
                print(transaction)

    def deposit(self):
        try:
            amount = float(input("Enter amount to deposit: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            return
        self.balance += amount
        timestamp = datetime.now().strftime("%Y-%m-%d | %H:%M:%S")
        print(f"Deposited: {amount}. New balance: {self.balance}")
        transactions.append(f"{timestamp} - Deposit: {amount} | Balance: {self.balance}")
        
    def withdraw(self):
        try:
            amount = float(input("Enter amount to withdraw: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            return
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            timestamp = datetime.now().strftime("%Y-%m-%d | %H:%M:%S")
            print(f"Withdrawal: {amount}. New balance: {self.balance}")
            transactions.append(f"{timestamp} - Withdrew: {amount} | Balance: {self.balance}")
    
    def transfer(self):
        while True:
            try:
                print("1. Transfer to self")
                print("2. Transfer to new account")
                print("3. Transfer to beneficiary")
                option = input("Select option (1-3): ")
            except ValueError:
                print("Invalid input, please choose an option.")
                continue

            if option == '1':
                self.process()
                break
            elif option == '2':
                self.process()
                break
            elif option == '3':
                self.process()
                break
            else:
                print("Invalid input, please try again.")
                continue

    def process(self):
        try:
            amount = float(input("Enter amount: "))
            acc_number = input("Enter recipient account number: ")
        except ValueError:
            print("Invalid input.")
        
        acc_name = input("Enter account name: ")

        if amount > self.balance:
            print("Insufficient funds, please deposit to transfer")

        elif amount <= 0.0:
            print("Enter a valid amount")

        if len(acc_number) <= 10:
            print("Invalid account number, try again.")

        else:
            self.balance -= amount
            print(f"Successfully transfered {amount} to {acc_name} | {acc_number}")
            timestamp = datetime.now().strftime("%Y-%m-%d | %H:%M:%S")
            transactions.append(f"{timestamp} - Transfer: {amount} | Balance: {self.balance}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

    def display_owner(self):
        print(f"Account owner: {self.owner}")
    
    def options(self):
        print("Welcome to the Bank Account Management System")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. Check Balance")
        print("5. Transaction history")
        print("6. Display Owner")
        print("7. Exit")

    def run(self):
        while True:
            self.options()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.deposit()
            elif choice == '2':
                self.withdraw()
            elif choice == '3':
                self.transfer()
            elif choice == '4':
                self.check_balance()
            elif choice == '5':
                self.transaction_history()
            elif choice == '6':
                self.display_owner()
            elif choice == '7':
                print("Thank you for using the Bank Account Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    account = Bankaccount("Destiny", 0.0) #the object and values
    account.run() #this calls the method while accessing the object values