password = input("Enter your password: ")

if len(password) < 8:
    print("Weak ❌ - Too short")
elif password.isalpha():
    print("Weak ❌ - Add numbers")
elif password.isdigit():
    print("Weak ❌ - Add letters")
else:
    print("Strong ✅")

if len(password) < 8:
    if password.isalpha() or password.isdigit():
        print('Weak password, must be alphanumeric')
    else:
        print('Strong')
else:
    print('Invalid input')