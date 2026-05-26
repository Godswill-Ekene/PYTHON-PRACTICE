
from banking import withdraw, deposit, balance_enquiry
from menu import menu
from history import transaction_history
from authe import login

def ATM():
    result = login()
    if result == "Account locked!":
        print("Account locked! Too many failed attempts.")
        return
    while True:
        choice = menu()
        if choice == "1":
            result = withdraw()
            if result:
                print(result)

        elif choice == "2":
            result = deposit()
            if result:
                print(result)

        elif choice == "3":
            result = balance_enquiry()
            if result:
                print(result)

        elif choice == "4":
            transaction_history()

        elif choice == "5":
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid! Please try again.")

if __name__ == "__main__":
    ATM()
