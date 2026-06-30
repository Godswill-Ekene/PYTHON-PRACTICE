
from storage import load_users, save_user
def register_user(accounts, owner, pin, balance):
        if owner in accounts:
            return "user already exists"
        
        save_user(owner, pin, balance)
        return "Registration successful!"

def login():
    attempts = 3
    logged_in = False
    while attempts > 0:
        accounts = load_users()
        try:
            option = input("Register / Login: ").strip().lower()
        except ValueError:
            print("Invalid input")
            return
                
        if option == "register":
            owner = input("Enter name: ").strip().lower()
            pin = input("Enter PIN: ").strip()
            balance = input("Enter balance: ").strip()
            message = register_user(accounts, owner, pin, balance)
            print(message)

        elif option == "login":
            owner = input("Enter name: ").strip().lower()
            pin = input("Enter PIN: ").strip()
            if owner in accounts:
                account = accounts[owner]
                if pin == account.pin:
                    print("Login successful!")
                    logged_in = True
                    account.run() #this calls the method while accessing the object values
                    exit()
                else: 
                    print("Wrong PIN, try again")

            else:
                print("User not found")

            attempts -= 1
            print(f"You have {attempts} attempts left")

    if not logged_in:
        print("Try again later.")   