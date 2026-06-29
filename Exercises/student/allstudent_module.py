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

def show_students():
    for student in students:
        print(f"{student['name'].capitalize()} - {student['course'].title()}")