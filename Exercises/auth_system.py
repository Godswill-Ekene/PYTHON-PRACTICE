
# CORRECT VERSION

def check_password():   
   
        password = input('Enter password:\n  ')

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

result = check_password()
if result:
    print(result)

elif result == 'Strong':
    print('Access granted')

else:
    print('Access denied')

        