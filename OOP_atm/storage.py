from bank_account import BankAccount
def save_user(owner, pin, balance):
        with open("users_atm.txt", "a") as file:
            file.write(
                f"{owner},"
                f"{pin},"
                f"{balance}\n"
            )

def load_users():
    accounts = {}

    try:
        with open("users_atm.txt", "r") as file:
            for line in file:
                owner, pin, balance = line.strip().split(",")

                accounts[owner] = BankAccount(  
                     owner,
                     pin,    
                    float(balance)
                )   #this is where we create a new instance of the Bankaccount class for each user and store it in the accounts dictionary
                

    except FileNotFoundError:
        print('No registered users yet.')

    return accounts