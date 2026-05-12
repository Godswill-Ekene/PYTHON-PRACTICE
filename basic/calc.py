
def calc_sum(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    
    elif operation == "-":
        return num1 - num2
    
    elif operation == "*":
        return num1 * num2
    
    elif operation == "/":
        if num1 or num2 == 0:
            return "0 is not divisible"
        return num1 / num2
    
    else:
        return "Invalid operation"
    

def calculator():

    while True:

        try: #if user enters a non-numeric value, it will raise a ValueError and prompt the user to enter a valid number. The program will continue to run until the user chooses to exit by entering "No" when prompted to continue.
            num1 = float(input("Enter number:\n "))
            num2 = float(input("Enter number:\n "))
            operation = input("Choose operation(+,-,*,%,):\n ")

        except ValueError:
            print("Invalid input. Please enter a number.")  
            
        else:
            result = calc_sum(num1, num2, operation)
            print(f"Result = {result}")

            calc_more = input("Continue? (Yes/No): ").lower()
            if calc_more == "No":
                print("Calculator closed.")
                break

    
calculator()

#history = .append() results each

