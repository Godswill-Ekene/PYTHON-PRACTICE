 


def check_username(username):
    return  username == "admin" 


def check_password(password):
    return password == "1234"

        
def login(username, password):
    if check_username(username) and check_password(password) :
        return True
    else:
        return False


def login_system():

    attempts = 3
    while attempts > 0:
        
        username = input("Enter username:\n  ")
        password = input("Enter password:\n  ")

        if login(username,password):
            print("Access granted ")
            return
        
        else:
            print("Invalid credentials ")
        
        attempts -= 1
        print(f"attempts left: {attempts}")

        if attempts == 1:
            print("Suspicious activity detected ")

    if attempts == 0:
            print("Account locked! ")

login_system()


