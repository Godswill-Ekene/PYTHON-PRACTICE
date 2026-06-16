

users = {
    "admin": "1234",
    "user1": "pass1",
    "ekene": "secure123"
}


def register(username, password):
    if username in users:
        return "Username already exists!"
    
    else:
        users[username] = password
        return "User registered successfully"
    
def login(username, password):
    if username not in users:
        return False, "User not found "
    elif users[username] != password:
        return False, "Wrong password "
    else:
        return True, "Access granted "
    

def login_system():
    attempts = 3

    while attempts > 0:
        action = input("Register(new user) / Login(existing user)?\n ").strip().lower()
        username = input("Enter username:\n").strip().lower()
        password = input("Enter password:\n").strip()

        if action == "register":
            message = register(username, password)
            print(message)
            
        elif action == "login":
            status, message = login(username, password)
            print(message)  

        else:
            print("Invalid option")

        attempts -= 1
        print(f"Attempts left: {attempts}")

        if attempts == 1:
            print("Suspicious activity detected ")

    print("Account locked ")


login_system()