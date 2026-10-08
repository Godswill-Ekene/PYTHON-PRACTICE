from bank_account import BankAccount

account1 = BankAccount("John", "1234", 2000.0)
account2 = BankAccount("Ebube", "5678", 1500.0)

account1.beneficiaries.append({
    "name": account2.owner,
    "account": "1029384756",
    "account_object": account2
}) #here we are adding the account2 object to the beneficiaries list of account1.

for i, beneficiary in enumerate(account1.beneficiaries, start=1):
    print(f"{i}. {beneficiary['name']} - {beneficiary['account']}")

choice = int(input("Select a beneficiary: "))
recipient = account1.beneficiaries[choice - 1]["account_object"]#this will get the account_object of the selected beneficiary from the beneficiaries list of account1.

amount = float(input("Enter amount to transfer: "))
account1.transfer_to(recipient, amount)#this will call the transfer_to method of account1 and pass the recipient (account2) and the amount to transfer.``

#self represents the current instance of the class (account1), 
#recipient represents the account object of the selected beneficiary (account2). 
# amount represents the amount to be transferred from account1 to account2.
#self.balance -= amount will deduct the amount from account1's balance
#recipient.balance += amount will add the amount to account2's balance.
