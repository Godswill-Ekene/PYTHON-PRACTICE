
from storage import load_users, save_user
def register_user():
        accounts = load_users()
        owner = input("Enter name: ").strip().lower()
        pin = input("Enter PIN: ").strip()
        balance = input("Enter balance: ").strip()
        
        if owner in accounts:
            return "user already exists"
        
        save_user(owner, pin, balance)
        return "Registration successful!"

def authenticate_user():
    attempts = 3
    logged_in = False
    while attempts > 0:
        accounts = load_users()
        
        owner = input("Enter name: ").strip().lower()
        pin = input("Enter PIN: ").strip()

        if owner in accounts:
            account = accounts[owner]

            if pin == account.pin:
                print("Login successful!")
                logged_in = True
                return account
            else: 
                print("Wrong PIN, try again")

        else:
            print("User not found")

        attempts -= 1
        print(f"You have {attempts} attempts left")

    if not logged_in:
        print("Try again later.")   