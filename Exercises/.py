student = {
    "name": "ekene",
    "age": 21,
    "course": "cybersecurity"
}

for key, value in student.items():
    print(key, "=", value)
#output is name = ekene, age = 21, course = cybersecurity
for key in student:
    print(key)
#output is name, age, course
for value in student.values():
    print(value)
#output is ekene, 21, cybersecurity
for key, value in student.items():
    print(key, value)
#output is name ekene, age 21, course cybersecurity
