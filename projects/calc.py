
calculations = []

def option():
    print("1. Calculate")
    print("2. Calculation History")
    print("3. Exit")
    return input("Choose an option (1, 2, 3): ")

def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    
    elif operation == "-":
        return num1 - num2
    
    elif operation == "*":
        return num1 * num2
    
    elif operation == "/":
        if num2 == 0:
            return "0 is not divisible"
        return num1 / num2
    
    else:
        return "Invalid operation"
    
def calculations_history():
    if len(calculations) == 0:
        return "No calculations yet."
    else:
        for calculation in calculations:
            print(calculation)
    return

from datetime import datetime
def calculator():

    while True:

        try: #if user enters a non-numeric value, it will raise a ValueError and prompt the user to enter a valid number. The program will continue to run until the user chooses to exit by entering "No" when prompted to continue.
            num1 = float(input("Enter number:\n "))
            num2 = float(input("Enter number:\n "))
            operation = input("Choose operation(+,-,*,/):\n ")

        except ValueError:
            print("Invalid input. Please enter a number.")  
            continue
            
        else:
            result = calculate(num1, num2, operation)
            timestamp = datetime.now().strftime("%Y-%m-%d | %H:%M:%S")
            calculations.append(f"{timestamp} | {num1} {operation} {num2} = {result}")
            print(f"Result = {result}")

        calc_more = input("Continue? (Yes/No): ").strip().lower()
        if calc_more == "no":
            print("Calculator closed.")
            break
        elif calc_more == "yes":
            continue
        else:
            break

def main():
    while True:
        user_option = option()

        if user_option == "1":
            calculator()

        elif user_option == "2":
            calculations_history()

        elif user_option == "3":
            print("Exiting program.")
            break

        else:
            print("Invalid option.")

main()
#history = .append() results each

