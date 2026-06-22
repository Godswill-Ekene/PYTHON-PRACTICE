
from allstudent_module import users, books, students
def search_student():    
    search = input('Search for a student in dict: \n').strip().lower()

    if search in users:
        print(f"Name: {search.capitalize()}")
        print(f"Age: {users[search]['age']}")
        print(f"Course: {users[search]['course']}")
    
    else:
        print('Student not found!')

    search = input('Search for a student in list: \n').strip().lower()

    found = False
    for student in students:
        if search == student["name"]:
            print(f"Name: {student['name'].capitalize()}")
            print(f"Age: {student['age']} years")
            print(f"Course: {student['course']}")
            found = True
            break

    if not found:
        print("Student not found!")

    choice = input('Enter book name: \n').strip().lower()
    if choice in books:
        print(f"Author: {books[choice]['author']}")
        print(f"Price: {books[choice]['price']}")

    else:
        print('Book not found!')