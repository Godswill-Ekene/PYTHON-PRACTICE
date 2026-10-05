from bank_account import BankAccount

account1 = BankAccount("John", "1122", 2000)
account2 = BankAccount("Ebube", "1212", 1500)

account1.beneficiaries.append({
    "name" : account2.owner,
    "account" : "1029384756",
    "account_object" : account2 
})

recipient = account1.beneficiaries[0]["account_object"]
amount = 300
account1.transfer_to(recipient, amount)

print(recipient.owner)
print(recipient.balance)
print(account1.beneficiaries)