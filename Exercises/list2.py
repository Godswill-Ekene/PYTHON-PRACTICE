

text = []
name = input("Enter name:\n ")
text.append(name)

if name not in text:
    print("user not found")

else:
    for user in text:
        print(user)
        