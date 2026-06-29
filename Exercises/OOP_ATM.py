#OOP approach to ATM system
#This program demonstrates object-oriented programming principles in a simple ATM simulation

from datetime import datetime
class Bankaccount:
    
    def __init__(self, owner, pin, balance):
        self.owner = owner
        self.pin = pin
        self.balance = balance
        self.transactions = []

    def transaction_history(self):
        
        if len(self.transactions) == 0:
            print("No transactions yet.")
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
        print(f"Deposited: {amount} | New balance: {self.balance}")
        self.transactions.append(f"{timestamp} - Deposit: {amount} | Balance: {self.balance}")
        
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
            print(f"Withdrawal: {amount} | New balance: {self.balance}")
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

        elif len(acc_number) != 10:
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
    balance = 0
    def save_user(owner, pin, balance):
        with open ("bank.txt", "a") as file:
            file.write(f"{owner},{pin},{balance}\n")

    def register_user(accounts, owner, pin, balance):
        if owner in accounts:
            print("User already exists, Login.")
        save_user(owner, pin, balance)
        print("User registered successfully.")

    def load_users():
        accounts = {}
        try:
            with open ("bank.txt", "r") as file:
                for line in file:
                    owner, pin, balance = line.strip().split(",")

                    accounts[owner] = {
                        "pin" : pin,
                        "balance" : balance
                    }
        except FileNotFoundError:
            print('No registered users yet.')

        return

    #account1 = Bankaccount("Destiny", "1234", 1000.0) #the object and values
    #account2 = Bankaccount("John", "2143", 2000.0)
    #account3 = Bankaccount("Believe", "3142", 2500.0)

    def check_user():
        attempts = 3
        while attempts > 0:
            accounts = load_users()
            choice = input("Register / Login: ").strip().lower()
            owner = input("Enter name: ").strip().lower()
            pin = input("Enter PIN: ").strip()

            if choice == "register":
                method = register_user(accounts, owner, pin, balance)
                print(method)
                return
            
            elif choice == "login":
                if owner in accounts:
                    account = accounts[owner]
                    if pin == account.pin:
                        print("Login successful!")
                        account.run() #this calls the method while accessing the object values
                        exit()
                    else: 
                        print("Wrong PIN, try again")

                else:
                    print("User not found")
                                
            else: 
                print("Invalid input.")
                return
            
            attempts -= 1
            print(f"You have {attempts} attempts left")

        print("Try again later")
        return
       
    check_user()