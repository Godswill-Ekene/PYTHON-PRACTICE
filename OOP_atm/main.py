#OOP approach to ATM system
#This program demonstrates object-oriented programming principles in a simple ATM simulation
from auth import register_user, login

def menu():
    print("1. Register")
    print("2. Login")
    print("3. Exit")

def main():

    while True:

        menu()

        choice = input("> ")

        if choice == "1":
            register_user(accounts, owner, pin, balance)

        elif choice == "2":
            account = login()

            if account:
                account.run()

        elif choice == "3":
            print("Goodbye.")
            break

if __name__ == "__main__":    
    main()