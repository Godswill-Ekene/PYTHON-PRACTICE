def double_number(x):  # passing a variable into a function
    return x * 2       # return is used to tell the function what to execute when you call it


num = int(input("Enter number: "))   # input from the user
print(double_number(num))            # displaying the content of the function


def check_even(x):              # name the function and pass the key variables
            
    if x % 2 == 0:              # the condition for execution
        return "Even"           # what happens when the function executes
    else: 
        return "odd"            
    
num = int(input("Enter a number:\n  "))
print(check_even(num))


def is_correct_password(password):
    if password == "1234" :
        return True
    else:
        return False
    
password = int(input("Enter password:\n  "))
if is_correct_password :
    print("Correct")
else:
    print("Wrong")


def reduce_attempts(attempts):
    return attempts - 1

attempts = 3

print(f"attempts left: {reduce_attempts(attempts)}")

