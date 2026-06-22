
attempts = 3

while attempts > 0:
    try:
        password = input("Enter your password: ")
        if password == "secret":
            print("Access granted!")
            break
        else:
            print(f"Incorrect password.")

    except ValueError:
        print("\nOperation cancelled by user.")
    
    attempts -= 1
    print(f"You have {attempts} attempts left.")
else:
    print("Too many failed attempts. Access denied.")