
from allstudent_module import users, students
def add_student():
    while True:
        try:
            name = input('Enter your name here:\n ').strip().lower()
            age = int(input('Enter your age here:\n '))
        except ValueError:
            print('Please enter a valid INPUT!')
            continue

        course = input('Enter your course here:\n ').strip().lower()

        if name in users:
            print('User already exists!')

        else:
                users[name] = {
                    'age' : f"{age} years",
                    'course' : course
                }    

        students.append({
            "name": name,
            "age": age,
            "course": course
        })
        
        print('User added successfully!')
        break    