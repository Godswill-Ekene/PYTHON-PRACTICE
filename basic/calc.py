
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

        num1 = float(input("Enter number:\n "))
        num2 = float(input("Enter number:\n "))
        operation = input("Choose operation(+,-,*,%,):\n ")


        result = calc_sum(num1, num2, operation)
        print(f"Result = {result}")

        calc_more = input("Continue? (Yes/No): ").lower()
        if calc_more == "No":
           print("Calculator closed.")
           break

    
calculator()

#history = .append() results each

