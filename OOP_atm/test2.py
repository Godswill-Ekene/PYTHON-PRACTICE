#Show beneficiary
  #     ↓
#Get selected beneficiary
 #      ↓
#Get account_object
 #      ↓
#Ask user for amount
 #      ↓
#Transfer the amount

from bank_account import BankAccount
account1 = BankAccount("John", "1234", 2000.0)
account2 = BankAccount("Ebube", "5678", 1500.0)

beneficiaries = []
account1.beneficiaries.append({
    "name": account2.owner,
    "account": "1029384756",
    "account_object": account2
}) #here we are adding the account2 object to the beneficiaries list of account1. 
#and we can access the account2 object through the beneficiaries list of account1.

print("-" * 30)
print("     Welcome to the ATM")
print("-" * 30)

for i, beneficiary in enumerate(account1.beneficiaries, start=1):
    print(f"{i}. {beneficiary['name']} ({beneficiary['account']})")

choice = int(input("Select a beneficiary: "))
recipient = account1.beneficiaries[choice - 1]["account_object"]

amount = float(input("Enter amount to transfer: "))

account1.transfer_to(recipient, amount)
   