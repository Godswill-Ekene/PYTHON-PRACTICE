

def check_password(password):

    if len(password) < 8:
        return 'Weak'
    
    elif password.isdigit():
        return 'Add letters'
    
    elif password.isalpha():
        return 'Add numbers'

    elif any(c in "@#$!" for c in password):
        return 'Strong'
    
    else:
        return 'Strong'


password = input('Enter password:\n  ')

result = check_password(password)
print(result)

if result == 'Strong':
    print('Access granted')

else:
    print('Access denied')


# CORRECT VERSION


def check_password(password):

    has_letter = any(c.isalpha() for c in password)
    has_number = any(c.isdigit() for c in password)
    has_special = any(c in "@#$!" for c in password)

    if len(password) < 8:
        return "Weak"
    
    elif not has_letter:
        return "Add letters"
    
    elif not has_number:
        return "Add numbers"
    
    elif not has_special:
        return "Add special character"
    
    else:
        return "Strong"
   