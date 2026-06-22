

#save new user
def save_user(username, password):
    with open("users.txt", "a") as file:
        file.write(f"{username},{password}\n")

#convert file to dictionary
def convert_file():
    users = {}

    with open("users.txt", "r") as file:
        for line in file:
            username, password = line.strip().split(",")
            users[username] = password

    return users
            

def register_users():
    while True:

        username = input("Enter username:\n").strip().lower()
        password = input("Enter password:\n").strip()

        users = convert_file()
        if username in users:
            print("Username already exists")
        else:
            add = save_user(username, password)
            if add:
                convert = convert_file()
                print(convert)
            
        again = input("Do you want to register another user? (yes/no)\n").strip().lower()
        if again != "yes":
            print("Exiting registration.")
            break
        
register_users()
