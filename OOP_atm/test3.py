from bank_account import BankAccount

account1 = BankAccount("John", "1234", 2000.0, "1029384756")
account2 = BankAccount("Ebube", "5678", 1500.0, "1029384757")

accounts = (account1, account2)
def find_account(accounts, account_number):
    for account in accounts:
        if account.account_number == account_number:
            return account
    return None
account_number = input("Enter account number: ")
recipient = find_account(accounts, account_number)
if not recipient:
    print("Account not found.")
elif recipient == account1:
    print("You cannot transfer to your own account.")
else:
    print(recipient.owner)
    amount = float(input("Enter amount to transfer: "))
    result = account1.transfer_to(recipient, amount)#this will call the transfer_to method of account1 and pass the recipient (account2) and the amount to transfer.``
    print(result)
    print(f'Balance: {account1.balance}')
    print(f'Recipient Balance: {recipient.balance}')
#self represents the current instance of the class (account1), 
#recipient represents the account object of the selected beneficiary (account2). 
# amount represents the amount to be transferred from account1 to account2.
#self.balance -= amount will deduct the amount from account1's balance
#recipient.balance += amount will add the amount to account2's balance.