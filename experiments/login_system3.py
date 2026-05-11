# login_system.py
# 🎯 Task:

# Build a simple login system:
# 1. Ask for: username, password
# 2. Check: Username: admin ,Password: 1234
# ✅ Output:
#  If correct → "Login successful ✅"
#  Else → "Access denied ❌"
#  step up the game... with this
# If username is correct but password is wrong:
# "Wrong password"
# 👉 If username is wrong:
# "User not found"

print('Login..')

username = input('Enter username:\n  ')

password = input('Enter password:\n  ')

colour = input('What is your favourite colour?\n  ')

if username == 'admin' :
    if password == '1234' :
        if colour == 'red' :
            print('Access granted')
        else:
            print('Wrong colour')
    else:
        print('Not found')
else:
    print('User not found')
