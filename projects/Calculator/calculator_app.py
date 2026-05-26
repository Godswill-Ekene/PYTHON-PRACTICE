
calculations = []
memory = 0

def option():
    print("1. Calculate")
    print("2. Calculation History")
    print("3. Memory")
    print("4. Exit")
    return input("Choose an option (1, 2, 3, 4): ")
    
def calculations_history():
    if len(calculations) == 0:
        return "No calculations yet."
    else:
        for calculation in calculations:
            print(calculation)
    return

from datetime import datetime
from op_calc import calculate
def calculator():
    global memory
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

            # Memory operations: M+ adds last numeric result to memory,
            # MR displays memory, MC clears memory.
            mem_cmd = input("Memory? (M+ to add, MR to recall, MC to clear, Enter to skip): ").strip().upper()
            if mem_cmd == "M+":
                if isinstance(result, (int, float)):
                    memory += result
                    print(f"Added to memory. Memory = {memory}")
                else:
                    print("Cannot add non-numeric result to memory.")
            elif mem_cmd == "MR":
                print(f"Memory = {memory}")
            elif mem_cmd == "MC":
                memory = 0
                print("Memory cleared.")

        calc_more = input("Continue? (Yes/No): ").strip().lower()
        if calc_more == "no":
            print("Calculator closed.")
            break
        elif calc_more == "yes":
            continue
        else:
            break

def main():
    global memory
    while True:
        user_option = option()

        if user_option == "1":
            calculator()

        elif user_option == "2":
            calculations_history()

        elif user_option == "3":
            if memory == 0:
                print("No value stored in memory.")
            else:
                print(f"Memory = {memory}")
            clear = input("Type MC to clear memory / Enter to return: ").strip().upper()
            if clear == "MC":
                memory = 0
                print("Memory cleared.")

        elif user_option == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid option.")

main()
#history = .append() results each

