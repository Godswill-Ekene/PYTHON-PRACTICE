from bank_account import BankAccount
def save_user(owner, pin, balance, account_number):
        with open("users_atm.txt", "a") as file:
            file.write(
                f"{owner},"
                f"{pin},"
                f"{balance},"
                f"{account_number}\n"
            )

def load_users():
    accounts = {}

    try:
        with open("users_atm.txt", "r") as file:
            for line_number, line in enumerate(file, start=1):
                parts = line.strip().split(",")

                if len(parts) != 4:
                    print(f"Skipping invalid record on line {line_number}.")
                    continue

                owner, pin, balance, account_number = parts

                try:
                    accounts[owner] = BankAccount(  
                        owner,
                        pin,                        
                        float(balance),
                        account_number
                    )
                except ValueError:
                    print(f"Invalid balance on line {line_number}.")

    except FileNotFoundError:
        print('No registered users yet.')

    return accounts

def find_account(accounts, account_number):
    for account in accounts.values():
        if account.account_number == account_number:
            return account
    return None

