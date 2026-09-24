from datetime import datetime
class BankAccount:
    
    def __init__(self, owner, pin, balance):
        self.owner = owner
        self.pin = pin
        self.balance = balance
        self.transactions = []
        self.beneficiaries = []  # Initialize an empty list for beneficiaries

    def transfet_to(self, recipient, amount):
        try:
            amount = int(input('Enter amount: '))
            recipient = input('Enter recipient account: ')
            bank = input('Enter recipient bank: ')
            name = input('Enter recipient bank name: ')
        except ValueError:
            print('Inalid input, please try again..')
            return
        if amount <= 0:
            return "inavlid amount"
        elif amount > self.balance:
           return "insufficient funds!"
        if len(recipient) != 10:
            print("Invalid account number, try again.")
            return        
        else:
            amount -= self.balance
            timestamp = datetime.now().strftime("%Y-%m-%d | %H:%M:%S")
            print(f"Transfered: {amount} | to {name} | Bank {bank} | Account {recipient} | New balance: {self.balance}")
            self.transactions.append(f"{timestamp} - Transfered: {amount} | to {name} | Bank {bank} | Account {recipient} | Balance: {self.balance}")            


    def transaction_history(self):        
        if len(self.transactions) == 0:
            print("No transactions yet.")
            return
        else:
            for i, transaction in enumerate(self.transactions, start = 1):
                print(f"{i}. {transaction}")

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
        
    def withdraw(self):
        try:
            amount = float(input("Enter amount to withdraw: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            return        
        if amount > self.balance:
            print("Insufficient funds.")
            return
        elif amount <= 0.0:
            print("Invalid amount. Please enter a positive value.")
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
                self.transfer_to_beneficiary()
                break
            else:
                print("Invalid input, please try again.")
                continue

    def process(self):
        while True:
            try:
                bank_name = input("Enter bank name: ")
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
                print(f"Successfully transfered {amount} to {acc_name} | {bank_name} - {acc_number}")
                timestamp = datetime.now().strftime("%Y-%m-%d | %H:%M:%S")
                self.transactions.append(f"{timestamp} - Transfer: {amount} | Balance: {self.balance} | Recipient: {acc_name} ({acc_number}) | Bank: {bank_name}")
                
            exists = any(
                b["account"] == acc_number
                for b in self.beneficiaries
            )

            if exists:
                print("Beneficiary already exists.")
            else:
                enlist = input("Save beneficiary? (yes/no): ").lower()

                if enlist == "yes":
                    self.beneficiaries.append({
                        "name": acc_name,
                        "account": acc_number
                    })
                    print("Beneficiary saved.")
                    break
                elif enlist == "no":
                    print("Beneficiary not saved.")
                    break
                else:
                    break

    def beneficiary_list(self):
        if not self.beneficiaries:
            print("No beneficiaries found.")
            return

        print("\nBeneficiaries")
        print("-" * 30)

        for i, beneficiary in enumerate(self.beneficiaries, start=1):
            print(f"{i}. {beneficiary['name']} - {beneficiary['account']}")

    def transfer_to_beneficiary(self):

        if not self.beneficiaries:
            print("No beneficiaries available.")
            return

        self.beneficiary_list()

        try:
            choice = int(input("\nSelect beneficiary: "))
            beneficiary = self.beneficiaries[choice - 1]
        except (ValueError, IndexError):
            print("Invalid selection.")
            return

        try:
            amount = float(input("Enter amount: "))
        except ValueError:
            print("Invalid amount.")
            return

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        if amount > self.balance:
            print("Insufficient funds.")
            return

        self.balance -= amount
        timestamp = datetime.now().strftime("%Y-%m-%d | %H:%M:%S")
        self.transactions.append(
            f"{timestamp} - Transfer: {amount} -> "
            f"{beneficiary['name']} ({beneficiary['account']}) "
            f"| Balance: {self.balance}"
        )

        print(
            f"Transferred {amount} to "
            f"{beneficiary['name']} successfully."
        )

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