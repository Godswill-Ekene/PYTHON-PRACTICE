from bank_account import Bankaccount
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

                accounts[owner] = Bankaccount( #the object and values
                    owner,
                    pin,
                    float(balance)
                )

    except FileNotFoundError:
        print('No registered users yet.')

    return accounts