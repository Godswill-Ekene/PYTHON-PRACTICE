#Advanced list and data stuctures

users = {
    'john': {
        'age' : '25 years',
        'course' : 'computer science'
    },

    'mary': {
        'age' : '19 years',
        'course' : 'mathematics'
    }
}

books = {
    "python": {
        "author": "John Smith",
        "price": 5000
    },

    "cybersecurity": {
        "author": "Mike Ross",
        "price": 7000
    }
}

students = [
    {
        "name": "john",
        "age": 25,
        "course": "computer science"
    },

    {
        "name": "mary",
        "age": 19,
        "course": "mathematics"
    }
]

while True:
    try:
        name = input('Enter your name here:\n ').strip().lower()
        age = int(input('Enter your age here:\n '))
    except ValueError:
        print('Please enter a valid age!')
        continue

    course = input('Enter your course here:\n ').strip().lower()

    if name in users:
        print('User already exists!')

    else:
            users[name] = {
                'age' : f"{age} years",
                'course' : course
            }

    print('User added successfully!')

    students.append({
        "name": name,
        "age": age,
        "course": course
    })
    
    for student in students:
        print(f"{student['name'].capitalize()} - {student['course'].title()}")

    choice = input('Enter book name: \n').strip().lower()
    if choice in books:
        print(f"Author: {books[choice]['author']}")
        print(f"Price: {books[choice]['price']}")

    else:
        print('Book not found!')

    search = input('Search for a student: \n').strip().lower()

    if search in users:
        print(f"Name: {search.capitalize()}")
        print(f"Age: {users[search]['age']}")
        print(f"Course: {users[search]['course']}")
    
    else:
        print('Student not found!')

    search = input('Search for a student: \n').strip().lower()
    for student in students:
        if search == student['name']:
            print(f"Name: {student['name'].capitalize()}")
            print(f"Age: {student['age']} years")
            print(f"Course: {student['course']}")
            break
    else:
        print('Student not found!')

    
