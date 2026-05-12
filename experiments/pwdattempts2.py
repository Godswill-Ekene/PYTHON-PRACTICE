
attempts = 3

while attempts > 0:

    
        pin = int(input("Enter PIN: "))

        if pin == 1234:
            print("Access granted ✅")
            

        else:
            print("Wrong PIN ❌")

    

        attempts -= 1
        print(f"Attempts left: {attempts}")

else:
    print("Too many wrong attempts, account locked!")
