#OOP approach to ATM system
#This program demonstrates object-oriented programming principles in a simple ATM simulation

from datetime import datetime
class Bankaccount:
    
    def __init__(self, owner, balance, pin):
        self.owner = owner
        self.balance = balance
        self.pin = pin
        self.transactions = []

    def transaction_history(self):
        
        if len(self.transactions) == 0:
            print("No transactions yet.")
            return
        else:
            for transaction in self.transactions:
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
        self.transactions.append(f"{timestamp} - Deposit: {amount} | Balance: {self.balance}")
        
        timestamp = datetime.now().strftime("%Y-%m-%d | %H:%M:%S")
        print(f"Deposited: {amount}. New balance: {self.balance}")
        self.transactions.append(f"{timestamp} - Deposit: {amount} | Balance: {self.balance}")
        
    def withdraw(self):
        try:
            amount = float(input("Enter amount to withdraw: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            return        
        if amount > self.balance:
            print("Insufficient funds.")
            return
        else:
            self.balance -= amount
            timestamp = datetime.now().strftime("%Y-%m-%d | %H:%M:%S")
            print(f"Withdrawal: {amount}. New balance: {self.balance}")
            self.transactions.append(f"{timestamp} - Withdrew: {amount} | Balance: {self.balance}")
    
    def transfer(self):
        while True:
            try:
                print("1. Transfer to self")
                print("2. Transfer to new account")
                print("3. Transfer to beneficiary")
                option = input("Select option (1-3): ")
            except ValueError:
                print("Invalid input, please choose an option.")
                return

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
            return
        
        acc_name = input("Enter account name: ")

        if amount > self.balance:
            print("Insufficient funds, please deposit to transfer")
            return

        elif amount <= 0.0:
            print("Enter a valid amount")
            return

        if len(acc_number) != 10:
            print("Invalid account number, try again.")
            return

        else:
            self.balance -= amount
            print(f"Successfully transfered {amount} to {acc_name} | {acc_number}")
            timestamp = datetime.now().strftime("%Y-%m-%d | %H:%M:%S")
            self.transactions.append(f"{timestamp} - Transfer: {amount} | Balance: {self.balance}")

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

    def save_user(owner, pin, balance):
        with open("users_atm.txt", "a") as file:
            file.write(f"{owner},{pin},{balance}\n")

    def register_user(accounts, owner, pin, balance):
        if owner in accounts:
            return "user already exists"
        
        save_user(owner, pin, balance)
        return "Registration successful!"

    def load_users():
        accounts = {}

        try:
            with open("users_atm.txt", "r") as file:
                for line in file:
                    owner, pin, balance = line.strip().split(",")

                    accounts[owner] = Bankaccount( #the object and values
                        owner,
                        float(balance),
                        pin
                    )

        except FileNotFoundError:
            print('No registered users yet.')

        return accounts
    
    def main():
        attempts = 3
        logged_in = False

        while attempts > 0:
            accounts = load_users()
            try:
                option = input("Register / Login: ").strip().lower()
                owner = input("Enter name: ").strip().lower()
                pin = input("Enter PIN: ").strip()
                balance = input("Enter balance: ").strip()
            except ValueError:
                print("Invalid input")
                return
            
            if option == "register":
                message = register_user(accounts, owner, pin, balance)
                print(message)

            elif option == "login":
                if owner in accounts:
                    account = accounts[owner]
                    if pin == account.pin:
                        print("Login successful!")
                        logged_in = True
                        account.run() #this calls the method while accessing the object values
                        exit()
                    else: 
                        print("Wrong PIN, try again")

                else:
                    print("User not found")

                attempts -= 1
                print(f"You have {attempts} attempts left")

        if not logged_in:
            print("Try again later.")   

    main()