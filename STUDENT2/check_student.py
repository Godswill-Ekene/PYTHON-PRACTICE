
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
        pass # File doesn't exist yet, return empty dict

    return users

def register_user(users, name, age, course,):
    if name in users:
        return "User already exists!"

    else:
        add_user(name, age, course)
        return "User registered successfully"

def options():
    print("1. Register a new user")
    print("2. View all users")
    print("3. Exit")

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

    name = input("Enter your name:\n").strip().lower()
    age = input("Enter your age:\n").strip()
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
            print("Exiting the program...")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()