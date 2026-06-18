#OOP approach to ATM system
#This program demonstrates object-oriented programming principles in a simple ATM simulation
#

class Bankaccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self):
        try:
            amount = float(input("Enter amount to deposit: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            return
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

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
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

    def display_owner(self):
        print(f"Account owner: {self.owner}")
    
    def options(self):
        print("Welcome to the Bank Account Management System")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Display Owner")
        print("5. Exit")

    def run(self):
        while True:
            self.options()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.deposit()
            elif choice == '2':
                self.withdraw()
            elif choice == '3':
                self.check_balance()
            elif choice == '4':
                self.display_owner()
            elif choice == '5':
                print("Thank you for using the Bank Account Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    account = Bankaccount("Destiny", 0.0) #the object and values
    account.run() #this calls the method while accessing the object values