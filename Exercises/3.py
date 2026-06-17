#This program defines a Student class with an initializer and an introduce method. 
#It then creates an instance of the Student class and calls the introduce method 
# to display the student's information.
class Student:
    
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"My name is {self.name}")
        print(f"I am {self.age} years old")
        print(f"I am studying {self.course}")

student = Student(
    "Ekene",
    12,
    "Cybersecurity"
)

student.introduce()