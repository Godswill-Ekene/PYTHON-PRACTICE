
calculations = []

def option():
    print("1. Calculate")
    print("2. Calculation History")
    print("3. Exit")
    return input("Choose an option (1, 2, 3): ")

def calc_sum(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    
    elif operation == "-":
        return num1 - num2
    
    elif operation == "*":
        return num1 * num2
    
    elif operation == "/":
        if num1 == 0 and num2 == 0:
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
            result = calc_sum(num1, num2, operation)
            timestamp = datetime.now().strftime("%Y-%m-%d | %H:%M:%S")
            calculations.append(f"{timestamp} - Result : {result}")
            print(f"Result = {result}")

        calc_more = input("Continue? (Yes/No): ").strip().lower()
        if calc_more == "no":
            print("Calculator closed.")
            break
        elif calc_more == "yes":
            continue
        else:
            return main()

def main():
        user_option = option()
        if user_option == "1":
            result = calculator()
            if result:
                print(result)

        elif user_option == "2":
            result = calculations_history()
            if result:
                print(result)

        elif user_option == "3":
            print("Exiting the program.")

        else:
            print("Invalid option. Please choose 1, 2, or 3.")

main()
#history = .append() results each

