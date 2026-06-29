
users = ["admin", "user1", "ekene"]

name = input("Enter name:\n ")

if name in users:
    print("user found")

else:
    print("User not found")

           #OR

users = "admin, user1, ekene" 
text = users.split(",")

name = input("Enter name:\n ")


if name not in text:
    print("user not found")

else:
    for user in text:
        print(user)

# .upper()-make upper case, 
# .lower()-make lowercase, 
# .strip()-remove spaces, 
# .replace()-change characters, 
# .startswith()-check beginning, 
# .endswith()-check ending, 
# .isdigit()-numbers only, 
# .isalpha()-letters only, 
# .isalnum()-letters + numbers