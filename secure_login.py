
# secure_login.py
# 🎯 Task:
# User has 3 attempts
# Correct password → access granted
# Wrong → reduce attempts
# If attempts finish → lock account
# 🔥 Bonus Challenge

# Upgrade it:

# 👉 Add username check (like before)
# 👉 Only allow attempts if username is correct

attempts = 3

print('Login now..')

while attempts > 0:
    username = input('Enter username:\n  ')
    password = input('Enter password:\n  ')

    if username == 'admin': 
        if password == '1234': 
            print('Access granted')
            break
        else:
            print('Wrong password')
    else:
        print('Invalid login')

    attempts -= 1
    print(f'Attempts left: {attempts}' )

    if attempts == 1:
        print('Last attempt remaining')

if attempts == 0:
    print('Account locked!')
