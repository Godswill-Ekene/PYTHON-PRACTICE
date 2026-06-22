
#creating file
with open("users.txt", "w") as file:
    file.write("admin,1234\n")

#opening file
with open("users.txt", "r") as file:
    data = file.readlines()

print(data)

#convert file to dictionary
def convert_file(users, username, password):
    users = {}

    with open("users.txt", "r") as file:
        for line in file:
            username, password = line.strip().split(",")
            users[username] = password

            print(users)

#save new user
def save_user(username, password):
    with open("users.txt", "a") as file:
        file.write(f"{username},{password}\n")
        return "User registered!"

def register_users():
    while True:

        username = input("Enter username:\n")
        password = input("Enter password:\n")

        add = save_user(username, password)
        if add:
            convert = convert_file( username, password)
            print(convert)

        
