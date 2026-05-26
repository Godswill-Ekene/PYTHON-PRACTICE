
def login():
    validate = validate_pin()
    if validate == "Account locked!":
        return "Account locked!"
    return validate

def reduce_attempts(attempts):
    attempts -= 1
    print(f"Attempts left: {attempts}")

    if attempts == 1:
        print("Last attempt remaining. Please try again.")
            #if i use return "Account locked!" here, it will end the program immediately after the last attempt, which is not what I want. I want the user to have one last chance to enter the correct pin before the account is locked.
    return attempts

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
            return True
    return "Account locked!" 
