student = (
    "Ekene",
    21,
    "Cybersecurity"
)

name, age, course = student

print(name)
print(age)
print(course)
print(student)

users = {
    "john",
    "mary",
    "john",
    "ekene",
    "mary"
}

users.add("admin")
name = input("Enter your username: ").strip().lower()
if name in users:
    print("User found")
else:
    print("User not found")
print(users)
