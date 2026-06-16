def load_users():
    users = {}

    with open("users.txt", "r") as file:
        for line in file:
            username, password = line.strip().split(",")
            users[username] = password

    return users


def save_user(username, password):
    with open("users.txt", "a") as file:
        file.write(f"{username},{password}\n")


def register(users, username, password):
    if username in users:
        return "Username already exists!"

    save_user(username, password)
    return "User registered successfully"


def reduce_attempts(attempts):
    attempts -= 1
    print(f"Attempts left: {attempts}")

    if attempts == 1:
        print("Suspicious activity detected ")
    return attempts


def login_system():
    attempts = 3

    while attempts > 0:
        users = load_users()
        #since we are using the same variable to reduce attempts, we need to load users inside the loop to make sure we have the most updated list of users after registration
        #if we load users outside the loop, we will not have the new user in the users dictionary after registration, and the user will not be able to login with the new account until they restart the program
        #since the input is not value sensitive no need for try / except block to handle value errors, we can just use strip() and lower() to handle extra spaces and case sensitivity
        action = input("Register(new user) / Login(existing user)?\n").strip().lower()
        username = input("Enter username:\n").strip().lower()
        password = input("Enter password:\n").strip()

        if action == "register":
            message = register(users, username, password)
            print(message)

        elif action == "login":

            if username not in users:
                print("User not found ")
                attempts = reduce_attempts(attempts)

            elif users[username] != password:
                print("Wrong password ")
                attempts = reduce_attempts(attempts)

            else:
                print("Access granted ")
                return

        else:
            print("Invalid option")
            
        attempts = reduce_attempts(attempts)

    print("Account locked ")


login_system()