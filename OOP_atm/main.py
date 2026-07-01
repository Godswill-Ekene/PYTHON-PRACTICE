#OOP approach to ATM system
#This program demonstrates object-oriented programming principles in a simple ATM simulation
from auth import authenticate_user, register_user

def menu():
    print("1. Register")
    print("2. Login")
    print("3. Exit")

def main():

    while True:

        menu()

        choice = input("> ")

        if choice == "1":
            register_user()

        elif choice == "2":
            account = authenticate_user()

            if account:
                account.run()

        elif choice == "3":
            print("Goodbye.")
            break

if __name__ == "__main__":    
    main()