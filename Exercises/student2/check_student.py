#This program:
#1. Register's users
#2. View users
#3. Search users
#4. Exit

def add_user(name, age, course):
    with open("register.txt", "a") as file:
        file.write(f"{name},{age},{course}\n")

def load_users():
    users = {}

    try:
        with open("register.txt", "r") as file:
            for line in file:
                name, age, course = line.strip().split(",")

                users[name] = {
                    "age": age,
                    "course": course
                }

    except FileNotFoundError:
        print('No registered users yet.')

    return users

def register_user(users, name, age, course,):
    if name in users:
        return "User already exists!"

    else:
        add_user(name, age, course)
        return "User registered successfully"

def search_users():
    #when you search for a user, the program should display the user's name, age, and course if found. If not found in the nested dictionary.
    users = load_users()
    name = input("Enter the name of the user to search for: \n").strip().lower()

    if name in users:
        print(f"\nName: {name.capitalize()}")
        print(f"Age: {users[name]['age']}")
        print(f"Course: {users[name]['course']}")
    else:
        print("User not found.")

def options():
    print("1. Register a new user")
    print("2. View all users")
    print("3. Search for a user")
    print("4. Exit")

#def action1(users, name, age, course,):
    #try:
            #name = input("Enter your name: \n").strip().lower()
            #age = input("Enter your age: \n").strip()
            #course = input("Enter your course: \n").strip().lower()
    #except ValueError:
            #print("Invalid input. Please try again.")

    #message = register_user(users, name, age, course,)
    #print(message)
            
def action1(users):
    try:
        name = input("Enter your name:\n").strip().lower()
        age = input("Enter your age:\n").strip()
    except ValueError:
        print("Invalid input. Enter age..")
    course = input("Enter your course:\n").strip().lower()

    message = register_user(
        users,
        name,
        age,
        course
    )

    print(message)

#def action2():
    #users = load_users()
    #print(users)

def action2():

    users = load_users()

    if not users:
        print("No users found.")

    else:
        for name, details in users.items():
            print(f"\nName: {name.capitalize()}")
            print(f"Age: {details['age']}")
            print(f"Course: {details['course']}")

def main():
    while True:
        options()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            users = load_users()
            action1(users)
        elif choice == "2":
            action2()
        elif choice == "3":
            search_users()
        elif choice == "4":
            print("Exiting the program...")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()