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
        print("Suspicious activity detected 🚨")


def login_system():
    attempts = 3

    while attempts > 0:
        users = load_users()

        action = input("Register(new user) / Login(existing user)?\n").strip().lower()
        username = input("Enter username:\n").strip().lower()
        password = input("Enter password:\n").strip()

        if action == "register":
            message = register(users, username, password)
            print(message)

        elif action == "login":

            if username not in users:
                print("User not found ❌")
                attempts = reduce_attempts(attempts)

            elif users[username] != password:
                print("Wrong password ❌")
                attempts = reduce_attempts(attempts)

            else:
                print("Access granted ✅")
                return

        else:
            print("Invalid option")
            
        attempts = reduce_attempts(attempts)

    print("Account locked 🔒")


login_system()