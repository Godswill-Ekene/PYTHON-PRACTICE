

def analyze_number(number):
    if number > 100:
        return "Too large"
    elif number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"
    

def run_num_checker():

    attempts = 3
    while attempts > 0:
        try:
            number = int(input("Enter a number:\n  "))

        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            attempts -= 1
            print(f"Attempts left: {attempts} ")
            continue

        result = analyze_number(number)
        print(result)

        if result == "Positive":
            print("Good, keep going ")

        attempts -= 1
        print(f"Attempts left: {attempts} ")

        if attempts == 1:
            print("Suspicious activity detected")

    print("Account locked! ")


run_num_checker()
