from storage import find_account, load_users
from bank_account import BankAccount

account = load_users()

account_number = input("Enter account number: ")
recipient = find_account(account, account_number)

if not recipient:
    print("Account not found.")
    
elif recipient == account:
    print("You cannot transfer to your own account.")
else:
    print(recipient.owner)
    try:
        amount = float(input("Enter amount to transfer: "))
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
    result = account.transfer_to(recipient, amount)
    print(result)
    print(f'Balance: {account.balance}')
    print(f'Recipient Balance: {recipient.balance}')


