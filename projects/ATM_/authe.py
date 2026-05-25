
def login():
    validate = validate_pin()
    if validate == "Account locked!":
        return "Account locked!"
    
    else:
        return ATM()

def validate_pin():
    attempts = 3
    while attempts > 0:
        try:
            pin = int(input("Enter 4-digit pin: "))
        except ValueError:
            print("Invalid input. Please enter a 4-digit number.")
            attempts = reduce_attempts(attempts)
            continue

        if pin != 1234:
            print("Wrong PIN!.")
            attempts = reduce_attempts(attempts)
            continue

        else:
            print("Correct!.")
            return #if don't return here it will keep asking for pin even after putting the correct one 
    return "Account locked!" 
